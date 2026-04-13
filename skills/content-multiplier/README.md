# Content Multiplier

Transform one piece of content into multiple platform-optimized formats. Turn a blog post, video transcript, or idea into LinkedIn posts, Twitter threads, WeChat articles, and more.

## Usage

### Quick Start

```bash
cd skills/content-multiplier

# Generate LinkedIn and Twitter versions
python scripts/multiplier.py --input blog_post.txt --platforms linkedin,twitter --topic "AI Tools"

# Generate all platforms
python scripts/multiplier.py -i talk_transcript.txt -p linkedin,twitter,wechat,newsletter --topic "Startup Growth"
```

### Command Line Options

```bash
python scripts/multiplier.py --help

# Required:
#   --input, -i       Source content file path
#   --platforms, -p   Comma-separated platforms
#   --topic           Content topic/title

# Optional:
#   --type, -t        Source type: blog|video|talk|product (default: blog)
#   --audience, -a    Target audience (default: founders)
#   --tone            Content tone (default: professional)
#   --output, -o      Output directory (default: ./generated_content)
```

### Supported Platforms

| Platform | Output | Characteristics |
|----------|--------|-----------------|
| `linkedin` | `{topic}_linkedin.md` | 150-300 words, professional, hashtags, CTA |
| `twitter` | `{topic}_twitter.md` | 5-10 tweet thread, punchy, scannable |
| `wechat` | `{topic}_wechat.md` | 1000-2000 chars, article format, Chinese |
| `xiaohongshu` | `{topic}_xiaohongshu.md` | 300-500 chars, casual, emoji-heavy, Chinese |
| `newsletter` | `{topic}_newsletter.md` | 500-800 words, subject lines, personal |
| `instagram` | `{topic}_instagram.md` | <2200 chars, visual-focused, hashtags |
| `video` | `{topic}_video.md` | Scene-by-scene outline with timing |

### Example Workflow

```bash
# 1. Write your source content
cat > my_article.txt << 'EOF'
The future of AI in startups is not about replacing humans, but augmenting them.
Here are three key trends:
• AI as a co-pilot, not autopilot
• Vertical-specific AI solutions
• AI-native workflows from day one
EOF

# 2. Generate multiple versions
python scripts/multiplier.py \
  --input my_article.txt \
  --platforms linkedin,twitter,wechat,newsletter \
  --topic "AI Startups" \
  --audience "founders" \
  --type blog

# 3. Check output
ls generated_content/
# AI_Startups_linkedin.md
# AI_Startups_twitter.md
# AI_Startups_wechat.md
# AI_Startups_newsletter.md
```

### Output Examples

**LinkedIn Post:**
```markdown
I spent weeks researching AI Startups. Here's what I learned:

1. AI as a co-pilot, not autopilot

2. Vertical-specific AI solutions

3. AI-native workflows from day one

What would you add? Let me know in the comments 👇

#startup #founder #aistartups #growth
```

**Twitter Thread:**
```markdown
🧵 AI Startups in 8 tweets:

(Bookmark this)

---

1/ AI as a co-pilot, not autopilot

---

2/ Vertical-specific AI solutions

...
```

### Content Transformation Principles

1. **Platform-native formatting** - Each platform has distinct conventions
2. **Audience-aware tone** - Adjusts formality and jargon
3. **Value-first** - Every piece delivers standalone value
4. **Consistent core** - Same key message, different packaging

### Tips for Best Results

1. **Source content** should be clear and structured
2. **Topic** should be specific (e.g., "B2B SaaS Pricing" not just "Business")
3. **Audience** helps tailor tone and examples
4. Review and customize generated content before publishing

## Dependencies

- Python 3.7+
- No external dependencies

## License

MIT © UniqueClub
