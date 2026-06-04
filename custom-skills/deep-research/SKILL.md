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

These sit exactly at the 3 decisions where, if you get it wrong, everything downstream is wasted:

1. **After Step A — the plan.** Show which lenses you'll light up and how heavy. User confirms/adjusts.
2. **After Discovery — "who"** (the object set). Present a classified candidate list; user prunes/adds.
3. **Before Compare — "what"** (the dimension axis). You *suggest* dimensions from Concept+Discovery
   results; **user finalizes**. Never let the skill silently decide what to compare.

> Checkpoints 2 and 3 are symmetric: one fixes the **rows** (objects), one fixes the
> **columns** (dimensions). The dimension axis drives BOTH lenses at once: for Teardown it
> defines *what to collect*; for Compare it defines *what to lay side by side*. One checkpoint
> keeps "what we collect" and "what we compare" aligned — no mismatch.
>
> The dimension checkpoint is also where **business vs technical scope** gets decided. Do NOT
> preset business dimensions (pricing, target segment, GTM, funding). Offer them; the user adds
> them if they care, drops them if they only want product capability.

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
Use `delegate_task` to run **parallel subagents, each on a DIFFERENT entry point** (avoids
single-source bias). Typical entries: vendor/product catalogs, framework/tech ecosystems,
analyst/funding/news, academic→productized. Each subagent returns **structured rows only**
(name + one-line what + scenario + source URL), never raw pages. Then main session:
1. **Dedup** (same item from multiple sources → merge, confidence↑).
2. **Filter** against the Concept inclusion/exclusion criteria.
3. **Classify** into 3–5 meaningful categories.
4. ⛳ **Checkpoint 2**: hand the user the classified candidate list; they prune/add.

> Pro tip: a sharp Concept lens used as a *gate* first (inclusion/exclusion criteria)
> dramatically improves Discovery precision — it stops the divergence from dragging back
> near-misses (e.g. single-agent tools when you wanted agent *teams*).

### 🗺️ Pattern→Forms
The differentiator from a plain competitor list: **re-cluster the candidate set along a
FORM axis**, not by company. Each form must be filled with a **real representative** — if a
form can't be populated with a real example, delete it (never invent plausible-looking
forms). Output: a forms table (form | defining trait | representative | maturity).

### 🔬 Teardown (single object; depth/width tunable)
Run with parameters: `Teardown(object, dimensions, depth)`.
- **Full**: what it is (one-line) → components → mechanism/flow → user journey/cohorts →
  architecture/deployment → boundary/maturity.
- **Dimension-limited (profiling for a compare)**: fill ONLY the agreed dimension axis,
  each cell with an evidence URL. Run these in **parallel subagents, one per object**, each
  answering the same fixed dimensions → one structured row per object.
Does NOT compare to others (that's Compare's job).

### ⚖️ Compare (consumes Teardown results)
1. Object set — from Discovery (checkpoint 2).
2. Dimension axis — user-ratified (checkpoint 3).
3. Lay the N teardown results side by side → build the matrix (rows = objects/dimensions,
   cells = ✅/partial/❌ + a one-line "how": rule/AST/dataflow/LLM/runtime, + evidence).
4. Read the **pattern** and write a **stance-bearing positioning conclusion** (who's deep,
   who's shallow, where AI pulls someone ahead). Optionally deep-Teardown the #1 rival while
   the rest stay dimension-limited.
Does NOT collect raw data itself — it only arranges what Teardown produced.

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
- **Tables for comparison, prose for analysis.** Active voice, concise, no filler conclusions.
- **No explicit level labels** in prose; say "machine learning"/"deep learning" etc. directly.

---

## Output & Persistence

Land two files in `/Users/taoxu/git/nengba-kb/work/research/`:
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
- Do NOT let Compare collect raw data or deep-dive a single object — that's Teardown.
  Compare only arranges Teardown results.
- Do NOT silently pick the comparison dimensions — that's checkpoint 3, the user's call.
  Offer a suggested axis, let them add/drop (this is also where business vs technical scope
  is set).
- Do NOT deep-teardown all N competitors — that drowns you. Dimension-limited teardown for
  all, full teardown only for the #1 rival if needed.
- Do NOT invent forms/matrix cells that "look plausible" — every form needs a real
  representative, every cell needs evidence, or it gets deleted.
- Do NOT skip the plan checkpoint — picking the wrong lenses wastes the whole run.
- Do NOT write to nengba-kb without explicit approval.
