---
name: deep-research
description: "Composable product/market/concept research for PMs — assemble lenses (concept, discovery, teardown, compare, forms, trends, strategy) to fit any research question, with human checkpoints and an evidence-graded output."
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

## The 7 Lenses (single responsibility each — do not overlap them)

| Lens | The one question it answers | Object count | Output shape |
|---|---|---|---|
| 🔍 **Concept** | "What does this term/idea *mean*?" | 1 abstract idea | definition + boundary + relation to neighbors |
| 🧭 **Discovery** | "Who/what should I even study?" | unknown → set | a deduped, classified candidate list |
| 🗺️ **Pattern→Forms** | "What product *forms* does this pattern take?" | a set | clustering along a FORM axis, not a vendor list |
| 🔬 **Teardown** | "How does this single object work inside?" | 1 concrete thing | deep analysis (depth/width tunable) |
| ⚖️ **Compare** | "How do these differ; who's stronger?" | 2+ analyzed objects | matrix + positioning conclusion |
| 📈 **Trends** | "How is this evolving over time?" | a field | 5–7 named, argued trajectories |
| 🎯 **Strategy** | "So what — for MY product?" | — | defensible wedge + concrete bets |

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

## The 3 Human Checkpoints (stop and get user ratification)

Three things must be ratified by the user. **Checkpoints 2 and 3 are presented TOGETHER**, in one
review right after Discovery — so the comparison dimensions are always confirmed before Teardown.

1. **After Step A — the plan.** Which lenses you'll light up and how heavy. User confirms/adjusts.
2. **After Discovery — the object set (rows).** The classified candidate list — *who* to study.
   User prunes/adds.
3. **With checkpoint 2 — the dimensions (columns).** The recommended comparison dimensions —
   *what* to compare on. User edits/finalizes. Presented in the SAME review as checkpoint 2:
   prune/add the tools and finalize the dimensions in one pass. **Locked here, before Teardown** —
   never after, because Teardown is filled against these exact dimensions.

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
   - a *capability/pattern* ("how is X productized") → Discovery → Pattern→Forms
   - a *capability domain* ("who does X") → Discovery → Compare
2. **Is the object set known?** If no → Discovery is required. If yes → skip Discovery.
3. **Which lenses, how heavy?** (● heavy / ○ light / — none)

Example plan reply (for "what is MDASH and how does it differ from Evergreen"):
> Subject: one unfamiliar product (MDASH) + one known object (Evergreen). Objects are
> already fixed → no Discovery. Plan: Teardown MDASH (full) → Compare the two → Strategy
> for Evergreen's positioning. Proceed?

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
| **Strategy** | everything above | the defensible wedge + 3 near-term / 2 long-term bets | — |
| **Persist** | the finished report | two files in the research folder | ⛳ approval before writing |

Lighter flows drop steps (a single-product teardown skips Discovery), but the input→output
contract per step never changes. Step A decides which rows of this table light up.

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

### 🗺️ Pattern→Forms
The differentiator from a plain competitor list: **re-cluster the candidate set along a
FORM axis**, not by company. Each form must be filled with a **real representative** — if a
form can't be populated with a real example, delete it (never invent plausible-looking
forms). Output: a forms table (form | defining trait | representative | maturity).

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
> **Plus: summarize each object's new features from the last ~3 months.** On top of the fixed
> dimensions, give each object a short dated list of what it shipped recently (named feature +
> month + citation). This is collected here in Teardown so Compare can read it as a trend.
>
> All of this — the dimension profiles AND the recent-features summary — is the prepared input
> for the next step. Write the prose profile first, then the matrix cell is just its compression.

### ⚖️ Compare (consumes Teardown results)
1. Object set — from Discovery (checkpoint 2).
2. Dimension axis — user-ratified (checkpoint 3).
3. Lay the N teardown results side by side → build the matrix (rows = objects/dimensions,
   cells = ✅/partial/❌ + a one-line "how": rule/AST/dataflow/LLM/runtime, + evidence).
