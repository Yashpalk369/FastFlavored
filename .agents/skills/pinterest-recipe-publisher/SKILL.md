---
name: pinterest-recipe-publisher
description: >-
  Discover viral Pinterest & upcoming seasonal recipe trends, publish complete AEO/GEO optimized
  recipes with mandatory AI-first photography (zero duplicates), copy-ready Pinterest SEO packages,
  and automated blog database and sitemap synchronization.
---

# Pinterest Recipe Publisher Skill

This skill governs the end-to-end workflow for researching, generating, and publishing viral, trending recipes on **The Spiced Spoon**, driven by current Pinterest search trends and upcoming seasonal demand.

---

## Core Principles & Non-Negotiable Rules

### 1. Mandatory Unique AI-Generated Image & Zero-Duplicate Policy
* **All images MUST be generated with AI**: Every recipe image for all future recipes MUST be generated using AI (`generate_image`) with an aspect ratio of `1:1`.
* **Strict Recipe Relevance**: Every AI image prompt must specifically and appetizingly represent the exact recipe, including its key ingredients, garnish, textures, steam, and culinary styling. Generic, mismatched, or unrelated food photography is strictly prohibited.
* **WebP Optimization**: Convert all AI-generated images to **600x600 WebP** at quality `92` into `assets/<slug>.webp`.
* **Zero-Duplicate Policy**: Under NO circumstances reuse, borrow, duplicate, or mirror images across recipes. Every single recipe must have its own distinct, dedicated image.
* **Strict Quota Handling**:
  * If the AI image generation model returns a quota error (`429 RESOURCE_EXHAUSTED`):
    * Publish the recipe **WITHOUT an image** (styled with an elegant typography card and icon badge), or wait until the quota window resets.
    * Mark the recipe in `recipes_database.json` as awaiting image (`"image_filename": ""`).
    * **STRICTLY PROHIBITED**: NEVER use placeholder duplicates from existing recipes.

### 2. Mandatory Priority Image Backfill for Imageless Recipes (Await & Backfill First)
* **First Action on Limit Reset**: Before or when posting any new recipes, the agent MUST ALWAYS first check `recipes_database.json` for any existing recipes that are currently without images due to previous quota limits (e.g. `prosciutto-wrapped-stuffed-pork-tenderloin`, `creamy-tuscan-white-bean-soup`, `maple-brown-butter-pumpkin-cake`).
* **Test Quota**: Test if the AI image generation limit has reset.
* **Generate Waiting Recipes First**: If the quota is available, the agent **MUST generate AI images for the awaiting imageless recipes FIRST** before generating or publishing new recipes.
* **Automatic Full Synchronization Upon Backfilling**:
  1. Generate unique AI macro food photography specifically matching the dish using `generate_image`.
  2. Optimize and convert to `assets/<slug>.webp` (600x600 WebP at quality 92).
  3. Update `recipes_database.json` with the new `image_filename`, `image_prompt`, and image metadata.
  4. Update the recipe's individual page in `recipes/<slug>.html` with the hero image, responsive styling, and updated JSON-LD schema.
  5. Update the recipe card in `index.html` to display the new image thumbnail.

### 3. Pinterest Trend & Upcoming Trend Sourcing
* When selecting new recipes, identify dishes currently dominating Pinterest feeds or emerging for the upcoming season:
  * **Autumn / Fall**: Creamy one-pot pasta, squash/pumpkin creations, warm spiced baked goods, slow-cooker stews, high-protein dips, cozy restorative soups.
  * **Winter / Holidays**: Rich braised meats, festive holiday cookies, comfort bakes, warm ciders, molten chocolate desserts.
  * **Spring**: Bright lemon pasta, asparagus & pea dishes, fresh berry galettes, vibrant Mediterranean salads, whipped feta.
  * **Summer**: Sheet pan grilled skewers, elote street corn, refreshing mocktails/spritzes, no-bake icebox cakes, chilled watermelon salads.
  * **Year-Round Viral Cravings**: High-protein cottage cheese hacks, air fryer crispy proteins, 15-minute aesthetic brunch toasts, hot honey variations.
* **Catalog Check**: Always check `recipes_database.json` first to avoid creating recipes with the same or near-identical concepts as existing ones.

