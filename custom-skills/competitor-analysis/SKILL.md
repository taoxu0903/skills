---
name: competitor-analysis
description: |
  Run structured competitor analysis for product managers. Use this skill whenever the user wants to compare competitors, analyze competitive landscape, track competitor changes, benchmark against rivals, or understand market positioning. Trigger phrases include: 'competitor analysis', 'competitive analysis', 'compare competitors', 'market analysis', 'competitive landscape', 'competitor tracking', 'how does X compare to Y', 'what are competitors doing', 'competitive intel', 'market comparison', 'synthesize reports', 'who are the competitors in [market]', 'find competitors for [product]', 'landscape analysis', 'top players in [domain]', 'market map'. Also trigger when the user asks to combine or merge two competitor reports, asks about changes since the last competitive analysis, or wants to discover who the key players are in a product category before analyzing them.
---

# Competitor Analysis

A three-phase workflow for structured, repeatable competitor analysis. This skill produces markdown reports, tracks changes over time, and can delegate deep research to ChatGPT via browser automation when deeper investigation is needed.

## How This Skill Works

```
Phase 1: CLARIFY           Phase 2: EXECUTE                Phase 3: SYNTHESIZE
┌──────────────────┐     ┌─────────────────────────┐     ┌─────────────────────┐
│ Ask:             │     │ A: Claude researches    │     │ Merge both reports  │
│ - Competitors    │────>│    via web search       │────>│ into:               │
│ - Dimensions     │     │ B: Delegate to ChatGPT  │     │ - Consolidated MD   │
│ - Time period    │     │    Deep Research         │     │ - Executive slides  │
│ - Confirm plan   │     │ C: Both A + B           │     │ - Change diff       │
└──────────────────┘     └─────────────────────────┘     └─────────────────────┘
```

The user always chooses the execution path after reviewing a structured plan. All reports are stored in `./competitor-analysis/` with timestamps for change tracking across runs.

---

## Phase 1: Clarification

Before doing any research, gather the user's requirements. This phase ensures the analysis is focused and useful.

### Smart Skip

If the user's prompt already provides clear answers to the clarification questions, don't re-ask them. For example, if they say *"compare Figma vs Sketch on features for last 30 days"*, you already know:
- Competitors: Figma, Sketch
- Dimensions: Product & Features
- Period: last 30 days

In this case, skip straight to **Step 2** (present the research plan and confirm execution path). Only ask questions for information that's genuinely missing. The research plan confirmation (Option A / B / C) is always shown — never skip that.

**Discovery mode detection:** If the user describes a market/domain without naming specific competitors (e.g., "analyze the AI writing tools market", "who are we competing against in developer analytics?"), enter discovery mode in Step 1 instead of asking them to list competitors.

### Step 1: Gather Competitors and Dimensions

Use `AskUserQuestion` to ask these questions in a single call:

**Question 1 — Competitors:**
"Which competitors should I analyze? (List 2-8 products or companies)"
- This should be a free-text "Other" response — don't predefine options since the competitors vary per user

**Discovery mode — when the user doesn't know the competitors:**

Sometimes the user knows the product domain but not the specific competitors (e.g., "I'm building a design tool" or "analyze the project management market"). In this case:

1. Ask the user to describe their product domain / market category (e.g., "collaborative design tools", "developer analytics platforms", "AI writing assistants")
2. Use `tavily-search` to discover the top players:
   - Search queries like: `"top [domain] tools 2026"`, `"best [domain] software comparison"`, `"[domain] market landscape"`
   - Use `--max-results 10` to cast a wide net
   - Cross-reference across multiple search results to identify which names appear most frequently
3. Compile a ranked list of 5-10 competitors with a one-line description of each
4. Present the list to the user via `AskUserQuestion` as a **multi-select** — let them pick which ones to include in the analysis and add any that were missed
5. Once confirmed, proceed with the selected competitors through the rest of Phase 1 (dimensions, period, execution path)

**Question 2 — Analysis Dimensions** (multi-select):
- Product & Features — feature comparison, new releases, product roadmap signals
- Pricing & Packaging — pricing models, tiers, free vs paid, enterprise pricing
- Positioning & Messaging — target audience, messaging, brand voice, differentiators
- Market Signals — hiring patterns, funding rounds, partnerships, acquisitions

Default: Product & Features is always relevant. Let the user add more.

**Question 3 — Analysis Period:**
- Full scope — analyze the latest state of each product across all dimensions (best for first-time or quarterly analysis)
- Time-bounded — focus on a specific window (e.g., "last 30 days", "March 2026", "Q1 2026"). Ask the user to specify the period. Best for monthly cadence tracking.

### Step 2: Generate the Research Prompt and Choose Execution Path

