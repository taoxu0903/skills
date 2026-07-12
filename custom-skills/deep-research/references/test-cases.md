# Deep-research skill — regression test cases

Four real user research requests, each with the flow the skill SHOULD compose and the
behaviors a correct run MUST / MUST-NOT exhibit. These are the **oracle** for this skill.

## How to use these (run after ANY edit to SKILL.md or its references)

For each test case, check four things against the current skill text:
1. **Step A typing** — does the skill still classify the subject the same way?
2. **Flow composition** — does the same lens sequence still fall out of the design?
3. **MUST assertions** — is every required behavior still demanded by the skill text?
4. **MUST-NOT** — has any edit introduced a path that allows a failure signal?

A change that breaks a MUST, enables a MUST-NOT, or silently re-types a subject is a
regression — fix the skill or update the test case deliberately (and say which).

Optional live check: hand one request + this file to a `delegate_task` subagent and ask it
to produce ONLY the Step A plan (lenses + checkpoints), then diff against "Expected flow"
below. Cheap dry-run, no full research spend.

Notation: ● heavy · ○ light · — absent. ⛳ = human checkpoint.

---

## TC1 — Pure concept (no product, no comparison)

**Request:** "What is evergreen, and how does it relate to modernization?"
(调研 evergreen 是什么，以及和 modernization 的关系)

- **Step A typing:** abstract concept, no product.
- **Discovery required?** No.
- **Expected flow:** `Concept ● (define evergreen) → Concept-relation ● (evergreen ↔ modernization)`
- **Checkpoints that fire:** ⛳1 plan · ⛳persist-approval · ⛳4 self-review. **⛳2+3 do NOT fire** (no Discovery, no Compare, no dimensions).

**MUST**
- Lead with a concrete example/scenario BEFORE naming "evergreen".
- Produce an is / is-not boundary table.
- Frame the relation as **event vs state**: migration is a one-time event, evergreen is keeping it from going stale again.
- Name at least one common misconception (e.g. treating evergreen as a sub-step of modernization).

**MUST-NOT**
- Do NOT run Discovery divergence or build a candidate list.
- Do NOT build a comparison matrix or list competitors.
- Do NOT fabricate vendors/products to fill a section that doesn't need them.
- Do NOT append a strategy / "implications for your product" / recommendations section — this skill stops at objective research substrate.

---

## TC2 — Forms (capability productization survey)

**Request:** "How is 'agent team' (multi-agent collaboration) applied in vertical scenarios — what product forms and products exist?"
(调研 agent team 在垂直场景的应用，有哪些产品化形态和产品)

- **Step A typing:** capability / pattern ("how is X productized").
- **Discovery required?** Yes.
- **Expected flow:** `Concept ○ gate → Discovery ● → Teardown ○ (sample reps) → Forms ● → Trends ○`
- **Checkpoints that fire:** ⛳1 plan · ⛳2 candidate set · ⛳persist-approval · ⛳4 self-review. **The "columns" ratified here are the FORM-clustering axis, not comparison dimensions** (this flow has no Compare).

**MUST**
- **Property-word gate FIRST:** gate "agent team / multi-agent" before diverging — bucket candidates into multi-agent (pass) / single-agent-multi-tool (fail) / partial, and scope to the right superset.
- **Unseeded Discovery:** category map = the vertical DOMAINS (security, support, legal, healthcare, sales, coding…); zero vendor names in queries.
- **Teardown BEFORE Forms:** tear down the sampled representatives first (3–5 sentence prose profile each), THEN induce forms bottom-up from the real mechanics — never name forms before understanding the players.
- Each form in the forms table filled with a **real representative** drawn from the teardowns; a form with no real example gets deleted.
- Light Trends read on top (where the forms are heading); stop there — no strategy/implications section.

