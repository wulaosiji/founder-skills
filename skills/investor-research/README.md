# Investor Research

Research venture capital firms, angel investors, and funding sources for startup fundraising. Generates a structured markdown report with investor profiles, outreach strategy, and action items.

## Usage

### Quick Start

```bash
cd skills/investor-research
python scripts/research_investors.py --input config.json --output report.md
```

### Input JSON Format

```json
{
    "company_name": "DevAI",
    "stage": "Seed",
    "sector": "AI / Developer Tools",
    "target_amount": "$2M",
    "location": "San Francisco, USA",
    "investor_type": "VC + Angel",
    "scope": "Top 10",
    "language": "en",
    "investors": [
        {
            "name": "Accel",
            "type": "VC",
            "stage": "Seed - Series B",
            "check_size": "$1M - $5M",
            "focus": "SaaS, Developer Tools",
            "priority": "A",
            "location": "Palo Alto, CA",
            "fund_size": "$3B",
            "thesis": "Early-stage B2B software with strong product-market fit",
            "recent_investments": ["Linear", "Raycast", "Vercel"],
            "key_partners": ["Arun Mathew", "Ashu Garg"],
            "timeline": "4-6 weeks",
            "warm_intro": "Portfolio founder at Vercel",
            "fit": "Strong track record in developer tools",
            "angle": "Emphasize developer productivity metrics",
            "recent_signal": "Recently led a devtools Series A"
        },
        {
            "name": "Naval Ravikant",
            "type": "Angel",
            "stage": "Pre-seed - Seed",
            "check_size": "$100K - $500K",
            "focus": "AI, Crypto, SaaS",
            "priority": "S",
            "location": "Bay Area",
            "thesis": "Backing founders with unique insights",
            "recent_investments": ["Notion", "Clubhouse", "Opensea"],
            "warm_intro": "Twitter DM or mutual connection",
            "fit": "Aligns with AI-native tools thesis",
            "angle": "Focus on unique insight around code generation",
            "recent_signal": "Active on AI Twitter"
        }
    ]
}
```

### Command Line Options

```bash
python scripts/research_investors.py --help

# Required:
#   --input, -i   Path to JSON config file

# Optional:
#   --output, -o  Output markdown file path
```

### Report Structure

The generated markdown report includes:

1. **Executive Summary** - Overview of your fundraising context
2. **Investor Summary Table** - Quick-reference table of all investors
3. **Detailed Profiles (Top 10)** - In-depth analysis of priority investors
4. **Outreach Strategy** - Per-investor approach angles and warm intro paths
5. **Action Items** - Prioritized next steps checklist
6. **Appendix** - Additional investors and research notes

### Language Support

Set `"language": "zh"` for Chinese reports, `"en"` for English.

```bash
# English report (default)
python scripts/research_investors.py -i config_en.json

# Chinese report
python scripts/research_investors.py -i config_zh.json
```

### Without API Keys

This script works entirely offline using the data you provide in the JSON config. If you don't have Crunchbase API access:

1. Manually research investors on Crunchbase (free tier works)
2. Copy key data into the JSON config
3. Run the script to generate a beautifully formatted report

### Example

```bash
# Create minimal config
echo '{
    "company_name": "MyStartup",
    "stage": "Seed",
    "sector": "SaaS",
    "target_amount": "$1M",
    "language": "en",
    "investors": [
        {"name": "Sequoia", "type": "VC", "priority": "A", "check_size": "$1M-$10M"}
    ]
}' > config.json

# Generate report
python scripts/research_investors.py -i config.json
# Output: MyStartup_Investor_Research.md
```

## Dependencies

- Python 3.7+
- No external dependencies required

## License

MIT © UniqueClub
