# Platform-Capability Research — connector / MCP / agent-platform I/O knowledge bank

Condensed, primary-sourced domain notes for auditing an agent platform's input/output
foundation (connectors, tools, channels, MCP). Reuse these across capability-audit runs.
Counts and GA/preview status are **date-sensitive** — re-verify against the dated primary
page before each report (see the always-on recency rule in `verification-and-recency.md`).

## The 3 consumption surfaces (how a primitive gets leveraged)

A platform primitive (a connector, a channel) is consumed at **three altitudes**. The same
primitive looks different at each, so "good" means something different per surface:

| Surface | Who consumes | What "good" requires | Gap test |
|---|---|---|---|
| **1. Build-direct on primitives** | Enterprise builders + partners/SIs | Breadth + good authoring UX (they touch it) | A present-but-painful capability **is** a gap |
| **2. Build-from-templates** | Enterprise builders | Primitive **pre-wired** into a template, auth only | "Available via SDK but not templated" = a real gap |
| **3. Buy a ready-made vertical agent** | The **vendor's own first-party builders** (primitive is invisible to the customer) | Vendor can wire it internally | *Which* agents to build is a **vertical-research** question, NOT a capability one |

Key framing: it's **one primitive set seen at three altitudes (SDK / template / embedded)**,
not three capability sets. Audit dimension that falls out → **"exposure altitude"**: do we
expose each capability at all three surfaces, or only some? Partners/SIs behave like Surface 1
(consume primitives directly) — fold them in there, don't spin up a 4th lane.

Input vs output asymmetry: the altitude lens is **sharp for input** (connectors: full catalog
vs curated vs invisible) but **flatter for output** (even a bought agent still reaches the user
on Teams/WeCom — channel reach stays visible at every altitude).

## Deliverable shape for a capability audit — CONCRETE per-cell data, NOT a mark matrix

The generic Compare lens reaches for a ✅/partial/❌ matrix. For a **per-platform capability
audit**, that is the wrong shape and a user (Ken) rejected it outright — "you can't just mark
yes/no/partial, it's useless totally." Two hard rules for this sub-type:

1. **Each cell is a concrete capability statement + mechanism, never a mark.** Write what the
   platform actually provides and how — e.g. IN-5 Memory = "AgentCore Memory: short-term (session)
   + long-term (namespace-scoped)", not "●". A reader must learn the *substance* from the cell.
   Marks (●◐○ / ✅partial❌) carry zero information here; they read back as filler.