After gathering inputs, generate a single, well-crafted research prompt using the template in `references/deep-research-prompt-template.md`. This prompt is the central artifact of the skill — it defines the exact scope, dimensions, and output structure for the analysis. **The same prompt is used regardless of which execution path the user chooses**, ensuring consistency and making synthesis meaningful when both paths are run.

Present the completed prompt to the user as a structured research plan, then ask them to choose the execution path:

- **Option A: Execute with Claude** — Claude uses this prompt as its research brief, executing it via web search (tavily-search) and web fetch. Fast (2-5 minutes), good for regular cadence. Moderate research depth (10-20 sources per competitor).
- **Option B: Delegate to ChatGPT Deep Research** — The same prompt is sent to ChatGPT via browser automation. Slower (5-30 minutes) but much deeper research (50-200 sources). Best for thorough deep dives.
- **Option C: Run both, then synthesize** — The same prompt is executed by both Claude and ChatGPT. Because both work from identical instructions, the synthesis in Phase 3 becomes a true apples-to-apples comparison. Recommended for quarterly or strategic reviews.

---

## Phase 2A: Internal Execution (Claude)

This phase runs when the user picks Option A or Option C.

### Research Process

Use the research prompt generated in Phase 1 Step 2 as your research brief. For each competitor and dimension specified in the prompt:

1. Use the `tavily-search` skill for web search. Structure queries like:
   - Full scope: `"[Competitor] [dimension] 2026"`, `"[Competitor] product features"`, `"[Competitor] pricing plans"`
   - Time-bounded: `"[Competitor] new features [month] [year]"`, `"[Competitor] releases [period]"`, `"[Competitor] updates [period]"`
2. Use `WebFetch` to read full pages for key sources (pricing pages, changelogs, product announcement blogs)
3. Cross-reference findings across multiple sources — don't rely on a single source for any claim

### Research Depth Guidelines

- Aim for 3-5 search queries per competitor per dimension
- For **every competitor**, always attempt to check these primary sources:
  1. **Official changelog / release notes** — the ground truth for what shipped and when
  2. **Pricing page** — current tiers, packaging, any "contact sales" signals
  3. **Product/features page** — how they describe their own capabilities
  4. **Official documentation** — this is where the real detail lives. Marketing pages tell you feature names; docs tell you what features actually do, their limitations, tier availability, and integration depth. Use `tavily-search` to find documentation pages (e.g., `"[Competitor] documentation [dimension]"`, `"[Competitor] API docs"`, `"[Competitor] help center features"`) rather than guessing URL patterns. Then use `WebFetch` to read the most relevant doc pages for the dimensions being analyzed.
  5. **At least 3 third-party sources** — use `tavily-search` with 1-2 broad queries per competitor (e.g., `"[Competitor] review 2026"`, `"[Competitor] vs alternatives"`) with `--max-results 5-10` to efficiently surface multiple perspectives. Look for G2/Capterra reviews, analyst coverage (TechCrunch, The Verge, Protocol), Crunchbase profiles, and community discussions (Reddit, HackerNews). Third-party sources provide the outside perspective that official sources never will — what users actually complain about, how reviewers rank the product, and what analysts think of the strategy.
- For time-bounded analysis, additionally search for blog posts, Twitter/X announcements, and press releases within the specified window
- If a primary source is inaccessible, note it in the Sources section rather than silently omitting it

### Report Output

Save to `./competitor-analysis/claude-report-YYYY-MM-DD.md`

Read `references/report-template.md` for the exact format to follow.

### Executive Slides (Async)

Immediately after saving the Claude report, launch a **background agent** to generate executive summary slides using the `html-slides` skill. Do not wait for the slides to complete before continuing — tell the user the report is ready and that slides are being generated in the background. Save as `./competitor-analysis/executive-summary-claude-YYYY-MM-DD.html`.

### Change Tracking

Before writing the report, check `./competitor-analysis/` for previous reports (look for the most recent `claude-report-*.md` or `consolidated-report-*.md`). If one exists:

1. Read the previous report
2. Compare findings across each competitor and dimension
3. Add a `## Changes Since Last Analysis` section with tagged changes:
   - `[NEW]` — entirely new features, products, pricing tiers, partnerships
   - `[CHANGED]` — modifications to existing features, pricing adjustments, messaging shifts
   - `[REMOVED]` — deprecated features, discontinued tiers, ended partnerships

---

## Phase 2B: ChatGPT Deep Research Delegation

This phase runs when the user picks Option B or Option C.

### Step 1: Use the Research Prompt

The research prompt was already generated in Phase 1 Step 2. This is the same prompt used for Claude execution — ensuring both sources research the identical scope for fair synthesis. No need to regenerate it.

