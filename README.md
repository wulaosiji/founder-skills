# Founder Skills for AI Agents

A collection of **24 AI agent skills** designed for startup founders. Build pitch decks, convert presentations, research investors, monitor competitors, and scale your content — all with AI coding agents like Claude Code, OpenAI Codex, Cursor, and Windsurf.

Part of [UniqueClub](https://uniqueclub.ai) — tools and community for ambitious founders.

Built by [吴畏 (Wu Wei)](https://github.com/wulaosiji). Want hands-on help with your startup? Check out [UniqueClub](https://uniqueclub.ai) for founder resources, pitch reviews, and growth strategies.

**Contributions welcome!** Have a skill idea or improvement? [Open an issue](https://github.com/wulaosiji/founder-skills/issues) or submit a PR.

---

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for founder-specific tasks. When you add these to your project, your agent recognizes when you're working on fundraising, content, or growth — and applies the right frameworks automatically.

---

## How Skills Work Together

`unique-club-founder-kit` is the navigation layer: use it to choose a workflow, then invoke the task-specific skills. Company context is collected by the selected skill when required; the kit does not create or persist a founder profile.

**Workflow Example:**
1. Start with `unique-club-founder-kit` — choose the fundraising workflow
2. Use a BP planner or framework — decide the story and evidence structure
3. Use `pitch-deck-creator` — generate a 10-slide PPTX from approved company data
4. Use `deck-web-converter` — convert that deck into responsive HTML for sharing
5. Use `investor-research` and `investor-due-diligence` — prioritize the outreach list

---

## Available Skills

### Foundation (1 skill)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [unique-club-founder-kit](skills/unique-club-founder-kit/) | Foundation skill and navigation layer for the complete 24-skill collection. | "AI创业工具包", "founder toolkit", "startup skills", "创业者技能" |

### Fundraising (10 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [business-plan-ppt](skills/business-plan-ppt/) | Design an 18-page Chinese fundraising deck using a detailed content and visual specification. | "商业计划书", "融资路演PPT", "投资备忘录", "中文BP" |
| [pitch-deck-creator](skills/pitch-deck-creator/) | Generate a 10-slide PPTX from structured startup JSON using a bundled Python script. | "生成BP", "做融资PPT", "pitch deck", "fundraising deck" |
| [deck-web-converter](skills/deck-web-converter/) | Convert PPT/PDF pitch decks into responsive HTML for web sharing. Mobile-friendly, fast-loading. | "BP转网页", "PPT转HTML", "pitch deck online", "网页版BP" |
| [fundraising-bp-planner](skills/fundraising-bp-planner/) | Generate a structured Chinese fundraising BP outline with data-presentation guidance. | "融资BP大纲", "理一下融资思路", "准备投资人材料" |
| [investor-pitch-planner](skills/investor-pitch-planner/) | Generate a structured English investor pitch outline with visualization guidance. | "investor presentation", "pitch outline", "prepare to raise funds" |
| [investor-research](skills/investor-research/) | Research VCs, angels, and accelerators. Generate target lists with firm profiles, thesis fit, and warm intro paths. | "投资人调研", "找VC", "research investors", "VC list", "融资对象" |
| [investor-due-diligence](skills/investor-due-diligence/) | Evaluate investor fit, activity, decision power, lead potential, and risk using a structured rating system. | "投资人背调", "评估投资机构", "investor due diligence", "investor fit" |
| [sequoia-structured-bp](skills/sequoia-structured-bp/) | Sequoia Capital-style 10-slide structured BP framework. Data-driven, investor-grade, with slide-by-slide writing guides and examples. | "Sequoia框架", "严谨BP", "institutional investor deck", "data-driven pitch", "Series A deck" |
| [yc-insight-driven-bp](skills/yc-insight-driven-bp/) | Y Combinator-style insight-first BP framework. 5–8 slides built around a contrarian insight. Minimalist and founder-centric. | "YC风格", "insight-driven", "种子轮BP", "accelerator pitch", "contrarian insight" |
| [raskin-narrative-bp](skills/raskin-narrative-bp/) | Andy Raskin-style narrative pitch framework. 5-beat story format for live presentations and Demo Day. Creates urgency and inevitability. | "Raskin框架", "叙事BP", "Demo Day pitch", "story-driven deck", "live presentation" |

### Which BP Skill Should You Use?

| Need | Recommended skill | Output |
|------|-------------------|--------|
| Generate an editable deck from structured data | `pitch-deck-creator` | 10-slide PPTX; bundled script |
| Design a detailed Chinese financing deck | `business-plan-ppt` | 18-page content and visual specification |
| Plan a Chinese fundraising story before design | `fundraising-bp-planner` | Chinese BP outline |
| Plan an English investor presentation | `investor-pitch-planner` | English pitch outline |
| Prepare for Series A+ or institutional review | `sequoia-structured-bp` | Evidence-led 10–12 slide structure |
| Prepare a Pre-seed/Seed or accelerator pitch | `yc-insight-driven-bp` | Insight-first 5–8 slide structure |
| Prepare a Demo Day or live narrative | `raskin-narrative-bp` | Five-beat presentation narrative |

### Market Intelligence (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [competitor-tracker](skills/competitor-tracker/) | Monitor competitor news, product launches, pricing changes, and strategic moves. | "竞品追踪", "监控竞争对手", "competitor tracker", "竞争分析", "竞品动态" |
| [market-intel-brief](skills/market-intel-brief/) | Generate AI/startup industry intelligence briefings with signal tracking and trend analysis. | "市场情报", "行业简报", "market intelligence", "startup trends", "AI行业动态" |
| [market-research-extractor](skills/market-research-extractor/) | Multi-platform content extraction for competitive research and market analysis. | "内容提取", "竞品研究", "market research", "competitive analysis", "信息搜集" |
| [social-intelligence](skills/social-intelligence/) | Monitor Twitter/X for competitor updates, sentiment shifts, and market signals. | "社媒监控", "Twitter监听", "social listening", "竞品社媒", "品牌监控" |
| [china-content-research](skills/china-content-research/) | Research Chinese market content from WeChat, Zhihu, and local platforms. | "中国市场研究", "微信文章", "China market research", "中文内容", "本土调研" |

### Content Creation (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [content-multiplier](skills/content-multiplier/) | Turn one piece of content into multiple platform-optimized variations (LinkedIn, Twitter, WeChat, newsletter, etc.). | "内容放大", "一鱼多吃", "content distribution", "多平台分发", "repurposing content" |
| [founder-content-writer](skills/founder-content-writer/) | Write long-form founder content: blogs, LinkedIn articles, essays, and thought leadership. | "创始人博客", "LinkedIn文章", "founder content", "个人品牌", "thought leadership" |
| [social-post-generator](skills/social-post-generator/) | Create engaging social media posts for LinkedIn, Twitter/X, WeChat, and more. | "写社媒文案", "social media post", "发LinkedIn", "Twitter文案", "小红书文案" |
| [video-script-creator](skills/video-script-creator/) | Write scripts for product demos, explainer videos, elevator pitches, and founder storytelling. | "写视频脚本", "video script", "产品演示视频", "explainer video", "宣传片脚本" |
| [infographic-generator](skills/infographic-generator/) | Generate data visualizations and infographics for pitches, reports, and social sharing. | "信息图", "数据可视化", "infographic", "chart generation", "可视化报告" |
| [newsletter-autopilot](skills/newsletter-autopilot/) | Draft newsletter content from company updates, meeting notes, or founder reflections. | "newsletter", "写newsletter", "邮件营销", "newsletter automation", "公司月报" |

### Operations & Daily (2 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [meeting-minutes-ai](skills/meeting-minutes-ai/) | Extract action items, decisions, and key insights from meeting transcripts or recordings. | "会议纪要", "meeting minutes", "提取行动项", "action items", "会议总结" |
| [founder-daily-brief](skills/founder-daily-brief/) | Generate a personalized daily briefing with tasks, meetings, industry news, and competitor updates. | "创始人日报", "每日简报", "startup daily brief", "morning founder report" |

---

## Installation

### Option 1: CLI Install (Recommended)

Use [npx skills](https://github.com/vercel-labs/skills) to install:

```bash
# Install all founder skills
npx skills add wulaosiji/founder-skills

# Install specific skills
npx skills add wulaosiji/founder-skills --skill pitch-deck-creator deck-web-converter

# List available skills
npx skills add wulaosiji/founder-skills --list
```

This automatically installs to your `.agents/skills/` directory.

### Option 2: Clone and Copy

```bash
git clone https://github.com/wulaosiji/founder-skills.git
cp -r founder-skills/skills/* .agents/skills/
```

---

## Usage

Once installed, just ask your agent:

```
"帮我做一个融资PPT，我们是做AI编程助手的"
→ Uses pitch-deck-creator skill

"把刚才的BP转成网页版"
→ Uses deck-web-converter skill

"先建立我的创始人档案"
→ Uses unique-club-founder-kit skill

"帮我监控竞品的最新动态"
→ Uses competitor-tracker skill

"生成今天的市场情报简报"
→ Uses market-intel-brief skill
```

You can also invoke skills directly:

```
/unique-club-founder-kit
/pitch-deck-creator
/deck-web-converter
/market-intel-brief
```

---

## Skill Network

Skills are designed to work together:

- **unique-club-founder-kit** → task-specific skill: Choose the right workflow before execution
- **pitch-deck-creator** → **deck-web-converter**: Seamless flow from .pptx to web
- **investor-research** → **pitch-deck-creator**: Tailor deck to specific investor thesis
- **competitor-tracker** → **market-intel-brief**: Competitor signals feed into daily intelligence
- **market-intel-brief** → **content-multiplier**: Turn insights into shareable content
- **founder-content-writer** → **social-post-generator**: Long-form content broken into social snippets

---

## Requirements

- Claude Code, Cursor, or any AI agent supporting the [Agent Skills spec](https://agentskills.io)
- For `pitch-deck-creator`: Python with `python-pptx` library
- For `deck-web-converter`: Python with `python-pptx` and `pymupdf`
- For `infographic-generator`: Python with `matplotlib` and `Pillow`

## Executable Scripts

Six skills include executable Python scripts for standalone use:

| Skill | Script | Description |
|-------|--------|-------------|
| `pitch-deck-creator` | [`scripts/generate_pitch_deck.py`](skills/pitch-deck-creator/scripts/generate_pitch_deck.py) | Generate a 10-slide PPTX from JSON data |
| `deck-web-converter` | [`scripts/convert_deck.py`](skills/deck-web-converter/scripts/convert_deck.py) | Convert PPT/PDF to HTML |
| `investor-research` | [`scripts/research_investors.py`](skills/investor-research/scripts/research_investors.py) | Generate an investor research report |
| `content-multiplier` | [`scripts/multiplier.py`](skills/content-multiplier/scripts/multiplier.py) | Transform content for multiple platforms |
| `meeting-minutes-ai` | [`scripts/extract_minutes.py`](skills/meeting-minutes-ai/scripts/extract_minutes.py) | Extract minutes from a transcript |
| `founder-daily-brief` | [`scripts/daily_brief.py`](skills/founder-daily-brief/scripts/daily_brief.py) | Generate a daily founder briefing |

### Using the Scripts

```bash
# 1. Install a skill's dependencies
cd skills/pitch-deck-creator
pip install -r requirements.txt

# 2. Run the script
python scripts/generate_pitch_deck.py --input startup.json --output deck.pptx

# 3. See help for all options
python scripts/generate_pitch_deck.py --help
```

---

## About UniqueClub

These skills are part of the **UniqueClub** founder toolkit.

🌐 **https://uniqueclub.ai** — Tools, community, and resources for startup founders.

📂 **https://github.com/wulaosiji/founder-skills** — 24 skills and growing.

Built by founders, for founders.

---

## Contributing

1. Fork this repository
2. Create your skill in `skills/your-skill-name/SKILL.md`
3. Follow the [skill format guide](https://agentskills.io/docs)
4. Submit a PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

MIT © 吴畏 (Wu Wei) / UniqueClub