2. **Drop the GA/preview tag from every cell** unless the user asks for it. Ken found per-cell
   maturity tags to be clutter in a capability audit (note: this is the OPPOSITE of a live-product
   *gap* run, where GA-vs-preview is mandatory — so the recency discipline stays ON during research;
   you just don't surface the tag in every audit cell). Keep one ⚠️ flag for a load-bearing
   exception (e.g. "this builder is being wound down Nov 30").

**Presentation when 9–10 dimensions × 15 rows won't fit one readable table:** lay it out as a
**per-provider list** — one short block per provider, each dimension a labeled line — instead of a
giant matrix. Same fixed dimension order for every provider so they're still comparable. The
provider name carries the brand; the lines carry the concrete capability. This is the format Ken
ratified after rejecting the matrix.

**Column tuning is the user's call — expect them to drop/rename dimensions and swap framing.**
In one run Ken cut IN-7 Ambient context entirely, replaced OUT-2 "Actions & effects" with a
focused **Compute Use** dimension (is computer/GUI use supported + which: browser/desktop/code),
and tightened each remaining dimension to one specific question (e.g. IN-3 → "curated list? local
vs remote"; IN-6 → "supported + trigger formats"). Lock the tuned column set with the user BEFORE
filling cells, the same as the standard rows+columns checkpoint.



## Connector anatomy (the unit being audited)

A connector is a **proxy/wrapper around an API** (Microsoft's own words). Four parts:

| Part | Meaning | I/O side |
|---|---|---|
| **Auth** | How it logs in (OAuth, API key) | — |
| **Triggers** | Events that start the agent ("when a record is created") | **Input (2.1)** |
| **Actions** | Things the agent does ("update record", "send message") = **tool calls** | Actions span input/output; writes lean **output (2.2)** |
| **Schema** | Fields each action/trigger reads/writes | — |

So a connector is a **source of tools** (its action half) + an event source (trigger half).
"Tool" is the bigger circle — also code interpreter, web search, local functions. A **read**
tool fetches context (input-flavored); a **write** tool acts (output-flavored). Tools/connectors
are a **shared substrate under BOTH 2.1 and 2.2**, not a 2.1-only topic.

## Connector vs MCP — content vs packaging (do not conflate)

- **Connector = the CONTENT** — the actual integration logic (auth to Salesforce, its fields, ops).
- **MCP (Model Context Protocol) = a PACKAGING + transport STANDARD** — vendor-neutral way to
  expose tools/resources/prompts so any MCP client can discover + call them.

Same connector capability can be exposed in several **formats** — match the format to the consumer,
not to fashion:

| Format | Best for |
|---|---|
| Native SDK / function tool | In-process, lowest latency, hot path |
| MCP server | Reusable, shareable, cross-vendor third-party tools (interop) |
| OpenAPI import | The huge set of SaaS that already publish an OpenAPI spec |
| CLI | Dev/coding agents — shell-native, composable (`gh`, `kubectl`), local |
| Raw REST | One-off / fully custom |

**"Should most be MCP?" → No.** MCP is the **interop edge**, not the whole story. Raw MCP is thin
on enterprise governance (who-may-call, DLP, audit, multi-tenant auth) and the servers must be
hosted somewhere. Right move for a vendor with a managed catalog (Microsoft): **put an MCP-compatible
facade ON TOP of the existing governed connector catalog** — keep auth/hosting/DLP, speak MCP at the
edge. CLIs are a real slice (dev agents), not the backbone.

## What COUNTS as a connector (strict) — the IN-2 audit test

A **connector** is a **pre-built, packaged integration to a NAMED third-party business app**
(Salesforce, SAP, Slack, ServiceNow…) sitting in a **catalog** that a connector provider builds
and hosts — an iPaaS (Zapier, Workato, Boomi) OR a platform that owns its own catalog (Microsoft
Power Platform, Google Integration Connectors). This is the definition from the Stream-A provider
list (the `A1 — Connector providers` table); honor it exactly when auditing IN-2.

**A connector is NOT** (the trap — easy to over-broaden, observed and corrected in a real run):
- a **generic plugin / tool** (web search, code interpreter, image-gen, a knowledge-base node);
- an **MCP server** (that's packaging/transport — audit it under the MCP dimension, not connectors);
- a **custom API / Lambda / OpenAPI wrap** you build yourself (that's tool-wiring, not a catalog).

Counting any of those three as "connectors" inflates the cell and makes a plugin-store platform
look like a connector-provider. The IN-2 test per platform is narrow: **(a)** can you pick pre-built
*named-app* connectors when building, **(b)** which catalog do they come from (own / third-party
iPaaS / none → bring-your-own-API), **(c)** roughly how many.

**Per-platform classification that falls out (verified 2026-06-17 — re-verify counts):**
- **Real owned named-app catalogs:** Microsoft (~1,400+ Power Platform/Logic Apps), Google (~90+
  Integration Connectors), Salesforce (MuleSoft Anypoint, hundreds), ServiceNow (~200 Integration
  Hub Spokes), **Tencent ADP** ("Connectors + Tools" → third-party SaaS + enterprise + Tencent
  ecosystem; the clearest China connector-provider posture).
- **Narrow catalogs:** **AWS Bedrock AgentCore** — *correction to the "pure BYO-tools" framing in
  the market map below*: Gateway DOES ship a **small pre-built 1-click set** (Salesforce, Slack,
  Jira, Asana, Zendesk + AWS-Marketplace SaaS targets); beyond those you wrap your own APIs/Lambda/
  OpenAPI/Smithy. **OpenAI** — Connector Registry ≈ 40+ ChatGPT "apps", largely read-only retrieval.
- **No named-app catalog — they reach tools via plugins + MCP instead:** Alibaba Bailian (data-source
  connectors + plugin store), ByteDance Ark, Baidu AppBuilder (~37 Baidu-built components), Huawei
  AgentArts (300+ tools/assets, not clearly named-SaaS), Coze, Yuanqi.
- **Special — Anthropic:** its "connectors" *ARE* MCP servers (the Connectors Directory is ~439
  Anthropic-verified remote MCP servers, not an iPaaS catalog). File it as "connectors = verified MCP."

> Honest correction worth remembering: a user's first instinct ("only MS/Google/Salesforce own a
> catalog") was actually *close* — add ServiceNow + Tencent for full catalogs, AWS/OpenAI as narrow
> ones. The first audit pass *over-broadened* the other way by counting every plugin/MCP store as a
> connector catalog. Strict definition first, then classify.

## Agent-platform market map — "two doors, two camps" (verified ~2025)

Every platform offers tools via **two doors**: a pre-built connector catalog + an MCP path. The
real differentiator is whether a **deep, governed catalog** sits underneath the MCP layer.

| Camp | Players | Shape |
|---|---|---|
| **Catalog + MCP facade** | **Microsoft** (Power Platform 1500+ connectors; MCP GA in Copilot Studio), **Google** (Vertex/ADK 100+ Integration Connectors + MCP Toolbox), **Salesforce** (MuleSoft connectors; Agentforce 3 native MCP client) | Deep governed catalog = the moat; MCP = interop edge. Serves **Surface 2 (templates)** well. |
| **MCP-native, BYO-tools** | **OpenAI** (Agents SDK / Responses API take MCP servers), **Anthropic** (Connectors Directory IS remote MCP servers; authored MCP), **AWS** (Bedrock AgentCore Gateway turns your APIs/Lambdas into MCP tools) | Lean runtime + MCP; you/ecosystem supply integrations. Serves **Surface 1 (build-direct devs)**. |

> ⚠️ **Refinement (2026-06-17 run):** the "MCP-native, BYO-tools" camp is not pure BYO. **AWS**
> Gateway also ships a small pre-built 1-click connector set (Salesforce, Slack, Jira, Asana,
> Zendesk); **OpenAI** runs a ~40+ read-only connector registry. So even the lean-runtime camp has
> a *narrow* owned catalog — see the strict per-platform classification under "What COUNTS as a
> connector" above. The camp split still holds as a SHAPE (deep governed catalog vs lean+MCP), but
> don't state AWS/OpenAI as having zero pre-built connectors.

**Two findings:**
1. **MCP has won as the interop standard** — universally adopted across all six players in ~12 months.
2. **The differentiator is NOT MCP — it's the governed catalog underneath it.** Only MS/Google/
   Salesforce own one; MS's is largest by a wide margin (1500+ vs Google's 100+). That catalog's
   built-in auth + DLP is exactly the governance raw MCP lacks. **Audit this as a hypothesis to
   test, not a foregone moat** — verify the counts + what governance actually travels.

## MCP gateway market — classify by HOST-vs-ROUTE, don't trust the label (verified 2026-06)

The names that appear under "MCP gateway" lists (Lunar.dev/MCPX, MCP Manager, Obot, Arcade,
Composio, Klavis, Pipedream) are **not one uniform product type**, and "MCP gateway" is a **loose
marketing label, not a settled category** (Gartner names an "AI Gateways" category, Oct 2025, but
NOT a distinct "MCP Gateways" one yet). Auditing them needs two independent axes, both primary-
verifiable from the vendor's own page:

- **What a gateway fundamentally IS = a router/proxy.** It "sits between the agent and the MCP
  servers; the agent talks only to the gateway, and every tool call routes through it" where
  identity/RBAC/audit/DLP get applied (Speakeasy's definition). This exists because the MCP protocol
  gives ONLY tool discovery + calling and says governance is explicitly out of scope — so a separate
  layer must add it. **Routing is the defining job.**
- **HOSTING the server (running the process) is a SEPARATE, optional capability.** Host and route
  are independent axes, not a spectrum. Three patterns: **route-only** (aggregates/governs servers
  that run elsewhere — e.g. Lunar MCPX "aggregates other MCP servers rather than hosting them"),
  **host-only** (serves servers but isn't primarily a routing-governance proxy), **both**.
- **Second axis = self-host vs managed (SaaS).** Most offer both; this is the data-residency
  question for an enterprise (does the proxy run in my boundary or the vendor's).

**Verified classification of the 7 (2026-06, each from its own site):** Lunar.dev/MCPX = pure
gateway, **routes only**, self-host(OSS)+managed. MCP Manager = pure gateway, **routes only**,
managed(+self-host). Obot = gateway+host, **both**, self-host(MIT)+managed. Arcade = runtime+gateway,
**both**, managed+self-host. Composio = tool platform+gateway, **both** (ships a reverse-proxy MCP
Gateway), managed+self-host/BYO-cloud. Klavis = **hosting/infra** (not a routing gateway),
managed+self-host(OSS). Pipedream = **iPaaS exposing MCP** (not a gateway at all), managed.
So only **2 of 7 are pure routing gateways**; 3 do both; 1 is hosting infra; 1 is an iPaaS.

> **The honest-presentation move (Ken ratified):** when a "market" list mixes true gateways with
> hosting/iPaaS products, do NOT force them all under one label or silently drop the misfits. Add a
> **Type column** + a **Hosts-or-routes column**, and state plainly in the read-out which ones are
> NOT gateways in the strict sense (Klavis, Pipedream here). Keep them in the table — they show up in
> every market list — but labeled honestly. A descriptive **takeaway** that ties the section together
> is welcome, but in a Stream-A inventory it stays DESCRIPTIVE ("the label is loose; two axes organize
> the space") — never prescriptive about what to build.

## "Top-N connectors/primitives" is a DEMAND-INTERSECTION, never a catalog rank

When the deliverable is "the top N connectors" and the supply sources are huge catalogs
(Zapier 9,000+, Make 3,000+, Power Automate 1,400+), do NOT gather the full lists and rank them —
it's infeasible AND it answers the wrong question (a catalog dump says what EXISTS, not what
MATTERS). The Top-N is the **intersection of widely-supplied AND widely-used**, frequency-ranked
across independent DEMAND signals:

1. **Vendor-published "most-used / most-popular" lists (the cheap 80%) — but only SOME catalogs
   actually publish one; verify per-vendor, never assume.** Overlay the lists that genuinely exist and
   count how many independent lists each app recurs on (an app on 3–4+ vendor lists is a Top-N lock).
   Three rules learned the hard way (2026-06):
   - **Keep each vendor's list SEPARATE in the provider-stream findings; do NOT merge into one
     cross-vendor rank there.** Merging is the deferred synthesis step, not provider-collection. The
     user (Ken) explicitly asked for "each top list for the 3 providers, listed separately."
   - **Grade each list by how it was sourced, and never fabricate a rank a vendor doesn't publish.**
     Only **Zapier** ("Most Popular" default sort on zapier.com/apps) and **n8n** (surfaced
     integrations) publish a genuine popularity-ORDERED list → grade [P]. **Power Automate does NOT** —
     its connector reference is ALPHABETICAL only; the "most-used" Microsoft-365 core set (Outlook,
     SharePoint, Teams…) is a secondary signal → grade [S] and label it "not a vendor ranking."
     Secondary sources even disagree on Power Automate's tail (some cite Slack/Jira/Power BI), which is
     itself proof no authoritative ranking exists.
   - **Make / Pipedream / Workato don't surface a clean ranked list** (Make's apps page is JavaScript-
     rendered and won't fetch) → exclude them and note the gap, rather than invent a ranking.
   - **Audit ALL providers in the locked list, not just the obvious few, and record the misses as a
     table.** When the A1.2 deliverable is "each provider's own top list if it publishes one," check
     every one of the locked providers — don't stop at the 2–3 that clearly have lists. Across the
     full 14-provider iPaaS/platform set (2026-06), **only Zapier + n8n publish a genuine vendor-ranked
     list**; the other 12 sort alphabetically or by category, and EVERY "most popular X connectors"
     answer for them (SnapLogic→Salesforce/Workday, Tray→Salesforce/Slack, Boomi→NetSuite, IBM→
     Salesforce/AWS, MuleSoft→Salesforce/SAP, etc.) traces to a THIRD-PARTY BLOG, not the vendor's own
     page — grade [S], never pass off as a vendor ranking. Borderline to reject: ServiceNow has
     "Integration Hub Usage Dashboards" but that's a CUSTOMER's own usage, not a published global rank.
     Present the audit as: the real lists in full (graded [P]) + the secondary exception (Power
     Automate, [S]) + a one-row-per-remaining-provider table ("ranked list? No / what exists instead").
     Ken wants the COMPLETE audit shown (every provider checked), not just the providers that passed.
   With only 2–3 real lists the max recurrence is low (in the run nothing hit 3×), so Method-1 alone
   yields the stable DEMAND CORE (Google Workspace, Microsoft 365, Slack, Salesforce, Notion, Airtable,
   the AI models), NOT a clean ranked 30 — the platform-exposure votes from the consumer stream break
   the ties. This is a frequency-rank across DEMAND, not a rank of raw catalogs.
2. **The MCP category-demand signal** (the per-category connector counts from `/mcp/attributes`
   above) — an independent, agent-native demand vote to cross-check #1.
3. **Platform-exposure votes** — which connectors each agent platform ships pre-built. In a
   two-stream program (provider research + per-platform consumer audit) this half comes from the
   CONSUMER-audit stream, so don't try to finish Top-N inside the provider stream. Top-N is a
   DEFERRED synthesis step = supply/demand (provider) + who-exposes (consumer).

So provider-side research only needs to COLLECT the demand lists (the vendor popularity lists +
the MCP category counts); the actual Top-N frequency-rank waits until the consumer-audit exposure
data lands. Never gather or rank a full catalog.

- Copilot Studio — connectors as tools: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-connectors
- Copilot Studio — add tools: https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent
- Salesforce connector reference (actions/triggers/auth): https://learn.microsoft.com/en-us/connectors/salesforce
- Copilot Studio MCP GA: https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/model-context-protocol-mcp-is-now-generally-available-in-microsoft-copilot-studio
- Copilot Studio extend with MCP: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
- Anthropic MCP (origin): https://www.anthropic.com/news/model-context-protocol
- Anthropic remote-MCP connectors: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- Google Vertex multi-system agents (100+ connectors): https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai
- AWS Bedrock AgentCore Gateway: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development
- Salesforce Agentforce 3 native MCP client: https://www.salesforce.com/news/press-releases/2025/06/23/agentforce-3-announcement
- MuleSoft MCP connector: https://architect.salesforce.com/docs/architect/fundamentals/guide/mulesoft-architecting-agentic-enterprise

## MCP registry / Glama counts are JavaScript-rendered — hit the JSON API, not the page

The server-count numbers on MCP registry pages (official registry, Glama, Smithery, OpenTools)
are **client-side rendered**: a static fetch/extract (`tavily-extract`, curl, `r.jina.ai`) returns
the page chrome WITHOUT the number, so you either get nothing or scrape a stale blog figure. Two
registries DO expose the count in static HTML (mcp.so prints "...N MCP Servers collected"; PulseMCP
prints "Showing 1–42 of N servers") — copy those directly. For the rest, go to the JSON API:

- **Official MCP Registry** — `GET https://registry.modelcontextprotocol.io/v0/servers?limit=100`
  returns `{servers:[...], metadata:{nextCursor, count}}`. There is **no total-count field and no
  `/v0/stats`** (404); to size it you must paginate the cursor and tally. Do this inside
  `execute_code` with a wall-clock cap (`if time.time()-start > 70: break`) so it can't hang — you'll
  get a *floor* (e.g. "4,100+ and still paginating"), which is honest and enough. Note the registry
  allows duplicate server/version records, so the record count **overstates unique servers** — say so.
- **Glama** — public REST API `https://glama.ai/api/mcp/v1`, no auth, `GET /servers` lists all repos
  (cursor-paginated, leaner than the site: hosting/author/license yes, A–F grades NO). The per-category
  counts ARE recoverable — not from the filter sidebar (top ~30 only) but from the server-rendered
  **`glama.ai/mcp/attributes`** page, which lists every category with BOTH a server-count AND a
  hosted-connector-count, plus the other 5 attribute dimensions (Languages, Capabilities, Hosting,
  Environment, Author). That connector-count column is a cleaner enterprise-demand signal than the
  server count (Search 1,426 / Finance 914 / Research 806 / Open+Gov Data ~1,425 connectors).
  **Know exactly what "connector" counts before trusting it — it is NARROWER than "remote" (verified
  against Glama's own FAQ, 2026-06). Glama uses four NESTED terms:**
  (1) **server** = any MCP server (≈37k), mostly local run-it-yourself.
  (2) **remote-capable** (the Hosting attribute, ≈16k) = the server's CODE supports an HTTP transport
  (Streamable HTTP / SSE) so it *can* run remotely. This is a property of the code, NOT a live
  deployment — most are still just a GitHub repo with no public URL. The attribute is literally named
  remote-*capable* ("can", not "does").
  (3) **connector** (≈5.9k, the `/mcp/connectors` count) = a server that actually HAS a live listed
  remote URL you can point an agent at today (each card shows an endpoint + a "Connect" button) — the
  zero-install, plug-and-play slice. So **connector ⊊ remote-capable ⊊ server**, and 5.9k < 16k is
  exactly why: only ~⅓ of remote-capable servers have a live endpoint listed.
  (4) **Glama connector** = the managed subset where Glama itself hosts it + handles OAuth/credentials +
  per-tool access control. The directory ALSO lists connectors on third-party domains, so connector ≠
  Glama-hosted. Net: the per-category connector column = "servers in this category with a live remote
  endpoint" (a real ready-today demand signal); remote-capable is only "could go remote if deployed"
  (softer). Do NOT treat the two as interchangeable when reading the demand signal. The A–F
  grades live only in the per-server page HTML blob (`\"maintenance\",\"<A-F>\",\"quality\",\"<A-F>\"`).
  **Grade COVERAGE is the headline, not the distribution:** only ~18–24% of randomly-sampled servers
  carry a Quality/Maintenance grade (the rest read "quality – not tested"), so the A–F numbers describe
  a vetted MINORITY, not the population — report coverage first. Author: only ~6.6% (2,449/37k) are
  "official" first-party; ~93% community. Full extraction ladder (REST → aggregate page → browser DOM
  → per-detail blob) + the bounded-concurrent census pattern + delegation-reliability rules →
  `references/javascript-rendered-data-extraction.md`.

Verified snapshot (2026-06-17, primary-sourced — re-verify, these move monthly): Glama **36,238**
servers / **85** categories (A–F grades on License·Quality·Maintenance still live); mcp.so **22,273**;
PulseMCP **18,572**; official registry **thousands** (4,100+ live floor); Docker MCP Catalog **270+**;
Anthropic Connectors Directory **~439** (secondary). Connector catalogs same day: Zapier 9,000+, Make
**3,000+**, Workato 1,200+, Boomi/Celigo/SnapLogic **1,000+**, Tray **700+**, n8n 400+, Google **90+**.
Microsoft/ServiceNow/OpenAI **stopped publishing a headline connector total** — "1,400+" for Microsoft
is blog-only; do not state it as vendor-confirmed. OpenAI renamed ChatGPT "connectors" → "apps"
(2025-12-17). MCP-gateway market (all primary-confirmed): Lunar.dev/MCPX, MCP Manager, Obot, Arcade,
Composio, Klavis, Pipedream (joined Workday Nov 2025). Gartner tracks "AI Gateways" (Oct 2025); a named
"MCP Gateways" Gartner category is vendor-claimed only.

## Glossary
- **MCP** — Model Context Protocol (open standard for exposing tools/resources to agents).
- **DLP** — Data Loss Prevention (admin rules restricting data movement).
- **SI** — System Integrator (partner who builds + resells agents on a platform).
- **GA** — Generally Available (shipped; not preview).
