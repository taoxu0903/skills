---
name: writing-quality
description: Quality standards and review process for any writing task — articles, explanations, documentation, summaries. Load this before starting any writing assignment.
triggers:
  - write article
  - write a post
  - write an explanation
  - rewrite
  - explain concept
  - draft
  - wechat article
  - technical writing
---

# Writing Quality Standards

Load and follow this skill for any writing task. These rules exist because writing coherence and rhetorical smoothness can silently override factual accuracy if you don't check deliberately.

---

## Rule 1 — Correctness Above Everything Else

Content correctness is the highest priority. It outranks:
- Narrative elegance
- Rhetorical devices ("they all share X", "the common thread is Y")
- Flow and transitions
- Conciseness

A sentence that is smooth but wrong is worse than a sentence that is awkward but true.

**Specific failure mode to guard against:** reaching for a unifying claim to make writing feel tighter, without verifying the claim holds for every item it covers. Before writing any generalizing sentence, check it against each individual case first.

---

## Rule 2 — Concept Grounding Before Terminology

Before introducing any concept or technical term, ask: can a new reader understand this without prior knowledge?

- If yes: introduce it directly.
- If no: ground it first with a concrete, relatable example or scenario. Only then name the term.

**Pattern to follow:**
1. Concrete experience / scenario (reader understands the problem)
2. Name the term (reader now has something to attach the name to)
3. Precise definition (reader can now absorb it)

**Anti-pattern to avoid:**
- Defining a term using other undefined terms
- Opening a section with jargon and explaining it afterward
- Using "the intuition is..." as a substitute for actually building the intuition

---

## Rule 3 — Post-Write Review (Mandatory)

After completing any piece of writing, do a full review pass before delivering. Check every section against:

**Factual accuracy**
- Does every sentence that makes a factual claim actually state a true fact?
- Do generalizing claims ("all three share X", "both cases involve Y") hold for every individual item? Check each one.
- Are numbers, dates, names, and attributed quotes correct?

**Concept consistency**
- Are terms used consistently throughout? If a term is defined one way in section A, it must mean the same thing in section B.
- Does each concept appear in its correct scope? (e.g. DL-specific content should not appear in an ML-only article)

**Reader comprehension**
- Is every term that a new reader wouldn't know either explained inline or grounded with an example before use?
- Are there any sentences that sound authoritative but don't actually say anything verifiable?

**Structural logic**
- Does each section follow logically from the previous one?
- Are cross-references (e.g. "as covered in Q3") accurate — do they point to where the content actually is?

---

## Rule 4 — Audience-Calibrated Depth

Before writing, explicitly identify the intended audience's knowledge level. For each major concept:
- What does this audience already know?
- What can be assumed vs. what must be explained?
- What analogies will land vs. feel condescending or confusing?

Never assume a knowledge level — state it explicitly at the start of the project, then apply it consistently throughout. A concept that requires no explanation for one audience may need three paragraphs of grounding for another.

---

## Rule 5 — Scope Discipline

Each piece has a defined scope. Before writing any section, ask: does this belong in this piece, or in a different one?

For standalone pieces: stay within the declared topic boundary.

For multi-part series: content that belongs in a later piece should be mentioned briefly as a forward pointer ("covered in depth in Part N"), not explained in depth here. Content from an earlier piece should be referenced back, not re-explained at the same level of detail — only go deeper if the new context genuinely adds something the earlier piece didn't.

---

## Review Checklist (run before delivering any written piece)

- [ ] Every factual sentence is true and verifiable
- [ ] Every generalizing claim checked against all items it covers
- [ ] Every new term grounded with a concrete example before being named
- [ ] No undefined terms used to define other terms
- [ ] Scope respected — no content that belongs in a different piece
- [ ] Cross-references point to where content actually lives
- [ ] Audience knowledge level correctly assumed throughout
