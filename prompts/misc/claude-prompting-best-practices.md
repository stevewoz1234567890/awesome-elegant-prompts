---
title: "Claude prompting best practices (Anthropic)"
description: "One reusable scaffold: clear instructions, motivating context, XML sections, few-shot examples, and long-context layout—aligned with Anthropic’s official guide."
models: ["Claude", "ChatGPT", "Gemini", "Grok"]
tags: ["prompting", "claude", "system-prompt", "xml", "few-shot"]
---

## When to use

- You are drafting or refactoring a **system prompt** or a **heavy user message** for Claude (or similar models) and want it to follow Anthropic’s current guidance.
- Your prompt mixes **instructions, background, variable inputs, and examples** and you need clean separation so the model does not confuse them.
- You are sending **long documents** (roughly 20k+ tokens): you want data **above** the question and a clear **document + query** structure.

Official reference: [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (Anthropic).

## Prompt

Paste below into a system prompt, or prepend to a user message and fill the tagged sections. For several documents, repeat `<document>` blocks and keep your **task and question after** the closing `</documents>` tag.

```text
<role>
You are [one-sentence role: expertise + tone + audience].
</role>

<instructions>
Follow these steps in order:
1. [Step 1 — be specific about format and constraints]
2. [Step 2]
3. [Step 3]

Golden rule: if a colleague with no prior context would be confused, add the missing detail here.
</instructions>

<context>
[Why this behavior matters — e.g. downstream system, TTS, compliance, or user experience. Claude generalizes well from a short, honest rationale.]
</context>

<documents>
  <document index="1">
    <source>[filename or label]</source>
    <document_content>
[Paste or inject longform content here.]
    </document_content>
  </document>
</documents>

<examples>
  <example>
    <input>[Representative input]</input>
    <output>[Ideal output shape, tone, and structure]</output>
  </example>
  <example>
    <input>[Edge case or variant]</input>
    <output>[Matching ideal output]</output>
  </example>
</examples>

<task>
[Your question or deliverable. For long inputs, ask for brief quoted evidence from the documents first if grounding matters, then the analysis.]
</task>
```

## Tips

- Prefer **what to do** over long lists of bans (e.g. ask for “smooth prose paragraphs” instead of only “do not use markdown”).
- Use **3–5 diverse examples** when format or edge cases matter; keep tags consistent every time.
- If the model should **act** (edit code, call tools) rather than only suggest, say so plainly: e.g. “Change this function…” instead of “Can you suggest changes?”
- Newer Claude models are **more concise** by default; if you want narrated progress after tool use, say so explicitly.
