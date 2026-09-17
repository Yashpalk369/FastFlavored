---
name: listicle-publisher
description: >-
  Publish high-converting listicle and product/tool roundup articles (e.g. "10 Best...",
  "7 Top...", "12 Proven...") for any niche blog. Creates semantic HTML, comparison tables,
  item ranking cards with pros/cons, ItemList schema, and updates the blog database.
---

# Listicle Publisher Skill

This skill formats, writes, and publishes high-converting, SEO-optimized listicle and roundup articles for your niche static blog.

## When to Use This Skill
- Publishing numbered product roundups (e.g., "9 Best Hiking Backpacks of 2026")
- Publishing curated recommendation lists (e.g., "15 High-Protein Dinner Recipes Under 30 Mins")
- Publishing tool/software roundups (e.g., "7 Best AI Coding Tools for Beginners")
- Publishing tip lists or strategy roundups (e.g., "10 Proven Ways to Lower Grocery Bills")

## Architecture of a Professional Listicle Article

Every listicle article generated must include the following structural components in `articles/<slug>.html`:

1. **Header & Metadata**:
   - Semantic `<header>` matching the blog's theme.
   - SEO `<title>` (50-60 characters, e.g., `10 Best [Niche Items] in 2026 (Tested & Ranked) | [BlogName]`).
   - Meta `<description>` (140-160 characters).
   - Canonical link tag.
   - OpenGraph and Twitter cards.
   - **Schema.org JSON-LD**:
     - `ItemList` schema with each item represented as a `ListItem` containing `name`, `position`, and `url`.
     - `FAQPage` schema for the FAQ section.

2. **Hero Header**:
   - Category badge chip.
   - Post Title (H1) and Subtitle.
   - Author, publish date, reading time (e.g., "8 min read"), and "Tested & Fact-Checked" trust badge.

3. **Quick Comparison Table (Top Picks at a Glance)**:
   - Placed right before the detailed breakdown so readers in a hurry can see the top 3-5 picks instantly.
   - Table columns: `Rank`, `Item Name`, `Award / Best For`, `Key Highlight`, `Rating`, `Quick Link`.

4. **Itemized Detailed Ranking Cards (`#1`, `#2`, `#3`...)**:
   Each item must be housed in a styled card container:
   - **Ranking Number Badge**: `#1`, `#2`, etc.
   - **Award Badge**: (e.g., "Best Overall", "Best Value", "Editor's Choice", "Best Premium").
   - **High-Res Image**: Responsive WebP image placeholder with descriptive alt text.
   - **In-Depth Editorial Review**: What it is, why it stands out, who it is best for.
   - **Visual Pros & Cons Grid**:
     - Green checkmark pros (`<i class="fa-solid fa-check"></i>`).
     - Red cross cons (`<i class="fa-solid fa-xmark"></i>`).
   - **Key Specifications / Features List**.
   - **Our Verdict**: 2-sentence summary of why this earned its rank.
   - **CTA Button**: High-converting button (e.g., `Check Current Price &rarr;`).

5. **Buying Guide & Methodology Section**:
   - "How We Evaluated & Tested These [Items]"
   - 3-4 criteria readers should consider before buying.

6. **Frequently Asked Questions (FAQ)**:
   - 3-5 common long-tail search questions with clear, direct answers formatted for Google Featured Snippets.

7. **Social Sharing & Author Bio**:
   - Social buttons: Pinterest, Twitter/X, Facebook, and Copy Link.
   - Author bio with avatar and expertise credentials.

## Automatic Database Registration

Whenever a listicle is published, execute the helper script:
```bash
python .agents/skills/listicle-publisher/scripts/register_article.py \
  --title "10 Best Wireless Earbuds in 2026" \
  --slug "best-wireless-earbuds-2026" \
  --category "Reviews" \
  --author "Alex Morgan" \
  --read-time "8 min read" \
  --excerpt "We tested 25 pairs of wireless earbuds for sound quality, battery life, and noise cancellation. Here are the top 10 winners." \
  --image "./assets/earbuds.webp" \
  --type "listicle"
```

This script automatically:
1. Adds the metadata entry into `articles_database.json`.
2. Adds the new card into `index.html` with data categories for instant live search.
3. Appends the new URL to `sitemap.xml`.
