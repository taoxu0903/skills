---
name: pm-writing-gater
description: >-
  The single gate a PM doc passes through before it ships — two stages in order.
  Load this whenever you write or rewrite a PM doc for Ken (PRDs, product specs,
  roadmaps, framing docs, design briefs), or when he says the writing is "wrong",
  "too simple", "too obscure", "doesn't read like the leader's docs", "hard to
  read", or asks to "polish the framing" / "gate this doc". STAGE 1 (content) —
  is every claim true, grounded, and in-scope? STAGE 2 (framing) — does the
  English land in the right register (Tina / Foundry voice), with AI-tells
  stripped? Run Stage 1 before Stage 2. Replaces the old writing-quality +
  writing-gater pair.
version: 1.0.0
author: taoxu
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [writing, framing, english, register, correctness, anti-ai-slop, pm-docs]
    related_skills: [product-spec-writing, humanizer, deep-research]
---

# PM Writing Gater — the one gate a PM doc passes before it ships

A finished PM doc passes through **one gate with two stages, run in order**:

1. **Stage 1 — CONTENT.** Is every claim true, grounded, and in-scope? Rhetorical
   smoothness can silently override factual accuracy, so this is checked first and
   deliberately. (Was the standalone `writing-quality` skill.)
2. **Stage 2 — FRAMING.** With content settled, does the English *read* right —
   register, word choice, AI-tells, expression discipline — so it lands like
   Tina's and the Foundry framing docs? (Was the standalone `writing-gater` skill.)

Order matters: **never polish framing on top of a wrong claim, and never
re-litigate a fact during the framing pass.** If Stage 2 turns up a factual
doubt, kick it back to Stage 1 (or flag it to Ken) — don't silently rewrite
content under the banner of "framing".

> Scope: this gate is for **Ken's PM docs** — formal peer-register framing. It is
> NOT a general-purpose "any writing" checker and NOT a fact *research* pass (that
> is the writing stage / `deep-research`). It assumes the doc is drafted; it makes
> it correct, then makes it read well.

═══════════════════════════════════════════════════════════════════
# STAGE 1 — CONTENT (correctness before elegance)
═══════════════════════════════════════════════════════════════════

Run this FIRST. These rules exist because coherence and rhetorical smoothness can
silently override factual accuracy if you don't check deliberately.

## 1 — Correctness above everything else
Content correctness is the highest priority. It outranks narrative elegance,
rhetorical devices ("they all share X", "the common thread is Y"), flow, and
conciseness. A sentence that is smooth but wrong is worse than one that is awkward
but true.

**Specific failure mode to guard against:** reaching for a unifying claim to make
the writing feel tighter without verifying it holds for every item it covers.
Before writing any generalizing sentence, check it against each individual case.

## 2 — Concept grounding before terminology
Before introducing any concept or technical term, ask: can a reader understand
this without prior knowledge?
- If yes: introduce it directly.
- If no: ground it first with a concrete, relatable example or scenario, THEN name
  the term, THEN give the precise definition.

Anti-patterns: defining a term using other undefined terms; opening a section with
jargon and explaining it afterward; "the intuition is…" as a substitute for
actually building the intuition.

