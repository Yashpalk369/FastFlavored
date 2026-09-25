import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "20-minute-sheet-pan-chicken-shawarma",
        "title": "20-Minute Sheet-Pan Crispy Chicken Shawarma Bowls with Garlic White Sauce",
        "headline": "20-Minute Sheet-Pan Chicken Shawarma Bowls (Halal Cart Style at Home)",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/sheet-pan-chicken-shawarma.jpg",
        "image_file": "sheet-pan-chicken-shawarma.jpg",
        "excerpt": "Juicy, caramelized spiced chicken thigh strips roasted with charred red onions, cherry tomatoes, warm pita triangles, and drizzled with creamy NYC street-cart garlic white sauce in 20 minutes.",
        "description": "Recreate NYC halal cart magic at home in 20 minutes: tender chicken thighs rubbed with cumin, coriander, turmeric, and smoked paprika, roasted to crispy charred perfection on one pan with garlic white sauce.",
        "keywords": "sheet pan chicken shawarma, halal cart chicken, 20 minute chicken dinner, easy sheet pan dinner, street cart white sauce, middle eastern chicken",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Middle Eastern / Mediterranean",
        "calories": "480 kcal",
        "protein": "38g",
        "fat": "24g",
        "carbs": "28g",
        "fiber": "3g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "188",
        "quick_answer": "To make 20-minute sheet-pan chicken shawarma, slice 1.5 lbs boneless skinless chicken thighs into thin strips and toss with 2 tbsp olive oil, 1 tsp cumin, 1 tsp coriander, 1 tsp smoked paprika, 1/2 tsp turmeric, 1/2 tsp garlic powder, salt, and juice of 1 lemon. Spread onto a baking sheet alongside 1 sliced red onion and 1 cup cherry tomatoes. Roast at 425°F (220°C) for 14 minutes, broiling for the last 2 minutes until edges are deeply charred. Whisk 1/2 cup Greek yogurt, 2 tbsp mayo, 2 grated garlic cloves, 1 tbsp lemon juice, and a pinch of sugar; drizzle over hot chicken and serve with warm pita.",
        "takeaways": [
            ("Chicken Thigh Moisture Shield", "Boneless skinless chicken thighs have enough intramuscular fat to withstand high-heat 425°F roasting without drying out, delivering juicy street-cart texture."),
            ("Turmeric & Paprika Char Base", "Ground turmeric and smoked paprika form a signature golden-orange crust that chars into savory roasted bits under the broiler."),
            ("Yogurt-Mayo White Sauce Emulsion", "Combining whole milk Greek yogurt with real mayonnaise creates the authentic velvety texture and tang of New York street cart white sauce.")
        ],
        "matrix_title": "Chicken Cut Performance for Sheet-Pan Shawarma",
        "matrix_headers": ["Chicken Cut", "Juiciness Level", "Char Potential", "Bake Time", "Verdict"],
        "matrix_rows": [
            ["Boneless Skinless Thighs", "Maximum (never dries out)", "Deep, crispy caramelized edges", "14–15 minutes", "Gold Standard Winner (Recommended)"],
            ["Boneless Chicken Breasts", "Moderate (watch closely)", "Good char", "12 minutes (overcooks fast)", "Good lean alternative"],
            ["Chicken Tenderloins", "Tender", "Moderate", "10–12 minutes", "Fast weeknight alternative"],
            ["Bone-In Chicken Thighs", "High", "Skin crisps nicely", "25–30 minutes", "Too slow for 20-minute dinner"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken thighs, sliced into 1/2-inch strips",
            "1 medium red onion, sliced into thin wedges",
            "1.5 cups cherry or grape tomatoes",
            "2 tbsp extra virgin olive oil (divided)",
            "Juice of 1 large organic lemon",
            "4 cloves garlic, minced (divided)",
            "1.5 tsp ground cumin",
            "1.5 tsp smoked paprika",
            "1 tsp ground coriander",
            "1/2 tsp ground turmeric",
            "1/4 tsp ground cinnamon & cayenne pepper",
            "1/2 cup whole-milk Greek yogurt",
            "2 tbsp real mayonnaise",
            "1 tbsp white vinegar or fresh lemon juice (for sauce)",
            "1/2 tsp dried oregano or sumac",
            "Warm pita bread triangles, for serving",
            "Fresh flat-leaf parsley, chopped"
        ],
        "instructions": [
            ("Preheat Oven & Season Chicken", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper or heavy foil. In a large bowl, toss sliced chicken thighs with 1.5 tbsp olive oil, lemon juice, half the minced garlic, cumin, smoked paprika, coriander, turmeric, cinnamon, cayenne, 1 tsp salt, and 1/2 tsp black pepper until thoroughly coated."),
            ("Arrange on Sheet Pan", "Spread the seasoned chicken strips in a single layer across the baking sheet. Scatter sliced red onions and whole cherry tomatoes around the chicken. Drizzle vegetables with remaining 1/2 tbsp olive oil and a pinch of salt."),
            ("Roast & Broil to Crispy Char", "Roast at 425°F for 12–14 minutes until chicken is cooked through (165°F). Switch oven to High Broil for the final 2 minutes, watching closely until chicken edges are sizzled, crackled, and deeply caramelized."),
            ("Whisk NYC Halal White Sauce", "While chicken roasts, whisk Greek yogurt, mayonnaise, remaining minced garlic, white vinegar, dried oregano, 1/2 tsp sugar, and a pinch of salt in a small bowl until smooth and pourable."),
            ("Assemble & Serve", "Tuck warm pita bread triangles onto the sheet pan or platter. Drizzle the creamy garlic white sauce generously over the sizzling chicken and burst tomatoes. Sprinkle with fresh chopped parsley and a dusting of sumac. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s 2-Minute High-Broil Char Hack",
        "pro_tip": "Authentic shawarma gets its legendary flavor from the rotating vertical spit that chars the edges of the meat over open fire. To replicate this on a weeknight sheet pan, don't just bake: always switch to HIGH BROIL for the final 120 seconds of cooking! The spices and chicken fat will blister and sizzle into dark, crispy edges that taste identical to a five-star street cart.",
        "faqs": [
            ("Can I make this in the air fryer?", "Yes! Air fry the chicken strips and onions at 400°F for 10–12 minutes, shaking the basket halfway through until charred and crispy."),
            ("What should I serve with chicken shawarma bowls?", "Serve over yellow turmeric jasmine rice, spiced basmati rice, or alongside a fresh chopped cucumber tomato salad and warm garlic naan."),
            ("How do I store and reheat leftovers?", "Store chicken and white sauce in separate airtight glass containers for up to 4 days. Reheat chicken in a skillet or air fryer to restore the crispy charred edges.")
        ],
        "wiki_entities": [
            ("Shawarma", "https://en.wikipedia.org/wiki/Shawarma"),
            ("Halal cart", "https://en.wikipedia.org/wiki/The_Halal_Guys"),
            ("Tahini", "https://en.wikipedia.org/wiki/Tahini")
        ],
        "pinterest": {
            "board": "Sheet Pan Meals / Mediterranean Recipes",
            "title": "20-Minute Sheet-Pan Crispy Chicken Shawarma Recipe (Halal Cart Style!)",
            "desc": "Juicy, caramelized spiced chicken thighs roasted on one sheet pan with charred red onions, burst tomatoes, warm pita, and drizzled with street-cart garlic white sauce in 20 minutes! Save this viral weeknight dinner now!",
            "tags": "#chickenshawarma #sheetpanmeals #20minutedinner #halalcart #mediterraneandiet #easyweeknightdinner #dinnerideas"
        }
    }
]

def generate_article_html(r):
    howto_steps = []
    for step_title, step_text in r["instructions"]:
        howto_steps.append({
            "@type": "HowToStep",
            "name": step_title,
            "text": step_text
        })

    faq_entities = []
    for q, a in r["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    about_entities = []
    for name, same_as in r.get("wiki_entities", []):
        about_entities.append({
            "@type": "Thing",
            "name": name,
            "sameAs": same_as
        })

    recipe_json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Recipe",
                "@id": f"https://fastflavored.com/articles/{r['slug']}.html#recipe",
                "name": r["title"],
                "headline": r["headline"],
                "description": r["description"],
                "image": f"https://fastflavored.com/assets/images/{r['image_file']}",
                "author": {
                    "@type": "Person",
                    "name": "Elena Bennett"
                },
                "datePublished": r["date"],
                "prepTime": r["prepTime"],
                "cookTime": r["cookTime"],
                "totalTime": r["totalTime"],
                "recipeYield": r["recipeYield"],
                "recipeCategory": r["recipeCategory"],
                "recipeCuisine": r["recipeCuisine"],
                "keywords": r["keywords"],
                "nutrition": {
                    "@type": "NutritionInformation",
                    "calories": r["calories"],
                    "fatContent": r["fat"],
                    "saturatedFatContent": "8 g",
                    "proteinContent": r["protein"],
                    "carbohydrateContent": r["carbs"],
                    "fiberContent": r["fiber"],
                    "sodiumContent": r["sodium"]
                },
                "recipeIngredient": r["ingredients"],
                "recipeInstructions": howto_steps,
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": r["ratingValue"],
                    "reviewCount": r["reviewCount"]
                },
                "about": about_entities
            },
            {
                "@type": "FAQPage",
                "@id": f"https://fastflavored.com/articles/{r['slug']}.html#faq",
                "mainEntity": faq_entities
            }
        ]
    }

    headers_html = "".join([f"<th>{h}</th>" for h in r["matrix_headers"]])
    rows_html = ""
    for row in r["matrix_rows"]:
        cells = [f"<td><strong>{cell}</strong></td>" if i == 0 or "Recommended" in cell else f"<td>{cell}</td>" for i, cell in enumerate(row)]
        rows_html += f"<tr>{''.join(cells)}</tr>\n"

    ing_html = ""
    for i, ing in enumerate(r["ingredients"], 1):
        ing_id = f"ing_{r['slug'][:4]}_{i}"
        ing_html += f'<li><input type="checkbox" id="{ing_id}"><label for="{ing_id}">{ing}</label></li>\n'

    inst_html = ""
    for title, text in r["instructions"]:
        inst_html += f"<li><strong>{title}:</strong> {text}</li>\n"

    takeaways_html = ""
    for title, desc in r["takeaways"]:
        takeaways_html += f"<li><strong>{title}:</strong> {desc}</li>\n"

    faqs_html = ""
    for q, a in r["faqs"]:
        faqs_html += f"""
          <div class="faq-item" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden;">
            <div class="faq-question" style="padding: 1.25rem; font-weight: 700; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
              <span>{q}</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer" style="padding: 0 1.25rem 1.25rem; color: var(--text-secondary); font-size: 1rem;">
              {a}
            </div>
          </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-MBPEDTLCPJ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-MBPEDTLCPJ');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Pinterest Domain Verification -->
  <meta name="p:domain_verify" content="08c552b8c75f9a024d0b29a5c8de9474"/>
  
  <title>{r['title']} | FastFlavored</title>
  <meta name="description" content="{r['excerpt']}">
  <meta name="author" content="Elena Bennett">
  <link rel="canonical" href="https://fastflavored.com/articles/{r['slug']}.html">
  <meta name="robots" content="max-image-preview:large, max-snippet:-1">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{r['headline']}">
  <meta property="og:description" content="{r['excerpt']}">
  <meta property="og:image" content="../assets/images/{r['image_file']}">
  <meta property="og:url" content="https://fastflavored.com/articles/{r['slug']}.html">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{r['headline']}">
  <meta name="twitter:description" content="{r['excerpt']}">
  <meta name="twitter:image" content="../assets/images/{r['image_file']}">

  <!-- Schema.org Recipe + FAQPage JSON-LD -->
  <script type="application/ld+json">
{json.dumps(recipe_json_ld, indent=2)}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
  <link rel="stylesheet" href="../css/style.css?v=2.1">

  <style>
    .article-layout {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 3.5rem;
      align-items: start;
    }}
    .sticky-toc {{
      position: sticky;
      top: 90px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
    }}
    .toc-list {{
      list-style: none;
      padding: 0;
      margin: 1rem 0 0;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      font-size: 0.9rem;
    }}
    .toc-list a {{
      color: var(--text-secondary);
      transition: color var(--transition);
    }}
    .toc-list a:hover {{
      color: var(--accent-color);
    }}
    @media (max-width: 960px) {{
      .article-layout {{
        grid-template-columns: 1fr;
        gap: 2rem;
      }}
      .sticky-toc {{
        position: relative;
        top: 0;
      }}
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header class="header glass-panel">
    <div class="container navbar">
      <a href="../index.html" class="logo">
        <i class="fa-solid fa-utensils" style="color: var(--accent-color);"></i>
        <span>FastFlavored</span>
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
  <div class="container" style="padding-top: 2.5rem; margin-bottom: 5rem;">
    
    <!-- Hero Header -->
    <div style="max-width: 900px; margin: 0 auto 2.5rem;">
      <span class="card-badge">{r['badge']}</span>
      <h1 style="font-size: 2.8rem; margin: 1rem 0 0.75rem;">{r['title']}</h1>
      <p style="font-size: 1.25rem; color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.6;">
        {r['description']}
      </p>

      <div style="display: flex; gap: 1.25rem; align-items: center; flex-wrap: wrap; color: var(--text-muted); font-size: 0.95rem;">
        <span>By <strong>Elena Bennett</strong></span>
        <span>&bull;</span>
        <span><i class="fa-regular fa-clock"></i> {r['read_time']}</span>
        <span>&bull;</span>
        <span><i class="fa-solid fa-fire" style="color: var(--accent-color);"></i> {r['calories']} &bull; {r['protein']} Protein</span>
      </div>

      <div class="recipe-quick-actions">
        <a href="#recipe-card" class="btn-jump">
          <i class="fa-solid fa-arrow-down"></i> Jump to Recipe
        </a>
        <button class="btn-outline btn-print">
          <i class="fa-solid fa-print"></i> Print Recipe
        </button>
      </div>
    </div>

    <!-- Layout: TOC + Body -->
    <div class="article-layout">
      <!-- Sticky Sidebar TOC -->
      <aside class="sticky-toc">
        <h4 style="font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem; margin: 0;">
          <i class="fa-solid fa-list" style="color: var(--accent-color);"></i> Table of Contents
        </h4>
        <ul class="toc-list">
          <li><a href="#quick-answer">Quick Answer &amp; Overview</a></li>
          <li><a href="#comparison-matrix">Ingredient &amp; Technique Matrix</a></li>
          <li><a href="#recipe-card">Printable Recipe Card</a></li>
          <li><a href="#pro-tips">Elena’s Chef Pro-Tip</a></li>
          <li><a href="#faqs">Frequently Asked Questions</a></li>
        </ul>
      </aside>

      <!-- Main Editorial Body -->
      <main style="max-width: 800px; font-size: 1.15rem; line-height: 1.85; color: var(--text-secondary);">

        <!-- AEO Direct-Answer Box -->
        <div class="aeo-answer-box" id="quick-answer">
          <strong style="color: var(--accent-color); display: block; font-size: 1.1rem; margin-bottom: 0.4rem;">
            <i class="fa-solid fa-bolt"></i> Bottom Line Up Front (Quick Answer):
          </strong>
          <p style="margin: 0; color: var(--text-primary);">
            {r['quick_answer']}
          </p>
        </div>

        <!-- Real Food Photo -->
        <div style="border-radius: var(--radius-lg); overflow: hidden; margin-bottom: 2.5rem; box-shadow: var(--shadow-md);">
          <img src="../assets/images/{r['image_file']}" alt="{r['title']}" style="width: 100%; height: auto;">
        </div>

        <!-- Key Takeaways Box -->
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.75rem; margin-bottom: 2.5rem;">
          <h3 style="font-size: 1.3rem; margin-bottom: 1rem; color: var(--text-primary); display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-wand-magic-sparkles" style="color: var(--accent-color);"></i> Why This Recipe Conquers Weeknights
          </h3>
          <ul style="padding-left: 1.25rem; display: flex; flex-direction: column; gap: 0.6rem; color: var(--text-primary);">
            {takeaways_html}
          </ul>
        </div>

        <h2 id="comparison-matrix" style="color: var(--text-primary); margin-top: 2rem;">{r['matrix_title']}</h2>
        <div class="comparison-table-wrapper">
          <table class="comparison-table" data-comparison="true">
            <thead>
              <tr>
                {headers_html}
              </tr>
            </thead>
            <tbody>
              {rows_html}
            </tbody>
          </table>
        </div>

        <!-- RECIPE CARD -->
        <div class="recipe-box" id="recipe-card">
          <div class="recipe-header">
            <div>
              <span class="card-badge" style="margin-bottom: 0.5rem; display: inline-block;">Official FastFlavored Recipe</span>
              <h2 style="font-size: 2rem; margin: 0.25rem 0;">{r['title']}</h2>
              <p style="color: var(--text-muted); font-size: 0.95rem; margin: 0;">Tested and approved by Elena Bennett &bull; Serves 4</p>
            </div>
            <button class="btn-print" aria-label="Print Recipe Card">
              <i class="fa-solid fa-print"></i> Print Recipe
            </button>
          </div>

          <div class="recipe-meta-grid">
            <div class="recipe-meta-item">
              <span>Prep Time</span>
              <strong>{r['prepTime'].replace('PT', '').replace('M', ' Mins')}</strong>
            </div>
            <div class="recipe-meta-item">
              <span>Cook Time</span>
              <strong>{r['cookTime'].replace('PT', '').replace('M', ' Mins')}</strong>
            </div>
            <div class="recipe-meta-item">
              <span>Total Time</span>
              <strong>{r['totalTime'].replace('PT', '').replace('M', ' Mins')}</strong>
            </div>
            <div class="recipe-meta-item">
              <span>Yield</span>
              <strong>{r['recipeYield']}</strong>
            </div>
            <div class="recipe-meta-item">
              <span>Calories</span>
              <strong>{r['calories']}</strong>
            </div>
          </div>

          <div class="recipe-columns">
            <!-- Ingredients -->
            <div>
              <h3 style="font-size: 1.3rem; margin-bottom: 1rem; color: var(--text-primary); display: flex; align-items: center; gap: 0.5rem;">
                <i class="fa-solid fa-basket-shopping" style="color: var(--accent-color);"></i> Ingredients
              </h3>
              <ul class="ingredients-list">
                {ing_html}
              </ul>
            </div>

            <!-- Instructions -->
            <div>
              <h3 style="font-size: 1.3rem; margin-bottom: 1rem; color: var(--text-primary); display: flex; align-items: center; gap: 0.5rem;">
                <i class="fa-solid fa-fire-burner" style="color: var(--accent-color);"></i> Step-by-Step Instructions
              </h3>
              <ol class="instructions-list">
                {inst_html}
              </ol>
            </div>
          </div>

          <!-- Nutrition Breakdown -->
          <div class="nutrition-grid">
            <div><strong>{r['calories'].replace(' kcal', '')}</strong><span>Calories</span></div>
            <div><strong>{r['protein']}</strong><span>Protein</span></div>
            <div><strong>{r['fat']}</strong><span>Total Fat</span></div>
            <div><strong>{r['carbs']}</strong><span>Carbs</span></div>
            <div><strong>{r['fiber']}</strong><span>Fiber</span></div>
            <div><strong>{r['sodium']}</strong><span>Sodium</span></div>
          </div>
        </div>

        <h2 id="pro-tips" style="color: var(--text-primary); margin-top: 2.5rem;">{r['pro_tip_title']}</h2>
        <div class="pro-tip-box">
          <strong><i class="fa-solid fa-lightbulb"></i> Chef Secret:</strong>
          {r['pro_tip']}
        </div>

        <!-- FAQ Section -->
        <h2 id="faqs" style="color: var(--text-primary); margin-top: 3rem;">Frequently Asked Questions</h2>
        <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1.5rem;">
          {faqs_html}
        </div>

      </main>
    </div>
  </div>

  <!-- NEWSLETTER -->
  <section class="container">
    <div class="newsletter-section">
      <h2 class="newsletter-title">Get 5 Fast Dinners Every Sunday</h2>
      <p class="newsletter-desc">Join 28,000+ busy home cooks who receive our weekly dinner meal plan, shopping checklist, and 30-minute recipes.</p>
      <form class="newsletter-form" id="newsletterForm">
        <input type="email" class="newsletter-input" placeholder="Enter your email address..." required>
        <button type="submit" class="btn btn-primary">Send My Dinners</button>
      </form>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <div class="logo">
          <i class="fa-solid fa-utensils" style="color: var(--accent-color);"></i>
          <span>FastFlavored</span>
        </div>
        <p class="footer-desc">Simple, Delicious 30-Minute Weeknight Dinners for Real Life. Triple-tested recipes with minimal sink cleanup.</p>
      </div>
      <div>
        <h4 class="footer-links-title">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="../index.html">Home</a></li>
          <li><a href="../about.html">About Us</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 class="footer-links-title">Legal &amp; Safety</h4>
        <ul class="footer-links">
          <li><a href="../privacy.html">Privacy Policy</a></li>
          <li><a href="../terms.html">Terms &amp; Food Disclaimer</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; 2026 FastFlavored. All rights reserved.</p>
      <p>High-speed zero-build culinary architecture.</p>
    </div>
  </footer>

  <script src="../js/main.js?v=2.1"></script>
  <script>
    // FAQ Accordion
    document.querySelectorAll('.faq-question').forEach(q => {{
      q.addEventListener('click', () => {{
        const item = q.parentElement;
        item.classList.toggle('active');
        const icon = q.querySelector('i');
        if (icon) {{
          icon.classList.toggle('fa-chevron-up');
          icon.classList.toggle('fa-chevron-down');
        }}
      }});
    }});

    // Print Button
    document.querySelectorAll('.btn-print').forEach(btn => {{
      btn.addEventListener('click', () => window.print());
    }});
  </script>
</body>
</html>
"""
    return html

