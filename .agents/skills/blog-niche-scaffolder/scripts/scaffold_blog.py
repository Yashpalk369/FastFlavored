#!/usr/bin/env python3
"""
Blog Niche Scaffolder CLI
Generates a complete, zero-build, ultra-fast static niche blog.
"""

import os
import sys
import json
import argparse

def get_palette(preset_name, resources_dir):
    presets_file = os.path.join(resources_dir, "palette_presets.json")
    if os.path.exists(presets_file):
        with open(presets_file, "r", encoding="utf-8") as f:
            presets = json.load(f)
            if preset_name in presets:
                return presets[preset_name]
    # Fallback to tech_indigo
    return {
        "name": "Tech Indigo",
        "font_heading": "'Plus Jakarta Sans', sans-serif",
        "font_body": "'Inter', sans-serif",
        "light": {
            "bg_primary": "hsl(220, 30%, 98%)",
            "bg_secondary": "hsl(220, 25%, 94%)",
            "bg_card": "hsl(0, 0%, 100%)",
            "text_primary": "hsl(222, 47%, 11%)",
            "text_secondary": "hsl(215, 16%, 38%)",
            "accent_color": "hsl(243, 75%, 59%)",
            "accent_hover": "hsl(243, 75%, 50%)",
            "accent_light": "hsl(243, 80%, 95%)",
            "badge_color": "hsl(175, 80%, 35%)"
        },
        "dark": {
            "bg_primary": "hsl(222, 47%, 9%)",
            "bg_secondary": "hsl(222, 40%, 13%)",
            "bg_card": "hsl(222, 35%, 17%)",
            "text_primary": "hsl(210, 40%, 96%)",
            "text_secondary": "hsl(215, 20%, 72%)",
            "accent_color": "hsl(243, 90%, 68%)",
            "accent_hover": "hsl(243, 90%, 76%)",
            "accent_light": "hsl(243, 50%, 20%)",
            "badge_color": "hsl(175, 75%, 45%)"
        }
    }