## 3 — Post-write factual review (mandatory)
After drafting, do a full pass before handing to Stage 2:
- **Factual accuracy** — every factual sentence states a true fact; numbers,
  dates, names, attributed quotes correct; generalizing claims ("all three share
  X") hold for *every* item — check each.
- **Concept consistency** — a term defined one way in section A means the same in
  section B; each concept stays in its correct scope.
- **Reader comprehension** — every term a new reader wouldn't know is explained or
  grounded before use; no sentence that sounds authoritative but says nothing
  verifiable.
- **Structural logic** — each section follows from the previous; cross-references
  ("as covered in §3") actually point where the content lives.

## 4 — Audience-calibrated depth
State the audience's knowledge level explicitly at the start, then apply it
consistently. For each major concept: what does this audience already know? What
can be assumed vs must be explained? What analogy lands vs feels condescending? A
concept needing no explanation for one audience may need three paragraphs for
another.

## 5 — Scope discipline
Each doc has a defined scope. Before writing any section, ask: does this belong
here, or in a different doc? For a standalone doc, stay inside the declared topic
boundary. For a multi-part series, forward-point to later parts ("covered in Part
N") instead of explaining them here; reference earlier parts back instead of
re-explaining at the same depth.

## Stage 1 checklist (clear before moving to Stage 2)
- [ ] Every factual sentence is true and verifiable
- [ ] Every generalizing claim checked against all items it covers
- [ ] Every new term grounded with a concrete example before being named
- [ ] No undefined terms used to define other terms
- [ ] Scope respected — no content that belongs in a different doc
- [ ] Cross-references point to where content actually lives
- [ ] Audience knowledge level correct and consistent throughout

═══════════════════════════════════════════════════════════════════
# STAGE 2 — FRAMING (English register pass)
═══════════════════════════════════════════════════════════════════

Now the content is correct and settled. This stage only fixes how the English
*reads*: register, word choice, AI tells, expression discipline. Do **not**
re-litigate scope, restructure sections, or fact-check here. If you catch a
factual problem, kick it back to Stage 1 — don't silently rewrite content.

**Before rewriting anything substantial, read `references/gold-standard.md`.**
Those annotated excerpts from Tina's and the Foundry framing docs are the *ear* —
the register you are calibrating toward. The rules below are how to hit it; the
gold standard is what "hit" sounds like.

## The one target: write for a smart peer

Every rule here collapses into a single audience. You are writing for a **smart
peer in the field** — not teaching a novice, not performing for a review board.
Ken's two recurring complaints are the two ways to miss this target:

- **Too simple** → you wrote for a novice: vague verbs, no specifics, filler.
- **Too obscure** → you wrote for a review board: nominalization soup, invented
  jargon, no reader in mind.

One idea, three ways to write it:

- ❌ *Too simple:* "You can use different models easily."
- ❌ *Too obscure:* "The harness facilitates provider-agnostic model
  substitutability via abstraction of the underlying inference backend."
- ✅ *Peer register:* "Swap models without rewriting your agent; the harness
  abstracts the provider."

That gap — plain on the left, inflated in the middle, **right on the far right** —
is the whole job.

## Three principles (not a checklist to fill)

1. **Write for a smart peer.** (the target above)
2. **Every word earns its place.** Concrete, load-bearing, no throat-clearing.
3. **Precision before rhetoric.** Metaphor, antithesis, appositive — all optional
   seasoning that serves clarity. Never the main course.

**These are principles, not quotas.** The gold-standard docs *happen* to use
semicolon antithesis, triads, appositive labels, controlling metaphors. Do **not**
force those in to look the part — forced Tina reads worse than plain prose. Use
the techniques as an ear to calibrate against, not a bingo card to complete.

## Action 1 — Register calibration

Read a draft and place each sentence on the line between the two failure modes.

| | Too simple (novice) | Too obscure (board) | Peer register (target) |
| --- | --- | --- | --- |
| **Verbs** | use, make, do, get | facilitate, utilize, leverage | **inject** credentials, **wire up**, **route through** the proxy, **spin up**, **rehydrate** |
| **Specifics** | "faster", "better" | buried under abstraction | "**up to 10 points** on harder tasks", "in **minutes**" |
| **Concepts** | hand-waved | named but never grounded | named once, glossed once: "brain (harness) / hands (sandboxes)" |

Fix the extremes toward the target column. Don't manufacture a target where a
plain declarative was already fine.

## Action 2 — Word choice: the three-gate test

This is Ken's core pain. A word is "right" only if it clears **all three gates**.
Each gate blocks one failure mode.

1. **Register gate** — *Would a domain expert SAY this word to a peer, out loud?*
   Blocks too-casual (get / thing / stuff) **and** too-academic (utilize /
   facilitate / leverage). Both fail: one is under-dressed, one is costumed.
2. **Information gate** — *Does the word carry weight? Can a hostile editor
   DELETE it with no loss of meaning?* If yes, it's filler. Blocks the empty
   flourish that looks full but says nothing: powerful, seamless, robust,
   cutting-edge, solutions, vibrant.
3. **Ownership gate** — *Can I DEFINE this word? Is it a real term the field
   uses, or did I coin it to sound smart?* Blocks fake-fancy inventions like
   "provider-agnostic substitutability".

**Fancy ≠ wrong — this is the trap.** `checkpoint`, `rehydrate`, `co-optimize`,
`on-behalf-of delegated access`, `microVM` are hard words, but they are precise
**and** domain-standard, so they pass the ownership gate. Keep them. The enemy is
**empty** flourish, not flourish itself. Never downgrade a precise technical term
just because it looks advanced.

**Three-way calibration** (leftmost too plain, middle too costumed, **rightmost is
the target** — the concept midpoint between the two failures):

| Intent | Too plain | Too costumed | Right (peer term) |
| --- | --- | --- | --- |
| use X | use it | leverage / utilize it | **inject** credentials · **wire up** the integration · **route through** the proxy |
| make it easier | make it easy | streamline / facilitate adoption | **cut the friction** · a **low-friction** path |
| recover after loss | it comes back | achieve state re-instantiation | **rehydrate** in a new sandbox |
| tune two things together | make them work well | synergistically optimize | **co-optimize** the model and harness |

## Action 3 — Strip AI tells (subtract only)

Run the draft against the AI-tell list. The high-frequency offenders for Ken's
docs:

- **Banned vocabulary:** delve, tapestry, testament, underscore, pivotal,
  landscape (abstract), showcase, seamless, robust, vibrant, crucial, foster,
  intricate, realm, navigate (figurative), ever-evolving.
- **Rule of three overuse** — forcing ideas into groups of three. A real pair or a
  real four beats a manufactured triad.
- **Negative parallelism** — "It's not just X, it's Y"; tailing negations ("…, no
  guessing").
- **Superficial -ing tails** — "…, highlighting the platform's flexibility". Cut
  them; they add fake depth.
- **Copula avoidance** — "serves as / stands as / represents a" where "is" is
  truer. Foundry writes "The agent state **is** the continuity layer…". Use "is".
- **Em-dash overuse**, mechanical **boldface**, **title-case headings**, emojis.
- **Signposting** — "Let's dive in", "Here's what you need to know". Just say it.
- **Significance inflation** — "marks a pivotal moment", "reflects a broader
  shift". State what happened.

Full catalogue with before/afters: `references/ai-tells.md` (and the standalone
`humanizer` skill).

**⚠️ CRITICAL — subtract only, do not add "soul".** The `humanizer` skill also
tells you to *inject* first-person voice, casual words ("stuff", "things"),
jokes, and deliberate messiness. **Do NOT do that here.** Ken's docs are formal
peer-register framing — Tina and Foundry contain zero "I genuinely don't know how
to feel about this". Take humanizer's **removals**, ignore its **additions**. Your
"human voice" is defined by `gold-standard.md`, not by essay-blog personality.

## Action 4 — Expression discipline

- **Concise above all.** "Too long" is Ken's most repeated correction. Default to
  the tightest form that carries the information; prefer a table over prose; when
  he says "list", produce a list, not paragraphs. Cut a bloated draft hard.
- **Customer-scenario voice** where the section calls for it: *"As a [Java team /
  .NET developer / …], I want … so that …."* No internal jargon, no implementation
  terms — the outcome they care about. Foundry's "From a customer's point of view,
  a long-running agent continues meaningful work across time boundaries…" is the
  model.
- **Deliverables as plain-English bullets** — each a short phrase mapping to its
  scenario, not a dense comma-run, not implementation detail.
- **Precision before rhetoric** (again, because it's the one that saves you):
  settle the literal claim first, *then* add the metaphor/antithesis if it earns
  its place.

## Register conventions (Ken's house style)

- **Abbreviations:** spell out on first use, short form after, Glossary at the END
  — do NOT spell out everywhere.
- **Two registers, know which you're in:** chat replies stay plain and short; DOC
  CONTENT wants richer, more polished, vivid English (match the gold-standard
  voice) — still readable, never a jargon dump or hard-to-parse compound sentence.
  Ken pushes back if writing is genuinely hard to read.

═══════════════════════════════════════════════════════════════════
# Final pass (run before delivering)
═══════════════════════════════════════════════════════════════════

**Stage 1 — content (must already be clean):**
- [ ] Every factual sentence true; generalizing claims checked per-item
- [ ] New terms grounded with an example before being named; no undefined-defines-undefined
- [ ] Scope respected; cross-references point where content lives; audience level consistent

**Stage 2 — framing:**
- [ ] **Register:** every sentence reads as one smart peer talking to another — no
      novice hand-waving, no board-room costume.
- [ ] **Words:** each load-bearing word clears all three gates (register /
      information / ownership). Precise technical terms kept, empty flourish cut.
- [ ] **AI tells:** banned vocab gone; no forced triads, negative parallelisms,
      -ing tails, copula avoidance, em-dash spray, signposting, significance
      inflation. **No added essay-blog "soul".**
- [ ] **Discipline:** as tight as it can be; customer-scenario voice where asked;
      deliverables are plain bullets; abbreviations spelled out once + Glossary.
- [ ] **Read one paragraph aloud** against a `gold-standard.md` excerpt. Same
      register? If it sounds plainer or more costumed than the anchor, adjust.
- [ ] **Content untouched in Stage 2:** you changed how it reads, not what it
      claims. Any factual doubt kicked back to Stage 1, not silently rewritten.
