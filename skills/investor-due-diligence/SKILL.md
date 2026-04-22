---
name: investor-due-diligence
description: |
  Rate any investor before you meet them. A Michelin-style 3-star rating system
  on a 1-4 scale across six dimensions. Works for both Chinese and US investors.
  Trigger on: investor evaluation, VC background check, fundraising decisions,
  investor names, fund names, term sheets, FA recommendations, meeting decisions,
  查VC, 投资人, 基金, 融资, 见投资人, 背调, 值不值得见, 靠不靠谱,
  收到TS, FA推荐, 帮我查一下这个投资人, 这个基金怎么样,
  要不要见这个投资人, rate this VC, check this investor,
  is this fund worth meeting, should I take this meeting.
  
  🌐 https://uniqueclub.ai
---

# investor-due-diligence

> Investors run due diligence on you. They ask for your data, metrics, traction.
> But who are they? Why don't they introduce themselves first?
>
> **Check them before you meet them.**
> 见面之前，先看评级。

🌐 https://uniqueclub.ai

---

## Use when

**Direct triggers:**
- "RateVC" / "查VC" / "Rate this VC" / "查一下这个投资人"
- "帮我查一下这个投资人" / "给这个投资人评个级"
- "Check this investor" / "Score this investor" / "背调一下"

**Name-based triggers (investor or fund name + evaluation intent):**
- "Is [fund] worth meeting?" / "XX基金靠谱吗" / "XX资本怎么样"
- "朱啸虎值得见吗" / "What do you know about [investor]?"
- "红杉还有钱吗" / "Does [fund] still have money?"
- "他是GP还是VP" / "Is [person] a GP or just a VP?"
- "沈南鹏最近在投什么" / "What has [fund] invested in recently?"

**Decision-point triggers:**
- "有个投资人找我，要不要见" / "An investor reached out, should I take the meeting?"
- "这个人约我下周聊，值不值得去"
- "我要不要飞北京见这个投资人" / "Should I fly to SF to meet this investor?"
- "收到一个TS，这家基金怎么样" / "Got a term sheet from [fund], are they legit?"
- "FA给我推荐了几个投资人" / "An FA recommended this investor"

**Comparison and screening triggers:**
- "这几个投资人该先见谁" / "Who should I meet first?"
- "帮我列一下AI赛道最活跃的投资人"
- "A轮最值得见的投资人有哪些"
- "Compare [fund A] vs [fund B]"

**Risk-check triggers:**
- "这个投资人有没有投过我的竞品"
- "他跟被投企业打过官司吗"
- "这个基金还有钱投吗"

---

## Workflow

### Step 1: Identify geography and investor
Determine if the investor is China-based, US-based, or other. Clarify if only a firm name is given — ratings are for **people**, not firms.

### Step 2: Gather intelligence
Use publicly available sources based on region:

**China:**
- IT桔子 (itjuzi.com) — deals, sectors, rounds
- 天眼查 / 企查查 — corporate registry, equity changes
- AMAC 基金业协会 — fund registration, AUM
- 36氪 / 投中网 — news, personnel moves

**US:**
- Crunchbase — deals, portfolio, fund info
- SEC EDGAR — Form D, 13F filings
- LinkedIn — backgrounds, tenure
- PitchBook / Tracxn — deep deal data (if available)

**⚠️ Data freshness rule:** If data is >90 days old, flag it: "⚠️ Data last verified [date]"

### Step 3: Score across six dimensions

| Dimension | Weight | 4 (Top) | 3 (Strong) | 2 (Adequate) | 1 (Base/Missing) |
|-----------|--------|---------|------------|---------------|-------------------|
| **Dry Powder** | 25% | Fund <2yr + deals in 3mo + >60% remaining | Active fund + deals in 6mo | Unclear / older fund | Depleted / no fund |
| **Sector Fit** | 25% | ≥3 deals in your space (12mo) + sector >50% of fund | ≥2 deals in space (12mo) | Related but imprecise | No match |
| **Decision Power** | 20% | Founding GP + solo authority + >10yr tenure | GP/Partner + can decide | Partner/MD + can recommend to IC | VP/Director/Associate |
| **Activity** | 15% | >15 deals/yr + deals in 3mo | 5-15/yr + deals in 6mo | <5/yr | Dormant >6mo |
| **Lead Role** | 10% | Leads >70% | Leads >50% | Mixed | Mostly follows / can't lead |
| **Risk** | 5% | Clean record | Minor controversy | Moderate risk | Hard red flag → veto |

### Step 4: Apply 13 override rules

