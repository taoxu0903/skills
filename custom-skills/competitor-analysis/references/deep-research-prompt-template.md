# Deep Research Prompt Template

When delegating to ChatGPT Deep Research, generate a prompt by filling in this template. Replace every `[PLACEHOLDER]` with the user's actual inputs. Remove any sections for dimensions the user didn't select.

The quality of this prompt directly determines the quality of ChatGPT's output. The template is designed to:
- Activate ChatGPT's Deep Research mode explicitly
- Provide enough structure for consistent output without over-constraining the research
- Request source attribution so findings can be cross-referenced during synthesis
- Match our report format headers so synthesis is straightforward

---

## Template

Fill in the bracketed placeholders below, then send the entire block to ChatGPT.

```
I need a comprehensive competitive analysis using Deep Research. Please conduct thorough, multi-source research across the web for each competitor listed below.

## Competitors to Analyze

[LIST EACH COMPETITOR AS A BULLET — include their URL if known]
- **CompanyA** (https://companya.com)
- **CompanyB** (https://companyb.com)

## Analysis Scope

[PICK ONE OF THE TWO PARAGRAPHS BELOW — delete the other]

OPTION A (Full Scope):
Analyze the current state of each competitor — their latest product offerings, most recent features, current pricing, and overall market positioning as of today.

OPTION B (Time-Bounded):
Focus specifically on the period: [SPECIFY PERIOD, e.g., "March 2026", "last 30 days", "Q1 2026"]. I want to understand what changed, launched, or shifted during this window. Include any announcements, releases, pricing changes, or strategic moves that occurred in this timeframe.

## Dimensions to Cover

For each competitor, research and report on:

[INCLUDE ONLY THE DIMENSIONS THE USER SELECTED — delete the rest]

### Product & Features
Core product description, key features, recent releases (with dates), notable strengths, and gaps compared to alternatives. Check their product pages, changelogs, release notes, and blog posts.

### Pricing & Packaging
Pricing model (per-seat, usage-based, freemium, etc.), tier breakdown (Free/Pro/Enterprise), recent pricing changes. Check their pricing pages and any third-party comparisons.

### Positioning & Messaging
Target audience, core value proposition, messaging tone, claimed differentiators. Review their homepage, about page, and marketing materials.

### Market Signals
Recent funding rounds, valuation signals, notable hires or job postings (especially leadership and engineering), partnerships, acquisitions, geographic expansion. Check Crunchbase, LinkedIn, news outlets, and press releases.

## Output Format

Structure your response as a markdown document with these exact sections:

# Competitor Analysis Report (ChatGPT Deep Research)

**Date:** [today's date]
**Period:** [Full Scope or the specified time window]
**Competitors:** [list]

## Executive Summary
3-5 sentences: the most important takeaway, biggest competitive shift, overall landscape trajectory.

## Competitor Deep Dives

### [Competitor Name]
#### [Dimension — e.g., Product & Features]
- Bulleted findings with specifics (feature names, dates, numbers)

[Repeat for each selected dimension, then repeat for each competitor]

## Comparative Matrix

| Dimension | [Comp A] | [Comp B] | [Comp C] | ... |
|-----------|----------|----------|----------|-----|
[One row per key comparison point, cells kept to 1-2 phrases]

## Strategic Implications
- What threats emerge from this analysis?
- Where are competitors weak — what opportunities exist?
- What patterns appear across multiple competitors?
- 3-4 actionable recommendations

## Sources
Number each source with its URL so I can verify findings:
1. [Source title](URL)
2. ...

## Important Instructions
- Prioritize PRIMARY sources (official product pages, pricing pages, press releases, blog posts) over secondary sources (review sites, aggregators)
- Include specific dates, numbers, and version names whenever available
- If information is uncertain or conflicting across sources, note the uncertainty rather than picking one
- For time-bounded analysis, clearly distinguish between what existed before the period vs. what's new
- Cast a wide net — check product blogs, changelogs, Twitter/X announcements, LinkedIn posts, Crunchbase, G2, job postings, and news outlets
```

---

## How to Fill the Template

1. **Competitor list** — Replace the example bullets with the user's actual competitors. Include URLs if known; just the name is fine if not.

2. **Analysis scope** — Keep only the relevant paragraph (Full Scope or Time-Bounded) and delete the other. Fill in the time period if applicable.

3. **Dimensions** — Keep only the sections for dimensions the user selected. Delete the rest entirely to keep the prompt focused.

4. **Output format** — This section stays as-is. Don't modify the structure requests — they match our report template for easy synthesis.

## Tips for Maximum Quality

- If the user mentioned their own product, add a line: "For context, our product is [X] and we compete primarily on [Y]. Frame strategic implications relative to our positioning."
- If specific competitor URLs are known, include them to help ChatGPT start research at the right place
- For time-bounded analysis, mention the previous analysis date if available: "Our last analysis was on [date], so focus on what changed since then"
