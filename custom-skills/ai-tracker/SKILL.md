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

### Pre-flight: Check `TAVILY_API_KEY`

**Before doing ANYTHING else** (including Step 0 clarification questions), check if `TAVILY_API_KEY` is set by running `echo $TAVILY_API_KEY`.

- If it's set (non-empty), proceed to Step 0.
- If it's **empty or not set**, **stop immediately**. Do NOT ask clarification questions, do NOT fetch any sources. Display the following message and wait for the user to fix it:

  > **`TAVILY_API_KEY` is not set.** This skill depends on Tavily for web search enrichment and cannot run without it.
  >
  > Get your key at https://tavily.com (free tier available), then set it:
  >
  > **macOS / Linux** — add to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):
  > ```bash
  > export TAVILY_API_KEY="your-key-here"
  > ```
  > Then restart your terminal or run `source ~/.zshrc` (or `~/.bashrc`).
  >
  > **Windows (PowerShell)**:
  > ```powershell
  > [Environment]::SetEnvironmentVariable("TAVILY_API_KEY", "your-key-here", "User")
  > ```
  > Then restart your terminal.
  >
  > **Windows (CMD)**:
  > ```cmd
  > setx TAVILY_API_KEY "your-key-here"
  > ```
  > Then restart your terminal.
  >
  > Once set, re-run `/ai-tracker`.

---

### Step 0: Clarify Before Executing

**Before doing ANY fetching or research**, confirm the execution plan with the user by asking clarification questions. Parse the user's prompt and present a summary of what you understood, then ask for confirmation or corrections. Use the AskUserQuestion tool with the following questions as applicable:

1. **Scope** — What products/models to check:
   - If the user said nothing specific: confirm "I'll check all default agents and models — is that right, or do you want to narrow it down?"
   - If the user named specific items: confirm the list — "I'll check: [list]. Anything to add or remove?"
   - If ambiguous (e.g., "check on the latest stuff"): ask what they want covered.

2. **Time period** — What window to cover:
   - Ask: "What time period should I cover?" with options like "This week (last 7 days)" (default), "Yesterday", "Last 2 weeks", "This month".

3. **Any other clarifications** — Only if genuinely ambiguous:
   - Custom products the user mentioned that you're unsure about (e.g., "By 'Windsurf', do you mean the Codeium editor?")
   - Whether they want agents only, models only, or both when the prompt is unclear.

**Rules for this step:**
- Do NOT skip this step. Always confirm the plan before executing.
- Keep it lightweight — 1-3 questions max, not an interrogation.
- If the user's request is very explicit (e.g., "/ai-tracker cursor,gpt --this-week"), you still confirm but can combine everything into a single concise confirmation question.
- Once the user confirms (or adjusts), proceed to fetching. Do not re-ask.

---

### Handling Arguments

- **No arguments**: Check all default agents AND all default models.
- **"agents"** or **"agents only"**: Check only the 6 default agents.
- **"models"** or **"models only"**: Check only the 3 default models.
- **One or more names** (comma-separated): Check only those. If a name doesn't match any default, treat as custom and use Tavily.

**Important: Only show what was requested.** If the user asks for agents only, do NOT include a "Models" section or any model content. If the user asks for models only, do NOT include an agents section. If asking for specific items, only show those — no empty headers or unrelated categories. The report title should reflect what's covered.

### Time Period

Use the time period confirmed in Step 0. Default to **this week** (last 7 days) if the user accepted the default. Use the answer to:
1. **Filter results** to the specified period.
2. **Scope Tavily** — map to `--time-range` (day/week/month).
3. **Set the report header** — e.g., "AI Updates — This Week (Mar 28 – Apr 3, 2026)"

If a product/model has no updates in the period, say so. Don't backfill.

### How to Fetch Updates (after Step 0 confirmation)

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

For every notable item in a roundup, the "Why It Matters" column must go beyond a simple restatement of the feature. It should include **two layers**:

1. **What problem it solves** — the rationale, impact, or strategic context.
2. **A concrete user scenario** — a brief, realistic before/after or "imagine this" example showing how a practitioner's workflow changes.

This is what makes the skill valuable beyond just reading changelogs. Draw from The Batch, Tavily results, and your own reasoning. If you can't find external context, infer the rationale and scenario from the feature itself.

**Example of a good "Why It Matters" entry:**

> **MCP payload limit raised to 500K** (Apr 2)
> Previously, large payloads like database schemas were truncated, forcing users to chunk data manually. *Scenario: You ask Claude Code to "analyze my Postgres schema" — before, the 300K DDL dump was silently cut off and the agent gave incomplete advice. Now the full schema passes through in one shot.*

**Example of a bad "Why It Matters" entry (don't do this):**

> **MCP payload limit raised to 500K** (Apr 2)
> The payload limit was increased from 100K to 500K.

**Guidelines for scenarios:**
- Keep them to 1-2 sentences — vivid but concise.
- Use second person ("you") to make it relatable.
- Show the before/after contrast or the concrete situation the feature handles.
- For security features: describe the attack or risk scenario it prevents.
- For breaking changes: describe what breaks and what the user must do.
- Not every row needs an elaborate scenario — minor items can have a shorter "Why It Matters." Reserve the richest scenarios for the 2-3 most significant changes per product.

### Roundup Output Format

```
# [Title] — [Period] ([Date Range])

---

# Coding Agents

## [Agent Name]
**Latest**: [version] — [summary] ([date])

| Change | Why It Matters |
|--------|---------------|
| **[Feature]** (date) | [Impact / rationale]. *Scenario: [1-2 sentence concrete user example]* |
| ⚠️ **Breaking**: [desc] | [What breaks]. *Scenario: [what user must do and what happens if they don't]* |

Sources: [Official Changelog](url)

---

# Models

## [Model Family]
**Latest**: [version] — [summary] ([date])

| Change | Why It Matters |
|--------|---------------|
| **[New model/version]** (date) | [Capability / benchmark / use case]. *Scenario: [1-2 sentence concrete user example]* |
| ⚠️ **Deprecation**: [old model] | [Timeline and migration]. *Scenario: [what breaks for users still on the old model]* |

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
