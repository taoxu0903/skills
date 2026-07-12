# Discovery lens — reliable search & fetch tooling

Practical notes on getting clean, citable candidate rows during the Discovery lens,
learned the hard way when the first attempt produced no usable data.

## Unseeded enumeration + body-mining + frequency-rank (the convergence mechanics)

The SKILL's anti-anchoring protocol is non-negotiable; this is the tactical "how" that
actually surfaced the tools a seeded run missed. Three mechanical rules:

1. **Pull `include_raw_content: true`.** The default `content` snippet is ~1–2 sentences and
   often just the title restated. The candidate names live deeper in listicle bodies. Request
   raw content and harvest from it:
   ```python
   body = {"query": q, "max_results": 7, "search_depth": "basic",
           "include_answer": True, "include_raw_content": True}
   ```
2. **Build queries from the CATEGORY MAP, zero vendor names.** One enumeration query per
   sub-category. Anchoring self-test: if a query string contains a product name, rewrite it.
   ```python
   queries = [
     "best SAST static analysis security tools 2026 list",
     "top software composition analysis SCA tools enterprise 2026",
     "best automated dependency update tools 2026",
     "best continuous code quality and technical debt tools 2026",
     "best secret scanning tools for repositories 2026",
     "application security posture management ASPM platforms comparison 2026",
     "automated code modernization and framework upgrade tools 2026",
   ]
   ```
3. **Frequency-rank product-like names across the whole corpus (convergence).** Concatenate
   every title + content + raw_content, extract candidate names, count recurrence. CamelCase
   and two-word Capitalized tokens catch most product names; keep a stopword set of generic
   capitalized terms ("Best", "Security", "Tools", language names) so they don't rank.
   ```python
   import re
   from collections import Counter
   text = "\n".join(all_titles_contents_and_raw)
   camel  = re.findall(r'\b[A-Z][a-z]+[A-Z][A-Za-z]+\b', text)        # SonarQube, OpenRewrite, JFrog
   twowd  = re.findall(r'\b[A-Z][a-z]+ (?:[A-Z][a-z]+|Duck|Climate)\b', text)  # Black Duck, Code Climate
   cnt = Counter(t for t in camel + twowd if t not in STOP)
   # recurrence >= 2 across independent listicles == real candidate; one-off == noise
   ranked = sorted([(k,v) for k,v in cnt.items() if v >= 2], key=lambda x: -x[1])
   ```
   This single step is the difference between discovery and confirmation. A real run this way
   surfaced Mend, Renovate, Semgrep, Black Duck, Codacy, GitGuardian, Cycode, Apiiro, and the
   whole Application Security Posture Management category — none of them seeded.

4. **Include any user-named tools by default.** The unseeded rule applies to your QUERIES, not
   to the user's input. If the user handed you product names, add them straight into the
   candidate set (after a quick scope check), then let the unseeded discovery above find more on
   top. The user's list is the floor, not the ceiling.
   ```python
   candidates = set(ranked_names) | set(user_provided_names)   # user names always included
   ```
   There is no fixed "old report" to check against — do not build the run around diffing a prior
   roster. If some reference list happens to exist, you may eyeball it as a sanity check, but it
   is optional, never a required step and never a seed.

> **Fire category queries directly from the main session via Tavily** (parallel entry points),
> not through delegate_task subagents. The subagent web_search no-op failure mode (below) plus
> the need to mine raw_content centrally make the direct Tavily-in-`execute_code` path both more
> reliable and easier to converge. Reserve subagents for the per-object Teardown step, where
> each child fills one fixed dimension row.

## Which retrieval skill to load (this Hermes setup)

There is no skill literally named `web-access` here. The working retrieval path is the
**Tavily skill family** — load `tavily-search` for the exact CLI usage. Two ways to call it,
both fine:
- **`tvly` CLI** (preferred for interactive): `export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env
  | xargs)` then `tvly search "query" --depth advanced --max-results 6 --include-answer advanced
  --json -o /tmp/out.json` and read the file. Write JSON to a file with `-o` (Unicode can break
  stdout). Chinese queries work as-is (no CJK splitting).
- **Direct API via Python `urllib`** inside `execute_code` (preferred for batch / programmatic
  mining) — the pattern documented below.
Related skills: `tavily-extract` (fetch full page content), `tavily-crawl-map`, `tavily-research`.

## Decision order for retrieval (most reliable first)

1. **Tavily Search API** — primary workhorse when a key is available (`TAVILY_API_KEY`,
   stored in `~/.hermes/.env`). POST `https://api.tavily.com/search` with
   `{"query": ..., "max_results": 5, "search_depth": "basic", "include_answer": true}`
   and header `Authorization: Bearer $TAVILY_API_KEY`.
   - Returns clean JSON: `results[].title / .url / .content` (a ready evidence snippet)
     plus a one-line `answer` summary per query. **No Chinese word-segmentation
     mangling, no bot wall, no rate-limit anomaly pages** — far steadier than scraping
     under batch load. Tavily free tier ≈ 1000 searches/month, ample for one Discovery run.
   - **Call it from Python `urllib.request`, NOT shell curl.** Inline-JSON shell escaping
     repeatedly broke (`unexpected EOF while looking for matching '"'`) even via a written
     `.sh` file, because bash re-evaluates the quoting. `urllib.request.Request(url,
     data=json.dumps(body).encode(), headers={...})` inside `execute_code` sidesteps the
     shell entirely and just works. This is the reliable batch pattern.
   - Verify one query first (confirm `results` is non-empty), then loop the full
     candidate list with a small `time.sleep(0.8)` between calls.
