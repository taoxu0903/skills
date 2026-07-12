---
name: product-spec-writing
description: Author and revise product specs, PRDs, roadmaps, and milestone/scenario docs as Markdown. Use for product-management documentation — feature specs, delivery milestones, user-scenario breakdowns, execution plans — especially when distilling a long PRD into a tight, customer-facing artifact.
---

# Product spec / PRD / roadmap writing

Authoring product-management Markdown docs: feature specs, PRDs, delivery
milestones, user-scenario breakdowns, roadmaps. Distinct from `writing-plans`
and `plan`, which are about *code implementation* plans — this is product-level
documentation aimed at stakeholders, not engineers executing tasks.

## When to use
- Drafting or rewriting a product spec / PRD section.
- Turning a long PRD or research doc into a milestone or roadmap doc.
- Breaking a feature into user scenarios + deliverables.
- Authoring a **golden-path / experience-design doc** (opinionated end-to-end
  walkthrough of a user task across its lifecycle) — see
  `references/golden-path-experience-docs.md` for the canonical definition, a
  lifecycle-gap audit checklist (catches commonly-missed stages: local
  build/test, create-the-containing-project, grant-identity RBAC, decommission),
  a proven section skeleton, and a verified fact bank.
- **Deriving a private/public preview scope from a settled GA scope** (with
  rationale), and the scope-integrity rules Ken enforces (no invented platform
  "delta" on a "same as today" step; don't restate a GA non-goal as a preview
  non-goal; prefer a self-serve CLI package over per-customer concierge for
  onboarding) — same reference file, "Deriving a PREVIEW scope" +
  "Scope-integrity corrections" sections.

## Workflow
1. **Read all source docs first.** PRD, execution plan, any prior scenario/spec
   doc. Ground the new doc in them; don't invent scope. Reconcile the framing of
   the new doc with the execution plan's structure (e.g. milestones/quarters),
   not just the PRD's original wave/phase structure.
2. **Mirror the keyword header block** the user already uses (Product/Feature,
   Author, Status, Last Updated table) at the top of new docs for consistency.
3. **Draft, then expect to cut.** First drafts here run too long. See style rules.
4. **Carry an explicit pointer** to the deeper companion doc (e.g.
   `*Full spec: work/research/<doc>.md*`) rather than duplicating its content.

## Drafting a spec from raw bullets / from scratch (structured mode)
When the user hands over **raw content bullets or a bare product need** (not an
existing PRD to distill), run this checkpoint-driven flow instead of free-drafting.
Ken's house style above still governs the *prose*; this governs the *procedure*.

1. **Parse the input.** Mode A = user gave explicit sections/TOC → keep their
   structure. Mode B = user gave only a need/bullets → structure is inferred after
   clarification.
2. **Clarify (use the `clarify` tool for the general questions).** Ask only what
   isn't already answered in the prompt (smart-skip): target audience, detail
   level (high-level vs detail-oriented), and — Mode B only — spec type
   (discovery / feature design / full product design). Then ask plain-text
   content questions for any ambiguous bullet (quote it, say why it's unclear).
3. **Present the TOC for review — mandatory checkpoint, never skip.** Draw
   sections from `references/spec-sections-guide.md` (core vs supplementary +
   selection heuristics by spec type). Show a table: `# | Section | What will be
   covered | Approach`, then ask for sign-off before writing.
4. **Write** each confirmed section, applying `references/content-standards.md`
   (customer-value framing, precise/unambiguous language, correct PM terminology,
   completeness, consistent formatting, direct tone) — these are the floor;
   Ken's explicit inputs and house style are the ceiling and override them.
5. **Review** silently against the brief: every input bullet addressed, every
   TOC section present, audience/detail level consistent, standards met.

Reference files:
- `references/spec-sections-guide.md` — the standard section catalog (core +
  supplementary) and per-spec-type selection heuristics. Use when the user says
  "standard layout" or gives no structure.
- `references/content-standards.md` — the non-negotiable PM content-quality bar
  (value framing, precision, terminology, completeness, formatting, tone).

## Style rules for THIS user (Ken Tao) — learned from corrections
- **Concise above all.** "too long" is a recurring correction. Default to the
  tightest form that carries the information. Prefer a **table** over multiple
  prose sections. When asked to "list" something, produce an actual list/table,
  not paragraphs. Cut a 15KB draft to ~5KB without being asked twice.
- **Customer-oriented scenario voice.** When a column/section is "scenario to
  cover" or "user scenario," write it in the customer's voice:
  *"As a [Java team / .NET developer / …], I want … so that …."* Focus on the
  outcome the customer cares about — no internal jargon, no implementation terms.
- **Deliverables as plain-English bulleted lists.** "Deliverables" / "what ships"
  columns are bullet lists of high-level items, each a short plain-English phrase
  that maps to its scenario. Not dense comma-runs, not implementation detail.
- **Summaries in customer voice too.** When asked for a summary of
  milestones/phases, frame each in the customer's point of view (a short
  "headline in quotes" + an "As a…, I want…" paragraph), then one tie-together
  line.
