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

This is a multi-file skill (`SKILL.md` + `references/test-cases.md` + `references/discovery-search-tooling.md`)
with numbered invariants that other sections cross-reference. Edits here have a habit of leaving
silent breakage. Four hazards earned the hard way:

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
| **Review** | candidate list + recommended dimensions | user-edited tools AND locked dimensions | ⛳ 2+3 — rows + columns together |
| **Teardown** (per tool) | locked tools + locked dimensions | one prose profile per tool (fills the dimensions) + a dated last-3-months feature list | — |
| **Compare** | all teardown profiles | §1 table + plain summary · §2 recent-3-month trend summary | — |
| **Trends** (optional) | the field + Compare output | 5–7 named market trajectories | — |
| **Persist** | the finished report | two files in the research folder | ⛳ approval before writing |
| **Self-review** | the persisted report + this skill | a gap list (followed / deviated), then fixes | ⛳ 4 — user reviews gaps before you fix |

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
   dimensions in one pass. **Confirmed dimensions are locked here, before Teardown.**

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

> 🔧 **Retrieval reliability:** Discovery lives or dies on clean rows. Use the **Tavily Search
> API** (`TAVILY_API_KEY` in `~/.hermes/.env`) via Python `urllib` for batch queries — clean
> JSON, no shell-escaping traps. Full playbook (request shape, the body-mining + frequency-rank
> code, fallbacks, and "ratify rows before spending evidence effort" sequencing) →
> `references/discovery-search-tooling.md`.
>
> 🌐 **ALWAYS load the `web-access` skill for any web search/fetch — in BOTH Discovery and
> Teardown.** Call `skill_view(name='web-access')` before searching so you use a guaranteed-available
> retrieval path (its layered model: static `web_search`/`web_extract`/`curl` + `r.jina.ai` reader →
> browser layer only if needed). This is not optional polish — it prevents the single worst silent
> failure of this skill: **running a Teardown with no working web tool at all.** When the Teardown is
> delegated to subagents, the child often does NOT inherit a usable search tool, so it quietly falls
> back to training knowledge and returns confident-but-unverified pricing/features. Before trusting
> any delegated profile, (a) give the child the `web` toolset AND tell it to load `web-access`, and
> (b) verify the volatile axes (pricing, last-3-month features) carry real source URLs — if they
> don't, re-fetch those cells yourself from the main session via `web-access` Layer 0 (curl +
> `r.jina.ai`, processed inside `execute_code` to keep raw HTML out of context).

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
> **Plus (only when the downstream synthesis is Compare/Trends): summarize each object's new
> features from the last ~3 months.** On top of the fixed dimensions, give each object a short
> dated list of what it shipped recently (named feature + month + citation). This is collected
> here in Teardown so Compare can read it as a trend. **Skip it for a Forms flow** — a forms
> survey of sampled representatives doesn't consume recent-features data, so collecting it there
> is over-spec.
>
> All of this — the dimension profiles AND the recent-features summary — is the prepared input
> for the next step. Write the prose profile first, then the matrix cell is just its compression.

> 🛰️ **Delegating Teardown to subagents — three guards (each earned the hard way).** Parallel
> per-object subagents are the right pattern, but a naive dispatch fails silently in two ways:
> 1. **Budget or you lose everything.** A research subagent with no cap will over-research and hit
>    the wall (e.g. 600s / 50 calls), and a timed-out child returns **NOTHING** — all its work is
>    discarded. Give every Teardown child a HARD cap: \"≤N searches, lean on training knowledge for
>    stable facts, **start writing your answer by minute M** no matter what.\" A complete, slightly
>    thinner profile beats a perfect one that times out to zero.
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
Compare always outputs **two sections, never a bare table** — a table alone is not a comparison.

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
5. **Section 2 — recent-3-month trend summary, built from the Teardown recent-features data.**
   Take the "new features in the last ~3 months" that Teardown collected for each object, put them
   together, and read them as one picture: what is the whole market adding right now? Where is it
   heading? A summary of direction, not just a list of releases.

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
  but must be **argued, not asserted**. Prefer primary (vendor doc) over secondary commentary. This applies to **matrix/table cells**
  too — link the source ON the verified cell (the pricing row, the recent-feature row). Do NOT
  defer citations to a footnote or an end "evidence note": parked sources read as verified-looking
  but unlinked, and footnoting is the easy way to violate the inline rule when the claims live in a
  dense comparison table (observed: a landscape report shipped pricing + feature cells with sources
  collected at the bottom instead of linked per cell).
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
- **Full names, not abbreviations or short forms.** Spell terms out: "dependencies" not "deps",
  "GitHub Advanced Security" not "GHAS", "Software Composition Analysis" not "SCA" on first use,
  "Static Application Security Testing" not "SAST" on first use. Acronyms may follow in
  parentheses on first mention and be reused, but never coin informal shortenings. Matrix cells
  and prose alike — clarity over compression. A reader should never have to decode a stub.

---

## Output & Persistence

Land two files in `~/git/nengba-kb/work/research/` (home-relative — resolves correctly on
any machine, do NOT hardcode an environment-specific absolute path like `/mnt/c/...` or a
bare `/Users/...`):
1. `<topic>.md` — the research body in the user's standard structure.
2. `<topic>-research-prompt.md` — the plan / dispatch (lenses chosen, dimensions, subagent
   split) for traceability and reuse.

