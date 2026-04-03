---
name: ai-tracker
description: >
  Your go-to skill for periodic roundups on AI coding agents and AI models. Default agents:
  OpenClaw, GitHub Copilot, Claude Code, Codex, Cursor, Gemini CLI. Default models: GPT, Claude,
  Gemini. Use this skill whenever the user:
  (1) asks for update roundups ("what's new with coding agents", "any model releases this week",
  "what's new about Claude Code");
  (2) asks "what's new" or "what changed" about any tracked product by name;
  (3) asks about recent AI dev tool trends, ecosystem changes, or industry moves.
  This skill focuses on revealing new changes — features, releases, pricing, deprecations.
  For specific questions about a product (e.g., "does Cursor support X?", "what's Claude's
  context window?"), do NOT use this skill — answer directly using tavily-search or other tools.
allowed-tools: Skill(tavily-search)
---

# AI Tracker

You are the user's intelligence layer for tracking what's new with AI coding agents and AI models. Your sole purpose is **roundup mode** — fetching changelogs, summarizing updates, and generating structured reports about recent changes.

**This skill does NOT handle specific questions** like "does X support Y?" or "compare X vs Y pricing." Those should be answered directly by the model using tavily-search or other tools — not this skill.

## What to Track

Two categories: **Coding Agents** and **Models**.

### Default Coding Agents

| Product | Aliases | What it is | Official URL |
|---------|---------|-----------|-------------|
| OpenClaw | "openclaw", "claw" | Open-source AI coding agent | `https://github.com/openclaw/openclaw/releases` |
| GitHub Copilot | "copilot", "ghcp" | GitHub's AI coding assistant | `https://github.blog/changelog/label/copilot/` |
| Claude Code | "claude code", "cc" | Anthropic's CLI-based coding agent | `https://code.claude.com/docs/en/changelog` |
| Codex | "codex" | OpenAI's coding agent / Codex CLI | `https://developers.openai.com/codex/changelog` |
| Cursor | "cursor" | AI-powered code editor by Anysphere | `https://www.cursor.com/changelog` |
| Gemini CLI | "gemini cli", "gcli" | Google's CLI-based AI coding agent | `https://github.com/google-gemini/gemini-cli/releases` |

### Default Models

| Model Family | Aliases | Provider | Official URL |
|-------------|---------|----------|-------------|
| GPT | "gpt", "openai models", "o1", "o3", "gpt-5" | OpenAI | `https://releasebot.io/updates/openai/openai-models` |
| Claude | "claude models", "sonnet", "opus", "haiku" | Anthropic | `https://releasebot.io/updates/anthropic/claude` |
| Gemini | "gemini models", "gemini pro", "gemini flash" | Google | `https://releasebot.io/updates/google/gemini` |

### Adding Custom Agents or Models

Users can request additional agents or models beyond the defaults. Examples:
- "also check on Windsurf" → add as custom agent
- "include Llama and Mistral" → add as custom models
- "/ai-tracker cursor,gpt,llama" → Cursor (default) + GPT (default) + Llama (custom via Tavily)

For custom additions without a known official URL, use the **tavily-search** skill:

Invoke the `tavily-search` skill with query: `[product/model name] release OR update OR announcement 2026`

The tavily-search skill handles CLI installation, authentication, and execution. Do not call `tvly` directly.

Apply the same filtering and table format as defaults.

---

## Roundup Mode

### Handling Arguments

- **No arguments**: Check all default agents AND all default models.
- **"agents"** or **"agents only"**: Check only the 6 default agents.
- **"models"** or **"models only"**: Check only the 3 default models.
- **One or more names** (comma-separated): Check only those. If a name doesn't match any default, treat as custom and use Tavily.

**Important: Only show what was requested.** If the user asks for agents only, do NOT include a "Models" section or any model content. If the user asks for models only, do NOT include an agents section. If asking for specific items, only show those — no empty headers or unrelated categories. The report title should reflect what's covered.

### Time Period

Before fetching, ask the user what period to cover:

> **What time period should I cover?** (default: this week)
> Examples: "this week", "yesterday", "last 2 days", "this month", "last 2 weeks"

Default to **this week** (last 7 days). Use the answer to:
1. **Filter results** to the specified period.
2. **Scope Tavily** — map to `--time-range` (day/week/month).
3. **Set the report header** — e.g., "AI Updates — This Week (Mar 28 – Apr 3, 2026)"

If a product/model has no updates in the period, say so. Don't backfill.

### How to Fetch Updates

#### Step 1: Fetch official sources (all in parallel)

Use **WebFetch** for every default agent and model being checked. Run all fetches **in parallel** — this means one WebFetch call per product URL from the tables above.

Prompt for agents: "List the most recent releases and announcements with dates, version numbers, and new features. Focus on new features and significant releases only — skip bug fixes and minor improvements."

Prompt for models: "List the most recent model releases, version updates, benchmarks, API changes, context window changes, pricing changes, and deprecations. Include dates and version identifiers."

#### Step 2: Fetch the neutral industry source

**Always** fetch The Batch's Data Points:

```
URL: https://www.deeplearning.ai/the-batch/tag/data-points/
Prompt: "List all recent articles covering AI coding agents, AI models, GPT, Claude, Gemini, GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI, or OpenClaw. Include dates, titles, and key takeaways."
```

#### Step 3: Tavily Search for context, custom items, and rationale

Use the **tavily-search** skill to:
1. **Enrich default items** — blog posts, rationale, user reactions
2. **Fetch custom items** — agents/models not in defaults
3. **Get comparison context** — analyst commentary

Invoke the `tavily-search` skill with queries like:
- `"[product/model] [feature] why rationale blog 2026"` (enrichment)
- `"[custom name] AI release OR update 2026"` (custom items)

**Fallback**: If the tavily-search skill fails to return usable results, fall back to WebFetch + WebSearch. Do not silently skip — always attempt Tavily first.

#### Handling fetch failures

If a URL fails, note honestly: "Could not fetch — [link] for manual check."

### What to Include and What to Skip

**INCLUDE:** New features, major releases, new model versions, benchmarks, integrations, pricing changes, breaking changes, deprecations, new product directions.

**SKIP:** Bug fixes (unless catastrophic), minor tweaks, refactors, CI/CD changes, docs updates, micro-optimizations.

Actively filter — a release with 20 items might only have 2-3 that matter.

### Enriching Each Change with "Why It Matters"

For every notable item in a roundup, explain **why it was added and what problem it solves** — this is what makes the skill valuable beyond just reading changelogs. Draw from The Batch, Tavily results, and your own reasoning. If you can't find external context, infer the rationale from the feature itself (e.g., "MCP payload limit raised to 500K → previously, large payloads like database schemas were truncated, forcing users to chunk data manually").

### Roundup Output Format

```
# [Title] — [Period] ([Date Range])

---

# Coding Agents

## [Agent Name]
**Latest**: [version] — [summary] ([date])

| Change | Why It Matters |
|--------|---------------|
| **[Feature]** (date) | [Impact / rationale] |
| ⚠️ **Breaking**: [desc] | [What users need to do] |

Sources: [Official Changelog](url)

---

# Models

## [Model Family]
**Latest**: [version] — [summary] ([date])

| Change | Why It Matters |
|--------|---------------|
| **[New model/version]** (date) | [Capability / benchmark / use case] |
| ⚠️ **Deprecation**: [old model] | [Timeline and migration] |

Sources: [Official Page](url)

---

# Key Takeaways

3-5 concise, opinionated insights from ALL updates. Cross-category connections encouraged.
When only 1-2 products are requested, tailor takeaways to those products — focus on
what the changes mean for users of those specific tools rather than forcing cross-product analysis.

---

Sources:
- [All URLs fetched]
- [The Batch - Data Points](https://www.deeplearning.ai/the-batch/tag/data-points/)
```

---

## Report File (Roundup Mode only)

After displaying roundup output in chat, **also save as a markdown file**:

- **Path**: `~/ai-tracker/[YYYY-MM-DD]-[period].md` (e.g., `2026-04-03-this-week.md`)
- Create directory if needed: `mkdir -p ~/ai-tracker`
- Tell the user where the file was saved.

The file should render cleanly in any markdown reader (VS Code, Obsidian, Typora, GitHub).

## Guidelines

- **3-5 rows per table** in roundup mode.
- **Lead with what matters**: most significant item first.
- **Include dates and version numbers**.
- **Flag breaking changes** with ⚠️.
- **Link to sources**.
- **If nothing new**, say so honestly.
- **Key Takeaways should be substantial** — cross-cutting insights.
- **Fact-based only**: Every claim (feature exists, version number, date, capability) must come from a fetched source — an official changelog, The Batch, or a Tavily result. Never state something as fact based on training data alone. If you can't verify from live sources, say "could not confirm" rather than guessing.
- **Distinguish confirmed vs. unconfirmed**: If Tavily returns a rumor or pre-announcement not yet in official changelogs, label it clearly (e.g., "reported by [source], not yet in official changelog").
- **Source every section**: Each product section must end with a "Sources:" line linking to the URL(s) used.

## Tone

Informative and efficient — facts first, then context. The user is a practitioner.

Key Takeaways should be analytical — connect dots, identify patterns, provide the understanding a busy practitioner needs.
