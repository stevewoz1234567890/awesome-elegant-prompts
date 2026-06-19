---
title: "AI coding: 7 token habits that cut costs"
description: "Clear context, compact early, match the model, subagents for heavy reads, deterministic scripts, lean project rules, and check usage before each task—Claude Code and Cursor workflows."
models: ["Claude", "Cursor", "ChatGPT"]
tags: ["development", "coding", "tokens", "cost", "productivity"]
---

## Hook

Token costs are the number one complaint in AI coding right now. Most of the damage comes from a few default habits that are easy to fix. These seven made the biggest difference—and most take less than a minute to build into your workflow.

## Quick reference

| Habit | Claude Code | Cursor |
| --- | --- | --- |
| 1. Fresh context between tasks | `/clear` | New chat or new Agent session |
| 2. Compact at ~60%, not 95% | `/compact focus on [task]` | Summarize thread, or start fresh with a handoff note |
| 3. Match model to task | Opus / Sonnet / Haiku | Opus-class / Sonnet-class / fast model in model picker |
| 4. Heavy reads in subagents | Subagent task | Agent **Task** tool or separate chat |
| 5. Deterministic scripts | Shell, scripts, CI | Same—run tools locally, LLM orchestrates |
| 6. Lean project rules | Keep `CLAUDE.md` under ~200 lines | Keep `AGENTS.md` and rules lean; scope the rest |
| 7. Check before next task | `/usage` | Context meter in chat; review open files and rules |

Run all seven together. The compounding effect is what matters—each one shaves a layer.

---

## 1. Clear context between tasks

Every new message re-sends your full conversation history as input tokens. That debugging session from an hour ago is still inflating every prompt you send. A fresh start costs nothing. Carrying stale context costs you on every turn.

**When to clear:** you finished a task, switched bugs/features, or the thread is mostly old debugging noise.

**Claude Code:** `/clear`

**Cursor:** start a **New Chat** or **New Agent** session. Paste only what the next task needs—a one-paragraph handoff beats dragging the whole thread.

### Handoff prompt (paste into a fresh session)

```text
Handoff for the next task only—do not assume earlier conversation context.

Project: [name/repo]
Current goal: [one sentence]
Decisions already made: [bullets]
Files touched: [paths]
Blockers: [none or list]
Today's task: [specific next step]

Confirm you understand, then proceed.
```

---

## 2. Compact at 60%, not 95%

Claude auto-compacts near 95% context capacity. By then, output quality has already degraded. Compact yourself around 60% while the model still performs well.

**Claude Code:** `/compact focus on [current task]`

**Cursor:** when the context meter climbs past half, either compact manually or start fresh with the handoff prompt above. Name the **current task** in the compact request so the summary stays actionable.

### Manual compact prompt

```text
Compact this conversation for continuation. Focus only on: [current task].

Output:
1. Goal and scope (2 sentences max)
2. Decisions locked (bullets)
3. Current state of code/files (bullets with paths)
4. Open questions (bullets)
5. Exact next step (one sentence)

Drop debugging noise, failed attempts, and unrelated tangents.
```

---

## 3. Match the model to the task

Most tasks do not need the most expensive model. One team documented a **72% cost reduction** over three months from model switching and prompt caching alone.

| Task type | Use | Avoid |
| --- | --- | --- |
| Architecture, subtle bugs, multi-file refactors | Opus-class / strongest reasoning | Paying Opus prices for formatting |
| Routine implementation, tests, CRUD | Sonnet-class / balanced | Defaulting to Opus for every edit |
| Lookups, renames, formatting, simple grep-style questions | Haiku / fastest model | Slow expensive models for trivial work |

**Rule:** if you would trust a mid-level dev with the task, you probably do not need the top-tier model.

### Model-check prompt (before a long session)

```text
I'm about to: [describe task].

Recommend the cheapest model tier that can do this reliably (fast / balanced / reasoning). One sentence why. Then proceed with the task.
```

---

## 4. Offload heavy reads to subagents

A 10,000-line log file that the model reads early in a session stays in context for **every message after it**. Instead, spin up a subagent. It reads in isolated context and returns only the findings. Your main window stays clean.

**Use subagents for:** huge logs, full-repo scans, dependency trees, migration diffs, security audits across many files.

**Keep in main session:** the decision, the patch, the PR description.

### Subagent brief (Claude Code subagent or Cursor Task)

```text
Read-only investigation—do not edit files.

Target: [file path, directory, or log]
Question: [what you need to know]
Return format:
- Findings (max 10 bullets, each with file:line or log timestamp)
- Root cause hypothesis (if applicable)
- Recommended next action (one sentence)

Do not paste large excerpts. Summarize.
```

---

## 5. Build deterministic tools that cost zero tokens

Not everything needs an LLM call. Data formatting, file moves, test runners, API calls with known inputs—write these as regular scripts. The LLM orchestrates. Deterministic code executes. The scripts run for free, every time, with predictable output.

**Examples in any repo:**

- Index generators (`python tools/build_index.py`)
- Linters and formatters in CI
- Token or line-count checks before bloating project rules
- Test runners, codegen, database migrations

### Orchestration prompt

```text
Before using the LLM for [task], list which steps can run as local commands or scripts with zero token cost. Run those first. Only use the model for judgment calls and code that requires reasoning.
```

---

## 6. Keep project rules lean

`CLAUDE.md` (Claude Code) and `AGENTS.md` (Cursor) load into **every session before you type a word**. A 5,000-token rules file costs 5,000 tokens every turn, every session.

**Target:** under **200 lines** in the always-on file. Move project-specific context into scoped markdown that loads only when relevant—category docs, feature folders, or `@`-referenced files.

**Audit locally (no LLM):**

```bash
python tools/token_stats.py
```

Trim anything that is nice-to-know but not needed on every turn.

---

## 7. Run usage check before starting a new task

Do not wait until the model makes mistakes it would not have made twenty minutes ago. Check where you stand, then decide whether to compact or clear before committing to the next chunk of work.

**Claude Code:** `/usage`

**Cursor:** check the context indicator before a large refactor or multi-file read. If you are past ~60%, compact or clear first.

### Pre-task checkpoint (30 seconds)

```text
Before we start [next task]:
1. Is this thread still about one task? If not, I will start fresh.
2. Are there large files or logs still in context we no longer need?
3. Is this task matched to the right model tier?

Answer in three short bullets, then wait for my go-ahead.
```

---

## Daily workflow (copy this checklist)

```text
[ ] New task → clear context or new Agent session
[ ] Context >60% → compact with task focus or hand off to fresh session
[ ] Heavy read → subagent, findings only back to main thread
[ ] Repeated step → script or CI, not another LLM call
[ ] Project rules → under 200 lines; scope the rest
[ ] Right model → fast for trivial, reasoning only when needed
[ ] /usage or context meter → check before big work
```

## Related prompts in this repo

- [Claude at work: 9 prompts](../productivity/claude-at-work-nine-prompts.md) — context briefs and long-session hygiene
- [Five things to make every prompt better](../misc/five-things-better-prompts.md) — tighter prompts mean fewer retries (and fewer tokens)
