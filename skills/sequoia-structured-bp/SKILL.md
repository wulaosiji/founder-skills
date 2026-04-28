---
name: sequoia-structured-bp
description: "Sequoia Capital-style structured business plan / pitch deck framework. 10-slide data-driven format with slide-by-slide writing guides, examples, and checklists. Best for Series A+ and institutional investors. Trigger when users need a rigorous, investor-grade BP structure."
license: MIT
---

# Skill: Sequoia Structured BP

## Meta

- **Style**: Data-driven, investor-grade, modular
- **Best For**: Series A and beyond; institutional investors; due-diligence-heavy rounds
- **Source**: Sequoia Capital pitch framework
- **Output Length**: 10–12 slides
- **Tone**: Confident, evidence-based, no hype

## Core Philosophy

The investor has 3 minutes. Every slide must either (a) reduce risk or (b) increase upside. No decoration.

> "If you can't explain it with data, you don't understand it well enough." — adapted from Einstein

---

## Slide-by-Slide Guide

### Slide 1: Company Purpose (1 sentence)

**Goal**: Make the investor "get it" in 5 seconds.

**Formula**:
```
[Company] is a [category] that helps [target customer] [solve problem] by [unique mechanism].
```

**Good Example**:
> "ChainLedger is a compliance settlement network that helps cross-border B2B traders reduce settlement time from 7 days to 4 hours through real-time sanction screening."

**Bad Example**:
> "ChainLedger is a blockchain-based fintech platform leveraging AI and machine learning to disrupt the payments industry."

**Check**:
- [ ] Can a non-expert understand it?
- [ ] No buzzwords (AI, blockchain, disruptive, synergy)
- [ ] Contains: who, what problem, how

---

### Slide 2: Problem

**Goal**: Prove the problem is real, urgent, and valuable.

**Structure**:
1. **Scene-setting** (1 sentence): What world do your customers live in?
2. **Pain quantification**: Use a number. $18B/yr in fines. 3–5 intermediaries. 4–7 day delay.
3. **Who feels it most**: Define your ICP (Ideal Customer Profile) narrowly.

**Good Example**:
> "Cross-border B2B payments involve 3–5 intermediaries, 4–7 day settlement, and compliance gaps that cost enterprises $18B/yr in fines globally. The pain is most acute for mid-market manufacturers importing from Asia — they have 2-person finance teams and zero compliance expertise."

**Bad Example**:
> "Cross-border payments are broken. They're slow, expensive, and non-compliant."

**Check**:
- [ ] The problem is quantified with a specific number
- [ ] The ICP is defined narrowly (not "all businesses")
- [ ] The investor can feel the pain (emotional hook)

---

### Slide 3: Solution

**Goal**: Show your solution is inevitable once the problem is understood.

**Structure**:
1. **The insight** (1 sentence): What did you see that others missed?
2. **How it works** (2–3 sentences): Mechanism, not architecture.
3. **Before/After**: One sentence contrasting old way vs. your way.

**Good Example**:
> "We built an end-to-end compliance settlement network using real-time sanction screening, automated KYC/KYB, and instant settlement rails. Instead of routing through 3 correspondent banks over 7 days, we settle directly in 4 hours with full audit trails."

**Bad Example**:
> "Our platform uses a microservices architecture with PostgreSQL, Redis, and Kubernetes on AWS."

**Check**:
- [ ] Describes outcome, not technology stack
- [ ] Contains a before/after contrast
- [ ] Can be explained to a 10-year-old

---

### Slide 4: Why Now?

**Goal**: Convince the investor the timing is non-negotiable.

**Structure**:
List 2–3 market tailwinds that make this business possible *now* but not 5 years ago.

**Examples**:
- Regulatory: "PSD2 + open banking APIs made real-time settlement legally possible in EU"
- Technology: "Cloud compliance tools dropped KYC cost from $50 to $5 per check"
- Behavior: "Post-COVID, 73% of CFOs now prioritize cash flow visibility over relationship banking"

**Check**:
- [ ] At least one tailwind is verifiable (cite source if possible)
- [ ] The tailwinds are accelerating, not static
- [ ] Without these tailwinds, the business doesn't work

---

### Slide 5: Market Size

**Goal**: Show the prize is worth the investor's time.

**Structure**:
```
TAM: $X billion (top-down, industry report)
SAM: $Y billion (bottom-up, reachable in 5–7 years)
SOM: $Z million (what you can capture in 2–3 years)
```

**Good Example**:
> "TAM: $180B cross-border B2B payments
> SAM: $12B mid-market Asia-Europe trade corridor
> SOM: $840M Chinese manufacturers with <500 employees"

**Bad Example**:
> "The fintech market is $300T. If we capture 0.01%..."

**Check**:
- [ ] TAM is from a credible source (not self-calculated)
- [ ] SAM is defensible (geography + segment + use case)
- [ ] SOM is achievable (implies realistic market share)

---

### Slide 6: Competition

**Goal**: Show you understand the landscape and have a differentiated position.

**Structure**:
1. **2x2 matrix**: X-axis = speed, Y-axis = compliance depth (pick axes relevant to your market)
2. **Where you sit**: Explain *why* you're in the top-right.
3. **Moat preview**: Hint at what's hard to replicate (don't fully reveal yet).

