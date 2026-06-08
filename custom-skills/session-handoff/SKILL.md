---
name: session-handoff
description: "Use when a long Hermes session is degrading from repeated context compaction and you want to migrate the unfinished work to a fresh session. Two directions: write a handoff brief in the dying session, then resume from it in a new one."
version: 1.0.0
author: taoxu
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [session, handoff, context, compaction, migration, continuity]
    related_skills: [writing-plans]
---

# Session Handoff — Migrate an Unfinished Session

## Overview

Long Hermes sessions get auto-compacted when context fills up. Each compaction is
**lossy**, and stacking several of them is what actually degrades response quality —
the model is now reasoning from a summary of a summary. The fix is a single,
deliberate, high-fidelity baton-pass written **while context is still good**, instead
of riding N rounds of silent lossy compression.

This skill has two directions that run in **two different sessions**:

- **HAND OFF** — runs in the *dying* session. Distills live state into a brief file.
- **RESUME** — runs in a *fresh* session. Reads the brief, restates it, continues.

They cannot run in one invocation: the resume half needs a session that *lacks* the
old degraded context — shedding it is the entire point.

## When to Use

- User says: "migrate this session", "hand this off", "context is degrading",
  "start fresh but keep going", "session handoff", "continue into a new session",
  "migrate the session".
- You've seen **one or two** compaction warnings and quality still feels intact — do
  it EARLY. Waiting until the 4th-5th warning means the brief is itself built from
  already-degraded memory, defeating the purpose.
- A fresh session opens with: "resume from handoff", "continue previous session",
  "resume from the handoff brief".

**Don't use for:** short sessions, or a clean topic switch where losing context is
fine (just `/new`). This is for preserving *unfinished work*, not tidiness.

## Core Principles

1. **Do it early.** Fidelity only falls. The best brief is written before the first
   compaction, the acceptable one before the second, and a salvage operation after that.
