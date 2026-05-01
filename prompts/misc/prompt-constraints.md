---
title: "Constraints in prompts"
description: "What constraints are, common kinds, a worked brainstorming example (length, formatting, style), and why realistic limits beat contrived ones."
models: ["ChatGPT", "Claude", "Gemini", "Grok"]
tags: ["prompting", "constraints", "format", "context"]
---

## Constraints

One way to help LLMs perform complex tasks is to give them **specific constraints**.

**Constraints** are conditions that your prompt puts on the model’s response. They can include requests for a specific format, tone, length, audience, or the exclusion of a specific topic.

Constraints **increase** the complexity of a prompt while giving the model extra context and detail for how it should respond.

**Be cautious with your constraints.** Contrived, unrealistic constraints will push the model toward information that probably is not in its training set. Keep your constraints realistic, specific, and directly connected to your needs.

## Kinds of constraints

### Content

Tell the model to include or exclude certain information.

### Style and tone

Request a specific style (long sentences, plain vocabulary) or tone (humorous, professional).

### Length

Ask for a minimum or maximum length for the response.

### Formatting

Use specific formatting (bullets, tables) or structure (start with a summary, use essay form).

### Expertise

Request that the model respond at a specific level of expertise (beginner, PhD-level expert, etc.).

### Uncertainty

Ask the model to say how certain it is of its answer, or to avoid guessing when unsure.

### Geography

Mention where you are located when asking for recommendations (restaurants, directions).

### Time range

Instruct the model to provide responses relevant to a particular time frame or historical context.

## Constraint examples

### Brainstorming-style prompt

Here is a single prompt that layers several constraints so the output is easier to use.

**Length constraint** — asks for a specific number of examples (“three”).

**Formatting constraint** — asks for bold category labels with bullet points under each.

**Example prompt:**

```text
Generate three realistic, relatable, natural-sounding LLM prompts for me that fall under each of the following categories. Put them in a format that makes them easy to use (e.g., category in bold with the prompts in bullet points under them). Make sure the prompts sound like things that a real user would input. Vary the length, complexity, user profile, and topics of the prompts. They should involve different use cases but also be understandable by a general audience.
```

(Add the actual category names in the prompt—e.g. “categories: productivity, learning, career”—so the model knows what to fill in.)

**Style constraint** — asks for language that sounds like real user input (natural, relatable), with varied length, complexity, profiles, and topics, and stays understandable to a general audience.

Adding constraints is a natural way to guide the LLM to perform complex tasks for you.

If you were asking a friend to help you out, what information, context, and details would you need to give them so that they could do their best? Ask the model for the same.