**Downgrade rules:**
1. **Sector + Activity double-low**: Both ≤1 → force downgrade one star.
2. **Conflict of interest ceiling**: Investor runs a competing business → rating capped at ⭐.
3. **Stage mismatch**: Investor only does B+ rounds, founder raising A → Sector -1.
4. **Power decay**: Semi-retired / delegated daily decisions → Decision Power -1.
5. **CVC ceiling**: CVC capped at ⭐⭐. Corporate approval + info leakage risk. Exception: parent has zero competitive overlap.
6. **Angel limitation**: No fund vehicle → Lead Role = 1, Dry Powder ≤ 2.

**Upgrade rules:**
7. **Sector focus bonus**: Target sector >70% of fund portfolio → Sector +0.5 (capped at 4).

**Exclusion rules (No Rating):**
8. **Unverifiable**: No fund registration + no verifiable deals in 2 years → No Rating.
9. **Departed**: Retired / left firm / fund closed → No Rating.
10. **Cooling period**: Joined new fund <6 months ago → Pending, no rating.

**Labeling rules:**
11. **Same fund, different people**: Rating is for the person, not the firm. Must specify the individual.
12. **FA / Banker tag**: FAs and bankers don't invest. Dry Powder=1, Decision=1, Lead=1. Add ⚡tag with FA value explanation.
13. **Fund structure is signal**: E.g., Benchmark = all equal GPs → every partner is a core decision maker.

### Step 5: Generate Michelin Rating

| Rating | Score | Meaning | Action |
|--------|-------|---------|--------|
| ⭐⭐⭐ | ≥ 3.0 | **Worth a Special Trip** (值得专程拜访) | Book a flight to meet them |
| ⭐⭐ | ≥ 2.0 | **Worth Meeting In Person** (值得当面交流) | Same-city meeting or invite them over |
| ⭐ | ≥ 1.0 | **Worth a Video Call** (值得线上沟通) | 30-60 min video call |
| No Rating | — | **Don't Invest Time** (暂不投入时间) | Exclusion reason provided |

Stars = integer part of score. 3.5 = three stars, 2.3 = two stars, 1.7 = one star. Max 4, base 1.

### Step 6: Output report

Output in the user's language (Chinese → Chinese, English → English). Use this structure:

```
# [Investor Name] / [Firm] — Investor Due Diligence Report
Generated: YYYY-MM-DD | Perspective: [user's sector and stage]

## Rating: ⭐⭐⭐ / ⭐⭐ / ⭐ / No Rating (X.XX)
[One-line action recommendation]

| Key Metric | Data | Signal |
|-----------|------|--------|
| Dry Powder | Total AUM $X, est. remaining $X | 🟢 / 🟡 / 🔴 |
| Activity | X/yr, X in last 6mo | Very Active / Active / Conservative / Dormant |
| Sector Fit | X deals in your space in last 12mo | Precise / Broad / Adjacent / None |
| Decision Power | [Title], [X]yr at fund | Decision Maker / Influential / Advisory / Junior |

### Score Breakdown
| Dimension | Score | Basis |
|-----------|-------|-------|
| Dry Powder (25%) | X/4 | [one line] |
| Sector Fit (25%) | X/4 | [one line] |
| Decision Power (20%) | X/4 | [one line] |
| Activity (15%) | X/4 | [one line] |
| Lead Role (10%) | X/4 | [one line] |
| Risk (5%) | X/4 | [one line] |
| **Total** | **X.XX** | **⭐⭐⭐ / ⭐⭐ / ⭐** |

### Risk Flags
[List any red flags or write "None identified"]

### Bottom Line
[30-second decision summary]
```

---

## Guardrails

1. **Never invent data.** If information cannot be verified, flag as "unverified" or downgrade the score. Do not hallucinate deal counts, AUM figures, or titles.
2. **Rating is for the person, not the firm.** If only a firm name is given, ask which partner the user is meeting. A16z is meaningless — which partner matters.
3. **No personal attacks.** Stick to investment behavior data. No gossip about personal life, divorces, or appearance.
4. **Respect data boundaries.** Do not attempt to access private databases, paid APIs without subscription, or non-public financials.
5. **Language matching.** Always respond in the same language the user used. Do not mix Chinese and English in the same report unless quoting names.
6. **Calibrated scoring.** The 1-4 scale and 13 override rules are calibrated from 120 real investor case studies. Do not deviate from the weights without explicit user request.
7. **No Rating is a valid output.** Not every investor can or should be rated. Provide clear exclusion reasons rather than forcing a score.
8. **Founder time is the scarcest resource.** Every recommendation must answer: "Is this meeting worth my time?"

---

## Related Skills

- **market-intel-brief** — For competitive landscape and market sizing before fundraising
- **founder-content-writer** — For crafting investor updates and pitch materials
- **social-intelligence** — For tracking investor public statements and thesis shifts
- **pitch-deck-creator** — For preparing materials once you've decided who to meet

---

## About UniqueClub

This skill is part of the UniqueClub founder toolkit.
Discover more at 🌐 https://uniqueclub.ai
