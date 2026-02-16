## Contributing to Awesome Elegant Prompts

Thanks for helping make this prompt library genuinely useful.

### What we accept

- **Original prompts** you wrote yourself
- **Improved rewrites** of existing prompts in this repo (clearer, safer, more reusable)
- **New categories** when a group of prompts clearly doesn’t fit existing ones

### What we don’t accept

- **Copyrighted text** copied from paid courses, books, or private communities
- **Harmful or illegal guidance**, including instructions to break laws or platform rules
- **Medical / mental health claims** presented as professional advice (see “Safety”)

### Prompt quality checklist (PRs should meet this)

- **Reusable**: uses placeholders like `[topic]`, `[audience]`, `[constraints]`
- **Specific**: includes output format, tone, and constraints
- **Safe**: avoids instructions for wrongdoing; includes disclaimers where needed
- **Readable**: short sections, consistent formatting, no walls of text

### File format

Add prompts under `prompts/<category>/<slug>.md` using the template:

- `prompts/_template.md`

### Update the index

This repo keeps a browsable index in `PROMPTS.md`.

Run:

```bash
python tools/build_index.py
```

Your PR should include the updated `PROMPTS.md`.

### Safety notes (important)

- **Mental health**: If a prompt touches therapy-like content, include a short note that it’s not a substitute for professional care, and add a crisis disclaimer.
- **Finance**: Avoid “buy/sell” recommendations. Prefer analysis frameworks and risk management prompts.
- **Travel / pricing**: Avoid instructions that break terms of service. If a tactic is risky or commonly disallowed, call that out.

