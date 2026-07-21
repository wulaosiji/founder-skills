# Pitch Deck Creator

Generate a professional, VC-ready 10-page pitch deck as a .pptx file.

## Usage

### Quick Start

```bash
# Enter the skill directory and install its dependency
cd skills/pitch-deck-creator
python3 -m pip install -r requirements.txt

# Create startup.json using the schema below, then generate the deck
python3 scripts/generate_pitch_deck.py --input startup.json --output MyStartup_BP.pptx
```

### Input JSON Format

Create a JSON file with your startup information:

```json
{
    "project_name": "AI Assistant Pro",
    "tagline": "The AI-powered coding assistant for developers",
    "value_props": [
        "10x faster code completion",
        "Context-aware suggestions",
        "Privacy-first architecture"
    ],
    "pain_points": [
        {"title": "Slow Development", "description": "Developers spend hours writing repetitive code"},
        {"title": "Context Switching", "description": "Constantly looking up documentation breaks flow"},
        {"title": "Code Quality", "description": "Hard to maintain consistency across teams"}
    ],
    "market_size": {
        "tam": "$50B",
        "sam": "$10B",
        "som": "$500M"
    },
    "solution": {
        "features": [
            {"title": "Smart Completion", "description": "AI predicts your next line of code"},
            {"title": "Documentation", "description": "Inline docs and examples"},
            {"title": "Refactoring", "description": "One-click code improvements"}
        ],
        "differentiation": "Privacy-first, works offline"
    },
    "business_model": {
        "revenue_streams": ["SaaS Subscription", "Enterprise License", "API Access"],
        "pricing": "$29/month pro, $99/month team"
    },
    "product_status": {
        "demo": true,
        "users": "5,000 beta users",
        "metrics": "95% retention rate"
    },
    "competitors": [
        {"name": "GitHub Copilot", "comparison": "We focus on privacy"},
        {"name": "TabNine", "comparison": "Better context awareness"}
    ],
    "team": [
        {"name": "John Doe", "role": "CEO", "background": "Ex-Google, Stanford CS"},
        {"name": "Jane Smith", "role": "CTO", "background": "Ex-OpenAI, MIT PhD"}
    ],
    "traction": {
        "milestones": ["MVP Launch", "Beta Users", "First Revenue"],
        "metrics": "$10K MRR, 15% MoM growth"
    },
    "roadmap": {
        "short": ["Mobile app", "IDE plugins"],
        "mid": ["Enterprise features", "Team collaboration"],
        "long": ["AI code review", "Global expansion"]
    },
    "fundraising": {
        "amount": "$2M Seed",
        "equity": "15%",
        "use_of_funds": ["Engineering 50%", "Marketing 30%", "Operations 20%"]
    },
    "language": "en",
    "colors": {
        "primary": "#1a73e8",
        "dark": "#202124",
        "accent": "#34a853"
    }
}
```

### Command Line Options

```bash
python scripts/generate_pitch_deck.py --help

# Required:
#   --input, -i   Path to JSON input file

# Optional:
#   --output, -o  Output PPTX file path (default: {project_name}_BP.pptx)
```

### Generated Slides

The script creates a 10-slide pitch deck with:

1. **Cover** - Project name, tagline, value propositions
2. **Market Pain Points** - 3 key pain points with TAM/SAM/SOM
3. **Solution** - Product features and differentiation
4. **Business Model** - Revenue streams and pricing
5. **Product Demo** - Screenshot placeholder + product status
6. **Competitive Analysis** - Feature comparison table
7. **Traction** - Milestones and key metrics
8. **Roadmap** - Short/mid/long-term phases
9. **Team** - Core team members with backgrounds
10. **Fundraising** - Target amount, equity, use of funds

### Design System

- **Dimensions**: Widescreen 16:9 (13.333 x 7.5 inches)
- **Default Colors**: Tech Blue (#1a73e8), Dark (#202124), Green Accent (#34a853)
- **Fonts**: Arial (fallback from Microsoft YaHei/Calibri)
- **Style**: Clean, minimal, professional VC-ready design

### Example

```bash
# Create example data
echo '{
    "project_name": "DevAI",
    "tagline": "AI Coding Assistant",
    "value_props": ["Fast", "Smart", "Private"],
    "language": "en"
}' > example.json

# Generate deck
python scripts/generate_pitch_deck.py --input example.json
# Output: DevAI_BP.pptx
```

## Dependencies

- Python 3.7+
- python-pptx >= 0.6.21

## License

MIT © UniqueClub