### 4. Complete AEO / GEO & Google Discover Standards
Every recipe published through this skill must be generated using `scripts/recipe_engine.py` to guarantee:
* **AEO Direct-Answer Box (BLUF)**: Positioned above the recipe card with `<div class="aeo-summary-box">` and `<div class="aeo-badge"><i class="fa-solid fa-wand-magic-sparkles"></i> The Quick Takeaway</div>` to capture Google AI Overviews, Perplexity, and ChatGPT Search.
* **GEO Entity Knowledge Graph**: JSON-LD `Recipe` schema must link the dish's cuisine, technique, and core ingredients to authoritative Wikidata and Wikipedia entities (`about` and `sameAs`).
* **Google Discover Compliance**: Include `<meta name="robots" content="max-image-preview:large, max-snippet:-1">`.
* **Google Search Console Rich Snippets**:
  * Valid `aggregateRating` (rating `4.9` with `110+` reviews) to prevent missing field warnings in Search Console.
  * Complete nutrition data table (calories, carbs, protein, fat, fiber).
  * Prep time, cook time, total time in ISO 8601 format (`PT30M`).
  * Yield / servings, equipment list, and interactive ingredients with scaling support.
  * 3–4 culinary science pro-tips and 3 Google "People Also Ask" FAQs.

### 5. Pinterest Social Copy Package (No Pin Graphics Creation)
* **DO NOT generate HTML pin templates or image files**: The user creates Pinterest pins manually using their own design workflow.
* **Generate Social Copy Package**: For every recipe published, provide copy-ready metadata for easy manual pin publishing:
  * **Target Board**: Specific Pinterest board category (e.g. *Comfort Food Dinners*, *Fall Baking Ideas*).
  * **Pin Title**: High-CTR, search-optimized title under 100 characters.
  * **Pin Description**: 200–350 characters explaining why someone must make this tonight, ending with an explicit call-to-action.
  * **Hashtags**: 6–8 targeted niche hashtags.

---

## Step-by-Step Execution Workflow

When the user asks to *"post new recipes"* or *"post three new recipes"*:

### Step 0: Scan & Backfill Awaiting Imageless Recipes (Mandatory First Priority)
1. Inspect `recipes_database.json` for any recipes where `image_filename` is empty or missing (recipes awaiting images).
2. If imageless recipes are found, test if AI image quota is available.
3. If quota is available, **generate AI images for the awaiting recipes FIRST**:
   - Call `generate_image` with rich, authentic culinary prompts.
   - Convert to 600x600 WebP at quality 92 in `assets/<slug>.webp`.
   - Update `recipes_database.json`, `recipes/<slug>.html`, and `index.html`.
4. Only then proceed to generate and post new recipes.

### Step 1: Research & Trend Selection
1. Inspect `recipes_database.json` to review existing recipes.
2. Select 3 trending recipe concepts aligned with Pinterest search spikes and seasonal relevance.
3. Ensure all slugs and recipe concepts are 100% distinct.

### Step 2: AI Image Generation
1. Formulate detailed, hyper-realistic macro food photography prompts for each recipe.
2. Call `generate_image(AspectRatio="1:1", ImageName="...", Prompt="...")`.
3. If quota is active: Convert and save the generated image to `assets/<slug>.webp` (600x600 WebP at quality 92).
4. If quota returns 429:
   - Check if dedicated, 100% unique authentic culinary photography can be sourced specifically for that dish.
   - If not available, configure the recipe without an image.
   - **Under no circumstances reuse an existing image asset.**

### Step 3: Publish Through Recipe Engine
1. Execute `scripts/recipe_engine.py` or write an execution script that calls `publish_recipe(recipe_dict, project_dir=".")`.
2. Ensure the recipe dictionary contains:
   - `id`, `title`, `subtitle`, `description`
   - `category_id`, `category_name`, `categories_str`, `badge_class`
   - `image_filename`, `image_prompt`
   - `prep_time`, `cook_time`, `total_time`, `cuisine`, `yield`, `base_servings`
   - `calories`, `carbs`, `protein`, `fat`, `fiber`
   - `ingredients` (structured array with `qty`, `unit`, `name`, `notes`)
   - `instructions` (numbered steps with `step`, `title`, `text`)
   - `equipment`, `tips`, `faqs`, `bluf_summary`
   - `rating_value` ("4.9"), `review_count` ("120"-"150")

### Step 4: Formulate Pinterest Social Copy Package
1. Formulate the Pinterest title, description, board suggestion, and hashtags for the user to copy-paste into Pinterest.
2. Do NOT generate HTML or PNG pin graphics (the user creates pins manually).

### Step 5: Update Homepage, Log & Sitemap
1. Insert the new recipe cards at the beginning of the grid in `index.html` (inside `<!-- RECIPE_CARDS_START -->`).
2. Append the recipe IDs to `recipes/generated_log.json`.
3. Regenerate `sitemap.xml` and `robots.txt` using `.agents/skills/seo-auditor-optimizer/scripts/generate_sitemap.py`.

### Step 6: Git Commit & Deployment
1. Stage all new and modified files (`assets/*.webp`, `recipes/`, `index.html`, `recipes_database.json`, `sitemap.xml`, `robots.txt`).
2. Commit with a descriptive message detailing the recipes published.
3. Push to `origin main`.
