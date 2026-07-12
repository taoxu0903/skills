# Extracting primary-source counts from JS-rendered catalog / registry sites

When a research target is a modern web app (registry, marketplace, connector catalog — Glama,
Smithery, mcp.so, a vendor's integrations directory), `tavily-extract` / `web_extract` / a plain
`curl` often return only the HTML **shell**: the real data (counts, grades, category facets) is
fetched client-side and never appears in the static markup. Do NOT report "JavaScript-rendered,
can't get it" and move on — climb this ladder. Each rung is more work; stop at the first that
yields the data.

## The extraction ladder (cheapest first)

1. **Public REST / JSON API.** Most catalog sites have one, often unauthenticated. Probe the
   obvious paths: `/api/.../servers`, `/api/v1/...`, a `*.json` endpoint, or whatever the docs
   mention. Glama: `https://glama.ai/api/mcp/v1/servers` — cursor-paginated (`?after=<endCursor>`,
   read `pageInfo.hasNextPage`), no auth. Official MCP registry:
   `https://registry.modelcontextprotocol.io/v0/servers?limit=100` — same cursor shape; paginate it
   yourself under a wall-clock cap to get a live floor count. The list record is often **leaner**
   than the website (Glama's API gives hosting/author/license but NOT the A–F grades). Read one
   record, list its keys, see what's missing before assuming the API is enough.
2. **The site's own AGGREGATE / index page.** Sites that hide per-item data in JS frequently
   server-render an OVERVIEW page with exactly the totals you need. Glama's `/mcp/attributes` page
   carries every category + its server-count AND connector-count, fully server-side rendered (the
   `/mcp/servers` sidebar only shows the top ~30 by count). Look for `/attributes`, `/categories`,
   `/stats`, `/browse`. This is usually the fastest path to a complete category census.
3. **Browser tool → read the rendered DOM.** When only the live DOM has it, load the page with
   `browser_navigate` and pull values via `browser_console` JS (`document.querySelectorAll(...)`).
   The filter sidebar / facet list is gold: it lists every attribute WITH its population count. The
   page `<title>` often carries the live total ("37,176 in the Glama Registry"). A urllib fetch of
   the same URL frequently returns a bare shell (no `<script>`/`__NEXT_DATA__`) — that's the signal
   to switch to the real browser, not to give up.
4. **Parse the embedded data blob in the per-detail page HTML.** Next.js / React-Server-Component
   apps inline their data as escaped JSON inside the page (in `self.__next_f.push([...])` chunks or
   a raw `\"key\",\"value\"` stream). Fetch the detail page server-side and regex the blob. Glama
   per-server grades live as
   `\"license\",<n>,\"maintenance\",\"<A-F>\",\"quality\",\"<A-F>\",\"security\",...` — invisible to
   the API, present in the page HTML. Match with
   `re.compile(r'\\"maintenance\\",\\"([A-F])\\",\\"quality\\",\\"([A-F])\\"')`.

## Sampling a population census at scale (no bulk dump available)

If the data you need is only on per-item pages (e.g. grades) and there are tens of thousands of
items, you can't crawl them all, and a single delegated subagent WILL time out on the slow crawl.
Use a **bounded concurrent fetch from the MAIN session** inside `execute_code`:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
t0 = time.time()
# 1) harvest a random-ish ID pool FAST from the JSON API:
#    jump a random number of cursor pages to de-correlate from the alphabetical head, then collect slugs
# 2) fetch detail pages concurrently with a HARD wall-clock cap
with ThreadPoolExecutor(max_workers=12) as ex:
    futs = {ex.submit(fetch_one, item): item for item in pool[:400]}
    for f in as_completed(futs):
        if time.time() - t0 > 200:        # hard cap — never run to the tool limit
            break
        r = f.result()
        ...                               # tally into collections.Counter
```

~12 workers turns a 1–2 s/page sequential crawl (unworkable for 400 pages) into ~90 s. Always keep
a running tally so a mid-run break still yields a usable distribution; report the **exact N** you
reached, not a target you didn't hit.

## Coverage-before-distribution (a truth-contract pitfall)

Before reporting a distribution of per-item quality grades, **check what fraction of the population
is actually graded.** Registries publish grades only for a vetted MINORITY — on Glama only ~18–24%
of randomly-sampled servers carry a Quality/Maintenance grade; the rest read "quality – not tested."
A distribution computed over the graded subset is NOT a distribution over the population, and
reporting it as if it were silently overstates ecosystem maturity. Lead with the coverage number
("only ~1 in 5 servers is graded"), THEN the distribution within the graded set. For a "huge but
mostly unvetted" registry this coverage gap is usually the single most important finding.

## Delegation reliability for web-heavy census / teardown children

- **Wrap every network call in a per-call OS timeout** so one hung fetch can't burn the whole
  budget: `set -a && source ~/.hermes/.env && set +a && timeout 45 tvly search ... ; echo EXIT=$?`.
  On `EXIT=124` (timed out) move on after at most one retry. An uncapped child stuck on a single
  slow request returns NOTHING at 600 s — all its work discarded.
- **Split one heavy web task into independent parallel children.** A single subagent doing L1+L2+L3
  (or many objects at once) is the one that times out. The locked scope usually already states the
  sub-parts are independent ("different sources, different work, run in parallel") — honor that and
  dispatch one focused child per sub-part.
- **Two strikes → pull it into the main session.** If a web child times out TWICE even after the
  timeout-wrap and the split, stop delegating that piece. Do it yourself in the main session with
  direct API pagination + the bounded concurrent fetch above. Delegation is not always the right
  tool for slow-network census work, and the main session can run urllib with finer control.
