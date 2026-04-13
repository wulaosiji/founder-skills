#!/usr/bin/env python3
"""
Meeting Minutes AI by UniqueClub
Extract action items, decisions, and key insights from meeting transcripts.

Usage:
    python extract_minutes.py --input meeting_transcript.txt --output minutes.md
    python extract_minutes.py -i transcript.txt --title "Q4 Planning" --date 2024-01-15 --format standard

Supports three output formats: concise, standard, detailed
"""

import argparse
import os
import re
import sys
from datetime import datetime


def read_transcript(filepath):
    """Read meeting transcript from file."""
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def extract_decisions(text):
    """Extract decisions from transcript."""
    decision_patterns = [
        r'(?:我们决定|决定| agreed|decided|let\'s go with|we will|we agree)\s*[：:：]\s*([^\n。]+)',
        r'(?:通过|批准|approved|confirmed)\s*([^\n。]{10,200})',
        r'(?:最终选择|选定|chose|selected)\s*([^\n。]{10,200})',
        r'(?:结论|conclusion)\s*[：:]\s*([^\n。]+)'
    ]
    
    decisions = []
    for pattern in decision_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            clean = match.strip()
            if len(clean) > 10 and clean not in decisions:
                decisions.append(clean)
    
    # If no explicit decisions found, look for strong agreement statements
    if not decisions:
        agreement_patterns = [
            r'(?:好的|可以|没问题|yes|sounds good|makes sense)\s*[，,]\s*([^\n。]{15,200})',
        ]
        for pattern in agreement_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches[:3]:
                clean = match.strip()
                if len(clean) > 15 and clean not in decisions:
                    decisions.append(clean)
    
    return decisions[:8]


def extract_action_items(text):
    """Extract action items from transcript."""
    action_patterns = [
        r'(?:负责|由[^\n，。]{1,20})([^\n，。]{10,100})(?:在|by|before|之前)([^\n，。]{1,30})',
        r'(?:待办|todo|action item|task)\s*[：:]\s*([^\n]+)',
        r'(?:\b[A-Z][a-z]+\b)\s+(?:will|需要|负责|去)\s+([^\n。]{10,150})',
    ]
    
    actions = []
    for pattern in action_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                combined = " ".join(m.strip() for m in match if m.strip())
            else:
                combined = match.strip()
            if len(combined) > 10 and combined not in actions:
                actions.append(combined)
    
    # Fallback: look for task-like sentences
    if not actions:
        task_sentences = re.findall(r'[^\n。]*(?:完成|准备|整理|提交|发送|review|check|follow up|跟进)[^\n。]*', text, re.IGNORECASE)
        for sentence in task_sentences[:8]:
            clean = sentence.strip()
            if len(clean) > 15 and clean not in actions:
                actions.append(clean)
    
    return actions[:10]


def extract_topics(text):
    """Extract discussion topics."""
    # Split by obvious topic indicators or numbered lists
    lines = text.split('\n')
    topics = []
    current_topic = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if line looks like a topic header
        if (line.startswith(('议题', 'Topic', '##', '###', '讨论', '关于')) or
            re.match(r'^\d+[\.、]\s*[^：:]+[：:]', line) or
            (len(line) < 40 and ('：' in line or ':' in line))):
            if current_topic:
                topics.append(current_topic)
            current_topic = {"name": re.sub(r'^\d+[\.、]\s*', '', line).split('：')[0].split(':')[0].strip(), 
                             "points": []}
        elif current_topic:
            current_topic["points"].append(line)
    
    if current_topic:
        topics.append(current_topic)
    
    # If no structured topics, chunk by paragraphs
    if not topics:
        paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 20]
        for i, para in enumerate(paragraphs[:5]):
            first_sentence = para.split('.')[0].split('。')[0][:40]
            topics.append({
                "name": first_sentence or f"Discussion {i+1}",
                "points": [para[:200]]
            })
    
    return topics[:6]


