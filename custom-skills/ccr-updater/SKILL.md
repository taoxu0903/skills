---
name: ccr-updater
description: "Keep Claude Code and Claude Code Router up-to-date, and sync the CCR routing config with the latest Claude model versions available on GitHub Copilot (GHCP). Use this skill whenever the user asks to update Claude Code, update claude-code-router, check for latest Claude model versions on GitHub Copilot, refresh CCR config, or anything about keeping their CCR setup current. Trigger phrases include: 'update ccr', 'upgrade claude code', 'update router', 'check latest claude versions', 'sync models', 'update my setup', 'what's the latest claude on copilot', 'refresh config', 'update everything', 'ccr update', or any variation about keeping Claude Code Router or Claude Code up to date."
---

# CCR Updater

This skill performs three update tasks to keep the user's Claude Code Router setup current. Run all three steps in sequence, reporting results after each.

## Prerequisites

- **npm** must be available on PATH

## Step 1: Upgrade Claude Code to latest

Run:
```bash
npm install -g @anthropic-ai/claude-code
```

Report the installed version after completion. If already at the latest, say so.

## Step 2: Upgrade Claude Code Router to latest

Run:
```bash
npm install -g @musistudio/claude-code-router
```

Report the installed version after completion. If already at the latest, say so.

## Step 3: Check GHCP's latest Claude versions and update CCR config

This is the most important step. The goal is to find the latest Claude Sonnet and Claude Opus model versions available on GitHub Copilot, then update the routing config so CCR uses them.

### 3a: Research latest GHCP Claude models

Search the web for the latest Claude Sonnet and Opus model versions available on GitHub Copilot. Useful queries:

- `GitHub Copilot Claude model versions sonnet opus available site:github.blog`
- `GitHub Copilot Claude sonnet opus model version latest <year>`

Read the search results and identify:
- The latest Claude Sonnet version available on GHCP (e.g., `claude-sonnet-4.6`, `claude-sonnet-4.7`)
- The latest Claude Opus version available on GHCP (e.g., `claude-opus-4.6`, `claude-opus-4.7`)

The model ID format used in the CCR config for GHCP models is like: `claude-sonnet-4.6`, `claude-opus-4.7` (no "anthropic/" prefix, just the bare model name as GHCP exposes them).

### 3b: Update the CCR config file

The config file is at: `~/.claude-code-router/config.json`

Read the current config, then update these sections:

1. **Providers[].models array**: Add any new Claude model versions that aren't already listed. Keep existing models - don't remove them, just add new ones.

2. **Router section**: Update the model references to use the latest versions:
   - `default` and `background` and `webSearch`: should point to the latest Sonnet (e.g., `copilot,claude-sonnet-X.Y`)
   - `think`, `longContext`, and `image`: should point to the latest Opus (e.g., `copilot,claude-opus-X.Y`)

**Before making changes**, show the user:
- Current Sonnet version in config vs latest available
- Current Opus version in config vs latest available
- Proposed changes

**Only update if there are actually newer versions available.** If already up to date, say so.

### Example config Router section after update
```json
{
  "Router": {
    "default": "copilot,claude-sonnet-4.7",
    "background": "copilot,claude-sonnet-4.7",
    "think": "copilot,claude-opus-4.7",
    "longContext": "copilot,claude-opus-4.7",
    "longContextThreshold": 60000,
    "webSearch": "copilot,claude-sonnet-4.7",
    "image": "copilot,claude-opus-4.7"
  }
}
```

## Summary

After all three steps, present a summary table:

| Component | Previous Version | Updated Version | Status |
|-----------|-----------------|-----------------|--------|
| Claude Code | X.Y.Z | X.Y.Z | Updated / Already latest |
| Claude Code Router | X.Y.Z | X.Y.Z | Updated / Already latest |
| CCR Config - Sonnet | claude-sonnet-X.Y | claude-sonnet-X.Y | Updated / Already latest |
| CCR Config - Opus | claude-opus-X.Y | claude-opus-X.Y | Updated / Already latest |

Remind the user to restart CCR (`ccr restart`) if any config changes were made.
