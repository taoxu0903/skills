---
name: tavily-search
description: |
  Search the web with LLM-optimized results via the Tavily CLI. Use this skill when the user wants to search the web, find articles, look up information, get recent news, discover sources, or says "search for", "find me", "look up", "what's the latest on", "find articles about", or needs current information from the internet. Returns relevant results with content snippets, relevance scores, and metadata — optimized for LLM consumption. Supports domain filtering, time ranges, and multiple search depths.
allowed-tools: Bash(tvly *), Bash(export TAVILY_API_KEY=* && tvly *), Bash(which tvly*), Bash(echo $TAVILY_API_KEY*), Bash(curl -fsSL https://cli.tavily.com/install.sh | bash*)
---

# tavily search

Web search returning LLM-optimized results with content snippets and relevance scores.

## Before running any command — MANDATORY CHECK

**Step 1: Check if `tvly` is installed.** Run `which tvly`. If it returns "not found", you MUST install before proceeding:

```bash
curl -fsSL https://cli.tavily.com/install.sh | bash
```

**Step 2: Ensure the API key is available.** Check with `echo $TAVILY_API_KEY`.

- If it's already set (non-empty), run `tvly` commands directly: `tvly search "query" --json`
- If it's empty, export the key and run `tvly` in the same command:
  ```bash
  export TAVILY_API_KEY=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 && tvly search "query" --json
  ```

Do not skip these checks. Do not run any `tvly` command without completing both.

See [tavily-cli](../tavily-cli/SKILL.md) for alternative install methods and auth options.

## When to use

- You need to find information on any topic
- You don't have a specific URL yet
- First step in the [workflow](../tavily-cli/SKILL.md): **search** → extract → map → crawl → research

## Quick start

```bash
# Basic search
tvly search "your query" --json

# Advanced search with more results
tvly search "quantum computing" --depth advanced --max-results 10 --json

# Recent news
tvly search "AI news" --time-range week --topic news --json

# Domain-filtered
tvly search "SEC filings" --include-domains sec.gov,reuters.com --json

# Include full page content in results
tvly search "react hooks tutorial" --include-raw-content --max-results 3 --json
```

## Options

| Option | Description |
|--------|-------------|
| `--depth` | `ultra-fast`, `fast`, `basic` (default), `advanced` |
| `--max-results` | Max results, 0-20 (default: 5) |
| `--topic` | `general` (default), `news`, `finance` |
| `--time-range` | `day`, `week`, `month`, `year` |
| `--start-date` | Results after date (YYYY-MM-DD) |
| `--end-date` | Results before date (YYYY-MM-DD) |
| `--include-domains` | Comma-separated domains to include |
| `--exclude-domains` | Comma-separated domains to exclude |
| `--country` | Boost results from country |
| `--include-answer` | Include AI answer (`basic` or `advanced`) |
| `--include-raw-content` | Include full page content (`markdown` or `text`) |
| `--include-images` | Include image results |
| `--include-image-descriptions` | Include AI image descriptions |
| `--chunks-per-source` | Chunks per source (advanced/fast depth only) |
| `-o, --output` | Save output to file |
| `--json` | Structured JSON output |

## Search depth

| Depth | Speed | Relevance | Best for |
|-------|-------|-----------|----------|
| `ultra-fast` | Fastest | Lower | Real-time chat, autocomplete |
| `fast` | Fast | Good | Need chunks, latency matters |
| `basic` | Medium | High | General-purpose (default) |
| `advanced` | Slower | Highest | Precision, specific facts |

## Tips

- **Keep queries under 400 characters** — think search query, not prompt.
- **Break complex queries into sub-queries** for better results.
- **Use `--include-raw-content`** when you need full page text (saves a separate extract call).
- **Use `--include-domains`** to focus on trusted sources.
- **Use `--time-range`** for recent information.
- Read from stdin: `echo "query" | tvly search - --json`

## See also

- [tavily-extract](../tavily-extract/SKILL.md) — extract content from specific URLs
- [tavily-research](../tavily-research/SKILL.md) — comprehensive multi-source research
