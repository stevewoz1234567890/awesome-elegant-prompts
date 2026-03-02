---
title: "Investment banking financial models (Claude)"
description: "5 Claude prompts for DCF, three-statement model, M&A accretion/dilution, LBO, and trading comps."
models: ["Claude"]
tags: ["finance", "valuation", "modeling", "investment-banking"]
---

## Safety note

Not financial advice. Use these for education, scenario analysis, and draft modeling structure; validate assumptions with primary sources and a qualified professional.

## Prompts

AI can now build financial models like Goldman Sachs analysts (for free).

Here are 5 Claude prompts that replace $150K/year investment banking work:

1. **DCF Valuation Model**

```text
You are a Senior Analyst at Goldman Sachs. I need a complete DCF (Discounted Cash Flow) valuation model for [COMPANY NAME].

Please provide:

- Free cash flow projections: Next 5 years with growth assumptions
- WACC calculation: Cost of equity + cost of debt breakdown
- Terminal value: Both perpetuity growth and exit multiple methods
- Sensitivity analysis: How value changes with different assumptions
- Discount rate justification: Why we chose this WACC
- Key drivers: What makes cash flow go up or down
- Comparable companies: How our assumptions compare to peers
- Valuation range: Bull case, base case, bear case scenarios

Format as investment banking pitch book valuation page with clear formulas.

Company: [DESCRIBE COMPANY, INDUSTRY, FINANCIALS]
```

2. **Three-Statement Financial Model**

```text
You are a VP at Morgan Stanley. I need a complete three-statement model for [COMPANY NAME].

Please provide:

- Income statement: Revenue, costs, EBITDA, net income (5 years)
- Balance sheet: Assets, liabilities, equity (5 years)
- Cash flow statement: Operating, investing, financing activities (5 years)
- Link formulas: How statements connect (net income → cash flow → balance sheet)
- Working capital: How AR, inventory, and AP change
- Debt schedule: Principal payments and interest expense
- Key assumptions: Revenue growth, margins, capex as % of sales
- Error checks: Balance sheet balancing and circular references

Format as Excel-style model with formulas explained in plain English.

Company: [DESCRIBE BUSINESS, CURRENT FINANCIALS, GROWTH STAGE]
```

3. **M&A Accretion/Dilution Analysis**

```text
You are a Managing Director at JP Morgan. I need an accretion/dilution analysis for [ACQUIRER] buying [TARGET].

Please provide:

- Deal structure: Cash vs. stock mix and total consideration
- Pro forma income statement: Combined company earnings
- EPS impact: Accretion or dilution percentage
- Synergies: Cost savings and revenue opportunities with dollar amounts
- Funding sources: Debt, cash on hand, or equity issuance
- Credit impact: How debt/EBITDA ratio changes
- Break-even analysis: What synergies needed to be accretive
- Sensitivity table: EPS impact at different purchase prices

Format as M&A analysis memo with deal recommendations.

Deal: [DESCRIBE ACQUIRER, TARGET, DEAL SIZE, RATIONALE]
```

4. **LBO (Leveraged Buyout) Model**

```text
You are a Private Equity Associate at KKR. I need a complete LBO model for [COMPANY NAME].

Please provide:

- Sources and uses: How deal is funded (debt, equity, fees)
- Debt structure: Senior debt, mezzanine, interest rates, covenants
- Cash flow sweep: How excess cash pays down debt
- Exit scenarios: Strategic sale vs. IPO in year 5
- IRR calculation: Internal rate of return for equity investors
- Cash-on-cash multiple: Total proceeds divided by equity invested
- Debt paydown schedule: Year-by-year principal reduction
- Management assumptions: EBITDA growth and margin improvement

Format as private equity investment committee memo with returns analysis.

Company: [DESCRIBE COMPANY, EBITDA, ASKING PRICE, INDUSTRY]
```

5. **Comparable Company Analysis (Comps)**

```text
You are an Equity Research Analyst at Citi. I need a trading comps analysis for [COMPANY NAME].

Please provide:

- Peer group: 10-15 public companies in same industry
- Trading multiples: EV/EBITDA, EV/Revenue, P/E for each peer
- Financial metrics: Revenue, EBITDA, margins for comparison
- Valuation range: 25th percentile, median, 75th percentile multiples
- Implied valuation: What our company is worth at each multiple
- Adjustments: Why our company deserves premium or discount
- Growth comparison: How our growth compares to peers
- Quality screen: Which peers are most comparable and why

Format as comparable company valuation table with multiples highlighted.

Company: [DESCRIBE COMPANY, FINANCIALS, CLOSEST COMPETITORS]
```

