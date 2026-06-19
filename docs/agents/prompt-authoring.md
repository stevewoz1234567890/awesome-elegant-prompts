# Prompt authoring (scoped — load when writing prompts)

Use this when adding or rewriting files under `prompts/`. Not needed for index or tooling-only changes.

## File layout

```text
prompts/<category>/<slug>.md
```

Use `prompts/_template.md` as the starting point.

## Front matter

```yaml
---
title: "Short, clear title"
description: "One-line summary for PROMPTS.md"
models: ["ChatGPT", "Claude", "Gemini", "Grok"]
tags: ["category", "topic"]
---
```

## Body sections (typical)

- **Hook** — why this matters (short)
- **When to use** — bullets (optional but helpful)
- **Prompt(s)** — in fenced `text` blocks with `[placeholders]`
- **Tips** — iteration, safety, model notes (optional)

Match the tone of sibling files in the same category: direct, copy-paste friendly, no walls of text.

## Quality bar

- **Reusable:** placeholders instead of one-off examples
- **Specific:** output format, tone, constraints
- **Safe:** disclaimers for health, finance, legal gray areas
- **Readable:** short sections, consistent headings

## After adding a file

```bash
python tools/build_index.py
```

Commit the new prompt **and** updated `PROMPTS.md`.

## New category

Add the folder under `prompts/`. If it is not in the default list, `build_index.py` appends unknown categories alphabetically—prefer adding `development` or an existing category when possible.
