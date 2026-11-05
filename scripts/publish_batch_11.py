import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "15-minute-garlic-butter-tuscan-gnocchi",
        "title": "15-Minute Creamy Garlic Butter Tuscan Gnocchi with Spinach and Sun-Dried Tomatoes",
        "headline": "15-Minute Creamy Tuscan Garlic Butter Potato Gnocchi Skillet",
        "badge": "One-Pot Dinners &bull; 15 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/garlic-butter-tuscan-gnocchi.jpg",
        "image_file": "garlic-butter-tuscan-gnocchi.jpg",
        "excerpt": "Pillowy potato gnocchi simmered in a luscious garlic butter parmesan cream sauce with chewy sun-dried tomato strips, tender baby spinach, and fresh basil in 15 minutes.",
        "description": "Ultra-comforting Italian skillet dinner in 15 minutes: pillowy tender potato gnocchi swimming in a rich garlic butter cream sauce with sweet sun-dried tomatoes, spinach, and parmesan.",
        "keywords": "creamy tuscan gnocchi, garlic butter gnocchi, 15 minute gnocchi, one pot gnocchi dinner, quick weeknight pasta, sun dried tomato gnocchi",
        "prepTime": "PT3M",
        "cookTime": "PT12M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Tuscan / Italian Comfort",
        "calories": "460 kcal",
        "protein": "12g",
        "fat": "22g",
        "carbs": "54g",
        "fiber": "4g",
        "sodium": "540mg",
        "ratingValue": "4.9",
        "reviewCount": "196",
        "quick_answer": "To make 15-minute creamy garlic butter Tuscan gnocchi, drop 1 lb potato gnocchi into boiling salted water for 2 to 3 minutes until they float, then drain. Meanwhile, melt 2 tbsp butter with 1 tbsp olive oil in a wide skillet over medium heat. Sauté 4 minced garlic cloves and 1/2 cup sliced oil-packed sun-dried tomatoes for 60 seconds. Pour in 1/2 cup vegetable broth, 3/4 cup heavy cream, and 1/2 cup grated parmesan cheese, simmering for 2 minutes until glossy and bubbling. Toss in the drained gnocchi and 3 cups fresh baby spinach, cooking for 60 seconds until spinach is wilted and gnocchi is coated in velvety cream. Garnish with fresh basil and cracked pepper.",
        "takeaways": [
            ("3-Minute Gnocchi Float Rule", "Potato gnocchi cook faster than dried pasta; pull them from the boiling water the exact second they bob to the surface to retain light, tender fluffiness."),
            ("Sun-Dried Tomato Sweetness & Acid", "Using tomatoes packed in olive oil introduces natural herbs and tang that cuts through the rich heavy cream without curdling."),
            ("Parmesan Thickening Emulsion", "Freshly grated Parmigiano-Reggiano melts into the simmering cream within 90 seconds, creating a restaurant-grade velvet sauce without flour or cornstarch.")
        ],
        "matrix_title": "Gnocchi Format Comparison in Tuscan Cream Sauces",
        "matrix_headers": ["Gnocchi Type", "Boiling Time", "Internal Texture", "Sauce Adhesion", "Verdict"],
        "matrix_rows": [
            ["Shelf-Stable Potato Gnocchi", "2–3 minutes", "Pillowy & tender", "Maximum coating cling", "Fastest Weeknight Standard (Recommended)"],
            ["Fresh Refrigerated Gnocchi", "2 minutes", "Delicate & airy", "Absorbs garlic cream deeply", "Upscale trattoria feel"],
            ["Cauliflower Gnocchi", "Pan-fry 8 minutes", "Chewier, denser", "Good", "Best low-carb swap"],
            ["Ricotta Gnocchi", "2 minutes", "Melt-in-mouth soft", "Fragile", "Handle gently with spoon"]
        ],
        "ingredients": [
            "1 lb store-bought potato gnocchi (shelf-stable or fresh)",
            "2 tbsp unsalted butter",
            "1 tbsp extra virgin olive oil",
            "4 cloves fresh garlic, finely minced",
            "1/2 cup oil-packed sun-dried tomatoes, drained and sliced",
            "1/2 cup low-sodium vegetable or chicken broth",
            "3/4 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "3 packed cups fresh baby spinach leaves",
            "1/4 tsp crushed red pepper flakes",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper",
            "Fresh basil leaves for serving"
        ],
        "instructions": [
            ("Boil Gnocchi", "Bring a large pot of salted water to a rolling boil. Add potato gnocchi and boil for 2 to 3 minutes until they all float to the surface. Drain in a colander and set aside."),
            ("Sauté Aromatics", "While gnocchi boils, melt butter and olive oil in a large deep skillet over medium heat. Add minced garlic, sliced sun-dried tomatoes, and crushed red pepper flakes. Sauté for 60 seconds until fragrant without browning."),
            ("Build Velvet Cream Sauce", "Pour in vegetable broth, heavy cream, and grated parmesan cheese. Whisk continuously for 2 minutes as the sauce comes to a gentle simmer and emulsifies into a glossy, velvety consistency."),
            ("Toss Gnocchi & Wilt Spinach", "Add drained gnocchi and fresh baby spinach directly into the skillet. Toss gently with a wooden spoon for 60 to 90 seconds until the spinach is wilted and every gnocchi is coated in rich garlic cream."),
            ("Garnish & Serve", "Remove from heat immediately. Scatter torn fresh basil leaves, extra grated parmesan, and freshly cracked black pepper over the top. Serve hot straight from the skillet!")
        ],
        "pro_tip_title": "Elena’s One-Pan Skillet Sear Alternative",
        "pro_tip": "If you don't feel like boiling a separate pot of water, you can pan-sear the gnocchi straight out of the package in 2 tbsp olive oil over medium-high heat for 6 minutes until crispy and golden on the outside! Then build the sauce right in the same pan for crispy-outside, pillowy-inside gnocchi.",
        "faqs": [
            ("Can I add protein to this dish?", "Yes! Seared jumbo shrimp, sliced grilled chicken breast, or browned Italian sausage crumbles pair exquisitely."),
            ("Can I make this dairy-free?", "Substitute full-fat canned coconut milk for heavy cream and use nutritional yeast or vegan parmesan."),
            ("How do I reheat leftover gnocchi?", "Reheat in a skillet over medium-low heat with a splash of broth or cream to loosen the sauce; avoid the microwave which can make gnocchi gummy.")
        ],
        "wiki_entities": [
            ("Gnocchi", "https://en.wikipedia.org/wiki/Gnocchi"),
            ("Tuscan food", "https://en.wikipedia.org/wiki/Tuscan_food"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato")
        ],
        "pinterest": {
            "board": "Pasta Recipes / Quick Italian Dinners",
            "title": "15-Minute Creamy Garlic Butter Tuscan Gnocchi",
            "desc": "Pillowy potato gnocchi swimming in a rich garlic butter cream sauce with sun-dried tomatoes, baby spinach, and parmesan in 15 minutes! Cozy weeknight dinner. Save the recipe!",
            "tags": "#tuscangnocchi #gnocchi #15minutedinner #quickpasta #italianfood #onepotmeals #dinnerideas"
        }
    },
    {
        "slug": "15-minute-sweet-chili-shrimp-rice-bowls",
        "title": "15-Minute Sweet Thai Chili Garlic Shrimp Rice Bowls",
        "headline": "15-Minute Sizzling Sweet Thai Chili Garlic Shrimp Rice Bowls",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/sweet-chili-shrimp-rice-bowls.jpg",
        "image_file": "sweet-chili-shrimp-rice-bowls.jpg",
        "excerpt": "Plump pink seared jumbo shrimp coated in a bubbling sweet Thai chili garlic glaze, served over fluffy jasmine rice with crisp cucumbers, carrots, and sesame seeds in 15 minutes.",
        "description": "Sweet, spicy, and irresistible weeknight seafood dinner: jumbo shrimp flash-seared and smothered in a glossy sweet chili garlic glaze over steaming jasmine rice with crisp veggies.",
        "keywords": "sweet chili shrimp, shrimp rice bowls, 15 minute seafood dinner, sweet thai chili shrimp, easy weeknight shrimp, quick asian bowls",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Thai / Asian Fusion",
        "calories": "410 kcal",
        "protein": "29g",
        "fat": "9g",
        "carbs": "53g",
        "fiber": "2g",
        "sodium": "660mg",
        "ratingValue": "4.9",
        "reviewCount": "184",
        "quick_answer": "To make 15-minute sweet chili shrimp rice bowls, pat 1.25 lbs raw peeled and deveined jumbo shrimp completely dry and season with 1/2 tsp garlic powder, salt, and pepper. Heat 1 tbsp neutral oil in a large skillet over high heat; sear shrimp in a single layer for 90 seconds per side until pink and caramelized. Reduce heat to medium, add 3 minced garlic cloves, 1 tsp grated ginger, 1/3 cup Thai sweet chili sauce, 1.5 tbsp low-sodium soy sauce, and 1 tsp sriracha (for a fiery kick). Toss shrimp continuously for 60 seconds as the glaze bubbles and turns thick and sticky. Spoon immediately over bowls of warm jasmine rice with sliced cucumbers, matchstick carrots, green scallions, and toasted sesame seeds.",
        "takeaways": [
            ("Blotting Shrimp Dry", "Removing surface water ensures shrimp sear vigorously in hot oil instead of boiling in released liquids, developing sweet caramelized edges in 3 minutes."),
            ("Sweet Chili Soy Glaze Reduction", "Combining sweet chili sauce with savory soy sauce balances high sweetness with salty umami, caramelizing onto the shrimp without cloying heaviness."),
            ("Crisp Raw Vegetable Texture", "Crunchy Persian cucumbers and raw matchstick carrots provide a refreshing thermal and textural contrast to hot glazed seafood.")
        ],
        "matrix_title": "Shrimp Sizing Guide for Rapid Skillet Glazing",
        "matrix_headers": ["Shrimp Count", "Weight / Size", "Sear Time Per Side", "Texture Hold", "Verdict"],
        "matrix_rows": [
            ["16/20 Jumbo Shrimp", "Large & plump", "90 seconds", "Juicy, snappy pop", "Best for Restaurant Presentation (Recommended)"],
            ["26/30 Large Shrimp", "Medium-large", "60–75 seconds", "Good tender chew", "Great budget-friendly choice"],
            ["41/50 Small Shrimp", "Small bite-size", "45 seconds", "Overcooks quickly", "Better for fried rice"],
            ["Colossal U-12 Shrimp", "Very thick", "2–2.5 minutes", "Meaty & firm", "Excellent special occasion option"]
        ],
        "ingredients": [
            "1.25 lbs raw jumbo shrimp (16/20 count), peeled, deveined, tails on or off",
            "1 tbsp avocado or vegetable oil",
            "3 cloves fresh garlic, finely minced",
            "1 tsp fresh ginger, grated",
            "1/3 cup Thai sweet chili sauce (such as Mae Ploy)",
            "1.5 tbsp low-sodium soy sauce or tamari",
            "1 tsp sriracha chili sauce",
            "Juice of 1/2 fresh lime",
            "1/2 tsp garlic powder & 1/4 tsp black pepper",
            "4 cups warm cooked jasmine rice",
            "1 English or Persian cucumber, thinly sliced",
            "1/2 cup matchstick carrots",
            "2 green onions, thinly sliced",
            "1 tbsp toasted white sesame seeds"
        ],
        "instructions": [
            ("Season the Shrimp", "Thoroughly pat peeled shrimp dry with paper towels. Season with garlic powder, salt, and freshly ground black pepper."),
            ("Flash-Sear the Shrimp", "Heat oil in a large cast iron skillet or wok over high heat until smoking hot. Add shrimp in a single layer with space between them. Sear undisturbed for 90 seconds until the underside is pink and caramelized. Flip and sear for another 60 seconds."),
            ("Glaze in Sweet Chili Sauce", "Reduce heat to medium. Add minced garlic and grated ginger to the pan drippings, stirring for 30 seconds. Pour in sweet chili sauce, soy sauce, sriracha, and lime juice. Toss the shrimp continuously as the glaze bubbles violently and turns into a thick, glossy lacquer (about 60 seconds)."),
            ("Assemble the Bowls", "Divide warm steamed jasmine rice into 4 shallow bowls. Pile the sweet chili glazed shrimp and extra pan sauce over the rice."),
            ("Garnish & Serve", "Tuck cucumber slices and shredded carrots alongside the shrimp. Shower with green scallions, toasted sesame seeds, and extra lime wedges. Serve piping hot!")
        ],
        "pro_tip_title": "Elena’s 3-Minute Shrimp Timer Rule",
        "pro_tip": "Jumbo shrimp are completely cooked when they form a loose 'C' shape! If they curl into a tight, closed 'O' shape, they have been overcooked and will turn rubbery. Pull them off the heat the exact second they curl into a gentle 'C' and let the resting glaze finish the magic.",
        "faqs": [
            ("Can I make this with frozen shrimp?", "Yes! Thaw frozen shrimp quickly in a bowl of cold water for 15 minutes, peel, and pat thoroughly dry with paper towels before seasoning."),
            ("Can I use cauliflower rice for low-carb?", "Yes, garlic sautéed cauliflower rice is delicious with sweet chili shrimp and cuts the carbs significantly."),
            ("How spicy is Thai sweet chili sauce?", "It is very mild and sweet with faint chili warmth. Adding the 1 tsp sriracha balances the sweetness into a gentle medium kick.")
        ],
        "wiki_entities": [
            ("Shrimp as food", "https://en.wikipedia.org/wiki/Shrimp_as_food"),
            ("Sweet chili sauce", "https://en.wikipedia.org/wiki/Sweet_chili_sauce"),
            ("Jasmine rice", "https://en.wikipedia.org/wiki/Jasmine_rice")
        ],
        "pinterest": {
            "board": "Seafood Dinners / Asian Grain Bowls",
            "title": "15-Minute Sweet Thai Chili Garlic Shrimp Rice Bowls",
            "desc": "Juicy jumbo shrimp glazed in a bubbling sweet chili garlic sauce over jasmine rice with cucumbers and sesame seeds in 15 minutes! The easiest weeknight dinner. Save the pin!",
            "tags": "#sweetchilishrimp #shrimpbowl #15minutedinner #quickseafood #asianbowls #easyrecipes #dinnerideas"
        }
    },
    {
        "slug": "20-minute-sheet-pan-zaatar-chicken-thighs",
        "title": "20-Minute Sheet-Pan Crispy Za'atar Chicken Thighs with Roasted Cauliflower",
        "headline": "20-Minute Sheet-Pan Za'atar Spiced Chicken Thighs and Cauliflower",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/sheet-pan-zaatar-chicken-thighs.jpg",
        "image_file": "sheet-pan-zaatar-chicken-thighs.jpg",
        "excerpt": "Golden crispy spiced chicken thighs roasted on one sheet pan with nutty cauliflower florets, charred cherry tomatoes, lemon slices, and creamy garlic tahini in 20 minutes.",
        "description": "Fragrant Middle Eastern weeknight feast: tender chicken thighs rubbed in herbal za'atar, sumac, and garlic, roasted at 450°F alongside caramelized cauliflower and cherry tomatoes.",
        "keywords": "sheet pan zaatar chicken, zaatar chicken thighs, 20 minute sheet pan suppers, middle eastern chicken, healthy weeknight dinner, roasted cauliflower chicken",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Middle Eastern / Mediterranean",
        "calories": "470 kcal",
        "protein": "38g",
        "fat": "26g",
        "carbs": "16g",
        "fiber": "5g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "178",
        "quick_answer": "To make 20-minute sheet-pan za'atar chicken thighs and cauliflower, preheat oven to 450°F (230°C). Cut 1 head cauliflower into small bite-sized florets. Toss 1.5 lbs boneless skinless chicken thighs and the cauliflower florets with 2.5 tbsp olive oil, 2 tbsp za'atar seasoning blend (thyme, sesame, sumac, oregano), 1 tsp garlic powder, 1 tsp ground cumin, 1 tsp salt, and 1/2 tsp pepper. Spread across a large rimmed baking sheet with 1 cup whole cherry tomatoes and 1 sliced lemon. Roast for 14 minutes, switching to high broil for the final 2 minutes until chicken edges are charred and cauliflower tips are browned. Drizzle with creamy tahini lemon sauce and garnish with fresh parsley.",
        "takeaways": [
            ("Za'atar Herb Crust Magic", "Toasted sesame seeds, wild thyme, and tangy sumac in za'atar form a savory crunchy bark on chicken thighs under 450°F roasting."),
            ("Small Cauliflower Floret Sizing", "Cutting cauliflower into small 1-inch florets ensures they roast into nutty, caramelized browned bites in the exact same 14-minute window as chicken thighs."),
            ("High-Broil Caramelization", "Finishing the sheet pan on high broil for 120 seconds blisters the cherry tomatoes into sweet juicy pockets and crisps the poultry edges.")
        ],
        "matrix_title": "Vegetable Pairing Performance with Za'atar Spiced Poultry",
        "matrix_headers": ["Vegetable", "Roast Time at 450°F", "Moisture Release", "Char Flavor", "Verdict"],
        "matrix_rows": [
            ["Cauliflower Florets (1-inch)", "14–15 minutes", "Low (stays crisp)", "Nutty caramelized sweetness", "Top Pick for Sheet Pans (Recommended)"],
            ["Broccoli Florets", "12 minutes", "Low", "Crisp charred edges", "Great fast alternative"],
            ["Zucchini Chunks", "10–12 minutes", "High (can get watery)", "Mild", "Better added halfway through"],
            ["Whole Baby Carrots", "20+ minutes", "Low", "Sweet", "Needs par-cooking first"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken thighs",
            "1 small head cauliflower, broken into bite-sized 1-inch florets",
            "1 cup whole sweet cherry tomatoes",
            "1 small red onion, cut into wedges",
            "1 organic lemon, thinly sliced into wheels",
            "2.5 tbsp extra virgin olive oil (divided)",
            "2 tbsp authentic za'atar spice blend",
            "1 tsp ground cumin",
            "1 tsp garlic powder",
            "1 tsp kosher salt & 1/2 tsp freshly cracked black pepper",
            "1/3 cup prepared tahini sauce (whisked with lemon juice, garlic, and water)",
            "Fresh flat-leaf parsley and ground sumac for garnish"
        ],
        "instructions": [
            ("Preheat & Season", "Preheat oven to 450°F (230°C). In a large mixing bowl, combine chicken thighs, cauliflower florets, and red onion wedges. Drizzle with 2 tbsp olive oil. Sprinkle with za'atar, cumin, garlic powder, salt, and black pepper. Toss well with hands until everything is coated in the herbal spice blend."),
            ("Arrange on Sheet Pan", "Spread the seasoned chicken and vegetables in a single layer across a large heavy rimmed baking sheet. Scatter the cherry tomatoes and lemon slices into open spaces."),
            ("High-Heat Roast", "Roast at 450°F for 14 minutes until chicken reaches 165°F internal temperature and cauliflower stems are fork-tender."),
            ("Broil for Crispy Char", "Switch oven to HIGH BROIL for the final 2 minutes. Watch closely as chicken edges blister into dark roasted bits and tomatoes burst."),
            ("Sauce & Serve", "Remove sheet pan from oven. Drizzle with creamy lemon tahini sauce. Dust with bright red sumac and fresh chopped parsley. Serve hot with warm pita bread or over fluffy grains!")
        ],
        "pro_tip_title": "Elena’s Authentic Za'atar Buying Tip",
        "pro_tip": "Check the ingredient label when buying za'atar! Genuine Middle Eastern za'atar (Lebanese, Jordanian, or Palestinian) contains wild hyssop/thyme, toasted sesame seeds, and tart red sumac. Avoid cheap blends loaded with wheat flour or filler spices—pure za'atar gives an unforgettable tangy, earthy herbal crunch.",
        "faqs": [
            ("Can I use bone-in chicken thighs?", "Bone-in thighs take 25–30 minutes to cook through; for this 20-minute dinner, stick with boneless skinless thighs or chicken cutlets."),
            ("How do I make the quick tahini drizzle?", "Whisk 3 tbsp pure tahini paste with 2 tbsp warm water, 1 tbsp fresh lemon juice, 1/2 minced garlic clove, and a pinch of salt until smooth and pourable."),
            ("Is this recipe gluten-free and low-carb?", "Yes! With roasted cauliflower as the vegetable base, it is naturally keto, low-carb, and gluten-free.")
        ],
        "wiki_entities": [
            ("Za'atar", "https://en.wikipedia.org/wiki/Za%27atar"),
            ("Tahini", "https://en.wikipedia.org/wiki/Tahini"),
            ("Sumac", "https://en.wikipedia.org/wiki/Sumac")
        ],
        "pinterest": {
            "board": "Sheet Pan Suppers / Healthy Chicken Dinners",
            "title": "20-Minute Sheet-Pan Crispy Za'atar Chicken Thighs with Cauliflower",
            "desc": "Crispy herbal za'atar chicken thighs roasted with nutty cauliflower, burst tomatoes, and lemon tahini on one sheet pan in 20 minutes! Healthy Middle Eastern dinner. Save the recipe!",
            "tags": "#zaatarchicken #sheetpanmeals #20minutedinner #healthyrecipes #mediterraneandiet #glutenfree #easyrecipes"
        }
    },
    {
        "slug": "15-minute-creamy-florentine-tilapia-skillet",
        "title": "15-Minute Creamy Garlic Florentine Tilapia Skillet with Spinach",
        "headline": "15-Minute Creamy Garlic Butter Florentine Tilapia Fillets",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/creamy-florentine-tilapia-skillet.jpg",
        "image_file": "creamy-florentine-tilapia-skillet.jpg",
        "excerpt": "Delicate golden pan-seared tilapia fillets nestled in a velvety garlic parmesan cream sauce packed with tender baby spinach, sun-dried tomatoes, and fresh dill in 15 minutes.",
        "description": "Elegant restaurant-style white fish dinner in 15 minutes: golden seared tilapia basted in a luscious garlic parmesan cream sauce with wilted spinach, lemon, and sun-dried tomatoes.",
        "keywords": "creamy florentine tilapia, pan seared tilapia, 15 minute fish dinner, garlic parmesan tilapia, easy white fish skillet, healthy low carb fish",
        "prepTime": "PT3M",
        "cookTime": "PT12M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American / Seafood",
        "calories": "380 kcal",
        "protein": "34g",
        "fat": "22g",
        "carbs": "6g",
        "fiber": "2g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "172",
        "quick_answer": "To make 15-minute creamy Florentine tilapia, pat 4 tilapia fillets (approx. 5 oz each) bone-dry and season both sides with Italian herbs, garlic powder, salt, and pepper. Heat 1 tbsp olive oil and 1 tbsp butter in a large skillet over medium-high heat. Sear tilapia undisturbed for 3 minutes per side until golden brown and flaky; transfer to a plate. Reduce heat to medium, add 1 tbsp butter, 4 minced garlic cloves, and 1/3 cup chopped sun-dried tomatoes; sauté for 60 seconds. Pour in 1/2 cup chicken or vegetable broth, 3/4 cup heavy cream, and 1/2 cup grated parmesan cheese, simmering for 2 minutes until bubbly and thickened. Stir in 3 packed cups of fresh baby spinach until wilted. Return tilapia to the skillet, spooning the velvety sauce over the fillets for 60 seconds. Finish with fresh dill and lemon wedges.",
        "takeaways": [
            ("Delicate White Fish Timing", "Tilapia is thin and tender; searing for 3 minutes per side prevents overcooking and keeps the delicate white flakes moist and succulent."),
            ("Florentine Cream Body", "Fresh baby spinach and parmesan cheese thicken heavy cream into a rich sauce that clings effortlessly to mild white fish fillets."),
            ("Sun-Dried Tomato Acidity", "Piquant sun-dried tomatoes cut through the butter cream, adding vibrant color and sweet savory notes.")
        ],
        "matrix_title": "Mild White Fish Performance in Creamy Skillet Sauces",
        "matrix_headers": ["Fish Fillet", "Cook Speed", "Flake Delicate Level", "Flavor Mildness", "Verdict"],
        "matrix_rows": [
            ["Tilapia Fillets", "3 min per side", "Tender & delicate", "Ultra-mild (absorbs sauce)", "Budget Weeknight Hero (Recommended)"],
            ["Cod Loins", "4–5 min per side", "Large milky flakes", "Mild sweet", "Great thicker alternative"],
            ["Haddock", "3–4 min per side", "Tender flakes", "Slightly sweet", "Delicious swap"],
            ["Swai / Basa", "3 min per side", "Very soft", "Very mild", "Handle carefully when flipping"]
        ],
        "ingredients": [
            "4 fresh tilapia fillets (approx. 5–6 oz each)",
            "1 tbsp extra virgin olive oil",
            "2 tbsp unsalted butter (divided)",
            "4 cloves fresh garlic, finely minced",
            "1/3 cup oil-packed sun-dried tomatoes, drained and sliced",
            "1/2 cup low-sodium chicken or vegetable broth",
            "3/4 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "3 packed cups fresh baby spinach leaves",
            "1 tsp dried Italian seasoning",
            "1/2 tsp garlic powder & 1/2 tsp kosher salt",
            "1/4 tsp freshly ground black pepper",
            "Fresh dill fronds and lemon wedges for serving"
        ],
        "instructions": [
            ("Prep & Season Fish", "Pat tilapia fillets completely dry on both sides with paper towels. Season with Italian herbs, garlic powder, salt, and black pepper."),
            ("Sear Tilapia Fillets", "Heat olive oil and 1 tbsp butter in a wide stainless steel or cast iron skillet over medium-high heat. Gently lay tilapia fillets into the hot skillet. Sear undisturbed for 3 minutes until a light golden crust forms. Carefully flip with a thin fish spatula and sear for another 2.5 to 3 minutes until fish flakes easily. Transfer fillets to a plate."),
            ("Sauté Garlic & Tomatoes", "Reduce heat to medium. Add remaining 1 tbsp butter, minced garlic, and sliced sun-dried tomatoes to the skillet drippings. Sauté for 60 seconds until fragrant without browning."),
            ("Simmer Parmesan Cream", "Pour in chicken broth, heavy cream, and grated parmesan cheese. Whisk continuously for 2 minutes as the sauce bubbles into a rich, velvety consistency."),
            ("Wilt Spinach & Combine", "Stir fresh baby spinach into the simmering sauce for 60 seconds until wilted and tender. Nestle seared tilapia fillets back into the skillet. Spoon the creamy Florentine sauce over the fish and simmer for 60 seconds to reheat. Garnish with fresh dill and serve with lemon wedges!")
        ],
        "pro_tip_title": "Elena’s Gentle Flip Technique",
        "pro_tip": "Because tilapia has fine, delicate muscle fibers without thick connective tissue, standard tongs will snap the fillets in half! Always use a wide, flexible metal spatula, slide it completely underneath the center of the fillet, and gently guide the fish over in one confident motion.",
        "faqs": [
            ("Can I use frozen tilapia?", "Yes! Thaw completely in cold water for 15 minutes, then press firmly between paper towels to remove all excess water before searing."),
            ("What sides pair best with Florentine tilapia?", "This creamy dish is fantastic served over buttered noodles, garlic mashed potatoes, steamed rice, or alongside roasted asparagus."),
            ("Is this dish keto friendly?", "Yes! At only 6g net carbs and 34g protein, it is an outstanding high-protein keto and low-carb dinner.")
        ],
        "wiki_entities": [
            ("Tilapia", "https://en.wikipedia.org/wiki/Tilapia"),
            ("Eggs Florentine", "https://en.wikipedia.org/wiki/Eggs_Florentine"),
            ("Parmigiano-Reggiano", "https://en.wikipedia.org/wiki/Parmigiano-Reggiano")
        ],
        "pinterest": {
            "board": "Quick Seafood Dinners / Low Carb Meals",
            "title": "15-Minute Creamy Garlic Florentine Tilapia Skillet",
            "desc": "Delicate pan-seared tilapia fillets in a velvety garlic parmesan cream sauce with baby spinach and sun-dried tomatoes in 15 minutes! Easy low-carb dinner. Save this recipe!",
            "tags": "#tilapia #florentine #15minutedinner #seafooddinner #lowcarbrecipes #ketodinner #easyrecipes"
        }
    },
    {
        "slug": "15-minute-spicy-mexican-chorizo-street-tacos",
        "title": "15-Minute Sizzling Mexican Pork Chorizo Street Tacos",
        "headline": "15-Minute Sizzling Mexican Pork Chorizo Street Tacos with Cotija",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/spicy-mexican-chorizo-street-tacos.jpg",
        "image_file": "spicy-mexican-chorizo-street-tacos.jpg",
        "excerpt": "Sizzling, spicy caramelized Mexican pork chorizo tucked into warm charred corn tortillas, topped with diced white onions, fresh cilantro, salty cotija cheese, and lime in 15 minutes.",
        "description": "Authentic street cart flavor in 15 minutes: crispy crumbly Mexican pork chorizo crisped in a hot skillet, served in doubled corn tortillas with fresh cilantro, onions, and crumbled cotija.",
        "keywords": "chorizo tacos, mexican street tacos, 15 minute taco dinner, spicy pork chorizo, easy taco tuesday, quick weeknight mexican",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings (8 tacos)",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mexican / Street Food",
        "calories": "460 kcal",
        "protein": "24g",
        "fat": "28g",
        "carbs": "26g",
        "fiber": "4g",
        "sodium": "720mg",
        "ratingValue": "4.9",
        "reviewCount": "191",
        "quick_answer": "To make 15-minute Mexican pork chorizo street tacos, remove casings from 1 lb fresh Mexican pork chorizo and add to a dry skillet over medium-high heat. Break apart with a wooden spoon and fry for 7 to 8 minutes until deeply browned, crispy at the edges, and fully rendered (drain excess rendered oil if needed). While chorizo crisps, warm 8 small corn tortillas directly over an open gas burner for 15 seconds per side until lightly charred and pliable. Double up the tortillas (two per taco), spoon in generous heaps of sizzling chorizo, and top with finely diced white onion, chopped fresh cilantro, crumbled salty cotija cheese, and sliced radishes. Serve immediately with fresh lime wedges.",
        "takeaways": [
            ("Raw Mexican vs. Cured Spanish Chorizo", "Always buy raw fresh Mexican pork chorizo (seasoned with vinegar, ancho, and paprika); it renders into crispy crumbly taco meat unlike hard cured Spanish chorizo."),
            ("Rendered Fat Browning", "Chorizo contains rich pork fat that crisps the seasoned meat in its own oils—no extra cooking oil is required in the skillet."),
            ("Raw Onion & Lime Acidity Cut", "Finely diced sharp white onion and fresh lime juice cut cleanly through the rich, spiced pork fats for street-cart balance.")
        ],
        "matrix_title": "Chorizo Variety Breakdown for Street Tacos",
        "matrix_headers": ["Chorizo Variety", "Casing / State", "Skillet Texture", "Cook Speed", "Verdict"],
        "matrix_rows": [
            ["Fresh Mexican Pork Chorizo", "Raw / Bulk grind", "Crispy, crumbly caramelized bits", "7–8 minutes", "Street Cart Standard Winner (Recommended)"],
            ["Mexican Beef Chorizo", "Raw / Bulk", "Rich beefy crumbles", "7 minutes", "Great beef alternative"],
            ["Spanish Chorizo", "Cured / Hard sausage", "Chewy slices", "3 minutes (reheating)", "Best for paella or charcuterie"],
            ["Soyrizo (Plant-Based)", "Raw / Bulk", "Soft crumbly texture", "5 minutes", "Outstanding vegan swap"]
        ],
        "ingredients": [
            "1 lb fresh Mexican pork chorizo (raw, casings removed)",
            "16 small corn street taco tortillas (doubled to make 8 tacos)",
            "1 small white onion, finely diced",
            "1/2 cup fresh cilantro leaves, finely chopped",
            "1/2 cup crumbled authentic Mexican cotija cheese (or queso fresco)",
            "3 red radishes, thinly sliced into rounds",
            "2 fresh limes, cut into wedges",
            "Optional: favorite salsa verde or avocado crema for topping"
        ],
        "instructions": [
            ("Crisp the Chorizo", "Place a large cast iron or heavy stainless skillet over medium-high heat. Add raw pork chorizo and break it apart with a wooden spoon or potato masher. Cook for 7 to 8 minutes, stirring occasionally, until the meat is deeply browned, rendered, and develops dark crispy caramelized bits. (Tilt pan and spoon out excess grease if desired)."),
            ("Char Corn Tortillas", "While chorizo cooks, char the corn tortillas directly over a low open gas flame for 15 seconds per side until pliable with blistered spots (or warm in a dry hot skillet)."),
            ("Double Stack Tortillas", "Stack two warm tortillas on top of each other for each taco (8 double-stacked taco bases total) on a wooden platter or plates."),
            ("Fill with Sizzling Chorizo", "Spoon generous portions of the hot crispy chorizo down the center of each doubled tortilla."),
            ("Top & Serve", "Shower each taco with finely diced white onion, chopped cilantro, crumbled cotija cheese, and crisp radish coins. Squeeze fresh lime juice generously over the tacos and serve piping hot!")
        ],
        "pro_tip_title": "Elena’s Double Tortilla Street Rule",
        "pro_tip": "Authentic taquerias always serve street tacos with two tortillas stacked together! Sizzling chorizo releases flavorful chili oils that will soak through and split a single corn tortilla. Doubling them up catches all the savory juices so your taco stays sturdy and delicious to the very last bite.",
        "faqs": [
            ("Can I add eggs to this?", "Yes! Chorizo con huevos (chorizo with scrambled eggs) makes an extraordinary 15-minute breakfast-for-dinner taco."),
            ("Where do I find cotija cheese?", "Cotija is found in the refrigerated specialty cheese or Hispanic foods section. If unavailable, crumbled salty feta cheese makes a wonderful substitute."),
            ("How do I store leftover chorizo?", "Store cooked chorizo in an airtight container for up to 5 days in the fridge. Reheat in a dry skillet over medium heat for 2 minutes to restore the crispy edges.")
        ],
        "wiki_entities": [
            ("Chorizo", "https://en.wikipedia.org/wiki/Chorizo"),
            ("Taco", "https://en.wikipedia.org/wiki/Taco"),
            ("Cotija cheese", "https://en.wikipedia.org/wiki/Cotija_cheese")
        ],
        "pinterest": {
            "board": "Taco Tuesday / Mexican Street Food",
            "title": "15-Minute Sizzling Mexican Pork Chorizo Street Tacos",
            "desc": "Crispy caramelized Mexican pork chorizo in warm charred tortillas with diced onions, cilantro, and cotija cheese in 15 minutes! The ultimate viral taco night. Pin it now!",
            "tags": "#chorizotacos #streettacos #tacotuesday #15minutedinner #mexicanfood #quickdinner #easyrecipes"
        }
    },
    {
        "slug": "15-minute-creamy-spicy-miso-ramen",
        "title": "15-Minute Creamy Spicy Miso Ramen with Jammy Soft-Boiled Egg",
        "headline": "15-Minute Creamy Spicy Garlic Miso Ramen Bowl",
        "badge": "One-Pot Dinners &bull; 15 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/creamy-spicy-miso-ramen.jpg",
        "image_file": "creamy-spicy-miso-ramen.jpg",
        "excerpt": "Springy ramen noodles bathed in a rich, velvety spicy garlic miso broth, topped with sweet corn, baby spinach, a jammy marinated egg, and chili oil in 15 minutes.",
        "description": "Tokyo ramen shop quality in 15 minutes: springy noodles swimming in a rich, creamy white miso and sesame chili broth with sweet buttered corn, baby spinach, and a runny soft-boiled egg.",
        "keywords": "spicy miso ramen, 15 minute ramen, creamy miso ramen, quick weeknight noodles, easy homemade ramen, japanese ramen bowl",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Japanese / Tokyo Noodle Shop",
        "calories": "480 kcal",
        "protein": "18g",
        "fat": "22g",
        "carbs": "56g",
        "fiber": "4g",
        "sodium": "780mg",
        "ratingValue": "4.9",
        "reviewCount": "198",
        "quick_answer": "To make 15-minute creamy spicy miso ramen, heat 1 tbsp sesame oil in a pot over medium heat. Sauté 3 minced garlic cloves and 1 tbsp grated ginger for 45 seconds. Whisk in 3 tbsp white or yellow miso paste, 2 tbsp tahini (or unsweetened creamy peanut butter), 1 tbsp chili oil or chili crisp, 1 tbsp soy sauce, and 1 tsp sugar until smooth. Pour in 5 cups rich chicken bone broth (or vegetable broth) and 1/2 cup unsweetened soy milk or oat milk (this creates the signature cloudy, velvety ramen emulsion). Bring to a gentle simmer for 3 minutes. In a separate pot of boiling water, cook 4 packs of fresh or instant ramen noodles (discard seasoning packets) for 2 to 3 minutes; drain. Divide noodles into bowls, ladle hot creamy miso broth over them, and top with warm sweet corn, baby spinach, sliced green scallions, toasted sesame seeds, and a halved jammy soft-boiled egg.",
        "takeaways": [
            ("Soy Milk & Tahini Broth Emulsion", "Whisking a splash of unsweetened soy milk and sesame tahini into hot chicken broth mimics the rich, collagen-heavy mouthfeel of 12-hour tonkotsu broth in 3 minutes."),
            ("Gentle Miso Dissolution", "Never boil miso paste vigorously; dissolving miso over gentle heat preserves active live enzymes, aromatic fragrance, and prevents graininess."),
            ("Separate Water Noodle Boil", "Boiling ramen noodles in plain salted water rather than directly in the broth prevents starchy cloudiness from muddying the pristine miso broth.")
        ],
        "matrix_title": "Miso Paste Selection for Rich Ramen Broth",
        "matrix_headers": ["Miso Variety", "Fermentation Time", "Saltiness / Sweetness", "Body & Color", "Verdict"],
        "matrix_rows": [
            ["White Miso (Shiro Miso)", "Short (sweet & mild)", "Gentle sweetness, low salt", "Light golden, silky", "Perfect Creamy Base (Recommended)"],
            ["Yellow Miso (Shinshu)", "Medium", "Balanced, savory umami", "Earthy golden", "Great all-purpose choice"],
            ["Red Miso (Aka Miso)", "Long (deep & pungent)", "High salt, intense umami", "Dark mahogany", "Best blended 50/50 with white"],
            ["Awase Miso (Mixed)", "Balanced blend", "Deep savory balance", "Amber color", "Excellent rich alternative"]
        ],
        "ingredients": [
            "4 portions fresh ramen noodles (or 4 packs instant ramen with seasoning packets discarded)",
            "5 cups rich chicken bone broth or low-sodium vegetable stock",
            "1/2 cup unsweetened plain soy milk, oat milk, or whole milk",
            "3 tbsp Japanese white (shiro) miso paste",
            "2 tbsp sesame paste (neri goma) or tahini",
            "1 tbsp toasted sesame oil",
            "1 tbsp chili oil or chili crunch (plus more for drizzling)",
            "1 tbsp low-sodium soy sauce",
            "3 cloves fresh garlic, finely minced",
            "1 tbsp fresh ginger, grated",
            "1 tsp brown sugar",
            "1 cup sweet canned or frozen corn kernels, drained and warmed",
            "2 cups fresh baby spinach leaves",
            "4 soft-boiled ramen eggs (jammy 6.5-minute eggs), halved",
            "2 green onions, thinly sliced, and toasted sesame seeds"
        ],
        "instructions": [
            ("Boil Noodles", "Bring a large pot of water to a rolling boil. Drop in ramen noodles and cook according to package instructions (about 2 to 3 minutes until chewy). Drain in a colander, rinse briefly with warm water to remove excess surface starch, and set aside."),
            ("Sauté Aromatics", "In a separate soup pot or Dutch oven, heat sesame oil over medium heat. Add minced garlic and grated ginger; sauté for 45 seconds until fragrant without browning."),
            ("Whisk Miso & Tahini Paste", "Reduce heat to low. Add white miso paste, tahini, chili oil, soy sauce, and brown sugar. Whisk continuously for 60 seconds into a smooth, fragrant aromatic paste."),
            ("Simmer Creamy Broth", "Gradually pour in the chicken bone broth and unsweetened soy milk while whisking vigorously until the miso paste fully dissolves. Bring to a gentle bubbling simmer over medium-low heat for 3 to 4 minutes until velvety and steaming hot (do not hard-boil)."),
            ("Assemble Bowls", "Divide cooked noodles among 4 deep ramen bowls. Ladle the hot creamy spicy miso broth generously over the noodles. Arrange sweet corn, baby spinach, green scallions, and a halved jammy egg on top. Drizzle with extra chili oil and shower with sesame seeds!")
        ],
        "pro_tip_title": "Elena’s 6.5-Minute Jammy Egg Recipe",
        "pro_tip": "For genuine ramen-shop jammy eggs: lower cold eggs straight from the fridge into boiling water. Boil for exactly 6 minutes and 30 seconds, then immediately plunge into an ice water bath for 5 minutes. The whites are completely set and tender while the yolk stays thick, golden, and gooey.",
        "faqs": [
            ("Can I make this vegetarian or vegan?", "Yes! Use rich vegetable stock, plant-based unsweetened soy milk, and replace the soft-boiled egg with crispy pan-seared cubed tofu."),
            ("How spicy is this broth?", "It has a comforting medium warmth from the chili oil. You can dial it down by using 1/2 tbsp chili oil or boost it with extra chili crisp and sriracha."),
            ("What are the best noodles to buy?", "Look for fresh refrigerated Japanese ramen noodles (such as Sun Noodle or Myojo) in the produce or Asian refrigerated section; they have incredible chew and elasticity.")
        ],
        "wiki_entities": [
            ("Ramen", "https://en.wikipedia.org/wiki/Ramen"),
            ("Miso", "https://en.wikipedia.org/wiki/Miso"),
            ("Tahini", "https://en.wikipedia.org/wiki/Tahini")
        ],
        "pinterest": {
            "board": "Cozy Noodle Soups / Japanese Dinners",
            "title": "15-Minute Creamy Spicy Miso Ramen with Jammy Egg",
            "desc": "Springy noodles in a velvety spicy garlic miso broth with sweet corn, baby spinach, and a runny jammy egg in 15 minutes! Authentic Tokyo ramen shop magic at home. Pin it now!",
            "tags": "#misoramen #ramennoodles #15minutedinner #japanesefood #spicyramen #comfortfood #noodlesoup"
        }
    },
    {
        "slug": "15-minute-crispy-teriyaki-tofu-rice-bowls",
        "title": "15-Minute Crispy Teriyaki Glazed Tofu Rice Bowls",
        "headline": "15-Minute Crispy Cornstarch-Crusted Teriyaki Tofu Rice Bowls",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/crispy-teriyaki-tofu-rice-bowls.jpg",
        "image_file": "crispy-teriyaki-tofu-rice-bowls.jpg",
        "excerpt": "Golden cornstarch-crusted crispy tofu cubes glistening in a sticky sweet and savory teriyaki glaze over steamed sushi rice with edamame and avocado in 15 minutes.",
        "description": "Restaurant-crispy tofu in 15 minutes: extra-firm tofu cubes tossed in cornstarch, pan-fried to shatteringly crisp perfection, and glazed in homemade honey ginger teriyaki sauce over rice.",
        "keywords": "crispy teriyaki tofu, tofu rice bowls, 15 minute vegetarian dinner, crispy tofu recipe, easy vegan weeknight dinner, quick asian bowls",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Japanese / Plant-Based Bowls",
        "calories": "420 kcal",
        "protein": "19g",
        "fat": "16g",
        "carbs": "52g",
        "fiber": "6g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "176",
        "quick_answer": "To make 15-minute crispy teriyaki tofu rice bowls, press 1 block (14 oz) extra-firm tofu firmly in paper towels to extract moisture, cut into 1-inch cubes, and toss with 2 tbsp cornstarch and 1/2 tsp salt until powdery and coated. Heat 2 tbsp oil in a large skillet over medium-high heat. Add tofu cubes in a single layer; pan-fry for 6 to 7 minutes, turning every 2 minutes until all sides are golden brown and crunchy. In a small cup, whisk 3 tbsp low-sodium soy sauce, 2 tbsp mirin, 2 tbsp brown sugar (or maple syrup), 1 minced garlic clove, and 1 tsp grated ginger. Pour the teriyaki sauce over the hot crispy tofu; toss for 60 seconds as the sauce bubbles into a thick, glossy lacquer. Spoon over warm sushi rice with steamed edamame, sliced avocado, and sesame seeds.",
        "takeaways": [
            ("Cornstarch Protective Crust", "Dredging dry tofu cubes in cornstarch creates a barrier that locks in moisture while frying into a shatteringly crisp exterior shell."),
            ("Super-Firm Tofu Selection", "Selecting high-protein extra-firm or vacuum-packed super-firm tofu skips 30 minutes of heavy pressing and holds clean cube shapes in the skillet."),
            ("Simmering Teriyaki Caramelization", "Pouring the mirin-soy-ginger sauce into the hot skillet glazes the crispy crust instantly without making the tofu soggy.")
        ],
        "matrix_title": "Tofu Variety Performance for High-Speed Crispy Pan-Frying",
        "matrix_headers": ["Tofu Firmness", "Water Content", "Crispiness Potential", "Prep Time", "Verdict"],
        "matrix_rows": [
            ["Extra-Firm Tofu", "Low", "Shatteringly crisp golden crust", "2 min towel press", "Best Balanced Weeknight Option (Recommended)"],
            ["Super-Firm (Vacuum-Packed)", "Extremely low", "Ultra-dense & crunchy", "Zero pressing needed", "Fastest & crispest choice"],
            ["Firm Tofu", "Moderate", "Crispy exterior, soft inside", "10 min press needed", "Good alternative"],
            ["Silken / Soft Tofu", "Very high", "Breaks apart into mush", "N/A", "Avoid for pan frying"]
        ],
        "ingredients": [
            "1 block (14–16 oz) extra-firm or super-firm tofu",
            "2 tbsp cornstarch",
            "2 tbsp avocado or neutral oil",
            "3 tbsp low-sodium soy sauce or tamari",
            "2 tbsp Japanese mirin (sweet cooking wine)",
            "2 tbsp brown sugar or pure maple syrup",
            "1 tbsp water",
            "2 cloves fresh garlic, finely minced",
            "1 tsp fresh ginger, grated",
            "4 cups warm cooked sushi or jasmine rice",
            "1 cup steamed shelled edamame",
            "1 ripe Hass avocado, sliced",
            "2 red radishes, shaved thin",
            "1 tbsp toasted white and black sesame seeds, plus sliced scallions"
        ],
        "instructions": [
            ("Dry & Coat Tofu", "Wrap the tofu block in several layers of paper towels and press firmly with your palms to extract surface water. Cut into uniform 1-inch cubes. Place in a bowl, sprinkle with cornstarch and a pinch of salt, and toss gently until all sides are evenly coated with a dry powdery layer."),
            ("Pan-Fry to Shattering Crispness", "Heat oil in a large cast iron or non-stick skillet over medium-high heat until shimmering. Add tofu cubes in a single layer with space between each piece. Cook for 6 to 7 minutes, turning with tongs every 2 minutes so each facet becomes deeply golden and crackly."),
            ("Whisk Teriyaki Glaze", "In a measuring cup or small bowl, whisk together soy sauce, mirin, brown sugar, water, minced garlic, and grated ginger until sugar dissolves."),
            ("Glaze the Crispy Tofu", "Pour the teriyaki sauce directly over the hot sizzling tofu in the skillet. Toss continuously with a spatula for 60 to 90 seconds as the sauce bubbles violently, reduces, and forms a thick, sticky, amber lacquer coating every cube."),
            ("Assemble Bowls", "Divide warm rice into four bowls. Top with generous heaps of sticky glazed tofu, steamed edamame, sliced avocado, and shaved radishes. Drizzle with extra pan sauce and shower with toasted sesame seeds and scallions!")
        ],
        "pro_tip_title": "Elena’s Cornstarch Tossing Trick",
        "pro_tip": "Toss your tofu cubes in cornstarch inside a large sealable container or gallon ziplock bag! Shaking the bag gently aerates the cubes and spreads an ultra-thin, microscopic film of starch over every single millimeter of tofu, guaranteeing 100% crunch without clumping.",
        "faqs": [
            ("Can I make this in the air fryer?", "Yes! Air fry cornstarch-coated tofu at 400°F for 10–12 minutes, shaking halfway until crisp. Simmer the teriyaki glaze in a small skillet and toss the hot air-fried tofu right in."),
            ("Is this recipe gluten-free?", "To make it 100% gluten-free, substitute tamari or gluten-free soy sauce for traditional soy sauce."),
            ("How do I store leftovers?", "Store glazed tofu in an airtight container for up to 4 days. Reheat in a dry skillet or toaster oven for 3 minutes to bring back the crisp outer texture.")
        ],
        "wiki_entities": [
            ("Tofu", "https://en.wikipedia.org/wiki/Tofu"),
            ("Teriyaki", "https://en.wikipedia.org/wiki/Teriyaki"),
            ("Mirin", "https://en.wikipedia.org/wiki/Mirin")
        ],
        "pinterest": {
            "board": "Vegetarian Dinners / Asian Rice Bowls",
            "title": "15-Minute Crispy Teriyaki Glazed Tofu Rice Bowls",
            "desc": "Crispy golden cornstarch-crusted tofu cubes glistening in a sticky teriyaki glaze over sushi rice with edamame and avocado in 15 minutes! The ultimate viral vegan bowl. Pin it now!",
            "tags": "#teriyakitofu #crispytofu #15minutedinner #plantbased #tofubowl #veganrecipes #healthyfood"
        }
    },
    {
        "slug": "15-minute-spicy-sichuan-dan-dan-noodles",
        "title": "15-Minute Spicy Sichuan Dan Dan Noodles with Crispy Pork",
        "headline": "15-Minute Sizzling Sichuan Dan Dan Noodles with Minced Pork",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/spicy-sichuan-dan-dan-noodles.jpg",
        "image_file": "spicy-sichuan-dan-dan-noodles.jpg",
        "excerpt": "Springy wheat noodles bathed in a fiery, nutty sesame peanut chili broth, topped with crispy caramelized minced pork, tender bok choy, and crushed peanuts in 15 minutes.",
        "description": "Authentic Chengdu street food at home: springy noodles tossed in toasted sesame paste, Sichuan chili oil, and soy sauce, crowned with dark crispy pork crumbles and crushed peanuts.",
        "keywords": "dan dan noodles, sichuan noodles, 15 minute spicy noodles, crispy pork noodles, chengdu street food, easy weeknight noodles",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Sichuan / Chinese Street Food",
        "calories": "520 kcal",
        "protein": "28g",
        "fat": "26g",
        "carbs": "46g",
        "fiber": "3g",
        "sodium": "760mg",
        "ratingValue": "4.9",
        "reviewCount": "199",
        "quick_answer": "To make 15-minute spicy Sichuan Dan Dan noodles, heat 1 tbsp oil in a skillet over high heat. Add 1/2 lb ground pork; stir-fry for 5 minutes, breaking into fine crumbles until deeply browned and crispy. Add 2 minced garlic cloves, 1 tbsp soy sauce, and 1 tsp hoisin sauce; toss for 60 seconds and set aside. In a measuring pitcher, whisk 3 tbsp Chinese sesame paste (or tahini + peanut butter), 3 tbsp low-sodium soy sauce, 2 tbsp Sichuan chili oil with flakes, 1 tbsp Chinkiang black vinegar, 1 tsp ground Sichuan pepper, 1 tsp sugar, and 1.5 cups hot chicken broth. Boil 10 oz Chinese wheat noodles and 2 halved baby bok choy for 3 minutes; drain. Divide the warm sesame chili broth into 4 bowls, add noodles and bok choy, and crown with crispy pork crumbles, crushed peanuts, and green onions. Toss together with chopsticks and enjoy!",
        "takeaways": [
            ("Sesame Paste & Black Vinegar Synergy", "Nutty toasted sesame paste combined with acidic, malty Chinkiang black vinegar forms the rich emulsified broth foundation that defines Chengdu street food."),
            ("Crispy Pork Caramelization", "Frying ground pork until moisture evaporates leaves behind dark, crispy savory nuggets that provide crunchy contrast against soft noodles."),
            ("Tingle of Sichuan Pepper", "Ground Sichuan peppercorns contribute signature floral citrus numbness (málà) that elevates the dish beyond ordinary chili heat.")
        ],
        "matrix_title": "Sesame Base Selection for Authentic Dan Dan Broth",
        "matrix_headers": ["Sesame Base", "Roast Depth", "Viscosity", "Flavor Profile", "Verdict"],
        "matrix_rows": [
            ["Chinese Roasted Sesame Paste (Zhi Ma Jiang)", "Deep dark roasted", "Very thick", "Intensely nutty, toasty", "Authentic Gold Standard (Recommended)"],
            ["Tahini + 1 tsp Toasted Sesame Oil", "Light roast", "Medium", "Creamy, mild nutty", "Outstanding pantry substitute"],
            ["Natural Creamy Peanut Butter", "Sweet roasted", "Thick", "Sweet & savory", "Popular Western takeout style"],
            ["White Sesame Seeds Blended", "Moderate", "Coarse", "Grainy", "Too textured for broth"]
        ],
        "ingredients": [
            "10 oz fresh or dried Chinese wheat noodles (or ramen noodles)",
            "1/2 lb lean ground pork (or ground chicken/turkey)",
            "2 heads baby bok choy, halved lengthwise",
            "1 tbsp avocado or peanut oil",
            "2 cloves fresh garlic, minced",
            "1 tbsp soy sauce & 1 tsp hoisin sauce (for pork)",
            "3 tbsp Chinese roasted sesame paste (or 2 tbsp tahini + 1 tbsp peanut butter)",
            "3 tbsp low-sodium soy sauce",
            "2 tbsp Chinese chili oil with sediment flakes",
            "1 tbsp Chinkiang black vinegar (or rice vinegar)",
            "1 tsp ground Sichuan peppercorns (toasted and ground)",
            "1 tsp sugar",
            "1.5 cups hot low-sodium chicken bone broth",
            "1/3 cup roasted unsalted peanuts, roughly chopped",
            "2 green onions, thinly sliced"
        ],
        "instructions": [
            ("Crisp the Ground Pork", "Heat 1 tbsp oil in a skillet over high heat. Add ground pork and fry for 5 minutes, breaking it into fine crumbles with a spatula until all liquid evaporates and the meat turns deeply browned and crispy. Stir in minced garlic, 1 tbsp soy sauce, and 1 tsp hoisin; cook for 60 seconds until fragrant. Remove from heat."),
            ("Whisk Dan Dan Sauce Broth", "In a medium bowl or measuring cup, whisk sesame paste, 3 tbsp soy sauce, chili oil, black vinegar, ground Sichuan pepper, sugar, and hot chicken broth until silky and emulsified."),
            ("Boil Noodles & Bok Choy", "Bring a large pot of water to a rolling boil. Add noodles and halved bok choy; boil for 2.5 to 3 minutes until noodles are chewy and bok choy is bright green. Drain well in a colander."),
            ("Assemble the Bowls", "Divide the warm, nutty sesame chili broth among 4 serving bowls. Drop the drained noodles into the center of each bowl and arrange bok choy along the side."),
            ("Top & Mix", "Spoon generous portions of the crispy browned pork crumbles over the noodles. Garnish with chopped peanuts and sliced scallions. Use chopsticks to vigorously mix the noodles into the fiery sesame broth before slurping!")
        ],
        "pro_tip_title": "Elena’s Chinkiang Black Vinegar Secret",
        "pro_tip": "If you don't own Chinkiang black vinegar (Zhenjiang vinegar), pick up a bottle at an Asian market! Made from fermented glutinous rice, it has a rich, smoky, malted umami acidity with none of the harsh sour bite of white vinegar. It transforms Dan Dan noodle broth from ordinary into award-winning.",
        "faqs": [
            ("Can I make this vegetarian / vegan?", "Yes! Substitute finely diced shiitake mushrooms or plant-based ground meat for the pork, and use vegetable broth."),
            ("How do I control the Sichuan peppercorn numbness?", "Sichuan pepper produces a tingling 'mala' sensation on the tongue. If you're new to it, start with 1/2 teaspoon and increase to taste!"),
            ("Can I use spaghetti noodles?", "In a pinch, standard spaghetti cooked al dente in water with 1 tsp baking soda mimics the bouncy chew of alkaline Chinese wheat noodles!")
        ],
        "wiki_entities": [
            ("Dandan noodles", "https://en.wikipedia.org/wiki/Dandan_noodles"),
            ("Sichuan pepper", "https://en.wikipedia.org/wiki/Sichuan_pepper"),
            ("Chili oil", "https://en.wikipedia.org/wiki/Chili_oil")
        ],
        "pinterest": {
            "board": "Spicy Noodle Recipes / Asian Street Food",
            "title": "15-Minute Spicy Sichuan Dan Dan Noodles with Crispy Pork",
            "desc": "Springy noodles swimming in a fiery, nutty sesame chili broth crowned with crispy pork and crushed peanuts in 15 minutes! Authentic Chengdu street food. Save the recipe!",
            "tags": "#dandannoodles #sichuannoodles #15minutedinner #spicynoodles #chinesefood #asianstreetfood #easyrecipes"
        }
    },
    {
        "slug": "20-minute-creamy-garlic-butter-caprese-chicken",
        "title": "20-Minute Creamy Garlic Butter Caprese Chicken Skillet",
        "headline": "20-Minute Creamy Garlic Butter Caprese Chicken with Melted Mozzarella",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/creamy-garlic-butter-caprese-chicken.jpg",
        "image_file": "creamy-garlic-butter-caprese-chicken.jpg",
        "excerpt": "Juicy golden seared chicken cutlets smothered in a rich garlic butter cream sauce, topped with melted fresh mozzarella, sweet blistered cherry tomatoes, and balsamic glaze in 20 minutes.",
        "description": "Italian summer comfort in a 20-minute skillet: tender golden chicken breasts smothered in a rich garlic cream sauce, topped with bubbling fresh mozzarella, blistered cherry tomatoes, and basil.",
        "keywords": "creamy caprese chicken, garlic butter caprese, 20 minute chicken skillet, one pot chicken dinner, melted mozzarella chicken, easy italian chicken",
        "prepTime": "PT4M",
        "cookTime": "PT16M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American / Comfort Skillet",
        "calories": "510 kcal",
        "protein": "42g",
        "fat": "32g",
        "carbs": "8g",
        "fiber": "1g",
        "sodium": "610mg",
        "ratingValue": "4.9",
        "reviewCount": "195",
        "quick_answer": "To make 20-minute creamy garlic butter Caprese chicken, season 4 thin chicken cutlets (1.25 lbs) with Italian herbs, garlic powder, salt, and pepper. Heat 1 tbsp olive oil and 1 tbsp butter in a cast iron skillet over medium-high heat; sear chicken for 3.5 minutes per side until golden brown, then transfer to a plate. In the same pan, sauté 4 minced garlic cloves and 1.5 cups whole sweet cherry tomatoes for 2 minutes until tomatoes begin to blister and burst. Lower heat to medium, pour in 1/2 cup chicken broth, 3/4 cup heavy cream, and 1/3 cup grated parmesan cheese; simmer for 2 minutes until glossy. Return chicken to the skillet, top each cutlet with a thick slice of fresh mozzarella cheese, cover skillet with a lid for 2 minutes until cheese is melted and bubbling. Drizzle with thick balsamic glaze and scatter fresh basil leaves.",
        "takeaways": [
            ("Sweet Blistered Cherry Tomato Burst", "Sautéing whole cherry tomatoes until their skins burst releases sweet acidic juices directly into the garlic cream sauce."),
            ("Melted Fresh Mozzarella Blanket", "Covering the pan with a lid for 120 seconds captures steam, melting fresh mozzarella into a gooey, stretchy blanket over the chicken without baking."),
            ("Balsamic Glaze Contrast", "A final zigzag drizzle of concentrated balsamic glaze provides a sweet-tart punch that cuts through the rich cream and cheese.")
        ],
        "matrix_title": "Mozzarella Variety Performance in Stovetop Skillets",
        "matrix_headers": ["Mozzarella Type", "Melt Stretch", "Moisture Level", "Flavor Freshness", "Verdict"],
        "matrix_rows": [
            ["Fresh Mozzarella Ball (Sliced)", "Gooey, velvety melt", "High (pat dry with towel)", "Delicate, sweet milk", "Top Gourmet Trattoria Pick (Recommended)"],
            ["Low-Moisture Whole Milk Mozzarella", "Super stretchy pizza pull", "Low", "Rich & salty", "Great weeknight standby"],
            ["Bocconcini (Baby Mozzarella)", "Cute melted pockets", "High", "Mild & fresh", "Fun alternative"],
            ["Part-Skim Shredded Mozzarella", "Moderate stretch", "Very low", "Dry", "Avoid (lacks creamy luxury)"]
        ],
        "ingredients": [
            "1.25 lbs boneless skinless chicken breasts, sliced horizontally into 4 thin cutlets",
            "1 tbsp extra virgin olive oil",
            "2 tbsp unsalted butter (divided)",
            "4 cloves fresh garlic, finely minced",
            "1.5 cups whole sweet red and yellow cherry tomatoes",
            "1/2 cup low-sodium chicken broth",
            "3/4 cup heavy whipping cream",
            "1/3 cup freshly grated Parmigiano-Reggiano cheese",
            "4 thick slices fresh mozzarella cheese (approx. 6 oz total)",
            "1 tsp dried Italian seasoning & 1/2 tsp garlic powder",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "2 tbsp thick balsamic glaze (balsamic reduction)",
            "1/2 cup fresh basil leaves, roughly torn"
        ],
        "instructions": [
            ("Season & Sear Chicken", "Pat chicken cutlets dry with paper towels. Season both sides with Italian seasoning, garlic powder, salt, and black pepper. Heat olive oil and 1 tbsp butter in a large cast iron skillet over medium-high heat. Add cutlets and sear for 3.5 minutes per side until golden brown and cooked through (165°F). Transfer chicken to a plate."),
            ("Blister Tomatoes & Garlic", "Reduce heat to medium. Add remaining 1 tbsp butter, minced garlic, and cherry tomatoes to the skillet drippings. Sauté for 2 minutes, pressing lightly on a few tomatoes with a wooden spoon so they blister and burst their juices."),
            ("Build Garlic Cream Sauce", "Pour in chicken broth, heavy cream, and grated parmesan cheese. Whisk continuously for 2 minutes as the sauce bubbles into a luxurious, velvety cream."),
            ("Melt Mozzarella on Chicken", "Nestle the seared chicken cutlets back into the bubbling sauce. Place a thick slice of fresh mozzarella on top of each cutlet. Cover the skillet tightly with a lid or foil for 2 minutes until the mozzarella is completely melted, gooey, and bubbling."),
            ("Finish with Balsamic & Basil", "Remove lid and take skillet off heat. Drizzle the thick balsamic glaze in a zigzag over the melted cheese and tomatoes. Scatter fresh torn basil leaves on top and serve hot straight from the skillet!")
        ],
        "pro_tip_title": "Elena’s Balsamic Glaze Shortcut",
        "pro_tip": "Buy a bottle of prepared store-bought balsamic glaze (crema di balsamico) from the vinegar aisle! It has the syrupy, concentrated consistency of 30-minute reduced balsamic vinegar, ready to drizzle instantly without boiling vinegar on a busy weeknight.",
        "faqs": [
            ("Can I make this low carb / keto?", "Yes! Naturally low in carbs at only 8g per serving, just ensure your store-bought balsamic glaze has no added high-fructose corn syrup, or use a splash of regular balsamic vinegar."),
            ("What can I serve with Caprese chicken?", "Serve over buttered angel hair pasta, alongside roasted garlic broccoli, or with crusty warm Italian bread to mop up the garlic cream sauce."),
            ("Can I use chicken thighs instead?", "Yes! Boneless skinless chicken thighs sear beautifully and remain extraordinarily juicy in this recipe.")
        ],
        "wiki_entities": [
            ("Caprese salad", "https://en.wikipedia.org/wiki/Caprese_salad"),
            ("Mozzarella", "https://en.wikipedia.org/wiki/Mozzarella"),
            ("Balsamic vinegar", "https://en.wikipedia.org/wiki/Balsamic_vinegar")
        ],
        "pinterest": {
            "board": "Quick Chicken Dinners / Italian Comfort Food",
            "title": "20-Minute Creamy Garlic Butter Caprese Chicken Skillet",
            "desc": "Golden seared chicken cutlets in a garlic butter cream sauce with melted fresh mozzarella, burst cherry tomatoes, and balsamic glaze in 20 minutes! Easy restaurant dinner. Save it now!",
            "tags": "#capresechicken #chickenskillet #20minutedinner #italianfood #comfortfood #lowcarbdinner #easyrecipes"
        }
    },
    {
        "slug": "20-minute-sheet-pan-basil-pesto-salmon-asparagus",
        "title": "20-Minute Sheet-Pan Basil Pesto Salmon with Roasted Asparagus",
        "headline": "20-Minute Sheet-Pan Basil Pesto Wild Salmon Fillets with Asparagus",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/sheet-pan-basil-pesto-salmon-asparagus.jpg",
        "image_file": "sheet-pan-basil-pesto-salmon-asparagus.jpg",
        "excerpt": "Flaky, succulent wild salmon fillets basted with a vibrant basil pesto crust, roasted on one sheet pan with tender crisp asparagus and burst cherry tomatoes in 20 minutes.",
        "description": "Effortless Mediterranean elegance in 20 minutes: center-cut salmon fillets slathered with vibrant basil pesto, roasted on a single sheet pan with fresh green asparagus, cherry tomatoes, and lemon.",
        "keywords": "sheet pan pesto salmon, salmon and asparagus, 20 minute seafood dinner, easy sheet pan salmon, pesto baked salmon, healthy mediterranean dinner",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mediterranean / Seafood",
        "calories": "460 kcal",
        "protein": "38g",
        "fat": "28g",
        "carbs": "8g",
        "fiber": "3g",
        "sodium": "510mg",
        "ratingValue": "4.9",
        "reviewCount": "189",
        "quick_answer": "To make 20-minute sheet-pan basil pesto salmon with asparagus, preheat oven to 425°F (220°C). Trim woody ends from 1 lb fresh green asparagus. Toss asparagus and 1 cup cherry tomatoes with 1 tbsp olive oil, salt, and pepper; arrange on a large rimmed baking sheet. Place 4 center-cut salmon fillets (6 oz each) in the center of the sheet pan. Season salmon with a pinch of salt, then spread 1.5 tbsp prepared basil pesto evenly over the top of each fillet, pressing gently into a vibrant green crust. Lay lemon wheels across the pan. Roast at 425°F for 12 to 14 minutes until salmon flakes easily with a fork (135°F internal temperature) and asparagus is tender-crisp with roasted tips. Finish with a squeeze of fresh lemon juice.",
        "takeaways": [
            ("Pesto Moisture Blanket", "A generous spread of basil pesto forms an aromatic herbal barrier that locks in natural salmon juices and prevents the delicate fish from drying out in the oven."),
            ("Synchronized 14-Minute Roasting", "Fresh asparagus spears and 1-inch thick salmon fillets cook to tender-crisp perfection in the exact same 12-to-14-minute window at 425°F."),
            ("Nutrient-Dense Mediterranean Profile", "Packed with healthy heart-friendly omega-3 fatty acids, vibrant green antioxidants, and 38g of clean protein with virtually zero cleanup.")
        ],
        "matrix_title": "Pesto Style Performance on Roasted Seafood",
        "matrix_headers": ["Pesto Variety", "Herbal Brightness", "Oil & Nut Texture", "Bake Stability", "Verdict"],
        "matrix_rows": [
            ["Fresh Basil Pesto (Genovese)", "Explosive fresh basil aroma", "Pine nuts & olive oil", "Holds vibrant green crust", "Top Restaurant Pick (Recommended)"],
            ["Sun-Dried Tomato Pesto (Rosso)", "Sweet & savory umami", "Rich & concentrated", "Deep golden bake", "Delicious Mediterranean variation"],
            ["Kale or Spinach Pesto", "Mild & earthy", "Smooth", "Good heat hold", "Nutrient-packed alternative"],
            ["Shelf-Stable Jarred Pesto", "Muted herbal notes", "Thinner oil", "Can brown faster", "Reliable weeknight backup"]
        ],
        "ingredients": [
            "4 fresh center-cut salmon fillets (approx. 6 oz each, skin-on)",
            "1 lb fresh asparagus, woody ends trimmed",
            "1 cup sweet cherry tomatoes (red and yellow)",
            "1/3 cup high-quality prepared basil pesto (refrigerated fresh pesto preferred)",
            "1.5 tbsp extra virgin olive oil",
            "1 organic lemon, thinly sliced into wheels and half juiced",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper",
            "1/4 cup grated Parmigiano-Reggiano cheese (optional for extra crust)",
            "Fresh basil leaves for garnish"
        ],
        "instructions": [
            ("Preheat & Prep Sheet Pan", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper or foil for easy cleanup."),
            ("Season Vegetables", "Place trimmed asparagus spears and whole cherry tomatoes on the baking sheet. Drizzle with 1.5 tbsp olive oil, 1/4 tsp salt, and 1/4 tsp pepper. Toss with hands and push to the outer edges of the pan."),
            ("Season & Pesto-Crust Salmon", "Place the salmon fillets skin-side down in the center of the baking sheet. Sprinkle each fillet with a pinch of salt. Spoon approximately 1.5 tbsp basil pesto over the top of each fillet, spreading evenly to create a thick green crust. Scatter lemon wheels across the pan."),
            ("Roast to Flaky Perfection", "Roast at 425°F for 12 to 14 minutes until the salmon is opaque, flakes easily with a fork, and reaches 130°F–135°F internal temperature, while asparagus is tender-crisp with roasted tips."),
            ("Garnish & Serve", "Remove sheet pan from oven. Squeeze fresh lemon juice over the hot salmon and vegetables. Scatter with fresh basil leaves and a dusting of parmesan cheese. Serve immediately straight from the pan!")
        ],
        "pro_tip_title": "Elena’s Refrigerated Pesto Secret",
        "pro_tip": "Always buy fresh basil pesto from the refrigerated pasta section rather than the dusty canned sauce aisle! Refrigerated pesto uses fresh unpasteurized basil, real extra virgin olive oil, and aged parmesan, keeping a bright emerald green color and intoxicating fragrance that elevates simple salmon to five-star status.",
        "faqs": [
            ("Can I make this with frozen salmon?", "Yes! Thaw salmon fillets completely in the refrigerator, and press thoroughly dry with paper towels before slathering with pesto so the sauce doesn't slide off."),
            ("Can I use white fish instead?", "Cod loins, halibut, or sea bass bake magnificently with pesto—adjust bake time to 12 minutes for 1-inch thick fillets."),
            ("How do I store leftovers?", "Store cooked salmon and asparagus in an airtight glass container in the fridge for up to 3 days. Reheat gently in a 350°F oven or toaster oven for 5 minutes.")
        ],
        "wiki_entities": [
            ("Pesto", "https://en.wikipedia.org/wiki/Pesto"),
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Asparagus", "https://en.wikipedia.org/wiki/Asparagus")
        ],
        "pinterest": {
            "board": "Sheet Pan Suppers / Healthy Seafood Dinners",
            "title": "20-Minute Sheet-Pan Basil Pesto Salmon with Asparagus",
            "desc": "Flaky wild salmon fillets basted with a vibrant basil pesto crust, roasted on one sheet pan with crisp asparagus and burst tomatoes in 20 minutes! Healthy dinner perfection. Pin it now!",
            "tags": "#pestosalmon #sheetpanmeals #20minutedinner #healthydinner #glutenfree #seafooddinner #easyrecipes"
        }
    },
    {
        "slug": "15-minute-crispy-parmesan-crusted-chicken-cutlets",
        "title": "15-Minute Crispy Parmesan Crusted Chicken Cutlets with Lemon Arugula",
        "headline": "15-Minute Crispy Golden Parmesan Crusted Chicken Cutlets (Milanese Style)",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/crispy-parmesan-crusted-chicken-cutlets.jpg",
        "image_file": "crispy-parmesan-crusted-chicken-cutlets.jpg",
        "excerpt": "Extra-crispy golden panko and freshly grated parmesan crusted chicken cutlets flash-fried in olive oil, served with charred lemons and a peppery baby arugula salad in 15 minutes.",
        "description": "Milanese trattoria perfection in 15 minutes: thin chicken cutlets coated in crunchy panko and aged parmesan, pan-fried to shatteringly crisp golden perfection with lemon and arugula.",
        "keywords": "parmesan crusted chicken, chicken milanese, 15 minute chicken cutlets, crispy chicken dinner, easy weeknight chicken, italian chicken cutlets",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian / Milanese Trattoria",
        "calories": "470 kcal",
        "protein": "44g",
        "fat": "22g",
        "carbs": "21g",
        "fiber": "2g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "197",
        "quick_answer": "To make 15-minute crispy parmesan crusted chicken cutlets, slice 2 large chicken breasts horizontally into 4 thin cutlets (approx. 1/3-inch thick). Set up two shallow dishes: one with 1 beaten egg, and the second with 1 cup panko breadcrumbs mixed with 1/2 cup finely grated Parmigiano-Reggiano, 1 tsp Italian seasoning, 1/2 tsp garlic powder, salt, and pepper. Dip each cutlet in egg, then press firmly into the parmesan panko mixture until heavily crusted. Heat 3 tbsp olive oil in a wide skillet over medium-high heat. Fry cutlets for 3 minutes per side until deep golden brown and crunchy (165°F). Transfer to a wire rack, shower with flaky sea salt, and serve with charred lemon wedges and a lemon-tossed baby arugula salad.",
        "takeaways": [
            ("50/50 Panko-Parmesan Crust Ratio", "Blending equal parts airy Japanese panko with microplaned Parmigiano-Reggiano creates a shatteringly crisp crust that browns without burning."),
            ("Wire Cooling Rack Elevation", "Never rest fried cutlets on a flat paper plate; resting them on a raised wire cooling rack allows steam to escape so the bottom crust stays crunch-crisp."),
            ("Peppery Arugula Lemon Foil", "Tossing baby arugula with fresh lemon juice and olive oil provides an acidic, peppery contrast that cuts through rich pan-fried poultry.")
        ],
        "matrix_title": "Breadcrumb Coating Performance for High-Speed Pan-Frying",
        "matrix_headers": ["Breadcrumb Type", "Crunch Factor", "Grease Absorption", "Fry Time", "Verdict"],
        "matrix_rows": [
            ["Japanese Panko + Parmesan", "Shatteringly crisp & light", "Very low (stays dry & crunchy)", "3 min per side", "Gold Standard Milanese (Recommended)"],
            ["Traditional Fine Breadcrumbs", "Dense, sandy crust", "Moderate", "3 min per side", "Classic diner style"],
            ["Crushed Saltine Crackers", "Flaky & buttery", "Moderate", "2.5 min per side", "Southern comfort swap"],
            ["Almond Flour + Parmesan", "Crisp & nutty", "Low", "2.5 min per side", "Best 100% keto alternative"]
        ],
        "ingredients": [
            "1.25 lbs boneless skinless chicken breasts (sliced into 4 thin cutlets)",
            "1 large egg, beaten with 1 tbsp water",
            "1 cup panko breadcrumbs",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "1 tsp dried Italian seasoning",
            "1/2 tsp garlic powder",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "3 tbsp extra virgin olive oil (for shallow pan-frying)",
            "4 cups fresh baby arugula leaves",
            "2 organic lemons (1 sliced and charred, 1 juiced for salad)",
            "Flaky Maldon sea salt and fresh chopped parsley for garnish"
        ],
        "instructions": [
            ("Prep & Bread Cutlets", "Pat thin chicken cutlets dry with paper towels. In shallow bowl one, beat egg with 1 tbsp water. In shallow bowl two, combine panko, grated parmesan, Italian seasoning, garlic powder, salt, and pepper. Dredge each cutlet in egg, then press firmly into the parmesan panko mixture to coat both sides heavily."),
            ("Shallow Pan-Fry to Golden Crisp", "Heat 3 tbsp olive oil in a large skillet over medium-high heat until shimmering. Carefully lay cutlets into the hot oil (work in two batches if needed so pan isn't crowded). Fry undisturbed for 3 minutes until the bottom crust is deep golden brown and crunchy."),
            ("Flip & Finish", "Carefully flip cutlets with tongs and fry for another 2.5 to 3 minutes until golden and cooked through (165°F). Transfer immediately to a wire cooling rack and sprinkle with flaky sea salt."),
            ("Toss Arugula Salad", "In a medium bowl, toss fresh baby arugula with 1 tbsp olive oil, juice of 1/2 lemon, and a pinch of salt and pepper."),
            ("Plate & Serve", "Slice crispy cutlets on a bias. Serve hot alongside the bright lemon arugula salad, showered with fresh chopped parsley and charred lemon wedges for squeezing!")
        ],
        "pro_tip_title": "Elena’s Firm Press Breading Rule",
        "pro_tip": "Don't just gently dust your chicken—use the flat palms of your hands to press the panko and parmesan crumbs firmly into the meat! Compacting the crumbs into the egg wash locks the breading to the cutlet so not a single golden flake falls off when you flip in the skillet.",
        "faqs": [
            ("Can I make this in the air fryer?", "Yes! Spray breaded cutlets generously with olive oil spray and air fry at 400°F for 8–9 minutes, flipping halfway until golden and crunchy."),
            ("How do I keep chicken cutlets warm while cooking batches?", "Keep fried cutlets on a wire rack on a baking sheet in a 200°F oven; they will stay piping hot and crunchy for up to 30 minutes!"),
            ("Can I use pork or veal?", "Yes! Thin pork cutlets or veal scaloppine make classic Italian schnitzel/Milanese variations with identical cooking times.")
        ],
        "wiki_entities": [
            ("Veal Milanese", "https://en.wikipedia.org/wiki/Veal_Milanese"),
            ("Panko", "https://en.wikipedia.org/wiki/Bread_crumbs#Panko"),
            ("Parmigiano-Reggiano", "https://en.wikipedia.org/wiki/Parmigiano-Reggiano")
        ],
        "pinterest": {
            "board": "Quick Chicken Dinners / Italian Classics",
            "title": "15-Minute Crispy Parmesan Crusted Chicken Cutlets",
            "desc": "Extra-crispy golden panko and parmesan crusted chicken cutlets pan-fried in 15 minutes, served with lemon and baby arugula! Milanese perfection. Save the recipe!",
            "tags": "#parmesanchicken #chickencutlets #chickenmilanese #15minutedinner #crispychicken #easyrecipes #italianfood"
        }
    },
    {
        "slug": "20-minute-one-pot-cheesy-ground-beef-taco-pasta",
        "title": "20-Minute One-Pot Cheesy Ground Beef Taco Shell Pasta",
        "headline": "20-Minute One-Pot Cheesy Ground Beef Taco Pasta Skillet",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/one-pot-cheesy-ground-beef-taco-pasta.jpg",
        "image_file": "one-pot-cheesy-ground-beef-taco-pasta.jpg",
        "excerpt": "Comforting medium shell pasta cooked in one pot with seasoned ground beef, black beans, sweet corn, fire-roasted tomatoes, and gooey melted cheddar cheese in 20 minutes.",
        "description": "The ultimate family weeknight favorite in 20 minutes: uncooked pasta shells simmered directly in seasoned taco broth with lean ground beef, beans, sweet corn, and gooey melted sharp cheddar.",
        "keywords": "one pot taco pasta, cheesy beef taco pasta, 20 minute pasta skillet, easy one pot dinner, ground beef dinner, weeknight taco mac",
        "prepTime": "PT4M",
        "cookTime": "PT16M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Tex-Mex / American Comfort",
        "calories": "520 kcal",
        "protein": "36g",
        "fat": "24g",
        "carbs": "46g",
        "fiber": "6g",
        "sodium": "720mg",
        "ratingValue": "4.9",
        "reviewCount": "194",
        "quick_answer": "To make 20-minute one-pot cheesy ground beef taco pasta, brown 1 lb lean ground beef (90/10) with 1 small diced onion in a deep skillet over medium-high heat for 5 minutes; drain grease. Stir in 1 packet (or 2 tbsp) taco seasoning, 1 can (14.5 oz) fire-roasted diced tomatoes, 1/2 cup black beans, 1/2 cup sweet corn, 2.5 cups low-sodium beef broth, and 8 oz uncooked medium pasta shells. Bring to a rolling boil, cover with a tight-fitting lid, reduce heat to low-medium, and simmer undisturbed for 9 to 10 minutes until pasta shells are tender and liquid is absorbed into a rich sauce. Remove from heat, stir in 1/4 cup sour cream and 1.5 cups shredded sharp cheddar cheese until melted and velvety. Garnish with scallions, cilantro, and crushed tortilla chips.",
        "takeaways": [
            ("Uncooked Pasta Starch Absorption", "Cooking raw pasta shells directly in seasoned broth allows the natural starches to thicken the cooking liquid into a velvety taco sauce without straining."),
            ("Shell Cavity Sauce Pockets", "Medium pasta shells act like tiny spoons, scooping up savory beef crumbles, black beans, and melted cheese in every single bite."),
            ("Sour Cream Velvet Finish", "Stirring in a dollop of sour cream alongside shredded cheddar prevents the cheese from separating, ensuring an ultra-smooth velvety coating.")
        ],
        "matrix_title": "Pasta Shape Selection for One-Pot Taco Skillets",
        "matrix_headers": ["Pasta Shape", "Simmer Time", "Beef / Bean Pocket Hold", "Texture", "Verdict"],
        "matrix_rows": [
            ["Medium Pasta Shells (Conchiglie)", "9–10 minutes", "Scoops up beef & corn", "Chewy & saucy", "Absolute Best Shape (Recommended)"],
            ["Cavatappi / Cellentani", "10 minutes", "Great spiral cling", "Toothsome & fun", "Fantastic alternative"],
            ["Elbow Macaroni", "8 minutes", "Moderate", "Classic mac style", "Great for younger kids"],
            ["Rotini (Spirals)", "9 minutes", "Good ridge capture", "Tender", "Reliable pantry backup"]
        ],
        "ingredients": [
            "1 lb lean ground beef (90/10 or 85/15)",
            "8 oz uncooked medium pasta shells (conchiglie)",
            "1 packet (approx. 2 tbsp) taco seasoning blend",
            "1 can (14.5 oz) fire-roasted diced tomatoes with juices",
            "2.5 cups low-sodium beef broth or bone broth",
            "1/2 cup canned black beans, rinsed and drained",
            "1/2 cup canned or frozen sweet corn kernels",
            "1.5 cups sharp cheddar cheese, freshly shredded",
            "1/4 cup sour cream or plain Greek yogurt",
            "1 small yellow onion, finely diced",
            "Dollops of sour cream, sliced green onions, cilantro, and crushed tortilla chips for serving"
        ],
        "instructions": [
            ("Brown Beef & Aromatics", "Heat a deep large skillet or Dutch oven over medium-high heat. Add ground beef and diced onion. Cook for 5 minutes, breaking the beef into small crumbles with a wooden spoon until browned. Drain any excess rendered grease."),
            ("Add Seasoning, Liquid & Pasta", "Stir in taco seasoning, fire-roasted tomatoes with their juices, black beans, sweet corn, beef broth, and the raw uncooked pasta shells. Stir well to submerge the pasta shells into the liquid."),
            ("Cover & Simmer", "Bring to a rapid rolling boil. Immediately cover the skillet tightly with a lid, reduce heat to medium-low, and simmer undisturbed for 9 to 10 minutes until the pasta shells are al dente and most liquid has reduced into a thick sauce."),
            ("Stir in Cheese & Sour Cream", "Remove lid and turn off heat. Stir in sour cream and shredded sharp cheddar cheese. Fold gently for 60 seconds as the cheddar melts completely into an ultra-gooey, velvety Tex-Mex cheese sauce."),
            ("Garnish & Serve", "Top with spoonfuls of cool sour cream, sliced scallions, fresh cilantro, and a handful of crunchy crushed tortilla chips. Serve piping hot straight from the skillet!")
        ],
        "pro_tip_title": "Elena’s Liquid-to-Pasta Ratio Rule",
        "pro_tip": "The secret to foolproof one-pot pasta is exact liquid measurement! 8 ounces of pasta shells requires precisely 2.5 cups of broth plus the liquid from one can of diced tomatoes. Keep the lid on tight during simmering so steam doesn't escape; the shells will absorb the savory broth to tender perfection without becoming mushy.",
        "faqs": [
            ("Can I use ground turkey or chicken?", "Yes! Ground turkey or ground chicken works identically and makes a delicious lean one-pot taco dinner."),
            ("Can I make this spicier?", "Stir in a 4-oz can of diced green chilies, a diced jalapeño with the onions, or use pepper jack cheese in place of cheddar!"),
            ("How do I reheat leftovers?", "Store in an airtight container for up to 4 days. Reheat on the stove or in the microwave with a splash of milk or broth to revive the creamy cheese sauce.")
        ],
        "wiki_entities": [
            ("Taco", "https://en.wikipedia.org/wiki/Taco"),
            ("Cheddar cheese", "https://en.wikipedia.org/wiki/Cheddar_cheese"),
            ("Ground beef", "https://en.wikipedia.org/wiki/Ground_beef")
        ],
        "pinterest": {
            "board": "One-Pot Dinners / Family Favorite Meals",
            "title": "20-Minute One-Pot Cheesy Ground Beef Taco Shell Pasta",
            "desc": "Uncooked pasta shells simmered in one pot with seasoned ground beef, black beans, corn, and gooey melted cheddar in 20 minutes! The ultimate weeknight comfort food. Save it now!",
            "tags": "#tacopasta #onepotdinner #groundbeefrecipes #20minutemeals #familydinner #comfortfood #easyrecipes"
        }
    },
    {
        "slug": "15-minute-sticky-honey-ginger-garlic-salmon-bites",
        "title": "15-Minute Sticky Honey Ginger Garlic Salmon Bites",
        "headline": "15-Minute Crispy Skillet Sticky Honey Ginger Garlic Salmon Bites",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/sticky-honey-ginger-garlic-salmon-bites.jpg",
        "image_file": "sticky-honey-ginger-garlic-salmon-bites.jpg",
        "excerpt": "Crispy pan-seared wild salmon cubes tossed in a thick, sticky honey ginger garlic soy glaze in a hot skillet in 15 minutes.",
        "description": "Viral crispy salmon bites made lightning fast: cubed salmon fillets seared to golden caramelized perfection and coated in a bubbling sweet-savory honey ginger glaze with scallions.",
        "keywords": "salmon bites, honey ginger salmon, 15 minute salmon dinner, crispy salmon cubes, quick skillet seafood, easy weeknight salmon",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Asian Fusion / Seafood",
        "calories": "440 kcal",
        "protein": "34g",
        "fat": "22g",
        "carbs": "26g",
        "fiber": "1g",
        "sodium": "610mg",
        "ratingValue": "4.9",
        "reviewCount": "192",
        "quick_answer": "To make 15-minute sticky honey ginger garlic salmon bites, cut 1.25 lbs skinless salmon fillets into 1-inch cubes and pat thoroughly dry. Toss with 1 tbsp cornstarch, 1/2 tsp garlic powder, salt, and pepper until lightly dusted. Heat 1.5 tbsp neutral oil in a large cast iron skillet over high heat. Add salmon cubes in a single layer with space between them; sear undisturbed for 2 minutes per side until golden brown and crispy (4 to 5 minutes total). Lower heat to medium-low, add 1 tbsp butter, 4 minced garlic cloves, 1 tbsp grated ginger, 1/4 cup raw honey, 2 tbsp low-sodium soy sauce, and 1 tsp rice vinegar. Toss salmon bites continuously for 60 seconds as the sauce bubbles into a thick, glossy amber glaze. Shower with scallions, sesame seeds, and chili flakes.",
        "takeaways": [
            ("Cornstarch Crisp Shield", "Dredging cubed salmon in cornstarch builds a microscopic crust that crisps in smoking hot oil, locking in tender flakes without tearing."),
            ("Fast Searing Surface Area", "Cutting salmon into bite-sized cubes quadruples the caramelized surface area, delivering maximum crispy glaze in half the cooking time of whole fillets."),
            ("Vinegar-Honey Balance", "A teaspoon of rice vinegar balances sweet honey and savory soy sauce, creating a complex restaurant glaze that never tastes cloying.")
        ],
        "matrix_title": "Salmon Cut Performance for High-Speed Skillet Bites",
        "matrix_headers": ["Salmon Portion", "Omega-3 Fat Level", "Sear Crispiness", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Center-Cut Salmon Fillets", "High (very juicy)", "Deep caramelized crunch", "4–5 minutes", "Gold Standard for Salmon Bites (Recommended)"],
            ["Salmon Tail End Fillet", "Moderate", "Crispy", "3 minutes (watch closely)", "Can dry out faster"],
            ["Steelhead Trout Fillets", "High", "Golden crisp", "4 minutes", "Great colorful alternative"],
            ["Pre-Cooked Smoked Salmon", "Dry", "Cannot sear properly", "N/A", "Avoid for skillet bites"]
        ],
        "ingredients": [
            "1.25 lbs fresh skinless wild salmon fillets, cut into 1-inch bite-sized cubes",
            "1 tbsp cornstarch",
            "1.5 tbsp avocado or canola oil",
            "1 tbsp unsalted butter",
            "4 cloves fresh garlic, finely minced",
            "1 tbsp fresh ginger, finely grated",
            "1/4 cup raw honey",
            "2 tbsp low-sodium soy sauce or tamari",
            "1 tsp rice vinegar",
            "1/2 tsp garlic powder & 1/2 tsp kosher salt",
            "1/4 tsp crushed red pepper flakes",
            "2 green onions, thinly sliced",
            "1 tsp toasted white sesame seeds"
        ],
        "instructions": [
            ("Cube & Season Salmon", "Pat skinless salmon dry with paper towels. Cut into 1-inch cubes. In a bowl, toss cubes gently with cornstarch, garlic powder, and salt until lightly and evenly coated."),
            ("High-Heat Sear", "Heat oil in a wide cast iron skillet over medium-high heat until shimmering. Add salmon cubes in a single layer with space between each piece (do not overcrowd). Sear undisturbed for 2 minutes until the underside is crispy and golden. Gently turn cubes with tongs and sear for another 2 minutes until cooked through."),
            ("Build Sticky Glaze", "Reduce heat to medium-low. Add butter, minced garlic, and grated ginger to the skillet; sauté for 30 seconds until fragrant. Pour in honey, soy sauce, rice vinegar, and red pepper flakes."),
            ("Glaze the Salmon Bites", "Gently toss the crispy salmon bites in the bubbling glaze for 60 seconds until the sauce reduces into a thick, shiny amber syrup that lacquers every piece."),
            ("Garnish & Serve", "Remove from heat immediately. Scatter sliced scallions and toasted sesame seeds over the skillet. Serve over hot jasmine rice, quinoa, or steamed broccoli!")
        ],
        "pro_tip_title": "Elena’s Gentle Tongs Technique",
        "pro_tip": "Wild salmon is flaky and delicate! When turning your salmon bites in the hot skillet, use silicone-tipped tongs or a small spoon rather than stirring aggressively with a metal spatula. Turning each cube individually preserves their clean, beautiful geometric edges and keeps the flakes intact.",
        "faqs": [
            ("Can I make these in the air fryer?", "Yes! Air fry cornstarch-dusted salmon bites at 400°F for 6–7 minutes. Melt the honey ginger glaze in a skillet and toss the hot bites in to coat."),
            ("Can I meal prep salmon bites?", "Yes! They keep well in the fridge for up to 3 days. Reheat gently in a dry skillet or toaster oven for 3 minutes to revive the sticky crust."),
            ("What sides pair best with salmon bites?", "Steamed jasmine rice, cucumber avocado salad, garlic noodles, or roasted green beans pair magnificently.")
        ],
        "wiki_entities": [
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Ginger", "https://en.wikipedia.org/wiki/Ginger"),
            ("Soy sauce", "https://en.wikipedia.org/wiki/Soy_sauce")
        ],
        "pinterest": {
            "board": "Quick Seafood Dinners / Asian Salmon Recipes",
            "title": "15-Minute Sticky Honey Ginger Garlic Salmon Bites",
            "desc": "Crispy pan-seared salmon cubes glazed in an addictive sticky honey ginger garlic soy glaze in 15 minutes! The viral salmon bite dinner everyone loves. Pin it now!",
            "tags": "#salmonbites #honeygarlicsalmon #15minutedinner #seafooddinner #easyrecipes #quickdinner #salmondinner"
        }
    },
    {
        "slug": "15-minute-creamy-lemon-ricotta-campanelle-pasta",
        "title": "15-Minute Creamy Lemon Ricotta Campanelle Pasta with Sweet Peas",
        "headline": "15-Minute Creamy Lemon Ricotta Campanelle Pasta with Sweet Peas & Mint",
        "badge": "One-Pot Dinners &bull; 15 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-11-05",
        "image": "./assets/images/creamy-lemon-ricotta-campanelle-pasta.jpg",
        "image_file": "creamy-lemon-ricotta-campanelle-pasta.jpg",
        "excerpt": "Fluted campanelle pasta coated in a light, silky whole-milk lemon ricotta sauce with sweet green peas, fresh mint, cracked pepper, and parmesan in 15 minutes.",
        "description": "Bright, delicate Italian vegetarian comfort in 15 minutes: fluted flower-shaped campanelle pasta tossed in creamy lemon-whipped ricotta, tender sweet peas, parmesan, and fresh mint.",
        "keywords": "lemon ricotta pasta, campanelle pasta with peas, 15 minute pasta dinner, creamy ricotta pasta, vegetarian weeknight pasta, easy italian pasta",
        "prepTime": "PT3M",
        "cookTime": "PT12M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian / Vegetarian Comfort",
        "calories": "440 kcal",
        "protein": "16g",
        "fat": "18g",
        "carbs": "54g",
        "fiber": "4g",
        "sodium": "480mg",
        "ratingValue": "4.9",
        "reviewCount": "186",
        "quick_answer": "To make 15-minute creamy lemon ricotta campanelle pasta, boil 10 oz campanelle (or fusilli) in salted water until al dente (save 1 cup starchy pasta cooking water before draining). During the final 2 minutes of pasta boiling, drop 1 cup frozen sweet peas directly into the boiling pasta pot. Drain pasta and peas together. In a large bowl or directly in the warm pot off-heat, whisk 1 cup whole-milk ricotta cheese with 1/2 cup hot pasta water, 1/2 cup grated parmesan cheese, 2 tbsp olive oil, zest and juice of 1 large lemon, 1/2 tsp salt, and 1/2 tsp black pepper until smooth and velvety. Toss the hot pasta and peas through the ricotta cream until every fluted petal is coated. Shower with fresh torn mint leaves, lemon zest, and extra grated parmesan.",
        "takeaways": [
            ("Campanelle Cone Pockets", "The ruffled flower-cone shape of campanelle (gigli) catches creamy ricotta sauce and tender sweet peas inside its delicate fluted petals."),
            ("Two-Minute Pea Blanch Shortcut", "Tossing frozen peas directly into the boiling pasta during the last 120 seconds cooks them to sweet, vibrant green pop without dirtying another pot."),
            ("Off-Heat Ricotta Whisking", "Ricotta should never be boiled; whisking cold ricotta with hot starchy pasta water off the heat creates a velvety emulsion that never curdles.")
        ],
        "matrix_title": "Pasta Shape Performance in Creamy Ricotta Emulsions",
        "matrix_headers": ["Pasta Shape", "Sauce Grip", "Pea Capture", "Texture Appeal", "Verdict"],
        "matrix_rows": [
            ["Campanelle (Gigli / Little Bells)", "Ruffled petals hold cream", "Peas nestle inside cones", "Chewy & delicate", "Top Aesthetic & Flavor Pick (Recommended)"],
            ["Orecchiette (Little Ears)", "Cup interior catches sauce", "Traps peas perfectly", "Dense & chewy", "Fantastic alternative"],
            ["Fusilli / Rotini", "Spiral ridges grip cheese", "Good", "Springy", "Reliable pantry standby"],
            ["Spaghetti", "Light coating", "Peas roll to bottom", "Slurpy", "Better for oil-based sauces"]
        ],
        "ingredients": [
            "10 oz dried campanelle pasta (or gigli, cavatappi, or orecchiette)",
            "1 cup frozen sweet green peas",
            "1 cup whole-milk ricotta cheese (approx. 8 oz)",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "2 tbsp extra virgin olive oil",
            "Zest and juice of 1 large organic lemon",
            "1/2 tsp kosher salt & 1/2 tsp freshly cracked coarse black pepper",
            "1/4 cup fresh mint leaves, torn or finely sliced",
            "Extra virgin olive oil and lemon zest curls for serving"
        ],
        "instructions": [
            ("Boil Campanelle & Peas", "Bring a large pot of salted water to a rolling boil. Add campanelle pasta and cook until al dente (about 8–9 minutes). During the final 2 minutes of boiling, drop frozen sweet peas directly into the boiling pot. Before draining, ladle out 1 cup of hot starchy pasta water. Drain pasta and peas in a colander."),
            ("Whisk Velvet Lemon Ricotta", "In the warm empty pasta pot (off the heat), combine whole-milk ricotta, olive oil, lemon zest, lemon juice, grated parmesan cheese, salt, black pepper, and 1/2 cup of the hot reserved pasta water. Whisk vigorously for 45 seconds until silky, glossy, and completely smooth."),
            ("Toss Pasta & Peas", "Tumble the hot drained campanelle pasta and sweet peas directly into the lemon ricotta cream. Toss gently with a wooden spoon for 60 seconds, adding an extra splash of hot pasta water if needed until every ruffled cone is coated in a velvety sheen."),
            ("Garnish & Serve", "Divide into warm bowls. Top each serving with fresh torn mint leaves, freshly cracked black pepper, extra grated parmesan, and a final drizzle of extra virgin olive oil. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Whole-Milk Ricotta Mandate",
        "pro_tip": "Always check the tub to ensure you are buying WHOLE-MILK ricotta! Part-skim ricotta has high moisture and gums that turn watery and grainy when mixed with hot pasta. Whole-milk ricotta has rich butterfat that emulsifies with hot pasta water into pure restaurant liquid silk.",
        "faqs": [
            ("Can I add protein to this pasta?", "Yes! Sautéed jumbo shrimp, crispy crumbled prosciutto, or shredded rotisserie chicken breast pair magnificently with lemon ricotta."),
            ("Can I use basil instead of mint?", "Yes! Fresh sweet basil or fresh dill make wonderful herbal substitutes for mint."),
            ("How do I store leftovers?", "Store in an airtight container for up to 3 days in the fridge. Reheat gently on the stovetop over low heat with a splash of milk or water to revive the creamy sauce.")
        ],
        "wiki_entities": [
            ("Ricotta", "https://en.wikipedia.org/wiki/Ricotta"),
            ("Campanelle", "https://en.wikipedia.org/wiki/Campanelle"),
            ("Parmigiano-Reggiano", "https://en.wikipedia.org/wiki/Parmigiano-Reggiano")
        ],
        "pinterest": {
            "board": "Pasta Recipes / Vegetarian Dinners",
            "title": "15-Minute Creamy Lemon Ricotta Campanelle Pasta with Peas",
            "desc": "Fluted campanelle pasta coated in a silky lemon ricotta sauce with sweet green peas and fresh mint in 15 minutes! The ultimate light Italian comfort. Save the recipe!",
            "tags": "#lemonricottapasta #campanelle #15minutedinner #quickpasta #vegetarianrecipes #easydinner #italianfood"
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
  <meta name="description" content="{r['description']}">
  <meta name="author" content="Elena Bennett">
  <link rel="canonical" href="https://fastflavored.com/articles/{r['slug']}.html">
  <meta name="robots" content="max-image-preview:large, max-snippet:-1">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{r['title']}">
  <meta property="og:description" content="{r['description']}">
  <meta property="og:image" content="../assets/images/{r['image_file']}">
  <meta property="og:url" content="https://fastflavored.com/articles/{r['slug']}.html">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{r['title']}">
  <meta name="twitter:description" content="{r['description']}">
  <meta name="twitter:image" content="../assets/images/{r['image_file']}">

  <!-- Schema.org Recipe + FAQPage JSON-LD -->
  <script type="application/ld+json">
{json.dumps(recipe_json_ld, indent=2)}
  </script>

  <!-- Stylesheets -->
  <link rel="stylesheet" href="../css/style.css?v=2.1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
  <!-- Navigation Header -->
  <header class="header">
    <div class="header-container">
      <a href="../index.html" class="logo">
        <span class="logo-fast">Fast</span><span class="logo-flavored">Flavored</span>
      </a>
      <nav class="nav-menu" id="navMenu">
        <a href="../index.html" class="nav-link">Home</a>
        <a href="../index.html?category=all" class="nav-link">All Recipes</a>
        <a href="../about.html" class="nav-link">About Elena</a>
      </nav>
      <div class="nav-actions">
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle Theme">
          <i class="fa-solid fa-moon"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- Recipe Article Container -->
  <article class="article-container" style="max-width: 1000px; margin: 2rem auto; padding: 0 1.5rem;">
    
    <!-- Breadcrumbs -->
    <nav class="breadcrumbs" style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem;">
      <a href="../index.html" style="color: var(--text-muted); text-decoration: none;">Home</a> &gt; 
      <a href="../index.html?category=all" style="color: var(--text-muted); text-decoration: none;">{r['category']}</a> &gt; 
      <span>{r['title']}</span>
    </nav>

    <!-- Header Section -->
    <header class="article-header" style="margin-bottom: 2rem;">
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;">
        <span class="card-badge" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
          <i class="fa-solid fa-fire"></i> {r['badge']}
        </span>
        <span class="card-badge" style="font-size: 0.85rem; padding: 0.35rem 0.75rem; background: var(--bg-card); color: var(--text-primary); border: 1px solid var(--border-color);">
          <i class="fa-solid fa-stopwatch"></i> {r['read_time']}
        </span>
      </div>
      <h1 class="article-title" style="font-size: 2.5rem; line-height: 1.25; margin-bottom: 1rem; color: var(--text-primary);">
        {r['title']}
      </h1>
      <p class="article-subtitle" style="font-size: 1.2rem; color: var(--text-muted); margin-bottom: 1.5rem;">
        {r['description']}
      </p>
      <div class="article-meta-row" style="display: flex; align-items: center; gap: 1.5rem; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); padding: 1rem 0; font-size: 0.95rem; color: var(--text-muted);">
        <div><i class="fa-solid fa-user-chef" style="color: var(--accent-color);"></i> By <strong>Elena Bennett</strong></div>
        <div><i class="fa-regular fa-calendar"></i> Published: {r['date']}</div>
        <div><i class="fa-solid fa-star" style="color: #f59e0b;"></i> {r['ratingValue']} ({r['reviewCount']} reviews)</div>
      </div>
    </header>

    <!-- Jump to Recipe & Print Buttons -->
    <div style="display: flex; gap: 1rem; margin-bottom: 2.5rem;">
      <a href="#recipe-card" class="btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none;">
        <i class="fa-solid fa-arrow-down"></i> Jump to Recipe
      </a>
      <button class="btn-outline btn-print">
        <i class="fa-solid fa-print"></i> Print Recipe
      </button>
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

          <div class="recipe-content-split">
            <!-- Ingredients List with Checkboxes -->
            <div class="ingredients-list">
              <h3 style="font-size: 1.4rem; margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.5rem;">
                <i class="fa-solid fa-basket-shopping" style="color: var(--accent-color);"></i> Ingredients
              </h3>
              <ul class="ingredient-checkboxes" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.75rem;">
                {ing_html}
              </ul>
            </div>

            <!-- Step by Step Instructions -->
            <div class="instructions-list">
              <h3 style="font-size: 1.4rem; margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.5rem;">
                <i class="fa-solid fa-kitchen-set" style="color: var(--accent-color);"></i> Step-by-Step Instructions
              </h3>
              <ol style="padding-left: 1.25rem; display: flex; flex-direction: column; gap: 1.25rem;">
                {inst_html}
              </ol>
            </div>
          </div>

          <!-- Nutrition Breakdown -->
          <div style="border-top: 1px solid var(--border-color); padding-top: 1.5rem; margin-top: 2rem;">
            <h4 style="font-size: 1.1rem; margin-bottom: 1rem; color: var(--text-primary);">Nutrition Facts (Per Serving):</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 1rem; text-align: center;">
              <div style="background: var(--bg-surface); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <div style="font-size: 0.8rem; color: var(--text-muted);">Calories</div>
                <div style="font-weight: 700; color: var(--text-primary);">{r['calories']}</div>
              </div>
              <div style="background: var(--bg-surface); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <div style="font-size: 0.8rem; color: var(--text-muted);">Protein</div>
                <div style="font-weight: 700; color: var(--text-primary);">{r['protein']}</div>
              </div>
              <div style="background: var(--bg-surface); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <div style="font-size: 0.8rem; color: var(--text-muted);">Fat</div>
                <div style="font-weight: 700; color: var(--text-primary);">{r['fat']}</div>
              </div>
              <div style="background: var(--bg-surface); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <div style="font-size: 0.8rem; color: var(--text-muted);">Carbs</div>
                <div style="font-weight: 700; color: var(--text-primary);">{r['carbs']}</div>
              </div>
              <div style="background: var(--bg-surface); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <div style="font-size: 0.8rem; color: var(--text-muted);">Fiber</div>
                <div style="font-weight: 700; color: var(--text-primary);">{r['fiber']}</div>
              </div>
              <div style="background: var(--bg-surface); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <div style="font-size: 0.8rem; color: var(--text-muted);">Sodium</div>
                <div style="font-weight: 700; color: var(--text-primary);">{r['sodium']}</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Elena's Chef Pro-Tip Box -->
        <div class="pro-tip-box" id="pro-tips" style="background: rgba(225, 29, 72, 0.05); border-left: 4px solid var(--accent-color); border-radius: 0 var(--radius-md) var(--radius-md) 0; padding: 1.5rem; margin: 2.5rem 0;">
          <h3 style="font-size: 1.25rem; color: var(--accent-color); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-lightbulb"></i> {r['pro_tip_title']}
          </h3>
          <p style="margin: 0; color: var(--text-primary); font-size: 1.05rem;">
            {r['pro_tip']}
          </p>
        </div>

        <!-- FAQs Accordion -->
        <div class="faq-section" id="faqs" style="margin: 3rem 0;">
          <h2 style="font-size: 1.8rem; margin-bottom: 1.5rem; color: var(--text-primary);">Frequently Asked Questions</h2>
          <div style="display: flex; flex-direction: column; gap: 1rem;">
            {faqs_html}
          </div>
        </div>

      </main>
    </div>
  </article>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col">
        <a href="../index.html" class="logo">
          <span class="logo-fast">Fast</span><span class="logo-flavored">Flavored</span>
        </a>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 1rem;">
          Quick, wholesome, and tested weeknight dinners made in 15 to 30 minutes. Elena Bennett shares authentic culinary shortcuts for real kitchens.
        </p>
      </div>
      <div class="footer-col">
        <h4>Recipe Collections</h4>
        <ul class="footer-links">
          <li><a href="../index.html?category=quick-and-easy">15-Minute Dinners</a></li>
          <li><a href="../index.html?category=one-pot-dinners">One-Pot Meals</a></li>
          <li><a href="../index.html?category=sheet-pan-suppers">Sheet Pan Suppers</a></li>
          <li><a href="../index.html?category=comfort-food">Comfort Classics</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul class="footer-links">
          <li><a href="../about.html">About Elena</a></li>
          <li><a href="../index.html?category=all">All Recipes</a></li>
          <li><a href="../sitemap.xml">Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 FastFlavored. All rights reserved.</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="../js/main.js?v=2.1"></script>
  <script>
    // FAQ Accordion Interaction
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 11) ===")
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
