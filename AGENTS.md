# Agent instructions (keep lean)

This file loads into every Cursor Agent session. **Stay under 200 lines.** Put detailed guidance in scoped docs and load them only when relevant.

## Repo purpose

Markdown prompt library: `prompts/<category>/<slug>.md` with YAML front matter. Index at `PROMPTS.md` (auto-generated).

## Before you edit

1. Read `prompts/_template.md` for file format.
2. For prompt authoring details: `docs/agents/prompt-authoring.md`.
3. For token/cost habits when using AI on code: `prompts/development/ai-coding-seven-token-habits.md`.

## Required workflow for new/changed prompts

```bash
python tools/build_index.py
```

CI fails if `PROMPTS.md` is stale. Run `python tools/build_index.py --check` locally.

## Conventions

- **Front matter:** `title`, `description`, `models`, `tags`.
- **Placeholders:** `[brackets]` for user fill-ins.
- **Safety:** no buy/sell finance advice; therapy disclaimers where needed; no ToS-breaking travel tactics.
- **Scope:** minimal diffs; match existing tone and section structure in sibling prompts.
- **Do not** edit `PROMPTS.md` by hand.

## Deterministic tools (use these instead of LLM reads)

| Tool | Purpose |
| --- | --- |
| `python tools/build_index.py` | Regenerate `PROMPTS.md` |
| `python tools/build_index.py --check` | Verify index is current |
| `python tools/token_stats.py` | Estimate tokens in context files |

## Categories

`business`, `career`, `writing`, `productivity`, `learning`, `health`, `travel`, `finance`, `design`, `content`, `language`, `entertainment`, `mindset`, `development`, `misc`

## Git

Commit only when the user asks. Do not push unless asked.
