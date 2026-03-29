# Product Spec Content Standards

These are the quality requirements that must be met in every product spec produced by this skill. They reflect the standards expected by senior stakeholders and managers reviewing the document.

---

## 1. Customer Value Framing (Mandatory)

Every feature, use case, scenario, or requirement scoped into the product must be stated in terms of the value it delivers to the customer. This is non-negotiable.

**Pattern to follow:** `[User/persona] can [do X] so that [they achieve Y outcome / avoid Z problem].`

**Wrong:** "The system will support bulk CSV upload."
**Right:** "Operations managers can upload customer records in bulk via CSV, eliminating the manual entry that currently causes 2–3 hours of data prep per onboarding cycle."

Apply this framing in:
- Problem statements
- Feature descriptions
- Use case narratives
- Acceptance criteria
- Success metrics rationale

---

## 2. Precision and Unambiguous Language

Every statement must be specific enough that a reader cannot reasonably misinterpret it.

Rules:
- Avoid: "fast", "easy", "flexible", "robust", "seamless", "improved" — these are unmeasurable
- Replace with quantified or bounded language: "response time under 2 seconds", "configurable by an admin without engineering involvement"
- When scope is bounded, state it explicitly: "This applies to web only; mobile is out of scope for v1"
- When a term has multiple meanings in context, define it on first use

---

## 3. Correct PM Terminology

Use standard PM terminology correctly and consistently:

| Term | Correct Use |
|---|---|
| **Epic** | A large body of work that can be broken into stories |
| **User Story** | "As a [persona], I want [capability] so that [outcome]" format |
| **Acceptance Criteria** | Specific, testable conditions that define "done" for a requirement |
| **OKR** | Objective + 3–5 measurable Key Results; objective is aspirational, KRs are quantified |
| **KPI** | Ongoing metric that tracks health of a feature or product area |
| **MVP** | Minimum set of capabilities that delivers customer value and can be shipped |
| **Persona** | Named, archetypal user with defined goals, context, and pain points |
| **Success Metric** | Measurable outcome that confirms the feature/product is working as intended |
| **Assumption** | A belief held as true for planning purposes that has not been validated |
| **Constraint** | A non-negotiable boundary (technical, legal, resource, time) |
| **Dependency** | An external team, system, or deliverable the spec's delivery depends on |

Do not use these terms loosely or interchangeably.

---

## 4. Completeness — No Implicit Gaps

A complete spec leaves no section with implicit, unanswered questions that a reader would naturally ask.

For each scoped feature or requirement, ensure the following are either answered or explicitly flagged as open questions:
- **Who** is the target user / persona?
- **What** exactly is the capability or change?
- **Why** does it matter — what customer problem does it solve?
- **How will success be measured?** — at least one metric
- **What is out of scope?** — explicitly stated, not assumed
- **What are the dependencies or risks?**

If information is genuinely unknown, place it in `## Open Questions` with an owner and target resolution date if possible.

---

## 5. Consistent Formatting

Apply consistent formatting throughout the document:

- **Headings:** Use `##` for top-level sections, `###` for subsections, `####` for sub-subsections. Never skip levels.
- **Bullets:** Use `-` for unordered lists. Keep bullets parallel in grammatical structure within a list.
- **Tables:** Use tables when comparing options, listing attributes of multiple items, or showing structured data (e.g., personas, metrics, dependencies).
- **Bold:** Use `**bold**` for key terms on first use, and for field labels in tables or forms.
- **No walls of text:** Break paragraphs at 4–5 sentences max. Use bullets or tables for lists of 3+ items.
- **Numbered lists:** Use only for ordered steps or ranked items. Do not use numbers for unordered content.

---

## 6. Tone — Professional and Direct

- Professional but not bureaucratic: write for a smart reader, not a legal document
- Direct: lead with the point, then provide supporting context
- Active voice preferred: "The system sends a confirmation email" not "A confirmation email is sent by the system"
- Avoid hedging language unless uncertainty is intentional: "might", "could potentially", "in some cases" weaken specs unless they're genuinely capturing uncertainty
- First person is acceptable for rationale or intent statements in the author's voice; third person for requirements and system behavior
