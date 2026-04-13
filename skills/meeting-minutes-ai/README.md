# Meeting Minutes AI

Extract action items, decisions, and key insights from meeting transcripts or recordings. Transforms raw meeting content into structured, shareable minutes with owners and deadlines.

## Usage

### Quick Start

```bash
cd skills/meeting-minutes-ai

# Standard format (default)
python scripts/extract_minutes.py --input transcript.txt --title "Product Review"

# Concise format (just decisions + actions)
python scripts/extract_minutes.py -i transcript.txt -t "Q4 Planning" -f concise

# Detailed format with discussion topics
python scripts/extract_minutes.py -i transcript.txt -t "Board Meeting" -f detailed \
  --date 2024-01-15 --attendees "Alice, Bob, Charlie" --duration "90 min"
```

### Command Line Options

```bash
python scripts/extract_minutes.py --help

# Required:
#   --input, -i       Transcript file path

# Optional:
#   --output, -o      Output markdown file path
#   --title, -t       Meeting title
#   --date, -d        Meeting date (YYYY-MM-DD)
#   --attendees, -a   Comma-separated attendee list
#   --duration        Meeting duration
#   --format, -f      Output format: concise|standard|detailed (default: standard)
#   --lang, -l        Language: en|zh (default: en)
```

### Output Formats

| Format | Sections Included | Best For |
|--------|-------------------|----------|
| `concise` | Header + Decisions + Actions + Quick Share | Slack/email |
| `standard` | Full structure, 2-3 pages | Team documentation |
| `detailed` | Full structure + discussion topics | Board meetings, retrospectives |

### Generated Sections

1. **Header** - Title, date, duration
2. **Attendees** - Participant list
3. **Objective** - Meeting purpose
4. **Summary** - High-level overview
5. **Decisions Made** - Numbered list of explicit agreements
6. **Open Questions** - Unresolved items
7. **Discussion Topics** *(detailed only)* - Topic-by-topic breakdown
8. **Action Items** - Table with owner, due date, priority
9. **Risks & Blockers** - Mentioned obstacles
10. **Next Steps** - Follow-up actions
11. **Quick Share Version** - Copy-paste friendly summary

### Example Transcript

```text
Alice: Let's start the Q4 planning meeting. Our goal is to finalize the product roadmap.
Bob: I think we should prioritize the mobile app redesign. Our user feedback shows it's critical.
Alice: Agreed. Let's decide to move the redesign to Q4 priority #1.
Charlie: I'll need 2 weeks to prepare the design system for this.
Alice: Great, can you have that ready by October 15?
Charlie: Yes, I'll deliver the design system by October 15.
Bob: We also decided to postpone the API v2 launch to Q1 next year.
Alice: Right. And I need someone to update the stakeholders by Friday.
Bob: I'll take that action item and send the update on Friday.
```

### Example Output

**Decisions:**
```markdown
✅ DECISIONS MADE (2)
1. Move mobile app redesign to Q4 priority #1
2. Postpone API v2 launch to Q1 next year
```

**Action Items:**
```markdown
⚡ ACTION ITEMS

| # | Action | Owner | Due Date | Priority | Status |
|---|--------|-------|----------|----------|--------|
| 1 | Deliver design system | Charlie | October 15 | High | Open |
| 2 | Send stakeholder update | Bob | Friday | High | Open |
```

### Language Support

**English (default):**
```bash
python scripts/extract_minutes.py -i meeting.txt -l en
```

**Chinese:**
```bash
python scripts/extract_minutes.py -i meeting.txt -l zh
```

### Tips for Best Results

1. **Clean transcripts** work best (remove timestamps if possible)
2. **Explicit decision language** helps detection: "We decided...", "Let's go with...", "Agreed"
3. **Name action owners clearly**: "Bob will...", "Alice is responsible for..."
4. **Mention deadlines explicitly** for better extraction
5. Review extracted items and fill in `[TBD]` placeholders

## Dependencies

- Python 3.7+
- No external dependencies

## License

MIT © UniqueClub
