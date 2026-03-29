# copilot-skills

A collection of custom GitHub Copilot agent skills for VS Code.

## What are Skills?

Skills are reusable, domain-specific instruction sets that extend GitHub Copilot's capabilities in VS Code. Each skill packages a focused workflow, quality standards, and reference material that Copilot can load on demand to perform specialized tasks with consistent, high-quality results.

## Skills

### [`write-product-spec`](./write-product-spec/SKILL.md)

Drafts, refines, and formats professional product specification documents.

**Use it when you want to:**
- Turn bullet points into a polished, manager-ready product spec or PRD
- Structure raw product notes with standard PM sections
- Ensure every requirement is written with customer value framing and precise language

**How it works:**
1. You provide raw content bullets and an optional section structure (or say `"standard"`)
2. Copilot asks clarifying questions for anything ambiguous before writing
3. A complete, formatted spec is produced — using the bundled [content standards](./write-product-spec/references/content-standards.md) and [sections guide](./write-product-spec/references/spec-sections-guide.md) as quality bars

## Repo Structure

```
skills/
└── write-product-spec/
    ├── SKILL.md                          # Skill definition and workflow
    └── references/
        ├── content-standards.md          # Mandatory quality rules for every spec
        └── spec-sections-guide.md        # Standard section layouts and guidance
```

## Usage

These skills are picked up automatically by GitHub Copilot in VS Code when this folder is part of your `.copilot/skills` directory. Copilot will invoke the appropriate skill based on your request.
