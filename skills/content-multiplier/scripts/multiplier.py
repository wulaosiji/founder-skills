#!/usr/bin/env python3
"""
Content Multiplier by UniqueClub
Transform one piece of content into multiple platform-optimized formats.

Usage:
    python multiplier.py --input source.txt --platforms linkedin,twitter,wechat --output ./content/

Generates:
    - LinkedIn posts (150-300 words, professional tone)
    - Twitter/X threads (5-10 tweets)
    - WeChat articles (1000-2000 Chinese characters)
    - Xiaohongshu notes (300-500 characters, casual)
    - Newsletters (500-800 words)
    - Instagram captions
    - Video script outlines
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime


def read_source(filepath):
    """Read source content from file."""
    if not os.path.exists(filepath):
        print(f"Error: Source file not found: {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def extract_key_insights(text):
    """Extract key insights from source text."""
    # Simple extraction: first sentence as summary, bullet points as insights
    sentences = re.split(r'[.!?。！？]+', text)
    summary = sentences[0].strip() if sentences else text[:200]
    
    # Find bullet points or numbered lists
    insights = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith(('•', '-', '*', '1.', '2.', '3.', '4.', '5.')):
            insights.append(line.lstrip('•-*0123456789. '))
    
    # If no bullet points, use sentences
    if not insights:
        insights = [s.strip() for s in sentences[1:6] if len(s.strip()) > 20]
    
    return summary, insights[:5]


def generate_linkedin(content_type, summary, insights, audience, tone, topic):
    """Generate LinkedIn post."""
    hooks = {
        "blog": f"I spent weeks researching {topic}. Here's what I learned:",
        "video": f"After watching 100+ hours of {topic} content, here are the key insights:",
        "talk": f"Just gave a talk on {topic}. The #1 question I got was...",
        "product": f"We just shipped a major update to {topic}. Here's the story:",
        "default": f"Just learned something valuable about {topic}:"
    }
    
    hook = hooks.get(content_type, hooks["default"])
    
    body = f"{hook}\n\n"
    
    for i, insight in enumerate(insights[:3], 1):
        body += f"{i}. {insight}\n\n"
    
    ctas = [
        "What would you add? Let me know in the comments 👇",
        "Have you experienced this? Share your thoughts below.",
        "Which point resonates most with you?",
        "Agree or disagree? I'd love to hear your perspective."
    ]
    
    body += ctas[hash(topic) % len(ctas)]
    
    hashtags = " #".join([
        "startup", "founder", "entrepreneurship",
        topic.lower().replace(" ", ""), "growth", "insights"
    ])
    
    return f"{body}\n\n#{hashtags}"


def generate_twitter(content_type, summary, insights, audience, tone, topic):
    """Generate Twitter/X thread."""
    hook_templates = [
        f"🧵 {topic} in 8 tweets:\n\n(Bookmark this)",
        f"I studied {topic} for 100+ hours.\n\nHere are 8 things I learned:\n\n🧵",
        f"Most people get {topic} wrong.\n\nHere's the truth:\n\n🧵"
    ]
    
    hook = hook_templates[hash(topic) % len(hook_templates)]
    
    thread = [hook]
    
    for i, insight in enumerate(insights[:7], 1):
        tweet = f"{i}/ {insight}"
        if len(tweet) > 280:
            tweet = tweet[:277] + "..."
        thread.append(tweet)
    
    cta = f"{len(insights)+1}/ If you found this helpful:\n\n• Follow @{audience.lower().replace(' ', '_')} for more\n• RT the first tweet to share\n• Reply with your #1 takeaway"
    thread.append(cta)
    
    return "\n\n---\n\n".join(thread)


def generate_wechat(content_type, summary, insights, audience, tone, topic):
    """Generate WeChat article (Chinese)."""
    
    titles = [
        f"关于{topic}，我花了3个月时间总结出的核心观点",
        f"{topic}：90%的人都忽略了这一点",
        f"从{topic}中学到的5个重要认知"
    ]
    
    title = titles[hash(topic) % len(titles)]
    
    article = f"# {title}\n\n"
    article += f"**核心观点：{summary}**\n\n"
    article += "---\n\n"
    article += f"最近深入研究了{topic}，想和大家分享一些关键发现。\n\n"
    
    for i, insight in enumerate(insights, 1):
        article += f"## {i}. {insight[:30]}...\n\n"
        article += f"{insight}\n\n"
        article += "这一点对于" + audience + "来说尤其重要。\n\n"
    
    article += "---\n\n"
    article += "**总结**\n\n"
    article += f"{topic}是一个值得持续关注的领域。希望这篇文章对你有所启发。\n\n"
    article += "如果你有不同的看法，欢迎在评论区留言讨论。\n\n"
    article += "---\n\n"
    article += "*作者：创始人*\n"
    article += "*发表于：" + datetime.now().strftime("%Y年%m月%d日") + "*"
    
    return article


def generate_xiaohongshu(content_type, summary, insights, audience, tone, topic):
    """Generate Xiaohongshu note (Chinese, casual)."""
    
    title = f"🔥关于{topic}，我想说的几件事 | 创业日记"
    
    content = f"{title}\n\n"
    content += f"姐妹们，最近研究了{topic}，真的收获很多！\n\n"
    content += "💡 **核心发现：**\n"
    
    for insight in insights[:3]:
        content += f"✅ {insight[:40]}\n"
    
    content += "\n📝 **我的感受：**\n"
    content += f"作为一个{audience}，我觉得这个方向真的很有潜力。\n"
    content += "建议大家多关注这方面的信息！\n\n"
    
    content += "👇 **行动建议：**\n"
    content += "1. 多学习相关知识\n"
    content += "2. 关注行业动态\n"
    content += "3. 找到志同道合的伙伴\n\n"
    
    content += "#创业 #成长 #" + topic.replace(" ", "") + " #职场 #学习"
    
    return content


def generate_newsletter(content_type, summary, insights, audience, tone, topic):
    """Generate newsletter."""
    
    subjects = [
        f"This week: Deep dive into {topic}",
        f"5 insights on {topic} you shouldn't miss",
        f"The {topic} playbook"
    ]
    
    subject = subjects[hash(topic) % len(subjects)]
    
    newsletter = f"Subject: {subject}\n\n"
    newsletter += f"Preview: {summary}\n\n"
    newsletter += "---\n\n"
    newsletter += f"Hi there,\n\n"
    newsletter += f"This week I've been thinking a lot about {topic}.\n\n"
    newsletter += f"**The big idea:** {summary}\n\n"
    newsletter += "Here are the key insights:\n\n"
    
    for i, insight in enumerate(insights, 1):
        newsletter += f"**{i}.** {insight}\n\n"
    
    newsletter += "---\n\n"
    newsletter += "**Key Takeaways**\n\n"
    newsletter += "→ " + "\n→ ".join([i[:60] + "..." if len(i) > 60 else i for i in insights[:3]])
    newsletter += "\n\n"
    
    newsletter += "**What I'm reading**\n"
    newsletter += "• [Related resource #1]\n"
    newsletter += "• [Related resource #2]\n\n"
    
    newsletter += "Thanks for reading!\n"
    newsletter += "- The Founder\n\n"
    newsletter += "P.S. Reply to this email with your thoughts—I read every response."
    
    return newsletter


def generate_instagram(content_type, summary, insights, audience, tone, topic):
    """Generate Instagram caption."""
    
    caption = f"{summary}\n\n"
    caption += "Here's what I learned:\n\n"
    
    for i, insight in enumerate(insights[:3], 1):
        caption += f"{i}. {insight}\n"
    
    caption += "\nWhich one resonates with you? 👇\n\n"
    caption += "---\n\n"
    caption += "#" + " #".join([
        "startup", "founder", "business", "entrepreneur",
        topic.lower().replace(" ", ""), "success", "mindset"
    ])
    
    return caption


def generate_video_script(content_type, summary, insights, audience, tone, topic):
    """Generate video script outline."""
    
    script = f"# Video Script: {topic}\n\n"
    script += "**Duration:** 3-5 minutes\n\n"
    script += "**Target:** " + audience + "\n\n"
    script += "---\n\n"
    
    sections = [
        ("HOOK (0:00-0:05)", f"Most people get {topic} completely wrong. Here's what you actually need to know..."),
        ("PROBLEM SETUP (0:05-0:30)", f"The common misconception about {topic} is... But the reality is different."),
        ("MAIN CONTENT (0:30-2:30)", "\n".join([f"\nPoint {i+1}: {insight}\n[Visual: Show example/diagram]" for i, insight in enumerate(insights[:3])])),
        ("PROOF/EXAMPLE (2:30-3:30)", "Share a concrete example or case study that illustrates the main point."),
        ("CTA (3:30-4:00)", "If you found this helpful, follow for more. Comment with your biggest takeaway below!")
    ]
    
    for section, content in sections:
        script += f"### {section}\n{content}\n\n"
    
    script += "---\n\n"
    script += "**Visual Notes:**\n"
    script += "- Use B-roll of relevant footage\n"
    script += "- Add text overlays for key points\n"
    script += "- Include progress bar\n"
    script += "- End screen with subscribe CTA\n"
    
    return script


def generate_content(source_text, platforms, content_type, audience, tone, topic, output_dir):
    """Generate content for all requested platforms."""
    
    summary, insights = extract_key_insights(source_text)
    
    generators = {
        "linkedin": generate_linkedin,
        "twitter": generate_twitter,
        "wechat": generate_wechat,
        "xiaohongshu": generate_xiaohongshu,
        "newsletter": generate_newsletter,
        "instagram": generate_instagram,
        "video": generate_video_script
    }
    
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []
    
    for platform in platforms:
        platform = platform.strip().lower()
        if platform in generators:
            content = generators[platform](content_type, summary, insights, audience, tone, topic)
            
            filename = f"{topic.replace(' ', '_')}_{platform}.md"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated_files.append(filepath)
            print(f"  ✓ {platform}: {filepath}")
    
    return generated_files


def main():
    parser = argparse.ArgumentParser(description="Multiply content across platforms")
    parser.add_argument("--input", "-i", required=True, help="Source content file path")
    parser.add_argument("--platforms", "-p", required=True, 
                        help="Comma-separated list: linkedin,twitter,wechat,xiaohongshu,newsletter,instagram,video")
    parser.add_argument("--type", "-t", default="blog", 
                        choices=["blog", "video", "talk", "product", "default"],
                        help="Source content type")
    parser.add_argument("--audience", "-a", default="founders", help="Target audience")
    parser.add_argument("--tone", default="professional", help="Content tone")
    parser.add_argument("--topic", required=True, help="Content topic/title")
    parser.add_argument("--output", "-o", default="./generated_content", help="Output directory")
    args = parser.parse_args()
    
    source_text = read_source(args.input)
    platforms = [p.strip() for p in args.platforms.split(",")]
    
    print(f"🔄 Multiplying content for: {', '.join(platforms)}")
    
    files = generate_content(
        source_text, platforms, args.type, 
        args.audience, args.tone, args.topic, args.output
    )
    
    print(f"\n✅ Generated {len(files)} platform-optimized versions")
    print(f"   Output directory: {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
