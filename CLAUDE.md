# Global Instructions

## Web Search

**ALWAYS use Tavily search (`tvly` CLI) for any web search task. NEVER use the `WebSearch` tool.**

Reason: when running under Claude Code Router, the built-in `WebSearch` tool does not work, so it must be avoided unconditionally. `WebFetch` is fine for fetching a known URL, but for searching, only `tvly` is reliable.

`tvly` is already installed and authenticated on this machine. Call it directly — do not run install scripts, do not export `TAVILY_API_KEY`, do not export `PATH`. On Windows, prefer `-o <file>` to write JSON output to a file (stdout can hit Unicode encoding errors).

Example:
```bash
tvly search "your query" --depth advanced --max-results 5 -o /tmp/out.json --json
```
