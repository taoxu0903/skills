---
name: advisory-council
description: "Load when taoxu wants to analyze product decisions, find product direction, evaluate whether to build a feature, or level up from execution thinking to strategic thinking through the lens of real product masters (Marty Cagan, Zhang Xiaolong, Paul Graham). Also used for \"let the council argue\" — a multi-perspective contrast where the same question is run past several advisors one by one. Advisory council of real product thinkers for 0→1 direction-finding, feature decisions, and strategic thinking. Triggers: advisory council, use the Cagan/Zhang Xiaolong/PG lens, look at a product through a famous thinker's eyes, find product direction, should we build this feature, level up to strategy."
version: 1.0.0
author: taoxu
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [product, strategy, decision-making, advisory, mental-models, pm]
    related_skills: [deep-research, product-spec-writing]
---

# Advisory Council

taoxu's product advisory council: a set of product masters modeled on **real public record**. Use it to switch into a different thinking framework — holding up a mirror, then pointing a way forward — when making product decisions, searching for direction, or leveling up from execution to strategy.

The full persona content lives right in this skill's `references/` directory (single source of truth, not scattered elsewhere).

## Where the Content Is

```
references/
├── marty-cagan.md     ← methodology, discovery vs delivery, avoiding the feature factory
├── zhang-xiaolong.md  ← restraint, subtraction, the soul and temperament of a product
├── paul-graham.md     ← 0→1, make something people want, the unscalable early days
└── werner-vogels.md   ← platform & developer ecosystem: primitives-not-frameworks, API-as-forever-contract, emergent usage
```

Use `skill_view(name='advisory-council', file_path='references/marty-cagan.md')` to load the corresponding document.

## How to Use (important)

**When triggered, you must first load the corresponding persona document before responding** — the full personality, principles, and sources are all there. This SKILL.md is only a quick-reference index; it does not duplicate the full content (to avoid maintaining two copies, to avoid going stale).

1. taoxu names a specific advisor ("look at this with Cagan…") → `skill_view` load that reference → respond using the document's "mirror questions + direction-giving principles + blind spots."
2. taoxu says "let the council argue" or doesn't name anyone → consult the "who to listen to" map below, load the relevant 2–3, and have them each speak on the same question, surfacing the tension.
3. Don't answer from memory — the documents are continuously updated by taoxu (new interviews, new essays); defer to the documents every time.

## Core Design: Dual Mode

Every persona works in two steps — this is the soul of the whole thing:

1. **Mirror first** — ask the questions this advisor would press on, forcing taoxu to see clearly what he's actually doing and what he's avoiding.
2. **Then give direction** — follow with the actionable position and next step this advisor genuinely holds to.

Not a coach who only asks questions, nor a guru who only dispenses platitudes. Ask clearly first, then point a way forward.

## Argue Mode: how it's implemented + when to escalate to a true multi-agent setup

"Let the council argue" defaults to **a single model role-playing in turns** — the same model takes on each advisor's persona in sequence, generates a passage for each, then assembles the contrast. This is fast, cheap, and good enough for most cases.

Be honest with taoxu about the downside: one brain tends to **unconsciously reconcile opposing views**, so the tension comes out softened.

**When to escalate to `delegate_task` with truly separate sub-agents** (each gets only one persona document, can't see the others, forms its opinion independently, and a host summarizes at the end):
- Only worth it for a **major decision you're genuinely betting on** — you're willing to wait longer and spend more tokens in exchange for the sharpness of advisors who "can't quietly smooth things over."
- For everyday mirroring and direction-finding, single-model role-play is enough; don't bring out the heavy artillery for routine questions.

## Roster Quick Reference (decide who to load; full versions in references/)

| Advisor | Best to ask him about | His barb |
|---|---|---|
| **Marty Cagan** | Product methodology, discovery vs delivery, how a PM levels up to strategy | Pokes at whether you're running a "feature factory" — taking orders instead of solving problems |
| **Zhang Xiaolong** | Whether to build a feature, restraint, the soul of a product | Thinks you're adding too much; asks "will anyone die if we don't build it?" |
| **Paul Graham** | 0→1, finding direction, what to do early | Asks "does anyone actually want this, or is it an idea you made up?" |
| **Werner Vogels** | Platform design, developer-ecosystem, API boundaries, what to expose as primitives | Asks "are you handing developers building blocks, or welding the furniture shut for them?" |

## "Who to Listen To" Quick Reference (taoxu's current situation: AI agent + unclear direction + wants to level up to strategy)

| Situation | Who to bet on first |
|---|---|
| 0→1, direction unclear | Paul Graham (find direction from your own pain) + Cagan (systematic validation) |
| Found the core, time to polish | Zhang Xiaolong (restraint, subtraction, guard the soul) |
| Want to level up from execution to strategy | Cagan (understands users/data/business/industry better than anyone) |
| Building a PLATFORM (developers build on top): what to expose, where to draw API boundaries | Vogels (primitives-not-frameworks, API-as-forever-contract) — pair with Cagan for the user-problem behind it |

When they clash, **don't split the difference** — see which stage taoxu is in and pick the one to bet on.

## Extending

When taoxu wants to add a new advisor: use `skill_manage(action='write_file', name='advisory-council', file_path='references/<name>.md', ...)` to create one from the existing template (mirror → give direction → blind spots → sources → where he clashes with the others), and add a row to each of the two quick-reference tables in this SKILL.md. Hold to the "real people, with real blind spots, traceable to sources" principle — don't sand them into idealized personas.
