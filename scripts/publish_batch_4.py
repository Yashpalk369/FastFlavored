import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "15-minute-garlic-butter-corn-shrimp-orzo",
        "title": "15-Minute Creamy Garlic Butter Corn and Shrimp Orzo",
        "headline": "15-Minute Creamy Garlic Butter Corn and Shrimp Orzo (One-Skillet Summer Comfort)",
        "badge": "15-Minute Meals &bull; Coastal Comfort",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/garlic-butter-corn-shrimp-orzo.jpg",
        "image_file": "garlic-butter-corn-shrimp-orzo.jpg",
        "excerpt": "Plump seared jumbo shrimp nestled in creamy, risotto-style garlic butter orzo loaded with sweet blistered corn kernels, fresh basil, and shaved parmesan in 15 minutes.",
        "description": "A 15-minute one-skillet showstopper: tender orzo simmered in sweet corn milk and broth until risotto-creamy, topped with garlic-seared shrimp, summer sweet corn, and ribbons of fresh basil.",
        "keywords": "creamy shrimp orzo, garlic butter shrimp orzo, corn and shrimp skillet, 15 minute seafood dinner, one pot orzo recipe, summer weeknight meals",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Coastal Italian-American",
        "calories": "460 kcal",
        "protein": "32g",
        "fat": "16g",
        "carbs": "48g",
        "fiber": "3g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "141",
        "quick_answer": "To make 15-minute creamy corn and shrimp orzo, sear 1 lb peeled jumbo shrimp in 1 tbsp olive oil and 1 tbsp butter for 2 minutes per side until pink; set aside. In the same skillet, melt 2 tbsp butter with 4 minced garlic cloves and 1.5 cups sweet corn kernels for 2 minutes. Stir in 1 cup dry orzo pasta and toast for 1 minute. Pour in 2.5 cups chicken broth and 1/4 cup heavy cream. Simmer uncovered for 8–9 minutes, stirring frequently until creamy like risotto. Fold in 1/2 cup parmesan and fresh basil, top with seared shrimp, and serve hot.",
        "takeaways": [
            ("Risotto-Style Starch Emulsion", "Cooking dry orzo directly in broth releases natural starches, creating an authentic silky risotto mouthfeel in half the time."),
            ("Sweet Corn Milk Infusion", "Sautéing corn kernels in foaming butter extracts natural corn sugars that season every grain of pasta."),
            ("Two-Minute Shrimp Safeguard", "Seared shrimp are removed before cooking the pasta, preventing overcooking and ensuring plump, juicy bites.")
        ],
        "matrix_title": "Pasta Shapes for 15-Minute Skillet Seafood",
        "matrix_headers": ["Pasta Shape", "Starch Release", "Simmer Time", "Shrimp Integration", "Verdict"],
        "matrix_rows": [
            ["Orzo Pasta", "High (instant creaminess)", "8–9 minutes", "Exceptional (spoons like risotto)", "Gold Standard Winner (Recommended)"],
            ["Ditalini", "Medium-High", "9–10 minutes", "Great spoonable texture", "Fabulous alternative"],
            ["Spaghetti or Linguine", "Medium", "10–12 minutes", "Requires separate twirling", "Lacks risotto-like cohesive texture"],
            ["Angel Hair", "Low", "5 minutes", "Fragile in heavy sauce", "Cooks too fast for corn reduction"]
        ],
        "ingredients": [
            "1 lb raw peeled and deveined jumbo shrimp (16/20 count, pat dry)",
            "1 cup dry orzo pasta",
            "1.5 cups fresh or frozen sweet corn kernels",
            "3 tbsp unsalted butter (divided)",
            "1 tbsp extra virgin olive oil",
            "4 cloves garlic, finely minced",
            "2.5 cups low-sodium chicken or vegetable broth",
            "1/4 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "1/4 cup fresh sweet basil leaves, cut into thin ribbons",
            "Zest and juice of 1/2 organic lemon",
            "Kosher salt & freshly cracked black pepper"
        ],
        "instructions": [
            ("Sear Jumbo Shrimp", "Heat olive oil and 1 tbsp butter in a large 12-inch skillet over medium-high heat. Season shrimp with 1/2 tsp salt and 1/4 tsp pepper. Add shrimp to the hot pan and sear for 2 minutes on the first side, flip and cook 1 minute until pink and opaque. Transfer shrimp to a clean plate."),
            ("Sauté Corn & Garlic", "In the same skillet, melt remaining 2 tbsp butter over medium heat. Add sweet corn kernels and minced garlic; sauté for 2 minutes until corn begins to blister and garlic is fragrant."),
            ("Toast Orzo", "Pour in dry orzo pasta directly into the buttery corn skillet. Stir continuously for 1 minute to lightly toast the grains in the garlic butter."),
            ("Simmer into Creamy Orzotto", "Pour in chicken broth and heavy cream. Bring to a lively simmer, then lower heat to medium-low. Cook uncovered for 8–9 minutes, stirring frequently with a wooden spoon so the orzo doesn't stick, until pasta is al dente and sauce is thick and creamy."),
            ("Fold Cheese & Serve", "Remove skillet from heat. Stir in grated Parmigiano-Reggiano, lemon juice, lemon zest, and half the fresh basil. Arrange the seared shrimp on top, season with cracked black pepper, and garnish with remaining basil ribbons. Serve piping hot!")
        ],
        "pro_tip_title": "Elena’s Frequent-Stir Starch Release Rule",
        "pro_tip": "Treat dry orzo like Italian risotto rice! Frequent stirring with a wooden spoon as the pasta simmers rubs the pasta grains against each other, sloughing off microscopic starch molecules into the broth. Combined with the sweet corn sugars, butter, and cream, this creates an impossibly velvety, mirror-smooth glaze without needing mounds of heavy cream.",
        "faqs": [
            ("Can I make this dairy-free?", "Yes! Replace butter with extra olive oil, substitute canned full-fat coconut milk for heavy cream, and use dairy-free parmesan or nutritional yeast."),
            ("Can I use frozen or canned corn?", "Yes! Frozen sweet corn (especially sweet petite or fire-roasted corn) works brilliantly. If using canned corn, drain and pat dry thoroughly before sautéing."),
            ("Can I use chicken or scallops instead of shrimp?", "Absolutely! Diced chicken breast cutlets or sea scallops sear wonderfully in 2–3 minutes and pair exquisitely with the sweet corn orzo.")
        ],
        "wiki_entities": [
            ("Orzo", "https://en.wikipedia.org/wiki/Orzo"),
            ("Shrimp as food", "https://en.wikipedia.org/wiki/Shrimp_as_food"),
            ("Corn on the cob", "https://en.wikipedia.org/wiki/Corn_on_the_cob")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / One-Pot Dinners",
            "title": "15-Minute Creamy Garlic Butter Corn and Shrimp Orzo (One-Skillet Dinner!)",
            "desc": "Tender orzo cooked risotto-style with sweet summer corn, juicy garlic-seared shrimp, fresh basil, and parmesan in one skillet in 15 minutes! Save this viral weeknight dinner recipe now!",
            "tags": "#shrimporzo #15minutedinner #onepotmeals #seafooddinner #easypasta #summerdinner #creamypasta"
        }
    },
    {
        "slug": "20-minute-crispy-hot-honey-lemon-pepper-chicken",
        "title": "20-Minute Crispy Hot Honey Lemon Pepper Chicken Cutlets",
        "headline": "20-Minute Crispy Hot Honey Lemon Pepper Chicken (Sweet, Zesty & Shatter-Crisp)",
        "badge": "20-Minute Meals &bull; Viral Hit",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/crispy-hot-honey-lemon-pepper-chicken.jpg",
        "image_file": "crispy-hot-honey-lemon-pepper-chicken.jpg",
        "excerpt": "Ultra-crispy panko and cornstarch breaded chicken cutlets pan-fried golden, drenched in an addictive hot honey glaze spiked with cracked black pepper and fresh lemon zest in 20 minutes.",
        "description": "The ultimate flavor trio: shatter-crisp chicken cutlets dredged in lemon pepper seasoning, pan-fried to deep golden crunch, and drizzled in a warm sweet-and-spicy honey butter glaze.",
        "keywords": "hot honey chicken, lemon pepper chicken tenders, crispy hot honey chicken, 20 minute chicken dinner, easy weeknight chicken, hot honey lemon pepper",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American Comfort",
        "calories": "490 kcal",
        "protein": "40g",
        "fat": "20g",
        "carbs": "36g",
        "fiber": "2g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "166",
        "quick_answer": "To make 20-minute crispy hot honey lemon pepper chicken, slice 1.5 lbs chicken breasts into thin cutlets and toss with 1 tbsp lemon pepper seasoning. Dredge cutlets in 1/2 cup cornstarch, then beaten egg, then 1.5 cups seasoned panko breadcrumbs. Pan-fry in 3 tbsp oil over medium-high heat for 3–4 minutes per side until deep golden and 165°F; transfer to a wire rack. In a small pan, warm 1/3 cup honey with 2 tbsp melted butter, 1 tsp hot sauce, 1 tsp coarse black pepper, and juice of half a lemon. Drizzle warm glaze over crispy chicken and garnish with flaky salt.",
        "takeaways": [
            ("Cornstarch-Panko Duo", "Cornstarch creates a glass-like barrier that keeps the chicken juicy, while coarse panko delivers an airy, stay-crisp exterior shell."),
            ("Lemon Pepper Zing Balance", "Citric acid and pungent black pepper in the seasoning cut through sweet wildflower honey, preventing cloying heaviness."),
            ("Wire Rack Rest Technique", "Resting freshly fried cutlets on a wire rack ensures 360-degree air circulation, preventing soggy bottom crusts.")
        ],
        "matrix_title": "Hot Honey Glaze Acid Profiles",
        "matrix_headers": ["Acid Element", "Sharpness", "Sweet-Heat Balance", "Glaze Shine", "Verdict"],
        "matrix_rows": [
            ["Fresh Lemon Juice + Zest", "Bright, aromatic citrus", "Perfect harmony with pepper", "Mirror gloss", "Gold Standard Winner (Recommended)"],
            ["Apple Cider Vinegar", "Sharp, fruity fermented tang", "Southern BBQ profile", "Glossy", "Great bold alternative"],
            ["Hot Sauce (Frank's / Louisiana)", "Direct vinegar heat", "Punchy spicy kick", "Deep amber", "Classic wing-style flavor"],
            ["Balsamic Vinegar", "Sweet & complex", "Darker molasses notes", "Sticky", "Too dark for lemon pepper"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken breasts (halved horizontally into 4 thin cutlets)",
            "1.5 cups panko breadcrumbs",
            "1/2 cup cornstarch",
            "2 large eggs, beaten with 1 tbsp water",
            "1.5 tbsp lemon pepper seasoning blend (salt-free or low-sodium)",
            "1 tsp garlic powder & smoked paprika",
            "1/3 cup pure wildflower honey",
            "2 tbsp unsalted butter",
            "1 tsp red pepper flakes or sriracha",
            "Zest and juice of 1 fresh organic lemon",
            "3 tbsp neutral cooking oil (avocado or vegetable oil)",
            "1 tbsp fresh thyme leaves & flaky Maldon sea salt"
        ],
        "instructions": [
            ("Prep Breading Trio", "Set up three shallow bowls: Bowl 1 with cornstarch, 1/2 tsp salt, and garlic powder; Bowl 2 with beaten eggs; Bowl 3 with panko mixed with lemon pepper seasoning and smoked paprika."),
            ("Dredge Cutlets", "Dredge each chicken cutlet first in cornstarch, shake off excess, dip into egg wash, then press firmly into the lemon pepper panko so crumbs adhere evenly."),
            ("Pan-Fry Until Golden", "Heat oil in a large 12-inch skillet over medium-high heat until shimmering. Add chicken cutlets in a single layer (cook in batches if needed). Fry for 3–4 minutes per side until deeply golden, crispy, and internal temperature reads 165°F. Transfer to an elevated wire rack."),
            ("Warm Hot Honey Glaze", "In a small saucepan over low heat, whisk together honey, melted butter, red pepper flakes (or hot sauce), lemon juice, and lemon zest for 1–2 minutes until warm, fluid, and glossy."),
            ("Glaze & Garnish", "Arrange crispy cutlets on a serving platter. Generously brush or drizzle the warm hot honey glaze over the sizzling chicken. Scatter fresh thyme leaves and flaky sea salt on top. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s 3-Minute Breading Cure",
        "pro_tip": "After pressing your chicken cutlets into the panko, let them rest on a dry plate for 3 full minutes before putting them into hot oil! This brief rest hydrates the cornstarch and egg wash, creating a permanent bond between the meat and the breading so your crust never separates or sloughs off in the skillet.",
        "faqs": [
            ("Can I make this in an air fryer?", "Yes! Preheat air fryer to 390°F. Spray breaded cutlets lightly with cooking spray and air fry for 10–12 minutes, flipping halfway. Drizzle with glaze right before serving."),
            ("What if my lemon pepper seasoning has salt?", "If using a salted lemon pepper blend, omit the added kosher salt in the cornstarch bowl to keep sodium levels perfectly balanced."),
            ("Can I use chicken tenders or bone-in thighs?", "Chicken tenders cook in 6–8 minutes total! For bone-in thighs, bake at 400°F for 25 minutes after crisping.")
        ],
        "wiki_entities": [
            ("Hot honey", "https://en.wikipedia.org/wiki/Hot_honey"),
            ("Lemon pepper", "https://en.wikipedia.org/wiki/Lemon_pepper"),
            ("Fried chicken", "https://en.wikipedia.org/wiki/Fried_chicken")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Chicken Recipes",
            "title": "20-Minute Crispy Hot Honey Lemon Pepper Chicken Recipe (Ultra-Crunchy!)",
            "desc": "Shatter-crisp panko-crusted chicken cutlets pan-fried golden and drenched in warm spicy hot honey lemon pepper glaze with flaky sea salt. Ready in 20 minutes! Save this viral weeknight dinner recipe now!",
            "tags": "#hothoneychicken #lemonpepper #crispychicken #20minutedinner #easyweeknightdinner #chickentenders #viralrecipes"
        }
    },
    {
        "slug": "20-minute-sheet-pan-moroccan-meatballs",
        "title": "20-Minute Sheet-Pan Moroccan Spiced Meatballs with Tahini Herb Sauce",
        "headline": "20-Minute Sheet-Pan Moroccan Spiced Meatballs (Tender, Smoky & Aromatic)",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/sheet-pan-moroccan-meatballs.jpg",
        "image_file": "sheet-pan-moroccan-meatballs.jpg",
        "excerpt": "Caramelized beef and lamb meatballs infused with cumin, coriander, and cinnamon, roasted on one pan with blistered cherry tomatoes, red onions, warm pita, and lemon tahini sauce in 20 minutes.",
        "description": "Juicy, aromatic Moroccan meatballs seasoned with warm Mediterranean spices, roasted on a single sheet pan with sweet cherry tomatoes, red onion ribbons, and warm pita, drizzled with nutty garlic tahini sauce.",
        "keywords": "moroccan meatballs, sheet pan meatballs, tahini sauce meatballs, 20 minute mediterranean dinner, easy sheet pan suppers, quick beef meatballs",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Moroccan / Middle Eastern",
        "calories": "470 kcal",
        "protein": "34g",
        "fat": "26g",
        "carbs": "26g",
        "fiber": "4g",
        "sodium": "590mg",
        "ratingValue": "4.9",
        "reviewCount": "154",
        "quick_answer": "To make 20-minute sheet-pan Moroccan meatballs, combine 1 lb ground beef (or beef/lamb mix) with 1/3 cup panko, 1 egg, 2 minced garlic cloves, 1 tsp cumin, 1 tsp coriander, 1/2 tsp cinnamon, 1/2 tsp paprika, and 1 tsp salt. Roll into 16 meatballs. Arrange on a rimmed baking sheet with 2 cups cherry tomatoes and 1 sliced red onion; toss veggies with 1 tbsp olive oil. Roast at 425°F (220°C) for 14 minutes until meatballs are browned and 160°F internal. Whisk 1/4 cup tahini with 2 tbsp lemon juice and warm water until drizzly, drizzle over meatballs, and serve with warm pita.",
        "takeaways": [
            ("Warm Spice Blend Magic", "Pairing savory cumin and coriander with sweet ground cinnamon delivers intoxicating authentic North African aroma in minutes."),
            ("High-Heat Blistering", "Roasting at 425°F caramelizes meatball fat while bursting tomatoes into natural sweet savory sauce."),
            ("Lemon Tahini Sauce Creaminess", "Nutty sesame tahini emulsified with lemon juice and ice water creates an unctuous sauce with zero dairy.")
        ],
        "matrix_title": "Meat Selection for Moroccan Meatballs",
        "matrix_headers": ["Meat Blend", "Fat Content", "Flavor Depth", "Tenderness", "Verdict"],
        "matrix_rows": [
            ["80/20 Ground Beef + Ground Lamb", "Medium-High", "Rich, gamey & traditional", "Ultra-tender & juicy", "Gold Standard Authentic Pick (Recommended)"],
            ["85/15 Ground Beef Only", "Medium", "Savory & comforting", "Very tender", "Best accessible weeknight choice"],
            ["Ground Turkey (Dark Meat)", "Medium-Low", "Mild, takes spices well", "Tender (add extra olive oil)", "Great lighter alternative"],
            ["Lean Ground Beef (90/10)", "Low", "Beefy but can dry out", "Firm", "Requires grated onion for moisture"]
        ],
        "ingredients": [
            "1 lb ground beef (85/15) or mix of ground beef and ground lamb",
            "1/3 cup panko breadcrumbs",
            "1 large egg, beaten",
            "4 cloves garlic, minced (divided)",
            "1 tsp ground cumin",
            "1 tsp ground coriander",
            "1/2 tsp ground cinnamon",
            "1/2 tsp smoked paprika",
            "1/4 tsp cayenne pepper",
            "2 cups cherry or grape tomatoes",
            "1 medium red onion, sliced into thin wedges",
            "2 tbsp extra virgin olive oil (divided)",
            "1/4 cup pure sesame tahini paste",
            "2 tbsp fresh lemon juice",
            "2 tbsp fresh mint or flat-leaf parsley, chopped",
            "2 tbsp toasted pine nuts",
            "Warm pita bread triangles, for serving"
        ],
        "instructions": [
            ("Preheat Oven & Season Meat", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper. In a bowl, combine ground meat, panko, egg, half the minced garlic, cumin, coriander, cinnamon, paprika, cayenne, 1 tsp salt, and 1/2 tsp pepper. Mix gently until combined (do not overwork)."),
            ("Shape & Arrange Pan", "Roll meat into 16 golf ball-sized meatballs (about 1.5 inches). Place on the baking sheet. Scatter cherry tomatoes and sliced red onions around the meatballs. Drizzle vegetables with 1 tbsp olive oil and a pinch of salt."),
            ("Roast to Golden Perfection", "Roast at 425°F for 12–14 minutes, switching to high broil for the final 2 minutes until meatballs are deeply browned and caramelized and internal temperature reaches 160°F."),
            ("Whisk Creamy Lemon Tahini", "While pan roasts, whisk tahini paste, remaining minced garlic, lemon juice, 1 tbsp olive oil, a pinch of salt, and 2–3 tbsp warm water in a small bowl until smooth, creamy, and pourable."),
            ("Assemble & Serve", "Tuck warm pita bread wedges onto the sheet pan or serving platter. Drizzle creamy lemon tahini generously over the sizzling meatballs and burst tomatoes. Garnish with chopped fresh mint and toasted pine nuts. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Gentle Hand Meatball Secret",
        "pro_tip": "Never squeeze or compress your meatballs tightly when shaping them! Compressing ground meat forces out fat and air pockets, resulting in dense, rubbery cannonballs. Cup your hands gently and roll each meatball just enough to hold its spherical shape. As they roast in the oven, the meatballs stay incredibly pillowy, juicy, and tender.",
        "faqs": [
            ("Can I freeze these meatballs?", "Yes! Shape raw meatballs and freeze on a baking sheet for 1 hour, then store in a freezer bag for up to 3 months. Bake straight from frozen at 400°F for 18–20 minutes."),
            ("What can I use if I don't have tahini?", "Greek yogurt whisked with lemon juice, grated garlic, and a drop of olive oil makes an incredible, zesty cooling sauce!"),
            ("Can I cook these in an air fryer?", "Yes! Air fry meatballs at 380°F for 9–10 minutes, shaking the basket halfway through.")
        ],
        "wiki_entities": [
            ("Meatball", "https://en.wikipedia.org/wiki/Meatball"),
            ("Tahini", "https://en.wikipedia.org/wiki/Tahini"),
            ("Moroccan cuisine", "https://en.wikipedia.org/wiki/Moroccan_cuisine")
        ],
        "pinterest": {
            "board": "Sheet Pan Meals / Mediterranean Recipes",
            "title": "20-Minute Sheet-Pan Moroccan Spiced Meatballs Recipe (One-Pan Feast!)",
            "desc": "Juicy spiced beef and lamb meatballs roasted on one sheet pan with sweet blistered tomatoes, red onions, warm pita, and creamy lemon tahini sauce in 20 minutes! Save this viral weeknight dinner now!",
            "tags": "#sheetpanmeals #moroccanmeatballs #20minutedinner #mediterraneandiet #tahinisauce #easydinnerrecipes #meatballdinner"
        }
    },
    {
        "slug": "20-minute-sheet-pan-burrata-pesto-gnocchi",
        "title": "20-Minute Sheet-Pan Crispy Gnocchi with Burst Tomatoes, Burrata, and Pesto",
        "headline": "20-Minute Sheet-Pan Crispy Gnocchi with Burrata & Pesto (Viral Italian Dream)",
        "badge": "Sheet Pan Suppers &bull; Viral Comfort",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/sheet-pan-burrata-pesto-gnocchi.jpg",
        "image_file": "sheet-pan-burrata-pesto-gnocchi.jpg",
        "excerpt": "Golden crispy oven-roasted potato gnocchi tossed with sweet blistered vine tomatoes and fragrant basil pesto, crowned with a creamy fresh burrata ball and toasted pine nuts in 20 minutes.",
        "description": "The viral social media sensation made effortlessly: crispy roasted potato gnocchi and sweet bursting cherry tomatoes tossed in basil pesto, torn open with molten, creamy burrata cheese.",
        "keywords": "sheet pan gnocchi, burrata pesto gnocchi, crispy roasted gnocchi, 20 minute vegetarian dinner, easy sheet pan pasta, viral gnocchi recipe",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian",
        "calories": "520 kcal",
        "protein": "16g",
        "fat": "26g",
        "carbs": "58g",
        "fiber": "4g",
        "sodium": "610mg",
        "ratingValue": "4.9",
        "reviewCount": "179",
        "quick_answer": "To make 20-minute sheet-pan burrata pesto gnocchi, preheat oven to 425°F (220°C). Toss 16 oz shelf-stable potato gnocchi (uncooked, straight from pack) and 2 cups cherry tomatoes on a large baking sheet with 2 tbsp olive oil, 1 tsp Italian seasoning, salt, and pepper. Roast for 15–18 minutes until gnocchi are golden and crisp and tomatoes are bursting. Remove pan, dollop 1/3 cup basil pesto over gnocchi, place a whole 8 oz ball of fresh burrata in the center, tear it open to release creamy stracciatella, and top with toasted pine nuts and fresh basil.",
        "takeaways": [
            ("Zero Water Boil Shortcut", "Roasting shelf-stable gnocchi dry on a sheet pan creates a crunchy, blistered exterior shell and a light cloud-like center."),
            ("Tomato-Pesto Pan Emulsion", "Tossing burst tomato juices with fragrant basil pesto directly on the hot sheet pan creates an effortless pan sauce."),
            ("Molten Burrata Centerpiece", "Tearing cold, creamy burrata cheese over the sizzling hot gnocchi creates a decadent, temperature-contrasting sauce.")
        ],
        "matrix_title": "Cheese Options to Crown Hot Sheet Pan Gnocchi",
        "matrix_headers": ["Cheese Type", "Creaminess", "Melt Behavior", "Visual Drama", "Verdict"],
        "matrix_rows": [
            ["Fresh Burrata (Whole Ball)", "Liquid stracciatella cream center", "Melts into luxurious sauce", "Spectacular table centerpiece", "Gold Standard Winner (Recommended)"],
            ["Fresh Mozzarella Pearls", "Mild & milky", "Gooey stringy melt", "Evenly distributed bites", "Great everyday budget substitute"],
            ["Whole Milk Ricotta Dollops", "Dense & velvety", "Warm dollops without melting", "Rustic Italian style", "Excellent light alternative"],
            ["Shaved Parmigiano-Reggiano", "Sharp & nutty", "Coats crispy edges", "Subtle garnish", "Add alongside burrata for depth"]
        ],
        "ingredients": [
            "16 oz shelf-stable or vacuum-packed potato gnocchi (uncooked)",
            "2 cups sweet multi-color cherry or grape tomatoes",
            "1 ball (8 oz) fresh burrata cheese (at room temperature)",
            "1/3 cup prepared basil pesto (store-bought or homemade)",
            "2 tbsp extra virgin olive oil",
            "3 cloves garlic, thinly sliced",
            "1 tsp dried Italian herbs (basil, oregano, thyme)",
            "1/4 tsp crushed red pepper flakes",
            "2 tbsp toasted pine nuts",
            "1/4 cup fresh basil leaves, torn",
            "Balsamic glaze drizzle (optional)",
            "Flaky sea salt & freshly cracked black pepper"
        ],
        "instructions": [
            ("Preheat & Prep Sheet Pan", "Preheat oven to 425°F (220°C). Line a large heavy-rimmed baking sheet with parchment paper for easy cleanup."),
            ("Toss Gnocchi & Tomatoes", "Scatter uncooked gnocchi and whole cherry tomatoes across the baking sheet. Add sliced garlic. Drizzle with 2 tbsp extra virgin olive oil and season with Italian herbs, red pepper flakes, 1/2 tsp salt, and 1/4 tsp pepper. Toss well with your hands and spread into an even, single layer."),
            ("Roast Until Crispy & Blistered", "Roast at 425°F for 15–18 minutes, shaking the pan once halfway through. Gnocchi should be puffed and golden with crispy edges, and tomatoes should be charred and bursting with juice."),
            ("Dollop Pesto", "Remove the baking sheet from the oven. Spoon dollops of basil pesto over the hot gnocchi and gently stir with a spatula so the sweet burst tomato juices and pesto meld into a rich pan sauce."),
            ("Crown with Burrata & Serve", "Place the ball of burrata directly in the center of the hot gnocchi. Use two forks or a knife to gently tear open the burrata ball, spilling the luscious, creamy stracciatella cheese over the crispy dumplings. Scatter toasted pine nuts, torn fresh basil, flaky sea salt, and a drizzle of balsamic glaze. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Room-Temperature Burrata Secret",
        "pro_tip": "Never place refrigerator-cold burrata onto hot gnocchi! Cold burrata shocks the hot food and drops the overall temperature of your dinner in seconds. Take your burrata ball out of the fridge and let it sit on the counter in its brine container for 20 minutes while the gnocchi roasts. When you tear open room-temperature burrata, its silky cream spills effortlessly into the hot pesto.",
        "faqs": [
            ("Do I need to boil the gnocchi first?", "NO! Boiling gnocchi before roasting ruins the crisp texture. Roast shelf-stable gnocchi dry right out of the package—the steam trapped in the oven cooks the interior while roasting the exterior."),
            ("Can I add protein like chicken or sausage?", "Yes! Slice 2 cooked Italian sausages or toss in 1 cup of shredded rotisserie chicken during the final 3 minutes of roasting to warm through."),
            ("What if I don't have burrata?", "Tear a 6 oz ball of fresh mozzarella into chunks or dollop whole-milk ricotta across the pan right after it comes out of the oven.")
        ],
        "wiki_entities": [
            ("Gnocchi", "https://en.wikipedia.org/wiki/Gnocchi"),
            ("Burrata", "https://en.wikipedia.org/wiki/Burrata"),
            ("Pesto", "https://en.wikipedia.org/wiki/Pesto")
        ],
        "pinterest": {
            "board": "Sheet Pan Meals / Pasta Dinners",
            "title": "20-Minute Sheet-Pan Crispy Gnocchi with Burrata & Pesto Recipe (Viral!)",
            "desc": "Crispy roasted potato gnocchi and sweet blistered tomatoes tossed in basil pesto, crowned with a whole ball of molten, creamy fresh burrata cheese. Ready in 20 minutes! Save this viral weeknight dinner now!",
            "tags": "#sheetpangnocchi #burratapesto #gnocchirecipe #20minutedinner #viralrecipes #easyvegetarian #pastatiktok"
        }
    },
    {
        "slug": "15-minute-teriyaki-salmon-bites",
        "title": "15-Minute Crispy Teriyaki Salmon Bites with Sesame Cucumbers",
        "headline": "15-Minute Crispy Teriyaki Salmon Bites (Sticky, Glazed & Fresh)",
        "badge": "15-Minute Meals &bull; High-Protein Power",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/teriyaki-salmon-bites.jpg",
        "image_file": "teriyaki-salmon-bites.jpg",
        "excerpt": "Bite-sized cubes of Atlantic salmon pan-seared to crispy edges and glazed in a rich homemade garlic ginger teriyaki glaze, paired with crunchy sesame chili cucumber salad in 15 minutes.",
        "description": "Tender caramelized cubes of fresh salmon seared to golden crispness in garlic butter, smothered in a sticky sweet soy teriyaki glaze, served alongside crisp smashed sesame cucumbers.",
        "keywords": "teriyaki salmon bites, crispy salmon cubes, 15 minute salmon dinner, easy weeknight salmon, sticky salmon bites, healthy asian bowls",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Japanese-American",
        "calories": "440 kcal",
        "protein": "38g",
        "fat": "20g",
        "carbs": "26g",
        "fiber": "2g",
        "sodium": "660mg",
        "ratingValue": "4.9",
        "reviewCount": "171",
        "quick_answer": "To make 15-minute crispy teriyaki salmon bites, cut 1.5 lbs skinless salmon into 1-inch cubes and toss with 1 tbsp cornstarch, salt, and pepper. In a small bowl, whisk 1/3 cup low-sodium soy sauce, 3 tbsp brown sugar, 1 tbsp mirin (or honey), 1 tbsp grated ginger, and 2 minced garlic cloves. Heat 2 tbsp oil in a large skillet over high heat. Sear salmon cubes for 2 minutes undisturbed, flip and sear 1 minute until crispy; transfer to a plate. Pour teriyaki sauce into skillet, simmer 1 minute until syrupy, return salmon to glaze, and serve with sesame cucumber salad.",
        "takeaways": [
            ("Cubed Salmon Surface Area", "Cutting salmon into 1-inch cubes quadruples the caramelized crispy surface area compared to whole fillets."),
            ("Cornstarch Searing Lock", "A light dusting of cornstarch prevents salmon from shedding albumin (white protein), guaranteeing a crunchy crust."),
            ("Sesame Cucumber Balance", "Cold, crunchy, vinegar-dressed cucumbers provide refreshing textural and acidic contrast against rich omega-3 glazed fish.")
        ],
        "matrix_title": "Salmon Cooking Formats for Weeknight Dinners",
        "matrix_headers": ["Format", "Sear Time", "Glaze Coverage", "Crispy Edge Ratio", "Verdict"],
        "matrix_rows": [
            ["1-Inch Cubes (Bites)", "3 minutes total", "360-degree full coating", "Maximum (4 crispy sides)", "Gold Standard Winner (Recommended)"],
            ["Whole Skin-On Fillets", "8–10 minutes", "Top glaze only", "Crispy skin only", "Classic, but slower cook time"],
            ["Thin Salmon Cutlets", "4 minutes", "Top & bottom", "Moderate", "Great for burgers or wraps"],
            ["Salmon Skewers", "6 minutes", "Good coverage", "Requires threading skewers", "Fun for grilling"]
        ],
        "ingredients": [
            "1.5 lbs skinless Atlantic salmon fillets, cut into 1-inch bite-sized cubes",
            "1 tbsp cornstarch",
            "1/3 cup low-sodium soy sauce (or tamari)",
            "3 tbsp dark brown sugar (or pure honey)",
            "1 tbsp mirin or seasoned rice vinegar",
            "1 tsp toasted sesame oil",
            "3 cloves garlic, finely minced",
            "1 tbsp fresh ginger, finely grated",
            "2 tbsp high-smoke oil (avocado or peanut oil)",
            "2 Persian cucumbers, thinly sliced",
            "1 tbsp rice vinegar & 1 tsp sesame seeds (for cucumbers)",
            "2 scallions (green onions), thinly sliced",
            "Steamed jasmine rice, for serving"
        ],
        "instructions": [
            ("Dry & Dust Salmon Bites", "Pat cubed salmon thoroughly dry with paper towels. Place in a medium bowl, sprinkle with 1 tbsp cornstarch, 1/2 tsp salt, and 1/4 tsp black pepper. Toss gently until each cube is lightly and evenly coated."),
            ("Whisk Quick Teriyaki Glaze", "In a measuring cup or small bowl, whisk together soy sauce, brown sugar, mirin, sesame oil, minced garlic, and grated ginger until sugar dissolves."),
            ("Flash-Sear Salmon Bites", "Heat neutral oil in a large 12-inch nonstick or cast-iron skillet over medium-high heat until shimmering. Add salmon cubes in a single layer with space between them. Sear undisturbed for 2 minutes until bottoms develop a deeply caramelized, crispy crust. Flip and sear 1 more minute. Transfer salmon to a plate."),
            ("Bubble Teriyaki Sauce", "Lower heat to medium. Pour the teriyaki sauce mixture into the empty hot skillet. Let it bubble vigorously for 1–2 minutes, stirring constantly as it reduces into a thick, glossy syrup that coats the back of a spoon."),
            ("Glaze Salmon & Assemble", "Return crispy salmon cubes to the skillet. Toss gently for 30 seconds until every piece is coated in shiny teriyaki glaze. Remove from heat immediately."),
            ("Prep Cucumbers & Serve", "Toss sliced cucumbers with rice vinegar, sesame seeds, and a pinch of salt. Spoon warm jasmine rice into bowls, top with glistening teriyaki salmon bites and crunchy cucumbers, and garnish with sliced scallions and sesame seeds!")
        ],
        "pro_tip_title": "Elena’s Salmon Skinless Cube Secret",
        "pro_tip": "Always remove the salmon skin before cutting into cubes! While crispy skin is delicious on whole roasted fillets, salmon skin shrinks and curls violently when cut into bite-sized cubes, making it impossible to get even, golden caramelization. Skinless cubes sear flat on all sides and drink in the homemade teriyaki glaze like a sponge.",
        "faqs": [
            ("Can I make this in the air fryer?", "Yes! Air fry salmon cubes at 400°F for 6–7 minutes until crispy, then toss in the simmering teriyaki glaze."),
            ("How do I avoid overcooking salmon bites?", "Because the cubes are bite-sized, they cook in just 3 minutes total! Pull them from the heat while the centers are still tender and coral-pink."),
            ("Can I use frozen salmon?", "Yes! Thaw completely in the refrigerator, and make sure to pat thoroughly dry with paper towels before tossing with cornstarch.")
        ],
        "wiki_entities": [
            ("Teriyaki", "https://en.wikipedia.org/wiki/Teriyaki"),
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Cucumber", "https://en.wikipedia.org/wiki/Cucumber")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Seafood Recipes",
            "title": "15-Minute Crispy Teriyaki Salmon Bites Recipe (Sticky & Glazed!)",
            "desc": "Crispy pan-seared Atlantic salmon cubes coated in a sweet sticky garlic ginger teriyaki glaze, served with sesame cucumbers and rice in 15 minutes! Save this viral weeknight seafood recipe now!",
            "tags": "#teriyakisalmon #salmonbites #15minutedinner #healthybowls #asianrecipes #easyweeknightdinner #seafoodtok"
        }
    },
    {
        "slug": "20-minute-creamy-white-cheddar-bacon-mac",
        "title": "20-Minute One-Pot Creamy White Cheddar and Bacon Mac and Cheese",
        "headline": "20-Minute Creamy White Cheddar Bacon Mac and Cheese (No-Boil Skillet Comfort)",
        "badge": "Comfort Food &bull; 20 Mins",
        "category": "Comfort Food",
        "categories_str": "all 30-minute-meals comfort-food one-pot-dinners",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/creamy-white-cheddar-bacon-mac.jpg",
        "image_file": "creamy-white-cheddar-bacon-mac.jpg",
        "excerpt": "Elbow macaroni simmered directly in milk and broth in one skillet, folded into melted sharp white cheddar, smoky bacon crumbles, and crisp garlic panko breadcrumbs in 20 minutes.",
        "description": "The ultimate weeknight macaroni and cheese: elbow pasta cooked directly in milk and broth, blended with sharp white cheddar and gruyère, topped with smoky bacon and buttery toasted panko.",
        "keywords": "white cheddar mac and cheese, bacon mac and cheese, 20 minute mac and cheese, one pot mac and cheese, easy skillet macaroni, gourmet mac and cheese",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American Comfort",
        "calories": "580 kcal",
        "protein": "26g",
        "fat": "28g",
        "carbs": "56g",
        "fiber": "2g",
        "sodium": "720mg",
        "ratingValue": "4.9",
        "reviewCount": "195",
        "quick_answer": "To make 20-minute one-pot creamy white cheddar bacon mac and cheese, crisp 4 slices chopped thick-cut bacon in a large skillet; transfer bacon to a plate, leaving 1 tbsp drippings. Add 1/2 cup panko and 1 tbsp butter to drippings; toast until golden (2 mins) and set aside. In the same skillet, combine 8 oz elbow macaroni, 2 cups low-sodium chicken broth, 1.5 cups whole milk, 1 tsp Dijon mustard, 1/2 tsp garlic powder, salt, and pepper. Bring to a boil, then simmer uncovered for 9–10 minutes, stirring constantly until pasta is tender and liquid is reduced to a creamy base. Remove from heat, fold in 2 cups shredded sharp white cheddar and 1/2 cup gruyère until velvety, and top with bacon and toasted panko.",
        "takeaways": [
            ("One-Pot Milk-Broth Starch Base", "Cooking pasta directly in milk and chicken broth locks in all the pasta starch, creating an ultra-creamy base without making a flour roux."),
            ("Sharp White Cheddar & Gruyère Duo", "Sharp white cheddar provides deep tangy punch while alpine gruyère delivers a dramatic, gooey cheese pull."),
            ("Bacon-Infused Panko Crunch", "Toasting panko breadcrumbs in rendered bacon fat provides crucial crispy texture contrast against velvety cheese sauce.")
        ],
        "matrix_title": "Cheese Blend Performance for Skillet Mac and Cheese",
        "matrix_headers": ["Cheese Blend", "Melt Smoothness", "Sharpness", "Cheese Pull", "Verdict"],
        "matrix_rows": [
            ["Sharp White Cheddar + Gruyère", "Silky & velvety", "Robust & tangy", "Exceptional stringy pull", "Gold Standard Winner (Recommended)"],
            ["Yellow Cheddar + Monterey Jack", "Smooth melt", "Mild & buttery", "High pull", "Classic kid-friendly substitute"],
            ["Smoked Gouda + White Cheddar", "Rich & creamy", "Deep smoky wood notes", "Medium pull", "Fabulous gourmet variation"],
            ["Pre-Shredded Bagged Cheddar", "Gritty & grainy melt", "Low flavor", "Poor", "Not recommended (wood pulp coating)"]
        ],
        "ingredients": [
            "8 oz elbow macaroni or cavatappi pasta (uncooked)",
            "4 slices thick-cut applewood bacon, chopped",
            "1/2 cup panko breadcrumbs",
            "2 cups shredded extra-sharp white cheddar cheese (freshly grated)",
            "1/2 cup shredded Gruyère or fontina cheese",
            "2 cups low-sodium chicken broth",
            "1.5 cups whole milk (or half-and-half)",
            "2 tbsp unsalted butter",
            "1 tsp Dijon mustard",
            "1/2 tsp garlic powder & onion powder",
            "1/4 tsp ground mustard & smoked paprika",
            "2 tbsp fresh chives, finely chopped",
            "Kosher salt & freshly ground black pepper"
        ],
        "instructions": [
            ("Crisp Bacon & Toast Panko", "In a deep 12-inch skillet over medium heat, fry chopped bacon for 5 minutes until deeply crispy. Transfer bacon with a slotted spoon to a paper towel-lined plate, reserving 1 tbsp bacon drippings in pan. Add 1 tbsp butter and 1/2 cup panko to the skillet; stir for 2 minutes until golden brown and toasted. Transfer panko to a small bowl."),
            ("Combine Pasta, Milk & Broth", "In the same skillet, add dry macaroni, chicken broth, whole milk, remaining 1 tbsp butter, Dijon mustard, garlic powder, onion powder, ground mustard, 1/2 tsp salt, and 1/4 tsp black pepper. Stir well."),
            ("Simmer Directly in Skillet", "Bring liquid to a boil over medium-high heat. Once boiling, immediately lower heat to medium-low. Simmer uncovered for 9–10 minutes, stirring frequently with a wooden spoon to prevent pasta from sticking to the bottom, until macaroni is tender and liquid has reduced into a thick, bubbly starchy cream."),
            ("Melt the Cheeses", "Turn off the heat completely. Gradually fold in freshly grated sharp white cheddar and shredded Gruyère, one handful at a time, stirring gently until cheese is fully melted into an ultra-smooth, velvety sauce."),
            ("Garnish & Serve", "Scatter the crispy bacon crumbles, golden toasted garlic panko breadcrumbs, and fresh chopped chives across the top. Serve immediately while hot and bubbly!")
        ],
        "pro_tip_title": "Elena’s Fresh-Block Grating Rule",
        "pro_tip": "Never buy pre-shredded bagged cheese for macaroni and cheese! Pre-shredded cheese is coated in cellulose (wood pulp) and potato starch to prevent clumping in the bag. That coating blocks proper melting, resulting in a separated, greasy, or gritty sauce. Grate a block of sharp white cheddar fresh on a box grater—it melts into silky liquid gold in under 30 seconds.",
        "faqs": [
            ("Can I use water instead of chicken broth?", "Yes, but low-sodium chicken broth adds tremendous savory depth and richness that water cannot match."),
            ("Can I make this ahead or reheat leftovers?", "Store in an airtight container for up to 4 days. Reheat gently in a saucepan with a splash of milk over low heat to restore the creamy sauce consistency."),
            ("Can I bake it with extra cheese on top?", "Yes! Pop the skillet under the broiler for 2–3 minutes after adding the panko and bacon for bubbly browned peaks.")
        ],
        "wiki_entities": [
            ("Macaroni and cheese", "https://en.wikipedia.org/wiki/Macaroni_and_cheese"),
            ("Cheddar cheese", "https://en.wikipedia.org/wiki/Cheddar_cheese"),
            ("Bacon", "https://en.wikipedia.org/wiki/Bacon")
        ],
        "pinterest": {
            "board": "Comfort Food Recipes / Pasta Dinners",
            "title": "20-Minute One-Pot White Cheddar & Bacon Mac and Cheese Recipe (No-Boil!)",
            "desc": "Elbow pasta simmered directly in milk and broth in one skillet, folded into melted sharp white cheddar, smoky bacon, and toasted garlic panko in 20 minutes! Save this viral comfort food recipe now!",
            "tags": "#macandcheese #baconmacandcheese #20minutedinner #onepotmeals #comfortfood #whitecheddar #pastarecipes"
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 4) ===")
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
