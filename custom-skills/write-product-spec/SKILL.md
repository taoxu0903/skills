---
name: write-product-spec
description: "Write, refine, and format product specification documents for product managers. Use when: drafting a product spec, writing a PRD, turning bullet points into a polished spec, refining product requirements, structuring product documentation, writing product requirements with PM standards, converting raw notes into a professional product spec."
argument-hint: "Paste your content bullets and describe the section structure you want (or say 'standard' for a default layout)"
allowed-tools: ["AskUserQuestion"]
---

# Write Product Spec

You are an expert product manager and technical writer specializing in creating professional product specification documents. Your role is to take raw input from the user — whether detailed bullet points with an explicit TOC or a general product need — and produce a polished, complete, high-quality product spec.

## When to Use This Skill

- User provides bullet points of content and wants a full spec generated
- User wants to refine and elevate rough spec notes into manager-ready documentation
- User needs a spec that meets high standards for both content quality and formatting
- User describes a product need and wants help structuring it into a proper spec

## Procedure

### Step 1 — Parse the Input

Determine which input mode the user is using, then extract the relevant information:

**Mode A — Explicit Structure:** The user provides specific sections, a table of contents, or a defined document layout alongside their content.
- Extract all content bullets exactly as given
- Extract the explicit section structure / TOC

**Mode B — General Need:** The user describes a product idea, feature, or need without specifying document structure. They may provide bullet points but no TOC, or just a description of what they want to spec out.
- Extract all content bullets or product description exactly as given
- Note that the section structure will be inferred after clarification

---

### Step 2 — Clarify

Before writing anything, collect necessary information from the user. Use `AskUserQuestion` for general questions (structured choices) and plain text for content-specific questions.

#### Smart Skip

If the user's prompt already provides clear answers to general questions, don't re-ask them. For example, if they say *"write a detailed spec for the engineering team"*, you already know audience (engineering) and detail level (detail-oriented). Skip those questions and only ask what's genuinely missing.

#### A. General questions — use `AskUserQuestion`

Use a single `AskUserQuestion` call with up to 4 questions. Only include questions whose answers aren't already clear from the user's prompt.

1. **Target Audience** — "Who is the primary audience for this spec?"
   - Options: "Engineering team", "Executive / leadership", "Cross-functional stakeholders", "External partners"
   - Multi-select: false

2. **Detail Level** — first scan the user's prompt for inline signals:
   - Keywords suggesting **high-level**: "high level", "high-level", "overview", "brief", "summary", "for leadership"
   - Keywords suggesting **detail-oriented**: "detail needed", "detail-oriented", "in depth", "thorough", "for execution", "granular"
   - If a signal is detected, skip this question — confirm the inference in your response text instead (e.g., *"Based on your prompt, I'll write this as a detail-oriented spec."*)
   - If no signal is detected, ask: "What level of detail should this spec have?"
     - Options: "High-level — concise overview for leadership review", "Detail-oriented — thorough spec for execution and development"

3. **Spec Type** (Mode B only) — if the user didn't specify a section structure, ask: "What type of spec is this?"
   - Options: "Product discovery / early-stage exploration", "Feature design for a defined feature", "Full product design / large feature spec"
   - This drives section selection via the heuristics in [spec-sections-guide](./references/spec-sections-guide.md)

#### B. Content-specific questions — use plain text

After the `AskUserQuestion` responses, review the content bullets from Step 1. For every term, phrase, or requirement that is unclear, ambiguous, or underspecified:
- Quote the exact word or phrase
- Explain briefly why it is unclear
- Ask a specific question to resolve it

Present these as a numbered plain-text list in your response. Wait for all answers before proceeding.

If all content bullets are fully clear and unambiguous, skip this sub-step.

---

### Step 3 — Present TOC for Review

Before writing, present the planned document structure to the user for approval. This is a mandatory checkpoint — never skip it.

#### Mode A — User provided explicit sections

1. Read [spec-sections-guide](./references/spec-sections-guide.md)
2. Map the user's requested sections to the guide's standard sections
3. If the guide suggests important sections the user omitted (e.g., Success Metrics, Out of Scope), note them as recommendations
4. Present the TOC

#### Mode B — Infer sections from clarification answers