def generate_minutes(transcript, title, date, attendees, duration, format_type, lang):
    """Generate meeting minutes in requested format."""
    
    decisions = extract_decisions(transcript)
    actions = extract_action_items(transcript)
    topics = extract_topics(transcript)
    
    date_str = date or datetime.now().strftime("%Y-%m-%d")
    duration_str = duration or "[TBD]"
    
    if lang == "zh":
        minutes = f"""═══════════════════════════════════════
    会议纪要
    {title or "未命名会议"}
    日期: {date_str}
    时长: {duration_str}
═══════════════════════════════════════

👥 参会人员

{chr(10).join(['• ' + a for a in attendees]) if attendees else '• [待补充]'}

🎯 会议目标
{title or "请补充会议目标"}

⏱️ 时长
{duration_str}

"""
        
        if format_type != "concise":
            minutes += f"""═══════════════════════════════════════
📝 会议摘要

[请根据以下内容进行总结]

✅ 已做决策 ({len(decisions)})
"""
        else:
            minutes += f"""✅ 已做决策 ({len(decisions)})
"""
        
        for i, d in enumerate(decisions, 1):
            minutes += f"{i}. {d}\n"
        if not decisions:
            minutes += "[未检测到明确决策]\n"
        
        minutes += "\n❓ 待解决问题\n"
        minutes += "[待补充]\n"
        
        if format_type == "detailed":
            minutes += "\n═══════════════════════════════════════\n📋 讨论议题\n\n"
            for topic in topics:
                minutes += f"议题: {topic['name']}\n─────────────────────\n"
                minutes += "要点:\n"
                for point in topic['points'][:4]:
                    minutes += f"• {point[:150]}\n"
                minutes += "\n"
        
        minutes += "\n═══════════════════════════════════════\n⚡ 行动项\n\n"
        minutes += "| # | 行动项 | 负责人 | 截止日期 | 优先级 | 状态 |\n"
        minutes += "|---|--------|--------|----------|--------|--------|\n"
        
        for i, action in enumerate(actions, 1):
            owner = "[待分配]"
            due = "[待确认]"
            priority = "高" if i <= 2 else "中"
            # Try to extract owner/deadline from action text
            owner_match = re.search(r'由([^\s]{1,20})', action)
            if owner_match:
                owner = owner_match.group(1)
            due_match = re.search(r'(\d{4}-\d{2}-\d{2}|\d{1,2}月\d{1,2}日|下周|明天)', action)
            if due_match:
                due = due_match.group(1)
            minutes += f"| {i} | {action[:50]} | {owner} | {due} | {priority} | 待办 |\n"
        
        if not actions:
            minutes += "| 1 | [未检测到明确行动项] | [待分配] | [待确认] | 中 | 待办 |\n"
        
        if format_type != "concise":
            minutes += "\n🚧 风险与阻碍\n\n"
            minutes += "• [待补充]\n"
            minutes += "\n═══════════════════════════════════════\n📅 后续安排\n\n"
            minutes += "1. [待补充下一步行动]\n"
            minutes += "2. [确认下次会议时间]\n"
        
        minutes += "\n═══════════════════════════════════════\n"
        minutes += "快速分享版 (可直接复制到 Slack/微信):\n"
        minutes += "────────────────────────────────────\n"
        minutes += f"🎯 会议: {title or '未命名'}\n"
        minutes += f"✅ 决策: {len(decisions)} 项\n"
        minutes += f"⚡ 行动项: {len(actions)} 项\n"
        for i, a in enumerate(actions[:5], 1):
            minutes += f"   {i}. {a[:60]}\n"
        minutes += "────────────────────────────────────\n"
    
    else:  # English
        minutes = f"""═══════════════════════════════════════
    MEETING MINUTES
    {title or "Untitled Meeting"}
    Date: {date_str}
    Duration: {duration_str}
═══════════════════════════════════════

👥 ATTENDEES

{chr(10).join(['• ' + a for a in attendees]) if attendees else '• [TBD]'}

🎯 OBJECTIVE
{title or "Meeting objective to be added"}

⏱️ DURATION
{duration_str}

"""
        
        if format_type != "concise":
            minutes += f"""═══════════════════════════════════════
📝 SUMMARY

[Summary to be added based on content below]

✅ DECISIONS MADE ({len(decisions)})
"""
        else:
            minutes += f"""✅ DECISIONS MADE ({len(decisions)})
"""
        
        for i, d in enumerate(decisions, 1):
            minutes += f"{i}. {d}\n"
        if not decisions:
            minutes += "[No explicit decisions detected]\n"
        
        minutes += "\n❓ OPEN QUESTIONS\n"
        minutes += "[TBD]\n"
        
        if format_type == "detailed":
            minutes += "\n═══════════════════════════════════════\n📋 DISCUSSION TOPICS\n\n"
            for topic in topics:
                minutes += f"Topic: {topic['name']}\n─────────────────────\n"
                minutes += "Key Points:\n"
                for point in topic['points'][:4]:
                    minutes += f"• {point[:150]}\n"
                minutes += "\n"
        
        minutes += "\n═══════════════════════════════════════\n⚡ ACTION ITEMS\n\n"
        minutes += "| # | Action | Owner | Due Date | Priority | Status |\n"
        minutes += "|---|--------|-------|----------|----------|--------|\n"
        
        for i, action in enumerate(actions, 1):
            owner = "[TBD]"
            due = "[TBD]"
            priority = "High" if i <= 2 else "Medium"
            owner_match = re.search(r'\b([A-Z][a-zA-Z\s]{2,20})\b', action)
            if owner_match:
                owner = owner_match.group(1).strip()[:15]
            due_match = re.search(r'(\d{4}-\d{2}-\d{2}|next week|tomorrow|by\s+\w+)', action, re.IGNORECASE)
            if due_match:
                due = due_match.group(1)
            minutes += f"| {i} | {action[:50]} | {owner} | {due} | {priority} | Open |\n"
        
        if not actions:
            minutes += "| 1 | [No explicit action items detected] | [TBD] | [TBD] | Medium | Open |\n"
        
        if format_type != "concise":
            minutes += "\n🚧 RISKS & BLOCKERS\n\n"
            minutes += "• [TBD]\n"
            minutes += "\n═══════════════════════════════════════\n📅 NEXT STEPS\n\n"
            minutes += "1. [Next steps to be added]\n"
            minutes += "2. [Confirm follow-up meeting time]\n"
        
        minutes += "\n═══════════════════════════════════════\n"
        minutes += "QUICK SHARE VERSION (copy to Slack/email):\n"
        minutes += "────────────────────────────────────\n"
        minutes += f"🎯 Meeting: {title or 'Untitled'}\n"
        minutes += f"✅ Decisions: {len(decisions)}\n"
        minutes += f"⚡ Action Items: {len(actions)}\n"
        for i, a in enumerate(actions[:5], 1):
            minutes += f"   {i}. {a[:60]}\n"
        minutes += "────────────────────────────────────\n"
    
    return minutes