def generate_css(palette):
    light = palette["light"]
    dark = palette["dark"]
    return f"""/* ==========================================================================
   DESIGN TOKENS & CSS VARIABLES ({palette.get('name', 'Custom')})
   ========================================================================== */
:root {{
  /* Light Theme */
  --bg-primary: {light['bg_primary']};
  --bg-secondary: {light['bg_secondary']};
  --bg-card: {light['bg_card']};
  --bg-glass: rgba(255, 255, 255, 0.85);
  
  --text-primary: {light['text_primary']};
  --text-secondary: {light['text_secondary']};
  --text-muted: hsl(215, 10%, 60%);
  
  --accent-color: {light['accent_color']};
  --accent-hover: {light['accent_hover']};
  --accent-light: {light['accent_light']};
  --badge-color: {light['badge_color']};
  
  --border-color: rgba(0, 0, 0, 0.08);
  --border-glass: rgba(255, 255, 255, 0.6);
  
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.12);
  
  /* Fonts */
  --font-heading: {palette.get('font_heading', "'Plus Jakarta Sans', sans-serif")};
  --font-body: {palette.get('font_body', "'Inter', sans-serif")};
  
  /* Radii & Transitions */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  --transition: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}}

body.dark-theme {{
  /* Dark Theme */
  --bg-primary: {dark['bg_primary']};
  --bg-secondary: {dark['bg_secondary']};
  --bg-card: {dark['bg_card']};
  --bg-glass: rgba(20, 24, 33, 0.85);
  
  --text-primary: {dark['text_primary']};
  --text-secondary: {dark['text_secondary']};
  --text-muted: hsl(215, 10%, 55%);
  
  --accent-color: {dark['accent_color']};
  --accent-hover: {dark['accent_hover']};
  --accent-light: {dark['accent_light']};
  --badge-color: {dark['badge_color']};
  
  --border-color: rgba(255, 255, 255, 0.1);
  --border-glass: rgba(255, 255, 255, 0.12);
  
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.5);
}}

/* ==========================================================================
   RESET & BASE STYLES
   ========================================================================== */
*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html {{
  scroll-behavior: smooth;
}}

body {{
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.65;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  transition: background-color var(--transition), color var(--transition);
  overflow-x: hidden;
}}

h1, h2, h3, h4, h5, h6 {{
  font-family: var(--font-heading);
  color: var(--text-primary);
  font-weight: 700;
  line-height: 1.3;
}}

a {{
  color: inherit;
  text-decoration: none;
}}

img {{
  max-width: 100%;
  height: auto;
  display: block;
}}

.container {{
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}}

/* Glassmorphism Panel */
.glass-panel {{
  background: var(--bg-glass);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
}}

/* ==========================================================================
   HEADER & NAVBAR
   ========================================================================== */
.header {{
  position: sticky;
  top: 0;
  z-index: 100;
  transition: box-shadow var(--transition);
}}

.header.scrolled {{
  box-shadow: var(--shadow-sm);
}}

.navbar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
}}

.logo {{
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-heading);
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--text-primary);
}}

.logo span.accent {{
  color: var(--accent-color);
}}

.nav-links {{
  display: flex;
  align-items: center;
  gap: 2rem;
}}

.nav-links a {{
  font-weight: 500;
  color: var(--text-secondary);
  transition: color var(--transition);
}}

.nav-links a:hover,
.nav-links a.active {{
  color: var(--accent-color);
}}

.nav-controls {{
  display: flex;
  align-items: center;
  gap: 1rem;
}}

.theme-toggle {{
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background var(--transition), transform var(--transition);
}}

.theme-toggle:hover {{
  transform: rotate(15deg);
}}

.theme-toggle .sun-icon {{ display: none; }}
.theme-toggle .moon-icon {{ display: block; }}
body.dark-theme .theme-toggle .sun-icon {{ display: block; }}
body.dark-theme .theme-toggle .moon-icon {{ display: none; }}

.mobile-menu-btn {{
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  flex-direction: column;
  gap: 5px;
}}

.mobile-menu-btn span {{
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text-primary);
  transition: transform var(--transition);
}}

/* ==========================================================================
   HERO SECTION
   ========================================================================== */
.hero-section {{
  padding: 3.5rem 0 2.5rem;
}}

.hero-grid {{
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 3rem;
  align-items: center;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: var(--shadow-sm);
}}

.hero-tag {{
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent-color);
  background: var(--accent-light);
  padding: 0.35rem 0.8rem;
  border-radius: var(--radius-full);
  margin-bottom: 1rem;
}}

.hero-title {{
  font-size: 2.5rem;
  margin-bottom: 1rem;
  line-height: 1.2;
}}

.hero-description {{
  font-size: 1.1rem;
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
}}

.hero-image-wrapper {{
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  aspect-ratio: 16 / 10;
}}

.hero-image-wrapper img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}}

.hero-image-wrapper:hover img {{
  transform: scale(1.03);
}}

/* ==========================================================================
   BUTTONS
   ========================================================================== */
.btn {{
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-full);
  transition: all var(--transition);
  cursor: pointer;
  border: none;
}}

.btn-primary {{
  background: var(--accent-color);
  color: #fff;
}}

.btn-primary:hover {{
  background: var(--accent-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}}

/* ==========================================================================
   FILTER & SEARCH SECTION
   ========================================================================== */
.filter-section {{
  margin: 2.5rem auto 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}}

.search-wrapper {{
  position: relative;
  width: 100%;
}}

.search-icon {{
  position: absolute;
  left: 1.25rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 1.1rem;
}}

.search-input {{
  width: 100%;
  padding: 0.9rem 1.25rem 0.9rem 3rem;
  font-size: 1rem;
  font-family: inherit;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-color);
  background: var(--bg-card);
  color: var(--text-primary);
  outline: none;
  transition: border-color var(--transition), box-shadow var(--transition);
}}

.search-input:focus {{
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px var(--accent-light);
}}

.category-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}}

.cat-btn {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  padding: 0.5rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition);
}}

.cat-btn:hover,
.cat-btn.active {{
  background: var(--accent-color);
  color: #fff;
  border-color: var(--accent-color);
}}

/* ==========================================================================
   ARTICLE CARDS GRID
   ========================================================================== */
.article-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
  margin-bottom: 3.5rem;
}}

.article-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: transform var(--transition), box-shadow var(--transition);
}}

.article-card:hover {{
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}}

.card-image-wrap {{
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
}}

.card-image-wrap img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}}

.article-card:hover .card-image-wrap img {{
  transform: scale(1.05);
}}

.card-badge {{
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: var(--bg-glass);
  backdrop-filter: blur(8px);
  color: var(--accent-color);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-glass);
}}

.card-content {{
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}}

.card-meta {{
  display: flex;
  align-items: center;
  gap: 1rem;
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 0.6rem;
}}

.card-title {{
  font-size: 1.25rem;
  margin-bottom: 0.6rem;
  line-height: 1.35;
}}

.card-excerpt {{
  color: var(--text-secondary);
  font-size: 0.95rem;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}}

.card-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--border-color);
  padding-top: 1rem;
  font-size: 0.85rem;
  color: var(--text-muted);
}}

.read-link {{
  color: var(--accent-color);
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}}

/* ==========================================================================
   NEWSLETTER CARD
   ========================================================================== */
.newsletter-section {{
  background: var(--accent-light);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 3rem 2rem;
  text-align: center;
  margin: 3rem auto;
  max-width: 800px;
}}

.newsletter-title {{
  font-size: 2rem;
  margin-bottom: 0.5rem;
}}

.newsletter-desc {{
  color: var(--text-secondary);
  max-width: 500px;
  margin: 0 auto 1.5rem;
}}

.newsletter-form {{
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  max-width: 500px;
  margin: 0 auto;
}}

.newsletter-input {{
  flex-grow: 1;
  padding: 0.85rem 1.25rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-color);
  outline: none;
  font-size: 0.95rem;
}}

/* ==========================================================================
   FOOTER
   ========================================================================== */
.footer {{
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-color);
  padding: 3.5rem 0 2rem;
  margin-top: 4rem;
}}

.footer-grid {{
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 3rem;
  margin-bottom: 2.5rem;
}}

.footer-desc {{
  color: var(--text-secondary);
  margin-top: 0.75rem;
  font-size: 0.95rem;
  max-width: 360px;
}}

.footer-links-title {{
  font-size: 1rem;
  margin-bottom: 1rem;
  color: var(--text-primary);
}}

.footer-links {{
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  list-style: none;
}}

.footer-links a {{
  color: var(--text-secondary);
  font-size: 0.9rem;
  transition: color var(--transition);
}}

.footer-links a:hover {{
  color: var(--accent-color);
}}

.footer-bottom {{
  border-top: 1px solid var(--border-color);
  padding-top: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--text-muted);
}}

/* ==========================================================================
   RESPONSIVE MEDIA QUERIES
   ========================================================================== */
@media (max-width: 900px) {{
  .hero-grid {{
    grid-template-columns: 1fr;
    padding: 1.5rem;
    gap: 1.5rem;
  }}
  .hero-title {{
    font-size: 2rem;
  }}
  .footer-grid {{
    grid-template-columns: 1fr 1fr;
  }}
}}

@media (max-width: 768px) {{
  .navbar {{
    height: 60px;
  }}
  .mobile-menu-btn {{
    display: flex;
  }}
  .nav-links {{
    position: fixed;
    top: 60px;
    right: -100%;
    width: 260px;
    height: calc(100vh - 60px);
    background: var(--bg-card);
    border-left: 1px solid var(--border-color);
    flex-direction: column;
    align-items: flex-start;
    padding: 2rem 1.5rem;
    box-shadow: var(--shadow-lg);
    transition: right var(--transition);
  }}
  .nav-links.active {{
    right: 0;
  }}
  .article-grid {{
    grid-template-columns: 1fr;
  }}
  .newsletter-form {{
    flex-direction: column;
  }}
  .footer-grid {{
    grid-template-columns: 1fr;
    gap: 2rem;
  }}
  .footer-bottom {{
    flex-direction: column;
    gap: 0.75rem;
    text-align: center;
  }}
}}
"""

