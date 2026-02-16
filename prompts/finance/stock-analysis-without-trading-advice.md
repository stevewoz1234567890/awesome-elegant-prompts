---
title: "Stock analysis (without trading advice)"
description: "Fundamental/technical frameworks, risk planning, and screening prompts — no buy/sell recommendations."
models: ["ChatGPT", "Claude", "Gemini", "Grok"]
tags: ["finance", "analysis", "risk"]
---

## Safety note

Not financial advice. Don’t ask for “buy/sell” calls; use these for structured analysis and learning.

## Prompts

1. **Personal Market Analyst (Fundamentals)**

```text
Act as a professional equity research analyst. Analyze this company using:
- business model
- competitive advantage
- management quality (based on public info)
- financial health and key ratios
- risks and bear case
- long-term drivers

Company/Ticker: [name]
Time horizon: [years]
Output as a structured report with a risk section.
```

2. **Technical Chart Breakdown (Scenarios, not predictions)**

```text
Interpret this price action using moving averages, RSI, MACD, trendlines, support/resistance, and volume.

Do not predict. Instead give 3 likely scenarios and what would invalidate each one.
Chart data: [paste]
Timeframe: [daily/weekly/etc]
```

3. **Strategy Simulator (Educational)**

```text
Act as a trading mentor for educational purposes. Compare how these strategy styles behave in different market regimes:
- swing
- intraday
- position

For each: define rules, risk controls, and typical failure modes.
Risk level: [low/medium/high]
```

4. **Personal Risk Manager (Allocation, not picks)**

```text
Analyze my risk appetite and create a diversified exposure plan.

Do NOT recommend specific stocks. Define:
- percentage allocations by asset class/style
- time horizon
- risk controls (position sizing, stop rules, rebalancing)

My profile: [age, goals, risk tolerance, income stability]
```

5. **AI Stock Screener Checklist**

```text
Create a screening checklist for identifying high-quality companies based on valuation, growth, financial health, competitive advantage, and risk factors.

Then apply the checklist to this company:
Company/Ticker: [name]
Public data I have: [paste metrics or links]
```

6. **News Impact Analyzer**

```text
Analyze how this news event may influence the company or sector.

Provide a balanced short-term and long-term view without buy/sell advice.
News: [paste]
Company/Sector: [name]
```

7. **10-Minute Daily Market Routine**

```text
Create a daily 10-minute market analysis routine that includes:
- indexes
- news scan
- watchlist review
- chart check
- risk check

Make it simple enough to follow consistently.
My focus: [long-term investing / trading / learning]
```