2. **Store only what dies with the session.** The brief's whole job is to preserve
   context that exists *nowhere else*. So before writing anything, sort it:
   - **Anchored** state already has a home outside the chat — files on disk, commits
     (only if the work touched a repo), URLs/IDs you were given. It does NOT die with
     the session, so don't copy its *contents* into the brief. Read the source only to
     record an accurate **pointer** — path, branch, sha, URL — and let the resume
     session re-read the live thing itself ("I changed 5 files" drifts; a path +
     `git status` doesn't). Storing a copy would only create a stale second version —
     exactly what Direction B's "trust the repo over the brief" exists to avoid.
   - **Unanchored** state lives ONLY in this conversation — the goal, the constraints
     the user stated, the decisions and their reasoning, open questions, the approach,
     plus the `todo` list (session-scoped — it won't follow you to the new session).
     There is no external copy; compaction is eating its only home. This gets written
     into the brief in full, and the sole defense is doing it EARLY, while still intact.
   So "don't write from memory" applies only to the *pointers* (read those from source).
   Unanchored content can come from nowhere but your current understanding — which is the
   whole reason to do it early. A pure-conversation session (writing, research, advice)
   may have nothing anchored at all; its brief is almost entirely unanchored state, and
   that's correct, not a degraded handoff.
3. **Protect the goal first.** The original objective and the user's constraints/style
   degrade earliest and hurt most when lost. Capture them verbatim near the top.
4. **One concrete next action.** The resume session should know the single next step
   without re-deriving the plan.

## Storage Layout

Briefs live at the **same level as session transcripts**, in `~/.hermes/handoffs/`:

```
~/.hermes/handoffs/
  LATEST.md                      # always the most recent brief (overwritten)
  handoff_YYYYMMDD_HHMMSS.md     # timestamped immutable copy
```

`LATEST.md` is the stable resume target; the timestamped copy is the audit trail.
These are transient scratch files, intentionally outside any project repo.

**Limitation — `LATEST.md` is a single slot.** Two unfinished sessions handed off
back-to-back both overwrite `LATEST.md`; the second wins. The first's content survives
only in its own `handoff_<TS>.md`, so resume that one by explicit filename. Fine for the
common case (one migration at a time); a real constraint if you run parallel long
sessions — if that becomes routine, switch to per-task names like `LATEST_<slug>.md`.

---

## Direction A — HAND OFF (in the dying session)

### Steps

1. **Capture both kinds of state** (see Core Principles #2):
   - **Anchored — record a pointer, don't copy contents.** Only what applies here:
     - *If* the work touched a repo:
       ```bash
       cd <repo> && git status --short && git log --oneline -5 && git branch --show-current
       ```
     - Files created/modified (absolute *paths*, not their text); URLs / IDs / config keys.
     - A pure-conversation session may have NONE of these — skip it, don't invent it.
   - **Unanchored — write it into the brief, from your current understanding.** Goal
     verbatim, the user's stated constraints/preferences, decisions + reasoning, open
     questions, the next action, and the open `todo` items (`todo` tool, no args — they're
     session-scoped and won't survive the new session). The bulk of most briefs; no
     source but your context.

2. **Write the brief** to BOTH paths (use the template below). Fill every section;
   write "none" rather than leaving a heading empty. Compute the timestamp with `date`:
   ```bash
   TS=$(date +%Y%m%d_%H%M%S); echo "$TS"
   ```
   Write `~/.hermes/handoffs/LATEST.md` and `~/.hermes/handoffs/handoff_${TS}.md`
   with identical content (use the `write_file` tool for both).

3. **Confirm and instruct** the user with the exact resume ritual:
   > Brief written to `~/.hermes/handoffs/LATEST.md`. Start a fresh session
   > (`/new`, or a new `hermes` launch), then say:
   > **"Resume from ~/.hermes/handoffs/LATEST.md"**

4. Do NOT continue the task in the old session after handing off — that defeats it.

### Handoff Template

Copy this structure into both files, filled in:

```markdown
# Session Handoff — <task title>
Date: <ISO timestamp>  |  Source session: <id or short description>

## Goal
<The original objective, verbatim. This degrades first — protect it.>

## Constraints & Preferences
<Style rules, do/don't, language, tone, "be careful not to rewrite X", etc.>

## Decisions Made (and why)
- <decision> — <reason>

## Durable Artifacts (pointers only — never paste file contents here)
- Files:  <absolute paths created/modified — paths, not their text>
- Repo:   <path> | branch <name> | last commit <sha+msg> | dirty: <yes/no, which files>
- Refs:   <URLs, API IDs, ticket numbers, config keys>

## State
- Done:        <what's finished and verified>
- In progress: <exactly where it stopped — file, function, line, half-edit>
- Next action: <the single next concrete step>

## Open Questions
<Anything awaiting a user decision, or unknowns blocking progress. "none" if clear.>

## Resume Instructions
Read this brief. Restate the goal + next action in ~3 lines and confirm with the
user BEFORE acting. Do not redo work listed under "Done". Reload any skills named
in Constraints/Decisions.
```

---

## Direction B — RESUME (in the fresh session)

### Steps

1. Read the brief:
   ```
   read_file ~/.hermes/handoffs/LATEST.md
   ```
   (If the user named a specific timestamped file, read that instead.)

2. **Re-establish ground truth — trust the repo over the brief.** The brief is a
   snapshot; the working tree may have moved. Re-run:
   ```bash
   cd <repo from brief> && git status --short && git log --oneline -3
   ```
   If reality and the brief disagree, believe the filesystem and flag the drift.

3. **Reload any skills** named in the brief's Constraints/Decisions — they don't
   carry over automatically.

4. **Restate, then confirm.** In ~3 lines: the goal, what's done, and the single next
   action. Ask the user to confirm before acting. This catches a stale or wrong brief
   before any work is redone.

5. On confirmation, execute the Next action. Do NOT repeat anything under "Done".

### Pitfall: don't re-summarize a compacted transcript

Resume from the *brief*, not by scrolling the old session's history. The whole point
was to escape the degraded record — re-reading it reintroduces the loss. If no brief
exists, say so and offer to reconstruct from what actually persists — `git` and files
(the old session's todo list is gone; it was session-scoped) — not from memory.

---

## Optional — `hh-resume` shell shortcut (shape B, fork-free)

If hand-typing the resume prompt gets old, this zsh function launches a fresh session
pre-pointed at the latest brief. It uses the documented `hermes -z PROMPT` launch flag
(verify once on your version with `hermes --help`). Add to `~/.zshrc`:

```bash
# Launch a fresh Hermes session that resumes from the latest handoff brief.
hh-resume() {
  local brief="${1:-$HOME/.hermes/handoffs/LATEST.md}"
  [[ -f "$brief" ]] || { echo "No handoff brief at $brief"; return 1; }
  hermes -z "Resume from $brief — read it, restate goal + next action, confirm before acting."
}
```

Then in a clean terminal: `hh-resume`. This is purely ergonomic — the skill works
without it. It does NOT touch hermes-agent source, so `hermes update` won't clobber it.

## Why not a real `/handoff` slash command?

Considered and rejected by default: a slash command is a framework source change
(`CommandDef` + handlers across Python/gateway/web-ui), it survives only the *write*
half (resume still runs in the spawned session, i.e. still needs this skill), and the
patch must be re-applied after every `hermes update`. Only graduate to that if this
becomes a daily ritual worth maintaining a fork for. See the
`debugging-hermes-tui-commands` skill for the command-layer wiring if you ever do.

## Common Pitfalls

1. **Handing off too late.** After 4-5 compactions the brief is built from mush. Trigger
   on the first or second warning.
2. **Treating "from memory" as always wrong.** Only *anchored* facts (what files exist,
   what's committed) must be read from their source instead of recalled. *Unanchored*
   content — goal, decisions, constraints — has no source but your understanding; the
   defense there is doing it EARLY, not avoiding memory.
3. **Only writing LATEST.md.** Write the timestamped copy too — `LATEST.md` gets
   overwritten by the next handoff and you lose the trail.
4. **Empty template sections.** Write "none" explicitly; a blank heading reads as
   "forgot to fill" in the resume session.
5. **Continuing work in the old session after handoff.** Pointless — you keep
   accumulating context in the session you're trying to abandon.
6. **Resume session trusting the brief over the repo.** Files are ground truth; the
   brief is a snapshot. Reconcile, and flag drift.
7. **Forgetting to reload skills** in the fresh session — skill context doesn't migrate.

## Verification Checklist

- [ ] `~/.hermes/handoffs/` exists, same level as `~/.hermes/sessions/`
- [ ] Both `LATEST.md` and `handoff_<TS>.md` written with identical content
- [ ] Goal + Constraints captured verbatim; every section filled (no blanks)
- [ ] Durable Artifacts are pointers (paths/sha/URLs) to real `git`/file state — no pasted contents
- [ ] Exactly one concrete Next action recorded
- [ ] User given the exact resume phrase
- [ ] (Resume) Goal + next action restated and confirmed before any work
- [ ] (Resume) "Done" items not repeated