**Good Example**:
> "Legacy banks (bottom-left): 7 days, high compliance but manual. Fintechs (top-left): 1 day, low compliance. We're the only player in top-right: 4 hours + full automated compliance."

**Check**:
- [ ] You acknowledge real competitors (not "we have no competition")
- [ ] The axes are meaningful to customers, not just to you
- [ ] You explain why others can't easily move to your position

---

### Slide 7: Product

**Goal**: Show the product is real and differentiated.

**Structure**:
1. **Screenshot/demo**: One image or 30-sec Loom.
2. **Key differentiator**: One feature no one else has.
3. **Integration**: How customers adopt (API, dashboard, Slack bot, etc.).

**Check**:
- [ ] There's visual evidence (screenshot, not wireframe)
- [ ] The differentiator is defensible (not "better UI")
- [ ] Adoption path is low-friction

---

### Slide 8: Business Model

**Goal**: Show how you make money and that the economics work.

**Structure**:
1. **Pricing**: Simple, transparent. One primary model.
2. **Unit economics**: CAC, LTV, gross margin if available.
3. **Expansion revenue**: How customers grow over time.

**Good Example**:
> "SaaS: 0.15% per transaction + $2k/mo platform fee. Enterprise: custom pricing.
> Unit economics: CAC $4,200 (inside sales), LTV $48,000, gross margin 82%."

**Check**:
- [ ] Pricing is simple enough to explain in one breath
- [ ] Unit economics are directionally correct (don't need perfection)
- [ ] There's a path to expansion revenue

---

### Slide 9: Traction

**Goal**: Prove momentum. This is the most important slide for early-stage.

**Structure**:
1. **The one metric that matters**: Pick the metric that best shows product-market fit.
2. **Trend line**: Show growth over time (6–12 months).
3. **Logo wall**: 3–5 customer logos (with permission).

**Metric Selection Guide**:
| Stage | Best Metric |
|-------|------------|
| Pre-launch | Waitlist size + engagement rate |
| Post-launch | MAU/DAU + retention curve |
| Revenue | MRR + MoM growth rate |
| Scale | Net revenue retention + expansion rate |

**Good Example**:
> "120+ enterprise customers, $50k MRR, 12% MoM growth last 6 months. Core vertical renewal 90%+."

**Check**:
- [ ] The metric is a leading indicator (not vanity)
- [ ] There's a trend (growth, not a static number)
- [ ] The metric is specific ("120 customers" not "rapidly growing")

---

### Slide 10: Team

**Goal**: Answer "Why you?" — why this team will win.

**Structure**:
1. **Founders**: Relevant experience, not credentials.
2. **Key hires**: Who you've recruited that validates the vision.
3. **Advisors**: 1–2 credible names if available.

**Good Example**:
> "CEO — ex-Ant Group payments lead (8 yrs, built $2B settlement product). CTO — ex-infrastructure architect at Stripe. COO — ex-HSBC compliance director."

**Bad Example**:
> "Team has degrees from MIT, Stanford, and Harvard."

**Check**:
- [ ] Each team member's experience directly maps to the business
- [ ] Credentials are secondary to relevant achievements
- [ ] There's no "MBA from HBS" without context

---

### Slide 11: Financials

**Goal**: Show you understand the financial trajectory.

**Structure**:
1. **Historical** (if any): Revenue, burn, runway.
2. **Projections**: 3-year forecast. Conservative, base, optimistic.
3. **Use of funds**: Where the new money goes.

**Rule**: Never show a hockey stick without explaining *what changes* to make it happen.

**Check**:
- [ ] Projections are bottom-up ("10 sales reps x 5 deals/quarter x $50k ACV") not top-down ("1% market share")
- [ ] Burn rate and runway are disclosed
- [ ] Use of funds is specific ("hire 3 engineers" not "growth")

---

### Slide 12: The Ask

**Goal**: Make it easy to say yes.

**Structure**:
```
We're raising $X on a $Y pre-money valuation.
Use of funds: [specific allocation]
Milestones with this round: [3 measurable goals]
```

**Good Example**:
> "Raising $1.1M on $8.3M pre-money.
> Use: 40% engineering (compliance automation), 30% sales (2 senior AEs), 30% operations.
> Milestones: $200k MRR, 3 enterprise pilots, EU regulatory approval."

**Check**:
- [ ] The amount is specific (not "$1–2M")
- [ ] Valuation is stated (or "open to discussion")
- [ ] Milestones are measurable and time-bound

---

## Self-Review Checklist

Before sending, run through this:

- [ ] Can I read the entire deck in 3 minutes?
- [ ] Is every number sourced or defensible?
- [ ] Do I explain "why now" with market tailwinds?
- [ ] Is the team slide about relevant experience, not credentials?
- [ ] Does the traction slide show a trend, not a snapshot?
- [ ] Is the ask specific with measurable milestones?
- [ ] Are there zero buzzwords (disrupt, synergy, AI-powered)?
- [ ] Would my mom understand the problem and solution?

## Anti-Patterns to Avoid

1. **The "Everything Deck"**: >15 slides. Cut to 10.
2. **The "TAM Fantasy"**: Top-down market size without SAM/SOM.
3. **The "No Competition" Claim**: Every market has competition. Acknowledge it.
4. **The "Team of Geniuses"**: Credentials without relevant experience.
5. **The "Hockey Stick"**: Exponential growth projections without mechanism.