> ⚠️ **Always ask the user for approval before writing to the knowledge base** — never
> write directly. This is a hard user rule for `nengba-kb`.

When done, report: (a) file path, (b) a 5-bullet TLDR, (c) any section where evidence was
thin and you relied on synthesis.

---

## Self-review against this skill (the last step — checkpoint 4)

After persisting, **do not declare done.** Run one final pass: read the finished `.md` back and
compare it, point by point, against this skill's **Quality Contract**, the active lens specs
(Compare/Forms/Teardown), and the **Pitfalls** list. The goal is to catch instructions that were
not well followed *before* the user has to.

1. **Produce a gap list, not a vibe check.** For each requirement, mark ✅ followed or ⚠️ deviated,
   with a one-line reason and the fix cost. Be specific and honest — name the rule and where the
   report breaks it. Common misses to check explicitly: inline citations on every pricing/feature/stat
   claim; acronyms spelled out on first use; per-object prose profile present before each matrix cell;
   Compare is two sections (table + plain summary, then recent-3-month trend), not a bare table;
   stayed descriptive, not prescriptive; example-before-terminology.
2. **Separate clear-cut errors from structural changes.** Fix unambiguous errors immediately (a
   missing acronym expansion, a dropped citation). For anything structural (adding prose profiles,
   re-citing every cell, reformatting the matrix), **present the gap list and let the user choose**
   before editing — this honors the user's "fix only 明确错误 unless more is requested; ask before
   rewriting structural sections" rule.
3. ⛳ **Checkpoint 4 — user reviews the gaps, then you fix the chosen ones.** Apply exactly the edits
   the user approves, then update the dispatch/prompt file's evidence note to reflect what changed
   (e.g. "pricing now cited inline").

> Why this is its own step: a research report *feels* finished once it's written and saved, so skill
> deviations (un-cited claims, missing profiles, bare-table Compare) survive silently into the
> persisted artifact. A forced read-back against the contract is the only reliable catch. This is
> also where you fold any newly-found process lesson back into the relevant skill via
> `skill_manage(action='patch')`.

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
  every object), plus a short dated summary of its new features from the last ~3 months,
  BEFORE it becomes a matrix cell. No floating cells.
- Do NOT ship a Compare that is a bare table. It must have two sections: (1) the comparison
  table with a plain-English summary that explains it so the reader gets it without decoding
  cells, and (2) a recent-3-month trend summary built from the Teardown recent-features data.
- Do NOT use abbreviations or coin short forms ("deps", "GHAS", bare "SCA"/"SAST" on first
  use). Spell terms out; acronym in parentheses on first mention, then reuse. Applies to
  matrix cells too.
- Do NOT silently pick the comparison dimensions — that's the user's call, confirmed at
  checkpoint 2+3 (shown together with the candidate tool list, right after Discovery, BEFORE
  Teardown). Offer a recommended axis; let them edit/add/drop (this is also where business vs
  technical scope is set). Teardown never starts without the locked dimension set.
- Do NOT deep-teardown all N competitors — that drowns you. Dimension-limited teardown for
  all, full teardown only for the #1 rival if needed.
- Do NOT invent forms/matrix cells that "look plausible" — every form needs a real
  representative, every cell needs evidence, or it gets deleted.
- Do NOT skip the plan checkpoint — picking the wrong lenses wastes the whole run.
- Do NOT skip the final self-review (checkpoint 4). A persisted report *feels* done, so un-cited
  claims, missing per-object profiles, a bare-table Compare, and unexpanded acronyms survive
  silently into the saved artifact. Read the `.md` back against the Quality Contract + Pitfalls,
  hand the user a followed/deviated gap list, fix clear-cut errors, and let the user choose on
  structural ones.
- Do NOT search or run a Teardown without the `web-access` skill loaded. The worst silent failure
  is a Teardown with no working web tool — especially a delegated subagent that quietly falls back
  to training knowledge and returns confident-but-unverified pricing/features. Load `web-access`,
  give delegated children the `web` toolset, and verify volatile cells carry real source URLs.
- Do NOT trust subagent Discovery output without checking rows carry real URLs — a
  delegated subagent can return narrated/literal tool-call text instead of executing the
  search. Verify the tool layer (not the network) and fall back to the curl+DDG pipeline
  in `references/discovery-search-tooling.md`.
- Do NOT dispatch Teardown subagents without a hard budget, a confirmed web toolset, and a
  self-check of the volatile axes. An uncapped child times out and returns nothing; a child with
  no web tool returns training-knowledge guesses dressed as fact. Always cap (\"≤N searches, start
  writing by minute M\"), put `web` in its toolset, and re-verify pricing + last-3-month features
  yourself from primary pages even when the child \"succeeds.\" See the Teardown lens guards.
- Do NOT cross from DESCRIPTIVE positioning into PRESCRIPTIVE strategy in Compare. Stating where
  the differences are, who's strong/weak and why (facts from the table) is required. Telling the
  user what their product should do about it — bets, "defensible wedge", "consume the rival as a
  dependency", "don't stake value on X", team handshakes — is not the skill's output. The PM
  draws the strategy; the skill delivers the objective substrate. This is the easiest rule
  to violate because a sharp Compare *feels* like it should end with a recommendation. It must not.
- Do NOT write to nengba-kb without explicit approval.