def generate_js():
    return """/**
 * Core JS Engine
 * Features: Theme toggle, mobile menu, live search & category filtering, and newsletter handling.
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initStickyHeader();
  initLiveSearchAndFilter();
  initNewsletter();
});

/* Theme Manager */
function initTheme() {
  const toggleBtn = document.getElementById('themeToggle');
  if (!toggleBtn) return;

  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-theme');
  }

  toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    const isDark = document.body.classList.contains('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
}

/* Mobile Menu Drawer */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('navLinks');
  if (!menuBtn || !navLinks) return;

  menuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    navLinks.classList.toggle('active');
  });

  document.addEventListener('click', (e) => {
    if (!menuBtn.contains(e.target) && !navLinks.contains(e.target)) {
      navLinks.classList.remove('active');
    }
  });
}

/* Sticky Header Shadow */
function initStickyHeader() {
  const header = document.querySelector('.header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 15) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* Real-Time Live Search & Category Chip Filter */
function initLiveSearchAndFilter() {
  const searchInput = document.getElementById('articleSearch');
  const catButtons = document.querySelectorAll('.cat-btn');
  const articleCards = document.querySelectorAll('.article-card');

  if (!articleCards.length) return;

  let currentCategory = 'all';
  let searchQuery = '';

  function filterCards() {
    articleCards.forEach(card => {
      const cardTitle = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const cardExcerpt = (card.querySelector('.card-excerpt')?.textContent || '').toLowerCase();
      const cardCategories = (card.getAttribute('data-categories') || '').toLowerCase();

      const matchesSearch = !searchQuery || cardTitle.includes(searchQuery) || cardExcerpt.includes(searchQuery);
      const matchesCategory = currentCategory === 'all' || cardCategories.includes(currentCategory.toLowerCase());

      if (matchesSearch && matchesCategory) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      filterCards();
    });
  }

  catButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      catButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.getAttribute('data-category') || 'all';
      filterCards();
    });
  });
}

/* Newsletter Feedback */
function initNewsletter() {
  const form = document.getElementById('newsletterForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input[type="email"]');
    if (input && input.value) {
      const originalText = form.querySelector('button').textContent;
      form.querySelector('button').textContent = 'Subscribed! 🎉';
      input.value = '';
      setTimeout(() => {
        form.querySelector('button').textContent = originalText;
      }, 3500);
    }
  });
}
"""

