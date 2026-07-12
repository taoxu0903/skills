# Platform & Ecosystem Scoping (altitude-aware competitive research)

Load this when the research subject is an enterprise PLATFORM that CONSUMES an ecosystem of
primitives — connectors, plugins, MCP servers, models, channels, tools. Naive Discovery/Compare
flattens two different things into one matrix and mislabels the players. These scoping moves keep
them straight. (Motivating run: scoping an "agent platform input/output capabilities" study —
connectors + MCP + channels across Foundry / Agentforce / Vertex / Bedrock / China clouds.)

## 1. Provider vs consumer — split into two streams BEFORE auditing
The cardinal move. A capability that platforms CONSUME has two research questions, and they are NOT
the same study:
- **Stream A — provider/supply + demand:** who PROVIDES the primitive, how broad is each catalog,
  and what does the market actually USE most? Subjects = the ecosystem providers (for connectors:
  Zapier, Power Automate, Workato, Boomi, MuleSoft, Celigo…; for MCP: the registries).
- **Stream B — platform consumer audit:** for each platform, what does it EXPOSE/consume and HOW
  (mechanism, governance, GA/preview)? Subjects = the platforms.

Rules:
- Do NOT audit the consumed primitive by looking at the platforms — the platform is the consumer,
  not the provider. Auditing "connectors" via agent platforms misses the real catalog owners.
- Keep the two streams as separate inventories. Run synthesis (rankings, "top-N must-have", rollout
  priority) only AFTER both streams are done — never inside either one.
- The vendors that appear in BOTH streams (own a catalog AND ship a platform — Microsoft Power
  Automate+Foundry, Google Integration Connectors+Vertex, Salesforce MuleSoft+Agentforce) are
  exactly the differentiated "owns the substrate too" players. The two-stream structure makes that
  overlap visible instead of buried.
- A single primitive can be SLICED across both streams, each taking its half (e.g. connectors:
  Stream A = which catalogs exist + most-used; Stream B = which each platform exposes). Neither
  stream "owns" the topic.

## 2. Provider-list correction checks
When handed a provider list, run these before trusting it:
- **Protocol ≠ catalog.** A standard/interface (e.g. "MCP") is not a connector catalog. It belongs
  in the ecosystem-maturity sub-list, not the provider inventory.
- **Consumer ≠ provider.** A platform that wraps your own APIs (AWS AgentCore Gateway) or an agent
  product ("Agentspace") is a consumer; the catalog is a differently-named product (Google's is
  "Integration Connectors").
- **Catalog-owner ≠ API-owner.** The iPaaS that hosts/certifies the connector is the provider, not
  the source system whose API it wraps.
- **Name the catalog precisely + capture breadth count** per provider, not the parent brand.

## 3. Membership gate for layered category terms ("platform")
Many enterprise categories are layered terms. Before Discovery diverges, gate the category word the
same way you gate a property word (the property-gate pitfall in SKILL.md):
- **Platform** = managed stack that builds, HOSTS, and GOVERNS (with its own primitive surface).
- **Builder** = few/zero-code authoring canvas (the build surface).
- **SDK/framework** = code library, self-host, no managed platform, no low-code canvas → usually OUT
  (belongs to an orchestration-frameworks study, not a platform audit).

