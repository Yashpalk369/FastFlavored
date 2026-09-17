# AEO & GEO Copywriting Formulas

## 1. Direct Definition Formula (For Concept & "What is" Queries)
> **[Term]** is a **[category/classification]** designed to **[core primary function]**. It operates by **[1-sentence mechanism]**, providing **[primary advantage]** compared to conventional alternatives.

*Example:*
> **Generative Engine Optimization (GEO)** is a content optimization framework designed to maximize visibility and citations within AI search engines like Perplexity, ChatGPT, and Google AI Overviews. It operates by structuring authoritative factual entities, comparison tables, and direct-answer summaries that LLM retrieval algorithms prioritize during response generation.

---

## 2. Recommendation Formula (For "Best" & Listicle Queries)
> The best **[item category]** for most users is **[Top Pick Name]**, which offers **[flagship feature]** at **[price tier]**. If you prioritize **[budget/specific use case]**, **[Alternative Pick]** is the superior alternative due to its **[secondary benefit]**.

---

## 3. Step-by-Step Action Formula (For "How-To" Queries)
> To **[achieve goal]**, follow these core steps: 
> 1. **[Action 1]**: [Brief explanation]
> 2. **[Action 2]**: [Brief explanation]
> 3. **[Action 3]**: [Brief explanation]
> This process typically takes **[time estimate]** and requires **[essential prerequisite]**.

---

## 4. Entity Schema JSON-LD Generator
Inject this into the `<head>` of any article to connect your content directly with Google's Knowledge Graph and Wikidata entities:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://yoursite.com/articles/slug.html#article",
      "headline": "Article Title",
      "about": [
        {
          "@type": "Thing",
          "name": "Primary Topic",
          "sameAs": "https://en.wikipedia.org/wiki/Primary_Topic"
        }
      ],
      "mentions": [
        {
          "@type": "Thing",
          "name": "Secondary Entity",
          "sameAs": "https://www.wikidata.org/wiki/Q12345"
        }
      ]
    }
  ]
}
```
