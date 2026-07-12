---
name: deep-research
description: "Composable product/market/concept research for PMs — assemble lenses (concept, discovery, teardown, forms, compare, trends) to fit any research question, with human checkpoints and an evidence-graded output."
triggers:
  - user asks to research a product, market, or concept
  - user asks for competitive analysis or competitor comparison
  - user asks what some product/system is or how it works
  - user asks how a capability or pattern is productized in the market
  - user asks to clarify a concept and its relationship to adjacent concepts
  - user asks to scope a landscape ("what products do X")
version: 1.0.0
author: taoxu
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, product, market, competitive-analysis, teardown, pm]
    related_skills: [pm-writing-gater, tavily-search, advisory-council]
---

# Deep Research — Product / Market / Concept (Composable)

Research is **not a fixed template you pick** — it is **building blocks you assemble**.
The research target changes every time (sometimes there is no product at all, just a
concept). What stays stable is a small set of **composable lenses** plus a **quality
contract**. The job of Step A is to read the question and decide *which lenses to light
up and how heavy each one is*.

> Core principle the user converged on: **the object list is an OUTPUT of research, not
> an input.** Never assume you already know who to study. If the target set is uncertain,
> the Discovery lens produces it — and the user ratifies it.

> 🥇 **GOLDEN DATA RULE (settled by Ken — overrides any instinct to the contrary).** For ALL
> factual data, **never use your own memory or training knowledge — always pull the latest
> yourself.** This is the default for every fact in every run, not just "fast-moving" topics.
> 1. **Pull the latest authoritative page, dated.** Fetch the vendor's / maintainer's OWN official
>    doc or blog. If no official page exists, use the most recent public article instead.
> 2. **What that page states IS the truth — take it at face value.** Once you've pulled the latest
>    authoritative page, trust what it says. Do NOT run another round of web searches to re-check
>    each sub-fact on it one by one. One good authoritative pull settles it. (This still kills the
>    classic failure: writing "X lacks Y" from memory — pull X's current page and read what it
>    actually says before any absence claim.)
> 3. **Only exception: data the user gave you explicitly, up front.** If Ken hands you a provider
>    list, a dimension list, or any datum before the research, use it as given. Even then, if it
>    could be stale or incomplete, **ask Ken and double-confirm** before building on it.

---

## The 6 Lenses (single responsibility each — do not overlap them)

Two stages: **understand each object** (Concept, Discovery, Teardown), then **synthesize across
them** (Forms and Compare are sibling synthesis steps — both run AFTER Teardown). Trends
reads the time axis on top.

| Lens | The one question it answers | Object count | Output shape |
|---|---|---|---|
| 🔍 **Concept** | "What does this term/idea *mean*?" | 1 abstract idea | definition + boundary + relation to neighbors |
| 🧭 **Discovery** | "Who/what should I even study?" | unknown → set | a deduped, classified candidate list |
| 🔬 **Teardown** | "How does this single object work inside?" | 1 concrete thing | deep analysis (depth/width tunable) |
| 🗺️ **Forms** | "What product *forms* does this set fall into?" | analyzed set | clustering along a FORM axis, not a vendor list |
| ⚖️ **Compare** | "How do these differ; who's stronger?" | 2+ analyzed objects | matrix + positioning conclusion |
| 📈 **Trends** | "How is this evolving over time?" | a field | 5–7 named, argued trajectories |