- **One big rock / scenario = one section** when using sections; but a single
  comparison table is preferred when the user asks to "list in one table."
- **Inline reference links, adjacent to the point — not footnoted.** When a doc
  narrates "the current/official experience," Ken wants each doc link placed
  *right next to the specific claim it backs* (inline `→ [Label](url) · [Label2](url)`
  after the sentence), so a reviewer can jump from any single point. Do NOT gather
  links into a References/footer section at the end. Pull each from the live doc,
  tag GA vs (preview), and verify every URL (HEAD/200) before shipping a
  leader-facing doc.

## Technique: bullet lists inside Markdown table cells
Plain Markdown `-` lists break inside a table cell. To render real bullets in a
cell, use inline HTML:

```
| Big rock | Deliverables |
| --- | --- |
| Foo | <ul><li>First item</li><li>Second item</li></ul> |
```

This renders correctly in VS Code preview and on GitHub. Flag the HTML choice to
the user and offer the pure-Markdown alternative (heading-per-row + bullet lists)
if they prefer no HTML.

## Delivering as .docx (when the user wants a Word file)
Pandoc is often unavailable (WSL / fresh boxes; `apt install pandoc` may fail).
Two bundled converters — **pick by how formatting-heavy the doc is:**

- **`scripts/md2docx.py`** — the simple one. Headings, bullets, pipe tables, and
  the inline `<ul><li>` table-cell bullets. Strips `**bold**`/`*italic*` to plain
  text and flattens sub-bullets — fine for plain docs.
- **`scripts/md2docx_rich.py`** — use this when the doc leans on **bold
  lead-ins**, `<span style="color:rgb(r,g,b)">…</span>` colored flags (e.g. Ken's
  red TBD/NOTE markers), **numbered step lists** (`1.`), indented sub-bullets, or
  inline `**bold**`/`` `code` `` inside table cells. The simple converter mangles
  all of these — the red spans leak through as literal `<span>` HTML text, bold
  lead-ins come through unbolded, and `1.` steps render as plain body paragraphs.
  The rich one preserves bold/italic/code runs, renders colored spans as real
  colored text, and maps `1.`→List Number, indented `-`→List Bullet 2,
  `>`→Intense Quote, `[label](url)`→blue underlined text. It self-verifies on save
  (counts tables/headings/red-runs, asserts zero leaked HTML). The BYO-AKS
  golden-path doc is a worked example: 2 tables, 9 headings, 4 red TBD flags
  preserved.

```
pip install python-docx        # one-time
# simple:
python3 scripts/md2docx.py work/research/<doc>.md          # -> same-name .docx
# rich (run from /tmp with ABSOLUTE paths, see shadow gotcha below):
cd /tmp && python3 /abs/path/to/scripts/md2docx_rich.py "/abs/IN.md" "/abs/OUT.docx"
```

The sandboxed `execute_code` interpreter lacks `python-docx`; run the converter
via `terminal`, not `execute_code`. Verify the output (paragraph/table counts)
before telling the user it's done.

