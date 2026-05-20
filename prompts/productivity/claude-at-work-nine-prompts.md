---
title: "Claude at work: 9 prompts"
description: "Parallel tasks, project audit, context briefs, deep problem solving, blind spots, long sessions, cross-project integration, code review, and meeting summaries—nine copy-paste prompts."
models: ["Claude", "ChatGPT", "Gemini", "Grok"]
tags: ["productivity", "work", "claude"]
---

## Hook

If you're not using Claude at your job, you're already behind.

Copy these 9 prompts:

## Prompts

1. **Parallel Task Coordinator**

```text
I have these tasks: [list them]. Handle each one fully and independently. Flag any conflicts between them as you go. Merge all outputs into one clean deliverable at the end.
```

2. **Project Auditor**

```text
Audit my uploaded project. Give me a prioritized list of: architecture problems, technical debt, security vulnerabilities, performance bottlenecks, and outdated dependencies. For each issue, severity, exact location, exact fix.
```

3. **Project Context Brief**

```text
Project: [name]. What we're building: [description]. Decisions already made: [list]. Conventions to follow: [list]. Reference this in every response. Flag anything I ask that contradicts a decision already made. Confirm you understand before we start.
```

4. **Deep Problem Solver**

```text
Problem: [describe it]. Before answering, calibrate how deep this needs to go, list what information is missing, and challenge whether I'm solving the right problem. Then solve it. End with your top recommendation and the three biggest risks.
```

5. **Blind Spot Checker**

```text
Review everything in this conversation. Find my logical errors, weak assumptions, overconfidence, and risks I haven't considered. Be direct. Don't soften it. I need to catch mistakes before they cost me.
```

6. **Long Project Brief**

```text
Project: [name]. Locked decisions: [list]. What didn't work: [list]. Current status: [summary]. Today's goal: [task]. At the end of this session, summarize what was decided, completed, and where to pick up next time.
```

7. **Cross-Project Integration Mapper**

```text
I have Project A: [describe] and Project B: [describe]. Goal: [what they should do together]. Map the integration: where they connect, what APIs to build, shared data structures needed, what breaks, and the safest order to execute it.
```

8. **The Code Reviewer**

```text
Review this code: [paste it]. Find: bugs, security holes, performance issues, bad naming, and anything that breaks under edge cases. For each issue, what's wrong, why it matters, exact fix. Don't praise what works. Only flag what doesn't.
```

9. **The Meeting Summarizer**

```text
Here's my meeting transcript: [paste it]. Extract: decisions made, action items with owners, unresolved issues, and anything that needs a follow-up. Format it so I can paste it straight into Slack or email.
```