**MUST-NOT**
- Do NOT list single-agent tools as "agent teams".
- Do NOT seed Discovery queries with known vendor names (Sierra, Harvey, Devin, MDASH…).
- Do NOT cluster into forms BEFORE Teardown — armchair categories instead of evidence-grounded forms.
- Do NOT invent a plausible-looking form with no real representative.
- Do NOT run a Compare matrix (this is a forms survey, not a who's-stronger comparison).

**Known friction this case exists to catch** (regression sentinels)
- checkpoint 2+3 is written around *comparison dimensions*; in a Forms flow there is no Compare, so confirm the **form axis** instead. If a skill edit makes the dimension checkpoint mandatory-as-comparison, this case should flag it.
- Teardown's "recent-3-month new features" mandate is **optional/over-spec** for a forms survey of sampled reps. An edit that hard-requires it everywhere over-burdens this flow.
- Discovery's category-map for a pattern question is a *domain* axis, but the search-tooling reference only illustrates security-tool categories. Watch that the protocol stays domain-agnostic.
- Forms must stay positioned AFTER Teardown (Compare's synthesis sibling). An edit that moves it back before Teardown is a regression.

---

## TC3 — Teardown + Compare (unfamiliar product vs known own product)

**Request:** "What is MDASH, and how does it differ from GHCP Mod Evergreen?"
(调研 MDASH 是什么，以及和 GHCP mod evergreen 的区别)

- **Step A typing:** one unfamiliar single product (MDASH) + one known own product (Evergreen). *(Hybrid type — covered by the worked-example table even though the subject-typing bullets lack an explicit "unfamiliar + known" row.)*
- **Discovery required?** No — both objects are already fixed.
- **Expected flow:** `Teardown ● (MDASH, full) → Compare ●`
- **Checkpoints that fire:** ⛳1 plan · ⛳dimensions confirmed BEFORE Teardown (even though Discovery is skipped) · ⛳persist-approval · ⛳4 self-review.

**MUST**
- Confirm the comparison axis with the user before tearing down MDASH — propose axes (Job / Scope / Languages / Depth-vs-breadth / Trigger / Audience / Maturity) and let them edit.
- **Full** teardown of MDASH: components → mechanism/pipeline (Prepare→Scan→Validate→Dedup→Prove) → surface (Defender tabs in Copilot app) → maturity (private preview) — not just dimension cells.
- Treat Evergreen as already-known; do not re-discover it.
- Compare produces **two sections**: (1) table + plain-English summary, (2) recent-3-month trend.
- Stop at the objective Compare. The overlap/differentiation falls out of the table + summary; the PM draws the strategic conclusion themselves.

**MUST-NOT**
- Do NOT run a Discovery divergence (objects are fixed).
- Do NOT ship a bare comparison table with no summary.
- Do NOT append a strategy / positioning-recommendation section (e.g. "don't stake value on the security pillar", "consume MDASH as a dependency", "handshake with the ACS team") — that is the PM's call, not the skill's output.

---

## TC4 — Full Discovery → Compare (the archetype)

**Request:** "What products do code assessment in the market — competitive analysis."
(调研市场上做 code assessment 的产品有哪些，竞品分析)

- **Step A typing:** capability domain ("who does X").
- **Discovery required?** Yes.
- **Expected flow:** `Concept ○ scope → Discovery ● → [Teardown ○×N dimension-limited] → Compare ● → Trends ●`
- **Checkpoints that fire:** ⛳1 plan · ⛳2+3 candidate list + comparison dimensions together, BEFORE Teardown · ⛳persist-approval · ⛳4 self-review (read report back against Quality Contract + Pitfalls).

**MUST**
- Scope gate: "code assessment" = the assess phase, NOT transform/execution — exclude pure execution tools.
- **Unseeded Discovery, full protocol:** category map (Static Application Security Testing, Software Composition Analysis, code-quality/tech-debt, secret scanning, Application Security Posture Management, modernization peers); one unseeded enumeration query per category; mine listicle BODIES (raw_content), not titles; frequency-rank, recurrence ≥ 2 = real.
- Include any user-named tools by default (unseeded rule binds queries, not the user's list).
- Present candidate list + recommended dimensions together (⛳2+3), lock dimensions before Teardown.
- Dimension-limited Teardown per tool: 3–5 sentence prose profile following the locked dimensions + a dated last-3-months feature list.
- Compare = two sections (matrix + plain summary; recent-3-month trend). Trends = 5–7 named trajectories. Stop there — no strategy/bets/wedge section.
- Spell each term out on FIRST use with the short form in parentheses (Software Composition Analysis (SCA)), use the short form after, and end the doc with a Glossary section listing every short form with its full name.
- After persisting, run the two-part self-review (checkpoint 4): Part 1 — read the report back against this skill's Quality Contract + Pitfalls, with a mechanical scan (citations inside volatile cells, glossary coverage of every short form, per-object profile count, two-section Compare); Part 2 — load the pm-writing-gater skill and run its checklist. Hand the user a followed/deviated gap list, fix clear-cut errors (missing citations, missing glossary entries, stale dates), and let the user choose on structural gaps.

**MUST-NOT**
- Do NOT seed queries with vendors you already know — the canonical failure: seeding "Dependabot Renovate Snyk" returned exactly those and missed Semgrep, Mend, Black Duck, Codacy, GitGuardian, and the whole Application Security Posture Management category.
- Do NOT treat one search result as one candidate — listicles are containers of many.
- Do NOT ship a Compare that is a bare table, or a Teardown that is a row of generic verb-cells.
- Do NOT write to the knowledge base without explicit approval.

---

## Coverage map (what each case guards)

| Mechanism in SKILL.md | TC1 | TC2 | TC3 | TC4 |
|---|:--:|:--:|:--:|:--:|
| Step A subject typing | ● | ● | ● (hybrid) | ● |
| Concept lens (define + is/is-not + relation) | ● | ○ gate | — | ○ scope |
| Property-word gate | — | ● | — | ○ |
| Unseeded Discovery protocol | — | ● | — | ● |
| checkpoint 2+3 (rows + columns) | — | ◐ form-axis | ◐ dims-only | ● |
| Teardown depth floor (3–5 sentence prose) | — | ● | ● full | ● |
| Teardown recent-3-month features | — | ◐ optional | ● | ● |
| Teardown BEFORE synthesis (Compare/Forms) | — | ● | ● | ● |
| Forms (synthesis sibling) | — | ● | — | — |
| Compare two-section rule | — | — | ● | ● |
| Trends lens | — | ○ | — | ● |
| No strategy/implications section | ● | ● | ● | ● |
| Persist + approval | ● | ● | ● | ● |
| Self-review vs skill (checkpoint 4) | ● | ● | ● | ● |

● core · ○ light · ◐ partial/edge-case · — not exercised

The two ◐ cells in TC2/TC3 are the **edge cases**: a non-Compare flow (TC2) and a
skip-Discovery flow (TC3) both still need the dimension/axis question answered, but in a
shape the comparison-centric checkpoint language doesn't fully spell out. Keep them.
