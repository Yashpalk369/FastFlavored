import os
import sys
import json
import re
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "20-minute-crispy-honey-butter-cornflake-chicken",
        "title": "20-Minute Crispy Honey Butter Cornflake Chicken",
        "headline": "20-Minute Crispy Honey Butter Cornflake Chicken (Ultra-Crunchy)",
        "badge": "20-Minute Meals &bull; Viral Crunch",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-22",
        "image": "./assets/images/honey-butter-cornflake-chicken.jpg",
        "image_file": "honey-butter-cornflake-chicken.jpg",
        "excerpt": "Ultra-crunchy pan-seared chicken cutlets coated in crushed golden cornflakes, drenched in a warm honey-butter glaze with flaky sea salt and fresh thyme in 20 minutes.",
        "description": "Crispy golden cornflake-crusted chicken tenders pan-fried to crunchy perfection, basted in a glossy melted honey butter glaze with flaky Maldon sea salt and fresh aromatic thyme.",
        "keywords": "honey butter chicken, cornflake chicken tenders, crispy cornflake chicken, 20 minute chicken dinner, easy weeknight chicken, hot honey butter chicken",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American Comfort",
        "calories": "480 kcal",
        "protein": "38g",
        "fat": "18g",
        "carbs": "42g",
        "fiber": "2g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "138",
        "quick_answer": "To make 20-minute crispy honey butter cornflake chicken, dredge 1.5 lbs chicken tenders in seasoned flour, beaten egg, and finely crushed cornflakes mixed with smoked paprika and garlic powder. Pan-fry in 2 tablespoons of oil over medium-high heat for 3–4 minutes per side until deeply golden and 165°F internal. Melt 3 tablespoons unsalted butter with 1/4 cup wildflower honey and a dash of hot sauce, brush generously over hot chicken, and finish with flaky Maldon sea salt and fresh thyme.",
        "takeaways": [
            ("Cornflake Crunch Secret", "Coarsely crushed cornflakes create a jagged, stay-crisp exterior that resists sogginess even after being drenched in warm honey glaze."),
            ("Two-Step Pan Sear", "Searing chicken over medium-high heat caramelizes the cornflake crust without scorching the natural sugars."),
            ("Warm Glaze Emulsion", "Whisking honey into melted butter off the heat preserves honey's floral aromatics and creates a clingy, mirror-gloss coating.")
        ],
        "matrix_title": "Crunch Coating Comparison for Weeknight Chicken",
        "matrix_headers": ["Coating Type", "Texture Profile", "Glaze Resistance", "Prep Effort", "Verdict"],
        "matrix_rows": [
            ["Crushed Cornflakes", "Ultra-shatter crispy & airy", "Exceptional (stays crisp 30+ mins)", "Low (crush in bag)", "Winner & Gold Standard (Recommended)"],
            ["Panko Breadcrumbs", "Light & flaky crunch", "Moderate (softens under heavy glaze)", "Low", "Good classic alternative"],
            ["Standard Breadcrumbs", "Dense & gritty", "Poor (gets soggy quickly)", "Lowest", "Not recommended for glazed chicken"],
            ["Potato Chip Crumbs", "Savory & rich crunch", "Moderate", "Medium (oily crust)", "Fun salty variation"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken tenders (pat dried)",
            "3 cups classic cornflakes cereal (coarsely crushed)",
            "1/2 cup all-purpose flour",
            "2 large eggs (beaten with 1 tbsp water)",
            "1 tsp smoked paprika",
            "1 tsp garlic powder",
            "1/2 tsp onion powder",
            "1/4 cup quality wildflower honey",
            "3 tbsp unsalted butter",
            "1 tsp hot sauce or apple cider vinegar (optional kick)",
            "2 tbsp neutral cooking oil (avocado or vegetable oil)",
            "1 tbsp fresh thyme leaves",
            "1 tsp flaky Maldon sea salt & cracked black pepper"
        ],
        "instructions": [
            ("Prep Breading Station", "Set up three shallow bowls: Bowl 1 with flour, salt, pepper, garlic powder, and paprika; Bowl 2 with beaten eggs; Bowl 3 with coarsely crushed cornflakes."),
            ("Dredge Chicken", "Dredge each chicken tender lightly in flour, dip into egg wash allowing excess to drip, then press firmly into crushed cornflakes to fully coat on both sides."),
            ("Pan-Fry Until Golden", "Heat neutral oil in a large 12-inch skillet over medium-high heat. Add chicken tenders in a single layer (cook in batches if needed). Fry for 3–4 minutes per side until deep golden brown and internal temperature reads 165°F. Transfer to a wire rack."),
            ("Make Honey Butter Glaze", "In a small saucepan over low heat (or microwave for 25 seconds), melt butter together with honey, hot sauce, and a pinch of salt. Whisk until silky and glossy."),
            ("Glaze & Garnish", "Immediately brush the warm honey butter generously over the hot crispy chicken cutlets. Sprinkle with flaky sea salt and fresh thyme leaves. Serve immediately while sizzling!")
        ],
        "pro_tip_title": "Elena’s Golden Wire Rack Hack",
        "pro_tip": "Never transfer freshly pan-fried cornflake chicken onto paper towels! Paper towels trap escaping steam beneath the hot chicken, which instantly softens the bottom crust into mush. Always rest fried cutlets on an elevated wire cooling rack for 90 seconds so air circulates 360 degrees, guaranteeing a glass-like crunch from first bite to last.",
        "faqs": [
            ("Can I make this in the air fryer or oven?", "Yes! For the air fryer, preheat to 390°F, spray chicken lightly with oil, and air-fry for 10–12 minutes, flipping halfway. In the oven, bake at 425°F on a greased wire rack for 15–18 minutes."),
            ("How do I keep the cornflake crust from falling off?", "Press the crushed cornflakes firmly into the tenders with your palms after dredging, and let the breaded chicken sit on a plate for 3 minutes before frying to allow the egg wash to set."),
            ("Can I use hot honey instead of regular honey?", "Absolutely! Hot honey adds an addictive sweet heat that complements the savory garlic-paprika cornflake crust beautifully.")
        ],
        "wiki_entities": [
            ("Corn flakes", "https://en.wikipedia.org/wiki/Corn_flakes"),
            ("Fried chicken", "https://en.wikipedia.org/wiki/Fried_chicken"),
            ("Honey", "https://en.wikipedia.org/wiki/Honey")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / 30-Minute Meals",
            "title": "20-Minute Crispy Honey Butter Cornflake Chicken Recipe (Viral Crunch!)",
            "desc": "The crispiest weeknight dinner ever! Tender juicy chicken coated in shattered cornflakes, pan-fried golden and drenched in warm glossy honey butter with flaky sea salt. Save this 20-minute dinner tonight!",
            "tags": "#honeybutterchicken #cornflakechicken #20minutedinner #crispychicken #easyweeknightdinner #viralrecipe #comfortfood"
        }
    },
    {
        "slug": "15-minute-creamy-lemon-ricotta-gnocchi",
        "title": "15-Minute Creamy Lemon Ricotta Gnocchi",
        "headline": "15-Minute Creamy Lemon Ricotta Gnocchi (One-Skillet Pillowy Comfort)",
        "badge": "15-Minute Meals &bull; One-Pot Comfort",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-22",
        "image": "./assets/images/creamy-lemon-ricotta-gnocchi.jpg",
        "image_file": "creamy-lemon-ricotta-gnocchi.jpg",
        "excerpt": "Pillowy skillet-toasted potato gnocchi enveloped in a silky whole-milk ricotta and lemon zest butter sauce with baby spinach, toasted pine nuts, and parmesan in 15 minutes.",
        "description": "Tender golden pan-seared potato gnocchi tossed in a velvety whole-milk ricotta sauce brightened with fresh lemon zest, wilted baby spinach, buttery toasted pine nuts, and cracked black pepper.",
        "keywords": "lemon ricotta gnocchi, creamy ricotta gnocchi, 15 minute gnocchi recipe, one skillet gnocchi, easy vegetarian dinner, quick weeknight pasta",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian",
        "calories": "440 kcal",
        "protein": "14g",
        "fat": "18g",
        "carbs": "56g",
        "fiber": "4g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "149",
        "quick_answer": "To make 15-minute creamy lemon ricotta gnocchi, melt 2 tbsp butter with 1 tbsp olive oil in a large skillet over medium-high heat. Add 16 oz shelf-stable potato gnocchi straight from the pack (no pre-boiling needed) and sauté undisturbed for 4 minutes until crisp and golden. Reduce heat to low, stir in 1 cup whole-milk ricotta, 1/3 cup vegetable broth or pasta water, zest and juice of 1 lemon, and 1/2 cup grated parmesan. Fold in 3 cups baby spinach until wilted, and top with toasted pine nuts.",
        "takeaways": [
            ("No Boiling Required", "Pan-searing shelf-stable gnocchi straight from the package develops a crispy golden exterior while keeping the interior pillowy and soft."),
            ("Ricotta Emulsion Technique", "Warming whole-milk ricotta over low heat with starchy broth produces a luxurious sauce with zero heavy cream."),
            ("Citrus Brightness", "Fresh lemon zest provides essential aromatic oils that balance rich ricotta and nutty parmesan.")
        ],
        "matrix_title": "Gnocchi Cooking Method Comparison",
        "matrix_headers": ["Cooking Method", "Exterior Texture", "Prep Time", "Skillet Cleanup", "Verdict"],
        "matrix_rows": [
            ["Skillet Pan-Sear (Direct)", "Crispy golden crust, tender chew", "6 minutes total", "1 pan only", "Gold Standard Winner (Recommended)"],
            ["Boil in Water", "Soft, slightly gummy exterior", "10 mins (waiting for boil)", "2 pots to clean", "Classic but lacks texture contrast"],
            ["Sheet Pan Roast", "Deeply roasted, very crunchy", "20-25 mins", "1 baking sheet", "Great for meal prep, slower for weeknights"],
            ["Air Fryer", "Ultra-crispy bite-sized puffs", "12 mins", "Air fryer basket", "Fun for finger food appetizers"]
        ],
        "ingredients": [
            "16 oz shelf-stable or vacuum-packed potato gnocchi (uncooked)",
            "1 cup whole-milk ricotta cheese",
            "2 tbsp unsalted butter",
            "1 tbsp extra virgin olive oil",
            "Zest and juice of 1 large organic lemon",
            "3 cloves garlic, minced",
            "3 cups fresh baby spinach",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "1/3 cup low-sodium vegetable or chicken broth (or hot water)",
            "3 tbsp toasted pine nuts",
            "1/4 tsp crushed red pepper flakes",
            "Flaky sea salt & freshly cracked black pepper"
        ],
        "instructions": [
            ("Pan-Sear Gnocchi", "Heat butter and olive oil in a large 12-inch nonstick or cast-iron skillet over medium heat. Add uncooked gnocchi in a single layer. Sauté undisturbed for 4 minutes until golden and lightly crisped, then flip and sauté 2 more minutes. Transfer gnocchi to a plate."),
            ("Sauté Aromatics", "In the same skillet, reduce heat to medium-low. Add minced garlic and crushed red pepper flakes; sauté for 45 seconds until fragrant without browning."),
            ("Build Lemon Ricotta Sauce", "Add whole-milk ricotta, lemon zest, lemon juice, broth, and grated parmesan. Whisk gently over low heat until a silky, creamy sauce forms (about 1 minute)."),
            ("Combine & Wilt Spinach", "Return crisped gnocchi to the skillet and add fresh baby spinach. Toss gently over low heat for 1–2 minutes until spinach is just wilted and glossy sauce coats each dumpling."),
            ("Garnish & Serve", "Season with flaky sea salt and lots of freshly cracked black pepper. Sprinkle generously with toasted pine nuts and extra shaved parmesan. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s No-Boil Skillet Crunch Rule",
        "pro_tip": "Skip the boiling water pot entirely! Shelf-stable vacuum-packed gnocchi already contain enough internal moisture to steam through in the pan. Searing them directly in foaming butter gives you a golden, slightly caramelized outer shell with a light, cloud-like center that holds onto the creamy lemon ricotta sauce infinitely better.",
        "faqs": [
            ("Can I use cauliflower gnocchi?", "Yes! For frozen cauliflower gnocchi (like Trader Joe's), cook in a dry skillet over medium-high heat first to cook off moisture, then add oil/butter and sear until crispy before adding the sauce."),
            ("Can I substitute cottage cheese for ricotta?", "You can, but blend the cottage cheese in a small blender until completely smooth first; otherwise, curds will separate when heated."),
            ("Can I add protein to this dish?", "Sautéed garlic shrimp, sliced grilled chicken breast, or crispy prosciutto crumbles pair exquisitely with the lemon ricotta sauce.")
        ],
        "wiki_entities": [
            ("Gnocchi", "https://en.wikipedia.org/wiki/Gnocchi"),
            ("Ricotta", "https://en.wikipedia.org/wiki/Ricotta"),
            ("Lemon", "https://en.wikipedia.org/wiki/Lemon")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / One-Pot Dinners",
            "title": "15-Minute Creamy Lemon Ricotta Gnocchi Recipe (One-Pan Comfort!)",
            "desc": "Crispy pan-seared gnocchi coated in a velvety lemon ricotta parmesan sauce with fresh baby spinach and toasted pine nuts. Ready in just 15 minutes in one skillet! Save this easy weeknight comfort dinner!",
            "tags": "#ricottagnocchi #15minutedinner #onepotmeals #gnocchirecipe #easyvegetarian #pastatiktok #lemonpasta"
        }
    },
    {
        "slug": "20-minute-sheet-pan-harissa-honey-salmon",
        "title": "20-Minute Sheet-Pan Harissa Honey Salmon and Asparagus",
        "headline": "20-Minute Sheet-Pan Harissa Honey Salmon (Sweet & Smoky Weeknight Feast)",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-22",
        "image": "./assets/images/harissa-honey-salmon.jpg",
        "image_file": "harissa-honey-salmon.jpg",
        "excerpt": "Flaky Atlantic salmon fillets caramelized in a spicy-sweet harissa honey glaze, roasted on one sheet pan with fresh asparagus, lemon slices, and crumbled feta in 20 minutes.",
        "description": "Tender caramelized salmon fillets coated in a ruby-red North African harissa honey glaze, roasted alongside tender asparagus spears, sweet blistered lemons, and creamy salty feta cheese.",
        "keywords": "harissa salmon, sheet pan salmon, honey harissa salmon recipe, 20 minute sheet pan dinner, mediterranean salmon, healthy weeknight dinner",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "North African / Mediterranean",
        "calories": "460 kcal",
        "protein": "39g",
        "fat": "22g",
        "carbs": "26g",
        "fiber": "4g",
        "sodium": "510mg",
        "ratingValue": "4.9",
        "reviewCount": "162",
        "quick_answer": "To make 20-minute sheet-pan harissa honey salmon, arrange 4 salmon fillets and 1 lb trimmed asparagus on a parchment-lined baking sheet. Whisk 2 tbsp mild rose harissa paste, 2 tbsp honey, 1 tbsp olive oil, 2 cloves minced garlic, and 1 tbsp lemon juice. Brush glaze over salmon and drizzle remaining oil over asparagus. Roast at 425°F (220°C) for 12–14 minutes until salmon flakes easily with a fork, then top with crumbled feta and fresh mint.",
        "takeaways": [
            ("Caramelized Sweet Heat", "The natural sugars in honey caramelize under high heat, taming harissa's smoky chile punch into an irresistible sticky glaze."),
            ("Single Sheet Pan Simplicity", "Roasting salmon and asparagus at 425°F synchronizes cooking times perfectly: tender-crisp greens and flaky, succulent fish."),
            ("Feta & Mint Contrast", "Tangy, briny feta cheese and fresh cooling mint cut through rich omega-3 salmon fats for restaurant-level flavor complexity.")
        ],
        "matrix_title": "Harissa Paste Spice Level & Flavor Profiles",
        "matrix_headers": ["Harissa Variety", "Heat Level", "Flavor Notes", "Best Application", "Recommendation"],
        "matrix_rows": [
            ["Rose Harissa Paste", "Medium-Gentle", "Floral rose petals, cumin, coriander", "Glazed salmon & roast veggies", "Gold Standard (Recommended)"],
            ["Smoky Tunisian Harissa", "Hot & Bold", "Deep smoked red peppers, garlic", "Hearty stews & roasted meats", "Great for heat lovers"],
            ["Dry Harissa Spice Blend", "Adjustable", "Pure powdered spices, earthier", "Dry rubs & marinades", "Whisk with oil & honey first"],
            ["Sriracha + Smoked Paprika", "Medium-Sweet", "Garlicky, vinegar tang", "Quick emergency pantry substitute", "Acceptable swap"]
        ],
        "ingredients": [
            "4 skin-on Atlantic salmon fillets (6 oz each, pat dry)",
            "1 lb fresh asparagus spears (woody ends snapped off)",
            "2 tbsp rose harissa paste (mild or medium)",
            "2 tbsp pure clover or orange blossom honey",
            "2 tbsp extra virgin olive oil (divided)",
            "3 cloves garlic, finely grated",
            "1 organic lemon (half juiced, half thinly sliced)",
            "1/3 cup crumbled Greek feta cheese",
            "2 tbsp fresh mint or cilantro leaves, chopped",
            "1 tsp toasted sesame seeds",
            "Kosher salt and freshly cracked black pepper"
        ],
        "instructions": [
            ("Preheat Oven & Prep Pan", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper or foil for zero-scrub cleanup."),
            ("Whisk Honey Harissa Glaze", "In a small bowl, whisk together harissa paste, honey, 1 tbsp olive oil, grated garlic, lemon juice, and a pinch of salt until glossy and blended."),
            ("Assemble Sheet Pan", "Arrange salmon fillets skin-side down in the center of the pan. Spread asparagus spears and thin lemon slices around the fish. Toss asparagus with remaining 1 tbsp olive oil, salt, and pepper."),
            ("Glaze Salmon", "Spoon and brush the harissa honey glaze generously over the top and sides of each salmon fillet."),
            ("Roast & Broil", "Roast for 12–14 minutes until salmon reaches 130°F internal temperature and flakes easily with a fork. For extra caramelized char, switch to broil for the final 90 seconds."),
            ("Garnish & Serve", "Scatter crumbled feta cheese, fresh mint leaves, and toasted sesame seeds over the hot salmon and asparagus. Serve immediately with warm pita or fluffy couscous!")
        ],
        "pro_tip_title": "Elena’s 90-Second Broiler Glaze Caramelizer",
        "pro_tip": "For that jaw-dropping restaurant char, switch your oven from Bake to High Broil for the final 90 seconds of cooking. Watch closely: the honey and harissa paste will bubble furiously and form deeply caramelized, lacquer-like charred edges while leaving the center of the salmon pink, silky, and melt-in-your-mouth moist.",
        "faqs": [
            ("What if I don't have harissa paste?", "You can substitute 2 tbsp tomato paste mixed with 1 tsp smoked paprika, 1/2 tsp ground cumin, 1/4 tsp cayenne pepper, and a dash of hot sauce."),
            ("Can I make this with chicken or shrimp instead?", "Yes! Boneless chicken cutlets take 15–18 minutes at 425°F. For peeled jumbo shrimp, roast for just 7–8 minutes."),
            ("How do I know when salmon is perfectly cooked?", "Gently press down on the top of the fillet with a fork or your finger; if the flakes begin to separate cleanly along the white fat lines, it is perfectly cooked. Avoid overcooking!")
        ],
        "wiki_entities": [
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Harissa", "https://en.wikipedia.org/wiki/Harissa"),
            ("Asparagus", "https://en.wikipedia.org/wiki/Asparagus")
        ],
        "pinterest": {
            "board": "Sheet Pan Meals / Healthy Dinners",
            "title": "20-Minute Sheet-Pan Harissa Honey Salmon Recipe (Sweet & Smoky!)",
            "desc": "Flaky caramelized salmon fillets coated in sweet and smoky honey harissa glaze, roasted on one pan with tender asparagus and crumbled feta in 20 minutes! Save this healthy weeknight dinner now!",
            "tags": "#sheetpansalmon #harissasalmon #20minutedinner #healthydinnerideas #mediterraneandiet #sheetpanrecipes #salmonrecipes"
        }
    },
    {
        "slug": "15-minute-creamy-gochujang-pasta",
        "title": "15-Minute Creamy Gochujang Vodka Pasta",
        "headline": "15-Minute Creamy Gochujang Vodka Pasta (The Viral Fusion Sensation)",
        "badge": "15-Minute Meals &bull; Viral Fusion",
        "category": "Comfort Food",
        "categories_str": "all 30-minute-meals comfort-food one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-22",
        "image": "./assets/images/creamy-gochujang-pasta.jpg",
        "image_file": "creamy-gochujang-pasta.jpg",
        "excerpt": "Ridged rigatoni coated in a fiery-sweet fermented Korean gochujang cream sauce with garlic, parmesan, scallions, and toasted sesame seeds in 15 minutes.",
        "description": "The viral social media fusion hit: al dente rigatoni tossed in an umami-rich Korean gochujang cream sauce, rounded out with butter, garlic, aged parmesan, and fresh scallions.",
        "keywords": "gochujang pasta, spicy vodka pasta, creamy gochujang rigatoni, 15 minute pasta dinner, viral pasta recipe, korean italian fusion",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Korean-Italian Fusion",
        "calories": "540 kcal",
        "protein": "15g",
        "fat": "24g",
        "carbs": "64g",
        "fiber": "3g",
        "sodium": "620mg",
        "ratingValue": "4.9",
        "reviewCount": "156",
        "quick_answer": "To make 15-minute creamy gochujang pasta, boil 12 oz rigatoni until al dente, reserving 1 cup of pasta cooking water. In a large skillet over medium heat, melt 2 tbsp butter with 1 tbsp olive oil. Sauté 4 minced garlic cloves and 2 finely chopped shallots for 2 minutes. Stir in 2 tbsp Korean gochujang paste and 1 tbsp tomato paste, cooking 2 minutes until deeply caramelized and fragrant. Pour in 3/4 cup heavy cream and 1/2 cup reserved pasta water, stirring until silky. Toss in rigatoni and 1/2 cup grated parmesan, garnishing with scallions and sesame seeds.",
        "takeaways": [
            ("Paste Caramelization Key", "Blooming gochujang and tomato paste in hot butter mellows sharp chile edges and deepens savory fermented glutamates."),
            ("Cream & Cheese Balancing Act", "Heavy cream and salty Parmigiano-Reggiano temper gochujang's heat into a velvety, restaurant-grade gloss."),
            ("Scallion & Sesame Freshness", "Raw scallions and nutty toasted sesame seeds provide essential sharpness and crunch against the rich sauce.")
        ],
        "matrix_title": "Spicy Cream Pasta Sauce Base Comparison",
        "matrix_headers": ["Sauce Base", "Spice Level", "Umami Depth", "Sweetness", "Verdict"],
        "matrix_rows": [
            ["Gochujang + Cream", "Medium warm heat", "Deep fermented umami", "Natural rice sweetness", "Gold Standard Viral Pick (Recommended)"],
            ["Classic Vodka Sauce", "Mild warmth", "Savory tomato-rich", "Subtle onion sweetness", "Traditional Italian-American classic"],
            ["Calabrian Chile + Cream", "Sharp, fiery kick", "Fruity & acidic", "Very low", "Bold & sharp for heat lovers"],
            ["Sriracha + Cream", "Direct vinegary heat", "Moderate garlic notes", "Medium corn sweetness", "Pantry emergency alternative"]
        ],
        "ingredients": [
            "12 oz rigatoni, mezze maniche, or penne pasta",
            "2 tbsp Korean gochujang (fermented chili paste)",
            "1 tbsp double-concentrated tomato paste",
            "3/4 cup heavy cream (or full-fat coconut milk)",
            "2 tbsp unsalted butter",
            "1 tbsp olive oil",
            "4 cloves garlic, finely minced",
            "1 medium shallot, finely minced",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "1 cup reserved starchy pasta cooking water",
            "3 scallions (green onions), thinly sliced",
            "1 tsp toasted black and white sesame seeds",
            "Kosher salt & freshly ground black pepper"
        ],
        "instructions": [
            ("Boil Pasta", "Bring a large pot of salted water to a rolling boil. Cook rigatoni until 1 minute shy of al dente. Reserve 1 cup of starchy pasta water before draining."),
            ("Sauté Aromatics", "While pasta cooks, melt butter with olive oil in a large deep skillet over medium heat. Add minced garlic and shallots; cook for 2 minutes until translucent and fragrant."),
            ("Caramelize the Pastes", "Add gochujang paste and tomato paste to the skillet. Cook, stirring constantly for 2 minutes, allowing the pastes to caramelize into a deep burgundy-red oil."),
            ("Emulsify Cream Sauce", "Pour in heavy cream and 1/2 cup reserved pasta water. Whisk continuously over medium-low heat until a smooth, vibrant orange cream sauce forms (about 2 minutes)."),
            ("Toss with Pasta", "Add drained rigatoni directly to the sauce. Toss vigorously over low heat for 1–2 minutes, adding more pasta water a tablespoon at a time until sauce clings to every tube."),
            ("Garnish & Serve", "Remove from heat, fold in grated Parmigiano-Reggiano, and garnish generously with sliced scallions, toasted sesame seeds, and extra parmesan. Enjoy immediately!")
        ],
        "pro_tip_title": "Elena’s Paste Caramelization Secret",
        "pro_tip": "Do not rush pouring the heavy cream into the pan! Always fry the gochujang and tomato paste directly in the foaming butter and aromatics for a full 2 minutes until it darkens into a deep brick-red oil. This caramelizes the fermented sugars in the gochujang, eliminating raw bitterness and unlocking an addictive, deeply savory umami foundation.",
        "faqs": [
            ("Is gochujang paste extremely spicy?", "Most commercial gochujang pastes are medium in heat. Combined with 3/4 cup of heavy cream and parmesan, the heat softens into a warm, cozy tingle rather than a burning spice."),
            ("Can I make this dairy-free or vegan?", "Yes! Substitute full-fat coconut cream or cashew cream for the heavy cream, use vegan butter, and finish with nutritional yeast or dairy-free parmesan."),
            ("Can I add protein to gochujang pasta?", "Crispy diced bacon or pancetta, grilled chicken breast strips, or sautéed garlic butter shrimp make sensational protein additions!")
        ],
        "wiki_entities": [
            ("Gochujang", "https://en.wikipedia.org/wiki/Gochujang"),
            ("Rigatoni", "https://en.wikipedia.org/wiki/Rigatoni"),
            ("Vodka sauce", "https://en.wikipedia.org/wiki/Vodka_sauce")
        ],
        "pinterest": {
            "board": "Pasta Recipes / Quick Dinners",
            "title": "15-Minute Creamy Gochujang Vodka Pasta Recipe (Viral Fusion Dinner!)",
            "desc": "The viral pasta everyone is obsessed with! Ridged rigatoni smothered in a velvety spicy-sweet gochujang cream sauce with garlic, parmesan, and scallions. Ready in 15 minutes! Save this viral recipe now!",
            "tags": "#gochujangpasta #15minutepasta #pastatiktok #viralpasta #easydinnerrecipes #fusionfood #comfortfood"
        }
    },
    {
        "slug": "15-minute-thai-basil-chicken",
        "title": "15-Minute Spicy Thai Basil Chicken (Pad Krapow Gai)",
        "headline": "15-Minute Spicy Thai Basil Chicken (Authentic Street Food Speed)",
        "badge": "15-Minute Meals &bull; Street Food Fast",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-22",
        "image": "./assets/images/thai-basil-chicken.jpg",
        "image_file": "thai-basil-chicken.jpg",
        "excerpt": "Savory caramelized ground chicken tossed in garlic, bird's eye chilies, and fragrant holy basil, crowned with a crispy bubbly-edged fried egg in 15 minutes.",
        "description": "Authentic Bangkok street food made lightning-fast: savory minced chicken caramelized with bird's eye chilies, garlic, sweet soy sauce, and fragrant holy basil, crowned with a crispy runny fried egg.",
        "keywords": "thai basil chicken, pad krapow gai, 15 minute thai dinner, spicy ground chicken, easy stir fry recipe, street food recipes",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Thai",
        "calories": "410 kcal",
        "protein": "34g",
        "fat": "19g",
        "carbs": "18g",
        "fiber": "2g",
        "sodium": "740mg",
        "ratingValue": "4.9",
        "reviewCount": "178",
        "quick_answer": "To make 15-minute Thai basil chicken (Pad Krapow Gai), whisk 1.5 tbsp oyster sauce, 1 tbsp soy sauce, 1 tsp dark soy sauce, 1 tsp fish sauce, and 1 tsp brown sugar. In a screaming-hot wok with 2 tbsp oil, fry 6 minced garlic cloves and 3 sliced Thai bird's eye chilies for 30 seconds. Add 1 lb ground chicken and stir-fry undisturbed until caramelized (3–4 mins). Pour sauce over chicken, toss until glazed, take off heat, and fold in 2 large cups of fresh holy basil or Thai sweet basil. Serve with jasmine rice and a crispy fried egg.",
        "takeaways": [
            ("Screaming Wok Heat", "High heat caramelizes minced chicken juices into savory browned bits without boiling or steaming the meat."),
            ("Dark Soy Color & Depth", "Dark soy sauce imparts the signature deep caramel hue and subtle molasses sweetness seen on Bangkok street carts."),
            ("Off-Heat Basil Wilt", "Folding basil in off the heat prevents bruising and preserves delicate essential oils and spicy peppery aromas.")
        ],
        "matrix_title": "Basil Variety Comparison for Pad Krapow",
        "matrix_headers": ["Basil Type", "Flavor Profile", "Aroma Strength", "Heat Resistance", "Authenticity"],
        "matrix_rows": [
            ["Thai Holy Basil (Krapow)", "Peppery, clove-like, pungent", "Intense & sharp", "High", "100% Authentic Bangkok Standard (Recommended)"],
            ["Thai Sweet Basil (Horapa)", "Anise, sweet licorice notes", "Strong & aromatic", "Medium-High", "Excellent & accessible alternative"],
            ["Italian Sweet Basil", "Sweet, floral, mild mint", "Mild", "Medium", "Acceptable pantry swap (add pinch of black pepper)"],
            ["Purple Opal Basil", "Earthy, mild clove", "Medium", "Medium", "Good visual & aromatic swap"]
        ],
        "ingredients": [
            "1 lb ground chicken (or finely hand-minced chicken thighs)",
            "2 cups fresh holy basil or Thai sweet basil leaves (loosely packed)",
            "6 cloves garlic, finely minced or pounded in mortar",
            "3–5 Thai bird's eye chilies, thinly sliced (adjust to spice preference)",
            "1.5 tbsp premium oyster sauce",
            "1 tbsp low-sodium soy sauce",
            "1 tsp dark sweet soy sauce (kecap manis or regular dark soy)",
            "1 tsp fish sauce",
            "1 tsp brown sugar",
            "2 tbsp high-smoke oil (avocado, peanut, or canola oil)",
            "4 large eggs (for crispy fried egg topping)",
            "Steamed jasmine rice, for serving",
            "Fresh lime wedges, for serving"
        ],
        "instructions": [
            ("Mix Savory Sauce", "In a small ramekin, whisk together oyster sauce, regular soy sauce, dark soy sauce, fish sauce, and brown sugar until sugar dissolves. Set next to stove."),
            ("Fry Crispy Thai Eggs", "Heat 2 tbsp oil in a wok or deep skillet over high heat until shimmering. Crack an egg directly into hot oil; spoon hot oil over egg white until edges bubble and turn deeply crispy and lace-like while yolk remains runny (about 90 seconds). Transfer egg to a plate. Repeat for remaining eggs."),
            ("Sear Garlic & Chilies", "In the remaining hot oil in the wok, add minced garlic and sliced Thai chilies. Stir-fry vigorously for 30 seconds until intensely aromatic (do not burn garlic)."),
            ("Caramelize Chicken", "Add ground chicken, breaking it apart with a wooden spoon or spatula. Spread across the hot surface and let sear undisturbed for 2 minutes to develop deep golden caramelization, then stir-fry 2 more minutes until cooked through."),
            ("Glaze with Sauce", "Pour the prepared sauce mixture over the hot chicken. Stir-fry vigorously over high heat for 1 minute until sauce reduces into a glossy, dark savory lacquer coating every morsel of chicken."),
            ("Fold Basil & Serve", "Turn off the heat immediately. Toss in the fresh basil leaves, folding gently for 30 seconds until just wilted by residual heat. Spoon over warm jasmine rice, crown with a crispy fried egg, and serve with lime wedges!")
        ],
        "pro_tip_title": "Elena’s Crispy Khai Dao (Fried Egg) Mastery",
        "pro_tip": "The soul of authentic Pad Krapow is the Thai-style fried egg ('Khai Dao'). Heat at least 2 tablespoons of oil until smoking hot before sliding the egg in. As the bottom bubbles and blisters into a golden, crackling lace collar, gently tilt the pan and ladle hot oil over the whites. The white becomes audibly crunchy while the yolk stays liquid gold!",
        "faqs": [
            ("What if I cannot find Thai holy basil?", "Thai sweet basil (with purple stems) is widely available at Asian grocery stores and works wonderfully. In a pinch, Italian sweet basil mixed with a pinch of fresh mint and cracked black pepper creates a great substitute."),
            ("How spicy is this dish?", "With 3–4 bird's eye chilies, it has an authentic medium-high kick. If you prefer mild heat, use 1 chili, remove the seeds, or substitute with a sliced red jalapeño or Fresno chili."),
            ("Can I use ground turkey or pork?", "Yes! Ground pork is the traditional alternative (Pad Krapow Moo), and ground turkey works identically with fantastic flavor.")
        ],
        "wiki_entities": [
            ("Phat kaphrao", "https://en.wikipedia.org/wiki/Phat_kaphrao"),
            ("Ocimum tenuiflorum", "https://en.wikipedia.org/wiki/Ocimum_tenuiflorum"),
            ("Bird's eye chili", "https://en.wikipedia.org/wiki/Bird%27s_eye_chili")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Asian Recipes",
            "title": "15-Minute Spicy Thai Basil Chicken Recipe (Pad Krapow Gai!)",
            "desc": "Bangkok street food on your dinner table in 15 minutes! Savory caramelized chicken stir-fried with fragrant holy basil, garlic, and chilies, topped with a crispy fried egg and runny yolk. Save this easy dinner!",
            "tags": "#thaibasilchicken #padkrapow #15minutedinner #thaifood #streetfood #stirfryrecipe #easyweeknightdinner"
        }
    },
    {
        "slug": "20-minute-creamy-marry-me-chickpeas",
        "title": "20-Minute Creamy Garlic Butter Marry Me Chickpeas",
        "headline": "20-Minute Creamy Garlic Butter Marry Me Chickpeas (Rich Vegetarian Feast)",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-22",
        "image": "./assets/images/creamy-marry-me-chickpeas.jpg",
        "image_file": "creamy-marry-me-chickpeas.jpg",
        "excerpt": "Plump chickpeas simmered in a luscious sun-dried tomato, garlic, and parmesan herb cream sauce with tender baby spinach and fresh basil in 20 minutes.",
        "description": "A comforting vegetarian twist on viral Marry Me chicken: tender chickpeas simmered in a velvety sun-dried tomato garlic parmesan cream sauce loaded with fresh spinach and fragrant basil.",
        "keywords": "marry me chickpeas, creamy chickpeas recipe, vegetarian marry me chicken, 20 minute one pot dinner, sun dried tomato cream sauce, easy vegetarian recipes",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American",
        "calories": "420 kcal",
        "protein": "16g",
        "fat": "20g",
        "carbs": "46g",
        "fiber": "9g",
        "sodium": "540mg",
        "ratingValue": "4.9",
        "reviewCount": "165",
        "quick_answer": "To make 20-minute creamy Marry Me chickpeas, sauté 4 minced garlic cloves and 1/3 cup chopped oil-packed sun-dried tomatoes in 2 tbsp butter over medium heat for 2 minutes. Add 2 cans (15 oz each) rinsed chickpeas, 1 tsp dried oregano, 1/2 tsp red pepper flakes, 1/2 cup vegetable broth, and 3/4 cup heavy cream. Simmer gently for 8–10 minutes until thickened and chickpeas are tender. Stir in 1/2 cup grated parmesan and 3 cups baby spinach until wilted, and finish with fresh basil.",
        "takeaways": [
            ("Umami Sun-Dried Tomato Oil", "Sautéing garlic directly in the flavored oil from the sun-dried tomato jar creates a rich, complex flavor base in seconds."),
            ("Chickpea Starch Thickening", "Lightly mashing a spoonful of chickpeas releases natural starches that thicken the sauce into a luxurious velvety gravy."),
            ("High-Fiber Plant Powerhouse", "With 9 grams of dietary fiber and 16 grams of plant protein per serving, this comforting dish is as wholesome as it is decadent.")
        ],
        "matrix_title": "Plant-Protein Bases for Marry Me Sauce",
        "matrix_headers": ["Protein Base", "Sauce Adhesion", "Simmer Time", "Protein per Serving", "Verdict"],
        "matrix_rows": [
            ["Canned Chickpeas (Garbanzo)", "Absorbs cream deeply, velvety chew", "8-10 minutes", "16g protein", "Gold Standard Winner (Recommended)"],
            ["Cannellini White Beans", "Ultra-creamy, softer texture", "6-8 minutes", "14g protein", "Excellent velvety substitute"],
            ["Crispy Pan-Seared Tofu", "Crispy exterior, chewy interior", "12-15 minutes", "18g protein", "Great for extra crunch"],
            ["Steamed Green Lentils", "Earthy & hearty", "10 minutes", "17g protein", "Rich & rustic alternative"]
        ],
        "ingredients": [
            "2 cans (15 oz each) chickpeas (garbanzo beans), rinsed and drained",
            "1/2 cup oil-packed sun-dried tomatoes, drained and thinly sliced (reserve 1 tbsp oil)",
            "4 cloves garlic, finely minced",
            "2 tbsp unsalted butter",
            "3/4 cup heavy cream (or full-fat canned coconut cream)",
            "1/2 cup low-sodium vegetable broth",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "3 cups fresh baby spinach leaves",
            "1/4 cup fresh basil leaves, torn or thinly sliced",
            "1 tsp dried oregano",
            "1/2 tsp dried thyme",
            "1/4 tsp crushed red pepper flakes",
            "Kosher salt and freshly cracked black pepper",
            "Crusty artisan bread or warm rice, for serving"
        ],
        "instructions": [
            ("Sauté Aromatics in Tomato Oil", "In a large deep skillet or Dutch oven, heat butter and 1 tbsp reserved sun-dried tomato oil over medium heat. Add minced garlic, sliced sun-dried tomatoes, dried oregano, dried thyme, and red pepper flakes. Sauté for 2 minutes until fragrant and oil turns ruby-orange."),
            ("Add Chickpeas & Simmer", "Pour in rinsed chickpeas, vegetable broth, and heavy cream. Stir well to combine. Bring to a gentle simmer over medium-low heat and cook for 8–10 minutes, stirring occasionally, until sauce thickens to your liking."),
            ("Light Mash for Extra Body", "Use the back of a wooden spoon or potato masher to crush about 1/4 cup of the chickpeas directly against the bottom of the pan. Stir into the sauce to instantly create a velvety, cohesive texture."),
            ("Melt Cheese & Wilt Greens", "Reduce heat to low. Stir in grated Parmigiano-Reggiano and fresh baby spinach. Cook for 1–2 minutes until the spinach is just wilted and cheese is completely melted."),
            ("Garnish & Serve", "Remove from heat, fold in fresh torn basil, and season to taste with flaky sea salt and cracked black pepper. Serve piping hot with toasted thick slices of sourdough bread for dipping!")
        ],
        "pro_tip_title": "Elena’s Starch-Crush Velvety Sauce Secret",
        "pro_tip": "Before taking the pan off the heat, take the back of your wooden spoon and crush about 15–20 chickpeas directly against the side or bottom of the pan! The creamy mashed chickpeas release natural starch that effortlessly binds the cream and cheese with the broth, creating a luxurious, restaurant-quality emulsion without having to add cornstarch or flour.",
        "faqs": [
            ("Can I make this dairy-free or vegan?", "Yes! Replace the heavy cream with full-fat canned coconut milk or unsweetened cashew cream, use vegan butter or extra olive oil, and swap the parmesan for nutritional yeast or vegan parmesan."),
            ("What should I serve with Marry Me chickpeas?", "Warm crusty sourdough or garlic naan is unbeatable for scooping up the velvety sauce! It also pairs wonderfully served over buttered egg noodles, orzo, or fluffy jasmine rice."),
            ("How do I store and reheat leftovers?", "Store in an airtight glass container in the refrigerator for up to 4 days. Reheat gently in a saucepan over medium-low heat with a small splash of broth or water to loosen the cream sauce.")
        ],
        "wiki_entities": [
            ("Chickpea", "https://en.wikipedia.org/wiki/Chickpea"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato"),
            ("Parmigiano Reggiano", "https://en.wikipedia.org/wiki/Parmigiano_Reggiano")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / One-Pot Dinners",
            "title": "20-Minute Creamy Marry Me Chickpeas Recipe (Rich One-Pot Dinner!)",
            "desc": "The vegetarian version of viral Marry Me chicken that everyone falls in love with! Plump chickpeas in a velvety garlic sun-dried tomato parmesan cream sauce with spinach and basil. Save this 20-minute dinner!",
            "tags": "#marrymechickpeas #onepotdinners #20minutedinner #vegetarianrecipes #chickpearecipes #meatlessmonday #pastatiktok"
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes ===")
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

    # 4. Append to recipe_data.py so master list stays updated
    try:
        recipe_data_path = os.path.join(BASE_DIR, "scripts", "recipe_data.py")
        with open(recipe_data_path, "r", encoding="utf-8") as f:
            rd_content = f.read()
        
        # Prepend to RECIPES list in recipe_data.py
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