def generate_index_html(name, niche, tagline, author, categories, palette):
    cat_buttons_html = '<button class="cat-btn active" data-category="all">All</button>\n'
    for cat in categories:
        cat_slug = cat.lower().replace(" ", "-")
        cat_buttons_html += f'        <button class="cat-btn" data-category="{cat_slug}">{cat}</button>\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>{name} | {tagline}</title>
  <meta name="description" content="{tagline}. Read the latest guides, reviews, and insights on {niche}.">
  <meta name="author" content="{author}">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{name} | {tagline}">
  <meta property="og:description" content="{tagline}. Read the latest guides and reviews on {niche}.">
  <meta property="og:image" content="./assets/placeholder.webp">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{name} | {tagline}">
  <meta name="twitter:description" content="{tagline}">
  <meta name="twitter:image" content="./assets/placeholder.webp">

  <!-- Preconnect Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="icon" type="image/svg+xml" href="./assets/favicon.svg">
  <link rel="stylesheet" href="./css/style.css">
</head>
<body>

  <!-- HEADER / NAVBAR -->
  <header class="header glass-panel">
    <div class="container navbar">
      <a href="./index.html" class="logo">
        <i class="fa-solid fa-bolt" style="color: var(--accent-color);"></i>
        <span>{name}</span>
      </a>
      
      <nav class="nav-links" id="navLinks">
        <a href="./index.html" class="active">Home</a>
        <a href="./about.html">About</a>
        <a href="./contact.html">Contact</a>
      </nav>
      
      <div class="nav-controls">
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">
          <i class="fa-solid fa-moon moon-icon"></i>
          <i class="fa-solid fa-sun sun-icon"></i>
        </button>
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Open menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="hero-section container">
    <div class="hero-grid">
      <div class="hero-content">
        <span class="hero-tag"><i class="fa-solid fa-star"></i> Featured Guide</span>
        <h1 class="hero-title">Welcome to {name}</h1>
        <p class="hero-description">{tagline}. We publish tested recommendations, in-depth breakdowns, and curated roundups for {niche} enthusiasts.</p>
        <a href="#articles" class="btn btn-primary">Explore Guides <i class="fa-solid fa-arrow-down"></i></a>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/placeholder.webp" alt="{name} Hero Image" loading="eager">
      </div>
    </div>
  </section>

  <!-- FILTER & SEARCH -->
  <section class="container" id="articles">
    <div class="filter-section">
      <div class="search-wrapper">
        <i class="fa-solid fa-magnifying-glass search-icon"></i>
        <input type="text" class="search-input" id="articleSearch" placeholder="Search guides, roundups, and topics...">
      </div>
      
      <div class="category-chips">
        {cat_buttons_html}
      </div>
    </div>
  </section>

  <!-- ARTICLES GRID -->
  <main class="container">
    <div class="article-grid" id="articleGrid">
      <!-- Starter Sample Article -->
      <article class="article-card" data-categories="{categories[0].lower().replace(' ', '-')}">
        <div class="card-image-wrap">
          <span class="card-badge">{categories[0]}</span>
          <img src="./assets/placeholder.webp" alt="Sample Article" loading="lazy">
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span><i class="fa-regular fa-calendar"></i> Just Now</span>
            <span>&bull;</span>
            <span><i class="fa-regular fa-clock"></i> 5 min read</span>
          </div>
          <h2 class="card-title">
            <a href="./articles/welcome-guide.html">Getting Started with {niche}: The Ultimate Playbook</a>
          </h2>
          <p class="card-excerpt">
            Everything you need to know to master {niche} from day one. In-depth tips, essential gear, and core strategies.
          </p>
          <div class="card-footer">
            <span>By {author}</span>
            <a href="./articles/welcome-guide.html" class="read-link">Read Full Guide <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </article>
    </div>
  </main>

  <!-- NEWSLETTER -->
  <section class="container">
    <div class="newsletter-section">
      <h2 class="newsletter-title">Join the {name} Dispatch</h2>
      <p class="newsletter-desc">Get our weekly roundup of the best {niche} insights, reviews, and private tips straight to your inbox.</p>
      <form class="newsletter-form" id="newsletterForm">
        <input type="email" class="newsletter-input" placeholder="Enter your email..." required>
        <button type="submit" class="btn btn-primary">Subscribe</button>
      </form>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <div class="logo">
          <i class="fa-solid fa-bolt" style="color: var(--accent-color);"></i>
          <span>{name}</span>
        </div>
        <p class="footer-desc">{tagline}. Honest advice, curated listicles, and deep dives.</p>
      </div>
      <div>
        <h4 class="footer-links-title">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="./index.html">Home</a></li>
          <li><a href="./about.html">About Us</a></li>
          <li><a href="./contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 class="footer-links-title">Legal</h4>
        <ul class="footer-links">
          <li><a href="./privacy.html">Privacy Policy</a></li>
          <li><a href="./terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; 2026 {name}. All rights reserved.</p>
      <p>Built with high-speed static architecture.</p>
    </div>
  </footer>

  <script src="./js/main.js"></script>
