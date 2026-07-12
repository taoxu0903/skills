# Verification & Recency (ALWAYS-ON for EVERY run)

This is the **fact-quality** file: how to make sure every datum in the report is REAL,
fresh, and officially sourced. **It is always on for every deep-research run** — see the
**Golden Data Rule** at the top of `SKILL.md`: for all factual data you never use memory, you
always fetch the latest yourself and date it; the vendor's own official blog/doc is the source
of truth, with other public articles only as a fallback when no official page exists; the sole
exception is data the user gave you explicitly before the research (and even then, double-confirm
with the user when it could be stale). The live-product mechanics below (general-availability vs
preview, "last updated" dates) carry the most weight where status flips month to month, but the
fetch-fresh default itself is universal, not reserved for fast-moving subjects.

It is **NOT** gap-specific. The JUDGMENT-quality rules — disprove-your-own-gap, catch-up vs
greenfield, structural non-gap, ahead-vs-parity, judge-don't-rubber-stamp,
descriptive→prescriptive — live in `competitive-gap-analysis.md` and fire ONLY on a
gaps / enhancement / "confirm my conclusion" follow-up.

Clean split: **this file = is the FACT true and current?** · **gap file = is the CONCLUSION sound?**

## 1. Primary-source recency check (before trusting any feature claim)
- Read the **"last updated" date** on the vendor's OWN doc page (Microsoft Learn, AWS docs,
  vendor "What's New" blog). Quote the date in the deliverable for time-sensitive facts.
