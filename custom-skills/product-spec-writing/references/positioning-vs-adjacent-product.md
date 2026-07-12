# Positioning the user's product vs. an adjacent / competing initiative

Use when Ken asks to "compare X with what we just planned" or "how does our
product relate to [competitor / another Microsoft system]." This is *analysis*,
not doc authoring — deliver it conversationally (terminal-readable plain text),
not as a file, unless asked to fold it into a doc.

## Read both sides first
- Re-read the user's own planning docs (spec, roadmap) before comparing — files
  get renamed mid-project (e.g. `roadmap planning for evergreen.md` →
  `evergreen-roadmap planning.md`); if `read_file` 404s, check the
  `similar_files` hint and re-read the renamed file. Don't compare from memory.
- Pull the competitor/adjacent source from primary text, not a summary.

## The comparison frame that worked (reuse this structure)
1. **Different job?** Lead by separating the job-to-be-done. State plainly if the
   two are NOT the same class of product. (e.g. MDASH = offensive *discovery* of
   net-new zero-days in proprietary systems code Microsoft owns; Evergreen =
   defensive *maintenance* of known-pattern debt in customer app code.) Kill any
   "it's basically X for our space" framing up front if the defect classes barely
   overlap.
2. **Where they converge — steal the thesis.** Find the adjacent product's
   headline architectural claim and check whether it validates the user's own
   bet. MDASH's "the model is one input; the system is the product… durable
   advantage is the agentic system around the model, not the model" is exactly
   Evergreen's bet (re-runnable loop + git-committed finding-state store is the
   moat, not a smarter model). Hand the user this as internal top-cover for the
   "won't a better base model make us obsolete?" question.
3. **Rigor pattern to copy.** Note any validation discipline worth adopting.
   MDASH validated on a never-published held-out codebase (StorageDrive) so
   "it reasons, not memorizes" can't be dismissed as training-data overfit.
   Translate to the user's LLM-judge pillars: define a held-out, never-public
   validation set so precision/gate numbers (e.g. ≥0.85 gate) are credible.
4. **Where the user is deliberately LESS ambitious — and right.** Call out cost/
   economics mismatches so the user can resist "make us more like X" pressure.
   (100+ agents + dynamic prove stage run by security PhDs on tier-1 targets does
   NOT transfer to per-repo weekly customer scans; annotate-only/suggestion-mode/
   single-language-first is the correct low-cost-breadth posture.)
5. **Positioning risk to manage.** Flag collision risk when both ship under the
   same banner (here: "AI + code + security + Microsoft"). Give a crisp
   one-sentence boundary the user can put in the spec *before* someone else draws
   it for them (different defect class / different surface / different user).

## Verify the competitor's REAL scope before claiming a moat (hard-won)
Don't anchor the user's differentiation on a boundary you haven't verified. A
first-pass framing claimed Evergreen's defensible ground was a "Java/.NET
language moat" because the competitor (MDASH) looked C/C++-memory-safety-only.
That collapsed: the competitor is actually **multi-language** (scans managed/
Python) and runs **two modes** (novel-vuln discovery AND known-CWE detection
against a supplied list). The single C/C++ ASan "prove" step was one bug-class
example, not the whole product.
- Read the competitor's primary text for what stages are *model/language
  agnostic by construction* vs. demonstrated on one target. Marketing benchmarks
  (one driver, one OS) are examples, not scope limits.
- When the moat you assumed evaporates, **shift the wedge** rather than defend
  the dead claim. Here the wedge moved from "language" to: (a) **breadth** across
  the non-security pillars the competitor ignores (deps/license debt, AI-native
  drift, AI-enablement); (b) **continuity + memory** (re-runnable loop + git-
  committed state store that remembers prior dismissals); (c) **modernization
  context** (debt vs migration baseline). On the *narrow* overlap (security CWE
  detection) concede there is NO differentiation if the competitor is deeper and
  ships first — say so plainly.
- Posture follow-through: when the competitor is deeper on the overlap, recommend
  **consume/compose** its signals (and a deliberate handshake with that team),
  NOT re-implement. Beware a three-way squeeze (e.g. GHAS broad+GA below, MDASH
  deep+preview above) crushing a single pillar — name it.

## Citation hygiene for unverifiable / private-preview competitor capability
Some competitor capabilities are only knowable from a private preview, a Build/
conference video, or the user's firsthand account — and are **publicly
unindexed** (search returns zero hits; the vendor blog doesn't mention them).
Accept the user's firsthand evidence as authority for the analysis, BUT in any
written note keep that integration **explicitly hedged in a Sources line** as
unverified, and offer to add a citation/link if the user supplies the session
URL. Do not state a private-preview integration as established public fact.

## When the comparison IS asked for as a file
The default is conversational plain text. But if the user says "write a md for
this research," produce a standalone note (e.g. `work/research/<x>-vs-<y>.md`)
using the 5-part frame as sections: §1 what each is, §2 overlap, §3 differences
table, §4 defensible ground, §5 positioning conclusion, + a Sources line.
Re-read before re-writing — the user may add inline annotations (highlighted
`<span>`s) or stub sections externally between your edits; preserve them.

## Bottom-line shape
Close with one line stating the relationship category: competitor vs. template
vs. **internal proof point + rigor bar** (MDASH was the latter — NOT a competitor
or template for Evergreen). Then offer to fold the boundary statement + rigor
idea into the spec.

## Extracting Microsoft Security blog text (breadcrumb/nav-heavy pages)
`browser_navigate` returns a truncated snapshot. Get clean body text via
`browser_console`:
`Array.from(document.querySelectorAll('main p, main h2, main li')).map(e=>(e.tagName==='H2'?'\n## ':'')+e.innerText.trim()).filter(t=>t.trim()).join('\n')`
Slice to a section with `s.indexOf('Heading text')`. Note: these pages duplicate
the intro under the in-page TOC, so `lastIndexOf` can land on an empty tail —
prefer the first `indexOf` of a heading and slice forward a fixed length.
