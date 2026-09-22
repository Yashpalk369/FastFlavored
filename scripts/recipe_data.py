import os
import json
import re

RECIPES = [
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
        "quick_answer": "To make 20-minute crispy honey butter cornflake chicken, dredge 1.5 lbs chicken tenders in seasoned flour, beaten egg, and finely crushed cornflakes mixed with smoked paprika and garlic powder. Pan-fry in 2 tablespoons of oil over medium-high heat for 3\u20134 minutes per side until deeply golden and 165\u00b0F internal. Melt 3 tablespoons unsalted butter with 1/4 cup wildflower honey and a dash of hot sauce, brush generously over hot chicken, and finish with flaky Maldon sea salt and fresh thyme.",
        "takeaways": [
                [
                        "Cornflake Crunch Secret",
                        "Coarsely crushed cornflakes create a jagged, stay-crisp exterior that resists sogginess even after being drenched in warm honey glaze."
                ],
                [
                        "Two-Step Pan Sear",
                        "Searing chicken over medium-high heat caramelizes the cornflake crust without scorching the natural sugars."
                ],
                [
                        "Warm Glaze Emulsion",
                        "Whisking honey into melted butter off the heat preserves honey's floral aromatics and creates a clingy, mirror-gloss coating."
                ]
        ],
        "matrix_title": "Crunch Coating Comparison for Weeknight Chicken",
        "matrix_headers": [
                "Coating Type",
                "Texture Profile",
                "Glaze Resistance",
                "Prep Effort",
                "Verdict"
        ],
        "matrix_rows": [
                [
                        "Crushed Cornflakes",
                        "Ultra-shatter crispy & airy",
                        "Exceptional (stays crisp 30+ mins)",
                        "Low (crush in bag)",
                        "Winner & Gold Standard (Recommended)"
                ],
                [
                        "Panko Breadcrumbs",
                        "Light & flaky crunch",
                        "Moderate (softens under heavy glaze)",
                        "Low",
                        "Good classic alternative"
                ],
                [
                        "Standard Breadcrumbs",
                        "Dense & gritty",
                        "Poor (gets soggy quickly)",
                        "Lowest",
                        "Not recommended for glazed chicken"
                ],
                [
                        "Potato Chip Crumbs",
                        "Savory & rich crunch",
                        "Moderate",
                        "Medium (oily crust)",
                        "Fun salty variation"
                ]
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
                [
                        "Prep Breading Station",
                        "Set up three shallow bowls: Bowl 1 with flour, salt, pepper, garlic powder, and paprika; Bowl 2 with beaten eggs; Bowl 3 with coarsely crushed cornflakes."
                ],
                [
                        "Dredge Chicken",
                        "Dredge each chicken tender lightly in flour, dip into egg wash allowing excess to drip, then press firmly into crushed cornflakes to fully coat on both sides."
                ],
                [
                        "Pan-Fry Until Golden",
                        "Heat neutral oil in a large 12-inch skillet over medium-high heat. Add chicken tenders in a single layer (cook in batches if needed). Fry for 3\u20134 minutes per side until deep golden brown and internal temperature reads 165\u00b0F. Transfer to a wire rack."
                ],
                [
                        "Make Honey Butter Glaze",
                        "In a small saucepan over low heat (or microwave for 25 seconds), melt butter together with honey, hot sauce, and a pinch of salt. Whisk until silky and glossy."
                ],
                [
                        "Glaze & Garnish",
                        "Immediately brush the warm honey butter generously over the hot crispy chicken cutlets. Sprinkle with flaky sea salt and fresh thyme leaves. Serve immediately while sizzling!"
                ]
        ],
        "pro_tip_title": "Elena\u2019s Golden Wire Rack Hack",
        "pro_tip": "Never transfer freshly pan-fried cornflake chicken onto paper towels! Paper towels trap escaping steam beneath the hot chicken, which instantly softens the bottom crust into mush. Always rest fried cutlets on an elevated wire cooling rack for 90 seconds so air circulates 360 degrees, guaranteeing a glass-like crunch from first bite to last.",
        "faqs": [
                [
                        "Can I make this in the air fryer or oven?",
                        "Yes! For the air fryer, preheat to 390\u00b0F, spray chicken lightly with oil, and air-fry for 10\u201312 minutes, flipping halfway. In the oven, bake at 425\u00b0F on a greased wire rack for 15\u201318 minutes."
                ],
                [
                        "How do I keep the cornflake crust from falling off?",
                        "Press the crushed cornflakes firmly into the tenders with your palms after dredging, and let the breaded chicken sit on a plate for 3 minutes before frying to allow the egg wash to set."
                ],
                [
                        "Can I use hot honey instead of regular honey?",
                        "Absolutely! Hot honey adds an addictive sweet heat that complements the savory garlic-paprika cornflake crust beautifully."
                ]
        ],
        "wiki_entities": [
                [
                        "Corn flakes",
                        "https://en.wikipedia.org/wiki/Corn_flakes"
                ],
                [
                        "Fried chicken",
                        "https://en.wikipedia.org/wiki/Fried_chicken"
                ],
                [
                        "Honey",
                        "https://en.wikipedia.org/wiki/Honey"
                ]
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
        "quick_answer": "To make 15-minute creamy lemon ricotta gnocchi, melt 2 tbsp butter with 1 tbsp olive oil in a large skillet over medium-high heat. Add 16 oz shelf-stable potato gnocchi straight from the pack (no pre-boiling needed) and saut\u00e9 undisturbed for 4 minutes until crisp and golden. Reduce heat to low, stir in 1 cup whole-milk ricotta, 1/3 cup vegetable broth or pasta water, zest and juice of 1 lemon, and 1/2 cup grated parmesan. Fold in 3 cups baby spinach until wilted, and top with toasted pine nuts.",
        "takeaways": [
                [
                        "No Boiling Required",
                        "Pan-searing shelf-stable gnocchi straight from the package develops a crispy golden exterior while keeping the interior pillowy and soft."
                ],
                [
                        "Ricotta Emulsion Technique",
                        "Warming whole-milk ricotta over low heat with starchy broth produces a luxurious sauce with zero heavy cream."
                ],
                [
                        "Citrus Brightness",
                        "Fresh lemon zest provides essential aromatic oils that balance rich ricotta and nutty parmesan."
                ]
        ],
        "matrix_title": "Gnocchi Cooking Method Comparison",
        "matrix_headers": [
                "Cooking Method",
                "Exterior Texture",
                "Prep Time",
                "Skillet Cleanup",
                "Verdict"
        ],
        "matrix_rows": [
                [
                        "Skillet Pan-Sear (Direct)",
                        "Crispy golden crust, tender chew",
                        "6 minutes total",
                        "1 pan only",
                        "Gold Standard Winner (Recommended)"
                ],
                [
                        "Boil in Water",
                        "Soft, slightly gummy exterior",
                        "10 mins (waiting for boil)",
                        "2 pots to clean",
                        "Classic but lacks texture contrast"
                ],
                [
                        "Sheet Pan Roast",
                        "Deeply roasted, very crunchy",
                        "20-25 mins",
                        "1 baking sheet",
                        "Great for meal prep, slower for weeknights"
                ],
                [
                        "Air Fryer",
                        "Ultra-crispy bite-sized puffs",
                        "12 mins",
                        "Air fryer basket",
                        "Fun for finger food appetizers"
                ]
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
                [
                        "Pan-Sear Gnocchi",
                        "Heat butter and olive oil in a large 12-inch nonstick or cast-iron skillet over medium heat. Add uncooked gnocchi in a single layer. Saut\u00e9 undisturbed for 4 minutes until golden and lightly crisped, then flip and saut\u00e9 2 more minutes. Transfer gnocchi to a plate."
                ],
                [
                        "Saut\u00e9 Aromatics",
                        "In the same skillet, reduce heat to medium-low. Add minced garlic and crushed red pepper flakes; saut\u00e9 for 45 seconds until fragrant without browning."
                ],
                [
                        "Build Lemon Ricotta Sauce",
                        "Add whole-milk ricotta, lemon zest, lemon juice, broth, and grated parmesan. Whisk gently over low heat until a silky, creamy sauce forms (about 1 minute)."
                ],
                [
                        "Combine & Wilt Spinach",
                        "Return crisped gnocchi to the skillet and add fresh baby spinach. Toss gently over low heat for 1\u20132 minutes until spinach is just wilted and glossy sauce coats each dumpling."
                ],
                [
                        "Garnish & Serve",
                        "Season with flaky sea salt and lots of freshly cracked black pepper. Sprinkle generously with toasted pine nuts and extra shaved parmesan. Serve immediately!"
                ]
        ],
        "pro_tip_title": "Elena\u2019s No-Boil Skillet Crunch Rule",
        "pro_tip": "Skip the boiling water pot entirely! Shelf-stable vacuum-packed gnocchi already contain enough internal moisture to steam through in the pan. Searing them directly in foaming butter gives you a golden, slightly caramelized outer shell with a light, cloud-like center that holds onto the creamy lemon ricotta sauce infinitely better.",
        "faqs": [
                [
                        "Can I use cauliflower gnocchi?",
                        "Yes! For frozen cauliflower gnocchi (like Trader Joe's), cook in a dry skillet over medium-high heat first to cook off moisture, then add oil/butter and sear until crispy before adding the sauce."
                ],
                [
                        "Can I substitute cottage cheese for ricotta?",
                        "You can, but blend the cottage cheese in a small blender until completely smooth first; otherwise, curds will separate when heated."
                ],
                [
                        "Can I add protein to this dish?",
                        "Saut\u00e9ed garlic shrimp, sliced grilled chicken breast, or crispy prosciutto crumbles pair exquisitely with the lemon ricotta sauce."
                ]
        ],
        "wiki_entities": [
                [
                        "Gnocchi",
                        "https://en.wikipedia.org/wiki/Gnocchi"
                ],
                [
                        "Ricotta",
                        "https://en.wikipedia.org/wiki/Ricotta"
                ],
                [
                        "Lemon",
                        "https://en.wikipedia.org/wiki/Lemon"
                ]
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
        "quick_answer": "To make 20-minute sheet-pan harissa honey salmon, arrange 4 salmon fillets and 1 lb trimmed asparagus on a parchment-lined baking sheet. Whisk 2 tbsp mild rose harissa paste, 2 tbsp honey, 1 tbsp olive oil, 2 cloves minced garlic, and 1 tbsp lemon juice. Brush glaze over salmon and drizzle remaining oil over asparagus. Roast at 425\u00b0F (220\u00b0C) for 12\u201314 minutes until salmon flakes easily with a fork, then top with crumbled feta and fresh mint.",
        "takeaways": [
                [
                        "Caramelized Sweet Heat",
                        "The natural sugars in honey caramelize under high heat, taming harissa's smoky chile punch into an irresistible sticky glaze."
                ],
                [
                        "Single Sheet Pan Simplicity",
                        "Roasting salmon and asparagus at 425\u00b0F synchronizes cooking times perfectly: tender-crisp greens and flaky, succulent fish."
                ],
                [
                        "Feta & Mint Contrast",
                        "Tangy, briny feta cheese and fresh cooling mint cut through rich omega-3 salmon fats for restaurant-level flavor complexity."
                ]
        ],
        "matrix_title": "Harissa Paste Spice Level & Flavor Profiles",
        "matrix_headers": [
                "Harissa Variety",
                "Heat Level",
                "Flavor Notes",
                "Best Application",
                "Recommendation"
        ],
        "matrix_rows": [
                [
                        "Rose Harissa Paste",
                        "Medium-Gentle",
                        "Floral rose petals, cumin, coriander",
                        "Glazed salmon & roast veggies",
                        "Gold Standard (Recommended)"
                ],
                [
                        "Smoky Tunisian Harissa",
                        "Hot & Bold",
                        "Deep smoked red peppers, garlic",
                        "Hearty stews & roasted meats",
                        "Great for heat lovers"
                ],
                [
                        "Dry Harissa Spice Blend",
                        "Adjustable",
                        "Pure powdered spices, earthier",
                        "Dry rubs & marinades",
                        "Whisk with oil & honey first"
                ],
                [
                        "Sriracha + Smoked Paprika",
                        "Medium-Sweet",
                        "Garlicky, vinegar tang",
                        "Quick emergency pantry substitute",
                        "Acceptable swap"
                ]
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
                [
                        "Preheat Oven & Prep Pan",
                        "Preheat oven to 425\u00b0F (220\u00b0C). Line a large rimmed baking sheet with parchment paper or foil for zero-scrub cleanup."
                ],
                [
                        "Whisk Honey Harissa Glaze",
                        "In a small bowl, whisk together harissa paste, honey, 1 tbsp olive oil, grated garlic, lemon juice, and a pinch of salt until glossy and blended."
                ],
                [
                        "Assemble Sheet Pan",
                        "Arrange salmon fillets skin-side down in the center of the pan. Spread asparagus spears and thin lemon slices around the fish. Toss asparagus with remaining 1 tbsp olive oil, salt, and pepper."
                ],
                [
                        "Glaze Salmon",
                        "Spoon and brush the harissa honey glaze generously over the top and sides of each salmon fillet."
                ],
                [
                        "Roast & Broil",
                        "Roast for 12\u201314 minutes until salmon reaches 130\u00b0F internal temperature and flakes easily with a fork. For extra caramelized char, switch to broil for the final 90 seconds."
                ],
                [
                        "Garnish & Serve",
                        "Scatter crumbled feta cheese, fresh mint leaves, and toasted sesame seeds over the hot salmon and asparagus. Serve immediately with warm pita or fluffy couscous!"
                ]
        ],
        "pro_tip_title": "Elena\u2019s 90-Second Broiler Glaze Caramelizer",
        "pro_tip": "For that jaw-dropping restaurant char, switch your oven from Bake to High Broil for the final 90 seconds of cooking. Watch closely: the honey and harissa paste will bubble furiously and form deeply caramelized, lacquer-like charred edges while leaving the center of the salmon pink, silky, and melt-in-your-mouth moist.",
        "faqs": [
                [
                        "What if I don't have harissa paste?",
                        "You can substitute 2 tbsp tomato paste mixed with 1 tsp smoked paprika, 1/2 tsp ground cumin, 1/4 tsp cayenne pepper, and a dash of hot sauce."
                ],
                [
                        "Can I make this with chicken or shrimp instead?",
                        "Yes! Boneless chicken cutlets take 15\u201318 minutes at 425\u00b0F. For peeled jumbo shrimp, roast for just 7\u20138 minutes."
                ],
                [
                        "How do I know when salmon is perfectly cooked?",
                        "Gently press down on the top of the fillet with a fork or your finger; if the flakes begin to separate cleanly along the white fat lines, it is perfectly cooked. Avoid overcooking!"
                ]
        ],
        "wiki_entities": [
                [
                        "Salmon as food",
                        "https://en.wikipedia.org/wiki/Salmon_as_food"
                ],
                [
                        "Harissa",
                        "https://en.wikipedia.org/wiki/Harissa"
                ],
                [
                        "Asparagus",
                        "https://en.wikipedia.org/wiki/Asparagus"
                ]
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
        "quick_answer": "To make 15-minute creamy gochujang pasta, boil 12 oz rigatoni until al dente, reserving 1 cup of pasta cooking water. In a large skillet over medium heat, melt 2 tbsp butter with 1 tbsp olive oil. Saut\u00e9 4 minced garlic cloves and 2 finely chopped shallots for 2 minutes. Stir in 2 tbsp Korean gochujang paste and 1 tbsp tomato paste, cooking 2 minutes until deeply caramelized and fragrant. Pour in 3/4 cup heavy cream and 1/2 cup reserved pasta water, stirring until silky. Toss in rigatoni and 1/2 cup grated parmesan, garnishing with scallions and sesame seeds.",
        "takeaways": [
                [
                        "Paste Caramelization Key",
                        "Blooming gochujang and tomato paste in hot butter mellows sharp chile edges and deepens savory fermented glutamates."
                ],
                [
                        "Cream & Cheese Balancing Act",
                        "Heavy cream and salty Parmigiano-Reggiano temper gochujang's heat into a velvety, restaurant-grade gloss."
                ],
                [
                        "Scallion & Sesame Freshness",
                        "Raw scallions and nutty toasted sesame seeds provide essential sharpness and crunch against the rich sauce."
                ]
        ],
        "matrix_title": "Spicy Cream Pasta Sauce Base Comparison",
        "matrix_headers": [
                "Sauce Base",
                "Spice Level",
                "Umami Depth",
                "Sweetness",
                "Verdict"
        ],
        "matrix_rows": [
                [
                        "Gochujang + Cream",
                        "Medium warm heat",
                        "Deep fermented umami",
                        "Natural rice sweetness",
                        "Gold Standard Viral Pick (Recommended)"
                ],
                [
                        "Classic Vodka Sauce",
                        "Mild warmth",
                        "Savory tomato-rich",
                        "Subtle onion sweetness",
                        "Traditional Italian-American classic"
                ],
                [
                        "Calabrian Chile + Cream",
                        "Sharp, fiery kick",
                        "Fruity & acidic",
                        "Very low",
                        "Bold & sharp for heat lovers"
                ],
                [
                        "Sriracha + Cream",
                        "Direct vinegary heat",
                        "Moderate garlic notes",
                        "Medium corn sweetness",
                        "Pantry emergency alternative"
                ]
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
                [
                        "Boil Pasta",
                        "Bring a large pot of salted water to a rolling boil. Cook rigatoni until 1 minute shy of al dente. Reserve 1 cup of starchy pasta water before draining."
                ],
                [
                        "Saut\u00e9 Aromatics",
                        "While pasta cooks, melt butter with olive oil in a large deep skillet over medium heat. Add minced garlic and shallots; cook for 2 minutes until translucent and fragrant."
                ],
                [
                        "Caramelize the Pastes",
                        "Add gochujang paste and tomato paste to the skillet. Cook, stirring constantly for 2 minutes, allowing the pastes to caramelize into a deep burgundy-red oil."
                ],
                [
                        "Emulsify Cream Sauce",
                        "Pour in heavy cream and 1/2 cup reserved pasta water. Whisk continuously over medium-low heat until a smooth, vibrant orange cream sauce forms (about 2 minutes)."
                ],
                [
                        "Toss with Pasta",
                        "Add drained rigatoni directly to the sauce. Toss vigorously over low heat for 1\u20132 minutes, adding more pasta water a tablespoon at a time until sauce clings to every tube."
                ],
                [
                        "Garnish & Serve",
                        "Remove from heat, fold in grated Parmigiano-Reggiano, and garnish generously with sliced scallions, toasted sesame seeds, and extra parmesan. Enjoy immediately!"
                ]
        ],
        "pro_tip_title": "Elena\u2019s Paste Caramelization Secret",
        "pro_tip": "Do not rush pouring the heavy cream into the pan! Always fry the gochujang and tomato paste directly in the foaming butter and aromatics for a full 2 minutes until it darkens into a deep brick-red oil. This caramelizes the fermented sugars in the gochujang, eliminating raw bitterness and unlocking an addictive, deeply savory umami foundation.",
        "faqs": [
                [
                        "Is gochujang paste extremely spicy?",
                        "Most commercial gochujang pastes are medium in heat. Combined with 3/4 cup of heavy cream and parmesan, the heat softens into a warm, cozy tingle rather than a burning spice."
                ],
                [
                        "Can I make this dairy-free or vegan?",
                        "Yes! Substitute full-fat coconut cream or cashew cream for the heavy cream, use vegan butter, and finish with nutritional yeast or dairy-free parmesan."
                ],
                [
                        "Can I add protein to gochujang pasta?",
                        "Crispy diced bacon or pancetta, grilled chicken breast strips, or saut\u00e9ed garlic butter shrimp make sensational protein additions!"
                ]
        ],
        "wiki_entities": [
                [
                        "Gochujang",
                        "https://en.wikipedia.org/wiki/Gochujang"
                ],
                [
                        "Rigatoni",
                        "https://en.wikipedia.org/wiki/Rigatoni"
                ],
                [
                        "Vodka sauce",
                        "https://en.wikipedia.org/wiki/Vodka_sauce"
                ]
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
        "quick_answer": "To make 15-minute Thai basil chicken (Pad Krapow Gai), whisk 1.5 tbsp oyster sauce, 1 tbsp soy sauce, 1 tsp dark soy sauce, 1 tsp fish sauce, and 1 tsp brown sugar. In a screaming-hot wok with 2 tbsp oil, fry 6 minced garlic cloves and 3 sliced Thai bird's eye chilies for 30 seconds. Add 1 lb ground chicken and stir-fry undisturbed until caramelized (3\u20134 mins). Pour sauce over chicken, toss until glazed, take off heat, and fold in 2 large cups of fresh holy basil or Thai sweet basil. Serve with jasmine rice and a crispy fried egg.",
        "takeaways": [
                [
                        "Screaming Wok Heat",
                        "High heat caramelizes minced chicken juices into savory browned bits without boiling or steaming the meat."
                ],
                [
                        "Dark Soy Color & Depth",
                        "Dark soy sauce imparts the signature deep caramel hue and subtle molasses sweetness seen on Bangkok street carts."
                ],
                [
                        "Off-Heat Basil Wilt",
                        "Folding basil in off the heat prevents bruising and preserves delicate essential oils and spicy peppery aromas."
                ]
        ],
        "matrix_title": "Basil Variety Comparison for Pad Krapow",
        "matrix_headers": [
                "Basil Type",
                "Flavor Profile",
                "Aroma Strength",
                "Heat Resistance",
                "Authenticity"
        ],
        "matrix_rows": [
                [
                        "Thai Holy Basil (Krapow)",
                        "Peppery, clove-like, pungent",
                        "Intense & sharp",
                        "High",
                        "100% Authentic Bangkok Standard (Recommended)"
                ],
                [
                        "Thai Sweet Basil (Horapa)",
                        "Anise, sweet licorice notes",
                        "Strong & aromatic",
                        "Medium-High",
                        "Excellent & accessible alternative"
                ],
                [
                        "Italian Sweet Basil",
                        "Sweet, floral, mild mint",
                        "Mild",
                        "Medium",
                        "Acceptable pantry swap (add pinch of black pepper)"
                ],
                [
                        "Purple Opal Basil",
                        "Earthy, mild clove",
                        "Medium",
                        "Medium",
                        "Good visual & aromatic swap"
                ]
        ],
        "ingredients": [
                "1 lb ground chicken (or finely hand-minced chicken thighs)",
                "2 cups fresh holy basil or Thai sweet basil leaves (loosely packed)",
                "6 cloves garlic, finely minced or pounded in mortar",
                "3\u20135 Thai bird's eye chilies, thinly sliced (adjust to spice preference)",
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
                [
                        "Mix Savory Sauce",
                        "In a small ramekin, whisk together oyster sauce, regular soy sauce, dark soy sauce, fish sauce, and brown sugar until sugar dissolves. Set next to stove."
                ],
                [
                        "Fry Crispy Thai Eggs",
                        "Heat 2 tbsp oil in a wok or deep skillet over high heat until shimmering. Crack an egg directly into hot oil; spoon hot oil over egg white until edges bubble and turn deeply crispy and lace-like while yolk remains runny (about 90 seconds). Transfer egg to a plate. Repeat for remaining eggs."
                ],
                [
                        "Sear Garlic & Chilies",
                        "In the remaining hot oil in the wok, add minced garlic and sliced Thai chilies. Stir-fry vigorously for 30 seconds until intensely aromatic (do not burn garlic)."
                ],
                [
                        "Caramelize Chicken",
                        "Add ground chicken, breaking it apart with a wooden spoon or spatula. Spread across the hot surface and let sear undisturbed for 2 minutes to develop deep golden caramelization, then stir-fry 2 more minutes until cooked through."
                ],
                [
                        "Glaze with Sauce",
                        "Pour the prepared sauce mixture over the hot chicken. Stir-fry vigorously over high heat for 1 minute until sauce reduces into a glossy, dark savory lacquer coating every morsel of chicken."
                ],
                [
                        "Fold Basil & Serve",
                        "Turn off the heat immediately. Toss in the fresh basil leaves, folding gently for 30 seconds until just wilted by residual heat. Spoon over warm jasmine rice, crown with a crispy fried egg, and serve with lime wedges!"
                ]
        ],
        "pro_tip_title": "Elena\u2019s Crispy Khai Dao (Fried Egg) Mastery",
        "pro_tip": "The soul of authentic Pad Krapow is the Thai-style fried egg ('Khai Dao'). Heat at least 2 tablespoons of oil until smoking hot before sliding the egg in. As the bottom bubbles and blisters into a golden, crackling lace collar, gently tilt the pan and ladle hot oil over the whites. The white becomes audibly crunchy while the yolk stays liquid gold!",
        "faqs": [
                [
                        "What if I cannot find Thai holy basil?",
                        "Thai sweet basil (with purple stems) is widely available at Asian grocery stores and works wonderfully. In a pinch, Italian sweet basil mixed with a pinch of fresh mint and cracked black pepper creates a great substitute."
                ],
                [
                        "How spicy is this dish?",
                        "With 3\u20134 bird's eye chilies, it has an authentic medium-high kick. If you prefer mild heat, use 1 chili, remove the seeds, or substitute with a sliced red jalape\u00f1o or Fresno chili."
                ],
                [
                        "Can I use ground turkey or pork?",
                        "Yes! Ground pork is the traditional alternative (Pad Krapow Moo), and ground turkey works identically with fantastic flavor."
                ]
        ],
        "wiki_entities": [
                [
                        "Phat kaphrao",
                        "https://en.wikipedia.org/wiki/Phat_kaphrao"
                ],
                [
                        "Ocimum tenuiflorum",
                        "https://en.wikipedia.org/wiki/Ocimum_tenuiflorum"
                ],
                [
                        "Bird's eye chili",
                        "https://en.wikipedia.org/wiki/Bird%27s_eye_chili"
                ]
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
        "quick_answer": "To make 20-minute creamy Marry Me chickpeas, saut\u00e9 4 minced garlic cloves and 1/3 cup chopped oil-packed sun-dried tomatoes in 2 tbsp butter over medium heat for 2 minutes. Add 2 cans (15 oz each) rinsed chickpeas, 1 tsp dried oregano, 1/2 tsp red pepper flakes, 1/2 cup vegetable broth, and 3/4 cup heavy cream. Simmer gently for 8\u201310 minutes until thickened and chickpeas are tender. Stir in 1/2 cup grated parmesan and 3 cups baby spinach until wilted, and finish with fresh basil.",
        "takeaways": [
                [
                        "Umami Sun-Dried Tomato Oil",
                        "Saut\u00e9ing garlic directly in the flavored oil from the sun-dried tomato jar creates a rich, complex flavor base in seconds."
                ],
                [
                        "Chickpea Starch Thickening",
                        "Lightly mashing a spoonful of chickpeas releases natural starches that thicken the sauce into a luxurious velvety gravy."
                ],
                [
                        "High-Fiber Plant Powerhouse",
                        "With 9 grams of dietary fiber and 16 grams of plant protein per serving, this comforting dish is as wholesome as it is decadent."
                ]
        ],
        "matrix_title": "Plant-Protein Bases for Marry Me Sauce",
        "matrix_headers": [
                "Protein Base",
                "Sauce Adhesion",
                "Simmer Time",
                "Protein per Serving",
                "Verdict"
        ],
        "matrix_rows": [
                [
                        "Canned Chickpeas (Garbanzo)",
                        "Absorbs cream deeply, velvety chew",
                        "8-10 minutes",
                        "16g protein",
                        "Gold Standard Winner (Recommended)"
                ],
                [
                        "Cannellini White Beans",
                        "Ultra-creamy, softer texture",
                        "6-8 minutes",
                        "14g protein",
                        "Excellent velvety substitute"
                ],
                [
                        "Crispy Pan-Seared Tofu",
                        "Crispy exterior, chewy interior",
                        "12-15 minutes",
                        "18g protein",
                        "Great for extra crunch"
                ],
                [
                        "Steamed Green Lentils",
                        "Earthy & hearty",
                        "10 minutes",
                        "17g protein",
                        "Rich & rustic alternative"
                ]
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
                [
                        "Saut\u00e9 Aromatics in Tomato Oil",
                        "In a large deep skillet or Dutch oven, heat butter and 1 tbsp reserved sun-dried tomato oil over medium heat. Add minced garlic, sliced sun-dried tomatoes, dried oregano, dried thyme, and red pepper flakes. Saut\u00e9 for 2 minutes until fragrant and oil turns ruby-orange."
                ],
                [
                        "Add Chickpeas & Simmer",
                        "Pour in rinsed chickpeas, vegetable broth, and heavy cream. Stir well to combine. Bring to a gentle simmer over medium-low heat and cook for 8\u201310 minutes, stirring occasionally, until sauce thickens to your liking."
                ],
                [
                        "Light Mash for Extra Body",
                        "Use the back of a wooden spoon or potato masher to crush about 1/4 cup of the chickpeas directly against the bottom of the pan. Stir into the sauce to instantly create a velvety, cohesive texture."
                ],
                [
                        "Melt Cheese & Wilt Greens",
                        "Reduce heat to low. Stir in grated Parmigiano-Reggiano and fresh baby spinach. Cook for 1\u20132 minutes until the spinach is just wilted and cheese is completely melted."
                ],
                [
                        "Garnish & Serve",
                        "Remove from heat, fold in fresh torn basil, and season to taste with flaky sea salt and cracked black pepper. Serve piping hot with toasted thick slices of sourdough bread for dipping!"
                ]
        ],
        "pro_tip_title": "Elena\u2019s Starch-Crush Velvety Sauce Secret",
        "pro_tip": "Before taking the pan off the heat, take the back of your wooden spoon and crush about 15\u201320 chickpeas directly against the side or bottom of the pan! The creamy mashed chickpeas release natural starch that effortlessly binds the cream and cheese with the broth, creating a luxurious, restaurant-quality emulsion without having to add cornstarch or flour.",
        "faqs": [
                [
                        "Can I make this dairy-free or vegan?",
                        "Yes! Replace the heavy cream with full-fat canned coconut milk or unsweetened cashew cream, use vegan butter or extra olive oil, and swap the parmesan for nutritional yeast or vegan parmesan."
                ],
                [
                        "What should I serve with Marry Me chickpeas?",
                        "Warm crusty sourdough or garlic naan is unbeatable for scooping up the velvety sauce! It also pairs wonderfully served over buttered egg noodles, orzo, or fluffy jasmine rice."
                ],
                [
                        "How do I store and reheat leftovers?",
                        "Store in an airtight glass container in the refrigerator for up to 4 days. Reheat gently in a saucepan over medium-low heat with a small splash of broth or water to loosen the cream sauce."
                ]
        ],
        "wiki_entities": [
                [
                        "Chickpea",
                        "https://en.wikipedia.org/wiki/Chickpea"
                ],
                [
                        "Sun-dried tomato",
                        "https://en.wikipedia.org/wiki/Sun-dried_tomato"
                ],
                [
                        "Parmigiano Reggiano",
                        "https://en.wikipedia.org/wiki/Parmigiano_Reggiano"
                ]
        ],
        "pinterest": {
                "board": "Quick Weeknight Dinners / One-Pot Dinners",
                "title": "20-Minute Creamy Marry Me Chickpeas Recipe (Rich One-Pot Dinner!)",
                "desc": "The vegetarian version of viral Marry Me chicken that everyone falls in love with! Plump chickpeas in a velvety garlic sun-dried tomato parmesan cream sauce with spinach and basil. Save this 20-minute dinner!",
                "tags": "#marrymechickpeas #onepotdinners #20minutedinner #vegetarianrecipes #chickpearecipes #meatlessmonday #pastatiktok"
        }
},

    {
        "slug": "15-minute-creamy-garlic-boursin-pasta",
        "title": "15-Minute Creamy Garlic Boursin Pasta",
        "headline": "15-Minute Creamy Garlic Boursin Pasta (One-Pot Viral Sensation)",
        "badge": "15-Minute Meals &bull; Viral Comfort",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/creamy-boursin-pasta.jpg",
        "image_file": "creamy-boursin-pasta.jpg",
        "excerpt": "Al dente rigatoni coated in melting garlic and fine herbs Boursin cheese with sweet blistered cherry tomatoes, spinach, and toasted golden breadcrumbs in 15 minutes.",
        "description": "Velvety one-pan rigatoni simmered with garlic and herbs Boursin cheese, sweet blistered cherry tomatoes, wilted baby spinach, and crisp golden panko.",
        "keywords": "boursin pasta, creamy boursin pasta recipe, 15 minute weeknight pasta, one pot boursin pasta, garlic herb cheese pasta, easy vegetarian dinner",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "French-Italian",
        "calories": "520 kcal",
        "protein": "16g",
        "fat": "24g",
        "carbs": "58g",
        "fiber": "4g",
        "sodium": "490mg",
        "ratingValue": "4.9",
        "reviewCount": "174",
        "quick_answer": "To make 15-minute creamy garlic Boursin pasta, boil 12 oz rigatoni until al dente, reserving 1 cup of pasta water. In a large skillet with 1 tbsp olive oil, blister 2 cups cherry tomatoes over medium-high heat until bursting (4 mins). Lower heat, drop in one 5.2 oz wheel of garlic & fine herbs Boursin cheese, 1/2 cup pasta water, and 4 cups baby spinach. Stir until a silky sauce forms, toss in pasta, and crown with toasted garlic panko breadcrumbs.",
        "takeaways": [
            ("Emulsion Magic", "Starchy salted pasta water turns rich Boursin cheese into a restaurant-glossy pan emulsion without needing heavy cream."),
            ("Blistered Sweetness", "High heat caramelizes tomato skins in 4 minutes, releasing acidic juices that slice through creamy cheese."),
            ("Panko Crunch Factor", "Toasting panko in a dash of olive oil adds crucial textural contrast that elevates weeknight comfort food.")
        ],
        "matrix_title": "Boursin Cheese Flavor Base Comparison",
        "matrix_headers": ["Cheese Base", "Flavor Profile", "Melt Rate", "Sauce Richness", "Verdict"],
        "matrix_rows": [
            ["Garlic & Fine Herbs Boursin", "Classic allium, parsley, chives", "Instant creamy melt", "Velvety & luxurious", "Gold Standard (Recommended)"],
            ["Shallot & Chive Boursin", "Mild sweet onion, delicate herbs", "Instant melt", "Silky & balanced", "Fabulous gourmet substitute"],
            ["Black Pepper Boursin", "Bold, peppery kick", "Instant melt", "Punchy & savory", "Great for cacio e pepe lovers"],
            ["Plain Cream Cheese + Garlic", "Mild lactic tang", "Requires whisking", "Heavier, less aromatic", "Budget emergency swap"]
        ],
        "ingredients": [
            "12 oz rigatoni or penne pasta",
            "1 wheel (5.2 oz) Boursin Garlic & Fine Herbs Gournay Cheese",
            "2 cups sweet cherry tomatoes (left whole)",
            "4 cups fresh baby spinach",
            "3 cloves garlic, thinly sliced",
            "2 tbsp extra virgin olive oil (divided)",
            "1/3 cup panko breadcrumbs",
            "1/2 cup freshly grated Pecorino Romano or Parmesan",
            "1 cup reserved starchy pasta cooking water",
            "1/4 tsp crushed red pepper flakes",
            "Kosher salt and freshly cracked black pepper"
        ],
        "instructions": [
            ("Boil Pasta & Toast Panko", "Boil rigatoni in heavily salted water until 1 minute shy of al dente. Reserve 1 cup pasta water, then drain. Meanwhile, toast panko in a small skillet with 1 tsp olive oil until deep golden (2 mins); set aside."),
            ("Blister Tomatoes", "In a deep 12-inch skillet, heat remaining olive oil over medium-high. Add cherry tomatoes and sliced garlic with a pinch of salt. Cook undisturbed for 3–4 minutes until skins blister and burst."),
            ("Melt the Boursin", "Reduce heat to low. Place the unwrapped Boursin wheel directly into the skillet. Pour in 1/2 cup reserved pasta water and stir gently with a wooden spoon as it melts into a velvety cream sauce."),
            ("Fold Spinach & Pasta", "Add baby spinach and drained rigatoni. Toss continuously over low heat for 1–2 minutes until spinach wilts and glossy sauce clings tightly to every ridge of pasta. Splash extra pasta water if needed."),
            ("Garnish & Serve", "Remove from heat, fold in grated Pecorino, and top with toasted golden panko and fresh black pepper. Serve piping hot!")
        ],
        "pro_tip_title": "Elena’s Liquid Gold Emulsion Secret",
        "pro_tip": "Never drain your pasta without scooping out a cup of hot pasta water first! The starch molecules in the water bond with the fat in the Boursin cheese, turning what could be an oily separation into a velvety, mirror-smooth restaurant glaze that coats every single noodle.",
        "faqs": [
            ("Can I make Boursin pasta with chicken or shrimp?", "Yes! Sear 1 pound of diced chicken breast or peeled shrimp in the skillet first, transfer to a plate, blister the tomatoes, build the sauce, and fold the cooked protein back in at the end."),
            ("Can I bake this like the viral baked feta pasta?", "Absolutely. Place tomatoes and the Boursin wheel into a baking dish with olive oil and bake at 400°F for 20 minutes, then mash with cooked pasta and spinach."),
            ("How do I store and reheat leftovers?", "Store in an airtight container in the fridge for up to 4 days. Reheat gently in a skillet with a splash of milk or water over medium-low heat to restore the creamy consistency.")
        ],
        "wiki_entities": [
            ("Boursin cheese", "https://en.wikipedia.org/wiki/Boursin_cheese"),
            ("Pasta", "https://en.wikipedia.org/wiki/Pasta")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / 30-Minute Meals",
            "title": "15-Minute Creamy Garlic Boursin Pasta Recipe (Viral One-Pot Dinner!)",
            "desc": "The easiest 15-minute weeknight dinner ever! Melt-in-your-mouth garlic and fine herbs Boursin cheese tossed with rigatoni, sweet blistered tomatoes, baby spinach, and golden panko. Save this viral recipe tonight!",
            "tags": "#boursinpasta #15minutedinner #onepotpasta #weeknightdinners #easyrecipes #pastatiktok #comfortfood"
        }
    },
    {
        "slug": "20-minute-sheet-pan-pesto-chicken",
        "title": "20-Minute Sheet-Pan Pesto Chicken and Mozzarella",
        "headline": "20-Minute Sheet-Pan Pesto Chicken and Mozzarella (Zero Cleanup Dinner)",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/sheet-pan-pesto-chicken.jpg",
        "image_file": "sheet-pan-pesto-chicken.jpg",
        "excerpt": "Juicy chicken cutlets baked with basil pesto, sweet cherry tomatoes, and gooey melted fresh mozzarella on one sheet pan in 20 minutes.",
        "description": "Succulent chicken breasts smothered in fragrant basil pesto, crowned with melted fresh mozzarella slices, and roasted alongside sweet blistered tomatoes.",
        "keywords": "sheet pan pesto chicken, baked pesto chicken mozzarella, 20 minute dinner, easy sheet pan suppers, low carb chicken recipes, quick weeknight meals",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American",
        "calories": "440 kcal",
        "protein": "42g",
        "fat": "26g",
        "carbs": "6g",
        "fiber": "2g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "158",
        "quick_answer": "To make 20-minute sheet-pan pesto chicken, arrange 4 thin-cut chicken cutlets on a parchment-lined baking sheet surrounded by 2 cups cherry tomatoes tossed in olive oil. Season chicken with Italian herbs, slather each cutlet with 1.5 tbsp basil pesto, and top with thick slices of fresh mozzarella. Roast at 425°F (220°C) for 14–16 minutes until cheese is golden bubbly and chicken registers 165°F. Drizzle with balsamic glaze and fresh basil.",
        "takeaways": [
            ("Cutlet Advantage", "Using thin-cut cutlets ensures the chicken cooks through to 165°F in exactly 15 minutes without drying out the edges."),
            ("Pesto Moisture Barrier", "Spoon-coating pesto under the mozzarella creates a protective fat-and-herb shield that keeps poultry ultra-juicy."),
            ("Single Pan Ease", "Parchment paper lining means zero pan scrubbing and a total prep-to-clean cycle under 25 minutes.")
        ],
        "matrix_title": "Pesto Selection Performance Matrix",
        "matrix_headers": ["Pesto Style", "Freshness / Flavor", "Bake Stability", "Fat Balance", "Recommendation"],
        "matrix_rows": [
            ["Refrigerated Fresh Basil Pesto", "Vibrant herb, bright garlic", "Retains green color", "Extra virgin olive oil base", "Top Choice (Highest Flavor)"],
            ["Shelf-Stable Jarred Pesto", "Muted herbal notes", "Darkens slightly", "Oil heavy", "Convenient pantry backup"],
            ["Homemade 5-Minute Pesto", "Peak freshness & pine nut crunch", "Excellent", "Customizable", "Gourmet weekend option"],
            ["Sun-Dried Tomato Pesto", "Tangy, sweet, umami", "Deep caramelization", "Rich", "Delicious variation"]
        ],
        "ingredients": [
            "4 thin-cut boneless skinless chicken breasts (or 2 large breasts halved horizontally)",
            "1/2 cup prepared basil pesto (refrigerated preferred)",
            "8 oz fresh whole-milk mozzarella cheese, sliced into 8 rounds",
            "2 cups cherry tomatoes (red and yellow mix)",
            "1.5 tbsp extra virgin olive oil",
            "1 tsp Italian seasoning (oregano, basil, thyme)",
            "1/2 tsp garlic powder",
            "Fresh cracked black pepper and kosher salt",
            "Fresh basil leaves and balsamic glaze for garnish"
        ],
        "instructions": [
            ("Prep Oven & Sheet Pan", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper for effortless cleanup."),
            ("Season Chicken & Veggies", "Pat chicken cutlets completely dry. Lay on the baking sheet and season both sides with salt, pepper, garlic powder, and Italian seasoning. Scatter cherry tomatoes around the cutlets, drizzle tomatoes with olive oil, and toss to coat."),
            ("Slather & Layer", "Generously spoon 2 tablespoons of basil pesto over the top of each chicken cutlet. Drape two thick slices of fresh mozzarella over each piece of chicken."),
            ("Bake to Bubbly Perfection", "Bake for 14–16 minutes until the chicken reaches 165°F internally and tomatoes are blistered. Switch to broiler on HIGH for 1–2 minutes if desired for golden blistered cheese spots."),
            ("Garnish & Serve", "Remove from oven, rest for 3 minutes, then scatter fresh torn basil leaves and drizzle with sweet aged balsamic glaze. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Cutlet Moisture Rule",
        "pro_tip": "Always use thin-cut chicken cutlets (about 1/2-inch thick). Thick whole chicken breasts take 25–30 minutes to bake, causing the fresh mozzarella on top to weep moisture and over-brown before the meat is safely cooked through. Thin cutlets bake in sync with the cheese and blistered tomatoes!",
        "faqs": [
            ("Can I make this with chicken thighs?", "Yes! Use boneless skinless chicken thighs. They take approximately 18–20 minutes at 425°F. Add the cheese for the final 6 minutes so it melts without over-browning."),
            ("What should I serve with sheet-pan pesto chicken?", "It pairs beautifully with crusty garlic bread, a crisp Caesar salad, garlic butter pasta, or over a bed of fluffy orzo."),
            ("Can I meal prep this dish?", "Yes. Store in airtight containers for up to 4 days. Reheat in an oven or air fryer at 350°F for 4–5 minutes to keep the cheese gooey.")
        ],
        "wiki_entities": [
            ("Pesto", "https://en.wikipedia.org/wiki/Pesto"),
            ("Mozzarella", "https://en.wikipedia.org/wiki/Mozzarella")
        ],
        "pinterest": {
            "board": "Sheet Pan Suppers / Easy Dinners",
            "title": "20-Minute Sheet-Pan Pesto Chicken and Mozzarella Recipe (Juicy & Low Carb)",
            "desc": "The easiest 20-minute weeknight dinner! Tender chicken baked with aromatic basil pesto, melted fresh mozzarella, and sweet burst cherry tomatoes on one pan with zero cleanup. Try it tonight!",
            "tags": "#pestochicken #sheetpandinner #20minutedinner #easyweeknightdinner #lowcarbrecipes #glutenfreerecipes #chickenbreastrecipes"
        }
    },
    {
        "slug": "20-minute-garlic-butter-steak-gnocchi",
        "title": "20-Minute Garlic Butter Steak and Gnocchi Skillet",
        "headline": "20-Minute Garlic Butter Steak and Gnocchi Skillet (Crispy & Tender)",
        "badge": "One-Pot Dinners &bull; Steakhouse Classic",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/garlic-butter-steak-gnocchi.jpg",
        "image_file": "garlic-butter-steak-gnocchi.jpg",
        "excerpt": "Caramelized seared steak bites and crispy golden potato gnocchi tossed in foaming garlic herb butter with rosemary and shaved parmesan in 20 minutes.",
        "description": "Tender sirloin steak cubes seared with a caramelized crust alongside pillowy, crisp pan-fried potato gnocchi basted in foaming garlic rosemary butter.",
        "keywords": "garlic butter steak gnocchi, steak bites recipe, pan seared gnocchi, 20 minute steak dinner, one pan comfort food, weeknight steak recipe",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American-Italian",
        "calories": "580 kcal",
        "protein": "38g",
        "fat": "30g",
        "carbs": "40g",
        "fiber": "3g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "192",
        "quick_answer": "To make 20-minute garlic butter steak and gnocchi, sear 1.25 lbs cubed sirloin or ribeye in 1 tbsp high-heat oil in a screaming hot cast iron skillet for 3–4 minutes until caramelized; transfer to a plate. In the same skillet, melt 3 tbsp butter, add 16 oz shelf-stable potato gnocchi straight from the package (no boiling!), and sauté for 6–8 minutes until golden and crisp. Return steak bites, add 4 minced garlic cloves and fresh rosemary, baste for 2 minutes, and top with parmesan.",
        "takeaways": [
            ("No Boiling Gnocchi", "Pan-frying shelf-stable gnocchi dry in foaming butter creates a shatteringly crisp exterior and pillowy dumpling center."),
            ("Searing Hot Cast Iron", "Steak bites need intense heat to achieve a deep Maillard crust in 3 minutes without overcooking the tender medium-rare interior."),
            ("Garlic Herb Baste", "Adding garlic and rosemary in the final 2 minutes infuses fragrant aromatics without scorching the garlic.")
        ],
        "matrix_title": "Best Cuts for 20-Minute Steak Bites",
        "matrix_headers": ["Steak Cut", "Tenderness", "Flavor Richness", "Pan Searing Speed", "Chef Verdict"],
        "matrix_rows": [
            ["Top Sirloin", "High", "Robust, beefy", "3–4 minutes", "Best Value & Performance (Recommended)"],
            ["Ribeye (Boneless)", "Extremely High", "Buttery, deeply marbled", "3 minutes", "Ultimate Luxury Indulgence"],
            ["New York Strip", "High", "Balanced, firm chew", "3–4 minutes", "Great steakhouse crust"],
            ["Flank Steak", "Medium", "Lean & hearty", "Requires thin bias slice", "Better for fajitas than bite cubes"]
        ],
        "ingredients": [
            "1.25 lbs top sirloin or ribeye steak, cut into 1-inch bite-sized cubes",
            "16 oz shelf-stable potato gnocchi (dry, do not boil)",
            "4 tbsp unsalted butter (divided)",
            "1 tbsp avocado or high-smoke-point olive oil",
            "4 cloves fresh garlic, finely minced",
            "2 sprigs fresh rosemary, needles stripped and minced",
            "2 sprigs fresh thyme",
            "1/3 cup freshly grated Parmesan cheese",
            "1 tsp smoked paprika and garlic powder",
            "Coarse kosher salt and cracked black pepper"
        ],
        "instructions": [
            ("Season the Steak", "Pat steak bites thoroughly dry with paper towels. Toss with olive oil, smoked paprika, garlic powder, 1 tsp kosher salt, and coarse black pepper."),
            ("Hard Sear Steak Bites", "Heat a 12-inch heavy cast-iron skillet over high heat until smoking. Add steak bites in a single layer (cook in batches if needed). Sear undisturbed for 2 minutes to build a dark crust, flip and cook 1–2 minutes more for medium-rare. Transfer steak to a plate."),
            ("Crisp the Gnocchi", "Turn heat to medium. Melt 2 tbsp butter in the same flavorful beef drippings. Pour the raw dry gnocchi directly into the skillet. Sauté, stirring frequently, for 6–8 minutes until gnocchi are deeply golden and crisp on the outside, tender inside."),
            ("Garlic Butter Rosemary Infusion", "Push gnocchi to the sides. Melt remaining 2 tbsp butter in the center. Add minced garlic, chopped rosemary, and thyme. Sizzle for 60 seconds until fragrant, tilting the pan to baste."),
            ("Toss, Top & Serve", "Return steak bites and their accumulated resting juices to the skillet. Toss everything together for 1 minute until glazed and piping hot. Remove from heat, shower with grated Parmesan, and serve straight from the skillet!")
        ],
        "pro_tip_title": "Elena’s Golden Gnocchi Rule: Never Boil!",
        "pro_tip": "Boiling gnocchi before pan-frying turns them soggy, waterlogged, and gummy. Toss shelf-stable or fresh vacuum-packed potato gnocchi directly into the hot foaming skillet butter dry! The residual starch fries into an irresistible golden hash-brown crunch while the interior steams into a soft, pillowy cloud.",
        "faqs": [
            ("Can I use frozen gnocchi?", "Yes! Thaw frozen gnocchi in the refrigerator for 2 hours or microwave for 45 seconds to remove surface ice crystals before pan-frying so excess water does not prevent browning."),
            ("What cut of meat works best on a budget?", "Top sirloin steak is our number one pick! It is lean, tender, affordable, and cooks into meltingly soft bites in under 4 minutes."),
            ("How do I store leftovers?", "Store in an airtight container for up to 3 days. Reheat in a dry skillet over medium heat for 3–4 minutes to re-crisp the gnocchi without making the steak rubbery.")
        ],
        "wiki_entities": [
            ("Gnocchi", "https://en.wikipedia.org/wiki/Gnocchi"),
            ("Steak", "https://en.wikipedia.org/wiki/Steak")
        ],
        "pinterest": {
            "board": "Steak Recipes / One-Pot Dinners",
            "title": "20-Minute Garlic Butter Steak and Gnocchi Skillet Recipe (Crispy & Juicy!)",
            "desc": "Tender, caramelized garlic butter steak bites paired with crispy pan-fried potato gnocchi and fresh rosemary. Prepared in one cast iron skillet in 20 minutes! Pin this easy weeknight steak dinner now!",
            "tags": "#steakbites #gnocchirecipe #garlicbutter #onepotmeals #castironskillet #20minutedinners #comfortfoodrecipes"
        }
    },
    {
        "slug": "15-minute-sweet-chili-chicken-meatballs",
        "title": "15-Minute Sweet Chili Garlic Chicken Meatballs",
        "headline": "15-Minute Sweet Chili Garlic Chicken Meatballs (Sticky & Glazed)",
        "badge": "15-Minute Meals &bull; High Protein",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/sweet-chili-chicken-meatballs.jpg",
        "image_file": "sweet-chili-chicken-meatballs.jpg",
        "excerpt": "Tender, juicy chicken meatballs browned crisp and glazed in a sticky, sweet chili garlic sauce with sesame seeds and green onions in 15 minutes.",
        "description": "Plump chicken meatballs seared in a hot skillet and tossed in an addictive sweet chili, garlic, soy, and ginger glaze garnished with toasted sesame seeds.",
        "keywords": "sweet chili chicken meatballs, easy weeknight meatballs, 15 minute dinner, sticky glazed meatballs, asian chicken meatballs, meal prep dinner",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Asian-Fusion",
        "calories": "390 kcal",
        "protein": "34g",
        "fat": "14g",
        "carbs": "32g",
        "fiber": "1g",
        "sodium": "680mg",
        "ratingValue": "4.9",
        "reviewCount": "142",
        "quick_answer": "To make 15-minute sweet chili chicken meatballs, mix 1 lb ground chicken with 1/3 cup panko, 1 egg, garlic, ginger, and soy sauce, rolling into 16 mini meatballs. Sear in 1 tbsp sesame oil over medium-high heat for 6–7 minutes until golden on all sides. Whisk 1/2 cup sweet Thai chili sauce, 2 tbsp low-sodium soy sauce, 1 tbsp sriracha, and 1 tsp rice vinegar. Pour glaze into the skillet, bubbling for 2 minutes until glossy and lacquered. Garnish with sesame seeds and scallions.",
        "takeaways": [
            ("High Protein Fast", "Ground chicken cutlets or thigh meat yield 34g protein per serving with a clean, light texture that absorbs bold glazes."),
            ("The 2-Minute Glaze Reduction", "Sweet chili sauce contains natural sugars that caramelize rapidly into a restaurant lacquer without cornstarch slurries."),
            ("Meal Prep Perfection", "These meatballs remain succulent when chilled and reheat beautifully over jasmine rice, cauliflower rice, or noodles.")
        ],
        "matrix_title": "Meatball Protein Texture Analysis",
        "matrix_headers": ["Meat Type", "Juiciness", "Browning Power", "Glaze Cling", "Verdict"],
        "matrix_rows": [
            ["Ground Chicken Thigh (93/7)", "Maximum tenderness", "Deep golden crust", "Exceptional", "Top Recommendation"],
            ["Ground Chicken Breast (99/1)", "Leaner", "Crisp sear", "Good (requires oil)", "Best for low-fat macros"],
            ["Ground Turkey", "Hearty & juicy", "Excellent browning", "Very Good", "Delicious 1:1 substitute"],
            ["Plant-Based Ground", "Firm", "Moderate browning", "Good", "Great vegan adaptation"]
        ],
        "ingredients": [
            "1 lb ground chicken (preferably 93/7 blend for juiciness)",
            "1/3 cup panko breadcrumbs",
            "1 large egg, beaten",
            "3 cloves garlic, finely grated",
            "1 tbsp fresh ginger, grated",
            "2 tbsp low-sodium soy sauce (divided)",
            "1 tbsp toasted sesame oil",
            "1/2 cup sweet Thai chili sauce",
            "1 tbsp sriracha or chili garlic crunch (adjust heat to taste)",
            "1 tbsp rice vinegar or lime juice",
            "2 green onions, thinly sliced",
            "1 tbsp toasted white sesame seeds"
        ],
        "instructions": [
            ("Mix Meatball Base", "In a medium bowl, combine ground chicken, panko breadcrumbs, beaten egg, grated ginger, half the minced garlic, 1 tbsp soy sauce, salt, and pepper. Mix gently until just incorporated (do not overwork)."),
            ("Shape Meatballs", "Use a 1.5-tablespoon scoop or damp hands to shape the mixture into 16 bite-sized meatballs."),
            ("Sear in Skillet", "Heat sesame oil in a large nonstick or cast-iron skillet over medium-high heat. Add meatballs in a single layer. Sear for 6–8 minutes, rolling occasionally, until golden-brown on all sides and internal temp reaches 165°F."),
            ("Simmer Sticky Glaze", "In a measuring cup, whisk sweet chili sauce, remaining 1 tbsp soy sauce, sriracha, rice vinegar, and remaining garlic. Pour sauce directly into the skillet over the hot meatballs."),
            ("Glaze & Garnish", "Simmer vigorously for 1.5 to 2 minutes, spooning sauce over meatballs until it reduces to a sticky, shimmering lacquer. Scatter sliced green onions and sesame seeds. Serve immediately over steamed rice!")
        ],
        "pro_tip_title": "Elena’s Tender Meatball Secret",
        "pro_tip": "Never compact or over-knead ground poultry! Ground chicken has very fine protein strands that turn tough and rubbery if compressed tightly. Scoop the mixture gently with damp hands, roll with a light touch, and drop straight into the hot skillet for melt-in-your-mouth tenderness.",
        "faqs": [
            ("Can I use frozen pre-cooked meatballs?", "Yes! Sauté frozen chicken or turkey meatballs in the skillet with a splash of water and oil for 6 minutes until heated through, then pour in the glaze and simmer for 2 minutes."),
            ("Can I make these in the air fryer?", "Yes! Air fry meatballs at 390°F (200°C) for 9–10 minutes, then transfer to a skillet or bowl and toss with the warm sweet chili glaze."),
            ("How do I make this gluten-free?", "Simply substitute tamari or coconut aminos for soy sauce, and use certified gluten-free panko breadcrumbs.")
        ],
        "wiki_entities": [
            ("Meatball", "https://en.wikipedia.org/wiki/Meatball"),
            ("Sweet chili sauce", "https://en.wikipedia.org/wiki/Sweet_chili_sauce")
        ],
        "pinterest": {
            "board": "Easy Weeknight Dinners / Asian Recipes",
            "title": "15-Minute Sweet Chili Garlic Chicken Meatballs Recipe (Sticky & Glazed!)",
            "desc": "Juicy, tender chicken meatballs browned and smothered in an addictive sweet chili garlic glaze with sesame seeds and scallions. Ready in 15 minutes! Perfect for weeknight dinner or high-protein meal prep.",
            "tags": "#chickenmeatballs #sweetchili #15minutemeals #easyweeknightdinner #highproteinrecipes #mealprepideas #asianfood"
        }
    },
    {
        "slug": "15-minute-mexican-turkey-taco-skillet",
        "title": "15-Minute Mexican Ground Turkey Taco Skillet",
        "headline": "15-Minute Mexican Ground Turkey Taco Skillet (One-Pan High Protein)",
        "badge": "15-Minute Meals &bull; One-Skillet",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/turkey-taco-skillet.jpg",
        "image_file": "turkey-taco-skillet.jpg",
        "excerpt": "Lean ground turkey simmered in zesty spices, black beans, sweet corn, and salsa, crowned with bubbling melted cheddar, fresh avocado, and lime in 15 minutes.",
        "description": "A rapid one-skillet Mexican dinner with seasoned ground turkey, sweet corn, tender black beans, rich salsa, melted cheese, and fresh creamy avocado.",
        "keywords": "turkey taco skillet, 15 minute mexican skillet, ground turkey dinner, healthy taco skillet, one pan taco bowl, low carb weeknight meals",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mexican-American",
        "calories": "420 kcal",
        "protein": "36g",
        "fat": "18g",
        "carbs": "28g",
        "fiber": "7g",
        "sodium": "620mg",
        "ratingValue": "4.9",
        "reviewCount": "165",
        "quick_answer": "To make a 15-minute Mexican ground turkey taco skillet, brown 1 lb lean ground turkey with 1 diced small red onion in 1 tbsp olive oil over medium-high heat for 5 minutes. Stir in 1 packet taco seasoning, 1 cup chunky salsa, 1 can rinsed black beans, and 1 cup sweet corn. Simmer for 4 minutes until thickened. Top with 1.5 cups shredded Monterey Jack and cheddar cheese, cover with a lid for 2 minutes until melted, and finish with diced avocado, cilantro, and lime.",
        "takeaways": [
            ("7 Grams Dietary Fiber", "Black beans and sweet corn infuse complex fiber, keeping you full and balancing the macros of lean turkey."),
            ("No Tortilla Cleanup", "Enjoy the vibrant flavors of loaded street tacos in a spoonable skillet served over rice, greens, or with tortilla chips."),
            ("Pantry Staple Hero", "Canned black beans, frozen corn, and jarred salsa create deep simmered flavor in under 10 minutes of active cooking.")
        ],
        "matrix_title": "Taco Skillet Cheese Melting Benchmark",
        "matrix_headers": ["Cheese Variety", "Melt Texture", "Salt / Tang", "Stretch Quotient", "Verdict"],
        "matrix_rows": [
            ["Monterey Jack + Sharp Cheddar", "Ultra-gooey, velvety", "Sharp savory tang", "High stretch", "Gold Standard (Recommended)"],
            ["Pepper Jack", "Creamy with chili flecks", "Zesty, spicy warmth", "High stretch", "Best for chili lovers"],
            ["Queso Oaxaca", "Strings like mozzarella", "Mild & buttery", "Maximum stretch", "Traditional authentic pick"],
            ["Cotija Cheese (Crumbled)", "Slightly crumbly, dry", "Salty, briny punch", "No melt stretch", "Best as a final garnish topping"]
        ],
        "ingredients": [
            "1 lb 93% lean ground turkey (or lean ground beef)",
            "1 tbsp olive oil",
            "1 small red onion, finely diced",
            "1 packet (2 tbsp) taco seasoning (cumin, chili powder, paprika, garlic)",
            "1 cup your favorite chunky tomato salsa",
            "1 can (15 oz) black beans, drained and rinsed",
            "1 cup frozen sweet corn kernels",
            "1.5 cups shredded Mexican blend cheese (Cheddar & Monterey Jack)",
            "1 ripe Hass avocado, sliced",
            "1/4 cup chopped fresh cilantro",
            "1 lime, cut into wedges",
            "Tortilla chips or warm corn tortillas for serving"
        ],
        "instructions": [
            ("Brown the Turkey", "Heat olive oil in a 12-inch oven-safe skillet over medium-high heat. Add ground turkey and diced red onion. Break apart with a wooden spoon and cook for 5 minutes until meat is browned and cooked through."),
            ("Simmer Beans & Salsa", "Stir in the taco seasoning, chunky salsa, rinsed black beans, and sweet corn. Simmer vigorously over medium heat for 3–4 minutes until liquids reduce and sauce thickens."),
            ("Melt the Cheese", "Smooth the top of the skillet and scatter the shredded Mexican cheese evenly across the meat. Cover with a lid or foil, reduce heat to low, and let steam for 2 minutes until cheese is completely melted and bubbly."),
            ("Garnish & Serve", "Remove lid. Arrange fresh avocado slices, chopped cilantro, and red onions on top. Squeeze fresh lime juice across the skillet and serve immediately with crunchy tortilla chips!")
        ],
        "pro_tip_title": "Elena’s Lean Ground Turkey Moisture Trick",
        "pro_tip": "Lean ground turkey (93/7) can dry out if cooked dry. Stirring in chunky tomato salsa directly with the taco seasoning provides an acid and moisture bath that rehydrates the meat fibers, ensuring every bite tastes as juicy as high-fat beef while slashing saturated fat by half!",
        "faqs": [
            ("Can I meal prep this taco skillet?", "Yes! Portion into meal prep containers with brown rice or quinoa. It stays fresh for 4 days in the fridge. Pack avocado and lime separately to prevent browning."),
            ("Is this recipe gluten-free?", "Yes, as long as your taco seasoning and salsa are certified gluten-free."),
            ("Can I swap the ground turkey for ground chicken or beef?", "Absolutely! 90/10 ground beef, ground chicken, or plant-based ground meat all work with identical cooking times.")
        ],
        "wiki_entities": [
            ("Taco", "https://en.wikipedia.org/wiki/Taco"),
            ("Ground turkey", "https://en.wikipedia.org/wiki/Ground_turkey")
        ],
        "pinterest": {
            "board": "Mexican Food / 15-Minute Dinners",
            "title": "15-Minute Mexican Ground Turkey Taco Skillet Recipe (Easy & Healthy!)",
            "desc": "A delicious 15-minute one-skillet dinner! Lean ground turkey, black beans, sweet corn, and salsa blanketed in melted cheese, fresh avocado, and lime. Ready in minutes with zero stress!",
            "tags": "#tacoskillet #groundturkeyrecipes #15minutedinners #onepotdinners #mexicanfood #healthydinnerideas #lowcarbrecipes"
        }
    },
    {
        "slug": "15-minute-spicy-peanut-sesame-noodles",
        "title": "15-Minute Spicy Peanut Sesame Noodles",
        "headline": "15-Minute Spicy Peanut Sesame Noodles (Creamy Chili Crunch)",
        "badge": "15-Minute Meals &bull; Plant-Powered",
        "category": "Comfort Food",
        "categories_str": "all 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/spicy-peanut-sesame-noodles.jpg",
        "image_file": "spicy-peanut-sesame-noodles.jpg",
        "excerpt": "Chewy noodles tossed in a rich garlic peanut butter and soy lime sauce, crowned with crispy chili oil, crunchy crushed peanuts, and fresh scallions in 15 minutes.",
        "description": "Slurpable noodles dressed in a velvety homemade garlic ginger peanut lime sauce, drizzled with spicy chili crunch, roasted peanuts, and herbs.",
        "keywords": "spicy peanut noodles, 15 minute peanut noodles, sesame peanut sauce, chili oil noodles, easy vegan pasta, weeknight noodle dinner",
        "prepTime": "PT7M",
        "cookTime": "PT8M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Asian-Inspired",
        "calories": "470 kcal",
        "protein": "18g",
        "fat": "22g",
        "carbs": "56g",
        "fiber": "5g",
        "sodium": "720mg",
        "ratingValue": "4.9",
        "reviewCount": "181",
        "quick_answer": "To make 15-minute spicy peanut sesame noodles, boil 10 oz ramen noodles, udon, or spaghetti according to package instructions (about 6 mins); reserve 1/2 cup pasta water and drain. In a bowl, whisk 1/2 cup creamy peanut butter, 3 tbsp low-sodium soy sauce, 1.5 tbsp maple syrup or honey, 1 tbsp toasted sesame oil, 1 tbsp lime juice, 2 cloves grated garlic, 1 tsp grated ginger, and 1 tbsp chili crisp. Whisk in warm pasta water until smooth and pourable. Toss with warm noodles, green onions, and crushed peanuts.",
        "takeaways": [
            ("The Noodle Water Whisk", "Starchy noodle water instantly emulsifies thick peanut butter into a glossy restaurant-quality coat without clumping."),
            ("Temperature Versatility", "These noodles taste sensational piping hot from the pot or chilled straight from the fridge the next day."),
            ("Pantry Staples Only", "Made entirely from shelf-stable ingredients you likely already stock in your kitchen cupboard.")
        ],
        "matrix_title": "Nut Butter Base Comparison for Savory Noodles",
        "matrix_headers": ["Nut Butter", "Flavor Profile", "Sauce Silkiness", "Authenticity", "Verdict"],
        "matrix_rows": [
            ["Creamy Peanut Butter", "Rich, nutty, comforting", "Extremely smooth", "Dan Dan / street style", "Gold Standard (Recommended)"],
            ["Chinese Sesame Paste (Zhimajiang)", "Toasty, earthy, deep", "Ultra-dense", "Authentic Sichuan", "Gourmet authentic choice"],
            ["Almond Butter", "Mild, slightly sweet", "Silky", "Western twist", "Great peanut allergy alternative"],
            ["Tahini", "Bitter sesame profile", "Smooth", "Middle Eastern fusion", "Needs extra honey/lime balance"]
        ],
        "ingredients": [
            "10 oz ramen noodles, wheat udon, or fettuccine",
            "1/2 cup creamy natural peanut butter (smooth)",
            "3 tbsp low-sodium soy sauce or tamari",
            "1.5 tbsp pure maple syrup or brown sugar",
            "1 tbsp toasted sesame oil",
            "1 tbsp fresh lime juice",
            "2 cloves garlic, finely grated",
            "1 tsp fresh ginger, grated",
            "1 to 2 tbsp crispy chili oil (chili crisp), to taste",
            "1/3 cup hot noodle cooking water (to emulsify)",
            "1/3 cup roasted salted peanuts, roughly chopped",
            "3 green onions, thinly sliced on bias",
            "Fresh cilantro leaves for garnish"
        ],
        "instructions": [
            ("Cook Noodles", "Bring a large pot of water to a boil. Cook noodles until al dente according to package instructions. Before draining, ladle out 1/2 cup of hot starchy cooking water; drain noodles and rinse briefly in warm water."),
            ("Whisk Creamy Sauce", "In a medium bowl, whisk together peanut butter, soy sauce, maple syrup, sesame oil, lime juice, grated garlic, ginger, and chili crisp. The mixture will look thick initially."),
            ("Emulsify with Noodle Water", "Pour in 1/4 cup hot noodle water while whisking vigorously until the sauce transforms into a glossy, velvety pourable dressing. Add another splash if needed."),
            ("Toss & Coat", "Add warm noodles into a large serving bowl. Pour the peanut sauce over the top and toss with tongs until every noodle strand is lavishly coated."),
            ("Top & Serve", "Shower with chopped roasted peanuts, sliced scallions, cilantro, and an extra swirl of fiery red chili oil. Serve warm or cold!")
        ],
        "pro_tip_title": "Elena’s Peanut Emulsion Secret",
        "pro_tip": "When you add cold water to peanut butter, it seizes up into a stiff, clay-like paste. The secret is adding boiling starchy pasta water! The hot liquid relaxes the nut fats while the starches bind everything together, producing a lustrous, silky coating that clings to noodles like velvet.",
        "faqs": [
            ("Can I make this peanut-free?", "Yes! Substitute creamy sunbutter (sunflower seed butter) or tahini. Both create delicious savory noodles with zero nuts."),
            ("Can I add protein or vegetables?", "Absolutely! Add shredded rotisserie chicken, seared tofu cubes, sautéed shrimp, steamed edamame, or thinly sliced bell peppers and cucumbers."),
            ("How do I store and reheat peanut noodles?", "Store in an airtight container for up to 5 days. Eat cold straight from the fridge or microwave with 1 tbsp of warm water to loosen the sauce.")
        ],
        "wiki_entities": [
            ("Peanut sauce", "https://en.wikipedia.org/wiki/Peanut_sauce"),
            ("Chili oil", "https://en.wikipedia.org/wiki/Chili_oil")
        ],
        "pinterest": {
            "board": "Noodle Recipes / 15-Minute Dinners",
            "title": "15-Minute Spicy Peanut Sesame Noodles Recipe (Creamy Chili Oil Pasta!)",
            "desc": "The ultimate quick comfort food! Chewy noodles tossed in a luxurious garlic ginger peanut sauce, crowned with crispy chili oil, crunchy peanuts, and scallions. Ready in 15 minutes! Save this recipe now!",
            "tags": "#peanutnoodles #spicynoodles #15minutedinners #easyweeknightdinner #veganrecipes #chilioil #asiannoodles"
        }
    },
    {
        "slug": "20-minute-creamy-spinach-artichoke-chicken",
        "title": "20-Minute Creamy Spinach and Artichoke Chicken Skillet",
        "headline": "20-Minute Creamy Spinach and Artichoke Chicken Skillet (One-Pan Dip Dinner)",
        "badge": "One-Pot Dinners &bull; Restaurant Favorite",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/spinach-artichoke-chicken.jpg",
        "image_file": "spinach-artichoke-chicken.jpg",
        "excerpt": "Golden pan-seared chicken cutlets simmered in a luscious parmesan garlic cream sauce loaded with tender artichoke hearts, baby spinach, and melted mozzarella in 20 minutes.",
        "description": "Everything you adore about warm spinach artichoke dip transformed into a high-protein 20-minute weeknight skillet with golden seared chicken breasts.",
        "keywords": "spinach artichoke chicken, creamy chicken skillet, 20 minute dinner, one pan chicken dinner, low carb chicken recipes, comfort food weeknight",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American-Italian",
        "calories": "480 kcal",
        "protein": "44g",
        "fat": "28g",
        "carbs": "8g",
        "fiber": "3g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "177",
        "quick_answer": "To make 20-minute creamy spinach and artichoke chicken, sear 4 seasoned chicken cutlets in 1 tbsp olive oil and 1 tbsp butter over medium-high heat for 4–5 minutes per side until golden (165°F); transfer to a plate. In the same skillet, sauté 4 cloves minced garlic for 30 seconds. Add 1 can drained chopped artichoke hearts, 4 cups fresh baby spinach, 3/4 cup heavy cream, 4 oz softened cream cheese, and 1/2 cup grated parmesan. Simmer for 3 minutes until velvety. Return chicken, top with 1/2 cup mozzarella, and melt under a lid for 2 minutes.",
        "takeaways": [
            ("Dip Turned Dinner", "Takes the beloved flavors of spinach artichoke dip and transforms them into a wholesome, low-carb 44g-protein dinner."),
            ("Pantry Artichoke Shortcut", "Canned quartered artichoke hearts packed in water or oil provide instant restaurant-grade tender acidity."),
            ("Cream Cheese Base", "Softened cream cheese delivers immediate silky body without separating or needing flour roux thickeners.")
        ],
        "matrix_title": "Artichoke Packing Medium Comparison",
        "matrix_headers": ["Packing Medium", "Flavor Profile", "Oil Content", "Acidity", "Verdict"],
        "matrix_rows": [
            ["Canned in Water", "Clean, earthy, tender", "Zero added fat", "Mild citric tang", "Top Choice (Controlled Fat)"],
            ["Marinated in Herb Oil", "Garlicky, zesty, rich", "High flavor oils", "Bright herbaceous acid", "Delicious punchy alternative"],
            ["Frozen Artichoke Hearts", "Firmest bite, grassy", "Zero fat", "Fresh neutral", "Requires 5 min pre-thaw"],
            ["Whole Fresh Artichokes", "Prime luxury flavor", "Zero fat", "Natural sweet floral", "Too labor-intensive for 20 mins"]
        ],
        "ingredients": [
            "4 boneless skinless chicken breasts (cut into thin cutlets)",
            "1 can (14 oz) quartered artichoke hearts, drained and roughly chopped",
            "4 cups fresh baby spinach",
            "4 oz cream cheese, softened at room temperature",
            "3/4 cup heavy whipping cream or whole milk",
            "1/2 cup freshly grated Parmesan cheese",
            "1/2 cup shredded whole-milk mozzarella cheese",
            "4 cloves fresh garlic, minced",
            "1 tbsp extra virgin olive oil",
            "1 tbsp unsalted butter",
            "1 tsp Italian herb seasoning & garlic powder",
            "Kosher salt and coarse black pepper"
        ],
        "instructions": [
            ("Sear the Chicken", "Pat chicken cutlets dry. Season both sides with Italian seasoning, garlic powder, salt, and pepper. Heat olive oil and butter in a large 12-inch skillet over medium-high. Sear chicken for 4–5 minutes per side until golden brown and cooked through (165°F). Transfer to a warm plate."),
            ("Sauté Aromatics & Artichokes", "Reduce heat to medium. Add minced garlic and chopped artichoke hearts to the pan juices. Sauté for 1–2 minutes until fragrant and lightly caramelized."),
            ("Build Velvet Cream Sauce", "Add softened cream cheese and heavy cream. Whisk continuously for 2 minutes until smooth and bubbly. Stir in grated Parmesan cheese until melted into a luxurious dip-like sauce."),
            ("Wilt Spinach", "Toss in fresh baby spinach. Stir for 1–2 minutes until leaves wilt gracefully into the rich cream sauce."),
            ("Simmer & Melt", "Nestle chicken cutlets and resting juices back into the bubbling sauce. Top each cutlet with shredded mozzarella. Cover skillet with a lid for 2 minutes until cheese melts into gooey perfection. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Cream Cheese Melting Rule",
        "pro_tip": "Always bring your cream cheese to room temperature before adding it to the hot skillet! Cold cream cheese from the fridge will clump into stubborn curd-like lumps. Softened cream cheese melts like liquid silk in 30 seconds when whisked into warm cream, creating a flawless restaurant emulsion.",
        "faqs": [
            ("Can I use frozen spinach instead of fresh?", "Yes! Use 8 oz frozen chopped spinach, thawed completely, and squeeze out ALL excess liquid with paper towels before stirring into the sauce."),
            ("Can I lighten this recipe up?", "Yes. Replace heavy cream with low-sodium chicken broth mixed with 1/2 cup half-and-half, or use 1/3-less-fat Neufchâtel cream cheese."),
            ("What sides pair best with this chicken?", "Serve over buttered noodles, garlic mashed potatoes, steamed rice, or with warm crusty sourdough bread for scooping up the sauce.")
        ],
        "wiki_entities": [
            ("Spinach dip", "https://en.wikipedia.org/wiki/Spinach_dip"),
            ("Artichoke", "https://en.wikipedia.org/wiki/Artichoke")
        ],
        "pinterest": {
            "board": "Chicken Skillet Recipes / One-Pot Dinners",
            "title": "20-Minute Creamy Spinach and Artichoke Chicken Skillet Recipe (Keto & Comforting!)",
            "desc": "Your favorite warm spinach artichoke dip turned into an incredible 20-minute weeknight dinner! Tender golden chicken smothered in creamy garlic parmesan sauce and melted mozzarella. Pin this one-pan dinner tonight!",
            "tags": "#spinachartichokechicken #chickendinner #20minutedinners #onepotskillet #lowcarbrecipes #ketodinner #comfortfoodrecipes"
        }
    },
    {
        "slug": "20-minute-sheet-pan-honey-balsamic-chicken",
        "title": "20-Minute Sheet-Pan Honey Balsamic Chicken Thighs",
        "headline": "20-Minute Sheet-Pan Honey Balsamic Chicken Thighs (Sticky Glaze)",
        "badge": "Sheet Pan Suppers &bull; Sweet & Savory",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/honey-balsamic-chicken-thighs.jpg",
        "image_file": "honey-balsamic-chicken-thighs.jpg",
        "excerpt": "Juicy chicken thighs roasted with tender baby potatoes, charred red onions, and crisp asparagus glazed in a sticky, tangy honey balsamic reduction in 20 minutes.",
        "description": "Boneless chicken thighs and spring vegetables roasted on a single sheet pan with a glossy caramelized honey, balsamic, Dijon, and garlic glaze.",
        "keywords": "honey balsamic chicken, sheet pan chicken thighs, 20 minute sheet pan dinner, balsamic glazed chicken, easy weeknight meals, one pan dinner",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mediterranean-American",
        "calories": "460 kcal",
        "protein": "38g",
        "fat": "20g",
        "carbs": "32g",
        "fiber": "4g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "149",
        "quick_answer": "To make 20-minute sheet-pan honey balsamic chicken thighs, preheat oven to 425°F (220°C). Whisk 1/3 cup balsamic vinegar, 3 tbsp clover honey, 1 tbsp Dijon mustard, 3 minced garlic cloves, and 2 tbsp olive oil. Toss 1.5 lbs boneless skinless chicken thighs, 1 lb halved baby potatoes, and 1 sliced red onion in half the glaze. Roast for 10 minutes on a parchment-lined baking sheet, toss in 1 bunch trimmed asparagus, spoon remaining glaze over chicken, and roast for 8–10 minutes more until caramelized (175°F).",
        "takeaways": [
            ("Balsamic Reduction Glaze", "Honey and balsamic vinegar reduce into a sticky, restaurant-style mahogany glaze that caramelizes over intense oven heat."),
            ("Dark Meat Resilience", "Boneless skinless chicken thighs stay exceptionally juicy at high heat and absorb the sweet-acidic marinade deeply."),
            ("Veggies in Sync", "Adding asparagus during the second half of cooking prevents limp, mushy spears while letting potatoes crisp.")
        ],
        "matrix_title": "Balsamic Vinegar Grade Selection for Roasting",
        "matrix_headers": ["Balsamic Type", "Viscosity", "Sweet / Acid Balance", "Roast Caramelization", "Chef Verdict"],
        "matrix_rows": [
            ["Balsamic Vinegar of Modena IGP", "Medium syrup body", "Sweet grape must + sharp acid", "Exceptional glossy crust", "Gold Standard (Recommended)"],
            ["White Balsamic Vinegar", "Thin body", "Fruitier, cleaner, light color", "Light caramelization", "Great if you want pale aesthetic"],
            ["Commercial Glaze (Pre-thickened)", "Thick paste", "Very sweet, sugar added", "Can burn easily at 425°F", "Use as a finishing drizzle only"],
            ["Standard Salad Balsamic", "Watery thin", "Sharper acid, tart", "Requires extra honey reduction", "Acceptable everyday swap"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken thighs (trimmed)",
            "1 lb baby gold potatoes, halved (or pre-steamed for fast cooking)",
            "1 medium red onion, cut into wedges",
            "1 bunch fresh asparagus, woody ends trimmed",
            "1/3 cup balsamic vinegar (Modena IGP)",
            "3 tbsp clover honey",
            "1 tbsp Dijon mustard",
            "3 cloves garlic, minced",
            "2 tbsp extra virgin olive oil",
            "1 tsp dried oregano and fresh thyme sprigs",
            "Kosher salt and coarse ground black pepper"
        ],
        "instructions": [
            ("Whisk the Glaze", "In a bowl, whisk balsamic vinegar, honey, Dijon mustard, minced garlic, olive oil, oregano, 1 tsp salt, and 1/2 tsp black pepper until smoothly emulsified. Reserve 3 tablespoons for the final baste."),
            ("Season Chicken & Potatoes", "Preheat oven to 425°F (220°C). Line a large rimmed sheet pan with parchment paper. Place halved baby potatoes, red onion wedges, and chicken thighs on the sheet. Pour the remaining marinade over top and toss thoroughly to coat."),
            ("Initial Roast", "Spread chicken and vegetables out into a single layer. Roast for 10 minutes undisturbed."),
            ("Add Asparagus & Final Baste", "Pull sheet pan out. Scatter trimmed asparagus across the empty spaces. Brush or spoon the reserved 3 tbsp of honey balsamic glaze generously over the chicken thighs."),
            ("Roast & Broil", "Return to oven for 8–10 minutes until chicken reaches 175°F and potatoes are fork-tender. Broil for 1 minute for extra sticky char. Garnish with fresh thyme and serve!")
        ],
        "pro_tip_title": "Elena’s High-Heat Glaze Secret",
        "pro_tip": "Reserving 3 tablespoons of clean glaze before touching raw chicken allows you to apply a fresh, un-diluted coat halfway through roasting. The fresh honey and balsamic sugars caramelize rapidly under the 425°F convection heat, creating that irresistible shiny lacquer seen in gourmet magazines!",
        "faqs": [
            ("Can I use chicken breasts instead of thighs?", "Yes! If using chicken breasts, pound them to an even 3/4-inch thickness so they cook through in 15–18 minutes without drying out."),
            ("Can I use sweet potatoes?", "Yes! Dice sweet potatoes into small 1/2-inch cubes so they roast tender in the same 20-minute window."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 4 days. Reheat on a sheet pan in a toaster oven or air fryer at 375°F for 5 minutes to restore the crispy edges.")
        ],
        "wiki_entities": [
            ("Balsamic vinegar", "https://en.wikipedia.org/wiki/Balsamic_vinegar"),
            ("Chicken as food", "https://en.wikipedia.org/wiki/Chicken_as_food")
        ],
        "pinterest": {
            "board": "Sheet Pan Suppers / Healthy Dinners",
            "title": "20-Minute Sheet-Pan Honey Balsamic Chicken Thighs Recipe (Sweet & Savory!)",
            "desc": "Sticky, caramelized honey balsamic chicken thighs roasted with tender baby potatoes, charred red onions, and fresh asparagus on one pan in 20 minutes! Effortless weeknight cooking at its best. Pin it now!",
            "tags": "#sheetpanchicken #honeybalsamic #20minutedinners #onepanmeals #chickenthighs #healthyfamilydinners #easyrecipes"
        }
    },
    {
        "slug": "15-minute-creamy-tuscan-garlic-salmon",
        "title": "15-Minute Creamy Tuscan Garlic Butter Salmon",
        "headline": "15-Minute Creamy Tuscan Garlic Butter Salmon (Silky One-Pan Luxury)",
        "badge": "15-Minute Meals &bull; Wild Seafood",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/creamy-tuscan-salmon.jpg",
        "image_file": "creamy-tuscan-salmon.jpg",
        "excerpt": "Flaky wild salmon fillets pan-seared in foaming butter and smothered in a velvety sun-dried tomato, spinach, and garlic parmesan cream sauce in 15 minutes.",
        "description": "Crisp-crusted pan-seared salmon fillets bathed in an indulgent garlic cream sauce studded with tangy sun-dried tomatoes, wilted spinach, and shaved parmesan.",
        "keywords": "creamy tuscan salmon, tuscan garlic salmon, 15 minute salmon recipe, pan seared salmon, easy seafood dinners, keto salmon recipe",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-Mediterranean",
        "calories": "520 kcal",
        "protein": "39g",
        "fat": "36g",
        "carbs": "6g",
        "fiber": "2g",
        "sodium": "540mg",
        "ratingValue": "4.9",
        "reviewCount": "195",
        "quick_answer": "To make 15-minute creamy Tuscan garlic butter salmon, season 4 salmon fillets with salt, pepper, and garlic powder. Sear in 1 tbsp olive oil and 1 tbsp butter in a cast-iron skillet over medium-high heat for 4 minutes per side until golden and flaky; transfer to a plate. In the same skillet, melt 1 tbsp butter and sauté 4 minced garlic cloves and 1/2 cup chopped sun-dried tomatoes for 1 minute. Add 3/4 cup heavy cream, 1/2 cup parmesan, and 3 cups baby spinach. Simmer for 2 minutes until spinach wilts. Return salmon to the sauce and serve with fresh lemon.",
        "takeaways": [
            ("Omega-3 Powerhouse", "Wild salmon provides 39g clean protein and heart-healthy omega-3 fatty acids in a 15-minute skillet dinner."),
            ("Sun-Dried Tomato Acid", "The natural tartness of sun-dried tomatoes balances the decadent heavy cream and aged parmesan cheese."),
            ("Golden Pan Sear", "Searing salmon undisturbed for the first 4 minutes locks in juices and builds a delectable crispy crust.")
        ],
        "matrix_title": "Salmon Varieties for 15-Minute Skillet Searing",
        "matrix_headers": ["Salmon Species", "Fat Content", "Flake Texture", "Pan Sear Result", "Verdict"],
        "matrix_rows": [
            ["King (Chinook) Salmon", "Highest fat / buttery", "Velvety, large flakes", "Sublime golden crust", "Luxury Choice"],
            ["Atlantic Salmon", "High fat / mild", "Tender, succulent", "Easy to sear without drying", "Gold Standard for Weeknights"],
            ["Sockeye Salmon", "Medium fat / deep red", "Firm, robust flavor", "Sears in 3 mins per side", "Great for bold fish lovers"],
            ["Coho (Silver) Salmon", "Leaner fat profile", "Delicate flake", "Requires butter basting", "Delicate & light"]
        ],
        "ingredients": [
            "4 center-cut salmon fillets (6 oz each, skin-on or skinless)",
            "1/2 cup oil-packed sun-dried tomatoes, drained and sliced",
            "3 cups fresh baby spinach",
            "3/4 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "4 cloves fresh garlic, minced",
            "2 tbsp unsalted butter (divided)",
            "1 tbsp extra virgin olive oil",
            "1/2 lemon (juice and slices)",
            "1/2 tsp dried oregano & garlic powder",
            "Kosher salt and freshly cracked black pepper",
            "Fresh chopped flat-leaf parsley for garnish"
        ],
        "instructions": [
            ("Dry & Season Salmon", "Pat salmon fillets thoroughly dry with paper towels (moisture prevents a crispy sear). Season both sides generously with salt, black pepper, and garlic powder."),
            ("Golden Pan Sear", "Heat olive oil and 1 tbsp butter in a 12-inch heavy skillet over medium-high heat. Place salmon fillets top-side down first. Sear undisturbed for 4 minutes until a deep golden crust forms. Flip carefully and sear 3 minutes more until medium. Transfer fillets to a warm plate."),
            ("Sauté Garlic & Tomatoes", "Reduce heat to medium. Add remaining 1 tbsp butter, minced garlic, and sun-dried tomatoes to the fragrant pan drippings. Sauté for 60 seconds until fragrant."),
            ("Build Tuscan Cream Sauce", "Pour in heavy cream and bring to a gentle simmer for 1–2 minutes. Stir in grated Parmesan cheese until melted and smooth."),
            ("Wilt Spinach & Serve", "Toss in baby spinach and stir until wilted (about 1 minute). Squeeze in fresh lemon juice. Slide the seared salmon fillets back into the bubbling sauce, spooning sauce over top. Garnish with parsley and lemon slices!")
        ],
        "pro_tip_title": "Elena’s Golden Salmon Sear Secret",
        "pro_tip": "Resist the urge to nudge or shake the skillet when searing salmon! When cold fish hits hot fat, the proteins contract and bond temporarily to the pan. If you let it sear undisturbed for 4 full minutes, the skin and flesh naturally release once the golden caramelized Maillard crust has fully formed, flipping cleanly with zero sticking!",
        "faqs": [
            ("Can I make this dairy-free?", "Yes! Replace heavy cream with full-fat canned coconut milk and substitute nutritional yeast or dairy-free parmesan. The sun-dried tomatoes and garlic mask the coconut flavor beautifully."),
            ("Can I use shrimp or chicken instead?", "Absolutely! Jumbo peeled shrimp cook in 3–4 minutes, and thin chicken cutlets cook in 8–10 minutes using the exact same Tuscan sauce."),
            ("What should I serve with Tuscan salmon?", "Serve with angel hair pasta, creamy garlic cauliflower mash, garlic butter rice, or warm crusty ciabatta bread.")
        ],
        "wiki_entities": [
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato")
        ],
        "pinterest": {
            "board": "Seafood Recipes / Quick Dinners",
            "title": "15-Minute Creamy Tuscan Garlic Butter Salmon Recipe (Restaurant Quality!)",
            "desc": "Crisp golden salmon fillets smothered in a velvety garlic parmesan cream sauce with sun-dried tomatoes and spinach. Cooked in one skillet in 15 minutes! The ultimate weeknight luxury dinner. Pin it now!",
            "tags": "#tuscansalmon #salmonrecipes #15minutedinners #seafooddinner #onepotmeals #ketodinners #lowcarbrecipes"
        }
    },
    {
        "slug": "20-minute-sheet-pan-teriyaki-chicken-broccoli",
        "title": "20-Minute Sheet-Pan Teriyaki Chicken and Broccoli",
        "headline": "20-Minute Sheet-Pan Teriyaki Chicken and Broccoli (Better Than Takeout)",
        "badge": "Sheet Pan Suppers &bull; Family Favorite",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/teriyaki-chicken-broccoli.jpg",
        "image_file": "teriyaki-chicken-broccoli.jpg",
        "excerpt": "Tender bite-sized chicken thighs and charred crisp broccoli florets roasted on a sheet pan and glazed in a savory-sweet homemade sesame teriyaki sauce in 20 minutes.",
        "description": "Crispy caramelized chicken pieces and charred broccoli roasted on a single sheet pan with a glossy homemade soy, honey, ginger, and garlic teriyaki glaze.",
        "keywords": "sheet pan teriyaki chicken, chicken and broccoli sheet pan, 20 minute dinner, homemade teriyaki chicken, easy family dinner, healthy takeout fakeaway",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Japanese-American",
        "calories": "410 kcal",
        "protein": "37g",
        "fat": "14g",
        "carbs": "34g",
        "fiber": "4g",
        "sodium": "680mg",
        "ratingValue": "4.9",
        "reviewCount": "163",
        "quick_answer": "To make 20-minute sheet-pan teriyaki chicken and broccoli, preheat oven to 425°F (220°C). Whisk 1/3 cup low-sodium soy sauce, 1/4 cup honey or brown sugar, 1 tbsp rice vinegar, 1 tbsp sesame oil, 3 minced garlic cloves, 1 tbsp grated ginger, and 1 tsp cornstarch. Toss 1.5 lbs bite-sized chicken thigh pieces and 4 cups broccoli florets with olive oil, salt, and pepper on a parchment-lined baking sheet. Roast for 10 minutes, brush generously with teriyaki glaze, and roast 5–7 minutes more until chicken reaches 175°F and edges char. Top with sesame seeds.",
        "takeaways": [
            ("Better Than Delivery", "Skip the greasy takeout container: this sheet-pan version cuts sugar in half while delivering authentic glossy umami."),
            ("High Heat Char", "Roasting broccoli florets at 425°F mimics wok hei, giving the broccoli sweet caramelized charred tips."),
            ("10-Minute Marinade Shortcut", "Basting hot chicken directly on the sheet pan creates a sticky lacquer in minutes without hours of marinating.")
        ],
        "matrix_title": "Teriyaki Sauce Thickening Benchmark",
        "matrix_headers": ["Thickener Method", "Glaze Shine", "Cling Factor", "Prep Time", "Chef Verdict"],
        "matrix_rows": [
            ["Cornstarch + Honey Simmer", "Mirror gloss", "Maximum cling to meat", "2 minutes", "Gold Standard (Recommended)"],
            ["Pure Sugar / Honey Reduction", "Glossy", "Medium cling", "Requires 8 min reduction", "Traditional tare style"],
            ["Store-Bought Bottled Sauce", "Thick syrup", "Heavy cling", "Instant pour", "High sodium & corn syrup"],
            ["Arrowroot Starch", "Very shiny", "Excellent cling", "2 minutes", "Great paleo alternative"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken thighs (cut into 1.5-inch bite-sized cubes)",
            "4 cups fresh broccoli florets (cut into bite-sized pieces)",
            "1/3 cup low-sodium soy sauce or tamari",
            "1/4 cup pure clover honey or light brown sugar",
            "1 tbsp rice vinegar",
            "1 tbsp toasted sesame oil",
            "3 cloves garlic, finely minced",
            "1 tbsp fresh ginger, finely grated",
            "1 tsp cornstarch whisked with 1 tbsp cold water",
            "1.5 tbsp olive oil (for tossing)",
            "1 tbsp toasted sesame seeds",
            "2 green onions, thinly sliced"
        ],
        "instructions": [
            ("Preheat & Prep Sheet Pan", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper."),
            ("Simmer 2-Minute Teriyaki Glaze", "In a small saucepan, combine soy sauce, honey, rice vinegar, sesame oil, garlic, ginger, and cornstarch slurry. Simmer over medium-low heat for 2 minutes until glossy and thickened like syrup. Remove from heat."),
            ("Season Chicken & Broccoli", "Place cubed chicken thighs and broccoli florets on the prepared baking sheet. Drizzle with olive oil and a pinch of salt and pepper; toss to coat evenly. Spread out in a single layer with space between pieces."),
            ("Bake & Baste", "Roast for 10 minutes. Remove pan from oven. Generously brush or spoon 3/4 of the warm teriyaki glaze all over the chicken and broccoli."),
            ("Caramelize & Garnish", "Return to oven for 5–7 minutes until chicken registers 175°F and edges of broccoli florets are deliciously charred. Drizzle remaining glaze, shower with sesame seeds and scallions, and serve over hot steamed rice!")
        ],
        "pro_tip_title": "Elena’s Broccoli Crispness Rule",
        "pro_tip": "Make sure your broccoli florets are completely dry before tossing them in oil! If freshly washed broccoli has water droplets clinging to the heads, it will steam rather than roast, turning limp and mushy. Dry broccoli roasted at 425°F develops nutty, charred tips with a tender-crisp bite!",
        "faqs": [
            ("Can I use chicken breast instead of thighs?", "Yes! Dice chicken breasts into slightly larger 2-inch chunks and bake for 12–14 minutes total so they stay juicy and tender."),
            ("Can I add other vegetables?", "Absolutely! Sliced bell peppers, snap peas, and sliced carrots roast wonderfully alongside chicken and broccoli."),
            ("How do I store leftovers?", "Pack into airtight meal prep containers with jasmine rice for up to 4 days. Reheat in a microwave for 90 seconds.")
        ],
        "wiki_entities": [
            ("Teriyaki", "https://en.wikipedia.org/wiki/Teriyaki"),
            ("Broccoli", "https://en.wikipedia.org/wiki/Broccoli")
        ],
        "pinterest": {
            "board": "Sheet Pan Dinners / Asian Recipes",
            "title": "20-Minute Sheet-Pan Teriyaki Chicken and Broccoli Recipe (Takeout Fakeaway!)",
            "desc": "Tender caramelized chicken thigh bites and roasted crispy broccoli glazed in homemade garlic ginger teriyaki sauce. Cooked on one sheet pan in 20 minutes! Better and healthier than delivery. Pin it tonight!",
            "tags": "#sheetpanmeals #teriyakichicken #20minutedinners #takeoutfakeaway #chickenandbroccoli #easyrecipes #healthydinners"
        }
    },
    {
        "slug": "20-minute-french-onion-chicken-skillet",
        "title": "20-Minute French Onion Chicken Skillet",
        "headline": "20-Minute French Onion Chicken Skillet (Caramelized & Cheesy)",
        "badge": "One-Pot Dinners &bull; Cozy Comfort",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/french-onion-chicken.jpg",
        "image_file": "french-onion-chicken.jpg",
        "excerpt": "Seared chicken cutlets simmered in sweet caramelized onions and rich beef thyme pan gravy, blanketed in bubbly golden melted Gruyère cheese in 20 minutes.",
        "description": "All the savory, rich indulgence of French onion soup reimagined as a 20-minute skillet dinner with golden chicken breasts and gooey melted Gruyère.",
        "keywords": "french onion chicken, one pan french onion chicken, 20 minute chicken skillet, caramelized onion chicken, gruyere cheese dinner, comfort food weeknight",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "French-American",
        "calories": "490 kcal",
        "protein": "46g",
        "fat": "24g",
        "carbs": "12g",
        "fiber": "2g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "188",
        "quick_answer": "To make 20-minute French onion chicken, sear 4 seasoned chicken cutlets in 1 tbsp olive oil and 1 tbsp butter over medium-high heat for 4 minutes per side; transfer to a plate. In the same skillet, melt 2 tbsp butter, add 2 thinly sliced yellow onions with a pinch of brown sugar and salt, and sauté over medium-high heat for 6–7 minutes until deeply caramelized. Deglaze with 1/2 cup beef broth and 1 tbsp balsamic vinegar or Worcestershire sauce, stirring in 1 tsp fresh thyme. Return chicken, smother with onions, top with 1 cup shredded Gruyère or Swiss cheese, and broil for 2 minutes until bubbly and golden.",
        "takeaways": [
            ("Onion Caramelization Hack", "A pinch of brown sugar and high heat with butter accelerates the onion Maillard reaction from 45 minutes down to 7 minutes."),
            ("Savory Beef Thyme Glaze", "Deglazing pan drippings with beef broth and Worcestershire creates an instant bistro-style French onion reduction."),
            ("The Gruyère Blanket", "Authentic aged Gruyère melts into nutty, golden, stretchy perfection that seals juices inside the chicken.")
        ],
        "matrix_title": "Melting Cheese Performance for French Onion Skillet",
        "matrix_headers": ["Cheese Choice", "Flavor Notes", "Melt Silkiness", "Golden Crust Under Broiler", "Verdict"],
        "matrix_rows": [
            ["Aged Gruyère", "Nutty, earthy, savory", "Luxurious silk", "Deep golden blister", "Classic Authentic (Recommended)"],
            ["Swiss Cheese (Emmental)", "Sweet, mild hazelnut", "High stretch", "Golden", "Accessible everyday substitute"],
            ["Fontina", "Buttery, mild cream", "Ultra-gooey", "Light golden", "Great for extra creaminess"],
            ["Provolone", "Mild, slightly sharp", "Medium stretch", "Good", "Easy budget swap"]
        ],
        "ingredients": [
            "4 thin-cut boneless skinless chicken breasts (about 1.5 lbs)",
            "2 large yellow onions, peeled and thinly sliced",
            "1.25 cups shredded Gruyère or Swiss cheese",
            "1/2 cup rich low-sodium beef broth",
            "1 tbsp Worcestershire sauce or balsamic vinegar",
            "3 tbsp unsalted butter (divided)",
            "1 tbsp olive oil",
            "1/2 tsp brown sugar (for rapid caramelization)",
            "1 tsp fresh thyme leaves (plus sprigs for garnish)",
            "2 cloves garlic, minced",
            "Kosher salt and freshly cracked black pepper"
        ],
        "instructions": [
            ("Sear the Chicken", "Pat chicken cutlets dry. Season both sides with salt, pepper, and garlic powder. Heat olive oil and 1 tbsp butter in a 12-inch oven-safe skillet over medium-high heat. Sear chicken for 4 minutes per side until golden brown (165°F). Transfer to a plate."),
            ("Fast-Caramelize Onions", "Melt remaining 2 tbsp butter in the skillet. Add sliced onions, brown sugar, and a pinch of salt. Sauté over medium-high heat, stirring frequently, for 6–7 minutes as onions soften and turn deep caramel amber."),
            ("Deglaze with Beef Thyme Broth", "Add minced garlic, Worcestershire sauce, beef broth, and fresh thyme to the skillet. Scrape up all delicious browned bits from the pan bottom and simmer for 2 minutes until sauce is syrupy."),
            ("Layer & Top with Gruyère", "Nestle chicken cutlets back into the skillet. Spoon sweet caramelized onions generously over the top of each cutlet. Blanket with shredded Gruyère cheese."),
            ("Broil to Golden Perfection", "Transfer skillet under the oven broiler set to HIGH for 2–3 minutes until the cheese is bubbling, melted, and flecked with golden-brown spots. Garnish with fresh thyme and serve immediately!")
        ],
        "pro_tip_title": "Elena’s 7-Minute Caramelized Onion Shortcut",
        "pro_tip": "Traditional French onion soup requires 45 minutes of slow stirring. For a rapid 20-minute weeknight dinner, slice your onions paper-thin on a mandoline and add a pinch of brown sugar to the hot foaming butter. The sugar triggers rapid surface caramelization while high heat cooks the onions tender in just 7 minutes flat!",
        "faqs": [
            ("Can I use mozzarella instead of Gruyère?", "Yes! While Gruyère offers that distinct nutty French bistro flavor, whole-milk mozzarella or provolone melts beautifully and tastes fantastic."),
            ("Can I make this in a non-oven-safe pan?", "Yes! Simply cover the skillet with a tight-fitting lid on the stovetop for 2 minutes over low heat until the cheese melts completely."),
            ("What should I serve with French onion chicken?", "It is phenomenal served with crusty French baguette slices for dipping, garlic mashed potatoes, or roasted green beans.")
        ],
        "wiki_entities": [
            ("French onion soup", "https://en.wikipedia.org/wiki/French_onion_soup"),
            ("Gruyère cheese", "https://en.wikipedia.org/wiki/Gruy%C3%A8re_cheese")
        ],
        "pinterest": {
            "board": "Comfort Food / Easy Chicken Dinners",
            "title": "20-Minute French Onion Chicken Skillet Recipe (Caramelized & Cheesy!)",
            "desc": "Everything you love about French onion soup in a 20-minute weeknight chicken skillet! Juicy seared chicken smothered in sweet caramelized onions, beef pan gravy, and bubbling Gruyère cheese. Save this comfort dinner!",
            "tags": "#frenchonionchicken #chickenskillet #20minutedinners #onepotdinners #comfortfoodrecipes #cheesychicken #easyrecipes"
        }
    },
    {
        "slug": "15-minute-creamy-tomato-parmesan-orzo",
        "title": "15-Minute Creamy Sun-Dried Tomato Parmesan Orzo",
        "headline": "15-Minute Creamy Sun-Dried Tomato Parmesan Orzo (One-Pot Velvet)",
        "badge": "15-Minute Meals &bull; One-Pot Vegetarian",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/creamy-tomato-orzo.jpg",
        "image_file": "creamy-tomato-orzo.jpg",
        "excerpt": "Velvety one-skillet orzo pasta simmered directly in rich garlic cream with sweet sun-dried tomatoes, wilted spinach, and shaved aged parmesan in just 15 minutes.",
        "description": "Pillowy orzo pasta cooked directly in flavorful broth and garlic cream, studded with tangy sun-dried tomatoes, tender baby spinach, and aged parmesan.",
        "keywords": "creamy tomato orzo, sun dried tomato orzo, 15 minute one pot pasta, creamy parmesan orzo, vegetarian weeknight dinner, easy orzo recipe",
        "prepTime": "PT3M",
        "cookTime": "PT12M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-Mediterranean",
        "calories": "460 kcal",
        "protein": "15g",
        "fat": "20g",
        "carbs": "54g",
        "fiber": "4g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "171",
        "quick_answer": "To make 15-minute creamy sun-dried tomato parmesan orzo, sauté 3 minced garlic cloves and 1/2 cup chopped sun-dried tomatoes in 1 tbsp olive oil and 1 tbsp butter in a large skillet for 1 minute. Add 1.5 cups dry orzo, stirring to toast for 1 minute. Pour in 3 cups low-sodium vegetable or chicken broth. Bring to a boil, reduce to medium-low, cover, and simmer for 9–10 minutes until orzo is tender and liquid is absorbed. Stir in 1/2 cup heavy cream, 1/2 cup grated parmesan, and 3 cups baby spinach until wilted and creamy.",
        "takeaways": [
            ("Risotto Texture Without Stirring", "Simmering dry orzo directly in broth creates a rich, creamy, risotto-like body in 10 minutes without 40 minutes of arm-tiring stirring."),
            ("Toasting Orzo First", "Toasting dry orzo in butter before adding liquid unlocks an irresistible nutty aroma and keeps the pasta distinct."),
            ("Vegetarian Flavor Bomb", "Sun-dried tomatoes and aged parmesan deliver intense umami depth that satisfies even dedicated meat lovers.")
        ],
        "matrix_title": "Orzo Liquid-to-Pasta Ratios for One-Pot Cooking",
        "matrix_headers": ["Ratio (Liquid to Orzo)", "Resulting Texture", "Cooking Time", "Risk of Scorching", "Chef Verdict"],
        "matrix_rows": [
            ["2:1 (3 cups liquid to 1.5 cups orzo)", "Al dente, risotto silk", "9–10 minutes", "Low", "Gold Standard (Recommended)"],
            ["2.5:1 (3.75 cups liquid)", "Soupy, softer pasta", "12 minutes", "Very low", "Best for brothy soups"],
            ["1.5:1 (2.25 cups liquid)", "Very firm, dry", "8 minutes", "High", "Too dry for cream additions"],
            ["Water instead of Broth", "Bland flavor base", "10 minutes", "Low", "Requires extra salt & seasonings"]
        ],
        "ingredients": [
            "1.5 cups dry orzo pasta (uncooked)",
            "3 cups low-sodium vegetable broth (or chicken broth)",
            "1/2 cup oil-packed sun-dried tomatoes, drained and sliced",
            "1/2 cup heavy whipping cream (or half-and-half)",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "3 cups fresh baby spinach",
            "4 cloves fresh garlic, minced",
            "1 tbsp unsalted butter",
            "1 tbsp extra virgin olive oil",
            "1/4 tsp crushed red pepper flakes",
            "Fresh basil leaves for garnish",
            "Kosher salt and cracked black pepper"
        ],
        "instructions": [
            ("Sauté Aromatics & Toast Orzo", "Heat olive oil and butter in a deep 12-inch skillet over medium heat. Add minced garlic, sun-dried tomatoes, and red pepper flakes; sauté for 60 seconds until fragrant. Add dry orzo and stir continuously for 1–2 minutes to lightly toast the grains."),
            ("Simmer Orzo in Broth", "Pour in 3 cups vegetable broth and a pinch of salt. Bring to a rolling boil, then reduce heat to medium-low. Cover with a lid and simmer for 9–10 minutes, stirring once halfway through, until orzo is tender and most broth is absorbed."),
            ("Stir in Cream & Cheese", "Remove lid. Pour in heavy cream and grated Parmesan cheese. Stir gently over low heat for 1 minute as the cheese melts into a luxurious, velvety sauce."),
            ("Fold Spinach & Wilt", "Add baby spinach by the handful, folding it into the warm orzo for 1 minute until completely wilted and bright emerald green."),
            ("Garnish & Serve", "Remove from heat. Season with freshly cracked black pepper, scatter fresh torn basil leaves on top, and serve warm in shallow bowls!")
        ],
        "pro_tip_title": "Elena’s One-Pan Orzo Secret",
        "pro_tip": "Do not rinse your orzo before cooking! The exterior starch on dry orzo grains is the secret engine that turns the broth and cream into a glossy, velvety emulsion. When you simmer the orzo directly in broth, that surface starch dissolves into the liquid, producing a luxurious restaurant risotto consistency with zero heavy labor.",
        "faqs": [
            ("Can I add protein like chicken or shrimp to this orzo?", "Yes! Sear bite-sized chicken breast pieces or peeled shrimp in the skillet first for 4 minutes, remove, cook the orzo, and fold the cooked protein back in with the spinach."),
            ("Can I make this dairy-free or vegan?", "Yes! Substitute full-fat canned coconut milk or unsweetened cashew cream for heavy cream, and use nutritional yeast or vegan parmesan."),
            ("How do I reheat leftover orzo?", "Orzo absorbs liquid as it sits in the fridge. When reheating, add 2 tablespoons of broth, milk, or water and microwave for 1–2 minutes to restore its creamy texture.")
        ],
        "wiki_entities": [
            ("Orzo", "https://en.wikipedia.org/wiki/Orzo"),
            ("Parmesan", "https://en.wikipedia.org/wiki/Parmesan")
        ],
        "pinterest": {
            "board": "Pasta Recipes / 15-Minute Meals",
            "title": "15-Minute Creamy Sun-Dried Tomato Parmesan Orzo Recipe (One-Pot Velvet!)",
            "desc": "Tender orzo pasta simmered in rich garlic cream with sun-dried tomatoes, baby spinach, and aged parmesan cheese. One skillet, 15 minutes, and pure comfort! Try this easy weeknight dinner tonight!",
            "tags": "#orzorecipe #onepotpasta #15minutedinners #creampasta #vegetarianrecipes #weeknightdinner #easycomfortfood"
        }
    },
    {
        "slug": "15-minute-lemon-butter-pan-seared-scallops",
        "title": "15-Minute Lemon Butter Pan-Seared Scallops",
        "headline": "15-Minute Lemon Butter Pan-Seared Scallops (Golden Crust Luxury)",
        "badge": "15-Minute Meals &bull; Date Night Classic",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-21",
        "image": "./assets/images/lemon-butter-pan-seared-scallops.jpg",
        "image_file": "lemon-butter-pan-seared-scallops.jpg",
        "excerpt": "Jumbo sea scallops pan-seared with a golden caramelized crust, basted in foaming garlic lemon parsley butter with crushed red pepper in 15 minutes.",
        "description": "Restaurant-quality pan-seared sea scallops basted with foaming garlic herb butter, fresh lemon, and white wine in just 15 minutes.",
        "keywords": "pan seared scallops, lemon butter scallops, 15 minute seafood dinner, garlic butter scallops, easy date night dinner, low carb seafood recipes",
        "prepTime": "PT7M",
        "cookTime": "PT8M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "French-American",
        "calories": "320 kcal",
        "protein": "28g",
        "fat": "18g",
        "carbs": "5g",
        "fiber": "0.5g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "184",
        "quick_answer": "To make 15-minute lemon butter pan-seared scallops, pat 1 lb dry sea scallops thoroughly with paper towels and remove side muscles; season with salt and pepper. Heat 1 tbsp avocado oil in a cast-iron skillet over high heat until smoking. Sear scallops undisturbed for 2 minutes until a deep golden crust forms. Flip, add 3 tbsp unsalted butter, 3 minced garlic cloves, and 1 lemon wheel. Baste foaming butter over scallops for 1.5–2 minutes. Squeeze fresh lemon juice, scatter parsley, and serve immediately.",
        "takeaways": [
            ("Bone-Dry Secret", "Scallops will steam instead of sear if moist; pressing with double paper towels guarantees a golden caramelized restaurant crust."),
            ("High Heat Speed", "Scallops take just 90 seconds to 2 minutes per side; cooking them longer makes them rubbery."),
            ("The Pan Baste (Arrosé)", "Spoon-basting foaming garlic lemon butter over the scallops cooks them gently while infusing decadent flavor.")
        ],
        "matrix_title": "Scallop Types & Searing Performance",
        "matrix_headers": ["Scallop Type", "Treatment", "Searing Crust", "Sweetness", "Chef Verdict"],
        "matrix_rows": [
            ["Dry-Packed Sea Scallops (U-10 to U-15)", "Chemical-free / natural", "Instant deep golden crust", "Pure sweet ocean flavor", "Gold Standard (Recommended)"],
            ["Wet-Packed Sea Scallops", "Soaked in sodium tripolyphosphate", "Exudes water / steams gray", "Muted, slightly soapy", "Avoid for pan searing"],
            ["Bay Scallops", "Tiny size (60-80 per lb)", "Cooks in 60 seconds", "Sweet but delicate", "Better for pasta / chowder"],
            ["Frozen Thawed Dry Scallops", "Quick-frozen at sea", "Good crust if dried well", "Sweet & tender", "Great accessible option"]
        ],
        "ingredients": [
            "1 lb fresh jumbo dry-packed sea scallops (about 12–16 count)",
            "3 tbsp unsalted butter",
            "1 tbsp high-smoke-point avocado oil or light olive oil",
            "3 cloves fresh garlic, finely minced",
            "1/2 fresh lemon (plus 1 lemon cut into wheels)",
            "2 tbsp fresh flat-leaf parsley, finely chopped",
            "1/4 tsp crushed red pepper flakes (optional)",
            "Flaky sea salt (Maldon) and freshly cracked black pepper"
        ],
        "instructions": [
            ("Prep & Dry the Scallops", "Inspect scallops and pull off the small tough rectangular side muscle (abductor) from each one. Place scallops between several layers of paper towels and press firmly to remove ALL surface moisture. Season tops generously with salt and pepper right before cooking."),
            ("Heat Cast Iron to Smoking", "Heat avocado oil in a 12-inch heavy cast-iron skillet over high heat until just beginning to smoke. The pan must be searing hot."),
            ("Hard Sear Undisturbed", "Place scallops seasoned-side down into the hot oil, leaving at least 1 inch of space between each (cook in batches if needed). Sear undisturbed for 2 minutes until a deep, caramelized golden crust forms."),
            ("Flip & Butter Baste", "Season the unseasoned side, then gently flip scallops. Immediately add butter, minced garlic, lemon wheels, and red pepper flakes to the pan. Tilt skillet and use a large spoon to baste the foaming garlic butter over the scallops for 1.5 to 2 minutes until opaque in the center."),
            ("Finish & Serve", "Remove from heat immediately to prevent overcooking. Squeeze fresh lemon juice over the top, sprinkle with chopped parsley and flaky sea salt, and spoon the pan butter over top. Serve right away!")
        ],
        "pro_tip_title": "Elena’s Golden Scallop Crust Secret",
        "pro_tip": "Always buy 'dry-packed' sea scallops! 'Wet' scallops are soaked in a chemical preservative bath that causes them to shed water in the pan, boiling them into gray rubber. Dry scallops, pressed with paper towels and placed in screaming-hot oil, caramelize in 120 seconds into sweet, buttery seafood perfection.",
        "faqs": [
            ("How do I know when scallops are cooked through?", "Scallops are done when the sides have turned from translucent to opaque white and feel slightly springy to the touch (125°F internal temperature). Never overcook!"),
            ("What can I serve with pan-seared scallops?", "They pair gorgeously with garlic parmesan risotto, angel hair pasta with white wine sauce, mashed cauliflower, or a crisp arugula salad."),
            ("Can I use frozen scallops?", "Yes! Thaw frozen scallops overnight in the refrigerator (never in warm water), then dry thoroughly between paper towels for 15 minutes before searing.")
        ],
        "wiki_entities": [
            ("Scallop", "https://en.wikipedia.org/wiki/Scallop"),
            ("Searing", "https://en.wikipedia.org/wiki/Searing")
        ],
        "pinterest": {
            "board": "Seafood Recipes / Date Night Dinners",
            "title": "15-Minute Lemon Butter Pan-Seared Scallops Recipe (Restaurant Quality Crust!)",
            "desc": "Tender jumbo sea scallops pan-seared with a gorgeous caramelized crust, basted in foaming garlic lemon herb butter. Elegant, restaurant-quality seafood ready in just 15 minutes! Save this recipe now!",
            "tags": "#searedscallops #scallopsrecipe #15minutedinners #seafooddinner #datenightdinner #garlicbutter #keto"
        }
    }
]

print(f"Loaded {len(RECIPES)} recipes ready for publishing.")
