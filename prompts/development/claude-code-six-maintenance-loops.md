---
title: "Claude Code: 6 maintenance loops (not one-shot prompts)"
description: "Paste-ready loop instructions for type errors, test coverage, dead code, dependency updates, pattern migration, and lint fixes—each with verify-after-every-step exit criteria for Claude Code and Cursor Agent."
models: ["Claude", "Cursor"]
tags: ["development", "coding", "claude-code", "loops", "automation", "maintenance"]
---

## Hook

The head of Claude Code at Anthropic says he does not write prompts anymore—he writes **loops**.

A one-shot prompt asks for a result once. A loop gives the agent a **goal**, **rules**, a **verify step after every change**, and a clear **exit condition**. The model keeps working until the metric hits zero (or every remaining item is logged for manual review).

These six loops are copy-paste ready for Claude Code, Cursor Agent, or any coding agent that can run commands and iterate. Customize placeholders in `[brackets]` before you start.

## Quick reference

| Loop | Goal | Primary verify command |
| --- | --- | --- |
| 1. Type Error Killer | Zero TypeScript errors | `tsc --noEmit` |
| 2. Test Gap Closer | Hit coverage target | Coverage report + full test suite |
| 3. Dead Code Sweeper | Remove unused code safely | Full test suite after each removal |
| 4. Dependency Updater | Current compatible deps | Full test suite after each package |
| 5. Pattern Migrator | Replace old pattern everywhere | Tests + recount old pattern |
| 6. Lint Fixer | Zero lint errors/warnings | Linter + tests after each rule batch |

**Loop hygiene (all six):** one unit of work at a time → verify → if metrics got worse, undo → log anything that cannot be auto-fixed.

---

## 1. The Type Error Killer

**When to use:** A TypeScript project with a non-zero error count you want cleared without changing runtime behavior.

```text
Goal: Fix every TypeScript type error in this project.

Rules:
- Run `tsc --noEmit` to get the full error list.
- Fix one file at a time, starting with the file that has the most errors.
- After each file, run `tsc --noEmit` again to confirm the count dropped.
- Do not add `@ts-ignore` or type assertions unless the type is genuinely unknown.
- Do not change runtime behavior. Types only.

Verify after each step:
- Run `tsc --noEmit`.
- Compare error count to the previous run.
- If the count went up, undo the last change and try a different fix.

Exit when: `tsc --noEmit` returns zero errors.
```

**Tips:** For monorepos, scope with `tsc --noEmit -p packages/[name]/tsconfig.json`. If errors cascade from one broken type definition, fix that file first even if it is not the noisiest.

---

## 2. The Test Gap Closer

**When to use:** Coverage is below target and you want steady, safe gains without breaking existing tests.

```text
Goal: Bring test coverage to [TARGET]% for [DIRECTORY].

Rules:
- Run the coverage report first.
- Identify the least-covered file.
- Write tests for that file. One file at a time.
- Test real behavior, not implementation details.
- Run the full test suite after each new test file to make sure nothing broke.
- Move to the next least-covered file and repeat.

Verify after each step:
- Run coverage report. Confirm the number went up.
- Run full test suite. Confirm zero new failures.

Exit when: Coverage report shows [TARGET]% or higher.
```

**Tips:** Replace `[TARGET]` with a realistic step (e.g. 80% → 85%). Replace `[DIRECTORY]` with `src/` or a package path. Use the project's existing test runner and coverage tool (`npm test -- --coverage`, `pytest --cov`, etc.).

---

## 3. The Dead Code Sweeper

**When to use:** Static analysis shows unused exports, functions, variables, or imports and you want to prune safely.

```text
Goal: Find and remove all unused exports, functions, variables, and imports in this project.

Rules:
- Use static analysis to identify unused code.
- Remove one item at a time.
- Run the full test suite after each removal.
- If a test fails, undo that removal, mark it as "in use despite no static reference," and move on.
- Do not remove anything inside files matching [EXCLUDE PATTERN] (e.g., config files, entry points).

Verify after each step:
- Run tests. If green, the removal was safe.
- If red, roll back and skip.

Exit when: No unused code remains, or all remaining items cause test failures when removed.
```

