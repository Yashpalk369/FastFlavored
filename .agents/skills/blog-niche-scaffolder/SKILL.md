---
name: blog-niche-scaffolder
description: >-
  Scaffold a complete, modern, production-ready static blog for any niche from scratch.
  Use when starting a new blog, initializing a new niche website, or creating a fresh
  vanilla HTML5/CSS3/JS blog with dark/light themes, live search, and SEO schemas.
---

# Blog Niche Scaffolder

This skill generates a complete, high-performance, zero-build static blog in the current working directory. The generated blog is 100% compatible with Cloudflare Pages, GitHub Pages, Netlify, and Vercel.

## Workflow Overview

When invoked to create a new blog:
1. **Niche & Brand Discovery**: Confirm or infer:
   - **Blog Name**: (e.g., "Peak Wanderer", "CodeCraft Hub", "Zenith Finance", "Bark & Whisker")
   - **Blog Tagline**: (e.g., "Field-tested hiking guides and gear reviews for modern explorers")
   - **Niche Focus**: (e.g., Hiking & Outdoors, Web Development, Personal Finance, Dog Care)
   - **Visual Aesthetic & Colors**: (e.g., Forest Green & Sand, Indigo & Sky, Warm Terracotta, Dark Neon)
   - **Initial 3-5 Categories**: (e.g., "Gear Reviews", "Trail Guides", "Survival Tips", "Camping Food")
   - **Author Name**: (e.g., "Alex Morgan")
   *(If the user provides these in their prompt, proceed immediately without blocking!)*

2. **Run Scaffolding Helper**:
   You can either run the Python helper:
   ```bash
   python .agents/skills/blog-niche-scaffolder/scripts/scaffold_blog.py --name "Blog Name" --niche "Niche" --palette "preset_name" --author "Author Name"
   ```
   Or generate the files directly following the specifications below.

3. **Generated File Structure**:
   ```text
   ├── index.html                  # Homepage with Hero, Search, Category Chips, Grid, Newsletter
   ├── about.html                  # About author / brand story page
   ├── contact.html                # Contact page with functional client-side form feedback
   ├── privacy.html                # Privacy policy (GDPR/CCPA compliant)
   ├── terms.html                  # Terms of service
   ├── css/
   │   └── style.css               # Design tokens (HSL variables for light/dark theme), glassmorphism, responsive grid
   ├── js/
   │   └── main.js                 # Theme persistence, real-time live search, category chip filter, mobile drawer
   ├── articles/                   # Directory where all articles will be published
   │   └── sample-article.html     # Initial starter article showcasing layout
   ├── assets/                     # Images, favicon, and SVG icons
   │   ├── favicon.svg             # Clean vector favicon
   │   └── placeholder.webp        # Default fallback image
   ├── articles_database.json      # Structured catalog of all articles for search & indexing
   ├── robots.txt                  # Search engine crawler directives
   └── sitemap.xml                 # XML sitemap for Google Search Console
   ```

## Design & Architecture Standards

- **Zero-Build Stack**: Pure HTML5 semantic elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`), CSS3, and Vanilla ES6 JavaScript.
- **Design Tokens**: All colors defined via CSS HSL variables in `:root` and `body.dark-theme`:
  - `--bg-primary`, `--bg-secondary`, `--bg-card`, `--bg-glass`
  - `--text-primary`, `--text-secondary`, `--text-muted`
  - `--accent-color`, `--accent-hover`, `--accent-light`
  - `--border-color`, `--shadow-sm`, `--shadow-md`, `--shadow-lg`
- **Responsive Down to 320px**: Mobile navigation hamburger drawer, touch-friendly filter tags, and responsive cards grid (`grid-template-columns: repeat(auto-fill, minmax(320px, 1fr))`).
- **Live Search & Category Filtering**: `js/main.js` instantly filters cards on the homepage in real-time as the user types or clicks category chips without page reloads.
- **Dark/Light Theme Toggle**: Saves state in `localStorage` and respects system preferences (`prefers-color-scheme`).
- **Ad & Monetization Ready**: Built-in placeholders for 728x90 desktop banner, 320x50 mobile banner, and in-feed sponsored cards.
- **SEO & Social**: Pre-wired with OpenGraph, Twitter Cards, canonical tags, and JSON-LD structured data.

## Color Presets Reference

See [palette_presets.json](./resources/palette_presets.json) for curated color combinations:
- `terracotta_warm` (Food, Recipes, Cooking, Homemaking)
- `forest_adventure` (Travel, Outdoors, Hiking, Camping, Nature)
- `tech_indigo` (SaaS, Coding, AI, Gadgets, Productivity)
- `emerald_finance` (Personal Finance, Investing, Crypto, Real Estate)
- `rose_lifestyle` (Beauty, Fashion, Wellness, Parenting)
- `sunset_fitness` (Fitness, Gym, Nutrition, Athletics)
