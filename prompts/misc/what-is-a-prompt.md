---
title: "What is a prompt?"
description: "A short primer: how LLMs relate to prompts, why shape and training data matter, and how that compares to search."
models: ["ChatGPT", "Claude", "Gemini", "Grok"]
tags: ["prompting", "basics", "llm", "primer"]
---

## What is a prompt?

Large Language Models (LLMs) are mathematical representations of language. A huge amount of naturally occurring text (aka, the internet) is fed into the model, and the model learns the patterns that exist in language. Then, when the model is fed new text, it uses those patterns to guess what language is most likely to come next.

That **new text** is a **prompt**. Prompts are language that you input into an LLM (such as ChatGPT). The model processes that language and returns the language that it predicts is most likely to come next, based on the text that it was trained on. The language that the model returns depends on the language of your prompt, as well as the languages and domains the model was originally trained on.

## What does a prompt look like?

Short answer: well, anything! An LLM can process any text that you input. But whether its output is useful in any way depends on (1) how you craft your prompt and (2) what text the model was trained on.

LLMs are huge pattern-matching machines.

If your prompt resembles language that the model has encountered many times in its training set, it is more likely to output useful, contextually appropriate text.

If your prompt is something new for the model—a niche topic that barely appears in the training set, a highly original combination of words, total gibberish—the model has less context to draw from.

## Okay, but what do prompts look like in practice?

All this might sound very abstract. In reality, people use chatbots because they are useful. Chatbot users have a need, and that need can be expressed in language and fulfilled by more language.

Think of your favorite search engine. When you enter a search, you are usually looking for some sort of information. You enter a formatted description of what you are looking for, and the search engine returns what its algorithm says are the websites most likely to meet your information needs.

With LLMs, you express what you need in your prompt, and the LLM returns the text its math says is most likely to meet that need.

Because many general-purpose LLMs have been trained on very broad slices of the web, they often have the language to address a wide variety of needs—when your prompt gives them enough signal to do so.
