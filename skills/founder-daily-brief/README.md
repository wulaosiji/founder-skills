# Founder Daily Brief

Generate a personalized daily briefing for startup founders. Compiles tasks, meetings, industry news, competitor updates, and personal priorities into a structured daily brief.

## Usage

### Quick Start

```bash
cd skills/founder-daily-brief
python scripts/daily_brief.py --input config.json --output brief.md
```

### Input JSON Format

```json
{
    "company_name": "DevAI",
    "stage": "growth",
    "date": "2024-01-15",
    "language": "en",
    "priorities": [
        {"task": "Review Q1 roadmap with engineering", "reason": "Alignment is critical before sprint planning"},
        {"task": "Send investor update email", "reason": "Monthly reporting commitment"},
        {"task": "Customer interview #5", "reason": "Validating new feature hypothesis"}
    ],
    "schedule": [
        {"time": "9:00 AM", "event": "Daily Standup", "prep": "Review sprint board", "goal": "Clear blockers"},
        {"time": "11:00 AM", "event": "Investor Call", "prep": "Update deck", "goal": "Get warm intro to Series A lead"},
        {"time": "2:00 PM", "event": "Customer Interview", "prep": "Prepare questions", "goal": "Validate pricing model"}
    ],
    "tasks": [
        {"task": "Finalize term sheet feedback", "priority": "high", "deadline": "EOD"},
        {"task": "Review product mockups", "priority": "high"},
        {"task": "Draft blog post on AI trends", "priority": "medium"},
        {"task": "Update CRM with new leads", "priority": "low"}
    ],
    "news": [
        {"headline": "OpenAI announces GPT-5 preview", "summary": "New model shows 40% improvement on coding benchmarks", "source": "TechCrunch"},
        {"headline": "VC funding for AI tools up 25%", "summary": "Developer tools category seeing renewed investor interest", "source": "PitchBook"}
    ],
    "competitors": [
        {"name": "CodeGen AI", "update_type": "Funding", "description": "Raised $10M Series A", "implication": "Market validation for our space, need to differentiate on privacy"}
    ],
    "metrics": {
        "revenue": "$45K",
        "revenue_goal": "$50K",
        "active_users": "2,400",
        "growth": "12",
        "new_signups": "180",
        "churn": "3.2%"
    }
}
```

### Command Line Options

```bash
python scripts/daily_brief.py --help

# Required:
#   --input, -i   Path to JSON config file

# Optional:
#   --output, -o  Output markdown file path (default: Founder_Brief_{date}.md)
```

### Generated Sections

1. **Today's Top 3** - Prioritized focus areas with reasoning
2. **Schedule & Meetings** - Calendar with prep notes and goals
3. **Action Items** - High/medium/low priority task lists
4. **Industry Updates** - Curated news with insight prompts
5. **Competitor Tracker** - Competitor moves and implications
6. **Founder Mindset** - Daily quote with context and action
7. **Key Metrics** - Revenue, users, growth, churn blanks
8. **Quick Scan Version** - One-line summary for mobile

### Language Support

Set `"language": "zh"` for Chinese briefs, `"en"` for English.

```bash
# English brief
python scripts/daily_brief.py -i config_en.json

# Chinese brief
python scripts/daily_brief.py -i config_zh.json
```

### Stage-Based Tips

The script adapts focus tips based on company stage:

| Stage | Tip Theme |
|-------|-----------|
| `early` | Product-market fit, customer conversations, speed |
| `growth` | Scaling, metrics alignment, hiring |
| `expansion` | Operational efficiency, standardization, discipline |

### Example

```bash
# Minimal config
cat > brief_config.json << 'EOF'
{
    "company_name": "MyStartup",
    "stage": "early",
    "language": "en",
    "tasks": [
        {"task": "Talk to 3 customers", "priority": "high"},
        {"task": "Update landing page", "priority": "medium"}
    ]
}
EOF

# Generate brief
python scripts/daily_brief.py -i brief_config.json
# Output: Founder_Brief_2024-01-15.md
```

### Daily Routine Integration

Suggested workflow:

```
Morning (8:00 AM):
├─ Review Founder Daily Brief (5 min)
├─ Confirm/adjust top 3 priorities (2 min)
└─ Block calendar for deep work (3 min)

Evening (6:00 PM):
├─ Update tomorrow's task list (5 min)
├─ Quick competitor/news scan (5 min)
└─ Send input for tomorrow's brief (2 min)
```

## Dependencies

- Python 3.7+
- No external dependencies

## License

MIT © UniqueClub