</body>
</html>
"""

def generate_sample_article(name, niche, author, category):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Getting Started with {niche}: The Ultimate Playbook | {name}</title>
  <meta name="description" content="A comprehensive beginner guide to mastering {niche}. Learn essential foundations, best practices, and expert recommendations.">
  <meta name="author" content="{author}">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="Getting Started with {niche}: The Ultimate Playbook">
  <meta property="og:description" content="A comprehensive beginner guide to mastering {niche}.">
  <meta property="og:image" content="../assets/placeholder.webp">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "Getting Started with {niche}: The Ultimate Playbook",
    "description": "A comprehensive beginner guide to mastering {niche}.",
    "author": {{
      "@type": "Person",
      "name": "{author}"
    }},
    "datePublished": "2026-09-08",
    "image": "../assets/placeholder.webp"
  }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

  <!-- HEADER -->
  <header class="header glass-panel">
    <div class="container navbar">
      <a href="../index.html" class="logo">
        <i class="fa-solid fa-bolt" style="color: var(--accent-color);"></i>
        <span>{name}</span>
      </a>
      <nav class="nav-links" id="navLinks">
        <a href="../index.html">Home</a>
        <a href="../about.html">About</a>
        <a href="../contact.html">Contact</a>
      </nav>
      <div class="nav-controls">
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
          <i class="fa-solid fa-moon moon-icon"></i>
          <i class="fa-solid fa-sun sun-icon"></i>
        </button>
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- ARTICLE CONTAINER -->
  <main class="container" style="max-width: 800px; padding-top: 3rem; margin-bottom: 5rem;">
    <article>
      <span class="hero-tag">{category}</span>
      <h1 style="font-size: 2.4rem; margin: 1rem 0 1rem;">Getting Started with {niche}: The Ultimate Playbook</h1>
      
      <div style="display: flex; gap: 1rem; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem;">
        <span>By <strong>{author}</strong></span>
        <span>&bull;</span>
        <span>5 min read</span>
        <span>&bull;</span>
        <span>Updated September 2026</span>
      </div>

      <div style="border-radius: var(--radius-md); overflow: hidden; margin-bottom: 2.5rem;">
        <img src="../assets/placeholder.webp" alt="{niche} guide banner" style="width: 100%;">
      </div>

      <div style="background: var(--accent-light); padding: 1.5rem; border-radius: var(--radius-md); margin-bottom: 2rem; border-left: 4px solid var(--accent-color);">
        <h4 style="margin-bottom: 0.5rem; color: var(--accent-color); font-size: 1.1rem;"><i class="fa-solid fa-lightbulb"></i> Key Takeaways</h4>
        <ul style="padding-left: 1.25rem; color: var(--text-primary); line-height: 1.7;">
          <li>Mastering {niche} starts with clear fundamentals rather than expensive gear or shortcuts.</li>
          <li>Consistency and structured testing yield the highest return on investment.</li>
          <li>Follow our step-by-step roadmap below to bypass common beginner pitfalls.</li>
        </ul>
      </div>

      <section style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary); display: flex; flex-direction: column; gap: 1.5rem;">
        <p>Entering the world of <strong>{niche}</strong> can be daunting with the flood of conflicting opinions, trendy gimmicks, and information overload. Whether you are completely brand new or looking to refine your methodology, having a reliable roadmap is paramount.</p>

        <h2 style="color: var(--text-primary); margin-top: 1.5rem;">1. Understand the Core Foundations</h2>
        <p>Before diving into advanced techniques, focus 80% of your energy on foundational principles. Identify what truly drives 80% of your results in {niche}. Keep notes on what works and what doesn't.</p>

        <h2 style="color: var(--text-primary); margin-top: 1.5rem;">2. Eliminate the Most Common Pitfalls</h2>
        <p>Most beginners fail not from lack of enthusiasm, but from inconsistency and overcomplicating their setup. Start with minimal friction and scale up your efforts as your confidence builds.</p>

        <h2 style="color: var(--text-primary); margin-top: 1.5rem;">3. Next Steps & Recommended Resources</h2>
        <p>Stay tuned to {name} as we break down detailed product comparisons, step-by-step tutorials, and expert interviews every week.</p>
      </section>
    </article>
  </main>

  <footer class="footer">
    <div class="container footer-bottom">
      <p>&copy; 2026 {name}. All rights reserved.</p>
      <a href="../index.html" class="read-link">Back to Home &rarr;</a>
    </div>
  </footer>

  <script src="../js/main.js"></script>
</body>
</html>
"""

