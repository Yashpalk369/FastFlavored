# FastFlavored Agent Guidelines & Automation Rules

Welcome to **FastFlavored** (`https://fastflavored.com`), a modern, high-speed culinary recipe blog featuring tested 15-to-30-minute weeknight dinners.

---

## 🎯 Primary Workflow: "Post Recipes" Trigger

Whenever the user prompts **"Post Recipes"**, **"Post new recipes"**, or **"post recipes as many till limit reset"**:

1. **Activate Skill**:
   - Always activate and adhere strictly to `.agents/skills/pinterest-recipe-publisher/SKILL.md` and `.agents/skills/aeo-geo-optimizer/SKILL.md`.

2. **Image Generation & Zero-Duplicate Policy**:
   - Every single recipe MUST have a unique, hyper-realistic AI-generated macro food photography image using `generate_image(AspectRatio="1:1", ImageName="...", Prompt="...")`.
   - Never reuse or duplicate images across recipes.
   - Optimize all generated images with Pillow to 600x600 progressive JPEGs (~75–120 KB) saved into `assets/images/<slug>.jpg`.
   - Test the image generation limit: generate and publish recipes consecutively until the image generation quota/limit is reached.

3. **Article Creation & Structure**:
   - Generate high-converting, fully styled HTML articles in `articles/<slug>.html`.
   - Each recipe must include:
     - Direct-Answer BLUF Box (`#quick-answer`) at the top for Google AI Overviews and Perplexity citations.
     - Schema.org `@graph` with complete `Recipe` and `FAQPage` JSON-LD schemas, linking ingredients and cuisine to Wikidata/Wikipedia entities.
     - Sticky Table of Contents, ingredient checkboxes, structured step-by-step instructions, nutrition breakdown grid, and Elena's Chef Pro-Tip box.
     - Collapsible FAQ accordion.
     - Cache-busted stylesheet and script links (`../css/style.css?v=2.1`, `../js/main.js?v=2.1`).

4. **Synchronization**:
   - **Database**: Prepend the new recipe entries to `articles_database.json`.
   - **Homepage**: Prepend the recipe card markup into `index.html` inside `<div class="article-grid" id="articleGrid">`. The homepage automatically handles 12-recipe pagination across pages.
   - **Sitemap**: Run `python .agents/skills/seo-auditor-optimizer/scripts/generate_sitemap.py --base-url https://fastflavored.com` to keep `sitemap.xml` and `robots.txt` synchronized.

5. **Git Deployment**:
   - Stage all new articles, images, and modified files.
   - Commit with a descriptive message (e.g., `feat: publish X new recipes with AI food photography`).
   - Push to `origin main` for automatic Vercel deployment.

6. **Pinterest Social Packages**:
   - Provide copy-ready Pinterest titles, search-optimized descriptions with hashtags, and recommended target boards for each published recipe.
