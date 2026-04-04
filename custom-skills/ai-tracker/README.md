# AI Tracker Skill

Your intelligence layer for tracking what's new with AI coding agents and AI models. Fetches official changelogs, enriches with third-party context, and generates structured roundup reports.

## Quick Start

```
/ai-tracker
```

Or ask naturally:
- *"What's new with coding agents this week?"*
- *"Any Claude or GPT model updates?"*
- *"What changed with Cursor and Copilot?"*
- *"Also check on Windsurf and Llama"*

## What It Tracks

### Default Coding Agents

| Agent | Official Source |
|-------|---------------|
| OpenClaw | [GitHub Releases](https://github.com/openclaw/openclaw/releases) |
| GitHub Copilot | [GitHub Blog Changelog](https://github.blog/changelog/label/copilot/) |
| Claude Code | [Changelog](https://code.claude.com/docs/en/changelog) |
| Codex | [Developer Changelog](https://developers.openai.com/codex/changelog) |
| Cursor | [Changelog](https://www.cursor.com/changelog) |
| Gemini CLI | [GitHub Releases](https://github.com/google-gemini/gemini-cli/releases) |

### Default Models

| Model Family | Provider | Official Source |
|-------------|----------|---------------|
| GPT | OpenAI | [ReleaseBot](https://releasebot.io/updates/openai/openai-models) |
| Claude | Anthropic | [ReleaseBot](https://releasebot.io/updates/anthropic/claude) |
| Gemini | Google | [ReleaseBot](https://releasebot.io/updates/google/gemini) |

### Custom Additions

Track anything beyond the defaults — just name it:
- *"Also check on Windsurf"* → discovered via tavily-search
- *"/ai-tracker cursor,gpt,llama"* → Cursor + GPT (defaults) + Llama (custom)

## How It Works

```
Pre-flight          Step 0             Steps 1-3              Output
┌──────────┐     ┌──────────────┐     ┌──────────────────┐    ┌────────────┐
│ Check    │────>│ Clarify:     │────>│ 1. Parallel      │───>│ Structured │
│ TAVILY   │     │ - Scope      │     │    WebFetch all   │    │ MD report  │
│ API_KEY  │     │ - Period     │     │    changelogs     │    │ + file     │
│          │     │ - Confirm    │     │ 2. Fetch The      │    │            │
└──────────┘     └──────────────┘     │    Batch Data     │    └────────────┘
                                      │ 3. Tavily search  │
                                      │    for enrichment  │
                                      └──────────────────┘
```

### Step 0: Clarify

Before any fetching, the skill confirms:
1. **Scope** — all defaults, agents only, models only, or specific names
2. **Time period** — this week (default), yesterday, last 2 weeks, this month

### Steps 1-3: Fetch & Enrich

1. **Parallel WebFetch** of all official changelogs for the selected products
2. **The Batch Data Points** — neutral industry source from deeplearning.ai
3. **Tavily search** — blog posts, user reactions, analyst commentary, and custom product lookups

### Filtering

The skill actively filters noise:

| Include | Skip |
|---------|------|
| New features, major releases | Bug fixes (unless catastrophic) |
| New model versions, benchmarks | Minor tweaks, refactors |
| Pricing changes, breaking changes | CI/CD changes, docs updates |
| Deprecations, integrations | Micro-optimizations |

## Output Format

Each product gets a structured table:

```markdown
## Claude Code
**Latest**: v1.2.3 — Multi-file editing support (Apr 2)

| Change | Why It Matters |
|--------|---------------|
| **Multi-file editing** (Apr 2) | Eliminates manual file-switching. *Scenario: You ask "refactor the auth module" — before, you had to point Claude at each file one by one. Now it reads and edits all related files in one pass.* |
| ⚠️ **Breaking**: Config format v2 | Old `.claude.yml` files need migration. *Scenario: If you don't update, Claude Code silently ignores your config and uses defaults.* |
```

### "Why It Matters" — The Key Differentiator

Every notable change includes two layers:
1. **What problem it solves** — the rationale and strategic context
2. **A concrete user scenario** — a brief before/after showing how your workflow changes

This is what makes the skill valuable beyond just reading changelogs yourself.

### Key Takeaways

Each report ends with 3-5 cross-cutting insights — patterns, trends, and connections across products that a busy practitioner needs to know.

## Output Files

Reports are saved to `~/ai-tracker/`:

```
~/ai-tracker/
├── 2026-04-03-this-week.md
├── 2026-03-27-this-week.md
├── 2026-03-20-last-2-weeks.md
└── ...
```

## Scope Shortcuts

| Command | What It Checks |
|---------|---------------|
| `/ai-tracker` | All defaults (6 agents + 3 models) |
| `/ai-tracker agents` | Only the 6 default agents |
| `/ai-tracker models` | Only the 3 default models |
| `/ai-tracker cursor,gpt` | Only Cursor and GPT |
| `/ai-tracker cursor,llama` | Cursor (default) + Llama (custom via Tavily) |

## Dependencies

- **tavily-search** skill — enrichment, custom product lookup, context
- `TAVILY_API_KEY` environment variable (free tier available at [tavily.com](https://tavily.com))

## Guidelines

- **Fact-based only** — every claim must come from a fetched source (changelog, The Batch, or Tavily). Training data alone is not sufficient.
- **Confirmed vs. unconfirmed** — rumors from Tavily are labeled as such (e.g., "reported by [source], not yet in official changelog")
- **If nothing's new, say so** — no backfilling or padding with old news
- **Breaking changes flagged** with ⚠️
- **Sources cited** per product section
