import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "15-minute-honey-harissa-chicken-bowls",
        "title": "15-Minute Sweet and Spicy Honey Harissa Chicken Bowls",
        "headline": "15-Minute Sweet and Spicy Honey Harissa Chicken Bowls with Couscous",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/honey-harissa-chicken-bowls.jpg",
        "image_file": "honey-harissa-chicken-bowls.jpg",
        "excerpt": "Juicy seared chicken thighs basted in a fiery sweet honey harissa glaze, served over fluffy couscous with crisp cucumbers, pickled onions, salty feta, and garlic tahini yogurt in 15 minutes.",
        "description": "Vibrant North African street flavors in 15 minutes: tender chicken thighs glazed in spicy rose harissa, honey, and lemon over steaming couscous with fresh herbs and cool garlic yogurt sauce.",
        "keywords": "honey harissa chicken, harissa chicken bowls, 15 minute chicken dinner, mediterranean grain bowls, spicy honey chicken",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "North African / Mediterranean",
        "calories": "490 kcal",
        "protein": "37g",
        "fat": "19g",
        "carbs": "43g",
        "fiber": "4g",
        "sodium": "620mg",
        "ratingValue": "4.9",
        "reviewCount": "182",
        "quick_answer": "To make 15-minute sweet and spicy honey harissa chicken bowls, cut 1.25 lbs boneless skinless chicken thighs into bite-sized strips and season with salt, cumin, and coriander. Whisk 2.5 tbsp North African harissa paste with 2 tbsp honey, 1 tbsp olive oil, and juice of 1/2 lemon. Heat 1 tbsp oil in a skillet over high heat; sear chicken undisturbed for 3 minutes per side until caramelized and cooked through (165°F). Lower heat to medium, pour in the honey harissa glaze, and toss for 60 seconds until chicken is lacquered. Meanwhile, pour 1 cup boiling salted broth over 1 cup dry couscous; cover for 5 minutes and fluff with a fork. Assemble bowls with couscous, spicy glazed chicken, diced Persian cucumbers, pickled red onions, crumbled feta cheese, and a drizzle of garlic lemon yogurt.",
        "takeaways": [
            ("Harissa Paste Bloom", "Tossing the sweet-spicy harissa glaze into the skillet during the final minute caramelizes the natural sugars and blooms the chili peppers without scorching."),
            ("5-Minute Steam Couscous", "Moroccan couscous requires no stovetop boiling—steeping in boiling water off-heat produces fluffy, delicate grains in the exact time it takes to sear chicken."),
            ("Cooling Yogurt-Tahini Balance", "A swirl of whole-milk Greek yogurt mixed with tahini and lemon provides a velvety, cooling fat barrier that balances the bold smoky heat of harissa.")
        ],
        "matrix_title": "Harissa Style Performance for High-Speed Glazes",
        "matrix_headers": ["Harissa Variety", "Spice Heat Level", "Flavor Notes", "Skillet Glaze Cling", "Verdict"],
        "matrix_rows": [
            ["Rose Harissa Paste", "Medium warmth", "Smoky chili with delicate floral sweetness", "Superior glossy coating", "Top Pick for Flavor Complexity (Recommended)"],
            ["Traditional Tunisian Harissa", "High heat & punchy", "Garlicky, smoky & intensely savory", "Excellent cling", "Great for serious spice lovers"],
            ["Dry Harissa Spice Blend", "Mild-Medium", "Toasted cumin & ground chili flakes", "Requires oil & honey emulsion", "Good pantry backup"],
            ["Sweet Pepper Harissa", "Very mild", "Red bell pepper forward", "Sweet finish", "Best for kid-friendly meals"]
        ],
        "ingredients": [
            "1.25 lbs boneless skinless chicken thighs, cut into 1-inch strips",
            "2.5 tbsp rose harissa paste (such as Mina or Belazu)",
            "2 tbsp raw clover honey",
            "2 tbsp extra virgin olive oil (divided)",
            "1 tsp ground cumin & 1/2 tsp ground coriander",
            "1/2 tsp kosher salt & 1/4 tsp cracked black pepper",
            "1 cup dry Moroccan couscous",
            "1 cup boiling chicken broth or water",
            "2 Persian cucumbers, diced",
            "1/3 cup pickled red onions",
            "1/2 cup crumbled Greek feta cheese",
            "1/2 cup plain Greek yogurt mixed with 1 tbsp lemon juice and 1 grated garlic clove",
            "Fresh mint and flat-leaf parsley for garnish"
        ],
        "instructions": [
            ("Fluff the Couscous", "Place 1 cup dry couscous in a heatproof bowl with 1/2 tsp salt and 1/2 tbsp olive oil. Pour 1 cup boiling chicken broth over the couscous, cover tightly with a plate, and let steam undisturbed for 5 minutes. Fluff with a fork."),
            ("Season Chicken", "Pat chicken thigh strips dry with paper towels. Toss in a bowl with cumin, coriander, salt, and black pepper."),
            ("High-Heat Sear", "Heat 1.5 tbsp olive oil in a wide heavy skillet over high heat. Add chicken strips in a single layer and sear undisturbed for 3 minutes until deep golden brown. Flip and sear for another 2.5 minutes until cooked through (165°F)."),
            ("Glaze in Honey Harissa", "Reduce heat to medium-low. In a small cup, stir harissa paste, honey, and lemon juice. Pour over the hot chicken in the skillet. Toss continuously for 60 to 90 seconds until a bubbling, sticky, fiery-red glaze coats every piece of chicken."),
            ("Assemble Bowls", "Divide fluffy couscous among 4 serving bowls. Top with generous scoops of the honey harissa chicken, diced cucumbers, pickled red onions, and crumbled feta. Drizzle with creamy garlic yogurt sauce and shower with torn fresh mint leaves!")
        ],
        "pro_tip_title": "Elena’s Sticky Glaze Heat Control",
        "pro_tip": "Honey burns quickly at high temperatures! Make sure to lower your stove burner to medium-low before pouring in the honey harissa mixture. You want the sauce to gently bubble and lacquer the seared chicken in 60 seconds rather than charring into bitterness.",
        "faqs": [
            ("What can I substitute for couscous?", "Quinoa, warm jasmine rice, farro, or cauliflower rice all make fantastic grain-bowl bases with this recipe."),
            ("Can I use chicken breasts instead of thighs?", "Yes! Boneless chicken breasts sliced into thin cutlets work well. Sear for 2.5 to 3 minutes per side to prevent drying out."),
            ("Is harissa extremely spicy?", "Most jarred harissa pastes offer rich smokiness and moderate warmth rather than pure fiery burn. If you prefer mild heat, use 1.5 tbsp harissa and increase honey to 2.5 tbsp.")
        ],
        "wiki_entities": [
            ("Harissa", "https://en.wikipedia.org/wiki/Harissa"),
            ("Couscous", "https://en.wikipedia.org/wiki/Couscous"),
            ("Feta", "https://en.wikipedia.org/wiki/Feta")
        ],
        "pinterest": {
            "board": "Mediterranean Recipes / Quick Chicken Dinners",
            "title": "15-Minute Sweet and Spicy Honey Harissa Chicken Bowls",
            "desc": "Caramelized seared chicken thighs basted in a sticky honey harissa glaze over fluffy couscous with feta, cucumbers, and garlic yogurt in 15 minutes! The ultimate weeknight flavor explosion. Pin it now!",
            "tags": "#harissachicken #mediterraneanfood #15minutedinner #chickenbowls #easyrecipes #grainbowl #quickdinner"
        }
    },
    {
        "slug": "20-minute-creamy-tuscan-garlic-salmon",
        "title": "20-Minute Creamy Garlic Parmesan Tuscan Salmon Skillet",
        "headline": "20-Minute Creamy Tuscan Garlic Butter Salmon Fillets with Sun-Dried Tomatoes",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/creamy-tuscan-garlic-salmon.jpg",
        "image_file": "creamy-tuscan-garlic-salmon.jpg",
        "excerpt": "Golden pan-seared salmon fillets simmering in a rich garlic parmesan cream sauce loaded with sun-dried tomatoes, wilted baby spinach, and fresh basil in 20 minutes.",
        "description": "Pan-seared crispy skin salmon fillets nestled into an Italian restaurant-worthy garlic parmesan cream sauce with chewy sun-dried tomatoes and fresh spinach in 20 minutes.",
        "keywords": "creamy tuscan salmon, garlic butter salmon, 20 minute salmon skillet, one pot salmon dinner, creamy salmon spinach, easy seafood dinner",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American / Seafood",
        "calories": "520 kcal",
        "protein": "38g",
        "fat": "36g",
        "carbs": "8g",
        "fiber": "2g",
        "sodium": "590mg",
        "ratingValue": "4.9",
        "reviewCount": "194",
        "quick_answer": "To make 20-minute creamy Tuscan garlic salmon, season 4 salmon fillets (6 oz each) with salt, black pepper, and Italian herbs. Heat 1 tbsp olive oil and 1 tbsp butter in a large cast iron skillet over medium-high heat. Sear salmon skin-side down for 4 minutes until crisp, flip, and cook for 3 minutes until medium-rare; transfer to a plate. Reduce heat to medium, add 1 tbsp butter and 4 minced garlic cloves with 1/2 cup chopped sun-dried tomatoes, and sauté for 1 minute. Pour in 1/2 cup low-sodium chicken broth, 3/4 cup heavy cream, and 1/2 cup grated parmesan cheese, simmering for 3 minutes until smooth and bubbly. Stir in 3 cups fresh baby spinach until wilted, return salmon to the skillet, and baste with the creamy sauce.",
        "takeaways": [
            ("Skin-Down Searing Crisp", "Starting skin-side down in hot butter renders the fatty layer beneath the salmon skin, creating an ultra-crisp barrier that protects the tender fish."),
            ("Sun-Dried Tomato Acidity", "Tangy sun-dried tomatoes cut through the luscious heavy cream and parmesan, providing vibrant Italian sweetness and umami."),
            ("Resting Fillet Reintegration", "Resting the salmon while building the sauce prevents overcooking; returning the fillets to the pan at the very end warms them through without drying out the flaky center.")
        ],
        "matrix_title": "Cooking Fat Selection for Pan-Searing Salmon",
        "matrix_headers": ["Cooking Fat", "Crispy Skin Potential", "Flavor Enhancement", "Smoke Tolerance", "Verdict"],
        "matrix_rows": [
            ["Olive Oil + Butter Blend", "Golden, shatteringly crisp", "Rich nutty browned butter notes", "High (oil raises smoke point)", "Best Balance for Restaurant Crust (Recommended)"],
            ["Pure Ghee (Clarified Butter)", "Extremely crisp", "Pure buttery richness", "Very high (485°F)", "Outstanding gourmet option"],
            ["Avocado Oil", "Good crisp", "Neutral", "Highest smoke point (520°F)", "Great for simple clean searing"],
            ["Unsalted Butter Alone", "Can burn before skin crisps", "Delicious but delicate", "Low (burns at 350°F)", "Add only after flipping"]
        ],
        "ingredients": [
            "4 center-cut salmon fillets (approx. 6 oz each, skin-on or skinless)",
            "1 tbsp extra virgin olive oil",
            "2 tbsp unsalted butter (divided)",
            "4 cloves fresh garlic, finely minced",
            "1/2 cup sun-dried tomatoes in oil, drained and sliced",
            "1/2 cup low-sodium chicken bone broth or dry white wine",
            "3/4 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "3 cups fresh baby spinach leaves",
            "1 tsp dried Italian herbs (oregano, basil, thyme)",
            "1/2 tsp kosher salt & 1/4 tsp cracked black pepper",
            "Fresh basil leaves and lemon wedges for serving"
        ],
        "instructions": [
            ("Season & Prep Salmon", "Thoroughly pat salmon fillets dry with paper towels. Season both sides with Italian herbs, kosher salt, and cracked black pepper."),
            ("Pan-Sear the Salmon", "Heat olive oil and 1 tbsp butter in a wide cast iron skillet over medium-high heat until shimmering. Add salmon fillets skin-side down. Sear undisturbed for 4 minutes until skin is crackly and golden. Flip gently and sear top side for 3 minutes. Transfer salmon to a warm plate (it will finish in sauce)."),
            ("Sauté Garlic & Tomatoes", "Reduce skillet heat to medium. Add remaining 1 tbsp butter, minced garlic, and sliced sun-dried tomatoes to the skillet drippings. Sauté for 60 seconds until fragrant."),
            ("Build Velvet Parmesan Cream", "Pour in chicken broth or white wine, scraping up the caramelized bits from the pan bottom. Pour in heavy cream and grated parmesan cheese. Whisk continuously for 2 to 3 minutes as sauce bubbles into a silky, emulsified cream."),
            ("Wilt Spinach & Finish", "Add fresh baby spinach to the bubbling sauce, stirring for 60 seconds until just wilted. Nestle the seared salmon fillets back into the skillet. Spoon the rich garlic cream over the fish for 1 minute until warmed through. Garnish with fresh basil and serve with lemon wedges!")
        ],
        "pro_tip_title": "Elena’s White Wine Deglazing Upgrade",
        "pro_tip": "If you keep dry white wine on hand (like Sauvignon Blanc or Pinot Grigio), swap out the chicken broth for 1/2 cup of wine! Deglazing the pan with white wine lifts every microscopic bit of caramelized salmon fond, infusing bright acidity that makes the cream sauce taste like an upscale Tuscan trattoria.",
        "faqs": [
            ("Can I use frozen salmon fillets?", "Yes! Thaw completely overnight in the refrigerator, and press firmly with paper towels to draw out all excess moisture before searing so the fish sears rather than steams."),
            ("What should I serve with Tuscan salmon?", "This creamy dish is heaven over angel hair pasta, potato gnocchi, garlic mashed potatoes, or alongside crusty warm sourdough bread for dipping."),
            ("Can I make this dairy-free?", "Yes! Substitute full-fat canned coconut milk for heavy cream and use nutritional yeast or vegan parmesan for a rich dairy-free alternative.")
        ],
        "wiki_entities": [
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Tuscan food", "https://en.wikipedia.org/wiki/Tuscan_food"),
            ("Parmigiano-Reggiano", "https://en.wikipedia.org/wiki/Parmigiano-Reggiano")
        ],
        "pinterest": {
            "board": "Seafood Dinners / One-Pot Skillets",
            "title": "20-Minute Creamy Garlic Parmesan Tuscan Salmon Skillet",
            "desc": "Crispy pan-seared salmon fillets simmering in a luxurious garlic parmesan cream sauce with sun-dried tomatoes and spinach in 20 minutes! Easy restaurant-quality dinner. Pin it now!",
            "tags": "#tuscansalmon #salmondinner #cremysalmon #onepotmeals #20minutedinner #easyseafood #dinnerideas"
        }
    },
    {
        "slug": "15-minute-crispy-honey-butter-garlic-chicken",
        "title": "15-Minute Crispy Honey Butter Garlic Chicken Bites",
        "headline": "15-Minute Crispy Pan-Seared Honey Butter Garlic Chicken Bites",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/crispy-honey-butter-garlic-chicken.jpg",
        "image_file": "crispy-honey-butter-garlic-chicken.jpg",
        "excerpt": "Ultra-crispy golden bite-sized chicken cutlets coated in a bubbling sweet and savory honey garlic butter glaze in 15 minutes.",
        "description": "Bite-sized chicken breast pieces dusted in cornstarch, pan-fried to shatteringly crisp golden perfection, and tossed in an addictive foaming honey garlic butter glaze.",
        "keywords": "honey butter garlic chicken, crispy chicken bites, 15 minute chicken recipe, quick skillet chicken, honey garlic chicken nuggets, easy weeknight chicken",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American / Asian Comfort Food",
        "calories": "470 kcal",
        "protein": "36g",
        "fat": "20g",
        "carbs": "34g",
        "fiber": "1g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "196",
        "quick_answer": "To make 15-minute crispy honey butter garlic chicken bites, cut 1.25 lbs boneless skinless chicken breasts into 1-inch bite-sized cubes and toss with 2 tbsp cornstarch, 1/2 tsp garlic powder, 1/2 tsp salt, and 1/4 tsp black pepper until evenly dusted. Heat 2 tbsp neutral oil in a large cast iron skillet over medium-high heat. Add chicken pieces in a single layer with space between them; pan-fry for 3 minutes per side until golden brown and super crispy (165°F). Push chicken aside or lower heat to medium-low, add 3 tbsp unsalted butter, 4 minced garlic cloves, 1/4 cup honey, and 1 tbsp soy sauce. Toss chicken in the foaming glaze for 60 seconds until sticky and shiny. Garnish with sliced green onions and toasted sesame seeds.",
        "takeaways": [
            ("Cornstarch Crisp Lock", "Tossing raw chicken in dry cornstarch creates a delicate starchy shell that crisps up instantly in hot oil and stays crunchy even under sticky glaze."),
            ("Foaming Honey Butter Chemistry", "Allowing butter and honey to foam together emulsifies the dairy fats with natural sugars, creating a thick, glossy caramel glaze that clings to every crevice."),
            ("Single Layer Spacing Rule", "Crowding the skillet causes chicken to steam rather than fry; keeping space between bites guarantees high-heat crispy browning.")
        ],
        "matrix_title": "Coating Starch Comparison for Skillet Chicken Bites",
        "matrix_headers": ["Coating Type", "Crispiness Level", "Glaze Durability", "Fry Time", "Verdict"],
        "matrix_rows": [
            ["Cornstarch", "Shatteringly crisp & light", "Holds crunch for 20+ mins", "5–6 minutes", "Superior Crunch Winner (Recommended)"],
            ["Potato Starch (Katakuriko)", "Ultra-crunchy & puffy", "Maximum crunch hold", "5 minutes", "Authentic Asian karaage style"],
            ["All-Purpose Flour", "Soft crust", "Gets soggy under glaze", "6–7 minutes", "Heavy & prone to softening"],
            ["Baking Powder Blend", "Very airy", "Crisp but salty", "5 minutes", "Better suited for oven wings"]
        ],
        "ingredients": [
            "1.25 lbs boneless skinless chicken breasts, cut into 1-inch cubes",
            "2 tbsp cornstarch",
            "1/2 tsp garlic powder",
            "1/2 tsp onion powder",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "2 tbsp avocado or canola oil",
            "3 tbsp unsalted butter",
            "4 cloves fresh garlic, finely minced",
            "1/4 cup raw honey",
            "1 tbsp low-sodium soy sauce",
            "1 tsp apple cider vinegar or lemon juice (balances sweetness)",
            "2 green onions, thinly sliced",
            "1 tsp toasted white sesame seeds"
        ],
        "instructions": [
            ("Coat the Chicken Bites", "Pat chicken cubes thoroughly dry with paper towels. In a mixing bowl, toss chicken with cornstarch, garlic powder, onion powder, salt, and black pepper until every piece has a light, even powdery coating."),
            ("Pan-Fry to Deep Golden Crunch", "Heat oil in a wide cast iron or heavy skillet over medium-high heat until shimmering hot. Add chicken bites in a single layer (work in two batches if needed so pan isn't crowded). Fry undisturbed for 3 minutes until deeply golden and crisp. Flip each piece and fry for another 2.5 to 3 minutes until cooked through (165°F)."),
            ("Melt & Foam Honey Butter", "Reduce heat to medium-low. Add butter and minced garlic to the skillet, stirring for 30 seconds until garlic is fragrant and butter begins foaming. Pour in honey, soy sauce, and apple cider vinegar."),
            ("Glaze the Chicken", "Toss the crispy chicken bites continuously with a silicone spatula for 60 to 90 seconds as the honey butter bubbles and thickens into an amber lacquer that coats every morsel."),
            ("Garnish & Serve", "Remove from heat immediately. Scatter sliced green onions and toasted sesame seeds over the skillet. Serve piping hot over steaming jasmine rice or with roasted green beans!")
        ],
        "pro_tip_title": "Elena’s Paper Towel Drying Habit",
        "pro_tip": "The biggest reason skillet chicken turns rubbery instead of crispy is invisible surface water! Before tossing your chicken in cornstarch, press it firmly between several layers of paper towels until completely dry. Dry chicken means the cornstarch adheres instantly and sizzles into shatteringly crisp edges.",
        "faqs": [
            ("Can I make this in the air fryer?", "Yes! Spray cornstarch-coated chicken with oil and air fry at 400°F for 8–10 minutes, shaking halfway. Melt the honey garlic butter in a skillet and toss the hot air-fried bites right in!"),
            ("Can I use chicken thighs?", "Absolutely! Boneless skinless chicken thighs cut into cubes stay extraordinarily juicy and have rich flavor in this honey butter sauce."),
            ("How do I store leftovers?", "Store in an airtight container in the fridge for up to 3 days. Reheat in an air fryer or dry skillet over medium heat for 3 minutes to restore the crispy coating.")
        ],
        "wiki_entities": [
            ("Fried chicken", "https://en.wikipedia.org/wiki/Fried_chicken"),
            ("Honey garlic sauce", "https://en.wikipedia.org/wiki/Honey_garlic_sauce"),
            ("Corn starch", "https://en.wikipedia.org/wiki/Corn_starch")
        ],
        "pinterest": {
            "board": "Quick Chicken Dinners / Easy Weeknight Meals",
            "title": "15-Minute Crispy Honey Butter Garlic Chicken Bites",
            "desc": "Ultra-crispy golden chicken bites coated in an addictive foaming honey garlic butter glaze in 15 minutes! Kids and adults will devour this easy dinner. Save this pin now!",
            "tags": "#honeybutterchicken #crispychicken #15minutedinner #chickenbites #honeygarlic #easyrecipes #quickdinner"
        }
    },
    {
        "slug": "20-minute-sheet-pan-moroccan-chicken-sweet-potatoes",
        "title": "20-Minute Sheet-Pan Moroccan Spiced Chicken and Roasted Sweet Potatoes",
        "headline": "20-Minute Sheet-Pan Moroccan Spiced Chicken Thighs and Sweet Potatoes",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/sheet-pan-moroccan-chicken-sweet-potatoes.jpg",
        "image_file": "sheet-pan-moroccan-chicken-sweet-potatoes.jpg",
        "excerpt": "Caramelized Moroccan-spiced chicken thighs roasted on one sheet pan with tender cubed sweet potatoes, charred red onions, garlic herb yogurt, and ruby pomegranate seeds in 20 minutes.",
        "description": "Warm fragrant spices meet sheet-pan convenience: juicy boneless chicken thighs roasted with diced sweet potatoes, cumin, cinnamon, and smoked paprika, served with cool garlic herb yogurt.",
        "keywords": "moroccan chicken sheet pan, sweet potato chicken dinner, 20 minute sheet pan suppers, spiced chicken thighs, healthy weeknight sheet pan",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Moroccan / North African",
        "calories": "480 kcal",
        "protein": "36g",
        "fat": "22g",
        "carbs": "34g",
        "fiber": "5g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "178",
        "quick_answer": "To make 20-minute sheet-pan Moroccan spiced chicken and sweet potatoes, dice 1 large sweet potato into small 1/2-inch cubes and microwave in a covered bowl with 1 tbsp water for 3 minutes to par-cook. Toss 1.5 lbs boneless skinless chicken thighs and the par-cooked sweet potatoes with 2 tbsp olive oil, 1.5 tsp cumin, 1 tsp smoked paprika, 1 tsp coriander, 1/2 tsp cinnamon, 1/2 tsp turmeric, 1 tsp salt, and 1/2 tsp black pepper. Spread across a large baking sheet with 1 sliced red onion. Roast at 425°F (220°C) for 14 minutes, switching to high broil for the final 2 minutes until chicken edges are charred and sweet potatoes are caramelized. Drizzle with garlic herb yogurt and scatter with fresh pomegranate seeds.",
        "takeaways": [
            ("Pre-Microwaved Sweet Potato Trick", "Dense sweet potatoes usually take 35 minutes to roast; par-cooking small 1/2-inch cubes in the microwave for 3 minutes slashes roasting time to just 14 minutes."),
            ("Warm Moroccan Spice Rub", "Cumin, smoked paprika, turmeric, and a hint of cinnamon create a fragrant, warm Mediterranean crust that pairs naturally with the sweetness of sweet potatoes."),
            ("Pomegranate & Fresh Mint Finish", "Sprinkling tart, juicy pomegranate arils and torn mint over the hot roasted pan introduces bursts of fresh acidity that brighten every bite.")
        ],
        "matrix_title": "Root Vegetable Pairing with Moroccan Spiced Poultry",
        "matrix_headers": ["Root Vegetable", "Par-Cook Need", "Caramelization", "Roast Time at 425°F", "Verdict"],
        "matrix_rows": [
            ["Orange Sweet Potatoes (1/2-inch)", "3 min microwave", "Rich caramelized natural sugars", "14 minutes", "Top Flavor Pairing (Recommended)"],
            ["Baby Gold Potatoes (halved)", "3 min microwave", "Crispy exterior, fluffy interior", "15 minutes", "Great classic savory option"],
            ["Butternut Squash Cubes", "2 min microwave", "Very sweet & tender", "12–14 minutes", "Delicious autumn alternative"],
            ["Carrot Coins", "No par-cook needed", "Firm & roasted", "15 minutes", "Good low-prep option"]
        ],
        "ingredients": [
            "1.5 lbs boneless skinless chicken thighs",
            "1 large sweet potato (approx. 12 oz), peeled and diced into 1/2-inch cubes",
            "1 medium red onion, cut into thin wedges",
            "2 tbsp extra virgin olive oil",
            "1.5 tsp ground cumin",
            "1 tsp smoked paprika",
            "1 tsp ground coriander",
            "1/2 tsp ground turmeric",
            "1/4 tsp ground cinnamon & pinch of cayenne pepper",
            "1 tsp kosher salt & 1/2 tsp cracked black pepper",
            "1/2 cup Greek yogurt mixed with 1 grated garlic clove and 1 tbsp lemon juice",
            "1/4 cup fresh pomegranate seeds (arils)",
            "Fresh cilantro and mint, chopped, plus lemon wedges for serving"
        ],
        "instructions": [
            ("Preheat Oven & Par-Cook Sweet Potatoes", "Preheat oven to 425°F (220°C). Place 1/2-inch diced sweet potatoes in a microwave-safe bowl with 1 tbsp water; cover with a plate and microwave on high for 3 minutes until fork-tender. Drain any remaining water."),
            ("Season Chicken & Vegetables", "In a large bowl, combine chicken thighs, par-cooked sweet potatoes, and red onion wedges. Drizzle with olive oil. Sprinkle with cumin, smoked paprika, coriander, turmeric, cinnamon, cayenne, salt, and pepper. Toss with hands until thoroughly coated in the fragrant spice rub."),
            ("Arrange on Sheet Pan", "Spread chicken and vegetables across a large rimmed baking sheet in a single layer. Make sure the sweet potatoes and onions are scattered evenly around the chicken thighs so everything roasts evenly."),
            ("Roast & Broil", "Roast at 425°F for 14 minutes until chicken reaches 165°F. Switch oven to HIGH BROIL for the final 2 minutes to blister the chicken skin and caramelize the sweet potato edges."),
            ("Garnish & Serve", "Remove sheet pan from oven. Drizzle the creamy garlic lemon yogurt across the hot chicken and sweet potatoes. Shower with ruby pomegranate arils, fresh chopped cilantro, and mint leaves. Serve straight from the pan with lemon wedges!")
        ],
        "pro_tip_title": "Elena’s 1/2-Inch Knife Uniformity Rule",
        "pro_tip": "Take 60 extra seconds to cut your sweet potatoes into uniform 1/2-inch dice! Uneven chunks mean tiny pieces burn while large ones stay hard in the center. Consistent sizing guarantees every single sweet potato cube turns creamy inside with golden caramelized edges in under 15 minutes.",
        "faqs": [
            ("Can I make this with chicken breasts?", "Yes! Boneless skinless chicken breasts work well; cut them into large 2-inch chunks so they roast evenly with the sweet potatoes in 12–14 minutes."),
            ("Can I prep this the night before?", "Yes, toss the chicken, potatoes, and spices together in an airtight container up to 24 hours in advance. When ready, spread on your sheet pan and roast!"),
            ("What can I substitute for pomegranate seeds?", "Dried cranberries, chopped dried apricots, or golden raisins provide a similar sweet-tart chewiness that complements Moroccan spices.")
        ],
        "wiki_entities": [
            ("Moroccan cuisine", "https://en.wikipedia.org/wiki/Moroccan_cuisine"),
            ("Sweet potato", "https://en.wikipedia.org/wiki/Sweet_potato"),
            ("Pomegranate", "https://en.wikipedia.org/wiki/Pomegranate")
        ],
        "pinterest": {
            "board": "Sheet Pan Suppers / Healthy Dinner Ideas",
            "title": "20-Minute Sheet-Pan Moroccan Spiced Chicken and Sweet Potatoes",
            "desc": "Juicy spiced chicken thighs roasted on one sheet pan with caramelized sweet potatoes, garlic yogurt, and pomegranate seeds in 20 minutes! Easy healthy dinner. Save it now!",
            "tags": "#moroccanchicken #sheetpanmeals #sweetpotatoes #20minutemeals #healthydinner #glutenfree #easyrecipes"
        }
    },
    {
        "slug": "15-minute-coconut-lime-shrimp-noodles",
        "title": "15-Minute Creamy Coconut Lime Garlic Shrimp Rice Noodle Bowls",
        "headline": "15-Minute Creamy Coconut Lime Garlic Shrimp Rice Noodle Bowls",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/coconut-lime-shrimp-noodles.jpg",
        "image_file": "coconut-lime-shrimp-noodles.jpg",
        "excerpt": "Succulent seared jumbo shrimp tossed with tender rice vermicelli noodles in a luscious coconut lime garlic broth with shredded cabbage, chilies, and crushed peanuts in 15 minutes.",
        "description": "Bright, aromatic Southeast Asian flavors in 15 minutes: plump pink shrimp flash-seared and bathed in a silky coconut milk, fresh lime, garlic, and ginger broth over vermicelli rice noodles.",
        "keywords": "coconut lime shrimp, shrimp rice noodles, 15 minute seafood dinner, coconut milk shrimp, easy asian noodles, quick weeknight shrimp",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Southeast Asian / Thai Inspired",
        "calories": "440 kcal",
        "protein": "28g",
        "fat": "18g",
        "carbs": "44g",
        "fiber": "2g",
        "sodium": "650mg",
        "ratingValue": "4.9",
        "reviewCount": "189",
        "quick_answer": "To make 15-minute creamy coconut lime shrimp noodle bowls, soak 8 oz thin rice vermicelli noodles in boiling water for 4 minutes, then drain and rinse with cold water. Pat 1 lb raw peeled jumbo shrimp dry and season with salt and pepper. Heat 1 tbsp coconut or avocado oil in a deep skillet over high heat; sear shrimp for 90 seconds per side until pink and curled, then transfer to a plate. Reduce heat to medium, add 1 tbsp oil, 4 minced garlic cloves, 1 tbsp grated fresh ginger, and 1 thinly sliced red chili; sauté for 45 seconds. Pour in 1 can (13.5 oz) full-fat coconut milk, 1.5 tbsp fish sauce (or soy sauce), 1 tbsp brown sugar, and zest and juice of 1 large lime. Simmer for 3 minutes until velvety. Return shrimp and noodles to the skillet to warm through. Serve topped with crushed peanuts, fresh cilantro, and shredded purple cabbage.",
        "takeaways": [
            ("Vermicelli Steep Shortcut", "Thin rice vermicelli noodles require no stove boiling—simply submerge in hot tap or kettle water for 4 minutes to achieve tender, springy noodles."),
            ("Flash-Sear Shrimp Timing", "Jumbo shrimp cook in just 3 minutes total; removing them from the skillet while making the coconut broth prevents rubbery overcooking."),
            ("Lime Zest Flavor Secret", "Fresh lime juice adds acidity, but the zest contains aromatic citrus oils that infuse authentic Southeast Asian vibrancy into rich coconut milk.")
        ],
        "matrix_title": "Noodle Variety Comparison in Coconut Lime Broth",
        "matrix_headers": ["Noodle Variety", "Soak / Boil Time", "Texture / Chew", "Broth Absorption", "Verdict"],
        "matrix_rows": [
            ["Rice Vermicelli (Rice Sticks)", "4 min hot soak", "Delicate, light & springy", "Drinks in coconut lime broth", "Top Speed & Texture Pick (Recommended)"],
            ["Pad Thai Rice Noodles (Fettuccine size)", "8 min soak + 2 min boil", "Chewy & flat", "High sauce cling", "Great heartier option"],
            ["Ramen Noodles", "3 min boil", "Springy & curly", "Moderate", "Fun everyday alternative"],
            ["Soba (Buckwheat) Noodles", "4 min boil", "Earthy & nutty", "Low", "Too heavy for bright lime broth"]
        ],
        "ingredients": [
            "1 lb raw jumbo shrimp (16/20 count), peeled, deveined, and tails removed",
            "8 oz thin rice vermicelli noodles",
            "1 can (13.5 oz) full-fat unsweetened coconut milk",
            "1 tbsp coconut oil or avocado oil",
            "4 cloves fresh garlic, finely minced",
            "1 tbsp fresh ginger, grated",
            "1 fresh red chili or serrano pepper, thinly sliced",
            "1.5 tbsp fish sauce (or tamari soy sauce)",
            "1 tbsp light brown sugar or coconut sugar",
            "Zest and juice of 2 fresh juicy limes",
            "1 cup shredded purple cabbage",
            "1/4 cup roasted salted peanuts, roughly chopped",
            "1/2 cup fresh cilantro leaves, chopped"
        ],
        "instructions": [
            ("Soak Rice Noodles", "Place rice vermicelli noodles in a large heatproof bowl. Pour boiling water over the noodles until fully submerged. Let soak for 4 minutes until tender. Drain in a colander, rinse briefly with cold water to stop cooking, and set aside."),
            ("Flash-Sear Shrimp", "Pat peeled shrimp completely dry with paper towels. Season with a pinch of salt and pepper. Heat 1 tbsp coconut oil in a wide deep skillet over high heat until shimmering. Add shrimp in a single layer and sear for 90 seconds per side until pink, curled, and slightly caramelized. Transfer shrimp to a plate."),
            ("Sauté Aromatics", "Reduce skillet heat to medium. Add minced garlic, grated ginger, and sliced red chilies. Sauté for 45 to 60 seconds until fragrant and sizzling without burning."),
            ("Simmer Coconut Lime Broth", "Pour in the full-fat coconut milk, fish sauce, brown sugar, lime zest, and lime juice. Whisk gently and bring to a bubbling simmer over medium heat for 3 minutes until smooth and fragrant."),
            ("Toss & Serve", "Add the drained rice noodles and seared shrimp into the bubbling coconut broth. Toss gently with tongs for 60 seconds until heated through. Divide into wide bowls and top with shredded purple cabbage, chopped peanuts, fresh cilantro, and lime wedges!")
        ],
        "pro_tip_title": "Elena’s Cold Rinse Noodle Habit",
        "pro_tip": "Always rinse cooked rice noodles under cold running water immediately after draining! Rinsing washes away excess surface starches that cause rice noodles to turn mushy and clump into a solid brick. When tossed into the hot coconut broth, the clean individual strands absorb the broth cleanly.",
        "faqs": [
            ("Can I make this vegetarian / vegan?", "Yes! Swap the shrimp for crispy pan-seared cubed tofu or edamame, and substitute soy sauce or vegetarian stir-fry sauce for fish sauce."),
            ("Can I use light coconut milk?", "You can, but light coconut milk produces a much thinner, watery broth. Full-fat canned coconut milk creates that luxurious, creamy restaurant texture."),
            ("How do I store leftovers?", "Store leftover shrimp and coconut broth separately from the rice noodles if possible, as noodles will continue absorbing liquid. Keep in the fridge for up to 2 days.")
        ],
        "wiki_entities": [
            ("Rice vermicelli", "https://en.wikipedia.org/wiki/Rice_vermicelli"),
            ("Coconut milk", "https://en.wikipedia.org/wiki/Coconut_milk"),
            ("Fish sauce", "https://en.wikipedia.org/wiki/Fish_sauce")
        ],
        "pinterest": {
            "board": "Quick Asian Dinners / Seafood Recipes",
            "title": "15-Minute Creamy Coconut Lime Shrimp Rice Noodle Bowls",
            "desc": "Tender jumbo shrimp tossed with delicate rice noodles in a velvety coconut lime garlic broth with crunchy peanuts and cilantro in 15 minutes! The ultimate weeknight noodle craving. Pin it now!",
            "tags": "#shrimpnoodles #coconutlime #15minutedinner #ricenoodles #asianfood #easyseafood #quickdinner"
        }
    },
    {
        "slug": "20-minute-tuscan-sausage-white-bean-soup",
        "title": "20-Minute Creamy Italian Sausage and Tuscan White Bean Soup",
        "headline": "20-Minute Creamy Italian Sausage, Kale, and Tuscan White Bean Soup",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/tuscan-sausage-white-bean-soup.jpg",
        "image_file": "tuscan-sausage-white-bean-soup.jpg",
        "excerpt": "Savory browned Italian sausage crumbles simmered with creamy white cannellini beans, tender Tuscan kale, and parmesan cream in a rich, restorative broth in 20 minutes.",
        "description": "Zuppa Toscana comfort in 20 minutes: savory browned Italian sausage, velvety white beans, and dark curly kale simmering in a creamy parmesan garlic broth with crusty sourdough bread.",
        "keywords": "tuscan sausage soup, white bean and sausage soup, 20 minute soup, zuppa toscana shortcut, creamy italian soup, easy weeknight soup",
        "prepTime": "PT4M",
        "cookTime": "PT16M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian / Tuscan Comfort",
        "calories": "510 kcal",
        "protein": "26g",
        "fat": "32g",
        "carbs": "31g",
        "fiber": "6g",
        "sodium": "690mg",
        "ratingValue": "4.9",
        "reviewCount": "191",
        "quick_answer": "To make 20-minute creamy Italian sausage and Tuscan white bean soup, heat a Dutch oven over medium-high heat. Brown 1 lb sweet or mild Italian sausage, breaking it into bite-sized crumbles for 5 minutes until crispy; remove half the rendered fat. Add 1 diced yellow onion and 4 minced garlic cloves; cook for 2 minutes. Pour in 4 cups low-sodium chicken bone broth and two 15-oz cans of drained, rinsed cannellini beans. Lightly mash 1/3 of the beans with a potato masher to naturally thicken the broth. Bring to a boil, reduce heat, and stir in 3 packed cups of chopped Tuscan or curly kale and 1/2 cup heavy cream. Simmer for 4 minutes until kale is tender. Finish with 1/2 cup grated parmesan cheese and crushed red pepper flakes. Serve with toasted rustic sourdough.",
        "takeaways": [
            ("Cannellini Starch Thickening", "Crushing a cup of tender cannellini beans directly in the pot releases natural bean starches that transform thin broth into a hearty, velvety chowder consistency."),
            ("Italian Sausage Fond Base", "Browning sausage meat builds deep savory caramelized fond on the bottom of the Dutch oven that deglazes into the broth for rich, slow-simmered taste in minutes."),
            ("Kale Tenderizing Simmer", "Chopped lacinato or curly kale wilts down into tender, silky ribbons in just 4 minutes of gentle simmering while holding vibrant dark green color.")
        ],
        "matrix_title": "Sausage Variety Performance in Tuscan Broth",
        "matrix_headers": ["Sausage Type", "Fennel & Herb Profile", "Fat / Richness", "Simmer Speed", "Verdict"],
        "matrix_rows": [
            ["Sweet Italian Pork Sausage", "Classic toasted fennel & garlic", "Rich & juicy", "5 minutes browning", "Traditional Gold Standard (Recommended)"],
            ["Spicy Hot Italian Sausage", "Bold chili pepper & fennel", "Rich & warming", "5 minutes browning", "Great for lovers of spice"],
            ["Italian Turkey / Chicken Sausage", "Herbal & clean", "Lean", "4–5 minutes browning", "Excellent lower-fat alternative"],
            ["Plant-Based Italian Sausage", "Savory herbal blend", "Moderate", "4 minutes browning", "Great vegetarian base"]
        ],
        "ingredients": [
            "1 lb bulk sweet or hot Italian sausage (casings removed)",
            "2 cans (15 oz each) cannellini or Great Northern beans, rinsed and drained",
            "1 medium yellow onion, finely diced",
            "4 cloves fresh garlic, minced",
            "4 cups rich chicken bone broth or vegetable broth",
            "3 cups packed chopped Tuscan (Lacinato) or curly kale leaves, stems discarded",
            "1/2 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "1 tsp dried oregano & 1/2 tsp dried thyme",
            "1/4 tsp crushed red pepper flakes",
            "1/2 tsp kosher salt & 1/2 tsp cracked black pepper",
            "Thick slices of toasted sourdough bread, for serving"
        ],
        "instructions": [
            ("Brown the Sausage", "Heat a large Dutch oven or heavy soup pot over medium-high heat. Add the Italian sausage and cook for 5 minutes, breaking it apart with a wooden spoon into bite-sized morsels until browned and crispy at the edges. (Drain excess fat if needed, leaving 1 tbsp in the pot)."),
            ("Sauté Onion & Garlic", "Add diced yellow onion, minced garlic, oregano, thyme, and red pepper flakes to the sausage. Sauté for 2 minutes until onion is softened and translucent."),
            ("Add Broth & Mash Beans", "Pour in chicken bone broth and the drained cannellini beans. Bring to a rolling boil. Use a potato masher or the back of a large spoon to gently crush about one-third of the beans against the side of the pot to thicken the soup."),
            ("Simmer Kale & Cream", "Reduce heat to medium-low. Stir in chopped kale and heavy cream. Simmer gently for 4 minutes until the kale is tender and wilted into the rich broth."),
            ("Stir in Parmesan & Serve", "Turn off heat. Stir in freshly grated parmesan cheese until melted throughout. Taste and season with additional salt and black pepper as desired. Ladle into warm bowls and serve with thick, crusty slices of toasted sourdough bread for dipping!")
        ],
        "pro_tip_title": "Elena’s Parmesan Rind Simmer Hack",
        "pro_tip": "Whenever you finish a wedge of real Parmigiano-Reggiano, save the hard cheese rind in a bag in your freezer! Tossing a frozen parmesan rind into this soup as it boils infuses deep, savory umami and glutamates that make a 20-minute weeknight soup taste like it simmered all afternoon.",
        "faqs": [
            ("Can I use spinach instead of kale?", "Yes! Fresh baby spinach wilts in just 60 seconds; simply stir it in right at the end when adding the parmesan cheese."),
            ("Can I freeze this soup?", "Soups with cream can sometimes separate when frozen. To freeze, freeze the soup before adding heavy cream; thaw, bring to a simmer, and stir in cream and parmesan fresh before serving."),
            ("Is this soup similar to Olive Garden's Zuppa Toscana?", "Yes! It has the same beloved flavor profile of Italian sausage, creamy broth, and kale, but swaps slow-cooking sliced potatoes for high-protein, creamy cannellini beans for a faster weeknight dinner.")
        ],
        "wiki_entities": [
            ("Zuppa toscana", "https://en.wikipedia.org/wiki/Zuppa_toscana"),
            ("Cannellini", "https://en.wikipedia.org/wiki/Phaseolus_vulgaris"),
            ("Kale", "https://en.wikipedia.org/wiki/Kale")
        ],
        "pinterest": {
            "board": "Cozy Soups & Stews / Italian Comfort Food",
            "title": "20-Minute Creamy Italian Sausage and Tuscan White Bean Soup",
            "desc": "Browned Italian sausage, creamy white cannellini beans, and tender kale simmered in a rich parmesan broth in 20 minutes! Cozy restaurant-style comfort food. Pin it now!",
            "tags": "#tuscansoup #zuppatoscana #italiansausage #whitebeansoup #20minutesoup #comfortfood #easyrecipes"
        }
    },
    {
        "slug": "15-minute-spicy-gochujang-beef-broccoli",
        "title": "15-Minute Spicy Korean Gochujang Beef and Broccoli Skillet",
        "headline": "15-Minute Sizzling Spicy Korean Gochujang Beef and Broccoli Stir-Fry",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/spicy-gochujang-beef-broccoli.jpg",
        "image_file": "spicy-gochujang-beef-broccoli.jpg",
        "excerpt": "Thinly sliced tender flank steak strips and bright green broccoli florets sizzling in a glossy spicy-sweet Korean gochujang garlic sauce with sesame in 15 minutes.",
        "description": "Better than takeout: tender seared beef sirloin and crisp-tender broccoli florets tossed in a fiery, sweet fermented gochujang chili garlic glaze in a blazing hot wok in 15 minutes.",
        "keywords": "gochujang beef and broccoli, spicy korean beef, 15 minute beef stir fry, quick wok dinner, easy weeknight beef, korean takeout at home",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Korean / Asian Wok",
        "calories": "460 kcal",
        "protein": "36g",
        "fat": "20g",
        "carbs": "32g",
        "fiber": "4g",
        "sodium": "680mg",
        "ratingValue": "4.9",
        "reviewCount": "193",
        "quick_answer": "To make 15-minute spicy Korean gochujang beef and broccoli, slice 1.25 lbs flank or sirloin steak thinly against the grain and toss with 1 tbsp soy sauce and 1 tbsp cornstarch. In a small bowl, whisk 2 tbsp Korean gochujang paste, 2 tbsp low-sodium soy sauce, 1.5 tbsp brown sugar, 1 tbsp toasted sesame oil, 1 tbsp rice vinegar, and 2 tbsp water. Heat 1 tbsp oil in a large wok over high heat. Add beef strips in a single layer; sear undisturbed for 2 minutes to caramelize, flip and sear for 1 minute, then transfer to a plate. Add 1 tbsp oil, 3 cups small broccoli florets, and 2 tbsp water; cover skillet for 2 minutes to steam-crisp. Add 3 minced garlic cloves, 1 tbsp grated ginger, the seared beef, and the gochujang sauce. Toss vigorously over high heat for 60 seconds until glossy. Shower with sesame seeds and green onions.",
        "takeaways": [
            ("Velveting Beef with Cornstarch", "Tossing thinly sliced beef in cornstarch before flash-searing protects the muscle fibers, locking in juices and delivering melt-in-mouth tenderness."),
            ("Wok Steam-Crisp Broccoli Hack", "Adding a splash of water and covering the wok for 2 minutes steams broccoli florets into vibrant emerald green crisp-tender perfection without boiling a separate pot."),
            ("Fermented Sweet-Spicy Balance", "Gochujang's fermented chili warmth combined with brown sugar and toasted sesame oil coats both meat and vegetable in a restaurant-quality glaze.")
        ],
        "matrix_title": "Beef Cut Performance for Rapid Stir-Frying",
        "matrix_headers": ["Beef Cut", "Slicing Orientation", "Tenderness Level", "Sear Time", "Verdict"],
        "matrix_rows": [
            ["Flank Steak", "Across the grain", "Very tender with cornstarch", "2.5 minutes", "Top Stir-Fry Value (Recommended)"],
            ["Top Sirloin", "Across grain or thin strips", "Naturally tender & lean", "2–3 minutes", "Superb all-around option"],
            ["Skirt Steak", "Thinly across the grain", "Intense beefy flavor", "2 minutes", "Excellent high-heat choice"],
            ["Stew Beef", "Cubed", "Tough without long braise", "N/A", "Avoid for quick stir-fries"]
        ],
        "ingredients": [
            "1.25 lbs flank steak or sirloin steak, thinly sliced against the grain",
            "1 tbsp cornstarch",
            "2 tbsp neutral oil (avocado or peanut oil, divided)",
            "3 cups fresh broccoli florets, cut into bite-sized pieces",
            "3 cloves fresh garlic, finely minced",
            "1 tbsp fresh ginger, grated",
            "2 tbsp Korean gochujang chili paste",
            "2 tbsp low-sodium soy sauce",
            "1.5 tbsp brown sugar",
            "1 tbsp toasted sesame oil",
            "1 tbsp rice vinegar",
            "2 tbsp water",
            "1 tbsp toasted sesame seeds",
            "2 green onions, thinly sliced",
            "Steamed white jasmine rice, for serving"
        ],
        "instructions": [
            ("Slice & Velvet Beef", "Slice flank steak thinly against the natural grain into bite-sized strips. In a bowl, toss beef with cornstarch and 1 tbsp soy sauce until lightly coated and glossy."),
            ("Whisk Gochujang Sauce", "In a small bowl, whisk gochujang, remaining soy sauce, brown sugar, sesame oil, rice vinegar, and 2 tbsp water until smooth."),
            ("Sear the Beef", "Heat 1 tbsp oil in a large wok or cast iron skillet over high heat until smoking hot. Add beef strips in a single layer and let sear undisturbed for 2 minutes to develop deep wok browning. Flip and stir-fry for 1 minute until just browned. Transfer beef to a plate."),
            ("Steam-Crisp Broccoli", "Add remaining 1 tbsp oil to the wok over medium-high heat. Add broccoli florets and 2 tbsp water; immediately cover with a lid or foil for 2 minutes to steam-cook until bright emerald green and crisp-tender. Uncover, add minced garlic and ginger, and sauté for 45 seconds."),
            ("Toss with Sauce & Glaze", "Return seared beef and any resting juices to the wok. Pour in the gochujang sauce mixture. Toss everything continuously over high heat for 60 to 90 seconds until the sauce bubbles, thickens, and lacquers every piece of beef and broccoli. Garnish with sesame seeds and green onions; serve with hot rice!")
        ],
        "pro_tip_title": "Elena’s 15-Minute Freezer Slicing Hack",
        "pro_tip": "Trying to slice raw, squishy steak paper-thin can be frustrating! Pop your steak into the freezer for 15 minutes before cooking. The cold firms up the beef just enough to let your chef's knife glide through effortlessly, yielding restaurant-thin slices that cook in 120 seconds.",
        "faqs": [
            ("Can I use frozen broccoli?", "Fresh broccoli delivers far superior crispness! If using frozen, thaw completely and pat thoroughly dry with paper towels to prevent watering down the sauce."),
            ("How spicy is this stir-fry?", "It has a pleasant medium kick. To make it milder, reduce gochujang to 1 tablespoon and increase soy sauce by 1 tablespoon. To make it fiery, add 1 tsp gochugaru (Korean chili flakes)."),
            ("Can I meal prep this?", "Yes! It reheats beautifully in a microwave or quick skillet toss for up to 4 days, making it an exceptional high-protein meal prep lunch.")
        ],
        "wiki_entities": [
            ("Gochujang", "https://en.wikipedia.org/wiki/Gochujang"),
            ("Broccoli", "https://en.wikipedia.org/wiki/Broccoli"),
            ("Flank steak", "https://en.wikipedia.org/wiki/Flank_steak")
        ],
        "pinterest": {
            "board": "Quick Asian Dinners / Easy Beef Recipes",
            "title": "15-Minute Spicy Korean Gochujang Beef and Broccoli Skillet",
            "desc": "Tender thinly sliced beef sirloin and crisp bright broccoli sizzling in a glossy spicy-sweet Korean gochujang sauce in 15 minutes! Better than takeout. Pin it now!",
            "tags": "#beefandbroccoli #gochujang #koreanbeef #15minutedinner #stirfry #asianfood #quickdinner #easyrecipes"
        }
    },
    {
        "slug": "20-minute-sheet-pan-feta-chickpea-gyro-bowls",
        "title": "20-Minute Sheet-Pan Crispy Roasted Feta and Chickpea Gyro Bowls",
        "headline": "20-Minute Sheet-Pan Roasted Feta and Crispy Chickpea Gyro Bowls",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/sheet-pan-feta-chickpea-gyro-bowls.jpg",
        "image_file": "sheet-pan-feta-chickpea-gyro-bowls.jpg",
        "excerpt": "Golden crispy spiced chickpeas and caramelized roasted feta cheese cubes from a hot sheet pan, served over turmeric rice with cucumbers, tomatoes, and cool tzatziki in 20 minutes.",
        "description": "High-protein Mediterranean vegetarian bowl in 20 minutes: spiced roasted chickpeas and charred feta cheese baked on one sheet pan, served with crisp Greek salad and creamy tzatziki.",
        "keywords": "roasted feta chickpea bowls, sheet pan gyro bowls, 20 minute vegetarian dinner, greek chickpea bowls, baked feta dinner, healthy mediterranean bowls",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Greek / Mediterranean Vegetarian",
        "calories": "450 kcal",
        "protein": "19g",
        "fat": "21g",
        "carbs": "49g",
        "fiber": "8g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "176",
        "quick_answer": "To make 20-minute sheet-pan roasted feta and chickpea gyro bowls, drain and thoroughly pat dry two 15-oz cans of chickpeas. Cut an 8-oz block of Greek feta cheese into 1-inch cubes. On a large rimmed baking sheet, toss chickpeas and feta cubes with 2 tbsp olive oil, 1 tsp dried oregano, 1 tsp garlic powder, 1 tsp smoked paprika, 1/2 tsp cumin, and 1/4 tsp black pepper. Spread into a single layer and roast at 425°F (220°C) for 14 minutes, switching to high broil for the final 2 minutes until chickpeas are crunchy and feta edges are deeply caramelized. Assemble into bowls with warm turmeric yellow rice, sliced Persian cucumbers, halved cherry tomatoes, kalamata olives, pickled red onions, and a generous swirl of chilled tzatziki.",
        "takeaways": [
            ("Drying Chickpeas for Crunch", "Rolling canned chickpeas between kitchen towels to remove moisture and loose skins ensures they roast into crunchy golden bites instead of remaining soft."),
            ("Caramelized Block Feta", "Roasting whole milk Greek feta at 425°F browns the exterior with savory golden edges while leaving the center warm, creamy, and spreadable."),
            ("Complete Plant-Based Protein", "Combining chickpeas with yellow rice and feta cheese delivers a satisfying 19 grams of protein and 8 grams of prebiotic fiber per bowl.")
        ],
        "matrix_title": "Feta Cheese Variety Performance for Sheet Pan Roasting",
        "matrix_headers": ["Feta Type", "Melt Resistance", "Caramelization Crust", "Salt Balance", "Verdict"],
        "matrix_rows": [
            ["Greek Block Feta (Sheep/Goat)", "High (holds cube shape)", "Deep golden brown edges", "Rich & briny", "Superior Roasting Choice (Recommended)"],
            ["French Feta (Sheep's Milk)", "Moderate (softens faster)", "Light golden", "Creamier & milder", "Delicious melt-in-mouth option"],
            ["American Cow's Milk Feta", "Low (tends to crumble)", "Uneven browning", "Salty & dry", "Avoid pre-crumbled containers"],
            ["Vegan Block Feta (Coconut base)", "Very low (melts into pool)", "Minimal browning", "Mild", "Add fresh instead of roasting"]
        ],
        "ingredients": [
            "2 cans (15 oz each) chickpeas (garbanzo beans), drained and rinsed",
            "8 oz high-quality Greek feta cheese (in brine), drained and cut into 1-inch cubes",
            "2 tbsp extra virgin olive oil",
            "1 tsp dried Greek oregano",
            "1 tsp garlic powder",
            "1 tsp smoked paprika",
            "1/2 tsp ground cumin",
            "1/2 tsp freshly cracked black pepper",
            "4 cups warm cooked yellow turmeric rice or brown rice",
            "2 Persian cucumbers, thinly sliced",
            "1 cup cherry tomatoes, halved",
            "1/3 cup kalamata olives, pitted",
            "1/3 cup pickled red onions",
            "3/4 cup prepared authentic Greek tzatziki sauce",
            "Fresh dill and lemon wedges for serving"
        ],
        "instructions": [
            ("Preheat & Dry Chickpeas", "Preheat oven to 425°F (220°C). Pour drained chickpeas onto a clean kitchen towel or paper towels. Gently roll them dry, discarding any loose skins that slip off."),
            ("Season on Sheet Pan", "Transfer dried chickpeas and cubed feta cheese to a large rimmed baking sheet. Drizzle with 2 tbsp olive oil. Sprinkle with dried oregano, garlic powder, smoked paprika, cumin, and cracked black pepper. Gently toss with hands to coat, taking care not to crush the feta cubes."),
            ("Roast & Broil", "Spread into a single layer across the sheet pan. Roast at 425°F for 14 minutes. Switch oven to HIGH BROIL for the last 2 minutes until chickpea skins are crackled and feta edges are blistered and deeply golden."),
            ("Assemble the Bowls", "Divide warm yellow rice into 4 wide bowls. Spoon the sizzling crispy chickpeas and warm roasted feta cubes over one side."),
            ("Add Fresh Toppings & Tzatziki", "Arrange sliced cucumbers, halved tomatoes, kalamata olives, and pickled red onions around the bowl. Top each with a generous dollop of creamy tzatziki, fresh dill fronds, and a squeeze of fresh lemon juice!")
        ],
        "pro_tip_title": "Elena’s Block Feta Rule",
        "pro_tip": "Always buy block feta preserved in brine rather than pre-crumbled tubs! Pre-crumbled feta is coated in anti-caking starches that dry out and burn into rubbery bits in the oven. Cutting a block of feta yourself ensures luscious, creamy centers with golden crispy roasted edges.",
        "faqs": [
            ("Can I make this in an air fryer?", "Yes! Air fry the chickpeas and feta cubes at 390°F for 8–10 minutes, shaking gently halfway through until golden and crispy."),
            ("Can I substitute cauliflower rice?", "Yes! For a low-carb grain bowl, swap the yellow rice for roasted garlic cauliflower rice."),
            ("How do I store leftovers?", "Store the roasted chickpeas and feta in an airtight container for up to 4 days. Reheat in the toaster oven or skillet for 3 minutes to crisp back up before topping fresh veggies.")
        ],
        "wiki_entities": [
            ("Feta", "https://en.wikipedia.org/wiki/Feta"),
            ("Chickpea", "https://en.wikipedia.org/wiki/Chickpea"),
            ("Tzatziki", "https://en.wikipedia.org/wiki/Tzatziki")
        ],
        "pinterest": {
            "board": "Vegetarian Bowls / Greek Recipes",
            "title": "20-Minute Sheet-Pan Crispy Roasted Feta and Chickpea Gyro Bowls",
            "desc": "Crispy spiced roasted chickpeas and caramelized golden feta cubes baked on one sheet pan in 20 minutes! Served over turmeric rice with tzatziki. Pin this healthy dinner now!",
            "tags": "#fetabowls #chickpeagyro #sheetpanmeals #20minutedinner #vegetariandinner #greekfood #healthybowls"
        }
    },
    {
        "slug": "15-minute-pan-seared-lemon-herb-cod",
        "title": "15-Minute Pan-Seared Garlic Herb Butter Cod with Zucchini Ribbons",
        "headline": "15-Minute Pan-Seared Garlic Herb Butter Cod over Zucchini Ribbons",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/pan-seared-lemon-herb-cod.jpg",
        "image_file": "pan-seared-lemon-herb-cod.jpg",
        "excerpt": "Thick flaky wild Pacific cod loins pan-seared with a golden crust, basted in bubbling lemon herb garlic butter over tender sautéed zucchini ribbons in 15 minutes.",
        "description": "Clean, light restaurant luxury in 15 minutes: tender pan-seared Pacific cod with a golden crust, basted in foaming garlic lemon thyme butter over shaved zucchini ribbons and capers.",
        "keywords": "pan seared cod, lemon herb butter cod, 15 minute fish dinner, cod with zucchini, easy white fish, healthy low carb seafood",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "French Bistro / Mediterranean",
        "calories": "340 kcal",
        "protein": "34g",
        "fat": "18g",
        "carbs": "6g",
        "fiber": "2g",
        "sodium": "490mg",
        "ratingValue": "4.9",
        "reviewCount": "180",
        "quick_answer": "To make 15-minute pan-seared garlic herb butter cod with zucchini ribbons, use a vegetable peeler to shave 2 medium green and yellow zucchinis into long ribbons. Pat 4 thick cod loins (6 oz each) completely dry with paper towels and season with salt, pepper, and garlic powder. Heat 1 tbsp olive oil in a heavy stainless or cast iron skillet over medium-high heat. Sear cod loins undisturbed for 4 minutes until a deep golden crust forms. Carefully flip, add 2.5 tbsp unsalted butter, 3 smashed garlic cloves, 1 tbsp drained capers, and fresh thyme sprigs. Baste the cod continuously with foaming butter for 3 minutes until flaky (135°F). Transfer fish to a plate, add zucchini ribbons to the pan drippings, and sauté for 90 seconds until tender-crisp. Serve cod over the ribbons with pan juices and lemon wedges.",
        "takeaways": [
            ("Loin Thickness Advantage", "Thick center-cut cod loins hold up to high-heat pan searing without falling apart, yielding moist, tender milky flakes."),
            ("Rapid Ribbon Sauté", "Shaving zucchini into ribbons using a Y-peeler allows the vegetable to cook in the fragrant fish drippings in just 90 seconds without turning watery."),
            ("Continuous Butter Arrosé", "Basting the top of the fish with foaming garlic herb butter cooks the delicate interior through gentle convection while building luxurious flavor.")
        ],
        "matrix_title": "Cod Cut Selection for High-Heat Pan-Searing",
        "matrix_headers": ["Cod Portion", "Thickness", "Flake Integrity", "Sear Time", "Verdict"],
        "matrix_rows": [
            ["Thick Center-Cut Cod Loins", "1.25–1.5 inches", "Large, succulent firm flakes", "7 minutes", "Gold Standard for Searing (Recommended)"],
            ["Cod Fillet Tail End", "Thin (0.5 inch)", "Fragile (breaks easily)", "3–4 minutes", "Better for fish tacos or poaching"],
            ["Lingcod", "Dense & steaky", "Very firm", "7–8 minutes", "Great regional substitute"],
            ["Haddock Loins", "Moderately thick", "Tender sweet flakes", "6 minutes", "Excellent everyday alternative"]
        ],
        "ingredients": [
            "4 thick wild Pacific cod loins (approx. 6 oz each)",
            "2 medium zucchini (1 green, 1 yellow squash), shaved into ribbons with a peeler",
            "1 tbsp extra virgin olive oil",
            "2.5 tbsp unsalted butter",
            "3 cloves fresh garlic, smashed and peeled",
            "1 tbsp drained briny capers",
            "4 sprigs fresh thyme",
            "1 organic lemon, thinly sliced and half juiced",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper",
            "1/2 tsp garlic powder",
            "Fresh chopped parsley for garnish"
        ],
        "instructions": [
            ("Prep Zucchini & Fish", "Using a Y-peeler, shave zucchinis lengthwise into long ribbons, stopping when you reach the seedy center. Pat cod loins thoroughly dry with paper towels. Season both sides with salt, pepper, and garlic powder."),
            ("Pan-Sear the Cod", "Heat olive oil in a large skillet over medium-high heat until shimmering hot. Gently add the cod loins. Sear undisturbed for 4 minutes without moving until a deep golden crust forms on the bottom."),
            ("Flip & Baste with Herb Butter", "Carefully flip cod with a fish spatula. Reduce heat to medium. Drop in unsalted butter, smashed garlic, capers, lemon slices, and thyme sprigs. As butter foams, tilt pan and spoon hot garlic butter continuously over the fish for 3 minutes until fish flakes easily with a fork."),
            ("Sauté Zucchini Ribbons", "Transfer cooked cod to a warm plate. Add the shaved zucchini ribbons directly into the hot pan drippings. Toss with tongs for 90 seconds until tender-crisp and glistening."),
            ("Plate & Serve", "Nestle sautéed zucchini ribbons onto plates. Crown with the golden pan-seared cod loins, spoon over the pan juices, capers, and lemon slices. Scatter fresh chopped parsley on top and serve immediately!")
        ],
        "pro_tip_title": "Elena’s Fish Spatula Essential",
        "pro_tip": "If you don't own a thin, flexible metal fish spatula, treat yourself to one! A thick plastic spatula will push, crush, and break delicate cod flakes when you try to flip them. A thin metal fish spatula slides effortlessly beneath the caramelized crust without disturbing the fish.",
        "faqs": [
            ("Can I use frozen cod loins?", "Yes! Thaw completely in the refrigerator, and press firmly between multiple layers of paper towels to extract surface moisture before searing."),
            ("What can I substitute for capers?", "Pitted green Castelvetrano olives or kalamata olives chopped small provide that same wonderful salty, briny burst of Mediterranean flavor."),
            ("Is this dish keto and gluten-free?", "Yes! It contains only 6g total carbs and 34g clean lean protein, making it naturally keto, low-carb, and gluten-free.")
        ],
        "wiki_entities": [
            ("Cod as food", "https://en.wikipedia.org/wiki/Cod_as_food"),
            ("Zucchini", "https://en.wikipedia.org/wiki/Zucchini"),
            ("Beurre noisette", "https://en.wikipedia.org/wiki/Beurre_noisette")
        ],
        "pinterest": {
            "board": "Healthy Seafood Dinners / Low Carb Dinners",
            "title": "15-Minute Pan-Seared Garlic Herb Butter Cod with Zucchini Ribbons",
            "desc": "Crispy golden wild cod loins basted in foaming garlic lemon herb butter over tender sautéed zucchini ribbons in 15 minutes! Clean, elegant restaurant dinner. Pin it now!",
            "tags": "#pansearedcod #codrecipe #15minutedinner #seafooddinner #zucchiniribbons #lowcarbdinner #healthyrecipes"
        }
    },
    {
        "slug": "20-minute-french-dijon-chicken-meatballs",
        "title": "20-Minute Creamy French Dijon Tarragon Chicken Meatball Skillet",
        "headline": "20-Minute Creamy French Dijon Tarragon Chicken Meatball Skillet",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/french-dijon-chicken-meatballs.jpg",
        "image_file": "french-dijon-chicken-meatballs.jpg",
        "excerpt": "Tender golden seared ground chicken meatballs simmering in a velvety French Dijon white wine and fresh tarragon cream sauce in 20 minutes.",
        "description": "Parisian bistro elegance on a weeknight: juicy seared chicken meatballs simmered in a luscious white wine Dijon mustard cream sauce with fresh anise-scented tarragon.",
        "keywords": "dijon chicken meatballs, french tarragon chicken, 20 minute skillet dinner, one pot chicken meatballs, creamy dijon sauce, easy gourmet dinner",
        "prepTime": "PT6M",
        "cookTime": "PT14M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "French Bistro / Modern European",
        "calories": "460 kcal",
        "protein": "35g",
        "fat": "26g",
        "carbs": "16g",
        "fiber": "1g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "174",
        "quick_answer": "To make 20-minute creamy French Dijon tarragon chicken meatballs, mix 1.25 lbs lean ground chicken with 1/4 cup panko, 1 lightly beaten egg, 2 minced garlic cloves, 1 tbsp chopped fresh tarragon, 1/2 tsp salt, and 1/4 tsp pepper; gently roll into 12 meatballs. Heat 1 tbsp olive oil and 1 tbsp butter in a wide skillet over medium-high heat. Sear meatballs for 5 minutes until golden brown on all sides; transfer to a plate. Deglaze the skillet with 1/3 cup dry white wine (or chicken broth), scraping up browned fond. Whisk in 2 tbsp smooth Dijon mustard, 1 tbsp whole-grain mustard, 3/4 cup heavy cream, and 1/2 cup chicken broth. Return meatballs to the skillet, bring to a gentle simmer, and cook for 6 minutes until cooked through (165°F) and sauce thickens into velvet. Stir in 2 tbsp fresh tarragon and serve with egg noodles or buttered potatoes.",
        "takeaways": [
            ("Two-Mustard French Balance", "Combining smooth Dijon for sharp silkiness with whole-grain mustard for rustic pop gives the sauce genuine Parisian bistro complexity."),
            ("Fresh Tarragon Pairing", "Fresh French tarragon has delicate sweet anise and herbal pepper notes that cut through the richness of heavy cream and poultry."),
            ("White Wine Pan Fond Deglaze", "Deglazing the skillet with dry white wine lifts the caramelized chicken juices, infusing gentle acidity and restaurant depth.")
        ],
        "matrix_title": "Mustard Variety Role in French Skillet Sauces",
        "matrix_headers": ["Mustard Type", "Pungency / Acidity", "Texture Contribution", "Cream Stability", "Verdict"],
        "matrix_rows": [
            ["Smooth Dijon (Maille)", "Sharp, bright & clean", "Silky emulsion base", "Locks cream together", "Indispensable Foundation (Recommended)"],
            ["Whole Grain / Moutarde à l'Ancienne", "Mellow & rustic", "Satisfying mustard seed pop", "High stability", "Essential Texture Partner (Recommended)"],
            ["Yellow American Mustard", "Vinegar forward", "Thin", "Tends to taste sour with cream", "Avoid in French sauces"],
            ["Honey Mustard", "Sweet", "Syrupy", "Masks herbal notes", "Too sweet for tarragon"]
        ],
        "ingredients": [
            "1.25 lbs lean ground chicken (or ground turkey)",
            "1/4 cup panko breadcrumbs",
            "1 large egg, lightly beaten",
            "3 cloves fresh garlic, minced (divided)",
            "2 tbsp fresh tarragon leaves, finely chopped (divided)",
            "1 tbsp extra virgin olive oil",
            "1 tbsp unsalted butter",
            "1/3 cup dry white wine (Sauvignon Blanc or Chardonnay) or chicken broth",
            "1/2 cup low-sodium chicken broth",
            "3/4 cup heavy whipping cream",
            "2 tbsp smooth Dijon mustard",
            "1 tbsp whole-grain Dijon mustard",
            "1/2 tsp kosher salt & 1/2 tsp freshly cracked black pepper",
            "Buttered egg noodles or steamed baby potatoes, for serving"
        ],
        "instructions": [
            ("Mix & Shape Chicken Meatballs", "In a mixing bowl, combine ground chicken, panko, beaten egg, half the minced garlic, 1 tbsp chopped tarragon, 1/2 tsp salt, and pepper. Mix gently until just combined. Roll into 12 meatballs with damp hands."),
            ("Sear Meatballs to Golden Brown", "Heat olive oil and butter in a large skillet over medium-high heat. Add meatballs and sear undisturbed for 2.5 minutes, turn and sear for another 2.5 minutes until browned on the exterior. Transfer meatballs to a plate."),
            ("Deglaze Pan with White Wine", "Pour dry white wine into the hot skillet, scraping up all browned savory bits from the bottom with a wooden spoon for 60 seconds until liquid reduces by half."),
            ("Build Dijon Cream Sauce", "Whisk in chicken broth, heavy cream, smooth Dijon mustard, whole-grain mustard, and remaining minced garlic. Bring to a gentle bubbling simmer."),
            ("Simmer & Finish", "Return the browned meatballs to the simmering sauce. Reduce heat to medium-low and cook uncovered for 6 to 7 minutes until meatballs reach 165°F and the sauce thickens into a glossy velvet glaze. Remove from heat, fold in remaining fresh tarragon, and serve over buttered egg noodles!")
        ],
        "pro_tip_title": "Elena’s Fresh Tarragon Mandate",
        "pro_tip": "If possible, always use fresh French tarragon instead of dried! Dried tarragon loses its delicate licorice-sweet aromatics and turns dusty. Fresh tarragon has glossy green leaves that release pure French bistro magic when folded into hot cream right at the end.",
        "faqs": [
            ("Can I make this without alcohol?", "Yes! Simply replace the white wine with chicken broth plus 1 teaspoon of fresh lemon juice or white wine vinegar for acidity."),
            ("Can I use ground pork or veal?", "Yes! A blend of pork and chicken or pork and veal is classic in French and Belgian cuisine and produces extraordinarily juicy meatballs."),
            ("How do I store leftovers?", "Store meatballs and Dijon sauce in an airtight container in the fridge for up to 4 days. Reheat gently in a skillet over low heat with a splash of broth.")
        ],
        "wiki_entities": [
            ("Dijon mustard", "https://en.wikipedia.org/wiki/Dijon_mustard"),
            ("Tarragon", "https://en.wikipedia.org/wiki/Tarragon"),
            ("Meatball", "https://en.wikipedia.org/wiki/Meatball")
        ],
        "pinterest": {
            "board": "French Recipes / Cozy Skillet Dinners",
            "title": "20-Minute Creamy French Dijon Tarragon Chicken Meatballs",
            "desc": "Tender golden chicken meatballs simmering in a luxurious French white wine Dijon cream sauce with fresh tarragon in 20 minutes! Easy Parisian bistro dinner. Pin it now!",
            "tags": "#dijonchicken #chickenmeatballs #frenchfood #20minutedinner #onepotmeals #comfortfood #easyrecipes"
        }
    },
    {
        "slug": "15-minute-cantonese-black-pepper-beef",
        "title": "15-Minute Sizzling Cantonese Black Pepper Beef and Onion Skillet",
        "headline": "15-Minute Sizzling Cantonese Black Pepper Beef and Onion Stir-Fry",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/cantonese-black-pepper-beef.jpg",
        "image_file": "cantonese-black-pepper-beef.jpg",
        "excerpt": "Tender caramelized flank steak strips, charred sweet onions, and crisp bell peppers coated in a dark, glossy, intensely aromatic Cantonese black pepper sauce in 15 minutes.",
        "description": "Authentic banquet-style Chinese takeout at home in 15 minutes: sizzling flank steak tossed in coarse cracked black pepper, oyster sauce, Shaoxing wine, and garlic with charred onions.",
        "keywords": "cantonese black pepper beef, black pepper steak stir fry, 15 minute beef dinner, easy chinese stir fry, quick wok beef, banquet black pepper beef",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Cantonese / Chinese Wok",
        "calories": "470 kcal",
        "protein": "36g",
        "fat": "21g",
        "carbs": "31g",
        "fiber": "3g",
        "sodium": "710mg",
        "ratingValue": "4.9",
        "reviewCount": "197",
        "quick_answer": "To make 15-minute Cantonese black pepper beef, slice 1.25 lbs flank steak thinly against the grain and toss with 1 tbsp soy sauce, 1 tbsp Shaoxing cooking wine (or dry sherry), 1 tsp sesame oil, and 1 tbsp cornstarch. In a small bowl, whisk 2.5 tbsp oyster sauce, 1.5 tbsp low-sodium soy sauce, 1 tsp dark soy sauce, 1 tbsp sugar, 1.5 tsp coarsely cracked black pepper, and 3 tbsp beef broth or water. Heat 1.5 tbsp high-smoke point oil in a large wok over high heat. Sear beef strips undisturbed for 2 minutes until deeply charred, flip and sear for 1 minute, then transfer to a plate. Add 1 tbsp oil, 1 sliced yellow onion, and 1 sliced green bell pepper; stir-fry for 2 minutes until blistered. Return beef to wok, pour in black pepper sauce, and toss vigorously for 60 seconds until a dark glossy glaze coats every bite. Serve over steamed jasmine rice.",
        "takeaways": [
            ("Freshly Cracked Coarse Peppercorns", "Pre-ground fine table pepper tastes dusty; crushing whole black peppercorns coarsely in a mortar or pepper mill releases aromatic essential oils that create that signature sizzling steakhouse warmth."),
            ("Velveting for Ultra-Tender Steak", "Cornstarch and Shaoxing wine create a protective gelatinous shield that prevents meat fibers from seizing under 500°F wok heat."),
            ("Blistered Onion Sweetness", "Charring yellow onion petals in the screaming hot wok brings out sweet sugars that balance the pungent cracked black pepper.")
        ],
        "matrix_title": "Pepper Texture Impact on Cantonese Stir-Fry Sauces",
        "matrix_headers": ["Pepper Grind", "Aroma & Heat", "Visual Appeal", "Sauce Integration", "Verdict"],
        "matrix_rows": [
            ["Coarse Butcher's Grind (Fresh)", "Explosive, warm & floral", "Glistening black pepper flecks", "Clings to glossy glaze", "Authentic Banquet Standard (Recommended)"],
            ["Mortar & Pestle Crushed", "Intense burst of heat", "Rustic coarse chunks", "Great mouthfeel", "Excellent traditional technique"],
            ["Fine Pre-Ground Pepper", "Muted & dusty", "Dull grey color", "Makes sauce muddy", "Avoid for black pepper beef"],
            ["White Peppercorns", "Fermented sharp heat", "Invisible", "Different flavor profile", "Best for soups, not beef"]
        ],
        "ingredients": [
            "1.25 lbs flank steak, thinly sliced across the grain into 2-inch strips",
            "1 tbsp cornstarch",
            "1 tbsp Shaoxing rice wine (or dry sherry)",
            "2.5 tbsp high-heat oil (avocado or peanut oil, divided)",
            "1 medium yellow onion, cut into 1-inch petals",
            "1 green bell pepper, cut into 1-inch squares",
            "4 cloves fresh garlic, minced",
            "1 tbsp fresh ginger, grated",
            "2.5 tbsp premium oyster sauce (such as Lee Kum Kee)",
            "1.5 tbsp low-sodium soy sauce",
            "1 tsp dark soy sauce (for rich mahogany color)",
            "1 tbsp brown sugar",
            "1.5 tsp freshly cracked coarse black pepper",
            "3 tbsp low-sodium beef broth or water",
            "Steamed white jasmine rice, for serving"
        ],
        "instructions": [
            ("Velvet the Flank Steak", "Slice flank steak across the grain into thin strips. In a mixing bowl, toss beef with cornstarch, Shaoxing wine, 1 tbsp soy sauce, and 1 tsp oil until glossy and evenly coated. Set aside for 5 minutes."),
            ("Mix Cantonese Black Pepper Sauce", "In a small bowl, whisk together oyster sauce, remaining soy sauce, dark soy sauce, brown sugar, cracked black pepper, and beef broth until sugar dissolves."),
            ("Wok-Sear the Beef", "Heat 1.5 tbsp oil in a carbon steel wok or heavy cast iron skillet over high heat until wisps of smoke appear. Add beef in a single layer. Let sear completely undisturbed for 2 full minutes to achieve deep wok-hei caramelization. Flip and toss for 60 seconds until just browned. Transfer beef to a plate."),
            ("Stir-Fry Onions & Peppers", "Add remaining 1 tbsp oil to the smoking wok. Add onion petals and green bell pepper squares. Stir-fry over high heat for 2 minutes until edges are blistered and lightly charred. Add minced garlic and ginger; toss for 30 seconds."),
            ("Glaze & Serve", "Return seared beef and resting juices to the wok. Pour in the black pepper sauce mixture. Stir-fry vigorously for 60 seconds as the sauce bubbles, thickens, and lacquers every strip of steak in a dark, glossy glaze. Serve immediately over hot jasmine rice!")
        ],
        "pro_tip_title": "Elena’s Mortar & Pestle Coarse Grind",
        "pro_tip": "For genuine Chinese banquet flavor, put 1.5 teaspoons of whole black peppercorns in a mortar and pestle and crush them coarsely (or smash them in a baggie with the bottom of a heavy skillet). You want crackled bits of peppercorn rather than dust. When they hit the hot oyster sauce, the oils bloom into an intoxicating, spicy-warm restaurant aroma.",
        "faqs": [
            ("What can I substitute for Shaoxing wine?", "Dry sherry, dry white wine, or mirin (reduce sugar by 1/2 tsp) make excellent direct substitutes."),
            ("Can I make this with chicken or tofu?", "Yes! Boneless chicken thighs or firm pressed tofu cubes work fantastically with the exact same marinade and cooking times."),
            ("How do I prevent beef from getting chewy?", "Always slice strictly against (perpendicular to) the visible grain of the flank steak, and do not cook the beef past 3 minutes total in the wok.")
        ],
        "wiki_entities": [
            ("Black pepper beef", "https://en.wikipedia.org/wiki/Black_pepper_beef"),
            ("Cantonese cuisine", "https://en.wikipedia.org/wiki/Cantonese_cuisine"),
            ("Wok", "https://en.wikipedia.org/wiki/Wok")
        ],
        "pinterest": {
            "board": "Quick Asian Dinners / Wok Stir-Fry Recipes",
            "title": "15-Minute Sizzling Cantonese Black Pepper Beef and Onion Skillet",
            "desc": "Tender caramelized flank steak strips, charred onions, and bell peppers in a dark glossy black pepper oyster sauce in 15 minutes! Authentic Chinese takeout at home. Pin it now!",
            "tags": "#blackpepperbeef #cantonesefood #15minutedinner #beefstirfry #chinesetakeout #wokcooking #easyrecipes"
        }
    },
    {
        "slug": "20-minute-creamy-roasted-red-pepper-rigatoni",
        "title": "20-Minute Creamy Roasted Red Pepper and Burrata Rigatoni",
        "headline": "20-Minute Creamy Roasted Red Pepper Rigatoni with Fresh Burrata",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/creamy-roasted-red-pepper-rigatoni.jpg",
        "image_file": "creamy-roasted-red-pepper-rigatoni.jpg",
        "excerpt": "Large tubular rigatoni pasta coated in a silky, vibrant orange-red roasted red pepper and garlic cream sauce, crowned with creamy torn Italian burrata cheese in 20 minutes.",
        "description": "Vibrant, silky Italian comfort food in 20 minutes: al dente rigatoni coated in a sweet roasted bell pepper, garlic, and parmesan cream sauce, topped with fresh torn burrata cheese and basil.",
        "keywords": "roasted red pepper pasta, burrata rigatoni, 20 minute pasta, creamy red pepper sauce, vegetarian pasta recipe, easy weeknight pasta",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian / Vegetarian Comfort",
        "calories": "490 kcal",
        "protein": "18g",
        "fat": "22g",
        "carbs": "56g",
        "fiber": "4g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "188",
        "quick_answer": "To make 20-minute creamy roasted red pepper and burrata rigatoni, boil 10 oz rigatoni in salted water until al dente (save 1 cup starchy pasta water before draining). While pasta cooks, blend one 12-oz jar of drained roasted red peppers, 1/2 cup heavy cream, 1/2 cup grated parmesan cheese, 3 peeled garlic cloves, and 1/2 tsp salt in a blender until silky and smooth (30 seconds). Melt 1 tbsp butter and 1 tbsp olive oil in a wide skillet over medium heat, pour in the blended red pepper puree, and simmer for 3 minutes until bubbling and thickened. Toss the drained hot rigatoni into the sauce with a splash of pasta water until every tube is coated. Divide into bowls, top each with a fresh ball of burrata cheese torn open to reveal the creamy stracciatella, fresh basil, and cracked black pepper.",
        "takeaways": [
            ("Jarred Roasted Pepper Blender Hack", "Using jarred roasted bell peppers eliminates 40 minutes of pepper roasting and peeling, blending into an intensely sweet, smoky sauce in 30 seconds."),
            ("Rigatoni Ridges & Tubes", "The deep ridges (rigati) and wide hollow interior of rigatoni capture and hold the thick, velvety roasted pepper cream inside and out."),
            ("Torn Cold Burrata Contrast", "The warm pasta melts the cool, buttery stracciatella center of fresh burrata, creating an opulent two-tone sauce experience on your fork.")
        ],
        "matrix_title": "Pasta Shape Performance in Roasted Red Pepper Cream",
        "matrix_headers": ["Pasta Shape", "Sauce Adhesion", "Internal Cavity Hold", "Al Dente Chew", "Verdict"],
        "matrix_rows": [
            ["Rigatoni (Mezze Rigatoni)", "Superior (heavy ridges)", "Cavity fills with rich sauce", "Hearty & toothsome", "Absolute Best Pairing (Recommended)"],
            ["Paccheri / Calamarata", "Excellent", "Large hollow pockets", "Chewy & dense", "Upscale Italian trattoria feel"],
            ["Penne Rigate", "Good", "Moderate fill", "Standard chew", "Reliable pantry standby"],
            ["Spaghetti / Linguine", "Moderate coating", "Zero internal fill", "Slurpy", "Better for thin oil sauces"]
        ],
        "ingredients": [
            "10 oz dried rigatoni pasta (or mezze rigatoni)",
            "1 jar (12 oz) roasted red bell peppers, drained",
            "1/2 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "3 cloves fresh garlic, peeled",
            "1 tbsp unsalted butter & 1 tbsp olive oil",
            "1/4 tsp crushed red pepper flakes",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper",
            "2 fresh balls (4 oz each) Italian burrata cheese, room temperature",
            "1/2 cup fresh basil leaves, torn",
            "Extra virgin olive oil for drizzling"
        ],
        "instructions": [
            ("Boil Rigatoni", "Bring a large pot of salted water to a rolling boil. Add rigatoni and cook until al dente according to package instructions (about 10–11 minutes). Before draining, ladle out 1 cup of hot starchy pasta cooking water. Drain pasta."),
            ("Blend Velvety Red Pepper Sauce", "In a blender or food processor, combine drained roasted red peppers, heavy cream, grated parmesan, raw garlic cloves, salt, black pepper, and red pepper flakes. Blend on high for 30 to 45 seconds until completely silky and bright orange-red."),
            ("Simmer the Sauce", "Melt butter and olive oil in a wide deep skillet over medium heat. Pour in the blended red pepper sauce. Bring to a gentle bubbling simmer for 3 minutes, stirring occasionally as the sauce thickens and aromas bloom."),
            ("Toss Rigatoni in Sauce", "Add the hot drained rigatoni directly into the simmering sauce. Toss with tongs or a spoon for 1 to 2 minutes, adding a splash (about 1/4 cup) of reserved pasta water as needed until every tube is lacquered in a glossy cream coating."),
            ("Crown with Burrata & Serve", "Divide hot pasta among shallow bowls. Place a half ball (or whole ball) of fresh burrata on top of each serving. Gently tear the burrata open with two forks to let the creamy stracciatella spill over the warm rigatoni. Garnish with fresh basil, cracked pepper, and a swirl of olive oil!")
        ],
        "pro_tip_title": "Elena’s Room-Temperature Burrata Secret",
        "pro_tip": "Never serve burrata straight from the cold refrigerator! Take your burrata out of the fridge 20 minutes before cooking. When burrata is at room temperature, its sweet cream center flows out luxuriously like liquid silk over the hot rigatoni, rather than sitting like a cold heavy lump.",
        "faqs": [
            ("Can I make this dairy-free / vegan?", "Yes! Blend the roasted red peppers with 1/2 cup raw soaked cashews and vegetable broth instead of heavy cream, and top with vegan almond ricotta or avocado!"),
            ("Can I add Italian sausage or chicken?", "Yes! Brown 1/2 lb of sweet Italian sausage or seared chicken breast slices in the skillet before adding the blended sauce for an incredible meaty variation."),
            ("How do I store and reheat leftovers?", "Store leftover pasta without burrata in an airtight container for up to 4 days. Reheat gently on the stove with a splash of milk or water, and top with fresh burrata right before serving.")
        ],
        "wiki_entities": [
            ("Rigatoni", "https://en.wikipedia.org/wiki/Rigatoni"),
            ("Burrata", "https://en.wikipedia.org/wiki/Burrata"),
            ("Roasted pepper", "https://en.wikipedia.org/wiki/Roasted_pepper")
        ],
        "pinterest": {
            "board": "Pasta Recipes / Vegetarian Italian Dinners",
            "title": "20-Minute Creamy Roasted Red Pepper and Burrata Rigatoni",
            "desc": "Rigatoni tubes in a silky sweet roasted red pepper cream sauce crowned with creamy torn burrata cheese and fresh basil in 20 minutes! Luxurious weeknight dinner. Save the recipe!",
            "tags": "#burratapasta #roastedredpepper #rigatoni #20minutemeals #vegetariandinner #pasta #easyrecipes"
        }
    },
    {
        "slug": "15-minute-maple-dijon-pork-chops",
        "title": "15-Minute Pan-Seared Crispy Maple Dijon Mustard Pork Chops",
        "headline": "15-Minute Pan-Seared Maple Dijon Glazed Pork Chops with Apples",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-20",
        "image": "./assets/images/maple-dijon-pork-chops.jpg",
        "image_file": "maple-dijon-pork-chops.jpg",
        "excerpt": "Juicy, caramelized pan-seared pork chops with a deep golden crust, basted in a bubbling pure maple syrup, whole-grain Dijon mustard, and rosemary butter glaze in 15 minutes.",
        "description": "Sweet, savory autumn comfort in 15 minutes: tender seared pork chops glazed in pure maple syrup, whole-grain Dijon mustard, fresh rosemary, and caramelized apple wedges in a cast iron skillet.",
        "keywords": "maple dijon pork chops, 15 minute pork chops, skillet pork chops with glaze, easy weeknight pork chops, honey dijon pork, autumn skillet dinner",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American / Farmhouse Autumn",
        "calories": "460 kcal",
        "protein": "38g",
        "fat": "22g",
        "carbs": "26g",
        "fiber": "2g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "184",
        "quick_answer": "To make 15-minute pan-seared maple Dijon pork chops, season 4 boneless pork chops (approx. 6 oz each, 3/4-inch thick) with salt, black pepper, and garlic powder. Heat 1 tbsp olive oil and 1 tbsp butter in a cast iron skillet over medium-high heat. Sear pork chops undisturbed for 3.5 to 4 minutes until deeply browned and caramelized. Flip chops, add 1 thinly sliced Honeycrisp apple, 2 sprigs fresh rosemary, and 2 tbsp butter to the pan. Whisk 3 tbsp pure maple syrup, 2 tbsp whole-grain Dijon mustard, 1 tbsp smooth Dijon, and 1 tbsp apple cider vinegar; pour into the skillet. Baste pork chops with the bubbling sweet-savory glaze for 3 minutes until internal temperature reaches 145°F. Rest for 3 minutes before serving with glazed apple slices.",
        "takeaways": [
            ("Pork Chop Thickness Sweet Spot", "3/4-inch thick boneless chops develop a deep, crunchy seared crust in 3.5 minutes per side while keeping the interior succulent and tender at 145°F."),
            ("Pure Maple Syrup Caramelization", "Real Grade A maple syrup contains complex woodsy notes that reduce with Dijon mustard into a glossy, finger-licking pan glaze."),
            ("Tart Apple Wedge Sauté", "Thinly sliced Honeycrisp or Granny Smith apples cook directly in the pork drippings, soaking up the maple mustard glaze for the ultimate autumn pairing.")
        ],
        "matrix_title": "Pork Chop Cut Suitability for High-Speed Skillets",
        "matrix_headers": ["Pork Chop Cut", "Thickness", "Juiciness / Tenderness", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Boneless Pork Loin Chops", "3/4 inch", "Lean & juicy at 145°F", "7–8 minutes", "Fast Weeknight Favorite (Recommended)"],
            ["Bone-In Rib Chops", "1 inch", "Extra juicy near bone", "9–10 minutes", "Outstanding flavor & presentation"],
            ["Thin Center Cut Chops", "1/4 inch", "Easily overcooks", "3–4 minutes", "Watch timer like a hawk"],
            ["Thick Cut Heritage Chops", "1.5–2 inches", "Ultra-succulent", "15+ minutes", "Requires oven finishing"]
        ],
        "ingredients": [
            "4 boneless pork loin chops (approx. 6 oz each, 3/4-inch thick)",
            "1 tbsp extra virgin olive oil",
            "3 tbsp unsalted butter (divided)",
            "1 medium Honeycrisp or Granny Smith apple, cored and cut into thin wedges",
            "3 tbsp pure Grade A maple syrup",
            "2 tbsp whole-grain Dijon mustard",
            "1 tbsp smooth Dijon mustard",
            "1 tbsp apple cider vinegar",
            "2 sprigs fresh rosemary",
            "1/2 tsp garlic powder",
            "1 tsp kosher salt & 1/2 tsp freshly ground black pepper"
        ],
        "instructions": [
            ("Prep & Season Pork", "Pat pork chops completely dry with paper towels. Season both sides generously with kosher salt, black pepper, and garlic powder."),
            ("High-Heat Sear", "Heat olive oil and 1 tbsp butter in a large cast iron skillet over medium-high heat until shimmering hot. Add pork chops in a single layer. Sear undisturbed for 3.5 to 4 minutes until a deep, dark golden-brown crust forms on the bottom."),
            ("Flip & Add Apples & Rosemary", "Carefully flip pork chops. Scatter apple wedges around the chops in the skillet drippings. Add fresh rosemary sprigs and remaining 2 tbsp butter."),
            ("Glaze in Maple Dijon", "In a small cup, whisk together maple syrup, whole-grain mustard, smooth Dijon, and apple cider vinegar. Pour sauce into the bubbling skillet. Tilt pan and spoon the foaming maple mustard glaze over the chops continuously for 3 minutes until chops reach 145°F internal temperature and apples are tender-crisp."),
            ("Rest & Serve", "Remove skillet from heat. Let pork chops rest in the warm pan juices for 3 minutes to redistribute moisture. Plate pork chops topped with caramelized apple wedges and spoonfuls of the glossy pan glaze. Serve with mashed potatoes or green beans!")
        ],
        "pro_tip_title": "Elena’s 145°F Thermometer Mandate",
        "pro_tip": "The secret to restaurant-juicy pork chops is pulling them off the heat at exactly 145°F on an instant-read meat thermometer! Overcooking pork to 165°F squeezes out all natural moisture and turns chops dry and leathery. At 145°F with a 3-minute rest, pork is juicy, tender, and safe to enjoy.",
        "faqs": [
            ("Can I use honey instead of maple syrup?", "Yes! Honey works beautifully with Dijon mustard with the exact same measurements."),
            ("Can I use bone-in pork chops?", "Yes! Bone-in chops take about 1 to 2 minutes longer per side depending on thickness; use a meat thermometer to ensure 145°F near the bone."),
            ("What sides pair best with maple Dijon pork?", "Garlic roasted green beans, creamy mashed potatoes, buttered egg noodles, or a shaved Brussels sprout salad pair magnificently.")
        ],
        "wiki_entities": [
            ("Pork chop", "https://en.wikipedia.org/wiki/Pork_chop"),
            ("Maple syrup", "https://en.wikipedia.org/wiki/Maple_syrup"),
            ("Dijon mustard", "https://en.wikipedia.org/wiki/Dijon_mustard")
        ],
        "pinterest": {
            "board": "Quick Pork Dinners / Autumn Comfort Food",
            "title": "15-Minute Pan-Seared Crispy Maple Dijon Pork Chops",
            "desc": "Juicy seared pork chops with a deep caramelized crust, basted in a bubbling pure maple syrup and whole-grain Dijon butter glaze with apples in 15 minutes! Pin this easy fall dinner!",
            "tags": "#porkchops #mapledijon #15minutedinner #porkrecipes #fallfood #comfortfood #easyrecipes #quickdinner"
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 10) ===")
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