> **Forms and Compare are the two synthesis siblings.** Both consume Teardown results;
> neither runs before Teardown. Compare lays objects against a dimension axis (who's stronger);
> Forms clusters the analyzed set along a form axis (what shapes exist). A flow uses one,
> the other, or neither — rarely both.

### Design invariants (deliberately chosen — do NOT "fix" these back)

These are settled decisions from the design of this skill. Each looks like something a future
editor might "improve" by reverting. Do not. If you think one is wrong, raise it with the user
first — they made these calls on purpose.

1. **Teardown precedes BOTH synthesis steps.** Forms and Compare are siblings that BOTH
   run after Teardown. Reason: you can only name genuine market forms / score real differences
   after you understand how each player works. Clustering or comparing first = armchair
   categories. Never move Forms (or Compare) above Teardown.
2. **The object list is an OUTPUT, never an input.** When the target set is unknown, Discovery
   produces it and the user ratifies it. Never pre-seed the deliverable with a vendor list you
   assumed.
3. **Lenses have single, non-overlapping responsibilities.** Teardown = deep-analyze ONE object
   (depth tunable). Compare = arrange Teardown RESULTS (never collects raw data, never
   deep-dives one object). "Directed profiling of each competitor" is not a new lens — it is
   `Teardown(dimensions=limited, depth=shallow)`. Don't split it out.
4. **Composability over templates.** This is building blocks you assemble per question, NOT three
   fixed modes (landscape/targeted/deep-dive). An earlier draft used fixed modes; it was rejected
   because the research target — and even whether a product exists at all — changes every time.
   Step A's whole job is choosing which blocks light up. Don't collapse it back into named modes.

Regression oracle for all of the above: `references/test-cases.md` (four real user requests with
expected flows + MUST/MUST-NOT). Re-check it after any structural edit.

### Editing this skill safely (this file is iterated often — read before you edit)

This is a multi-file skill (`SKILL.md` + `references/test-cases.md` +
`references/discovery-search-tooling.md` + `references/verification-and-recency.md` +
`references/competitive-gap-analysis.md`)
with numbered invariants that other sections cross-reference. Edits here have a habit of leaving
silent breakage. Six hazards earned the hard way:

> Reference file for platform/ecosystem competitive scoping (provider-vs-consumer two-stream split,
> platform/builder/SDK membership gate, build/host/pre-built altitude, official-registry definition,
> registry-TYPE taxonomy + discover-don't-recall sweep, ecosystem-maturity decomposition, output-side
> channel-gateway inventory):
> `references/platform-ecosystem-scoping.md`. Load it when the subject is an enterprise platform that
> CONSUMES an ecosystem of primitives (connectors, plugins, MCP servers, channels, models).

1. **Patch against a RAW file read, never against `skill_view` output.** This file is large
   (~28KB). `skill_view` can return an LLM-SUMMARIZED version that silently drops whole items
   (it once dropped an entire invariant). If you patch against the summary you'll target text
   that differs from disk and either fail to match or corrupt the file. Read the actual file
   first, copy the exact `old_string` from it.
2. **Deleting or reordering a numbered invariant breaks every `(invariant #N)` cross-reference.**
   Those references are scattered across the Compare lens, the Pitfalls list, AND
   `references/test-cases.md` (MUST/MUST-NOT lines + the coverage-map row). After any
   add/delete/reorder of the invariant list: renumber the list, re-point every `(invariant #N)`
   citation to the new target, then grep the whole skill dir for `invariant #` / stray `#N` and
   confirm zero stale hits. Renumbering silently mis-points citations — the file still "looks fine."
3. **Before deleting a rule, separate behavior-removal from label-demotion — they diverge sharply.**
   "Remove invariant X" can mean *(a)* reverse the behavior (the skill may now do X) → delete the
   rule AND its downstream guards/pitfalls/test-cases, or *(b)* just demote it from the invariant
   list while keeping the behavior → delete the list item and the `(invariant #N)` labels but KEEP
   the rule everywhere it's enforced. Confirm which before touching anything; the two produce
   different skills.
4. **A global rename must verify to ZERO across every `references/` file, not just SKILL.md.**
   Finishing the rename in SKILL.md feels done, but stragglers hide in test-cases.md (flow lines,
   MUST bullets, regression sentinels, coverage-map rows). After any rename, grep the whole skill
   directory for the old token and confirm 0 matches before declaring done.
5. **Reference files drift into topic-overlap — split them by WHEN they're consulted, not by topic.**
   This skill once grew THREE overlapping gap/verification reference files that repeated the same
   lessons (disprove-your-gap, catch-up-vs-greenfield, recency) because each was written for one
   session and named by subject. The fix that stuck: split by TRIGGER-TIME, not topic —
   `verification-and-recency.md` is ALWAYS-ON (fact-quality: is the datum true / fresh / officially
   sourced — runs on every live-product run) and `competitive-gap-analysis.md` is CONDITIONAL
   (judgment-quality: is the conclusion sound — loads ONLY on a gaps / enhancement / confirm-my-
   conclusion follow-up). Two rules from that cleanup: (a) when a SKILL.md pointer DESCRIBES a
   reference file, the description must match what's actually always-on vs conditional inside it —
   mislabeling a partially-always-on file as "gap-only" makes always-on rules (e.g. the recency /
   primary-source check) read as conditional, which is exactly the bug a user will catch; (b) before
   adding a new reference file, check whether its content belongs in an existing file under the same
   trigger-time axis, rather than starting a third near-duplicate.
6. **When folding a session's lesson in, STRIP the session-specific framing first — keep the
   principle, drop the artifact.** A lesson learned on one task arrives wrapped in that task's
   vocabulary (a report's section name, a vendor codename, a doc's structure). The class-level
   skill must state the lesson in ITS OWN general terms; importing the session's local noun makes
   the rule read as a narrow special case and the user rejects it. (Observed: the
   fetch-don't-recall lesson was first written as a rule about "the BASELINE / own-product cell" —
   "baseline" was THIS report's structure, not a deep-research concept. Ken rejected it: "there is
   no baseline stuff called out, and I don't want such thing surfaced." The fix: re-state it as
   "never fill a factual cell from memory, including the object you know best," which is the same
   lesson with zero session-specific framing.) Test before saving: would this wording make sense to
   someone who never saw today's task? If it names something only today's task had, generalize it.
   **And state the rule in its SIMPLEST form — Ken rejects over-engineered multi-clause rules.**
   (Observed same session: the Golden Data Rule was first written as a 4-clause rule with a
   "fetch every fact, each one, every time" re-check loop; Ken pushed back — "can you do it in a
   simple way?" — and the rule that stuck was "pull the latest official page once; what it says is
   the truth; don't re-check sub-facts one by one." When a settled rule reads heavy, cut it to the
   one sentence that carries the behavior before saving.)

### Memory anchors for the 3 lenses that blur together
- **Concept** plots the **point** on a map (what it means, where it sits).
- **Teardown** dissects that point's **internals** (parts, mechanism, journey, architecture).
- **Compare** measures the **distance** between points (it does NOT re-analyze a single object).

### The Teardown ↔ Compare boundary (the user's explicit definition)
- **Teardown = deep analysis of a SINGLE object.** Depth and width are **parameters**:
  - *Full teardown* — journey + architecture + mechanism (e.g. a deep dive on one unfamiliar product).
  - *Dimension-limited teardown* — only the few axes a comparison needs (the "shallow, even" profile of each competitor).
- **Compare = comparison of Teardown RESULTS** (2+ objects), whether those teardowns were
  full or dimension-limited. **Compare consumes teardown output; it never touches raw source
  material and never deep-dives a single object.**
- So "directed profiling of each competitor" is **not a separate lens** — it is just
  `Teardown(object, dimensions=limited, depth=shallow)`. Same lens, smaller parameters.

---

## The 4 Human Checkpoints (stop and get user ratification)

Four things must be ratified by the user. **Checkpoints 2 and 3 are presented TOGETHER**, in one
review right after Discovery — so the comparison dimensions are always confirmed before Teardown.

1. **After Step A — the plan.** Which lenses you'll light up and how heavy. User confirms/adjusts.
2. **After Discovery — the object set (rows).** The classified candidate list — *who* to study.
   User prunes/adds.
3. **With checkpoint 2 — the dimensions (columns).** The recommended comparison dimensions —
   *what* to compare on. User edits/finalizes. Presented in the SAME review as checkpoint 2:
   prune/add the tools and finalize the dimensions in one pass. **Locked here, before Teardown** —
   never after, because Teardown is filled against these exact dimensions.
   **Axis-coverage check before locking (hard guard):** if the user stated the scope as an explicit
   set of axes (e.g. "compare on (1) visibility, (2) management, (3) cost, (4) observability/alerting"),
   map every proposed column to one of those axes and confirm each axis has real coverage. An axis that
   collapses to ONE thin column — or zero — is silent under-scoping: the report will faithfully answer
   its columns while missing half the question, and the gap surfaces late as "you missed X from my
   scope." Add columns to cover any thin axis BEFORE locking.
   **Also ask, in this same review, whether to run the recent-3-month trend round (OPTIONAL).**
   The dedicated "what shipped in the last 3 months" search pass (see Teardown) is opt-in, not
   automatic. Once the rows + columns are locked, ask the user a plain yes/no: "Do you also want
   the recent-3-month trend research?" Run it ONLY if they say yes. Default to NO if they don't ask
   for it. Never kick off that extra round without this explicit OK.
4. **After Persist — the self-review gap list.** Read the finished report back against this skill's
   Quality Contract and Pitfalls, hand the user a followed/deviated gap list, and let them choose
   which structural gaps to fix. Details in *Self-review against this skill* near the end. Clear-cut
   errors you fix without asking; structural changes wait for the user's call.

> Why bundle rows and columns: the dimension axis drives BOTH downstream lenses — for Teardown it
> defines *what to collect per object*; for Compare it defines *what to lay side by side*. Confirming
> them together keeps "what we collect" and "what we compare" aligned, and guarantees Teardown never
> starts without a locked dimension set.
>
> This is also where **business vs technical scope** is decided. Do NOT preset business dimensions
> (pricing, target segment, GTM, funding). Offer them; the user adds them if they care, drops them
> if they only want product capability.
>
> (If a flow skips Discovery — e.g. a single unfamiliar product — still confirm the dimensions with
> the user before Teardown.)

---

## Step A — Translate the question into a plan (then checkpoint 1)

Read the request and answer three things, then show the user a one-paragraph plan:

1. **What is the subject?**
   - an *abstract concept* (no product) → Concept-led
   - an *unfamiliar single product/system* → Teardown-led
   - a *known object vs a known object* → Teardown(s) → Compare
   - a *capability/pattern* ("how is X productized") → Discovery → Teardown → Forms
   - a *capability domain* ("who does X") → Discovery → Teardown → Compare
2. **Is the object set known?** If no → Discovery is required. If yes → skip Discovery.
3. **Which lenses, how heavy?** (● heavy / ○ light / — none)

Example plan reply (for "what is MDASH and how does it differ from Evergreen"):
> Subject: one unfamiliar product (MDASH) + one known object (Evergreen). Objects are
> already fixed → no Discovery. Plan: Teardown MDASH (full) → Compare the two on a confirmed
> dimension axis. Stops at the objective comparison — no strategy section. Proceed?

---

## The pipeline at a glance (input → output per step)

For a full market/competitor run, the lenses chain like this. Each step's output is the next
step's input. The dimension set, locked at checkpoint 2+3, is the hinge that keeps Teardown and
Compare aligned.

| Step | Takes in | Produces | Checkpoint |
|---|---|---|---|
| **A. Plan** | the raw question | which lenses, how heavy | ⛳ 1 — user OKs the plan |
| **Concept** (gate) | the topic + any property word | definition + in/out criteria | — |
| **Discovery** | category map (NOT names) + any user-named tools | a classified, frequency-ranked candidate tool list | — |
| **Dimensions** | Concept + Discovery results | recommended comparison columns | — |
| **Review** | candidate list + recommended dimensions | user-edited tools AND locked dimensions + optional-trend-round yes/no | ⛳ 2+3 — rows + columns together, then ask the optional recent-3-month trend question |
| **Teardown** (per tool) | locked tools + locked dimensions | one prose profile per tool (fills the dimensions); IF trend round opted in, ALSO a dated last-3-months feature list from a SEPARATE pull of the official "What's New"/release-notes page | — |
| **Compare** | all teardown profiles | §1 table + plain summary (always) · §2 recent-3-month trend summary (only if trend round opted in) | — |
| **Trends** (optional) | the field + Compare output | 5–7 named market trajectories | — |
| **Persist** | the finished report | two files in the research folder | ⛳ approval before writing |
| **Self-review** | the persisted report + this skill + pm-writing-gater skill | a gap list (mechanical scan + both skills), then fixes | ⛳ 4 — user reviews gaps before you fix |

Lighter flows drop steps (a single-product teardown skips Discovery), but the input→output
contract per step never changes. Step A decides which rows of this table light up.

> Note: this table shows the **Compare** branch (`… → Teardown → Compare → Trends`). A
> **Forms** branch swaps the Compare row for a Forms row (cluster the analyzed
> set along a form axis instead of laying it against a dimension matrix). Both branches share the
> upstream `Discovery → Teardown` spine; they differ only in the synthesis step.

---

## Step B — Execute the chosen lenses

### 🔍 Concept
1. Lead with a **concrete example/scenario FIRST, then name the term** (hard user rule).
2. Operational definition.
3. Boundary: what it **is** and explicitly **is not**.
4. Relation to adjacent concepts (e.g. event vs. state: "migration is an event, evergreen
   is keeping it from going stale again").
5. Common misconception.
Output: definition + an "is / is-not" table + a relation diagram. Does NOT dissect
architecture, list competitors, or score.

### 🧭 Discovery (parallel divergence → convergence)

> **The cardinal rule: discovery must be UNSEEDED.** The object list is an OUTPUT. If you put
> the vendor names you already know INTO your search queries, you get confirmation, not
> discovery — the engine hands back your seeds plus their nearest neighbors and the rest of
> the field stays invisible. This is the #1 silent failure of Discovery. (Real failure that
> motivated this rule: seeding queries with "Dependabot Renovate Snyk…" returned exactly
> those and missed Semgrep, Mend, Black Duck, Codacy, GitGuardian, and the entire Application
> Security Posture Management category.)

**Discovery protocol (mandatory — run in this order):**
1. **Map the category SPACE first, not vendors.** List the 4–7 sub-categories the field could
   contain. This category map — never a vendor list — is your query plan, and guarantees per-lane
   coverage so you can't silently zero out a whole category.
2. **One UNSEEDED enumeration query per category.** Build each query from the category + an
   enumeration trigger ("best/top … 2026 list", "… tools comparison", "… alternatives") with
   **ZERO candidate names in it**. Anchoring test: if a query contains a product name, rewrite it
   around the capability. Fire these as parallel entry points through the Tavily Search API.
3. **Mine result BODIES, not titles.** Listicles ("Top 23 SCA tools") are containers of MANY
   candidates — pull `include_raw_content` and harvest every product-like name from the text.
   Never treat one result as one tool.
4. **Frequency-rank across sources (convergence).** Build a name→count map over the whole corpus.
   A name recurring across independent listicles (recurrence ≥ 2) is real; a one-off is noise.
   This is what turns divergent search into a trustworthy set — skipping it is what makes
   Discovery untrustworthy.
5. **Add any user-named tools by default.** The unseeded rule is about your QUERIES, not the
   user's input. Every product the user named goes into the set automatically (after a quick
   scope check); discovery just finds MORE on top. The user's list is the floor, not the ceiling.
