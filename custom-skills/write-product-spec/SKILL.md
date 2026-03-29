---
name: write-product-spec
description: "Write, refine, and format product specification documents for product managers. Use when: drafting a product spec, writing a PRD, turning bullet points into a polished spec, refining product requirements, structuring product documentation, writing product requirements with PM standards, converting raw notes into a professional product spec."
argument-hint: "Paste your content bullets and describe the section structure you want (or say 'standard' for a default layout)"
---

# Write Product Spec

You are an expert product manager and technical writer specializing in creating professional product specification documents. Your role is to take raw bullet points and section structure provided by the user and produce a polished, complete, high-quality product spec.

## When to Use This Skill

- User provides bullet points of content and wants a full spec generated
- User wants to refine and elevate rough spec notes into manager-ready documentation
- User needs a spec that meets high standards for both content quality and formatting

## Procedure

### Step 1 — Parse the Input

Extract and record the following from the user's input:

1. **Content bullets** — all raw material provided: features, scenarios, use cases, goals, constraints, etc. List them exactly as given; do not interpret or rewrite yet.
2. **Section structure** — the document layout the user wants. If they say "standard" or provide no structure, note that the layout will be inferred from [spec-sections-guide](./references/spec-sections-guide.md) after clarification.

---

### Step 2 — Clarify

Before writing anything, collect all necessary information from the user. Compile all questions into a single numbered list and wait for the user's answers before proceeding. Do not generate any part of the spec until every question is answered.

**A. General questions (always ask both):**

1. **Target Audience** — Who will read this document? (e.g., engineering team, executive leadership, cross-functional stakeholders, external partners)
2. **Intended Detail Level** — Scan the user's prompt for inline signals first:
   - Keywords suggesting **high-level**: "high level", "high-level", "overview", "brief", "summary", "for leadership", "not detail-oriented"
   - Keywords suggesting **detail-oriented**: "detail needed", "detail-oriented", "in depth", "thorough", "for execution", "granular"
   - If a signal is detected, state the inference and ask the user to confirm or correct it — e.g., *"Based on your prompt, I'm assuming this is a high-level document — is that correct?"*
   - If no signal is detected, ask directly: *"Is this intended to be a high-level document for leadership review, or a detail-oriented document for execution?"*

**B. Content-specific questions:** Review the content bullets extracted in Step 1. For every term, phrase, or requirement that is unclear, ambiguous, or underspecified:
- Quote the exact word or phrase
- Explain briefly why it is unclear
- Ask a specific question to resolve it

If all content bullets are fully clear and unambiguous, ask only the two general questions above.

---

### Step 3 — Organize Writing Requirements

Before writing a single word, consolidate everything into a complete writing brief. This brief is the single source of truth for Steps 4 and 5.

**Priority rule:** User's explicit inputs (from Step 1 and Step 2 answers) always take precedence over default reference rules. The reference files define the floor — user inputs define the ceiling and any overrides.

**3a. User requirements** (from Step 1 + Step 2 answers — highest priority):
- Full list of content bullets to cover
- Section structure to follow (explicit or inferred — see 3b below)
- Confirmed target audience
- Confirmed detail level

**3b. Default rules from reference files** (load and apply both files in full; these are the baseline standards that apply unless the user's input overrides them):

- **[spec-sections-guide](./references/spec-sections-guide.md):** Read and load the full contents of this file now. Use it to infer the document section structure when the user has not specified one, and to validate that any user-specified structure is complete. Apply the section selection heuristics it defines to choose which supplementary sections are appropriate for this spec.

- **[content-standards](./references/content-standards.md):** Read and load the full contents of this file now. Apply every rule defined there — customer value framing, precision and unambiguous language, correct PM terminology, completeness, consistent formatting, and tone — to every section of the document. These are non-negotiable defaults unless the user has explicitly instructed otherwise.

**3c. Writing calibration** (derived from confirmed inputs):
- **Target audience framing**: minimize jargon for executive/leadership audiences; be technically precise for engineering audiences; adjust tone and terminology accordingly
- **Detail level**:
  - *High-level*: concise summaries, no granular sub-details, implementation specifics, or edge-case conditions; favor breadth over depth
  - *Detail-oriented*: expand each bullet with rationale, sub-cases, examples, implications, and cross-functional considerations
  - *No clear signal*: balanced depth appropriate for a standard product spec

---

### Step 4 — Write

Execute the writing brief assembled in Step 3 exactly. Do not make new decisions here — all decisions were finalized in Step 3.

For each section:
1. Expand the content bullets into polished prose or structured lists, calibrated to the confirmed detail level and audience
2. Add necessary context, rationale, or implications the bullets imply but didn't state, as long as they are consistent with the user's confirmed answers
3. Apply the formatting rules from the content standards (3b) consistently throughout

---

### Step 5 — Review

Silently go through every requirement recorded in the Step 3 writing brief and verify it is met in the written document.

**From Step 3a — User requirements:**
- [ ] Every content bullet from Step 1 is addressed — none dropped or ignored
- [ ] All sections in the confirmed structure are present and complete
- [ ] Target audience is correctly reflected in tone, terminology, and framing
- [ ] Detail level is consistent throughout every section

**From Step 3b — Skill standards:**
- [ ] Customer value framing is present in all feature/use case descriptions
- [ ] No vague or ambiguous language remains
- [ ] PM terminology is correct and used consistently
- [ ] No section is incomplete or contains unanswered implicit questions

**From Step 3c — Writing calibration:**
- [ ] Audience framing is applied correctly (jargon level, tone, terminology)
- [ ] Depth of every section matches the confirmed detail level
- [ ] Formatting is uniform throughout (headings, bullets, tables)

If any check fails, fix the issue before proceeding to Step 6.

---

### Step 6 — Output

Output the complete spec as clean Markdown, ready to be copied into a doc or reviewed directly. Do not add meta-commentary, preamble, or explanations — output the document itself.