Then NAME THE BUILDER/PLATFORM PRODUCT, never the finished end-user assistant. A vendor usually ships
both; the assistant fails the gate. (Observed: a "grown-on-SaaS" list named finished assistants —
ServiceNow Now Assist, SAP Joule, ChatGPT Enterprise, Claude for Enterprise — all of which FAIL the
gate; the in-scope builder products are AI Agent Studio, Joule Studio, AgentKit, Claude Agent
SDK/Managed Agents.) Verify ambiguous product brands against the vendor's own product page before
locking (e.g. Huawei's agent platform is AgentArts/智果, not the lower-layer ModelArts).

## 4. Build / host / pre-built altitude (Compare caution)
"Platform" hides up to three jobs, sometimes shipped as SEPARATE products by one vendor:
- **Build tool** (author) — e.g. Google ADK, OpenAI AgentKit
- **Host runtime** (run + scale + govern) — e.g. Google Agent Engine, AWS AgentCore Runtime
- **Pre-built agents** (switch on) — the finished assistants

Do NOT compare a builder against a host as if they're peers — that's an altitude mismatch. Map each
object to its layer first, then compare layer-against-layer (build vs build, host vs host). SaaS
vendors usually run all three layers; infra players (AWS) are host-led with no pre-built; model
companies (OpenAI/Anthropic) are build-led and thin on managed host. Tag GA-vs-preview per layer —
managed-host layers are the newest and flip fast.

## 5. Reconciling differing prior object sets
When two prior research docs cover the same field with DIFFERENT object sets, neither is
automatically right for the new question. A doc scoped for "governance" may have dropped exactly the
players who matter for "I/O / channels". Reconcile by relevance to the CURRENT axis, merge, and flag
the divergence openly rather than copying one set wholesale.

## 6. Content-vs-packaging for a consumed primitive
A consumed primitive often has a CONTENT layer and a PACKAGING/transport layer that get conflated:
- **Content** = the actual integration logic (a connector: auth + triggers + actions + schema).
- **Packaging** = a standard for exposing it (MCP, OpenAPI import, CLI, native function tool).
The same content can ship through several packagings ("two doors": a governed catalog AND an MCP
facade). Audit packaging as an EXPOSURE-FORMAT dimension, not as a peer to the content catalog. The
durable moat is usually the governed/hosted/curated CONTENT catalog, not the (free, universal)
packaging standard — but track which advantages the standard is absorbing (e.g. MCP gained OAuth 2.1
mid-2025), because some are erodible.

## 7. "Official" registry / standard — what qualifies
When a field has an "official" registry/catalog, "official" is a precise status, not popularity:
published/governed by the standard's OWN maintainers, defines the spec others conform to, positioned
as single source of truth. Everything else is a community or vendor SUB-registry layering curation on
top. Tag each as official / vendor-sub / community, and note breadth-vs-curation (a huge unchecked
registry is breadth without trust — that gap is itself the maturity finding).

**What the official registry actually LISTS — check it, don't assume.** "Source of truth" does NOT
mean it contains the other registries. Hit its live API/about page: it usually lists GRANULAR items
(individual servers/packages), stores METADATA not code (pointers to npm/PyPI/Docker/a remote URL),
and the community registries are PEERS, not children. "Meta-registry" describes the SPEC role
(others conform to its format and can ingest from it), not containment. (Observed: the official MCP
registry at registry.modelcontextprotocol.io lists individual servers with duplicates — same
server/version published repeatedly — so its record count overstates unique servers; Glama/Smithery
are not inside it.)

**Sub-registries are NOT the same set as the official one — different intake.** The official one is
usually PUBLISH-IN (maintainer chooses to publish); community ones often CRAWL the source (e.g. Glama
clones+rebuilds every GitHub server) and then de-dup + grade. So counts differ 2–4×, and each holds
servers the others miss. Never count one registry and call it "the ecosystem size" — report it as
"~N active, counted differently by each registry," and treat the count/curation SPREAD as a finding.

## 8. Registry-TYPE taxonomy + the discover-don't-recall sweep
A consumed-primitive ecosystem (MCP servers, plugins, connectors) has registries in DISTINCT TYPES,
and a flat list hides the structure. A **registry is a CATALOG** — a list that points to where
servers live. Only three things are actually registries:

| Registry type | Optimizes for | Tell |
|---|---|---|
| Official / standard | the spec, source-of-truth format | run by the protocol maintainers |
| Large community directory | breadth / discovery | biggest counts, least curation |
| Vendor-curated catalog | trust + that vendor's distribution | signed/scanned/verified, narrower |

**Two ADJACENT layers get mis-filed as registry types — keep them OUT of the registry taxonomy**
(user correction, settled): a registry is a catalog; these two are not catalogs and must not sit as
rows in the registry table.
- **In-app marketplace** (VS Code's `@mcp` gallery, Cursor, Cline, Goose) — a CLIENT SURFACE inside
  an IDE/client that mostly RE-DISPLAYS servers already listed in the catalogs above and one-click
  installs into THAT app. It's a discovery/install convenience, not a distinct catalog of its own.
  (Precision: VS Code's browsable `@mcp` gallery IS the marketplace; hand-editing `mcp.json` is just
  manual config, not a marketplace.)
- **Aggregator / hosting platform** (Arcade, Composio, Klavis, Pipedream) — a RUNTIME layer, not a
  catalog at all. It HOSTS + RUNS servers and MANAGES AUTHORIZATION centrally: the client connects
  once to THEIR URL, and the platform holds each end user's OAuth tokens, so every user acts with
  their OWN permissions (on-behalf-of auth — "the security context travels with the user, not the
  agent"). Filing it under "registry" is a category error.

The separating axis: a directory answers "WHERE is the server"; an in-app marketplace answers
"install it where I work"; an aggregator answers "RUN it and authorize it FOR me." Aggregators exist
precisely because the bare protocol doesn't solve identity / per-user auth / token lifecycle — so an
aggregator is evidence of exactly that maturity gap (section 9). Worked flow (Arcade, verified from
docs.arcade.dev): pick tools in a dashboard → they bundle into ONE gateway URL → paste that URL into
the client once → just-in-time OAuth fires per tool on first use, tokens auto-refreshed → agent runs
across all tools through the single connection. Moat read: this is the same job Microsoft already
does natively with Logic Apps connectors + Entra ID (managed hosting + per-user delegated auth +
central governance) — the standalone aggregator startups sell, as a product, what a governed
catalog + identity fabric provides built-in.

> **Discover the registry list, don't RECALL it — and sweep for the types frequency-ranking
> under-counts.** Frequency-ranking "best X registries 2026" listicles (the SKILL.md Discovery
> protocol) favors general directories and SILENTLY drops vendor-curated + in-app + regional types,
> because bloggers list directories, not vendor catalogs. After the frequency rank, CONSCIOUSLY add a
> sweep query per under-counted type (vendor catalogs, IDE marketplaces, regional/China e.g. Baidu
> MCPWorld). (Observed twice in one session: listing from memory missed mcp.so + OpenTools, then a
> frequency rank missed Docker MCP Catalog + the Anthropic Connectors Directory entirely — both real,
> both vendor-curated. The user caught both.) Same anti-bias rule as unseeded Discovery, one level up:
> don't let the ranking method zero out a whole CATEGORY.

## 9. Measuring ecosystem MATURITY — decompose, never score "production-ready" as one axis
Frame the maturity question SHARPLY and from the adopter's side: not "how mature is this ecosystem"
(vague, un-actionable) but **"can an enterprise build a production VERTICAL AGENT on this ecosystem
today?"** That narrower goal tells you exactly which axes matter and which to drop.

**Split the axes by HOW they're measured — this is the method, not a detail (user insight, settled).**
Two kinds, and they run in PARALLEL because they use different sources and different work:
- **Population census** — you can only know it by examining the SERVER LIST itself (scan many items,
  read the distribution). Coverage and per-server quality are census axes.
- **Global read** — you read a FEW authoritative sources (the spec, deployment docs, the gateway
  landscape); no server-by-server scan. Deployment modes and governance are global-read axes —
  governance especially lives in the control plane you wrap around servers, never in any single
  server, so scanning servers would never find it.
Every per-server attribute (license, security, "self-hostable?", "implements the auth spec?")
concentrates in the census; the global-read axes are about the OPTION SPACE, not the population.

A clean 3-layer shape falls out (reuse it):
- **Layer 1 — registry landscape** (global read): the merged registry table from sections 7–8.
- **Layer 2 — richness & quality** (population census): scan one good registry; see census mechanics
  below.
- **Layer 3 — deployment & governance** (global read): the option space below.

### Census mechanics (Layer 2) — reuse published grades, scope to the enterprise subset
- **Don't hand-grade the whole corpus, and don't INVENT categories — reuse what the registry already
  publishes.** A good registry exposes its own grading + taxonomy; lean on it. (Glama: every server
  graded A–F on License / Quality / Maintenance, plus 102 attributes in 6 dimensions — 85 Categories,
  Languages, Capabilities, Hosting, Environment, Author. Pull these, don't re-derive them.) Add
  **category/scenario** as a first-class per-server dimension, sourced from the registry's real
  category list — never a category scheme you made up.
- **Scope the census to the ENTERPRISE-RELEVANT subset, not all 36k.** Censusing tens of thousands of
  mostly-hobby servers is impossible and pointless. Build a target list of the systems a production
  vertical agent actually needs (reuse the Stream-A connector/enterprise-system list) and measure
  against THAT.
- **Measure coverage TWO ways — the enterprise list is the focus, not the only lens (user correction).**
  (a) **Enterprise target-system check** — for each needed system, does a good FIRST-PARTY server
  exist? This finds the gaps that block a vertical agent. (b) **Category-taxonomy scan** — coverage +
  quality distribution across the registry's full category set, to catch strengths/weaknesses BEYOND
  the enterprise checklist (e.g. a whole category that's large but low-graded). First-party-vs-community
  ratio matters more than the headline count.

### Deployment & governance (Layer 3, global read)
- **Deployment = three modes, and the real question is the DATA BOUNDARY, not "self vs managed."**
  local (workstation/STDIO) · self-hosted remote (your VPC/tenant) · vendor-managed remote (SaaS host
  or aggregator). The enterprise test is **"does data stay inside my residency boundary?"** — a
  dedicated-tenant remote can pass it; a shared SaaS host fails it. (Glama's Hosting + Environment
  attributes give a first read.)
- **Governance = what the protocol GIVES vs what a GATEWAY must ADD.** The bare protocol gives
  discovery + tool-calling and nothing else; identity/attribution, access control, observability/audit,
  and compliance are bolted on by a gateway. The existence of an MCP-gateway MARKET (Lunar.dev, MCP
  Manager, Obot; Gartner already tracks the category) IS the finding — a whole product class forming to
  fill a hole means the hole is real.

The 8 axes below are the MENU these three layers draw from — capture each per registry/ecosystem,
each cell sourced:

| Axis | Asks |
|---|---|
| Discovery & breadth | how many items, how findable |
| Curation & quality | junk filtered? graded? de-duped? |
| Identity & authorization | OAuth? per-user tokens? scoped? |
| Security & supply chain | signed/scanned? known CVEs? |
| Hosting & runtime | metadata-only vs runs-it-for-you |
| Observability & governance | can you see what ran? admin control? |
| Reliability & maintenance | versioned? maintained? stale? |
| Adoption | who actually pulls from it |

The literature converges: "OAuth is necessary but not sufficient"; the bare protocol "does not
provide multi-tenant auth, observability, governance." So enterprise-readiness = identity + security
+ observability + governance STACKED — and those four are exactly what the protocol lacks, which is
why the aggregator/hosting type (section 8) exists. Measuring them separately turns "is it mature?"
from an opinion into a scorecard. Keep the capture raw (one row per registry, sourced cells); the
scoring/weighting is deferred synthesis, same as every other Stream-A inventory.

## 10. Output-side: channel gateways (the DELIVERY ecosystem)
Sections 1–9 develop the INPUT side (connectors, MCP, registries). The OUTPUT side of a platform
I/O audit has its own provider class — **channel gateways** (Twilio, Bird/ex-MessageBird, Microsoft
Bot Framework Channels / Azure AI Bot Service, Sinch, Vonage, Wechaty, …). A channel gateway is an
**output-side Stream-A provider**: it sells REACH — "integrate once, deliver to many messaging
channels." Its **supported-channel list is the output analog of a connector catalog's breadth count**,
and you can read that list as a channel-DEMAND signal (the gateway only bothers to support channels
its buyers want to reach). Inventory it the same way you inventory connector providers in Stream A.
(Motivating run: a LOCKED 4-gateway channel inventory for an enterprise-agent doc.)

**Rules that are specific to channel-gateway inventory (each earned in the run):**
- **The canonical primary source is the vendor's OWN "supported channels" page — copy it verbatim,
  don't paraphrase from memory.** Each vendor names/structures it differently: Twilio "Messaging
  Channels" (`/docs/messaging/channels`), Bird "Supported channels" (`docs.bird.com/.../supported-channels`),
  Microsoft "Channels list" (`learn.microsoft.com/.../bot-service-manage-channels`), Wechaty
  "Supported Instant Messaging services" (`wechaty.js.org/docs/wechaty` + the puppet-providers table).
  A `tvly search ... --include-raw-content` that lands the exact docs page lets you copy the literal
  channel bullets/table.
- **A hand-drafted / "locked" channel list is almost always INCOMPLETE — the vendor list runs
  longer.** Expect to EXPAND every row. (Run reality: the locked draft had Twilio = "SMS, WhatsApp,
  web chat, voice" but the vendor pages add MMS, Facebook Messenger, RCS; Bird's draft of 4 became
  7+ incl. LINE / Apple Messages for Business / LinkedIn Pages; MS Bot's real "Channels list" is ~17;
  Wechaty is not WeChat-only — also WhatsApp, WeCom, Lark, Gitter, Official Account.)
- **Track RENAMES to the CURRENT page — this space renames constantly.** MessageBird → **Bird**;
  Microsoft **Bot Framework Channels** is now delivered under **Azure AI Bot Service** (same channel
  model). Use the current name + current page, note the old name. (Same "re-confirm renamed products"
  rule as the main truth contract, but channel vendors rebrand especially often.)
- **Disambiguate the PRODUCT LAYER within ONE vendor — a bare ✓ is wrong.** A vendor's "channels"
  differ by product surface. Twilio: RCS is **GA at the Programmable Messaging layer but "Not
  supported" in classic Conversations**; Facebook Messenger is Public Beta in Conversations/Flex.
  Say WHICH surface supports the channel, and mark layer-conditional cells ◐, not ✓. (This is the
  section-4 build/host altitude caution applied to channels.)
- **GA-vs-preview and deprecated, PER channel → ◐, not ✓.** MS Bot Telephony / Outlook / Search are
  preview; Kik / Skype are "closed to new bot development." Don't promote a preview/closed channel to
  a clean check.
- **Adapter-reachable ≠ natively listed.** If a channel is only reachable via a third-party adapter
  and is NOT on the vendor's official channel list, record it as NOT listed (e.g. WhatsApp on MS Bot
  is adapter-only) — don't infer a ✓.
- **The matrix is the RAW deliverable; "overlap" is a COUNT, never a RANKING.** Columns = the UNION
  of every distinct channel any gateway lists; cells = ✓ / ◐ / —. Noting "SMS, WhatsApp, Facebook
  Messenger appear across the most gateways (3 of 4)" is a factual frequency read and is allowed.
  Computing a priority / must-have / recommendation FROM that demand-signal matrix is **deferred
  synthesis** — do NOT do it unless asked (same descriptive-not-prescriptive discipline as Compare).
- **Always ship an UNVERIFIED / could-not-confirm list.** Cells you couldn't confirm on the official
  page (a channel on a separate marketing page but absent from the canonical channels index; a
  layer-conditional ✓) go here rather than getting a fudged check.
- **Page DATE honesty:** vendor docs show a "Last updated" label, but the date string is often NOT in
  the fetched raw content. Record the **access date** and say the page's own date wasn't exposed in
  the capture — never invent a page date.
