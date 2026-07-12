---
name: tavily-extract
description: "Extract clean, LLM-ready content (markdown or text) from one or more specific URLs via the Tavily CLI. Use when you already have URLs and need their full page content without scraping noise."
version: 1.0.0
author: Tavily (ported to Hermes by Ken Tao)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web-extract, scraping, tavily, content, research]
    category: research
    related_skills: [tavily-search, tavily-crawl-map, tavily-research]
triggers:
  - user has one or more URLs and wants the full page content
  - user says "extract", "get the content of", "read this page"
  - you ran tavily-search and now need full text of a specific result
prerequisites:
  commands: [tvly]
---

# Tavily Extract

Pull clean, LLM-ready content from specific URLs (up to 20 at once). Second step
in the workflow: **search → extract → map/crawl → research**.

## Setup (Hermes / WSL)

Load the key before each call (full env details, `tvly` install, and the
`urllib` fallback live in the **`tavily-search`** skill — the canonical setup for
the whole Tavily family):

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)
```

Always write output to a file with `-o` (Unicode on stdout can crash on WSL),
then read the file.

## Quick start

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)

# Single URL
tvly extract "https://example.com/article" --json -o /tmp/tvly_extract.json

# Multiple URLs (max 20)
tvly extract "https://a.com" "https://b.com" --format markdown -o /tmp/tvly_extract.json

# Rerank page chunks by relevance to a query
tvly extract "https://example.com" --query "pricing tiers" --chunks-per-source 3 --json -o /tmp/tvly_extract.json
```

## Options

| Option | Description |
|--------|-------------|
| `--query` | Rerank chunks by relevance to this query |
| `--chunks-per-source` | Chunks per source (1-5, requires `--query`) |
| `--extract-depth` | `basic` (default) or `advanced` |
| `--format` | `markdown` (default) or `text` |
| `--include-images` | Include image URLs |
| `--timeout` | Max wait seconds (1-60) |
| `-o, --output` | Save output to file (use this on Hermes/WSL) |
| `--json` | Structured JSON output |

## Tips

- `extract` works without auth at a rate-limit cap, but exporting the key removes the cap.
- Use `--extract-depth advanced` for JS-heavy or complex pages.
- Pair with `tavily-search --include-raw-content` to skip extract when you only need a few results.

## Pitfalls

- **The depth flag is `--extract-depth`, NOT `--depth`.** `tvly extract ... --depth advanced`
  fails with `Error: No such option '--depth'. Did you mean '--extract-depth'?`. (Search uses
  `--depth`; extract uses `--extract-depth` — they differ.) Multi-URL extract still runs even
  when the bad flag is silently retried, so check the output file actually exists before parsing.
- **JS-rendered SPA directories fail to fetch.** Pages like `make.com/en/integrations` return
  `failed_results: [{... "error": "Failed to fetch url"}]` even at `--extract-depth advanced`,
  because the listing is client-side rendered. Don't retry endlessly — fall back to a static
  page (the vendor's pricing/help page often carries the headline count), grab that number, and
  report the dynamic list as unobtainable rather than fabricating it. Always inspect
  `failed_results` and confirm `len(results) > 0` before assuming an extract succeeded.

## See also

- `tavily-search` — find URLs first
- `tavily-crawl-map` — discover URLs across a whole site
- `tavily-research` — autonomous multi-source deep research