def main():
    parser = argparse.ArgumentParser(description="Extract meeting minutes from transcript")
    parser.add_argument("--input", "-i", required=True, help="Meeting transcript file path")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    parser.add_argument("--title", "-t", help="Meeting title")
    parser.add_argument("--date", "-d", help="Meeting date (YYYY-MM-DD)")
    parser.add_argument("--attendees", "-a", help="Comma-separated attendee list")
    parser.add_argument("--duration", help="Meeting duration")
    parser.add_argument("--format", "-f", default="standard", 
                        choices=["concise", "standard", "detailed"],
                        help="Output format")
    parser.add_argument("--lang", "-l", default="en", choices=["en", "zh"],
                        help="Language")
    args = parser.parse_args()
    
    transcript = read_transcript(args.input)
    attendees = [a.strip() for a in args.attendees.split(",")] if args.attendees else []
    
    minutes = generate_minutes(
        transcript, args.title, args.date, attendees, 
        args.duration, args.format, args.lang
    )
    
    if args.output:
        output_file = args.output
    else:
        safe_title = (args.title or "Meeting").replace(" ", "_")
        date_str = args.date or datetime.now().strftime("%Y-%m-%d")
        output_file = f"{safe_title}_Minutes_{date_str}.md"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(minutes)
    
    print(f"✅ Meeting minutes generated: {os.path.abspath(output_file)}")
    print(f"   Format: {args.format} | Language: {args.lang}")
    print(f"   Decisions detected: {len(extract_decisions(transcript))}")
    print(f"   Action items detected: {len(extract_action_items(transcript))}")


if __name__ == "__main__":
    main()
