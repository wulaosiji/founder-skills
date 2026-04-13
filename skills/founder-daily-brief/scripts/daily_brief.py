#!/usr/bin/env python3
"""
Founder Daily Brief by UniqueClub
Generate a personalized daily briefing for startup founders.

Usage:
    python daily_brief.py --input config.json --output brief.md

Compiles tasks, meetings, industry news, and personal priorities into a structured daily brief.
"""

import argparse
import json
import os
import random
import sys
from datetime import datetime


def load_config(filepath):
    """Load daily brief config from JSON."""
    if not os.path.exists(filepath):
        print(f"Error: Config file not found: {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_focus_tip(stage, lang):
    """Get a contextual focus tip based on company stage."""
    tips_zh = {
        "early": [
            "今天最重要的事：找到并验证一个真正的用户痛点。",
            "优先和客户对话，而不是写代码。",
            "早期阶段，速度比完美更重要。"
        ],
        "growth": [
            "关注可复制的增长杠杆，而不是一次性技巧。",
            "今天抽时间和团队对齐关键指标。",
            "成长期最重要的是招聘和保留核心人才。"
        ],
        "expansion": [
            "审视运营效率，确保扩张是有质量的。",
            "考虑哪些流程可以标准化和自动化。",
            "成熟期需要更强的财务纪律和战略耐心。"
        ]
    }
    
    tips_en = {
        "early": [
            "Your #1 job today: validate a real user pain point.",
            "Talk to customers before writing more code.",
            "At this stage, speed beats perfection."
        ],
        "growth": [
            "Focus on repeatable growth levers, not one-off hacks.",
            "Align your team around the key metrics today.",
            "Your most important task: hire and retain great people."
        ],
        "expansion": [
            "Review operational efficiency. Ensure growth is quality growth.",
            "Identify processes that can be standardized and automated.",
            "At this stage, financial discipline and strategic patience matter most."
        ]
    }
    
    tips = tips_zh if lang == "zh" else tips_en
    stage_key = stage.lower() if stage.lower() in tips else "early"
    return random.choice(tips[stage_key])


def generate_brief(data, output_file):
    """Generate the daily brief markdown."""
    
    company = data.get("company_name", "Your Startup")
    stage = data.get("stage", "early")
    lang = data.get("language", "en")
    date_str = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    day_name = datetime.strptime(date_str, "%Y-%m-%d").strftime("%A")
    
    schedule = data.get("schedule", [])
    tasks = data.get("tasks", [])
    news = data.get("news", [])
    competitors = data.get("competitors", [])
    metrics = data.get("metrics", {})
    
    priorities = data.get("priorities", tasks[:3] if tasks else [])
    
    focus_tip = get_focus_tip(stage, lang)
    
    if lang == "zh":
        brief = f"""═══════════════════════════════════════
    FOUNDER DAILY BRIEF
    {date_str} | {day_name}
    {company}
═══════════════════════════════════════

🎯 今日 TOP 3 优先事项

"""
        for i, p in enumerate(priorities[:3], 1):
            reason = ""
            if isinstance(p, dict):
                reason = f" — {p.get('reason', '')}" if p.get('reason') else ""
                p = p.get("task", f"优先事项 {i}")
            brief += f"{i}. {p}{reason}\n"
        
        brief += f"\n💡 专注建议：{focus_tip}\n\n"
        
        brief += "📅 今日日程\n\n"
        if schedule:
            for item in schedule:
                time_str = item.get("time", "")
                event = item.get("event", "")
                prep = item.get("prep", "")
                goal = item.get("goal", "")
                brief += f"{time_str} — {event}\n"
                if prep:
                    brief += f"  └─ 准备：{prep}\n"
                if goal:
                    brief += f"  └─ 目标：{goal}\n"
                brief += "\n"
        else:
            brief += "[今日暂无日程安排]\n\n"
        
        brief += "✅ 行动项\n\n"
        brief += "🔴 高优先级（今日必做）\n"
        high = [t for t in tasks if t.get("priority") == "high"]
        for t in high[:5]:
            brief += f"- [ ] {t.get('task', '')}{' — ' + t.get('deadline', '') if t.get('deadline') else ''}\n"
        if not high:
            brief += "- [ ] [待补充高优先级任务]\n"
        
        brief += "\n🟡 中优先级（本周完成）\n"
        med = [t for t in tasks if t.get("priority") == "medium"]
        for t in med[:5]:
            brief += f"- [ ] {t.get('task', '')}\n"
        if not med:
            brief += "- [ ] [待补充中优先级任务]\n"
        
        brief += "\n🟢 低优先级 / 待办池\n"
        low = [t for t in tasks if t.get("priority") == "low"]
        for t in low[:3]:
            brief += f"- [ ] {t.get('task', '')}\n"
        if not low:
            brief += "- [ ] [待补充低优先级任务]\n"
        
        brief += "\n"
        
        if news:
            brief += "📰 行业动态\n\n"
            for item in news[:5]:
                brief += f"• {item.get('headline', '')} — {item.get('summary', '')} ({item.get('source', '')})\n"
            brief += "\n💡 洞察：[请根据以上动态补充对业务的启示]\n\n"
        
        if competitors:
            brief += "👁️ 竞品动态\n\n"
            for c in competitors[:3]:
                brief += f"{c.get('name', '竞品')}:\n"
                brief += f"• 动态类型：{c.get('update_type', '')}\n"
                brief += f"• 详情：{c.get('description', '')}\n"
                brief += f"• 对我们的影响：{c.get('implication', '[待分析]')}\n\n"
        
        quotes_zh = [
            ("Paul Graham", "Build something people want.", "所有伟大的公司都始于解决一个真实的问题。"),
            ("Reid Hoffman", "If you are not embarrassed by the first version of your product, you've launched too late.", "早期阶段，完美主义是敌人。"),
            ("Sam Altman", "The way to build something great is to focus on the long term.", "创始人需要长期视角和短期执行力的平衡。")
        ]
        quote = random.choice(quotes_zh)
        brief += f"""🧠 创始人思维

Quote: "{quote[1]}" — {quote[0]}
Context: {quote[2]}
Action: 把这句话应用到今天的决策中。

"""
        
        brief += "📊 关键指标\n\n"
        brief += f"□ 收入: {metrics.get('revenue', '___')} (目标: {metrics.get('revenue_goal', '___')})\n"
        brief += f"□ 活跃用户: {metrics.get('active_users', '___')} (增长: {metrics.get('growth', '___')}%)\n"
        brief += f"□ 新注册: {metrics.get('new_signups', '___')}\n"
        brief += f"□ 流失率: {metrics.get('churn', '___')}\n\n"
        
        brief += "═══════════════════════════════════════\n"
        brief += "快速扫描版:\n"
        brief += "────────────────────────────────────\n"
        top_priority = priorities[0] if priorities else "[待确认]"
        if isinstance(top_priority, dict):
            top_priority = top_priority.get("task", "[待确认]")
        key_meeting = schedule[0].get("event", "无") if schedule else "无"
        urgent = high[0].get("task", "[待确认]") if high else "[待确认]"
        key_news = news[0].get("headline", "无重大新闻") if news else "无重大新闻"
        brief += f"🎯 最高优先级: {top_priority}\n"
        brief += f"📅 重要会议: {key_meeting}\n"
        brief += f"⚠️ 需立即处理: {urgent}\n"
        brief += f"📰 关键动态: {key_news}\n"
        brief += "────────────────────────────────────\n"
        brief += "\nGenerated by Founder Daily Brief\n"
        brief += "Part of UniqueClub Founder Toolkit\n"
        brief += "🌐 https://uniqueclub.ai\n"
        brief += "═══════════════════════════════════════\n"
    
    else:  # English
        brief = f"""═══════════════════════════════════════
    FOUNDER DAILY BRIEF
    {date_str} | {day_name}
    {company}
═══════════════════════════════════════

🎯 TODAY'S TOP 3

"""
        for i, p in enumerate(priorities[:3], 1):
            reason = ""
            if isinstance(p, dict):
                reason = f" — {p.get('reason', '')}" if p.get('reason') else ""
                p = p.get("task", f"Priority {i}")
            brief += f"{i}. {p}{reason}\n"
        
        brief += f"\n💡 Focus Tip: {focus_tip}\n\n"
        
        brief += "📅 TODAY'S SCHEDULE\n\n"
        if schedule:
            for item in schedule:
                time_str = item.get("time", "")
                event = item.get("event", "")
                prep = item.get("prep", "")
                goal = item.get("goal", "")
                brief += f"{time_str} — {event}\n"
                if prep:
                    brief += f"  └─ Prep: {prep}\n"
                if goal:
                    brief += f"  └─ Goal: {goal}\n"
                brief += "\n"
        else:
            brief += "[No meetings scheduled today]\n\n"
        
        brief += "✅ ACTION ITEMS\n\n"
        brief += "🔴 High Priority (Do Today)\n"
        high = [t for t in tasks if t.get("priority") == "high"]
        for t in high[:5]:
            brief += f"- [ ] {t.get('task', '')}{' — ' + t.get('deadline', '') if t.get('deadline') else ''}\n"
        if not high:
            brief += "- [ ] [Add high-priority tasks]\n"
        
        brief += "\n🟡 Medium Priority (This Week)\n"
        med = [t for t in tasks if t.get("priority") == "medium"]
        for t in med[:5]:
            brief += f"- [ ] {t.get('task', '')}\n"
        if not med:
            brief += "- [ ] [Add medium-priority tasks]\n"
        
        brief += "\n🟢 Low Priority / Backlog\n"
        low = [t for t in tasks if t.get("priority") == "low"]
        for t in low[:3]:
            brief += f"- [ ] {t.get('task', '')}\n"
        if not low:
            brief += "- [ ] [Add low-priority tasks]\n"
        
        brief += "\n"
        
        if news:
            brief += "📰 INDUSTRY UPDATES\n\n"
            for item in news[:5]:
                brief += f"• {item.get('headline', '')} — {item.get('summary', '')} ({item.get('source', '')})\n"
            brief += "\n💡 Insight: [Add your analysis based on the above news]\n\n"
        
        if competitors:
            brief += "👁️ COMPETITOR TRACKER\n\n"
            for c in competitors[:3]:
                brief += f"{c.get('name', 'Competitor')}:\n"
                brief += f"• Update: {c.get('update_type', '')}\n"
                brief += f"• Details: {c.get('description', '')}\n"
                brief += f"• Implication: {c.get('implication', '[To analyze]')}\n\n"
        
        quotes_en = [
            ("Paul Graham", "Build something people want.", "All great companies start by solving a real problem."),
            ("Reid Hoffman", "If you are not embarrassed by the first version of your product, you've launched too late.", "In the early days, perfectionism is the enemy."),
            ("Sam Altman", "The way to build something great is to focus on the long term.", "Founders need a balance of long-term vision and short-term execution.")
        ]
        quote = random.choice(quotes_en)
        brief += f"""🧠 FOUNDER MINDSET

Quote: "{quote[1]}" — {quote[0]}
Context: {quote[2]}
Action: Apply this to today's decisions.

"""
        
        brief += "📊 KEY METRICS\n\n"
        brief += f"□ Revenue: {metrics.get('revenue', '___')} (Goal: {metrics.get('revenue_goal', '___')})\n"
        brief += f"□ Active Users: {metrics.get('active_users', '___')} (Growth: {metrics.get('growth', '___')}%)\n"
        brief += f"□ New Signups: {metrics.get('new_signups', '___')}\n"
        brief += f"□ Churn Rate: {metrics.get('churn', '___')}\n\n"
        
        brief += "═══════════════════════════════════════\n"
        brief += "QUICK SCAN VERSION:\n"
        brief += "────────────────────────────────────\n"
        top_priority = priorities[0] if priorities else "[TBD]"
        if isinstance(top_priority, dict):
            top_priority = top_priority.get("task", "[TBD]")
        key_meeting = schedule[0].get("event", "None") if schedule else "None"
        urgent = high[0].get("task", "[TBD]") if high else "[TBD]"
        key_news = news[0].get("headline", "No major news") if news else "No major news"
        brief += f"🎯 Top Priority: {top_priority}\n"
        brief += f"📅 Key Meeting: {key_meeting}\n"
        brief += f"⚠️ Action Needed: {urgent}\n"
        brief += f"📰 Key News: {key_news}\n"
        brief += "────────────────────────────────────\n"
        brief += "\nGenerated by Founder Daily Brief\n"
        brief += "Part of UniqueClub Founder Toolkit\n"
        brief += "🌐 https://uniqueclub.ai\n"
        brief += "═══════════════════════════════════════\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(brief)
    
    print(f"✅ Daily brief generated: {os.path.abspath(output_file)}")
    print(f"   Company: {company} | Date: {date_str} | Language: {lang}")


def main():
    parser = argparse.ArgumentParser(description="Generate founder daily brief")
    parser.add_argument("--input", "-i", required=True, help="Path to JSON config file")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    args = parser.parse_args()
    
    data = load_config(args.input)
    
    if args.output:
        output_file = args.output
    else:
        date_str = data.get("date", datetime.now().strftime("%Y-%m-%d"))
        output_file = f"Founder_Brief_{date_str}.md"
    
    generate_brief(data, output_file)


if __name__ == "__main__":
    main()