def generate_svg_favicon():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="46" fill="#4f46e5" />
  <path d="M50 20 L30 55 L48 55 L40 82 L70 45 L52 45 Z" fill="#ffffff" />
</svg>"""

def main():
    parser = argparse.ArgumentParser(description="Scaffold a complete static niche blog.")
    parser.add_argument("--name", default="Apex Guide", help="Blog Name")
    parser.add_argument("--niche", default="Tech & Gadgets", help="Niche Focus")
    parser.add_argument("--tagline", default="Field-tested recommendations, curated listicles, and deep dives", help="Blog Tagline")
    parser.add_argument("--author", default="Editorial Team", help="Author Name")
    parser.add_argument("--palette", default="tech_indigo", help="Palette preset name")
    parser.add_argument("--categories", default="Reviews,Guides,Top Picks,Tips", help="Comma-separated categories")
    parser.add_argument("--output", default=".", help="Target output directory")

    args = parser.parse_args()

    out_dir = os.path.abspath(args.output)
    resources_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    palette = get_palette(args.palette, resources_dir)
    categories = [c.strip() for c in args.categories.split(",") if c.strip()]

    print(f"[*] Scaffolding '{args.name}' ({args.niche}) in: {out_dir}")

    # Make folders
    os.makedirs(os.path.join(out_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "js"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "articles"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "assets"), exist_ok=True)

    # 1. css/style.css
    with open(os.path.join(out_dir, "css", "style.css"), "w", encoding="utf-8") as f:
        f.write(generate_css(palette))

    # 2. js/main.js
    with open(os.path.join(out_dir, "js", "main.js"), "w", encoding="utf-8") as f:
        f.write(generate_js())

    # 3. index.html
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_index_html(args.name, args.niche, args.tagline, args.author, categories, palette))

    # 4. starter article
    with open(os.path.join(out_dir, "articles", "welcome-guide.html"), "w", encoding="utf-8") as f:
        f.write(generate_sample_article(args.name, args.niche, args.author, categories[0]))

    # 5. assets/favicon.svg
    with open(os.path.join(out_dir, "assets", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(generate_svg_favicon())

    # 6. articles_database.json
    starter_db = [
        {
            "id": "welcome-guide",
            "title": f"Getting Started with {args.niche}: The Ultimate Playbook",
            "slug": "welcome-guide",
            "category": categories[0],
            "categories_str": f"all {categories[0].lower().replace(' ', '-')}",
            "read_time": "5 min read",
            "author": args.author,
            "type": "single_article",
            "date": "2026-09-08",
            "image": "./assets/placeholder.webp",
            "excerpt": f"Everything you need to know to master {args.niche} from day one. In-depth tips, essential gear, and core strategies."
        }
    ]
    with open(os.path.join(out_dir, "articles_database.json"), "w", encoding="utf-8") as f:
        json.dump(starter_db, f, indent=2)

    # 7. robots.txt
    with open(os.path.join(out_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://yoursite.com/sitemap.xml\n")

    # 8. sitemap.xml
    with open(os.path.join(out_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yoursite.com/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://yoursite.com/articles/welcome-guide.html</loc>
    <priority>0.8</priority>
  </url>
</urlset>
""")

    print("[+] Blog scaffolding completed successfully!")

if __name__ == "__main__":
    main()
