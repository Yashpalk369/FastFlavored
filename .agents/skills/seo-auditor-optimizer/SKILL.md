---
name: seo-auditor-optimizer
description: >-
  Audit, optimize, and fix on-page and technical SEO for any static niche blog.
  Checks meta tags, heading hierarchies, image alt tags, JSON-LD schemas, orphan posts,
  and automatically generates/regenerates clean sitemap.xml and robots.txt.
---

# SEO Auditor & Optimizer Skill

This skill performs automated on-page SEO audits, discovers internal linking opportunities, and generates technical SEO assets (`sitemap.xml` and `robots.txt`) for your static blog.

## When to Use This Skill
- After publishing a batch of new articles or listicles
- When auditing existing blog pages for Google search ranking factors
- When resolving missing meta descriptions, image alt tags, or broken headings
- When generating or rebuilding `sitemap.xml`

## Core Workflows

### 1. Run Complete Site SEO Audit
Execute the automated audit script:
```bash
python .agents/skills/seo-auditor-optimizer/scripts/audit_seo.py --root .
```

The script evaluates:
- **Title Tag Health**: 45–65 characters; presence of primary keyword and brand suffix.
- **Meta Description**: 130–165 characters; clear call-to-action or summary.
- **Heading Structure**: Exactly one `<h1>`, proper nesting (`<h2>` before `<h3>`), no empty headings.
- **Image Attributes**: All `<img>` elements have meaningful `alt` text and `loading="lazy"` (except hero images).
- **Internal Linking Graph**: Scans all HTML files in `articles/` to find "orphan" articles that have zero internal links pointing to them.
- **Schema Validation**: Confirms valid JSON-LD `<script type="application/ld+json">` is present.

### 2. Generate / Rebuild Sitemap
To generate an XML sitemap encompassing all pages and articles:
```bash
python .agents/skills/seo-auditor-optimizer/scripts/generate_sitemap.py --base-url "https://yoursite.com"
```

### 3. Internal Linking Suggestions
When publishing a new article, search `articles_database.json` for related topics and add 2–3 contextual hyperlinks inside the article body pointing to existing posts, while also adding a reciprocal link from an older top-ranking post to the new post.
