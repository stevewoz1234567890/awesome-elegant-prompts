---
title: "Seven follow-ups instead of “you're wrong”"
description: "When a model caves, hallucinates, drifts, or stays shallow—seven copy-paste follow-ups that give it a job instead of a verdict, based on Anthropic sycophancy research."
models: ["ChatGPT", "Claude", "Gemini", "Grok"]
tags: ["prompting", "meta", "correction", "sycophancy", "iteration"]
---

## Hook

Stop telling AI it's wrong. That's the fastest way to turn a correct answer into a worse one.

Anthropic's research on [sycophancy in language models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) found that models often flip accurate answers and apologize for mistakes they never made when users push back. A simple "Are you sure?" can trigger the same collapse across models.

The people who get clean answers out of AI **direct** the model. They don't argue with it.

## When to use

- The model **caved immediately** when you expressed doubt, even though the first answer might have been right.
- It stated **made-up facts with full confidence** and you need to know what to trust.
- It answered a **different question** than the one you asked.
- It **ignored a rule or constraint** you gave earlier in the thread.
- A long answer is **mostly right** but you suspect a small reasoning error.
- The answer is **correct but shallow** and you need expert depth.
- It keeps **building on a wrong approach** instead of starting over.

## The principle

| Verdict (backfires) | Job (works) |
| --- | --- |
| "You're wrong." | "Find the error in step 3." |
| "That's not what I asked." | "Repeat my task in one sentence before redoing anything." |
| "Are you sure?" | "Re-examine your answer on its own merits. Defend it or show the exact mistake." |

Every follow-up below gives the model a **specific task**. None of them signal that you have already decided it failed.

## Follow-ups

### 1. When it caves the moment you doubt it

Pushing back reads as a signal to agree with you. Drop the signal.

```text
I'm not saying you're wrong. Re-examine your answer on its own merits. If it holds up, defend it and tell me why. If it doesn't, show me the exact mistake.
```

### 2. When it states made-up facts with full confidence

Make it rate its own certainty before you trust a word.

```text
Go through your answer claim by claim. Label each one confident, inferred, or unsure. For anything not confident, tell me what would verify it.
```

### 3. When it answers a different question than you asked

Get it to repeat the task back before it burns another response.

```text
Before you redo anything, tell me in one sentence what you think I'm asking for. If any part is unclear, ask me instead of guessing.
```

### 4. When it ignores a rule you gave it

Force a line-by-line check against your own instructions.

```text
List every requirement I gave you. Go through your answer and mark each one met or missed, with the line that proves it.
```

### 5. When a long answer contains a small error

Tell it an error exists so it hunts instead of skims.

```text
There is at least one error in the reasoning above. Find it and fix it. Walk through each step until you catch where it breaks.
```

### 6. When the answer is correct but shallow

Raise the bar and make it show you the gap.

```text
That's a beginner-level answer. Redo it as a top expert in [field] would, and list what they'd include that you left out.
```

### 7. When it keeps building on a wrong approach

Cut the anchor and name the flaw so it doesn't repeat.

```text
Drop your previous approach completely. It failed because [reason]. Start fresh and don't reuse that approach or its conclusions.
```

## Tips

- **Pick the failure mode first.** Match the follow-up to what actually went wrong—caving, hallucination, drift, rule-breaking, hidden error, shallowness, or a stuck approach—not to how frustrated you feel.
- **Stay in the same thread.** These prompts work best as the next message after a bad answer, while the model still has full context.
- **Combine with good first prompts.** Clear constraints up front reduce how often you need corrections. See [Five things to make every prompt better](five-things-better-prompts.md) for the upstream habits.
- **If it still caves**, add: "Do not change your answer just to agree with me. Only change it if you find a specific error." That turns pushback into an explicit instruction instead of an implicit verdict.
