#!/usr/bin/env python3
"""
Investor Research Report Generator by UniqueClub
Generates a structured markdown report for investor research.

Usage:
    python research_investors.py --input config.json --output investor_report.md

Features:
    - Loads startup profile and preferences from JSON
    - Generates structured report with investor profiles, outreach strategy, and action items
    - Includes web search integration hooks (template-based when no API key available)
    - Produces markdown ready for sharing or printing
"""

import argparse
import json
import os
import sys
from datetime import datetime


def load_json(filepath):
    """Load and validate JSON input."""
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_report(data, output_file):
    """Generate the investor research markdown report."""
    
    company = data.get("company_name", "Your Startup")
    stage = data.get("stage", "Seed")
    sector = data.get("sector", "Technology")
    amount = data.get("target_amount", "TBD")
    location = data.get("location", "TBD")
    investor_type = data.get("investor_type", "Both")
    scope = data.get("scope", "Top 10")
    lang = data.get("language", "en")
    
    investors = data.get("investors", [])
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    if lang == "zh":
        report = f"""# {company} 投资人研究报告

> 生成日期：{date_str}  
> 融资阶段：{stage}  
> 目标金额：{amount}  
> 行业领域：{sector}  
> 研究范围：{scope}

---

## 一、执行摘要

本报告为 **{company}** 的融资准备提供投资人研究与策略建议。公司目前处于 **{stage}** 阶段，专注 **{sector}** 领域，目标融资金额为 **{amount}**。根据行业匹配度、投资阶段偏好及地理位置，本报告筛选出最值得关注的投资机构与个人天使投资人。

---

## 二、投资人总览表

| 投资人 | 类型 | 阶段 | 单笔投资额 | 关注领域 | 优先级 |
|--------|------|------|-----------|----------|--------|
"""
    else:
        report = f"""# {company} Investor Research Report

> Generated: {date_str}  
> Stage: {stage}  
> Target Raise: {amount}  
> Sector: {sector}  
> Scope: {scope}

---

## 1. Executive Summary

This report provides investor research and outreach strategy for **{company}**. The company is currently at **{stage}** stage, focused on **{sector}**, targeting **{amount}** in funding. Based on sector fit, stage preference, and geography, the following investors are prioritized.

---

## 2. Investor Summary Table

| Investor | Type | Stage | Check Size | Focus | Priority |
|----------|------|-------|------------|-------|----------|
"""
    
    # Add investors to summary table
    for inv in investors[:20]:
        name = inv.get("name", "Unknown")
        inv_type = inv.get("type", investor_type)
        inv_stage = inv.get("stage", stage)
        check = inv.get("check_size", "[待确认]" if lang == "zh" else "[TBD]")
        focus = inv.get("focus", sector)
        priority = inv.get("priority", "B")
        report += f"| {name} | {inv_type} | {inv_stage} | {check} | {focus} | {priority} |\n"
    
    if not investors:
        placeholder_name = "[待补充]" if lang == "zh" else "[To be added]"
        report += f"| {placeholder_name} | {investor_type} | {stage} | [TBD] | {sector} | A |\n"
    
    if lang == "zh":
        report += "\n---\n\n## 三、重点投资人详细画像\n\n"
    else:
        report += "\n---\n\n## 3. Detailed Investor Profiles (Top 10)\n\n"
    
    # Detailed profiles for top-priority investors
    top_investors = [inv for inv in investors if inv.get("priority") in ["A", "S"]][:10]
    if not top_investors and investors:
        top_investors = investors[:10]
    
    for inv in top_investors:
        name = inv.get("name", "Unknown")
        inv_type = inv.get("type", "VC")
        inv_location = inv.get("location", "[待确认]")
        fund_size = inv.get("fund_size", "[待确认]")
        check_size = inv.get("check_size", "[待确认]")
        preferred_stages = inv.get("stage", stage)
        thesis = inv.get("thesis", "[待补充]")
        recent = inv.get("recent_investments", [])
        partners = inv.get("key_partners", [])
        timeline = inv.get("timeline", "[待确认]")
        warm_intro = inv.get("warm_intro", "[待补充]")
        
        if lang == "zh":
            report += f"""### {name}

- **类型**：{inv_type}
- **所在地**：{inv_location}
- **基金规模**：{fund_size}
- **典型投资金额**：{check_size}
- **偏好阶段**：{preferred_stages}
- **投资理念**：{thesis}
- **近期投资案例**：{', '.join(recent) if recent else '[待补充]'}
- **核心合伙人**：{', '.join(partners) if partners else '[待补充]'}
- **决策周期**：{timeline}
- **暖介绍路径**：{warm_intro}

"""
        else:
            report += f"""### {name}

- **Type**: {inv_type}
- **Location**: {inv_location}
- **Fund Size**: {fund_size}
- **Typical Check Size**: {check_size}
- **Preferred Stages**: {preferred_stages}
- **Investment Thesis**: {thesis}
- **Recent Investments**: {', '.join(recent) if recent else '[TBD]'}
- **Key Partners**: {', '.join(partners) if partners else '[TBD]'}
- **Decision Timeline**: {timeline}
- **Warm Intro Path**: {warm_intro}

"""
    
    if not top_investors:
        placeholder = "[待补充投资人详细信息。请使用Crunchbase、LinkedIn、机构官网等渠道进行补充。]" if lang == "zh" else "[Detailed investor profiles to be added. Use Crunchbase, LinkedIn, and firm websites to research.]"
        report += f"{placeholder}\n\n"
    
    # Outreach Strategy
    if lang == "zh":
        report += "---\n\n## 四、 outreach 策略\n\n"
        for inv in top_investors:
            name = inv.get("name", "Unknown")
            fit = inv.get("fit", "[待补充]")
            angle = inv.get("angle", "[待补充]")
            warm = inv.get("warm_intro", "[待补充]")
            signal = inv.get("recent_signal", "[待补充]")
            report += f"""### {name}

1. **匹配原因**：{fit}
2. **切入点**：{angle}
3. **暖介绍候选人**：{warm}
4. **时机信号**：{signal}

"""
        if not top_investors:
            report += "[待补充 outreach 策略]\n\n"
    else:
        report += "---\n\n## 4. Outreach Strategy\n\n"
        for inv in top_investors:
            name = inv.get("name", "Unknown")
            fit = inv.get("fit", "[TBD]")
            angle = inv.get("angle", "[TBD]")
            warm = inv.get("warm_intro", "[TBD]")
            signal = inv.get("recent_signal", "[TBD]")
            report += f"""### {name}

1. **Why they fit**: {fit}
2. **Approach angle**: {angle}
3. **Warm intro candidates**: {warm}
4. **Recent signal**: {signal}

"""
        if not top_investors:
            report += "[Outreach strategy to be added]\n\n"
    
    # Action Items
    if lang == "zh":
        report += """---\n\n## 五、行动计划\n
1. [ ] 确认目标投资人名单优先级
2. [ ] 研究每位合伙人的背景与公开言论
3. [ ] 寻找暖介绍路径（LinkedIn / 已投项目创始人 / 行业活动）
4. [ ] 准备定制版BP，针对重点投资人调整内容
5. [ ] 发送首轮 outreach 邮件 / 申请加速器项目
6. [ ] 跟进反馈，安排投资人会议

---

## 附录：补充投资人名单

| 投资人 | 类型 | 阶段 | 关注领域 | 备注 |
|--------|------|------|----------|------|
| [待补充] | VC | Seed-A | SaaS | 通过 Crunchbase 搜索 |

---

*免责声明：投资市场变化迅速，本报告中的数据仅供参考，请务必在 outreach 前进行最新信息核实。*
"""
    else:
        report += """---\n\n## 5. Action Items

1. [ ] Finalize and prioritize target investor list
2. [ ] Research each partner's background and public statements
3. [ ] Identify warm introduction paths (LinkedIn / portfolio founders / events)
4. [ ] Prepare tailored pitch deck for priority investors
5. [ ] Send initial outreach emails / apply to accelerators
6. [ ] Follow up and schedule investor meetings

---

## Appendix: Additional Investors

| Investor | Type | Stage | Focus | Notes |
|----------|------|-------|-------|-------|
| [To be added] | VC | Seed-A | SaaS | Search on Crunchbase |

---

*Disclaimer: The investment landscape changes rapidly. Please verify all information before outreach.*
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Report generated: {os.path.abspath(output_file)}")
    print(f"   Investors: {len(investors)} | Language: {lang}")


def main():
    parser = argparse.ArgumentParser(description="Generate investor research report")
    parser.add_argument("--input", "-i", required=True, help="Path to JSON config file")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    args = parser.parse_args()
    
    data = load_json(args.input)
    
    if args.output:
        output_file = args.output
    else:
        company = data.get("company_name", "Startup").replace(" ", "_")
        lang = data.get("language", "en")
        suffix = "Investor_Research" if lang == "en" else "投资人研究"
        output_file = f"{company}_{suffix}.md"
    
    generate_report(data, output_file)


if __name__ == "__main__":
    main()