4. Read the **pattern** and write a **stance-bearing positioning conclusion** (who's deep,
   who's shallow, where AI pulls someone ahead). Optionally deep-Teardown the #1 rival while
   the rest stay dimension-limited.
Does NOT collect raw data itself — it only arranges what Teardown produced.

> **Compare = two sections, never a bare table.** A table alone is not a comparison. The
> Compare step must always produce both of these:
>
> **Section 1 — Comparison table + a plain-English summary that explains it.** Lay the objects
> against the confirmed dimensions, then write a clear summary in plain words that walks the
> reader through the table: what the rows show, where the real differences are, who is strong
> or weak and why. The reader should understand the table from your summary WITHOUT having to
> decode the cells one by one.
>
> **Section 2 — Recent-3-month trend summary, built from the Teardown recent-features data.**
> Take the "new features in the last ~3 months" that Teardown collected for each object, put
> them together, and read them as one picture: what is the whole market adding right now? Where
> is it heading? This is a summary of direction, not just a list of releases.

### 📈 Trends (the vertical/time axis)
What horizontal comparison can't give: how the field is **evolving**. Identify **5–7 named,
argued trajectories** (not asserted). Cover both "what existing tools are adding now" (cited,
prefer recent) and "what the shift unlocks that wasn't possible before."

### 🎯 Strategy (always land here)
Synthesize everything into product input: capability gaps to close, capabilities to add, the
**defensible wedge** (what rivals are NOT doing), and **3 near-term + 2 long-term bets**. This
is heavier than a soft "implications" closer — it reaches stance-level recommendations (e.g.
"don't stake value on Pillar 1; consume the rival as a dependency; handshake with their team").

---

## Quality Contract (applies to ALL lenses)

- **Stance first, no info-dumps.** Produce opinionated conclusions, not feature catalogs.
- **Example before terminology** — ground a concept with a concrete case *before* naming it.
- **Evidence grading**: product/feature/stat claims MUST cite a primary source (vendor doc,
  release notes, case study), inline as markdown links. Trends/synthesis may be uncited POV
  but must be **argued, not asserted**. Prefer primary (vendor doc) over secondary commentary.
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

Land two files in `/mnt/c/Users/taoxu/Downloads/git/nengba-kb/work/research/` (the user's
actual repo lives under the WSL Windows mount — do NOT use a bare `/Users/...` macOS path):
1. `<topic>.md` — the research body in the user's standard structure.
2. `<topic>-research-prompt.md` — the plan / dispatch (lenses chosen, dimensions, subagent
   split) for traceability and reuse.

> ⚠️ **Always ask the user for approval before writing to the knowledge base** — never
> write directly. This is a hard user rule for `nengba-kb`.

When done, report: (a) file path, (b) a 5-bullet TLDR, (c) any section where evidence was
thin and you relied on synthesis.

---

## Worked dispatch examples (lens composition varies every time)

| Question | Lens composition |
|---|---|
| "What is evergreen & its relation to modernization" | Concept ● → Concept-relation ● → Strategy ○ (no Discovery, no matrix) |
| "Agent team productized forms in vertical scenarios" | Concept ○ gate → Discovery ● → Pattern→Forms ● → Teardown ○ (sample reps) → Strategy ○ |
| "What is MDASH & how it differs from Evergreen" | Teardown ● (MDASH full) → Compare ● → Strategy ● |
| "Code-assessment products & competitive analysis" | Concept ○ scope → Discovery ● → [Teardown ○×N dimension-limited] → Compare ● → Trends ● → Strategy ● |

No two flows are identical. Step A's whole job is choosing which blocks to light and how heavy.

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
- Do NOT trust subagent Discovery output without checking rows carry real URLs — a
  delegated subagent can return narrated/literal tool-call text instead of executing the
  search. Verify the tool layer (not the network) and fall back to the curl+DDG pipeline
  in `references/discovery-search-tooling.md`.
- Do NOT write to nengba-kb without explicit approval.