**Tips:** Common exclude patterns: `**/*.config.*`, `**/index.ts`, `**/main.*`, `**/routes/**`. Tools: `knip`, `ts-prune`, `eslint --rule unused-imports`, or your IDE's unused-symbol analysis.

---

## 4. The Dependency Updater

**When to use:** Dependencies are outdated and you want incremental updates with a clear rollback log.

```text
Goal: Update all outdated dependencies to their latest compatible versions.

Rules:
- Run the outdated check (`npm outdated`, `pip list --outdated`, or equivalent).
- Update one package at a time.
- Start with patch versions, then minor, then major.
- Run the full test suite after each update.
- If tests fail, roll back that package and log it with the failure reason.
- Do not update packages listed in [SKIP LIST].

Verify after each step:
- Run tests. If green, keep the update and move to the next package.
- If red, roll back and log.

Exit when: All packages are current, or all remaining outdated packages have been attempted and logged.
```

**Tips:** Put security-sensitive or pinned packages in `[SKIP LIST]` (e.g. `react`, `typescript`, internal packages). Keep a running log file or PR comment of failed updates and why.

---

## 5. The Pattern Migrator

**When to use:** A codebase-wide refactor (API style, component model, import path, etc.) must stay behavior-identical.

```text
Goal: Replace every instance of [OLD PATTERN] with [NEW PATTERN] across the codebase.

Rules:
- Scan the full codebase and list every instance of [OLD PATTERN] first.
- Migrate one file at a time.
- Run the test suite after each file.
- If tests fail, undo that file's migration and log it for manual review.
- Preserve all existing behavior. The output should be functionally identical.

Verify after each step:
- Run tests. Confirm the migrated file behaves the same as before.
- Recount remaining instances of [OLD PATTERN].

Exit when: Zero instances of [OLD PATTERN] remain and all tests pass. Or all remaining instances have been attempted and logged.
```

**Example placeholders:**

- `[OLD PATTERN]`: class components extending `React.Component`
- `[NEW PATTERN]`: functional components with hooks

**Tips:** The initial inventory pass prevents surprise stragglers. For large migrations, log blocked files with file path and failure reason so a human can finish them.

---

## 6. The Lint Fixer

**When to use:** Lint debt is blocking CI or slowing reviews and you want fixes without disabling rules.

```text
Goal: Fix all linting errors and warnings in this project without disabling any rules.

Rules:
- Run the linter.
- Group errors by rule.
- Fix the most common rule violation first, across all files.
- After fixing each rule category, rerun the linter.
- Do not add `eslint-disable`, `noqa`, or any rule suppression comments.
- If a fix would change logic (not just style), skip it and log the file and rule.

Verify after each step:
- Rerun linter. Confirm the total count dropped.
- Run tests to make sure fixes did not break behavior.

Exit when: Linter returns zero errors and zero warnings, or all remaining violations require logic changes and have been logged.
```

**Tips:** Auto-fix what you can first (`eslint --fix`, `ruff check --fix`). Batch by rule ID so progress is measurable. Separate "style-only" fixes from logic-touching fixes in your log.

---

## How to run a loop in Claude Code or Cursor

1. **Start fresh** — new session or `/clear` so the loop is the only task ([token habits](./ai-coding-seven-token-habits.md)).
2. **Paste one loop** — fill in `[brackets]` first.
3. **Let it iterate** — the agent should not stop after one file unless you interrupt.
4. **Checkpoint** — if context passes ~60%, compact with "current loop state + error/coverage/lint count" or hand off to a new session.
5. **Review the log** — anything marked for manual review needs a human before merge.

### Session handoff (mid-loop)

```text
Loop handoff—continue the same loop, do not restart from scratch.

Active loop: [name, e.g. Type Error Killer]
Last metric: [e.g. 12 tsc errors, was 47]
Last file touched: [path]
Blocked/logged items: [bullets or none]
Next action: [one sentence]

Confirm, then continue the loop rules and verify steps.
```

---

## Related prompts in this repo

- [AI coding: 7 token habits that cut costs](./ai-coding-seven-token-habits.md) — clear context, compact early, subagents for heavy scans
- [Claude at work: 9 prompts](../productivity/claude-at-work-nine-prompts.md) — code review and long-session hygiene
