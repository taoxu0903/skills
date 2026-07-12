---
name: tavily-crawl-map
description: "Discover URLs (map) or crawl full content across an entire website via the Tavily CLI, with natural-language guidance and path/domain filtering. Use to explore a site's structure or harvest many pages."
version: 1.0.0
author: Tavily (ported to Hermes by Ken Tao)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web-crawl, sitemap, tavily, content, research]
    category: research
    related_skills: [tavily-search, tavily-extract, tavily-research]
triggers:
  - user wants every URL on a site or section ("map this site")
  - user wants to crawl/harvest content from many pages of one site
  - user says "crawl", "map the site", "find all pages under"
prerequisites:
  commands: [tvly]
---

# Tavily Crawl & Map

Two related site-wide tools:
- **map** — discover all URLs on a website (no content, fast, cheap).
- **crawl** — discover AND extract full content for each page.

Third step in the workflow: **search → extract → map/crawl → research**.

## Setup (Hermes / WSL)

Load the key before each call (full env details, `tvly` install, and the
`urllib` fallback live in the **`tavily-search`** skill — the canonical setup for
the whole Tavily family):

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)
```

Write output to a file with `-o`, then read it.

## Map — discover URLs

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)

# All URLs from a starting page
tvly map "https://docs.example.com" --json -o /tmp/tvly_map.json

# Guided discovery, deeper
tvly map "https://example.com" --instructions "find all API reference pages" --max-depth 3 --limit 100 --json -o /tmp/tvly_map.json
```

## Crawl — discover + extract content

```bash
export $(grep '^TAVILY_API_KEY=' ~/.hermes/.env | xargs)

# Crawl and save each page as a .md file
tvly crawl "https://docs.example.com" --max-depth 2 --output-dir /tmp/tvly_crawl/

# Guided crawl, JSON to one file
tvly crawl "https://example.com" --instructions "collect pricing and product pages" --limit 30 --json -o /tmp/tvly_crawl.json
```

## Key options (shared by map & crawl)

| Option | Description |
|--------|-------------|
| `--max-depth` | Levels deep, 1-5 (default: 1) |
| `--max-breadth` | Links per page (default: 20) |
| `--limit` | Total pages/URLs cap (default: 50) |
| `--instructions` | Natural-language guidance for discovery |
| `--select-paths` / `--exclude-paths` | Comma-separated regex on URL paths |
| `--select-domains` / `--exclude-domains` | Comma-separated regex on domains |
| `--allow-external` / `--no-external` | Include/exclude external links |
| `--timeout` | Max wait seconds (10-150) |
| `-o, --output` | Save JSON to file |
| `--json` | Structured JSON output |

Crawl-only: `--extract-depth`, `--format`, `--chunks-per-source` (needs `--instructions`), `--output-dir` (one .md per page).

## Tips

- **Start with `map`** to scope a site cheaply, then `extract` the URLs you actually want — often cheaper than a full `crawl`.
- Use `--select-paths` (e.g. `"/docs/.*"`) to stay within a section.
- `--instructions` makes discovery semantic — describe what you're after in plain language.

## See also

- `tavily-search` — query the open web
- `tavily-extract` — pull content from a known URL list
- `tavily-research` — autonomous multi-source deep research