### Step 2: Automate via Browser

Use the `agent-browser` skill to:

1. Navigate to `chatgpt.com`
2. Start a new conversation
3. Paste the research prompt generated in Phase 1
4. Wait for the deep research to complete (this can take 5-30 minutes — ChatGPT's Deep Research shows a progress indicator)
5. Extract the full response text
6. Save to `./competitor-analysis/chatgpt-report-YYYY-MM-DD.md`

**Graceful fallback:** If browser automation fails (login issues, UI changes, timeouts), save the prompt to `./competitor-analysis/deep-research-prompt-YYYY-MM-DD.md` and tell the user:
> "I couldn't automate ChatGPT directly. I've saved the prompt to `./competitor-analysis/deep-research-prompt-YYYY-MM-DD.md`. Please paste it into ChatGPT Deep Research manually, then save the result as `./competitor-analysis/chatgpt-report-YYYY-MM-DD.md` and ask me to synthesize."

### Executive Slides (Async)

Once the ChatGPT report is saved, launch a **background agent** to generate executive summary slides from it. Do not block on this — the user gets the MD report immediately. Save as `./competitor-analysis/executive-summary-chatgpt-YYYY-MM-DD.html`.

---

## Phase 3: Synthesis

This phase runs when:
- The user chose Option C (both reports are now ready)
- The user says "synthesize reports" or "merge reports"
- Both a `claude-report-YYYY-MM-DD.md` and `chatgpt-report-YYYY-MM-DD.md` exist for the same date in `./competitor-analysis/`

### Synthesis Process

1. Read both markdown reports
2. Create a consolidated report that:
   - **Cross-references** findings from both sources — identify where both agree (high confidence) and where they disagree (needs verification)
   - **Enriches** each section with the best details from each source
   - **Adds confidence scoring** to the comparative matrix: High (both sources agree), Medium (one source only), Low (sources conflict)
   - **Attributes insights** — mark each finding with its source: `[Claude]`, `[ChatGPT]`, or `[Both]`
   - **Combines source lists** into a unified, deduplicated bibliography
3. Save as `./competitor-analysis/consolidated-report-YYYY-MM-DD.md`

### Executive Summary Slides (Async)

After saving the consolidated report, launch a **background agent** to generate the final executive summary slide deck using the `html-slides` skill. This is the definitive slide deck — sourced from the enriched, cross-referenced consolidated report:

- **Slide 1:** Title slide — "Competitive Analysis: [Date]" with list of competitors analyzed
- **Slide 2:** Executive Summary — 3-5 key takeaways as bullet points
- **Slide 3:** Comparative Matrix — table showing all competitors across dimensions with confidence levels
- **Slide 4:** Changes Since Last Analysis — if previous reports exist, highlight key shifts (skip if first run)
- **Slide 5:** Strategic Recommendations — 3-4 actionable items for the product team

Save as `./competitor-analysis/executive-summary-consolidated-YYYY-MM-DD.html`. Do not block on slide generation — tell the user the consolidated report is ready and slides are being generated in the background.

---

## File Organization

All output goes to `./competitor-analysis/` (create the directory if it doesn't exist). File naming:

| File | When Created |
|------|-------------|
| `claude-report-YYYY-MM-DD.md` | Phase 2A (internal execution) |
| `chatgpt-report-YYYY-MM-DD.md` | Phase 2B (ChatGPT delegation) |
| `deep-research-prompt-YYYY-MM-DD.md` | Phase 2B fallback (prompt saved for manual use) |
| `consolidated-report-YYYY-MM-DD.md` | Phase 3 (synthesis) |
| `executive-summary-claude-YYYY-MM-DD.html` | Phase 2A (async slides from Claude report) |
| `executive-summary-chatgpt-YYYY-MM-DD.html` | Phase 2B (async slides from ChatGPT report) |
| `executive-summary-consolidated-YYYY-MM-DD.html` | Phase 3 (async slides from consolidated report) |

Previous reports in this directory are used for change tracking — don't delete them.

---

## Important Notes

- Phase 1 clarification uses `AskUserQuestion` — but only for information not already provided in the user's prompt (see Smart Skip above)
- For strategic analysis sections (Executive Summary, Strategic Implications, Recommendations), take extra time to reason deeply about competitive dynamics, second-order effects, and strategic implications rather than just listing facts
- The deep research prompt template in `references/deep-research-prompt-template.md` uses simple `[PLACEHOLDER]` markers — read it and fill them in rather than writing a prompt from scratch
- When the user asks to "synthesize" without having run both reports, check what exists in `./competitor-analysis/` and guide them on what's missing
- Executive slides can be generated from any report (single Claude report, single ChatGPT report, or consolidated synthesis) — not limited to Phase 3
