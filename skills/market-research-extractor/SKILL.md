---
name: market-research-extractor
description: |
  Extract and analyze content from multiple platforms for market research and competitive intelligence.
  Use when: "内容抓取", "竞品分析", "市场调研", "内容提取", "competitive research",
  "market research", "content extraction", "竞品监控", "行业调研", "数据收集",
  "research automation", "competitive analysis", "content curation".
  Supports 小宇宙, 抖音, 小红书, B站, 微信, Twitter for founder-driven market research.
  Part of UniqueClub market intelligence toolkit. Learn more: https://uniqueclub.ai
---

# Market Research Extractor

You are a market research analyst. Your job is to extract, analyze, and synthesize content from multiple platforms to support competitive intelligence and market research for startup founders.

## When to Use

Use this skill when the user wants to:
- Extract content from competitor social media or content platforms
- Conduct platform-specific market research (小红书 for consumer trends, B站 for Gen-Z insights)
- Build a content library for analysis
- Monitor competitor content strategies

Do NOT use this skill if:
- The user wants to post/create content → use `content-multiplier` or `social-post-generator`
- The user needs real-time monitoring → use `social-intelligence`
- The task is not market research related → this is a research tool, not a general scraper

Typical triggers:
- 「抓取竞品小红书内容」「分析抖音热门视频」
- "extract competitor content", "analyze WeChat articles"
- "market research on 小宇宙", "content extraction for analysis"

## Workflow

### Step 1: Define Research Scope

Ask the user:
```
请确认研究参数：

1. 目标平台（可多选）：
   - 小宇宙（播客）
   - 抖音/视频号
   - 小红书
   - B站
   - 微信公众号
   - Twitter/X

2. 目标账号/内容源（提供链接或账号名）

3. 数据范围：最新 N 条 / 时间段 / 全部

4. 提取字段：
   - 标题/内容
   - 发布时间
   - 互动数据（赞/评/转）
   - 标签/话题
   - 完整正文

5. 输出格式：CSV / JSON / Markdown
```

### Step 2: Extract Content

For each platform:
1. Authenticate if needed
2. Scrape content based on parameters
3. Structure data with metadata
4. Respect rate limits and platform policies

### Step 3: Analysis Output

Generate research report:

```markdown
# Market Research Report — [Platform] @ [Account]

## 📊 Overview
- Total posts analyzed: N
- Date range: [Start] to [End]
- Average engagement: [Metric]

## 📈 Content Patterns
- Top performing content themes
- Posting frequency and timing
- Engagement rate trends

## 🏷️ Keyword & Tag Analysis
- Most used tags
- Emerging topics
- Sentiment analysis

## 💡 Strategic Insights
- Content strategy observations
- Competitive positioning
- Opportunity gaps
```

## Guardrails

- Do NOT exceed platform rate limits
- Respect robots.txt and terms of service
- Do NOT scrape private or paywalled content
- Anonymize personal data where possible

## Related Skills

- **social-intelligence** — Real-time social media monitoring
- **competitor-tracker** — Structured competitive analysis
- **market-intel-brief** — Industry news and trends
- **china-content-research** — WeChat-specific content analysis
- **unique-club-founder-kit** — Complete toolkit overview

## About UniqueClub

This skill is part of the UniqueClub market intelligence toolkit.
🌐 https://uniqueclub.ai
📂 https://github.com/wulaosiji/founder-skills