- When a secondary blog / listicle conflicts with the vendor's primary doc, **primary wins.**
  Aggregators are frequently stale or wrong. (Observed: blogs claimed a feature "went GA in
  June" while the vendor's own GA-status page still read Preview.)
- For time-sensitive runs, fire recency-filtered searches (Tavily `--time-range month`) AND
  read the primary page. Don't rely on either alone.
- A vendor doc can be primary AND stale — check its date, not just its domain. Prefer the
  freshest authoritative page (the vendor's GA-status overview and "What's New" index both
  carry dates). When the user says "check with the LATEST date," they mean exactly this:
  sort for freshness, read the date, cite it.

## 2. State general-availability vs preview for every capability claim
A feature *existing* is not the same as it being *generally available*. Enterprise buyers will
not build on preview (no service-level agreement). For each cell that matters, mark
general-availability vs preview, and source it from the vendor's official **GA-status /
"what's new"** page — then read that page's last-updated date. **GA-vs-preview is the single
most volatile axis** — never assert general availability from a secondary source.

## 3. Re-verify product names every pass — they rename fast
Open the current vendor page and confirm the name before using it. Seen in one session:
Vertex AI → "Gemini Enterprise Agent Platform"; Tencent LKE → "ADP"; Huawei → "ModelArts
Next / AgentArts"; OpenAI Assistants API retired → AgentKit / Responses. A stale product name
is an instant credibility hit.

## 4. Copy the real line; tag source type + date
- For each load-bearing fact, **quote the exact sentence** from the source and keep it (in the
  dispatch file or beside the cell). You cannot fabricate a quote you actually copied; if you
  can't find a real line to copy, treat the fact as unconfirmed, not true.
- **Two independent sources for fast-moving facts** (general-availability, prices, "just
  shipped", headline numbers): one official page, or two independent sources that agree. One
  blog alone is never enough for a volatile fact.
- Tag each key fact **official / secondary / inferred + date**, so weak or stale facts can't
  hide among solid ones.
- **Delegated research returns a link + the copied sentence per fact, or you re-verify it.**
  Subagents are the biggest source of confident-but-fabricated facts (they fall back on
  training knowledge). Any fact returned without both a real URL and the quoted line, re-fetch
  yourself before it enters the report.

## 5. Hunt the out-of-scope axes regional players compete on
When the object set mixes global and regional vendors (e.g. hyperscalers + China clouds), the
regional players often differentiate on axes a Western capability frame misses. Run an explicit
pass: "what do these players compete on that my locked dimensions don't capture?" Seen for China
clouds: domestic / sovereign full IT stack (信创 = 信息技术应用创新 — the WHOLE stack: chips
(Ascend / Kunlun / T-Head) + operating system + database + middleware + applications, NOT
silicon alone; and distinct from data-residency 数据不出域, which is about *where* data sits, not
*who builds* the stack), real-time audio/video + digital-human livestream agents, super-app
channel distribution (WeChat / DingTalk / Feishu), free-tier + token price war + agent
app-stores, robotic-process-automation / graphical-interface agents for no-application-
programming-interface legacy systems, and full-service business-to-business delivery ("陪跑").
Surface these as a callout rather than forcing China-only or non-capability axes into the main
matrix — and bring the list back to the user before adding columns. **Name each axis with its
precise local term** — a loose label is itself an error the user will catch. (Observed: labeling
the China stack axis "sovereign silicon" drew an immediate correction, because 信创 is whole-stack
self-reliance, not chips. Get the term's real scope right before you put it in front of the user.)

## 6. Propagate a corrected fact across ALL companion docs, and link-check review-grade claims
Research for this user lives as a FAMILY of companion docs in nengba-kb (a deep-dive, then
focused companions, then a competitor analysis + its dispatch file, then sometimes a gaps doc).
One verified fact often appears in several of them. When a check flips a fact:
- **Grep every companion doc for the old claim and fix them all in one pass** — not just the doc
  currently open. (Observed: a per-agent-control error sat in BOTH the platform doc and the token
  doc; fixing one would have shipped two docs that contradict each other.) After patching, grep
  the whole research folder for the old figure/phrasing and confirm zero stale hits.
- **Log the correction in each doc's evidence/confidence note** ("earlier draft said X; primary
  docs show Y, dated Z") — don't silently overwrite; the user values the audit trail.
- **When the user asks to "cite the references so I can double-confirm," put PRIMARY source URLs
  inline on the load-bearing cells/claims** (not a footnote), then **verify each URL resolves
  (HTTP 200)** before handing it over — a citation to a 404 is worse than none. A quick `urllib`
  HEAD/GET check in `execute_code` over the URL list is enough.

## 7. Never fill a factual cell from memory — even for a product you think you know
This is the detailed backing for the **Golden data rule** in SKILL.md (top of file). Every
factual datum gets fetched fresh from the web on the day you write it; your own recollection is
never the source. The trap is the fact you feel sure about — that's the one that silently goes
stale, because certainty suppresses the search.
- **Observed 2026-06-18:** a platform input/output audit searched and even self-corrected a
  competitor cell ("corrects my earlier 'bring-your-own only'") but wrote one vendor's memory
  cell as "no cross-session memory service in public docs" from recollection. The service had
  been in Public Preview for ~6 months and was the FIRST hit when finally searched. Not a recency
  miss — an un-run search on a cell that felt known. The phrase "in public docs" was the tell:
  it reads like a doc check but was a guess.
- **The disprove-absence rule applies to EVERY cell, no exceptions.** "X lacks Y" is the
  highest-risk claim whether X is a rival or the product the report is built around. Run the same
  disprove pass (search for evidence the feature EXISTS, in the vendor's own vocabulary, confirm
  against a primary page) on every absence claim regardless of whose it is.
- **Reconcile every cell against the Open Questions list before shipping.** If a cell states a
  fact as settled ("no memory service") while Open Questions still flags it as unconfirmed
  ("confirm whether memory exists"), the cell is overstating its own confidence. Resolve the open
  question BEFORE asserting the cell, or downgrade the cell to "unconfirmed." A cell that
  contradicts its own open-question entry is the clearest signal of an unverified claim.

## 8. Doc-family conventions to mirror (nengba-kb)
- A `> Companion to: <other docs>` header line.
- An `Open questions / to iterate later` tail section.
- A separate `<topic>-research-prompt.md` dispatch file recording lenses, rows, columns,
  retrieval method, and an evidence grade.
- Strength marks (●/◐/○) in matrices mean "breadth of coverage," not a depth benchmark — state
  this so a ● on one vendor isn't read as equal quality to another.
- A Glossary section at the END listing every short form used with its full name.
Always ask before writing to nengba-kb.
