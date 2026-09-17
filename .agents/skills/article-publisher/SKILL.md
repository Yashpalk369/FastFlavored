---
name: article-publisher
description: >-
  Publish in-depth single articles, deep-dive guides, and how-to tutorials (1,500-3,000+ words)
  for any niche blog. Generates sticky Table of Contents, key takeaways callouts,
  pro-tips, FAQPage & BlogPosting schema, and updates the blog database.
---

# Article Publisher Skill

This skill formats, writes, and publishes comprehensive, high-ranking single deep-dive articles, ultimate guides, and step-by-step tutorials for your static niche blog.

## When to Use This Skill
- Publishing long-form pillar guides (e.g., "The Complete Beginner's Guide to Sourdough Baking")
- Publishing how-to tutorials (e.g., "How to Build a Custom Mechanical Keyboard from Scratch")
- Publishing opinion pieces, case studies, or deep industry breakdowns
- Publishing single-topic reviews or deep-dive investigations

## Architecture of a Professional Deep-Dive Single Article

Every single article generated must include the following components in `articles/<slug>.html`:

1. **Header & Metadata**:
   - SEO `<title>` (50-60 characters, e.g., `How to [Goal] in [Year]: Complete Step-by-Step Guide | [BlogName]`).
   - Meta `<description>` (140-160 characters answering search intent directly).
   - Canonical tag, OpenGraph, Twitter card tags.
   - **Schema.org JSON-LD**:
     - `BlogPosting` or `Article` schema with `author`, `datePublished`, `headline`, `image`, and `publisher`.
     - `BreadcrumbList` schema.
     - `FAQPage` schema.

2. **Hero Header**:
   - Category badge chip (e.g., "Complete Guide", "Tutorial", "Strategy").
   - Article Title (H1) and Subtitle.
   - Author name, publish date, reading time (e.g., "11 min read"), and "Expert Verified" badge.

3. **Key Takeaways Box**:
   - Top summary card with `<i class="fa-solid fa-lightbulb"></i>` icon highlighting 3-4 critical conclusions so readers immediately get actionable value.

4. **Sticky Table of Contents (TOC)**:
   - Floating or collapsible card with jump links (`#section-1`, `#section-2`...) to all major H2 and H3 headings.
   - Enables smooth scrolling and rapid navigation for desktop and mobile readers.

5. **Editorial Body Layout (1,500 - 3,000 words)**:
   - **Visual Callouts**:
     - `pro-tip-box` (Blue or Green with lightbulb/star icon for insider tips).
     - `caution-box` (Amber or Red with alert icon for common mistakes to avoid).
     - `editorial-quote` (Styled blockquote with accent border and italics).
   - **Structured Headings**: Clean hierarchy (H1 &rarr; H2 &rarr; H3) with IDs matching the TOC.
   - **Data Tables & Step Checklists** where relevant to enhance engagement and dwell time.

6. **Interactive FAQ Accordion**:
   - 4-6 high-volume questions sourced from Google's "People Also Ask" box.
   - Click-to-expand accordion powered by `js/main.js`.

7. **Author Credential Box & Social Sharing Bar**:
   - Author expertise paragraph, profile initials/avatar, and disclaimer.
   - One-click share buttons for Pinterest, Twitter/X, Facebook, and Copy Link.

## Automatic Database Registration

Whenever a single article is published, execute the helper script:
```bash
python .agents/skills/article-publisher/scripts/register_article.py \
  --title "How to Build an Ultra-Quiet Home Office in 2026" \
  --slug "ultra-quiet-home-office-guide" \
  --category "Guides" \
  --author "Editorial Staff" \
  --read-time "10 min read" \
  --excerpt "A complete acoustic insulation and equipment guide to creating a distraction-free, soundproof home workspace." \
  --image "./assets/home-office.webp" \
  --type "single_article"
```

This script automatically updates `articles_database.json`, inserts the card into `index.html`, and registers the URL in `sitemap.xml`.