6. **Dedup, filter, classify.** Merge name variants (Sonar/SonarQube → one), filter against the
   Concept inclusion/exclusion criteria, then classify survivors into 3–5 meaningful categories.
   **Per-lane health check:** after classifying, look at the count and quality of each category.
   A lane that comes back THIN (few real candidates) or POLLUTED (mostly consultancies,
   agencies, or services dressed up as products in the listicles) is not a true \"this category
   is small\" signal — it usually means the generic enumeration query missed the real product
   vocabulary for that niche. Fire 1–2 **supplemental targeted** enumeration queries for that
   lane (still unseeded — built from the niche's concrete sub-capability, e.g. \"Java framework
   upgrade tools\" / \"COBOL mainframe migration tools\" for a starved modernization lane), then
   re-mine and re-rank. Do this BEFORE the checkpoint — never hand the user a starved or
   service-polluted category as if it were the finished set.
7. ⛳ **Checkpoint 2+3 (rows + columns together):** hand the user the classified candidate list
   AND your recommended comparison dimensions. They prune/add tools and edit/finalize the
   dimensions in one pass. **Confirmed dimensions are locked here, before Teardown.** Once the
   list + dimensions are locked, **ask the user the optional recent-3-month trend question**
   (plain yes/no) — run that extra search round only on an explicit yes (see checkpoint 3).

> ⚠️ **Gate any scoping PROPERTY word before diverging.** A sharp Concept gate (clear
> inclusion/exclusion criteria) improves Discovery precision — it stops divergence from dragging
> back near-misses. This matters most when the request attaches a property word to the set —
> "agentic", "self-healing", "continuous", "managed". Test every candidate category against that
> word BEFORE diverging. A frequent failure: the user names a market by a property the whole set
> does not actually share, so you scope to the wrong superset. Surface the split as concrete
> buckets (passes / fails / partial) and let the user pick. Watch the ongoing-STATE vs
> one-time-EVENT split: a property the tool must keep true over time is not the same as a single
> action or snapshot, and snapshot-only tools fail a state-property gate. Wrong label = wrong
> superset = wasted run.

> 🔧 **Retrieval reliability:** Discovery lives or dies on clean rows. Use the **Tavily web-access
> skills** (`tavily-search`, and `tavily-extract` for page bodies) for all queries — load
> `tavily-search` for the exact `tvly` CLI usage. For batch enumeration, the **Tavily Search API**
> (`TAVILY_API_KEY` in the Hermes env file) called via Python `urllib` is the clean-JSON path with
> no shell-escaping traps. Full playbook (request shape, the body-mining + frequency-rank code,
> fallbacks, and "ratify rows before spending evidence effort" sequencing) →
> `references/discovery-search-tooling.md`.
>
> 🌐 **ALWAYS use the Tavily web-access skills for any web search/fetch — in BOTH Discovery and
> Teardown.** In THIS user's setup the "web-access" path IS the Tavily skill family; there is NO skill
> literally named `web-access` here, so do NOT call `skill_view(name='web-access')` (it will fail).
> Load `tavily-search` (search) and `tavily-extract` (page fetch) — plus `tavily-crawl-map` /
> `tavily-research` when needed — before searching. The user MANDATES Tavily OVER the built-in
> `web_search`/`web_extract` tools: use it by default, not as a fallback. The `tavily-search` skill
> carries exact CLI usage (the `tvly` binary, loading `TAVILY_API_KEY` from the Hermes env file,
> writing JSON with `-o` then reading it; Python `urllib` fallback if `tvly` is missing). This is not optional polish — it prevents the single worst silent
> failure of this skill: **running a Teardown with no working web tool at all.** When the Teardown is
> delegated to subagents, the child often does NOT inherit a usable search tool, so it quietly falls
> back to training knowledge and returns confident-but-unverified pricing/features. Before trusting
> any delegated profile, (a) give the child the `web` toolset AND tell it to use the Tavily
> web-access skills (`tavily-search` / `tavily-extract`) — NOT a skill literally named `web-access`,
> which does not exist here — and (b) verify the volatile axes (pricing, last-3-month features) carry
> real source URLs — if they don't, re-fetch those cells yourself from the main session via a static
> Layer-0 fetch (`tavily-extract`, or curl + `r.jina.ai/<url>`, processed inside `execute_code` to
> keep raw HTML out of context).

### 🔬 Teardown (single object; depth/width tunable)
Teardown always runs against a **confirmed dimension set** (locked at checkpoint 2+3, before this
step). Two shapes, by depth:
- **Dimension-limited (the default for a comparison):** fill ONLY the confirmed dimensions, one
  structured row per object, each cell backed by a citation. Run in parallel subagents, one per
  object, all answering the same fixed dimensions.
- **Full (for a single unfamiliar product):** the confirmed dimensions PLUS deeper context —
  components → mechanism/flow → user journey → architecture/deployment → boundary/maturity. Use
  when the goal is to understand one product in depth, not to line several up.
Either way the dimensions are fixed first; "full" only adds depth on top. Does NOT compare to
others (that's Compare's job).

> **Depth floor — a teardown is NOT a row of one-liners.** Each object must yield a
> **3–5 sentence prose profile** that a reader could understand on its own BEFORE it gets
> compressed into a matrix cell. Generic verb-cells ("alert + fix") are a teardown failure —
> they read back as filler and the Compare matrix floats with nothing under it.
>
> **Follow the confirmed dimensions, strictly.** The dimension axis the user locked at the
> checkpoint AFTER Discovery and BEFORE Teardown is the exact template for every profile. Fill
> the same dimensions for every object, in the same order, each backed by a citation. Do not
> add your own dimensions and do not skip any — same shape for all objects so Compare can lay
> them side by side cleanly.
>
> **Plus (OPTIONAL — only if the user opted in at the checkpoint, and only when the downstream
> synthesis is Compare/Trends): a DEDICATED second search round for each object's new features from
> the last 3 months.** This round is OPT-IN: run it ONLY when the user said yes to the recent-3-month
> trend question at the rows+columns checkpoint. If they didn't opt in, skip this entirely — do not
> collect it and do not run the extra pull. When it IS on: it's its OWN web pull, separate from the
> dimension research above — not a side-item you grab in passing. Target the object's **official
> "What's New" / release-notes / changelog / product-blog page**, and filter to the **last 3
> months**. Record a short dated list of what it shipped (named feature + month + citation from that
> page). Why a separate round: "what shipped recently / where is it heading" is a DIFFERENT question
> than "what does this product do," with a different best source (the What's New page, not the
> feature docs) — so it earns its own pull. (This does NOT conflict with the Golden Data Rule's "one
> authoritative pull settles it" — that rule bars re-checking the SAME page's facts twice; this is a
> fresh pull of a DIFFERENT page answering a DIFFERENT question.) **Skip it for a Forms flow** — a
> forms survey of sampled representatives doesn't consume recent-features data, so collecting it
> there is over-spec.
>
> All of this — the dimension profiles AND (if opted in) the recent-features summary — is the
> prepared input for the next step. Write the prose profile first, then the matrix cell is just its
> compression.

> 🛰️ **Delegating Teardown to subagents — three guards (each earned the hard way).** Parallel
> per-object subagents are the right pattern, but a naive dispatch fails silently in two ways:
> 1. **Budget or you lose everything.** A research subagent with no cap will over-research and hit
>    the wall (e.g. 600s / 50 calls), and a timed-out child returns **NOTHING** — all its work is
>    discarded. Give every Teardown child a HARD cap: \"≤N searches, lean on training knowledge for
>    stable facts, **start writing your answer by minute M** no matter what.\" A complete, slightly
A complete, slightly thinner profile beats a perfect one that times out to zero. **But a search-COUNT cap is not enough by itself** — it limits how MANY searches the child runs, not how LONG any one fetch can hang, and a single stuck network call still times the whole child out to zero (observed: a properly-capped child died at the 600s wall with only 10 calls done). Two more mitigations are mandatory on a live-web Teardown: (a) tell the child to wrap EVERY network command in a shell wall-clock timeout — `timeout 45 tvly … ; echo EXIT=$?` — and skip that source on `EXIT=124` instead of retrying; (b) split a heavy aspect into INDEPENDENT parallel children (one per sub-list / lane), so one hang costs a single lane, not the whole aspect. **Two-strikes rule:** if a delegated task times out twice, stop delegating it — run it yourself in the main session with per-call `timeout`s and an overall wall-clock cap (e.g. paginate the source's own JSON API directly, breaking at ~70s), which also lets you fold in the volatile-axis check from guard #3.
> 2. **Confirm the child actually HAS a web tool before trusting its citations.** A child spun up
>    without a `web`/search toolset will still cheerfully return full profiles — built entirely from
>    training knowledge, with invented-looking but unverified pricing and \"recent\" features. Put
>    `web` in the child's toolset explicitly, and tell it to flag any cell it could not verify
>    rather than guess. If the summaries come back with every \"recent feature\" hedged as
>    \"could not verify,\" the tool layer was missing — don't ship those cells as fact.
> 3. **Verify the VOLATILE axes yourself regardless.** Pricing and last-3-month features are exactly
>    what training knowledge gets wrong (stale numbers, missed releases). Even when children
>    \"succeed,\" pull those two rows yourself from primary pages before finalizing — a static fetch
>    (`curl` + a reader like `r.jina.ai/<url>`, processed inside `execute_code` so raw HTML stays
>    out of context) is fast and is Layer-0, no login needed. Engine/scope/language/workflow rows
>    are stable and can ride on synthesis; pricing/recent-features cannot.

### ⚖️ Compare (consumes Teardown results)
Compare outputs **Section 1 (table + plain summary) always — never a bare table**, plus **Section 2
(recent-3-month trend) ONLY when the user opted into the trend round** at the checkpoint. A table
alone is not a comparison; Section 1 is mandatory, Section 2 is opt-in.

1. Object set — from Discovery (checkpoint 2).
2. Dimension axis — user-ratified (checkpoint 3).
3. **Build the matrix.** Lay the N teardown results side by side (rows = objects/dimensions,
   cells = ✅/partial/❌ + a one-line "how": rule/AST/dataflow/LLM/runtime, + evidence).
4. **Section 1 — the matrix + a plain-English summary that explains it.** Read the pattern across
   the matrix and write a summary in plain words that walks the reader through the table: what the
   rows show, where the real differences are, who's deep, who's shallow, where one player pulls
   ahead, where two overlap. The reader should understand the table from your summary WITHOUT
   decoding the cells one by one. This summary is **descriptive, not prescriptive**: it states the
   differences that fall out of the data, NOT what the user's product should do about them. No
   bets, no "defensible wedge", no "consume X as a dependency", no recommendations — the skill
   stops at the objective comparison and the PM draws strategy themselves. "MDASH scans deeper across more
   languages than Evergreen's security pillar" is allowed (a fact from the table); "so Evergreen
   should not stake value on security" is NOT (a strategy call).
5. **Section 2 — recent-3-month trend summary (OPTIONAL — only if the user opted in).** Include
   this section ONLY when the recent-3-month trend round was approved at the checkpoint and the
   Teardown actually collected the recent-features data. If the user did not opt in, **Compare is
   just Section 1** — omit Section 2 entirely, don't apologize for it or fill it from memory. When
   it IS on: take the "new features in the last 3 months" that Teardown collected for each object,
   put them together, and read them as one picture — what is the whole market adding right now?
   Where is it heading? A summary of direction, not just a list of releases.

Optionally deep-Teardown the #1 rival while the rest stay dimension-limited. Does NOT collect raw
data itself — it only arranges what Teardown produced.

### 🗺️ Forms (Compare's synthesis sibling — also runs AFTER Teardown)
Use this **instead of Compare** when the question is "what forms exist", not "who's stronger".
The capability/pattern you're researching gets productized into several **forms** in the market;
this lens names them. It consumes the **analyzed** object set (the Teardown profiles) and
**re-clusters it along a FORM axis**, not by company. Because you tore the objects down first, the
forms are induced **bottom-up from real mechanics** — not guessed up front and then back-filled. Each form must be
filled with a **real representative** drawn from the teardowns; if a form can't be populated with
a real example, delete it (never invent plausible-looking forms). Output: a forms table
(form | defining trait | representative | maturity). Does NOT score who's best (that's Compare).

> Why Teardown comes first: you can only name the genuine shapes of a market after you understand
> how each player actually works. Clustering before teardown produces armchair categories;
> clustering after produces forms grounded in evidence.

### 📈 Trends (the vertical/time axis)
What horizontal comparison can't give: how the field is **evolving**. Identify **5–7 named,
argued trajectories** (not asserted). Cover both "what existing tools are adding now" (cited,
prefer recent) and "what the shift unlocks that wasn't possible before."

---

## Quality Contract (applies to ALL lenses)

- **Stance first, no info-dumps.** Produce opinionated conclusions, not feature catalogs.
- **Example before terminology** — ground a concept with a concrete case *before* naming it.
- **Evidence grading**: product/feature/stat claims MUST cite a primary source (vendor doc,
  release notes, case study), inline as markdown links. Trends/synthesis may be uncited POV
  but must be **argued, not asserted**. This applies to **matrix/table cells** too — link the
  source ON the verified cell (the pricing row, the recent-feature row). Do NOT defer citations
  to a footnote or an end "evidence note": parked sources read as verified-looking but unlinked
  (observed: a landscape report shipped pricing + feature cells with sources collected at the
  bottom instead of linked per cell).
- **Truth contract — every fact must be REAL, not hallucinated or weakly sourced (always on).**
  A smooth report built on made-up or stale facts is the worst failure this skill has. For every
  factual claim, run these five by default:
  1. **Official source first.** Get the fact from the vendor's / maintainer's OWN page (doc,
     release notes, status page). Reach for blogs, analysts, or news ONLY when the official page
     doesn't cover what you need — and say so when you do.
  2. **Copy the real line, don't paraphrase from memory.** For each key fact, quote the exact
     sentence from the source and keep it (in the dispatch file or beside the cell). You cannot
     fabricate a quote you actually copied; if you can't find a real line to copy, treat the fact
     as unconfirmed, not true.
  3. **Two independent sources for fast-moving facts.** "GA vs preview", prices, "just launched",
     headline numbers — require one OFFICIAL page, or two independent sources that agree. One blog
     alone is never enough for a volatile fact.
  4. **Disprove absence claims before writing them.** Any "X lacks Y" / "only Z does this" is the
     highest-risk kind of claim. Before writing it, search hard for evidence it is FALSE, using the
     vendor's own vocabulary; it survives only if a primary source confirms absence. Expect to
     retract ~half your first-draft gaps.
  5. **Tag each key fact with source type + date.** Note official / secondary / inferred and the
     source's date, so weak or stale facts can't hide among solid ones.
  These five are always on. **Per the Golden Data Rule (top of file), the fetch-fresh-and-date-it
  default applies to EVERY fact in every run — not just "fast-moving" ones.** The extra
  live-product mechanics (read the vendor page's "last updated" date, confirm
  general-availability-vs-preview against the official page, prefer the freshest authoritative
  source) matter most where status flips month to month — `references/verification-and-recency.md`
  §1 carries them. The gap-specific passes in that file
  (disprove-your-own-gap, catch-up vs greenfield, descriptive→prescriptive) fire ONLY when the user
  asks a gaps/enhancement follow-up — they are not part of a normal run. For a report going to
  senior / external readers, also keep a **proof sheet** (a table: claim → source
  link → date → exact quote → checked yes/no) as the dispatch companion.
- **Freshness — pull the latest-dated information.** Every fact should come from the most recent
  source available; prefer recency-filtered search (Tavily `--time-range month`) and the vendor's
  current page over older write-ups. Note the date on time-sensitive facts so the report reflects
  today, not last year. Re-confirm renamed products (vendors rename often).
- **Delegated research returns a link + the exact quote per fact, or you re-verify it.**
  Subagents are the biggest source of confident-but-fabricated facts (they fall back on training
  knowledge). Require every returned fact to carry a real source URL AND the copied sentence; any
  fact that comes back without both, re-fetch yourself before it enters the report.
- **No speculation about unannounced products**; mark rumored/leaked items as such.
- **Generalizing claims** ("they all share X") must be checked **against each item
  individually** before writing.
- **Post-write review**: every factual sentence must be verified true. Forms/matrix cells
  that can't be backed by a real source get deleted, not fudged.
- **Plain, simple English (hard user rule).** Short sentences, common words. Avoid dense
  jargon, long compound sentences, and heavy em-dash chains. The reader should never have to
  re-read a sentence to parse it. This applies to BOTH the research deliverable AND to how you
  explain the plan, progress, and "what changed" to the user during the engagement. When the
  user reviews your work, walk them through it in plain words, not a compressed technical wall.
- **Tables for comparison, prose for analysis.** Active voice, concise, no filler conclusions.
- **No explicit level labels** in prose; say "machine learning"/"deep learning" etc. directly.
- **Abbreviations: spell out on FIRST use, short form after, plus a glossary at the end.**
  Spell each term out the first time it appears, with the short form in parentheses — "Software
  Composition Analysis (SCA)", "GitHub Advanced Security (GHAS)" — then use the short form freely
  for the rest of the doc, including matrix cells. Do NOT spell the full name out everywhere (it
  clutters a dense report). Instead, add a **Glossary** section as the LAST section of the doc
  listing every short form used, each with its full name (and a few words of meaning if helpful).
  Two rules keep this honest: (1) every short form that appears in the body must have a glossary
  entry; (2) a short form used ONLY inside a matrix cell (where there's no room for a first-use
  spell-out) still needs its glossary entry. Never coin informal shortenings ("deps") — only real,
  recognized acronyms.

---

## Planning a multi-module research PROGRAM (when the run is a whole section, not one question)

Sometimes the request is not one research question but a **program** — several sub-modules to be
done in a fixed window (e.g. "research section 2.1 + 2.2 in 5 working days"). Plan it bottom-up,
not as a flat task list. Five rules that the user (Ken) explicitly ratified:

1. **Layer the work fundamental → upper, and ORDER it.** L0 foundation → L1 discovery →
   L2 lock columns ⛳ → L3 audit → L4 synthesis → L5 self-review. Each layer is a prerequisite
   for the next; never present an unordered task list. The matrix columns are an OUTPUT of L0+L1,
   locked before any cell is filled.
2. **The L0 deliverable is a ratifiable SCOPE BOUNDARY, not "understand the primitives."**
   Primitive mechanism notes are supporting work; the core L0 output is a crisp **is / is-not**
   table — especially the borders with DEFERRED modules (e.g. "the pipe/connector is in scope,
   the knowledge store + retrieval logic is the deferred memory module"; "the channel is in scope,
   the cross-agent coordination logic is the deferred orchestration module"). Getting this line
   wrong makes every downstream cell inherit the wrong shape — Day 1 is the highest-leverage day.
3. **Split anything needing OTHER PEOPLE into a separate DEPENDENCY TRACK.** Internal-team
   alignment, telemetry pulls, customer interviews, gated-product trials do NOT sit on the
   self-driven critical path. The desk track ships a complete v1 without them; dependencies
   *upgrade specific cells* when answers land. Fire every dependency request on Day 1. Tag each
   `DEP-x` with who/unblocks-what/5-day-fallback. This list may run past the window — that's fine.
4. **Grade deliverables public-v1 vs AUTHORITATIVE.** "Authoritative" is a **source grade, not a
   writing-quality grade**: v1 = built from public evidence (the own-product coverage cells are
   best-read-from-public-docs); authoritative = those cells confirmed by an internal source. The
   dependency track swaps v1 → authoritative for specific cells later.
5. **Order sub-threads inside a module fundamental → frontier too.** e.g. inside an input module:
   traditional connectors (established) → MCP (new standard on top) → Computer-Use (frontier);
   inside output: established channels/gateways → proactive/event patterns → regional coverage.
   The frontier thread is also your compression valve if the window runs tight.

> 🧩 **Capability-audit framing helper:** when the program audits an agent PLATFORM's capabilities
> (connectors, tools, channels, MCP, I/O), load `references/platform-capability-research.md`. It
> carries the **3 consumption surfaces** lens (build-direct / build-from-templates / buy-ready —
> the same primitive at three altitudes, with a different gap-test per surface), connector anatomy,
> the connector-vs-MCP content-vs-packaging distinction, and a primary-sourced "two doors, two camps"
> market map. It ALSO carries two rules that govern HOW the audit is recorded: the **strict connector
> definition** (a connector = a pre-built named-app integration in a catalog; NOT a plugin, MCP server,
> or custom-API wrap — don't over-broaden the IN-2 cell) and the **deliverable shape** (concrete
> per-cell capability + mechanism, NOT a ✅/partial/❌ mark matrix, and drop per-cell GA/preview tags —
> a user rejected marks as "useless"; use a per-provider dimension list when the matrix won't fit). Two reusable conclusions: MCP has won as the INTEROP standard universally, but the real
> differentiator is the GOVERNED CATALOG underneath it — and "buy-ready vertical agent" design is a
> VERTICAL-research question, not a capability one (carve it out of a capability audit's scope line).
> It also carries the **"Top-N connectors is a demand-intersection, never a catalog rank"** method
> (frequency-rank across vendor popularity lists + the MCP category-demand signal + consumer-audit
> exposure — never gather and rank the full 9,000-item catalogs).
>
> 🛠️ **When a registry/marketplace count or grade is JavaScript-rendered** (a static fetch returns
> the page shell without the number), load `references/javascript-rendered-data-extraction.md`. It
> carries the extraction ladder (public JSON API → the site's own aggregate/`/attributes` page →
> browser-DOM facet counts → the per-detail-page embedded data blob), the bounded-concurrent
> ThreadPoolExecutor census pattern for sampling per-item data at scale from the main session, and
> the coverage-before-distribution rule (report what FRACTION is graded before reporting the grade
> distribution — registries grade only a vetted minority).

## Output & Persistence

Land two files in `~/git/nengba-kb/work/research/` (home-relative — resolves correctly on
any machine, do NOT hardcode an environment-specific absolute path like `/mnt/c/...` or a
bare `/Users/...`):
1. `<topic>.md` — the research body in the user's standard structure, ending with a **Glossary**
   section that lists every short form used with its full name.
2. `<topic>-research-prompt.md` — the plan / dispatch (lenses chosen, dimensions, subagent
   split) for traceability and reuse. For senior/external-bound reports, include the **proof
   sheet** here (claim → source link → date → exact quote → checked).

> ⚠️ **Always ask the user for approval before writing to the knowledge base** — never
> write directly. This is a hard user rule for `nengba-kb`.

When done, report: (a) file path, (b) a 5-bullet TLDR, (c) any section where evidence was
thin and you relied on synthesis (with its source grade), and (d) confirmation that the
self-review (checkpoint 4) ran, with its gap list.

---

## Self-review against this skill (the last step — checkpoint 4)

After persisting, **do not declare done.** This step is mandatory and produces a written gap list
as its output — you cannot skip it, because the gap list IS the deliverable of this step. It has
two parts. Run BOTH.

### Part 1 — review against THIS skill's rules
Read the finished `.md` back and compare it, point by point, against this skill's **Quality
Contract**, the active lens specs (Compare / Forms / Teardown), and the **Pitfalls** list. Mark
each requirement ✅ followed or ⚠️ deviated, with a one-line reason and the fix cost. Be specific —
name the rule and where the report breaks it.

Run a **mechanical pass first** (a short `execute_code` scan) for the checks that keep slipping
through a prose read-back — these have escaped TWICE now, so automate them:
- inline source link inside every volatile / headline matrix cell (count links in matrix rows; the headline-trend and GA-vs-preview cells must be > 0)
- every short form used in the body has a Glossary entry (extract capitalized short forms, diff against the glossary list)
- the doc HAS a Glossary section as its last section
- number of per-object prose profiles == number of objects (no floating cells)
- Compare has the section(s) it should: always §1 (table + plain summary); §2 recent-3-month trend ONLY if the user opted into the trend round (if they didn't, a one-section Compare is correct — don't flag it)
- every key fact carries a source tag/date (truth contract); absence claims went through a disprove pass
Then do the judgement checks by reading: descriptive-not-prescriptive, example-before-terminology,
freshness (latest-dated sources), generalizing claims verified per-item.

### Part 2 — review against the pm-writing-gater skill
Load the **pm-writing-gater** skill (`skill_view(name='pm-writing-gater')`) and run its Stage-1 (content) Review
Checklist against the report: correctness above elegance, concept-grounding before terminology,
the post-write factual pass, audience-calibrated depth, scope discipline. This catches readability
and correctness issues the research-specific checks above don't cover. Fold its findings into the
same gap list.

### Then: fix, with the user in the loop
1. **Separate clear-cut errors from structural changes.** Fix unambiguous errors immediately (a
   missing glossary entry, a dropped citation, a stale date). For anything structural (adding prose
   profiles, re-citing every cell, reformatting the matrix), **present the gap list and let the
   user choose** before editing — honoring the user's "fix only clear-cut errors unless more is
   requested; ask before rewriting structural sections" rule.
2. ⛳ **Checkpoint 4 — user reviews the gaps, then you fix the chosen ones.** Apply exactly the edits
   the user approves, then update the dispatch/prompt file's evidence note to reflect what changed.

> Why this is its own step: a research report *feels* finished once it's written and saved, so skill
> deviations (un-cited claims, missing profiles, a bare-table Compare, a missing glossary) survive
> silently into the persisted artifact. The mechanical pass + the pm-writing-gater pass are the only
> reliable catch — a prose read-back alone has missed these twice. This is also where you fold any
> newly-found process lesson back into the relevant skill via `skill_manage(action='patch')`.

---

## Worked dispatch examples (lens composition varies every time)

| Question | Lens composition |
|---|---|
| "What is evergreen & its relation to modernization" | Concept ● → Concept-relation ● (no Discovery, no synthesis step) |
| "Agent team productized forms in vertical scenarios" | Concept ○ gate → Discovery ● → Teardown ○ (sample reps) → Forms ● → Trends ○ |
| "What is MDASH & how it differs from Evergreen" | Teardown ● (MDASH full) → Compare ● |
| "Code-assessment products & competitive analysis" | Concept ○ scope → Discovery ● → Teardown ○×N (dimension-limited) → Compare ● → Trends ● |

No two flows are identical. Step A's whole job is choosing which blocks to light and how heavy.

> 🧪 **Regression test cases:** `references/test-cases.md` holds four real user requests
> (pure concept · forms · teardown+compare · full discovery→compare), each with its
> expected flow and MUST / MUST-NOT assertions. **After ANY edit to this SKILL.md or its
> references, re-check the four cases** — a change that breaks a MUST, enables a MUST-NOT, or
> silently re-types a subject is a regression. The two edge cases (TC2 non-Compare flow, TC3
> skip-Discovery flow) specifically guard how the dimension/axis checkpoint behaves when there
> is no comparison matrix.

---

## Pitfalls

- Do NOT assume the object list — for capability/domain questions it must be *produced* by
  Discovery and ratified by the user, never presented as a given.
- Do NOT treat the Concept gate for a capability-domain audit as merely "learn the primitives."
  The CORE foundational deliverable is an explicit, user-ratifiable scope-boundary (is / is-not)
  table — and its hardest, highest-value rows are the BORDER CALLS against adjacent or DEFERRED
  modules (e.g. "the connector / ingestion PIPE is in the input module, but the knowledge store +
  retrieval logic is the deferred memory module"; "the channel / protocol is output, but the
  coordination logic is the deferred orchestration module"). Draw and ratify these border calls
  BEFORE auditing — an audit built on an unratified boundary silently mis-scopes every downstream
  cell, and the user catches it late as "you audited the wrong thing." Understanding the primitives
  is supporting work in service of the boundary, not the deliverable itself.
- Do NOT SEED discovery queries with vendor names you already know — that is confirmation,
  not discovery, and it silently hides whole categories. Map the category space, run one
  unseeded enumeration query per category, mine result BODIES (not titles), frequency-rank.
  If a query contains a product name, rewrite it. BUT if the USER hands you product names,
  include them in the candidate set by default — the unseeded rule is about queries, not about
  ignoring the user's list.
- Do NOT treat a search result as a single candidate — listicles are containers of many.
  Read the body / raw_content and harvest every name, or you under-discover by an order of
  magnitude.
- Do NOT hand the user a THIN or SERVICE-POLLUTED discovery lane as the finished set. A category
  that returns only a handful of names, or mostly consultancies/agencies instead of products, is
  usually a missed-vocabulary signal, not a genuinely small market. Fire 1–2 supplemental targeted
  (still unseeded) enumeration queries for that niche and re-rank BEFORE the checkpoint. (Observed:
  a modernization lane came back with ~9 names, several of them service firms; two targeted queries
  on the concrete sub-capabilities surfaced the real product set.)
- Do NOT scope Discovery to a property LABEL without gating it first. If the market is named
  by a property word ("agentic", "continuous", "self-healing", "managed"), Concept-gate that
  word and bucket candidates into passes / fails / partial BEFORE diverging — especially the
  ongoing-STATE (must stay true over time) vs one-time-EVENT (single action or snapshot) split.
  Wrong label = wrong superset = wasted run.
- Do NOT let Compare collect raw data or deep-dive a single object — that's Teardown.
  Compare only arranges Teardown results.
- Do NOT ship a teardown that is a row of generic verb-cells. Each object needs a 3–5
  sentence prose profile that strictly follows the user-confirmed dimensions (same shape for
  every object). IF the user opted into the recent-3-month trend round at the checkpoint, ALSO add
  a short dated summary of its new features from the last 3 months, pulled in a SEPARATE search
  round against the object's official "What's New"/release-notes page (not grabbed in passing
  during the dimension research). If they did not opt in, skip the recent-features summary. Write
  the profile BEFORE it becomes a matrix cell. No floating cells.
- Do NOT ship a Compare that is a bare table. It always needs (1) the comparison table with a
  plain-English summary that explains it so the reader gets it without decoding cells. (2) The
  recent-3-month trend summary is added ONLY when the user opted into the trend round — otherwise
  Compare is just Section 1. Do NOT run the extra trend search, or invent a trend section from
  memory, when the user didn't ask for it.
- Do NOT spell every full name out everywhere, and do NOT coin informal short forms ("deps").
  Spell each real acronym out on FIRST use with the short form in parentheses, use the short form
  after (matrix cells included), and add a Glossary section at the END listing every short form
  with its full name. Every short form in the body — including matrix-cell-only ones — needs a
  glossary entry.
- Do NOT lock comparison dimensions without an axis-coverage check when the user named the scope as
  explicit axes. Map each column to a stated axis; an axis covered by only one thin column (or none)
  is silent under-scoping. The report answers its columns but misses half the question, and the user
  catches it late ("you missed the alerting axis"). Fix coverage BEFORE locking, not after the report
  ships. (Observed: a token-feature comparison locked 9 columns that loaded 7 onto two axes — visibility
  and cost — and left management and observability/alerting with one column each; the entire
  alerting/budgets dimension was absent until the user flagged it.)
- Do NOT deep-teardown all N competitors — that drowns you. Dimension-limited teardown for
  all, full teardown only for the #1 rival if needed.
- Do NOT invent forms/matrix cells that "look plausible" — every form needs a real
  representative, every cell needs evidence, or it gets deleted.
- Do NOT skip the plan checkpoint — picking the wrong lenses wastes the whole run.
- Do NOT skip the final self-review (checkpoint 4), and do NOT run it as a prose-only read-back —
  that has missed un-cited cells and unexplained short forms twice. Run BOTH parts: Part 1 (this
  skill's rules, with a mechanical `execute_code` scan for citations-in-cells, glossary coverage,
  profile count, two-section Compare) and Part 2 (load the pm-writing-gater skill and run its
  checklist). Produce a written followed/deviated gap list, fix clear-cut errors, let the user
  choose on structural ones.
- Do NOT trust a fact you didn't source to an official page and (for volatile facts) couldn't
  copy a real line from or corroborate with a second source. Official source first; blogs only
  when the official page is silent; copy the exact sentence rather than paraphrasing from memory;
  two independent sources for GA/preview, prices, "just shipped", headline numbers. A smooth
  report on fabricated or stale facts is the worst failure this skill has. Delegated subagents
  must return a link + the copied sentence per fact, or you re-verify it yourself.
- Do NOT search or run a Teardown without the Tavily web-access skills loaded (`tavily-search` for
  search, `tavily-extract` for fetch). There is NO skill named `web-access` in this user's library —
  do not try to load that name. The worst silent failure is a Teardown with no working web tool —
  especially a delegated subagent that quietly falls back to training knowledge and returns
  confident-but-unverified pricing/features. Use Tavily by default over the built-in web tools, give
  delegated children the `web` toolset, and verify volatile cells carry real source URLs.
- Do NOT trust subagent Discovery output without checking rows carry real URLs — a
  delegated subagent can return narrated/literal tool-call text instead of executing the
  search. Verify the tool layer (not the network) and fall back to the curl+DDG pipeline
  in `references/discovery-search-tooling.md`.
- Do NOT dispatch Teardown subagents without a hard budget, a confirmed web toolset, and a
  self-check of the volatile axes. An uncapped child times out and returns nothing; a child with
  no web tool returns training-knowledge guesses dressed as fact. Always cap (\"≤N searches, start
  writing by minute M\"), put `web` in its toolset, and re-verify pricing + last-3-month features
  yourself from primary pages even when the child \"succeeds.\" See the Teardown lens guards.
- Do NOT assert "Vendor lacks X" in a gap/enhancement analysis without first running a
  "disprove your own gap" pass — search for evidence the feature ALREADY exists, using the
  vendor's own vocabulary, and confirm absence against a PRIMARY source. Expect to retract
  ~half your first-draft gaps. And do NOT trust GA-vs-preview or "shipped" claims from
  secondary blogs — read the vendor's own dated doc; primary wins on every conflict. Full
  playbook (recency check, disprove pass, real/closed/greenfield triage, don't-rubber-stamp,
  doc-family conventions) → `references/verification-and-recency.md`.
- Do NOT cross from DESCRIPTIVE positioning into PRESCRIPTIVE strategy in Compare. Stating where
  the differences are, who's strong/weak and why (facts from the table) is required. Telling the
  user what their product should do about it — bets, "defensible wedge", "consume the rival as a
  dependency", "don't stake value on X", team handshakes — is not the skill's output. The PM
  draws the strategy; the skill delivers the objective substrate. This is the easiest rule
  to violate because a sharp Compare *feels* like it should end with a recommendation. It must not.
  **Exception:** an EXPLICIT user follow-up asking for gaps/enhancements makes prescriptive output
  the requested deliverable — see `references/competitive-gap-analysis.md`.
- Do NOT assert a competitor LACKS a feature without trying to DISPROVE it first. **This rule applies to EVERY object, not just competitors — including the product the report is built around, or any object you think you know best.** That familiar object is exactly where an absence claim silently skips the disprove search, because certainty suppresses the fetch (see the Golden Data Rule at the top of this file). Absence/negative
  claims ("X has no Y", "only Foundry does Z") are the highest-risk cells in the report and the ones
  stale secondary sources get wrong. Before writing a gap: run a search aimed at finding the feature
  EXISTS, resolve it against a PRIMARY vendor source, and for "GA vs preview / just shipped" read the
  vendor's own doc page (status flips fast; when a blog and the vendor doc disagree, the doc wins).
  In the motivating run 3 of 6 claimed gaps were false — the product already had them. Full pattern →
  `references/competitive-gap-analysis.md`.
- Do NOT label a missing feature a Foundry-specific gap without checking whether RIVALS have it
  either. If none do, it's GREENFIELD (a first-mover bet), not a catch-up hole — opposite framing.
  **But the catch-up-vs-greenfield verdict is itself an absence claim — verify it per-rival against
  each rival's PRIMARY agent-runtime/quota doc, and source any CORRECTION to a primary page too, not a
  secondary aggregator or a Tavily synthesized `answer`.** (Observed twice in one session: "per-agent
  control is greenfield" was wrong — AWS ships it; then the FIX "GCP enforces 30/min per agent" was ALSO
  wrong — GCP's real limit is 90/min per project/region, not per agent. Decompose coarse capabilities:
  per-run limits = catch-up vs AWS, per-agent cumulative dollar budget = the real greenfield.)
  And do NOT list every axis where the vendor trails as a gap to invest in: an axis blocked by a
  national mandate, a geography/platform you don't own, a different buyer segment, or a business-model
  choice is a STRUCTURAL NON-GAP — carve it out explicitly as "do not chase," never silently omit it.
  Triage is three-way (catch-up / greenfield / structural non-gap), not two. When auditing your own
  conclusion, prefer the defensible "complete / at parity" over the rebuttable "ahead of rivals," and
  tier your why-invest evidence (a hobbyist-harness signal proves the problem is real, NOT that
  enterprises will pay). All of these → `references/competitive-gap-analysis.md`.
- Do NOT protect a prior headline conclusion when the user later adds new dimensions to an
  already-shipped comparison. A late-added dimension can overturn the original verdict, and the
  honest move is to rewrite the takeaway + plain summary to match the new picture — never preserve
  the flattering old story for consistency. (Observed: a platform comparison shipped with "Foundry
  is the most complete — strong on all 7 aspects." The user then asked to add vertical-sector
  support, real-time multimodal, and channel distribution as aspects 8–10. On those three Foundry
  was middle-of-pack, and verticals was the FIRST aspect where it clearly trailed. The takeaway had
  to flip from "leads everywhere" to "leads the core 1–7, not the leader on 8–10." The user wants
  the accurate read, not a stable one — re-score every object on the new axes and let the verdict
  move.) Adding dimensions iteratively is a normal user pattern, not a redo: expect it, and when you
  propose columns, also surface the out-of-scope axes regional/vertical players compete on (see
  `references/verification-and-recency.md` §5) so fewer dimensions arrive late.
- Do NOT write to nengba-kb without explicit approval.
- **On EVERY run, load `references/verification-and-recency.md`** (always-on fact-quality, per the
  Golden Data Rule at the top of this file: never use memory, always fetch the latest yourself and
  date it, vendor official blog/doc is the source of truth, other public articles only when no
  official page exists, and the sole exception is data the user gave explicitly up front — double-
  confirm even then). It carries: read the doc's last-updated date, mark general-availability vs
  preview from the official page, primary beats blogs, re-verify renamed products, copy the real
  line, propagate a corrected fact across all companion docs + link-check. The live-product
  mechanics weigh most where status flips monthly, but the fetch-fresh default is universal. When
  the user then asks a GAP / enhancement
  / "confirm my conclusion" follow-up, ALSO load `references/competitive-gap-analysis.md` (judgment-
  quality: disprove your own gap, catch-up vs greenfield vs structural non-gap, present vs future gap,
  ahead-vs-parity, tier your evidence, complete who-wins evidence per rival, judge don't rubber-stamp,
  descriptive→prescriptive).
  Clean split: verification = is the FACT true; gap = is the CONCLUSION sound.
