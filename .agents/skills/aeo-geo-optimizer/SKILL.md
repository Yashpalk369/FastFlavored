---
name: aeo-geo-optimizer
description: >-
  Optimize blog articles for Answer Engine Optimization (AEO) and Generative Engine
  Optimization (GEO). Injects direct-answer target blocks (BLUF), Wikidata/Wikipedia
  entity schemas, and information-gain comparison matrices to win citations in Google
  AI Overviews, Perplexity, and ChatGPT Search.
---

# AEO & GEO Optimizer Skill

This skill transforms traditional SEO articles into AI-favored authority resources optimized for **Google AI Overviews**, **Perplexity**, **ChatGPT Search**, **Claude**, and **Gemini**.

## When to Use This Skill
- Before or after publishing any guide or listicle to maximize AI search citations
- When targeting conversational queries (e.g., "What is the best way to...", "Is X worth it?")
- When adding Knowledge Graph entity relationships (`about` and `mentions` schemas) to establish topical authority
- When aiming to win Google Featured Snippets and AI Summary cards

## Core Optimization Pillars

### 1. The BLUF (Bottom Line Up Front) Direct-Answer Formula
AI search engines (Perplexity, AI Overviews) look for concise, definitive answer paragraphs immediately beneath heading tags (`<h2>` or `<h3>`).

```html
<!-- Example AEO Direct Answer Block -->
<div class="aeo-answer-box">
  <p><strong>Quick Answer:</strong> The best method to [solve query] is [primary solution], because [key reason]. Most users should follow [step 1] and [step 2], which delivers [benefit] in [timeframe].</p>
</div>
```

**Formula Guidelines**:
- **Word count**: 40 to 60 words.
- **Placement**: Directly below the main question heading.
- **Tone**: Objective, authoritative, factual (third-person).
- **Structure**: Core answer in Sentence 1 &rarr; Supporting rationale in Sentence 2 &rarr; Key condition/metric in Sentence 3.

### 2. Entity-Salience & Knowledge Graph Schemas
LLMs use Knowledge Graphs to evaluate if your page is talking about authoritative entities. We link entities to **Wikidata** and **Wikipedia** within the article's JSON-LD:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "about": [
    {
      "@type": "Thing",
      "name": "Search Engine Optimization",
      "sameAs": "https://en.wikipedia.org/wiki/Search_engine_optimization"
    }
  ],
  "mentions": [
    {
      "@type": "Thing",
      "name": "Artificial Intelligence",
      "sameAs": "https://www.wikidata.org/wiki/Q11660"
    }
  ]
}
```

### 3. Structured Data Comparison Matrices
Generative engines prefer structured HTML tables over long paragraphs when synthesizing recommendations. Always include:
- Clear, descriptive table headers (`<th>`)
- Numeric data (percentages, prices, weights, durations)
- Direct binary ratings (`Yes/No`, `High/Medium/Low`)

## Automation Workflow

To automatically inject AEO direct answer blocks or validate an article:
```bash
python .agents/skills/aeo-geo-optimizer/scripts/inject_aeo_blocks.py --file "articles/sample.html" --query "How to master X" --answer "The fastest way to master X is..."
```

See [aeo_geo_templates.md](./resources/aeo_geo_templates.md) for full copywriting frameworks.