2. **curl the DuckDuckGo HTML endpoint** — fallback when no Tavily key.
   - `https://html.duckduckgo.com/html/?q=<urlencoded query>`
   - Send a desktop UA: `-A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"`.
   - Parse result anchors:
     `grep -oE 'result__a"[^>]*>[^<]+'` then strip the `uddg=` redirect wrapper.
   - Returns real titles + real destination URLs as plain text, no Chinese
     word-segmentation mangling. BUT under rapid batch load it serves a throttle page
     (body contains `anomaly`) and result blocks vanish — pace it, retry with backoff,
     and treat an `anomaly`/empty body as throttling, not "no results."
3. **execute_code pipeline** — wrap either of the above into search → parse → fetch-body →
   emit structured rows. Keeps raw pages out of the main context; only clean
   candidate rows return. Use the built-in `retry(fn)` helper around each fetch.
4. **browser tools** — fallback ONLY when neither API nor curl can reach a JS-gated page.
   Slower, occasional bot detection. Don't make it the default Discovery path.

## Fetching a KNOWN page when the extractor is down (the built-in tools share ONE backend)

The built-in `web_search` and `web_extract` BOTH route through Tavily in this setup, so a backend
hiccup (observed: HTTP 432 on every call) takes out both at once — and the Tavily skills
(`tavily-search` / `tavily-extract`) ride the same backend. Switching between them does NOT help;
they are one path. When you already HAVE the target URL (a doc / article / plain page, not a JS
app), bypass the extractor and fetch it yourself, then strip HTML → text inside `execute_code` so
raw markup never enters context:
```bash
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" --max-time 25 "$URL" \
  -o /tmp/page.html -w "HTTP %{http_code}, %{size_download} bytes\n"
```
```python
import re, html
raw  = open("/tmp/page.html", encoding="utf-8", errors="ignore").read()
m    = re.search(r'<main[^>]*>(.*?)</main>', raw, re.S)          # main content only
body = re.sub(r'<(script|style|nav|svg)[^>]*>.*?</\1>', '', m.group(1) if m else raw, flags=re.S)
text = re.sub(r'\n\s*\n+', '\n\n', html.unescape(re.sub(r'<[^>]+>', ' ', body)))
```
Useful follow-ons: grep the saved HTML for `href="..."` to discover the CURRENT doc slug when the
obvious URL is wrong/deprecated, and grep code blocks for exact commands. This is for FETCHING a
specific known page; to FIND new pages when search is down, use the DDG HTML fallback above. Treat
it as a fallback RECIPE, never as "Tavily/web_search is broken" — the backend recovers.

## Pitfalls observed

- **Subagent web_search can no-op.** A delegated Discovery subagent may return a
  summary containing literal tool-call markers (e.g. `%%%begin_tool_call%%%` /
  `%%%TOOLCALL%%%`) instead of real results — meaning the tool never actually fired.
  Symptom: the "summary" is the agent narrating a search rather than data with URLs.
  Before trusting subagent Discovery output, **sanity-check that rows carry real URLs**.
  If they don't, fall back to the curl pipeline above and run Discovery from the main
  session. Always confirm the local network is fine first (`curl -o /dev/null -w "%{http_code}"`
  against bing/baidu/duckduckgo) so you fix the *tool layer*, not chase a non-existent
  network problem.
- **Bing's rendered search page mis-segments Chinese queries** — a multi-keyword CN
  query like `多智能体 协作 数字员工 垂直行业` can match unrelated topics (e.g.
  教学方法/小组合作). Prefer DDG HTML, or quote exact product/vendor names.
- **DDG rate-limits rapid-fire queries** — three hits in the same second can return
  empty result blocks, and a sustained batch (20+ calls) trips a throttle page whose
  body contains `anomaly`. Space requests out / add jitter / wrap in `retry`. An empty
  block or `anomaly` body is throttling, not "no results for this term." If you have a
  Tavily key, prefer it for batch runs — it doesn't throttle this way.
- **Shell escaping breaks JSON POST bodies.** Sending an API call (e.g. Tavily) via
  `curl ... -d '{...}'` with CJK/quotes in the JSON repeatedly fails with
  `unexpected EOF while looking for matching '"'`, even when the command is written to a
  `.sh` file first — bash re-evaluates the quoting. Fix: skip the shell. Use Python
  `urllib.request` inside `execute_code` with `data=json.dumps(body).encode()`. Clean,
  deterministic, no escaping games.

## Sequencing: ratify the row set BEFORE spending evidence effort

Checkpoint 2+3 (the object set AND the comparison dimensions, presented together) fixes the
*rows* and *columns* first. Don't burn primary-source verification on candidates the user will
prune. Workflow that wastes the least effort:
1. Assemble the candidate list (threshold-filtered), marking each row's source confidence
   (e.g. ⚠️ = needs first-source check).
2. Hand it to the user — together with your recommended comparison dimensions — to prune/add
   tools and finalize the dimensions (checkpoint 2+3).
3. Only then run the verification pipeline to attach a primary source to each *surviving* row,
   collecting against the now-locked dimensions.
This honors the skill's "object list is an OUTPUT, ratified by the user" principle and avoids
verifying rows that get cut.