**Fully respect the file's latest content — inject nothing.** Ken corrected
mid-task with "fully respect the file latest content" after a converter hardcoded
a title the file no longer had. Convert EXACTLY what's on disk: no synthesized
title, metadata block, or heading the source doesn't contain. `md2docx_rich.py`
adds nothing on purpose. And **re-read the file immediately before converting** —
these docs are frequently edited in the editor DURING the session (title/metadata
removed, red TBD flags re-added between reads); a `patch` `_warning` that the file
was modified by an external writer is the tell. Convert ground truth, not a stale
in-context copy.

**Gotcha — `ImportError: cannot import name getargspec` / `getfullargspec` when
importing `docx` or `lxml`.** This is NOT a broken install (`pip show python-docx`
will say it's fine). It means a stray module on `sys.path[0]` is shadowing a
Python stdlib module — on this user's box a rogue `~/inspect.py` (and the CWD's
own files) shadow stdlib `inspect`, which breaks `lxml`'s import chain. Fix: run
the converter from a clean directory so CWD isn't on the path, e.g.
`cd /tmp && python3 /abs/path/to/md2docx.py "IN.md" "OUT.docx"`. Pass an explicit
absolute OUT path since CWD is no longer the doc folder. Mention the shadow file
to the user so they can delete it (it breaks other Python tools too).

**Known fidelity limits of this converter** (state them honestly when delivering,
offer a polish pass): it strips inline `**bold**`/`*italic*` to plain text, so
bold lead-ins like "**What the customer hits:**" come through unbolded; and it
flattens nested/indented sub-bullets to a single level. Headings, the metadata
table, pipe tables, and flat bullets all carry over correctly. If bold lead-ins
or true nesting matter for a leadership doc, post-process the .docx (re-bold the
runs, set `paragraph_format.left_indent`) or use a richer converter.

**Verify, don't trust the "saved" print.** Re-open the .docx with `Document()`
and assert: `zipfile.is_zipfile` true, expected heading texts/levels present,
table count right, and a few load-bearing facts (key numbers, names) survive via
a substring check over all paragraph text. Only then tell the user it's done.

## Verifying competitor claims (PRD competitive sections)
Before repeating any competitor capability claim — including ones already
written in the user's own research docs — verify it against primary sources.
This user explicitly distrusts face-value claims.
- Read the vendor's own docs, not summaries. Confirm what a feature *actually*
  does vs. what its marketing name implies (e.g. a "gates AI-generated code"
  label may just be a project tag + a stricter generic quality gate + a badge,
  with **zero** AI-specific detectors).
- Distinguish detection *mechanism* (content analysis vs. a usage signal) and
  *unit* (per-diff vs. per-project) — these change the competitive story.
- When search engines block you (Google CAPTCHA/"sorry" page, empty DDG iframe),
  extract real doc URLs from the vendor's nav via `browser_console`
  (`[...document.querySelectorAll('main a')].map(a=>a.href)`) and navigate those
  directly instead of guessing URLs (guessed paths 404).
- Apply strict logical filtering when the user asks for a category (e.g. "issues
  in AI-authored code ONLY"): exclude anything that also occurs in human code.
  Keep only the categorically-unique set; name why the rest were dropped.
- **Don't anchor differentiation on an unverified competitor-scope boundary.** A
  "we own language/scope X, they don't" moat can collapse when the competitor
  turns out broader (multi-language, multi-mode) than its marketing examples
  imply. Verify the competitor's real scope first; if the assumed moat evaporates,
  shift the wedge (breadth / continuity-memory / context) instead of defending the
  dead claim. Full play-by-play in `references/positioning-vs-adjacent-product.md`.

## Positioning the product vs. an adjacent / competing initiative
When the user asks to *compare* their product with a competitor or another
(often internal-Microsoft) system — not author a doc — use the 5-part frame in
`references/positioning-vs-adjacent-product.md`: (1) different job? (2) converge
— steal the architectural thesis as internal top-cover, (3) rigor pattern to
copy, (4) where the user is deliberately less ambitious and right, (5)
positioning/collision risk + a one-line boundary for the spec. Deliver as plain
text, then offer to fold the boundary statement into the spec.

## Naming a product/feature to match the official doc
When the user asks to name something \"how it's stated in the official doc\" (or
gives a Microsoft Learn / vendor URL), match it VERBATIM — casing, word order,
and the exact term. Pull the live doc; don't reuse the name from memory.
- Match the page H1 casing exactly: \"Hosted agents\" (lowercase a), not \"Hosted
  Agents\"; use the full product name on first mention (\"Hosted agents in Foundry
  Agent Service\"), short form after; keep (preview) where the doc shows it.