def main():
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 5) ===")
    os.makedirs(ARTICLES_DIR, exist_ok=True)

    # 1. Generate HTML articles
    for r in NEW_RECIPES:
        file_path = os.path.join(ARTICLES_DIR, f"{r['slug']}.html")
        html_content = generate_article_html(r)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[+] Created article: {file_path}")

    # 2. Update articles_database.json
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    existing_slugs = {item["slug"] for item in db}
    new_db_entries = []
    for r in NEW_RECIPES:
        if r["slug"] not in existing_slugs:
            new_db_entries.append({
                "id": r["slug"],
                "title": r["title"],
                "slug": r["slug"],
                "category": r["category"],
                "categories_str": r["categories_str"],
                "read_time": r["read_time"],
                "author": "Elena Bennett",
                "type": "recipe",
                "date": r["date"],
                "image": r["image"],
                "excerpt": r["excerpt"]
            })

    updated_db = new_db_entries + db
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(updated_db, f, indent=2)
    print(f"[+] Prepended {len(new_db_entries)} entries to articles_database.json (Total: {len(updated_db)})")

    # 3. Prepend recipe cards in index.html
    new_cards_html = ""
    for r in NEW_RECIPES:
        badge_text = r["badge"].split("&bull;")[0].strip()
        new_cards_html += f"""
      <!-- Recipe Card: {r['title']} -->
      <article class="article-card" data-categories="{r['categories_str'].replace('all ', '')}">
        <div class="card-image-wrap">
          <span class="card-badge">{badge_text}</span>
          <img src="{r['image']}" alt="{r['title']}" loading="lazy">
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span><i class="fa-solid fa-utensils"></i> {r['category']}</span>
            <span>&bull;</span>
            <span><i class="fa-regular fa-clock"></i> {r['read_time'].replace(' cook', '').capitalize()}</span>
          </div>
          <h2 class="card-title">
            <a href="./articles/{r['slug']}.html">{r['title']}</a>
          </h2>
          <p class="card-excerpt">
            {r['excerpt']}
          </p>
          <div class="card-footer">
            <span>By Elena Bennett</span>
            <a href="./articles/{r['slug']}.html" class="read-link">Get Recipe <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </article>"""

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index_content = f.read()

    grid_start_tag = '<div class="article-grid" id="articleGrid">'
    if grid_start_tag in index_content:
        index_content = index_content.replace(grid_start_tag, f"{grid_start_tag}\n{new_cards_html}")
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("[+] Prepend recipe cards into index.html successfully.")
    else:
        print("[-] Warning: Could not locate articleGrid in index.html")

    # 4. Append to recipe_data.py
    try:
        recipe_data_path = os.path.join(BASE_DIR, "scripts", "recipe_data.py")
        with open(recipe_data_path, "r", encoding="utf-8") as f:
            rd_content = f.read()
        
        target_marker = "RECIPES = ["
        if target_marker in rd_content:
            new_code_snippets = []
            for r in NEW_RECIPES:
                new_code_snippets.append(json.dumps(r, indent=8))
            all_snippets = ",\n    ".join(new_code_snippets) + ",\n"
            rd_content = rd_content.replace(target_marker, f"{target_marker}\n    {all_snippets}")
            with open(recipe_data_path, "w", encoding="utf-8") as f:
                f.write(rd_content)
            print("[+] Appended new recipes into scripts/recipe_data.py")
    except Exception as e:
        print(f"[-] Could not update recipe_data.py: {e}")

if __name__ == "__main__":
    main()
