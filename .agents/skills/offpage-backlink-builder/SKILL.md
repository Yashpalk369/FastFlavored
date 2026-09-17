---
name: offpage-backlink-builder
description: >-
  White-hat automated backlink acquisition engine. Generates embeddable interactive
  link magnets (calculators/widgets with attribution links), journalist expert pitches
  for Connectively/HARO/Qwoted, broken-link outreach emails, and guest post packages.
---

# Off-Page Backlink Builder Skill

This skill automates high-authority, white-hat backlink acquisition for your niche blogs without relying on risky spam or private blog networks (PBNs).

## When to Use This Skill
- Launching an outreach campaign for a newly published pillar guide or listicle
- Generating an embeddable interactive tool / calculator to attract passive backlinks
- Drafting expert commentary responses for reporters on Connectively (HARO), Qwoted, or Terkel
- Reaching out to webmasters to replace broken or outdated competitor links with your new guide
- Pitching and drafting guest articles for authority blogs in your niche

## The 4 Backlink Acquisition Engines

### 1. Interactive Link Magnet Generator
Interactive tools attract 10x to 50x more backlinks than standard text articles because bloggers prefer embedding a working calculator or widget rather than building their own.

- Antigravity can code a standalone, responsive, zero-dependency HTML/JS widget (e.g. *Macro Calculator*, *ROI Estimator*, *Brew Ratio Calculator*, *Sizing Guide*).
- Each widget includes an embed code snippet with an attribution link:
  ```html
  <iframe src="https://yoursite.com/tools/calculator.html" width="100%" height="450" frameborder="0"></iframe>
  <p style="font-size:12px;">Tool provided by <a href="https://yoursite.com" target="_blank">YourBlog</a></p>
  ```

### 2. Journalist & Digital PR Pitch Engine (HARO / Connectively / Qwoted)
Reporters from Forbes, Business Insider, Healthline, and major publications post daily queries looking for expert commentary.

**Workflow**:
1. Paste the reporter's query into Antigravity.
2. The skill formats an immediate, high-acceptance pitch containing:
   - 2–3 punchy soundbites (journalists can quote verbatim).
   - Author title and professional credentials.
   - Exact link to your relevant guide for citation and source attribution.

### 3. The Broken Link & Skyscraper Outreach Engine
Find authority websites with dead or outdated links in your niche and offer your comprehensive new guide as the superior replacement.

Run the helper script:
```bash
python .agents/skills/offpage-backlink-builder/scripts/generate_outreach_campaign.py \
  --article-title "The Ultimate Ultralight Backpacking Checklist" \
  --article-url "https://yoursite.com/articles/ultralight-backpacking.html" \
  --niche "Outdoors & Hiking" \
  --type "broken_link"
```

### 4. Guest Post Pitch & Draft Engine
Antigravity writes customized editor pitch emails presenting 3 unique, data-backed topic ideas, and then writes the full guest article embedding contextual, organic backlinks to your blog.

See [outreach_templates.md](./resources/outreach_templates.md) for proven outreach copy templates.
