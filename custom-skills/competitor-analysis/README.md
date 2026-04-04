# Competitor Analysis Skill

A three-phase workflow for structured, repeatable competitor analysis — built for Product Managers who need regular competitive intelligence.

## Quick Start

```
/competitor-analysis
```

Or just describe what you need:
- *"Compare Asana, Monday.com, and ClickUp on features and pricing"*
- *"Who are the top players in the AI writing tools market?"*
- *"What changed with our competitors in the last 30 days?"*
- *"Synthesize my two competitor reports"*

## How It Works

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

### Phase 1: Clarify

The skill gathers your requirements before doing any research:

| Question | What It Controls |
|----------|-----------------|
| **Competitors** | Which 2-8 products to analyze. If you don't know the names, the skill discovers them for you (see Discovery Mode below). |
| **Dimensions** | What to analyze: Product & Features (default), Pricing & Packaging, Positioning & Messaging, Market Signals |
| **Period** | Full scope (latest state) or time-bounded (e.g., "last 30 days", "Q1 2026") |
| **Execution path** | Option A (Claude), Option B (ChatGPT Deep Research), or Option C (both + synthesis) |

**Smart Skip:** If your prompt already contains the answers (e.g., *"compare Figma vs Sketch on features for last 30 days"*), the skill skips redundant questions and goes straight to the execution path choice.

### Phase 2: Execute

A single, well-crafted research prompt is generated from your inputs. The **same prompt** is used regardless of which execution path you choose — this ensures consistency and makes synthesis meaningful.

| Option | How It Works | Speed | Depth |
|--------|-------------|-------|-------|
| **A: Claude** | Web search via tavily-search + page reading via WebFetch | 2-5 min | 10-20 sources/competitor |
| **B: ChatGPT** | Prompt sent to ChatGPT Deep Research via browser automation | 5-30 min | 50-200 sources |
| **C: Both** | Same prompt executed by both, then merged in Phase 3 | Longest | Highest quality |

**Research depth per competitor:**
1. Official changelog / release notes
2. Pricing page
3. Product/features page
4. Official documentation (discovered via tavily-search)
5. At least 3 third-party sources (G2, TechCrunch, Crunchbase, Reddit, etc.)

### Phase 3: Synthesize

When both Claude and ChatGPT reports exist, the skill merges them into:

- **Consolidated MD report** — cross-referenced findings with `[Claude]` / `[ChatGPT]` / `[Both]` attribution and confidence scoring
- **Executive HTML slides** — 5-slide deck (title, summary, matrix, changes, recommendations)

## Discovery Mode

Don't know who your competitors are? Just describe your market:

- *"Analyze the developer analytics market"*
- *"Who are the top AI writing assistants?"*
- *"I'm building a design tool — who should I watch?"*

The skill uses tavily-search to find the top 5-10 players, presents them for your confirmation, and then proceeds with the full analysis.

## Output Files

All reports are saved to `./competitor-analysis/` with timestamps:

| File | When |
|------|------|
| `claude-report-YYYY-MM-DD.md` | After Claude execution (Option A/C) |
| `chatgpt-report-YYYY-MM-DD.md` | After ChatGPT execution (Option B/C) |
| `consolidated-report-YYYY-MM-DD.md` | After synthesis (Option C) |
| `executive-summary-*-YYYY-MM-DD.html` | Async slides from any report |
| `deep-research-prompt-YYYY-MM-DD.md` | Fallback if ChatGPT browser automation fails |

## Change Tracking

Reports accumulate in `./competitor-analysis/`. On each new run, the skill diffs against the most recent previous report and adds a **Changes Since Last Analysis** section with:

- `[NEW]` — new features, products, pricing tiers, partnerships
- `[CHANGED]` — modifications to existing features, pricing, messaging
- `[REMOVED]` — deprecated features, discontinued tiers

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **One prompt for both Claude and ChatGPT** | Ensures apples-to-apples comparison during synthesis |
| **Slides generated async** | Never blocks you — MD report is delivered immediately, slides appear in background |
| **Tavily for doc discovery** | Finds documentation pages dynamically instead of guessing URL patterns |
| **3+ third-party sources required** | Official sources tell you what a product claims; third-party sources tell you the truth |

## Dependencies

- **tavily-search** skill — web search for research and doc discovery
- **agent-browser** skill — ChatGPT browser automation (Option B/C)
- **html-slides** skill — executive summary slide generation
- `TAVILY_API_KEY` environment variable must be set

## Example Workflow

```
You:    /competitor-analysis
Skill:  Which competitors? → Notion, Coda, Roam Research
        Dimensions? → Product & Features, Pricing
        Period? → Last 30 days
        Here's the research plan. Execute with Claude, ChatGPT, or both?
You:    Option C — both
Skill:  [Claude researches via web search → saves claude-report]
        [Slides generating in background...]
        [ChatGPT Deep Research running via browser → saves chatgpt-report]
        [Slides generating in background...]
        [Synthesizing both reports → saves consolidated-report]
        [Final slides generating in background...]
        ✓ Done. Reports in ./competitor-analysis/
```
