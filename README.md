# Founder Skills for AI Agents

A collection of AI agent skills designed for startup founders. Build pitch decks, convert presentations, research investors, and scale your content — all with AI coding agents like Claude Code, OpenAI Codex, Cursor, and Windsurf.

Part of [UniqueClub](https://uniqueclub.ai) — tools and community for ambitious founders.

Built by [吴畏 (Wu Wei)](https://github.com/wulaosiji). Want hands-on help with your startup? Check out [UniqueClub](https://uniqueclub.ai) for founder resources, pitch reviews, and growth strategies.

**Contributions welcome!** Have a skill idea or improvement? [Open an issue](https://github.com/wulaosiji/founder-skills/issues) or submit a PR.

---

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for founder-specific tasks. When you add these to your project, your agent recognizes when you're working on fundraising, content, or growth — and applies the right frameworks automatically.

---

## How Skills Work Together

Skills reference each other and build on shared context. Start with `unique-club-founder-kit` as your foundation — it establishes your startup context, then other skills use that to generate personalized outputs.

```
                    ┌─────────────────────────────────────┐
                    │    unique-club-founder-kit          │
                    │  ( establishes startup context )    │
                    │  • company name & one-liner         │
                    │  • problem & solution               │
                    │  • target market & traction         │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────────┬───────────┼───────────┬──────────────┐
        ▼              ▼           ▼           ▼              ▼
   ┌──────────┐  ┌──────────┐ ┌────────┐ ┌──────────┐ ┌──────────┐
   │ Fundraise│  │ Content  │ │ Research│ │  Growth  │ │  Daily   │
   │          │  │          │ │         │ │          │ │          │
   ├──────────┤  ├──────────┤ ├────────┤ ├──────────┤ ├──────────┤
   │pitch-deck│  │content-  │ │investor│ │seo-audit │ │founder-  │
   │  creator │  │multiplier│ │research│ │         │ │daily-brief│
   │          │  │          │ │         │ │         │ │          │
   │deck-web  │  │          │ │         │ │         │ │          │
   │converter │  │          │ │         │ │         │ │          │
   └──────────┘  └──────────┘ └────────┘ └──────────┘ └──────────┘
```

**Workflow Example:**
1. Start with `unique-club-founder-kit` — define your startup context once
2. Use `pitch-deck-creator` — generates a 10-page VC-ready deck using your context
3. Use `deck-web-converter` — converts that deck into a responsive HTML page for sharing

---

## Available Skills

| Skill | Description | Triggers |
|-------|-------------|----------|
| [unique-club-founder-kit](skills/unique-club-founder-kit/) | Foundation skill. Sets up your startup context (problem, solution, market, traction) once, used by all other skills. | "帮我建立创始人档案", "startup context", "公司介绍模板", "founder kit" |
| [pitch-deck-creator](skills/pitch-deck-creator/) | Generate a professional, VC-ready 10-page pitch deck as a .pptx file. Auto-adapts to your startup context. | "帮我写商业计划书", "生成BP", "做融资PPT", "pitch deck", "fundraising deck" |
| [deck-web-converter](skills/deck-web-converter/) | Convert PPT/PDF pitch decks into responsive HTML for web sharing. Mobile-friendly, fast-loading. | "BP转网页", "PPT转HTML", "pitch deck online", "网页版BP" |

**Coming Soon:**
- `investor-research` — Research VCs, angels, and accelerator fit
- `content-multiplier` — Turn one piece of content into 10+ variations
- `founder-daily-brief` — Daily startup news, competitor moves, and opportunities

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
```

You can also invoke skills directly:

```
/unique-club-founder-kit
/pitch-deck-creator
/deck-web-converter
```

---

## Skill Network

Skills are designed to work together:

- **unique-club-founder-kit** → **pitch-deck-creator**: Your startup context feeds directly into deck generation
- **pitch-deck-creator** → **deck-web-converter**: Seamless flow from .pptx to web
- **investor-research** (coming) → **pitch-deck-creator**: Tailor deck to specific investor thesis

---

## Requirements

- Claude Code, Cursor, or any AI agent supporting the [Agent Skills spec](https://agentskills.io)
- For `pitch-deck-creator`: Python with `python-pptx` library
- For `deck-web-converter`: Node.js for web conversion tools

---

## About UniqueClub

These skills are part of the **UniqueClub** founder toolkit.

🌐 **https://uniqueclub.ai** — Tools, community, and resources for startup founders.

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