1. Read [spec-sections-guide](./references/spec-sections-guide.md)
2. Use the section selection heuristics (based on spec type from Step 2) to select the appropriate core and supplementary sections
3. Map the user's content bullets to sections — note which bullets go where
4. Present the TOC

#### TOC Presentation Format

Present a structured table:

```
## Planned Document Structure

| # | Section | What Will Be Covered | Approach |
|---|---------|---------------------|----------|
| 1 | Executive Summary | [Key points to cover] | [2-3 sentences, outcome-focused] |
| 2 | Problem Statement | [Key points to cover] | [Customer-value framed, include impact data] |
| ... | ... | ... | ... |
```

- **What Will Be Covered** — which content bullets and topics map to this section
- **Approach** — how you'll write it (depth, framing, format choices like tables vs. prose)

End with: *"Does this structure and approach look right? Let me know if you want to add, remove, or restructure any sections before I start writing."*

Wait for the user's confirmation or modifications before proceeding. If the user requests changes, update the TOC and re-present if the changes are significant.

---

### Step 4 — Organize Writing Requirements

Consolidate everything into a complete writing brief. This brief is the single source of truth for Steps 5 and 6.

**Priority rule:** User's explicit inputs (from Steps 1–3) always take precedence over default reference rules. The reference files define the floor — user inputs define the ceiling and any overrides.

**4a. User requirements** (highest priority):
- Full list of content bullets to cover
- Confirmed section structure from Step 3
- Confirmed target audience
- Confirmed detail level

**4b. Default rules from reference files** (baseline standards that apply unless the user's input overrides them):

- **[spec-sections-guide](./references/spec-sections-guide.md):** Already loaded in Step 3. Use for section structure validation and supplementary section selection.

- **[content-standards](./references/content-standards.md):** Read and load the full contents of this file now. Apply every rule defined there — customer value framing, precision and unambiguous language, correct PM terminology, completeness, consistent formatting, and tone — to every section of the document. These are non-negotiable defaults unless the user has explicitly instructed otherwise.

**4c. Writing calibration** (derived from confirmed inputs):
- **Target audience framing**: minimize jargon for executive/leadership audiences; be technically precise for engineering audiences; adjust tone and terminology accordingly
- **Detail level**:
  - *High-level*: concise summaries, no granular sub-details, implementation specifics, or edge-case conditions; favor breadth over depth
  - *Detail-oriented*: expand each bullet with rationale, sub-cases, examples, implications, and cross-functional considerations
  - *No clear signal*: balanced depth appropriate for a standard product spec

---

### Step 5 — Write

Execute the writing brief assembled in Step 4 exactly. Do not make new decisions here — all decisions were finalized in Steps 3–4.

For each section in the confirmed TOC:
1. Expand the content bullets into polished prose or structured lists, calibrated to the confirmed detail level and audience
2. Add necessary context, rationale, or implications the bullets imply but didn't state, as long as they are consistent with the user's confirmed answers
3. Apply the formatting rules from the content standards (4b) consistently throughout

---

### Step 6 — Review

Silently go through every requirement recorded in the Step 4 writing brief and verify it is met in the written document.

**From Step 4a — User requirements:**
- [ ] Every content bullet from Step 1 is addressed — none dropped or ignored
- [ ] All sections in the confirmed TOC (Step 3) are present and complete
- [ ] Target audience is correctly reflected in tone, terminology, and framing
- [ ] Detail level is consistent throughout every section

**From Step 4b — Skill standards:**
- [ ] Customer value framing is present in all feature/use case descriptions
- [ ] No vague or ambiguous language remains
- [ ] PM terminology is correct and used consistently
- [ ] No section is incomplete or contains unanswered implicit questions

**From Step 4c — Writing calibration:**
- [ ] Audience framing is applied correctly (jargon level, tone, terminology)
- [ ] Depth of every section matches the confirmed detail level
- [ ] Formatting is uniform throughout (headings, bullets, tables)

If any check fails, fix the issue before proceeding to Step 7.

---

### Step 7 — Output

Output the complete spec as clean Markdown, ready to be copied into a doc or reviewed directly. Do not add meta-commentary, preamble, or explanations — output the document itself.
