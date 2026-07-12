---
name: tavily-research
description: "Run Tavily's autonomous deep-research agent from the CLI — it searches many sources, synthesizes an answer, and returns citations. Use for comprehensive multi-source questions, not single lookups."
version: 1.0.0
author: Tavily (ported to Hermes by Ken Tao)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [deep-research, tavily, synthesis, citations, research]
    category: research
    related_skills: [tavily-search, tavily-extract, tavily-crawl-map]
triggers:
  - user wants a comprehensive, multi-source answer with citations
  - user says "do deep research on", "research X thoroughly", "give me a sourced report"
  - a single search is not enough — the question needs synthesis across sources
prerequisites:
  commands: [tvly]
---

# Tavily Research

Tavily's autonomous research agent: it plans, searches across many sources,
synthesizes, and returns a cited answer. Final step in the workflow:
**search → extract → map/crawl → research**.

> Scope note: this is Tavily's hosted research agent. For Ken's own structured
> PM research process (composable lenses + human checkpoints + evidence grading),
> use the separate `deep-research` skill — they are complementary. Use this one
> when you want a fast hosted synthesis; use `deep-research` when you want to
> drive the methodology yourself.

## Setup (Hermes / WSL)

Load the key before each call (full env details, `tvly` install, and the
`urllib` fallback live in the **`tavily-search`** skill — the canonical setup for
the whole Tavily family):

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)
```

Research tasks are long-running. Write to a file with `-o` and read it.

## Quick start

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)

# Run and wait for the full sourced answer (simplest form)
tvly research "中国市场上以 agent team 形态交付的垂直行业产品有哪些" -o /tmp/tvly_research.json --json

# Choose model + citation style
tvly research run "state of solid-state batteries 2026" --model pro --citation-format numbered -o /tmp/tvly_research.json --json
```

## Long tasks: fire-and-poll

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)

# Start without waiting — returns a request_id
tvly research run "your topic" --no-wait --json -o /tmp/tvly_req.json

# Check status / poll to completion (use the id from the previous step)
tvly research status <request_id> --json
tvly research poll <request_id> --json -o /tmp/tvly_research.json
```

## Options (research run)

| Option | Description |
|--------|-------------|
| `--model` | `mini`, `pro`, or `auto` (default) |
| `--no-wait` | Return request_id immediately, poll later |
| `--stream` | Stream results in real-time |
| `--output-schema` | Path to a JSON schema file for structured output |
| `--citation-format` | `numbered`, `mla`, `apa`, `chicago` |
| `--poll-interval` | Seconds between status checks (default: 10) |
| `--timeout` | Max seconds to wait (default: 600) |
| `-o, --output` | Save output to file |
| `--json` | Structured JSON output |

## Tips

- Use `--model pro` for hard/ambiguous topics; `auto` is fine for most.
- For very long research, prefer `--no-wait` + `poll` so you don't block a turn.
- Provide `--output-schema` when you need the result in a fixed JSON shape.
- Chinese topics work directly — no special handling needed.

## See also

- `tavily-search` — single web search
- `tavily-extract` — content from known URLs
- `tavily-crawl-map` — site-wide discovery/harvest
- `deep-research` — Ken's own checkpoint-driven PM research methodology
