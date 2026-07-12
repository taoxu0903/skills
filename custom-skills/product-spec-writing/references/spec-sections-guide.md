# Product Spec — Standard Sections Guide

Use this guide when the user does not specify a section structure, or says "standard layout". Select the sections most relevant to the spec's scope — not every section is required for every document. Use judgment based on the content provided.

---

## Core Sections (Include in Most Specs)

### 1. Document Header / Metadata
Minimal block at the top of every spec. Include:
- **Product / Feature Name**
- **Author**
- **Status** (Draft / In Review / Approved)
- **Last Updated**
- **Stakeholders / Reviewers**

### 2. Executive Summary
2–4 sentences. Answer: What is this, why does it matter, and what outcome are we targeting? Written for a reader who may not read further.

### 3. Problem Statement
Describe the customer problem being solved. Include:
- Who is affected (persona or user segment)
- What the current experience is and why it fails them
- The magnitude or business impact of the problem (data, qualitative insight, or reasoned proxy)

Avoid jumping to solutions here — stay in problem space.

### 4. Goals and Non-Goals
**Goals:** What this spec aims to achieve. State as outcomes, not features. Link to OKRs or KPIs where applicable.

**Non-Goals:** Explicitly what is *not* being solved here. Prevents scope creep and misaligned expectations.

### 5. Target Users / Personas
Define who this product or feature is for. For each persona:
- Name / role
- Context (what they're trying to accomplish, their environment)
- Key pain points this spec addresses

### 6. Solution Overview
A concise description of the proposed solution. This is narrative, not a feature list. Explain the approach and how it addresses the problem statement. Include a high-level flow or interaction model if helpful.

### 7. Detailed Requirements
The core of the spec. Break down by feature, epic, or user journey. For each item:
- **User Story** or requirement statement (customer-value framed)
- **Acceptance Criteria** — specific, testable conditions
- **Priority** — Must Have / Should Have / Nice to Have (MoSCoW) or P0/P1/P2
- **Notes / Context** — any constraints, edge cases, or implementation guidance

Use `###` subheadings to organize by feature area or epic.

### 8. Success Metrics
How will you know this worked? For each goal, define:
- The metric (KPI, event, rate, count)
- The baseline (current state)
- The target (what success looks like)
- The measurement method (analytics event, survey, support ticket reduction, etc.)

### 9. Out of Scope
A bulleted list of explicitly excluded capabilities or use cases for this version. Include a brief rationale where useful (e.g., "deferred to v2 pending infrastructure readiness").

---

## Supplementary Sections (Include When Relevant)

### 10. User Flow / Key Scenarios
Step-by-step narrative of how a user completes a key task using this feature. Use numbered steps. Include the happy path first, then notable edge cases or error states.

### 11. Dependencies
What does delivery of this spec depend on? Include:
- External teams or systems
- Other features or specs that must ship first
- Data, infrastructure, or legal/compliance prerequisites

### 12. Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Describe risk | High/Med/Low | High/Med/Low | How you'll reduce or respond |

### 13. Assumptions
Beliefs held as true for planning purposes that have not yet been validated. Flag high-risk assumptions explicitly. Each assumption should eventually be validated or falsified before shipping.

### 14. Open Questions
Unresolved issues that need answers before or during development. Format:

| Question | Owner | Target Date |
|---|---|---|
| What should happen if the user... | PM Name | YYYY-MM-DD |

### 15. Appendix / References
Links to related docs, research, designs, prior specs, or technical references.

---

## Section Selection Heuristics

| Spec Type | Typically Include |
|---|---|
| product Discovery / early-stage | Problem, goals/non-goals, personas, open questions |
| feature design | Summary, problem, requirements, metrics, out of scope |
| product design / large feature | All core + flows, dependencies, risks, assumptions |