- Adopt the doc's exact noun for the core object (\"VM-isolated sandbox,\" not a
  paraphrase like \"sealed box\").
- After matching one instance, grep the WHOLE doc for the same term and offer to
  align every other instance (intro, headers, body) — naming drift across one
  file looks sloppy. Flag stale instances rather than silently editing the brief.
- **Don't invent the category label or the value props.** Use only the doc's own
  framing. The doc calling it a "managed platform" does NOT license you to write
  "agent sandbox platform"; "sandbox" may be only the per-session unit, not the
  product class. Likewise pull benefit words verbatim ("predictable cold starts,"
  "scale-to-zero with stateful resume") instead of inventing a pitch like "pack
  many per machine / density" — verify, because the doc may state the OPPOSITE
  (e.g. "scale per session, not per replica"). The user stress-tests with "is it
  CALLED that in the doc?"; if a noun/claim isn't in the source, it's your
  invention — cut it. This applies to internal detail too: stop at the doc's
  abstraction (e.g. "VM-isolated"); add deeper engine names (Firecracker/microVM)
  only where they're truly internal and label them as such.
- learn.microsoft.com often fails `web_extract` (Tavily 432); fall back to the
  browser. To grab one section, use `browser_console` to find the heading and
  read its next siblings until the following h2.

## Composing an image-gen prompt for a flow / architecture diagram
The user often pairs a spec section with a generated diagram (GPT-image / image
gen). Workflow that worked:
1. **Tune the prose section first, get explicit sign-off, then write the diagram
   prompt.** Don't generate the image off rough notes — the diagram inherits the
   text's structure, so the text must be settled first.
2. **Write a single, self-contained prose prompt** (not JSON/keywords): state
   background, flat/vector style, muted palette, named sections with header bars,
   each node's exact label text, arrow labels, decision diamonds with Yes/No
   branches, loop-back arrows, and a footnote banner for the key invariant.
3. **Pull labels verbatim from the spec** so diagram and doc stay consistent.
4. **Honor explicit layout directives literally** — \"left-to-right not
   top-down,\" aspect ratio (16:9 slide vs 2:3 page). Restate the chosen aspect
   ratio in the prompt.
5. **When the user changes the diagram, mirror the change back into the prose**
   so they never drift. E.g. when they asked to make a Pull Request the explicit
   merge-guard in the diagram, the matching §6.2 text was rewritten to PR-check
   framing (open PR → CI check → pass/fail → fix in same PR branch → push →
   re-run). Offer this sync proactively; the user said \"yes\" both times.

## Tuning rough bullet notes into a finished section
When a doc has a half-written section (raw indented bullets), rewrite it to match
the rest of the doc's conventions before generating anything from it: name
sub-parts so a diagram has clean labels, restore any load-bearing invariant the
notes dropped (e.g. \"blocks only on NEW, undecided findings\"), and present the
proposed text for review before writing it to the file. Flag the deliberate
changes you made so the user can veto.

## Pitfalls
- **Don't over-explain in the reply.** Deliver the file, give a tight summary of
  what changed and why, surface one genuine judgment call if any. No padding.
- **Watch for duplicate `---` separators** after a `patch` insert near an
  existing divider — re-read and clean up.
- **Reconcile conflicting numbers across source docs** (e.g. "30 issues" vs "33
  issues") — either use the neutral phrasing both share, or flag the discrepancy
  and ask; don't silently pick one.
- After a `patch`, if the tool warns the file was modified by a sibling/external
  writer, re-read before the next write to avoid clobbering changes.
