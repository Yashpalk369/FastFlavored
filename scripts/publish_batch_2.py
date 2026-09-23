import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "15-minute-creamy-tortellini-prosciutto-peas",
        "title": "15-Minute Creamy Garlic Butter Tortellini with Crispy Prosciutto and Peas",
        "headline": "15-Minute Creamy Tortellini with Crispy Prosciutto and Sweet Peas",
        "badge": "15-Minute Meals &bull; Italian Comfort",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-23",
        "image": "./assets/images/creamy-tortellini-prosciutto-peas.jpg",
        "image_file": "creamy-tortellini-prosciutto-peas.jpg",
        "excerpt": "Pillowy three-cheese tortellini tossed in a velvety garlic parmesan cream with shattered crispy frizzled prosciutto, sweet tender green peas, and cracked black pepper in 15 minutes.",
        "description": "Tender refrigerated cheese tortellini smothered in a luscious garlic parmesan cream sauce, crowned with crackling pan-frizzled prosciutto, sweet green peas, and shaved Parmigiano-Reggiano.",
        "keywords": "creamy tortellini, tortellini with peas and prosciutto, 15 minute pasta dinner, one pot tortellini, quick weeknight dinner, easy creamy pasta",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Northern Italian",
        "calories": "560 kcal",
        "protein": "22g",
        "fat": "28g",
        "carbs": "54g",
        "fiber": "5g",
        "sodium": "780mg",
        "ratingValue": "4.9",
        "reviewCount": "144",
        "quick_answer": "To make 15-minute creamy tortellini with crispy prosciutto and peas, boil 16 oz refrigerated cheese tortellini for 3 minutes, reserving 1/2 cup pasta water. In a large skillet with 1 tbsp butter, fry 4 oz chopped prosciutto over medium-high heat until deeply crisp (3 mins); transfer to a plate. In the same skillet, melt 2 tbsp butter with 3 minced garlic cloves, stir in 3/4 cup heavy cream, 1/2 cup chicken broth, and 1 cup frozen sweet peas. Simmer 2 minutes, toss in drained tortellini and 1/2 cup grated parmesan, and crown with the crispy prosciutto.",
        "takeaways": [
            ("Frizzled Prosciutto Fat Base", "Rendering prosciutto in the skillet first leaves behind savory, salty cured pork fat that flavors the entire cream sauce."),
            ("Refrigerated Pasta Speed", "Refrigerated cheese tortellini cook tender in just 180 seconds, keeping total prep and cook under 15 minutes."),
            ("Sweet Pea Acid-Fat Balance", "Bright, pop-in-your-mouth sweet green peas slice through rich heavy cream and aged Parmigiano-Reggiano.")
        ],
        "matrix_title": "Cured Meat Comparison for Creamy Tortellini",
        "matrix_headers": ["Cured Meat", "Crisp Factor", "Salt Level", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Prosciutto di Parma", "Delicate, shatter-crisp lace", "Refined & sweet-savory", "3 minutes", "Gold Standard Perfection (Recommended)"],
            ["Pancetta (Cubed)", "Meaty, chewy crunch", "Medium-High", "5–6 minutes", "Hearty Italian classic substitute"],
            ["Applewood Smoked Bacon", "Smoky & heavy crunch", "High salt & smoke", "6–7 minutes", "Americanized comfort alternative"],
            ["Crispy Guanciale", "Melting rich fat, deep pork umami", "Intense", "5 minutes", "Exceptional for carbonara fans"]
        ],
        "ingredients": [
            "16 oz refrigerated three-cheese tortellini",
            "4 oz prosciutto (roughly chopped or torn into ribbons)",
            "1 cup frozen petite sweet peas (thawed)",
            "3 tbsp unsalted butter (divided)",
            "3 cloves garlic, finely minced",
            "3/4 cup heavy whipping cream",
            "1/2 cup low-sodium chicken or vegetable broth",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "1/2 cup reserved starchy pasta cooking water",
            "1/4 tsp ground nutmeg",
            "Freshly cracked black pepper and fresh flat-leaf parsley"
        ],
        "instructions": [
            ("Boil Tortellini", "Bring a large pot of salted water to a rolling boil. Drop in refrigerated tortellini and cook for 2–3 minutes until they float to the surface. Scoop out 1/2 cup starchy pasta water, then drain."),
            ("Frizzle Prosciutto", "While pasta cooks, melt 1 tbsp butter in a large 12-inch skillet over medium heat. Add chopped prosciutto and cook for 3–4 minutes until crackling and deep golden. Transfer prosciutto to a plate lined with a paper towel."),
            ("Build Garlic Cream Sauce", "In the same skillet with the rendered prosciutto drippings, melt remaining 2 tbsp butter over medium-low heat. Add minced garlic and cook for 45 seconds until fragrant. Pour in heavy cream, broth, and a pinch of ground nutmeg. Simmer gently for 2 minutes until bubbling."),
            ("Toss Tortellini & Peas", "Add thawed sweet peas and drained tortellini directly into the skillet. Toss gently for 1–2 minutes over low heat, adding splashes of pasta water until sauce clings in a glossy, velvety sheen."),
            ("Garnish & Serve", "Remove from heat. Fold in grated Parmigiano-Reggiano and freshly cracked black pepper. Top with the shattered crispy prosciutto and fresh parsley. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Whisper of Nutmeg Rule",
        "pro_tip": "Never skip the tiny pinch of ground nutmeg in garlic cream sauces! In classic Northern Italian cuisine, a whisper of nutmeg cuts the heavy lactic richness of dairy and complements the sweet green peas, transforming a standard cream sauce into a nuanced, five-star trattoria delicacy.",
        "faqs": [
            ("Can I use frozen or dried tortellini?", "Yes! Frozen tortellini take about 4–5 minutes to boil. Dried shelf-stable tortellini take 10–12 minutes; make sure to check package directions."),
            ("What can I substitute for heavy cream?", "You can use half-and-half whisked with 1 tsp cornstarch, or 1/2 cup mascarpone cheese melted with chicken broth for an authentic velvety texture."),
            ("Can I add mushrooms or spinach?", "Absolutely! Sauté 1 cup sliced cremini mushrooms with the garlic, or fold in 2 cups of fresh baby spinach during the final 60 seconds of simmering.")
        ],
        "wiki_entities": [
            ("Tortellini", "https://en.wikipedia.org/wiki/Tortellini"),
            ("Prosciutto", "https://en.wikipedia.org/wiki/Prosciutto"),
            ("Parmigiano Reggiano", "https://en.wikipedia.org/wiki/Parmigiano_Reggiano")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Pasta Recipes",
            "title": "15-Minute Creamy Tortellini with Crispy Prosciutto and Peas (One-Skillet Dinner!)",
            "desc": "Tender cheese tortellini coated in a rich garlic parmesan cream with sweet green peas and shattered crispy frizzled prosciutto. Ready in just 15 minutes! Save this viral weeknight dinner recipe now!",
            "tags": "#tortellini #15minutedinner #creamypasta #onepotmeals #easypastarecipe #weeknightdinner #prosciutto"
        }
    },
    {
        "slug": "20-minute-sheet-pan-parmesan-crusted-cod",
        "title": "20-Minute Sheet-Pan Crispy Parmesan Crusted Cod and Garlic Green Beans",
        "headline": "20-Minute Sheet-Pan Crispy Parmesan Crusted Cod (Zero-Mess Seafood)",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-23",
        "image": "./assets/images/sheet-pan-parmesan-crusted-cod.jpg",
        "image_file": "sheet-pan-parmesan-crusted-cod.jpg",
        "excerpt": "Flaky Pacific cod fillets topped with a golden garlic herb parmesan panko crust, roasted alongside tender charred green beans and caramelized lemon wheels in 20 minutes.",
        "description": "Succulent wild cod fillets crowned with a crunchy golden garlic parmesan and parsley panko crust, roasted on a single sheet pan with blistered green beans and sweet roasted lemon wheels.",
        "keywords": "parmesan crusted cod, sheet pan cod, baked cod recipe, 20 minute seafood dinner, healthy sheet pan meals, crispy white fish recipe",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mediterranean / American",
        "calories": "380 kcal",
        "protein": "36g",
        "fat": "14g",
        "carbs": "16g",
        "fiber": "4g",
        "sodium": "490mg",
        "ratingValue": "4.9",
        "reviewCount": "135",
        "quick_answer": "To make 20-minute sheet-pan parmesan crusted cod, toss 1 lb trimmed green beans and thin lemon slices on a rimmed baking sheet with 1 tbsp olive oil, salt, and pepper. Arrange 4 cod fillets in the center. In a small bowl, mix 1/2 cup panko, 1/2 cup grated parmesan, 2 tbsp melted butter, 2 minced garlic cloves, 1 tbsp chopped parsley, and lemon zest. Press the crunchy topping onto the cod. Roast at 425°F (220°C) for 12–14 minutes until cod flakes easily and the crust is deeply golden brown.",
        "takeaways": [
            ("Panko-Parmesan Crunch Shield", "Butter-infused panko breadcrumbs and parmesan form a golden protective crust that traps steam inside, ensuring flaky, ultra-moist fish."),
            ("High Heat Green Bean Char", "Roasting at 425°F blisters and sweetens green beans in the exact window the cod takes to cook through."),
            ("Caramelized Lemon Wheel Juice", "Roasting lemon wheels concentrates sugars and releases mellow citrus juices for squeezing over the hot crust.")
        ],
        "matrix_title": "Crust Binder Comparison for Baked White Fish",
        "matrix_headers": ["Binding Agent", "Crust Adhesion", "Richness Profile", "Moisture Retention", "Verdict"],
        "matrix_rows": [
            ["Melted Butter + Dijon", "Superior (sticks to fish tightly)", "Buttery & zesty tang", "Maximum (never dry)", "Gold Standard Winner (Recommended)"],
            ["Mayonnaise Base", "Excellent", "Rich & creamy", "High", "Keto-friendly classic alternative"],
            ["Olive Oil Drizzle", "Moderate (crumbs can scatter)", "Lighter Mediterranean taste", "Medium", "Great for dairy-free diets"],
            ["Egg Wash", "Traditional breading", "Firm coating", "Moderate", "Too heavy for delicate cod"]
        ],
        "ingredients": [
            "4 wild-caught Pacific or Atlantic cod fillets (6 oz each, 1-inch thick, pat dried)",
            "1 lb fresh green beans (trimmed)",
            "1/2 cup panko breadcrumbs",
            "1/2 cup finely grated Parmigiano-Reggiano",
            "3 tbsp unsalted butter, melted",
            "1 tbsp Dijon mustard (for brushing cod)",
            "2 tbsp extra virgin olive oil (for green beans)",
            "3 cloves garlic, finely minced",
            "Zest and juice of 1 large organic lemon (half sliced into thin wheels)",
            "2 tbsp fresh Italian flat-leaf parsley, finely chopped",
            "1/2 tsp smoked paprika & garlic powder",
            "Kosher salt & freshly ground black pepper"
        ],
        "instructions": [
            ("Preheat & Prep Sheet Pan", "Preheat oven to 425°F (220°C). Line a large heavy baking sheet with parchment paper or nonstick foil."),
            ("Season Vegetables", "Toss trimmed green beans and lemon wheels directly on the pan with 2 tbsp olive oil, 1/2 tsp salt, and 1/4 tsp pepper. Push them to the sides of the baking sheet, leaving the center clear."),
            ("Prep Cod & Dijon Base", "Pat cod fillets thoroughly dry with paper towels. Place them skin-side down in the center of the baking sheet. Brush the top of each fillet with a thin layer of Dijon mustard (this acts as the glue)."),
            ("Mix Parmesan Herb Crust", "In a medium bowl, combine panko, grated parmesan, melted butter, minced garlic, lemon zest, chopped parsley, smoked paprika, garlic powder, salt, and pepper. Stir until coarse, buttery crumbs form."),
            ("Crust & Bake", "Mound the parmesan topping generously onto each cod fillet, pressing down gently so it adheres. Roast at 425°F for 12–14 minutes, switching to high broil for the final 60 seconds until crust is deep golden brown and fish flakes with a fork (internal temp 140°F)."),
            ("Serve", "Squeeze caramelized roasted lemon juice over the crispy crust and green beans. Serve immediately while piping hot!")
        ],
        "pro_tip_title": "Elena’s Pat-Dry & Dijon Crust Glue",
        "pro_tip": "White fish like cod sheds moisture rapidly if not prepped correctly. Always press paper towels into the fillets for 30 seconds to absorb exterior water before brushing on a whisper-thin coat of Dijon mustard! The mustard provides zero sharp bite after baking, but its emulsifiers glue the buttery parmesan panko onto the fish so not a single golden crumb tumbles off.",
        "faqs": [
            ("Can I use frozen cod?", "Yes! Thaw frozen cod completely in the refrigerator overnight, then pat extremely dry with paper towels to prevent soggy crusts."),
            ("Can I use tilapia, halibut, or haddock?", "Any firm white fish works brilliantly! Halibut, haddock, seabass, or tilapia are fantastic drop-in substitutes."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 3 days. Reheat in the toaster oven or air fryer at 350°F for 4–5 minutes to re-crisp the panko coating.")
        ],
        "wiki_entities": [
            ("Cod as food", "https://en.wikipedia.org/wiki/Cod_as_food"),
            ("Panko", "https://en.wikipedia.org/wiki/Bread_crumbs#Panko"),
            ("Green bean", "https://en.wikipedia.org/wiki/Green_bean")
        ],
        "pinterest": {
            "board": "Sheet Pan Meals / Seafood Dinners",
            "title": "20-Minute Sheet-Pan Crispy Parmesan Crusted Cod Recipe (Zero Cleanup!)",
            "desc": "Tender flaky cod topped with a golden garlic herb parmesan panko crust, roasted on one sheet pan with blistered green beans and caramelized lemons. Ready in 20 minutes! Save this healthy weeknight recipe now!",
            "tags": "#parmesancod #sheetpanmeals #20minutedinner #healthyseafood #bakedfish #easyweeknightdinner #glutenfreeoptions"
        }
    },
    {
        "slug": "15-minute-sticky-mongolian-beef-noodles",
        "title": "15-Minute Sticky Mongolian Beef Noodles",
        "headline": "15-Minute Sticky Mongolian Beef Noodles (Better Than Takeout)",
        "badge": "15-Minute Meals &bull; Takeout Fast",
        "category": "Comfort Food",
        "categories_str": "all 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-23",
        "image": "./assets/images/sticky-mongolian-beef-noodles.jpg",
        "image_file": "sticky-mongolian-beef-noodles.jpg",
        "excerpt": "Thin tender ribbons of flank steak flash-seared and tossed with chewy ramen noodles, ginger, garlic, and fresh scallions in a glossy brown sugar soy glaze in 15 minutes.",
        "description": "Skip the delivery! Thinly sliced flank steak caramelized with fresh ginger and garlic, tossed with chewy noodles in a sweet, savory, and sticky Mongolian sauce loaded with fresh scallions.",
        "keywords": "mongolian beef noodles, beef and noodles stir fry, 15 minute beef dinner, easy weeknight noodles, takeout fakeout, sticky beef noodles",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Chinese-American",
        "calories": "520 kcal",
        "protein": "32g",
        "fat": "18g",
        "carbs": "60g",
        "fiber": "3g",
        "sodium": "790mg",
        "ratingValue": "4.9",
        "reviewCount": "182",
        "quick_answer": "To make 15-minute sticky Mongolian beef noodles, slice 1 lb flank steak thinly against the grain and toss with 1.5 tbsp cornstarch. Boil 8 oz ramen or lo mein noodles for 3 minutes and drain. In a small bowl, whisk 1/3 cup low-sodium soy sauce, 1/4 cup brown sugar, 1/3 cup beef broth, 1 tbsp hoisin sauce, and 1 tsp sesame oil. Sear beef in 2 tbsp hot oil for 2 minutes until caramelized; remove. Sauté 4 minced garlic cloves and 1 tbsp grated ginger for 30 seconds, pour in sauce to bubble and thicken, toss in noodles, beef, and 4 sliced scallions, and serve hot.",
        "takeaways": [
            ("Cornstarch Velveting Secret", "Dusting sliced steak in cornstarch creates an ultra-tender velvet texture while locking in juices during high-heat searing."),
            ("Ramen Noodle Chew", "Using instant ramen noodles (discarding flavor packets) boils in 180 seconds and absorbs sticky sweet soy sauce rapidly."),
            ("Caramelized Brown Sugar Glaze", "Simmering brown sugar with dark soy sauce produces the signature lacquer-like sheen that clings to every noodle.")
        ],
        "matrix_title": "Beef Cut Performance for 15-Minute Stir-Fries",
        "matrix_headers": ["Beef Cut", "Tenderness Level", "Sear Caramelization", "Cost Profile", "Verdict"],
        "matrix_rows": [
            ["Flank Steak", "Very tender (when cut across grain)", "Deep, savory char", "Moderate", "Gold Standard Winner (Recommended)"],
            ["Sirloin Steak", "Naturally tender & juicy", "Excellent sear", "Moderate-High", "Fabulous quick alternative"],
            ["Skirt Steak", "Robust beefy chew", "High caramelization", "Moderate", "Great flavor, must slice thin"],
            ["Chuck Roast Strips", "Tough without braising", "Moderate", "Low", "Not recommended for 15-minute stir-fry"]
        ],
        "ingredients": [
            "1 lb flank steak (or top sirloin), thinly sliced against the grain",
            "8 oz ramen noodles, lo mein noodles, or fresh udon (flavor packets discarded)",
            "1.5 tbsp cornstarch",
            "1/3 cup low-sodium soy sauce",
            "1/4 cup packed dark brown sugar",
            "1/3 cup low-sodium beef broth",
            "1 tbsp hoisin sauce",
            "1 tsp toasted sesame oil",
            "4 cloves garlic, finely minced",
            "1 tbsp fresh ginger, finely grated",
            "2 tbsp high-smoke oil (avocado or peanut oil)",
            "4 large scallions (green onions), cut into 2-inch batons",
            "1 tbsp toasted white and black sesame seeds",
            "1/4 tsp crushed red pepper flakes (optional heat)"
        ],
        "instructions": [
            ("Velvet Beef & Prep Sauce", "Toss thinly sliced flank steak in a bowl with 1.5 tbsp cornstarch until evenly coated. In a measuring cup, whisk together soy sauce, brown sugar, beef broth, hoisin sauce, and sesame oil."),
            ("Boil Noodles", "Cook ramen or lo mein noodles in a pot of boiling water for 2–3 minutes until just tender. Drain and rinse briefly under cold water to halt cooking."),
            ("Sear Beef in Screaming Skillet", "Heat 2 tbsp oil in a large wok or 12-inch heavy skillet over high heat until smoking. Add steak slices in a single layer. Sear undisturbed for 90 seconds until a deep caramelized crust forms, flip and cook 1 more minute. Transfer beef to a plate."),
            ("Bubble & Thicken Sauce", "Reduce heat to medium. Add minced garlic and grated ginger to the pan; stir-fry for 30 seconds until fragrant. Pour in the prepared sauce mixture. Bring to a vigorous simmer for 1–2 minutes until thick and glossy."),
            ("Toss & Glaze", "Toss cooked noodles, seared steak with resting juices, and scallions into the pan. Toss continuously over medium-high heat for 1 minute until sauce glazes every noodle. Top with sesame seeds and serve sizzling hot!")
        ],
        "pro_tip_title": "Elena’s 15-Minute Freezer Slice Hack",
        "pro_tip": "Getting paper-thin, restaurant-style beef strips at home is easy: pop your raw flank steak into the freezer for 15 minutes before cooking! The cold firms the meat up without freezing it solid, letting your chef's knife effortlessly shave gossamer-thin slices across the grain that melt in your mouth after a 90-second sear.",
        "faqs": [
            ("Can I make this with chicken or tofu?", "Yes! Thinly sliced chicken breast or pressed extra-firm cubed tofu dusted in cornstarch works identically well in this sticky Mongolian glaze."),
            ("Can I add veggies like broccoli or bell peppers?", "Absolutely! Sauté 1 cup of bite-sized broccoli florets or sliced red bell peppers in the skillet right before building the sauce."),
            ("What if I want it less sweet?", "Reduce the brown sugar to 2 tablespoons and add 1 tablespoon of extra beef broth or a splash of rice vinegar for a tangier balance.")
        ],
        "wiki_entities": [
            ("Mongolian beef", "https://en.wikipedia.org/wiki/Mongolian_beef"),
            ("Flank steak", "https://en.wikipedia.org/wiki/Flank_steak"),
            ("Ramen", "https://en.wikipedia.org/wiki/Ramen")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Asian Recipes",
            "title": "15-Minute Sticky Mongolian Beef Noodles Recipe (Better Than Delivery!)",
            "desc": "Tender caramelized flank steak strips and chewy noodles tossed in a sticky sweet-savory ginger garlic Mongolian glaze with fresh scallions. Ready in 15 minutes! Save this viral weeknight dinner now!",
            "tags": "#mongolianbeef #beefnoodles #15minutedinner #takeoutfakeout #asianrecipes #easyweeknightdinner #noodletok"
        }
    },
    {
        "slug": "15-minute-crispy-firecracker-shrimp",
        "title": "15-Minute Crispy Firecracker Shrimp Skillet",
        "headline": "15-Minute Crispy Firecracker Shrimp (Sweet, Spicy & Sizzling)",
        "badge": "15-Minute Meals &bull; Sweet & Spicy",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-23",
        "image": "./assets/images/crispy-firecracker-shrimp.jpg",
        "image_file": "crispy-firecracker-shrimp.jpg",
        "excerpt": "Jumbo shrimp pan-seared to juicy perfection and tossed in a bubbling sweet-and-spicy sriracha honey garlic firecracker glaze with fresh scallions in 15 minutes.",
        "description": "Succulent pan-seared jumbo shrimp glazed in a vibrant ruby-red firecracker sauce of sriracha, honey, soy, and garlic, garnished with scallions and sesame seeds.",
        "keywords": "firecracker shrimp, spicy honey shrimp, 15 minute shrimp dinner, easy skillet shrimp, sweet and spicy shrimp, quick seafood recipes",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Asian-American",
        "calories": "320 kcal",
        "protein": "29g",
        "fat": "9g",
        "carbs": "26g",
        "fiber": "1g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "160",
        "quick_answer": "To make 15-minute crispy firecracker shrimp, pat 1.5 lbs peeled jumbo shrimp dry and toss with 1 tbsp cornstarch, salt, and pepper. Whisk 1/3 cup sriracha, 1/4 cup honey, 2 tbsp low-sodium soy sauce, 1 tbsp apple cider vinegar, and 4 minced garlic cloves. Heat 2 tbsp oil in a large cast-iron skillet over medium-high heat. Sear shrimp for 2 minutes per side until pink and curled; remove. Pour firecracker sauce into the skillet, simmer for 1–2 minutes until bubbling and sticky, toss shrimp back in to glaze, and top with scallions and sesame seeds.",
        "takeaways": [
            ("Cornstarch Crisp Shield", "A light dusting of cornstarch absorbs surface moisture and creates a micro-crisp shell that locks in shrimp juices."),
            ("The Sweet Heat Equilibrium", "Combining sharp sriracha heat with floral honey and cider vinegar creates an addictive sweet-tangy flavor explosion."),
            ("Two-Minute Fast Sear", "Jumbo shrimp require only 120 seconds per side; removing them before reducing the glaze guarantees plump, never-rubbery seafood.")
        ],
        "matrix_title": "Firecracker Sauce Sweetener Comparison",
        "matrix_headers": ["Sweetener Base", "Glaze Viscosity", "Flavor Nuance", "Burn Resistance", "Verdict"],
        "matrix_rows": [
            ["Raw Clover Honey", "Thick, mirror-glossy cling", "Floral & rich", "High (melts smooth)", "Gold Standard Winner (Recommended)"],
            ["Pure Maple Syrup", "Slightly thinner glaze", "Woodsy & caramel notes", "Medium", "Delicious earthy alternative"],
            ["Dark Brown Sugar", "Deep molasses lacquer", "Caramelized sweetness", "Medium-High", "Classic restaurant takeout style"],
            ["Agave Nectar", "Medium viscosity", "Neutral clean sweet", "High", "Great low-glycemic option"]
        ],
        "ingredients": [
            "1.5 lbs raw jumbo shrimp (16/20 count, peeled, deveined, tails on)",
            "1 tbsp cornstarch",
            "1/3 cup sriracha chili sauce",
            "1/4 cup pure honey",
            "2 tbsp low-sodium soy sauce",
            "1 tbsp apple cider vinegar or rice vinegar",
            "4 cloves garlic, finely minced",
            "1 tbsp unsalted butter",
            "2 tbsp neutral cooking oil (avocado or vegetable oil)",
            "3 scallions (green onions), thinly sliced",
            "1 tsp toasted sesame seeds",
            "1/4 tsp crushed red pepper flakes",
            "Kosher salt & freshly ground black pepper"
        ],
        "instructions": [
            ("Dry & Dust Shrimp", "Thoroughly pat peeled shrimp dry with paper towels. Place in a bowl and toss with cornstarch, 1/2 tsp salt, and 1/4 tsp black pepper until lightly coated."),
            ("Whisk Firecracker Sauce", "In a glass bowl, whisk together sriracha, honey, soy sauce, apple cider vinegar, and minced garlic until smooth and emulsified."),
            ("Sear Jumbo Shrimp", "Heat neutral oil in a large 12-inch skillet over medium-high heat until shimmering. Add shrimp in a single layer without crowding. Sear for 2 minutes on the first side until golden pink, flip and sear 1 minute on the other side. Transfer shrimp to a clean plate."),
            ("Simmer & Gloss Glaze", "Lower heat to medium. Melt butter in the skillet, then pour in the firecracker sauce mixture. Bring to a lively boil for 1–2 minutes, stirring constantly until bubbly, thick, and reduced to a syrup consistency."),
            ("Glaze & Garnish", "Return the seared shrimp and resting juices to the skillet. Toss vigorously for 30 seconds until every shrimp is enrobed in glistening spicy glaze. Garnish with scallions and sesame seeds. Serve hot over jasmine rice!")
        ],
        "pro_tip_title": "Elena’s Shrimp Temperature Safeguard",
        "pro_tip": "The biggest home cook mistake with shrimp is cooking them in the sauce! High heat boils shrimp into rubbery tires. Always flash-sear your shrimp first in hot oil, transfer them to a plate while they are still slightly undercooked, reduce the glaze until thick, and only then toss them back in for 30 seconds off the heat. Your shrimp will be impossibly tender and plump.",
        "faqs": [
            ("How spicy is firecracker shrimp?", "It has a medium-high spicy kick with noticeable sweetness. To dial the heat down, use 1/4 cup sriracha and add 2 tbsp extra honey or sweet chili sauce."),
            ("Can I make this with chicken or salmon bites?", "Yes! 1-inch chicken breast cubes or cubed salmon fillets cooked in this firecracker glaze are absolute dynamite!"),
            ("Can I make this ahead for meal prep?", "Yes! Store the glazed shrimp and rice in separate containers for up to 3 days. Reheat gently in the microwave or skillet with a tablespoon of water.")
        ],
        "wiki_entities": [
            ("Shrimp as food", "https://en.wikipedia.org/wiki/Shrimp_as_food"),
            ("Sriracha", "https://en.wikipedia.org/wiki/Sriracha"),
            ("Honey", "https://en.wikipedia.org/wiki/Honey")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Seafood Recipes",
            "title": "15-Minute Crispy Firecracker Shrimp Recipe (Sweet & Spicy Skillet!)",
            "desc": "Plump juicy jumbo shrimp pan-seared and coated in a bubbling sweet, spicy sriracha honey garlic glaze with scallions and sesame seeds. Ready in 15 minutes! Save this easy weeknight dinner recipe now!",
            "tags": "#firecrackershrimp #15minutedinner #spicyshrimp #shrimprecipes #easyseafood #weeknightdinners #quickmeals"
        }
    },
    {
        "slug": "20-minute-creamy-chicken-piccata",
        "title": "20-Minute Creamy Lemon Basil Chicken Piccata",
        "headline": "20-Minute Creamy Lemon Basil Chicken Piccata (Velvety Skillet Feast)",
        "badge": "30-Minute Meals &bull; Italian Classic",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "20 min cook",
        "date": "2026-09-23",
        "image": "./assets/images/creamy-chicken-piccata.jpg",
        "image_file": "creamy-chicken-piccata.jpg",
        "excerpt": "Golden flour-dusted chicken cutlets pan-seared and simmered in a silky lemon butter white wine cream sauce with briny capers, fresh basil, and parsley in 20 minutes.",
        "description": "A luxurious modern twist on the classic trattoria favorite: tender golden chicken cutlets bathed in a velvety lemon garlic cream sauce studded with salty capers and fragrant fresh basil.",
        "keywords": "creamy chicken piccata, lemon chicken piccata, 20 minute chicken dinner, easy skillet chicken, italian chicken cutlets, creamy lemon sauce",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American",
        "calories": "470 kcal",
        "protein": "38g",
        "fat": "24g",
        "carbs": "14g",
        "fiber": "2g",
        "sodium": "610mg",
        "ratingValue": "4.9",
        "reviewCount": "172",
        "quick_answer": "To make 20-minute creamy lemon chicken piccata, slice 1.5 lbs chicken breasts into thin cutlets and dredge lightly in seasoned flour. Sear in 2 tbsp olive oil and 1 tbsp butter over medium-high heat for 3 minutes per side until golden; transfer to a plate. In the same skillet, sauté 3 minced garlic cloves for 30 seconds. Deglaze with 1/3 cup dry white wine (or chicken broth) and 1/3 cup lemon juice, scraping up browned bits. Pour in 1/2 cup heavy cream, 1/2 cup chicken broth, and 3 tbsp drained capers. Simmer 3 minutes, return chicken to skillet to warm through, and finish with fresh parsley and lemon slices.",
        "takeaways": [
            ("Flour Dredge Fond Builder", "Lightly dusting chicken cutlets in flour creates a crispy golden crust while leaving starch in the pan to thicken the wine-cream sauce."),
            ("Acid-Deglaze Foundation", "Deglazing with crisp dry Pinot Grigio and fresh lemon juice dissolves caramelized chicken fond into an intensely savory base."),
            ("Briny Caper Pops", "Salty, vinegar-cured capers pierce through rich butter and heavy cream, maintaining high flavor contrast in every mouthful.")
        ],
        "matrix_title": "Pan Deglazing Liquid Comparison for Piccata",
        "matrix_headers": ["Deglazing Liquid", "Acidity Level", "Sauce Depth", "Alcohol", "Verdict"],
        "matrix_rows": [
            ["Dry White Wine (Pinot Grigio/Sauvignon Blanc)", "High & crisp", "Complex, floral & rich", "Cooks off 95%", "Gold Standard Trattoria Choice (Recommended)"],
            ["Rich Chicken Bone Broth + Extra Lemon", "Bright & citrusy", "Savory & comforting", "None (0%)", "Best non-alcoholic substitute"],
            ["Dry White Vermouth", "Medium-High", "Herbal & aromatic", "Cooks off", "Sophisticated gourmet alternative"],
            ["Apple Cider Vinegar + Broth", "Sharp & tangy", "Fruity undertone", "None (0%)", "Use sparingly (1 tbsp only)"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken breasts (halved horizontally into 4 thin cutlets)",
            "1/3 cup all-purpose flour (for dredging)",
            "3 tbsp unsalted butter (divided)",
            "2 tbsp extra virgin olive oil",
            "4 cloves garlic, finely minced",
            "1/3 cup dry white wine (Pinot Grigio, Sauvignon Blanc) or chicken broth",
            "1/3 cup freshly squeezed lemon juice (about 2 lemons)",
            "1/2 cup low-sodium chicken broth",
            "1/2 cup heavy cream",
            "3 tbsp non-pareil capers (rinsed and drained)",
            "1 organic lemon, sliced into paper-thin wheels",
            "1/4 cup fresh flat-leaf Italian parsley, finely chopped",
            "Kosher salt & freshly ground black pepper"
        ],
        "instructions": [
            ("Pound & Dredge Chicken", "Pat chicken cutlets dry. Season both sides with 1 tsp kosher salt and 1/2 tsp black pepper. Dredge cutlets in flour, shaking off excess so only a sheer dusting remains."),
            ("Pan-Sear Until Golden", "Heat olive oil and 1 tbsp butter in a 12-inch heavy skillet over medium-high heat. Add cutlets and sear for 3–4 minutes per side until deeply golden and cooked to 165°F. Transfer chicken to a warm plate."),
            ("Deglaze the Skillet", "Lower heat to medium. Add minced garlic to the skillet drippings; sauté for 30 seconds. Pour in white wine and fresh lemon juice, scraping up all golden browned bits (fond) from the pan bottom. Simmer for 2 minutes until liquid reduces by half."),
            ("Simmer Cream & Capers", "Pour in chicken broth, heavy cream, and capers. Whisk continuously over medium-low heat for 2–3 minutes until a silky, velvety sauce forms and coats the back of a spoon."),
            ("Return Chicken & Serve", "Slide cooked chicken cutlets and lemon wheels back into the pan. Spoon the warm lemon cream sauce over the cutlets for 1 minute until warmed through. Garnish with fresh chopped parsley and serve with angel hair pasta or warm crusty bread!")
        ],
        "pro_tip_title": "Elena’s Wine Reduction Temperature Rule",
        "pro_tip": "Always reduce your white wine and lemon juice by half BEFORE pouring in the heavy cream! Boiling heavy cream in high-acid wine can cause the dairy proteins to separate or curdle. Reducing the wine first concentrates the aromatics, mellows harsh raw alcohol, and ensures the cream melds into a mirror-smooth restaurant emulsion.",
        "faqs": [
            ("What can I use instead of white wine?", "Substitute equal parts low-sodium chicken broth with 1 extra tablespoon of fresh lemon juice. The sauce will still be wonderfully flavorful!"),
            ("Can I make this gluten-free?", "Yes! Simply use 1-to-1 gluten-free baking flour or cornstarch to dredge the chicken cutlets."),
            ("What are the best side dishes for chicken piccata?", "Buttery garlic angel hair pasta, creamy mashed potatoes, or roasted asparagus are traditional and divine companions.")
        ],
        "wiki_entities": [
            ("Piccata", "https://en.wikipedia.org/wiki/Piccata"),
            ("Caper", "https://en.wikipedia.org/wiki/Caper"),
            ("Chicken as food", "https://en.wikipedia.org/wiki/Chicken_as_food")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Chicken Recipes",
            "title": "20-Minute Creamy Lemon Basil Chicken Piccata Recipe (Trattoria Style!)",
            "desc": "Golden pan-seared chicken cutlets simmered in a velvety lemon butter white wine cream sauce with briny capers and fresh parsley. Ready in 20 minutes in one skillet! Save this easy weeknight dinner recipe now!",
            "tags": "#chickenpiccata #20minutedinner #creamychicken #italianrecipes #skilletchicken #easyweeknightdinner #dinnerideas"
        }
    },
    {
        "slug": "20-minute-mexican-street-corn-chicken",
        "title": "20-Minute One-Pan Mexican Street Corn (Elote) Chicken Skillet",
        "headline": "20-Minute Mexican Street Corn Chicken Skillet (Sizzling Elote Feast)",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "20 min cook",
        "date": "2026-09-23",
        "image": "./assets/images/mexican-street-corn-chicken.jpg",
        "image_file": "mexican-street-corn-chicken.jpg",
        "excerpt": "Juicy spice-rubbed chicken cutlets topped with blistered charred sweet corn, creamy spiced cotija lime crema, smoky chili powder, and fresh cilantro in 20 minutes.",
        "description": "All the flavors of beloved Mexican street corn (Elote) piled high on juicy seared chicken breasts: charred sweet corn, tangy lime crema, salty cotija cheese, and fresh cilantro in one skillet.",
        "keywords": "street corn chicken, elote chicken skillet, 20 minute mexican dinner, one pan chicken dinner, easy weeknight meals, low carb mexican recipes",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mexican-American",
        "calories": "430 kcal",
        "protein": "37g",
        "fat": "19g",
        "carbs": "22g",
        "fiber": "3g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "168",
        "quick_answer": "To make 20-minute Mexican street corn chicken, season 1.5 lbs chicken cutlets with chili powder, cumin, smoked paprika, garlic powder, and salt. Sear in 2 tbsp oil in a cast-iron skillet over medium-high heat for 3–4 minutes per side until golden and 165°F; remove. In the same hot skillet with 1 tbsp butter, char 2 cups sweet corn kernels undisturbed for 4 minutes until blistered and smoky. Whisk 1/3 cup sour cream, 2 tbsp mayonnaise, juice of 1 lime, and a pinch of chili powder. Spoon charred corn over seared chicken, drizzle with lime crema, and top with crumbled cotija and fresh cilantro.",
        "takeaways": [
            ("High-Heat Dry Corn Char", "Allowing corn kernels to sit undisturbed in a smoking cast-iron skillet develops authentic caramelized dark blisters and nutty sweet depth."),
            ("Cotija & Lime Crema Dynamic", "Salty, crumbly Mexican cotija cheese combined with bright citrus lime crema provides the signature street-cart elote flavor balance."),
            ("Single Cast-Iron Skillet", "Searing chicken and blistering corn in the same pan captures all caramelized chicken juices in the corn topping.")
        ],
        "matrix_title": "Corn Variety Comparison for Weeknight Elote",
        "matrix_headers": ["Corn Option", "Char Potential", "Sweetness Level", "Prep Time", "Verdict"],
        "matrix_rows": [
            ["Frozen Fire-Roasted Sweet Corn", "Exceptional (already pre-charred)", "High & smoky", "0 minutes prep", "Ultimate Weeknight Shortcut (Recommended)"],
            ["Fresh Sweet Corn on Cob", "Superior crisp pop", "Peak natural sweetness", "5 minutes (shucking & cutting)", "Gold Standard in summer season"],
            ["Standard Canned Sweet Corn", "Moderate (must drain thoroughly)", "Medium sweetness", "1 minute (draining)", "Good budget pantry backup"],
            ["Creamed Corn", "None (too liquid)", "Artificial sweetness", "0 minutes", "Strictly avoid for Elote"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken breasts (cut into 4 thin cutlets)",
            "2 cups sweet corn kernels (fresh, frozen thawed, or fire-roasted)",
            "1 tsp chili powder",
            "1 tsp ground cumin",
            "1 tsp smoked paprika",
            "1 tsp garlic powder",
            "1/2 cup crumbled authentic Mexican cotija cheese (or queso fresco)",
            "1/3 cup Mexican crema or sour cream",
            "2 tbsp real mayonnaise",
            "Zest and juice of 2 fresh limes",
            "2 tbsp avocado or vegetable oil",
            "1 tbsp unsalted butter",
            "1/3 cup fresh cilantro leaves, finely chopped",
            "Kosher salt & freshly ground black pepper"
        ],
        "instructions": [
            ("Season Chicken Cutlets", "In a small bowl, combine chili powder, cumin, smoked paprika, garlic powder, 1 tsp salt, and 1/2 tsp black pepper. Rub spice blend evenly over all sides of the chicken cutlets."),
            ("Sear Chicken Golden", "Heat 2 tbsp oil in a large 12-inch cast-iron skillet over medium-high heat until shimmering. Add seasoned chicken cutlets and sear for 3–4 minutes per side until deep golden brown and cooked to 165°F. Transfer chicken to a warm serving platter."),
            ("Char Sweet Corn", "In the same hot skillet, melt 1 tbsp butter. Add sweet corn kernels and spread in an even layer. Let cook completely undisturbed for 3–4 minutes over high heat until kernels develop dark golden blisters and pop. Stir once and char 1 more minute."),
            ("Whisk Tangy Lime Crema", "In a small bowl, whisk together sour cream (or Mexican crema), mayonnaise, lime juice, lime zest, and a pinch of salt until smooth and drizzly."),
            ("Assemble & Serve", "Spoon the sizzling blistered charred corn generously over the seared chicken cutlets. Drizzle with tangy lime crema, sprinkle heavily with crumbled cotija cheese, dusting of chili powder, and fresh chopped cilantro. Serve immediately with extra lime wedges!")
        ],
        "pro_tip_title": "Elena’s Cast-Iron Corn Char Hack",
        "pro_tip": "Resist the urge to stir the corn! To get that authentic smoky Mexican street cart flavor, your sweet corn kernels need direct, uninterrupted contact with the screaming-hot cast-iron surface for a full 3 to 4 minutes. You will hear them snap, crackle, and pop as natural sugars caramelize into gorgeous deep mahogany blisters.",
        "faqs": [
            ("What can I substitute if I can't find cotija cheese?", "Crumbled Greek feta cheese is an exceptional substitute! It has the same dry, crumbly texture and salty, briny flavor profile as authentic cotija."),
            ("Can I make this with chicken thighs?", "Yes! Boneless skinless chicken thighs take about 5–6 minutes per side and deliver extra juicy tenderness."),
            ("What should I serve with street corn chicken?", "Serve alongside warm corn tortillas, cilantro lime rice, black beans, or over a bed of crisp chopped romaine for a spectacular high-protein salad.")
        ],
        "wiki_entities": [
            ("Elote", "https://en.wikipedia.org/wiki/Elote"),
            ("Cotija cheese", "https://en.wikipedia.org/wiki/Cotija_cheese"),
            ("Chicken as food", "https://en.wikipedia.org/wiki/Chicken_as_food")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Mexican Recipes",
            "title": "20-Minute Mexican Street Corn Chicken Skillet Recipe (One-Pan Elote!)",
            "desc": "Juicy spice-seared chicken cutlets topped with smoky blistered charred sweet corn, creamy lime crema, salty cotija cheese, and fresh cilantro in 20 minutes! Save this viral weeknight dinner now!",
            "tags": "#streetcornchicken #elotechicken #onepansupper #20minutedinner #mexicanrecipes #easyweeknightdinner #castironskillet"
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 2) ===")
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
