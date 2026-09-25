import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "15-minute-honey-chipotle-chicken-tacos",
        "title": "15-Minute Crispy Honey Chipotle Chicken Tacos",
        "headline": "15-Minute Crispy Honey Chipotle Chicken Tacos (Smoky, Sweet & Cheesy)",
        "badge": "15-Minute Meals &bull; Street Tacos Fast",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners",
        "read_time": "15 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/honey-chipotle-chicken-tacos.jpg",
        "image_file": "honey-chipotle-chicken-tacos.jpg",
        "excerpt": "Juicy shredded chicken glazed in sweet and smoky honey chipotle adobo, pan-crisped in warm corn tortillas with bubbly melted pepper jack cheese, pickled red onions, and lime crema in 15 minutes.",
        "description": "Crispy pan-fried corn tortillas loaded with juicy shredded chicken simmered in sweet and smoky honey chipotle sauce, melted pepper jack cheese, tangy pickled red onions, and zesty lime crema.",
        "keywords": "honey chipotle chicken tacos, crispy chicken tacos, 15 minute taco dinner, easy weeknight tacos, cheesy chicken tacos, quick mexican dinner",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mexican-American",
        "calories": "460 kcal",
        "protein": "34g",
        "fat": "18g",
        "carbs": "42g",
        "fiber": "4g",
        "sodium": "620mg",
        "ratingValue": "4.9",
        "reviewCount": "152",
        "quick_answer": "To make 15-minute crispy honey chipotle chicken tacos, toss 3 cups cooked shredded chicken with 2 tbsp finely minced chipotle peppers in adobo, 2 tbsp honey, 1 tbsp tomato paste, 2 minced garlic cloves, and juice of half a lime in a warm skillet for 3 minutes. In a second hot skillet brushed with oil, place corn tortillas flat, sprinkle with pepper jack cheese and chicken, fold over, and pan-fry for 2 minutes per side until golden and crispy. Serve immediately with pickled onions, lime crema, and fresh cilantro.",
        "takeaways": [
            ("Rotisserie Chicken Shortcut", "Using pre-cooked shredded rotisserie chicken reduces meat prep time to zero while soaking up honey chipotle glaze instantly."),
            ("Tortilla Cheese Glue", "Melting pepper jack cheese directly on the corn tortilla creates a moisture barrier that guarantees a crispy exterior shell."),
            ("Sweet Chipotle Contrast", "The floral sweetness of honey balances the pungent smoke and fiery capsaicin of Mexican chipotle adobo.")
        ],
        "matrix_title": "Taco Shell Pan-Crisping Method Comparison",
        "matrix_headers": ["Cooking Method", "Exterior Crispness", "Cheese Melt", "Cleanup", "Verdict"],
        "matrix_rows": [
            ["Skillet Pan-Fry (Fold-Over)", "Ultra-crisp & blistered", "Gooey & bubbly", "1 skillet", "Gold Standard Winner (Recommended)"],
            ["Sheet Pan Oven Bake", "Even crisp, slightly dry", "Melted thoroughly", "1 sheet pan", "Great for feeding 6+ people"],
            ["Air Fryer Basket", "Very crunchy shell", "Fast melt", "Small batch only", "Good for 2-person servings"],
            ["Microwave Warm", "Soft & pliable", "Uneven melt", "Zero crispness", "Not recommended for crispy tacos"]
        ],
        "ingredients": [
            "3 cups cooked shredded chicken breast or rotisserie chicken",
            "8 small yellow or white corn tortillas",
            "2 tbsp canned chipotle peppers in adobo sauce, finely minced",
            "2 tbsp pure wildflower honey",
            "1 tbsp double-concentrated tomato paste",
            "2 cloves garlic, finely minced",
            "1/2 tsp ground cumin & Mexican oregano",
            "1.5 cups shredded pepper jack or Monterey Jack cheese",
            "2 tbsp vegetable or avocado oil (for frying tortillas)",
            "1/3 cup sour cream or Mexican crema whisked with 1 tbsp lime juice",
            "1/3 cup quick pickled red onions",
            "1/4 cup fresh cilantro leaves, chopped",
            "Lime wedges, for serving"
        ],
        "instructions": [
            ("Simmer Honey Chipotle Chicken", "Heat a large skillet over medium heat. Add shredded chicken, minced chipotle peppers with adobo sauce, honey, tomato paste, minced garlic, cumin, oregano, and 2 tbsp water. Stir and cook for 3 minutes until chicken is hot, glossy, and evenly coated. Transfer chicken to a bowl."),
            ("Prep Tortillas in Skillet", "Wipe the skillet clean and heat 1 tbsp oil over medium-high heat. Place 2–3 corn tortillas flat in the hot pan. Cook for 30 seconds until pliable."),
            ("Fill & Fold Tacos", "Sprinkle a handful of shredded pepper jack cheese across each tortilla, then spoon 2 generous tablespoons of honey chipotle chicken over one half. Fold the tortilla in half using tongs, pressing down gently to form a taco."),
            ("Pan-Fry Until Crispy", "Cook undisturbed for 2 minutes until the bottom tortilla is deep golden and crisp. Flip carefully and fry the other side for 1–2 minutes until cheese is completely melted and bubbling at the edges. Transfer to a serving platter. Repeat with remaining tacos."),
            ("Garnish & Serve", "Open the crispy tacos slightly and garnish with pickled red onions, a drizzle of zesty lime crema, and fresh cilantro. Serve piping hot with lime wedges!")
        ],
        "pro_tip_title": "Elena’s Cheese-Barrier Crispness Trick",
        "pro_tip": "Never place warm saucy chicken directly against raw corn tortillas—they will split and turn to mush! Always lay down a layer of shredded pepper jack cheese FIRST on the warm tortilla before adding the chicken. The melting cheese creates a waterproof seal that keeps the tortilla shell audibly shatter-crisp while holding the juicy chicken inside.",
        "faqs": [
            ("How spicy is the chipotle adobo?", "With 2 tablespoons of minced chipotle, it has a warm medium kick that is tempered by the sweet honey and melted cheese. For mild tacos, use 1 tablespoon of adobo sauce without the chopped peppers."),
            ("Can I make this with flour tortillas?", "Yes! Flour tortillas fry up blistered, flaky, and golden, similar to mini quesadillas."),
            ("Can I use ground beef or turkey instead?", "Absolutely! Brown 1 lb ground beef or turkey, drain fat, and stir in the honey, chipotle, and seasonings.")
        ],
        "wiki_entities": [
            ("Taco", "https://en.wikipedia.org/wiki/Taco"),
            ("Chipotle", "https://en.wikipedia.org/wiki/Chipotle"),
            ("Corn tortilla", "https://en.wikipedia.org/wiki/Corn_tortilla")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Mexican Recipes",
            "title": "15-Minute Crispy Honey Chipotle Chicken Tacos Recipe (Street Taco Fast!)",
            "desc": "Crispy pan-fried tacos loaded with sweet smoky honey chipotle shredded chicken, melted pepper jack cheese, pickled red onions, and lime crema. Ready in 15 minutes! Save this viral weeknight dinner now!",
            "tags": "#chickentacos #crispytacos #15minutedinner #mexicanfood #taconight #easydinnerrecipes #rotisseriechicken"
        }
    },
    {
        "slug": "15-minute-egg-roll-in-a-bowl",
        "title": "15-Minute Sesame Ginger Egg Roll in a Bowl (Crack Slaw)",
        "headline": "15-Minute Sesame Ginger Egg Roll in a Bowl (Low-Carb Takeout Fast)",
        "badge": "15-Minute Meals &bull; Low-Carb Sensation",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/egg-roll-in-a-bowl.jpg",
        "image_file": "egg-roll-in-a-bowl.jpg",
        "excerpt": "Savory caramelized ground pork, shredded cabbage, carrots, and scallions stir-fried in ginger garlic soy sauce, drizzled with spicy sriracha mayo and crunchy wonton strips in 15 minutes.",
        "description": "All the savory, crave-worthy flavors of a crispy Asian egg roll without the deep-frying wrapper: ground pork, crunchy slaw, fresh ginger, garlic, sriracha mayo drizzle, and toasted sesame seeds in one pan.",
        "keywords": "egg roll in a bowl, crack slaw, 15 minute low carb dinner, keto egg roll bowl, easy ground pork dinner, quick asian stir fry",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Asian-American",
        "calories": "390 kcal",
        "protein": "28g",
        "fat": "22g",
        "carbs": "12g",
        "fiber": "4g",
        "sodium": "680mg",
        "ratingValue": "4.9",
        "reviewCount": "175",
        "quick_answer": "To make 15-minute egg roll in a bowl, brown 1 lb ground pork in a large skillet over medium-high heat with 1 tbsp sesame oil for 5 minutes, breaking it into small crumbles. Add 4 minced garlic cloves and 1 tbsp freshly grated ginger; cook 1 minute. Dump in a 14 oz bag of coleslaw mix (shredded cabbage and carrots) along with 3 tbsp soy sauce, 1 tbsp rice vinegar, and 1 tsp sriracha. Stir-fry for 3–4 minutes until cabbage is tender-crisp. Drizzle with sriracha mayo and top with scallions, sesame seeds, and crispy wonton strips.",
        "takeaways": [
            ("Coleslaw Bag Shortcut", "Using pre-shredded coleslaw mix eliminates 10 minutes of tedious cabbage chopping, delivering instant crunch and fiber."),
            ("High-Heat Slaw Wilt", "Stir-frying over high heat allows the cabbage to soften while retaining an audible, juicy crunch."),
            ("Sriracha Mayo Accent", "A zesty drizzle of spicy mayonnaise mirrors the rich decadence of fried takeout appetizers without the heavy grease.")
        ],
        "matrix_title": "Ground Meat Options for Egg Roll in a Bowl",
        "matrix_headers": ["Meat Option", "Flavor Authenticity", "Fat & Moisture", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Ground Pork", "Classic traditional egg roll flavor", "Rich & juicy", "5 minutes", "Gold Standard Winner (Recommended)"],
            ["Ground Turkey (93/7)", "Mild, takes sauce well", "Lean & tender", "5 minutes", "Best high-protein lean alternative"],
            ["Ground Chicken", "Light & savory", "Medium moisture", "5 minutes", "Fabulous mild substitute"],
            ["Plant-Based Crumbles", "Savory umami", "Varies by brand", "4 minutes", "Great vegetarian option"]
        ],
        "ingredients": [
            "1 lb lean ground pork (or ground turkey/chicken)",
            "1 bag (14–16 oz) classic tricolor coleslaw mix (shredded green/red cabbage & carrots)",
            "1 tbsp toasted sesame oil",
            "1 tbsp avocado or vegetable oil",
            "4 cloves garlic, finely minced",
            "1 tbsp fresh ginger, finely grated",
            "3 tbsp low-sodium soy sauce (or tamari/coconut aminos)",
            "1 tbsp rice vinegar",
            "1 tsp sriracha or chili garlic sauce",
            "1/2 tsp onion powder & white pepper",
            "3 scallions (green onions), thinly sliced",
            "1 tbsp toasted white sesame seeds",
            "2 tbsp spicy sriracha mayo (for drizzling)",
            "1/3 cup crispy fried wonton strips (optional crunch)"
        ],
        "instructions": [
            ("Brown the Meat", "Heat vegetable oil and sesame oil in a large deep skillet or wok over medium-high heat. Add ground pork, breaking it apart with a spatula. Cook undisturbed for 3 minutes to develop browned edges, then stir and cook 2 more minutes until no pink remains."),
            ("Add Aromatics", "Push pork slightly to the side of the skillet. Add minced garlic and grated ginger directly to the hot pan surface; stir-fry for 45 seconds until fragrant."),
            ("Dump Slaw & Sauce", "Add the entire bag of coleslaw mix. Pour in soy sauce, rice vinegar, sriracha, onion powder, and white pepper. Toss vigorously with tongs over medium-high heat for 3–4 minutes until cabbage begins to wilt but still maintains a crisp bite."),
            ("Finish & Garnish", "Remove skillet from heat. Drizzle the top generously with spicy sriracha mayo. Scatter fresh sliced scallions, toasted sesame seeds, and crispy wonton strips across the skillet."),
            ("Serve", "Serve piping hot straight from the skillet as a low-carb bowl, or spoon over steamed jasmine rice or quinoa!")
        ],
        "pro_tip_title": "Elena’s Tender-Crisp Cabbage Rule",
        "pro_tip": "Never overcook the cabbage into limp mush! The magic of an authentic egg roll is the contrasting crunch of the filling. Pull the pan off the heat while the cabbage ribbons still look vibrant green and have an audible snap when tasted. The residual heat of the cast-iron will finish cooking it to absolute perfection by the time you reach the table.",
        "faqs": [
            ("Can I make this strictly keto or gluten-free?", "Yes! For keto, omit the wonton strips and use coconut aminos or tamari instead of soy sauce. It comes out to under 8g net carbs per serving!"),
            ("Can I add extra vegetables?", "Yes! Sliced shiitake mushrooms, shredded zucchini, snap peas, or water chestnuts are fantastic additions."),
            ("How does it hold up for meal prep?", "Exceptionally well! Store in meal prep containers for up to 4 days in the fridge. Reheat in the microwave or skillet; the cabbage retains great texture.")
        ],
        "wiki_entities": [
            ("Egg roll", "https://en.wikipedia.org/wiki/Egg_roll"),
            ("Ground meat", "https://en.wikipedia.org/wiki/Ground_meat"),
            ("Sesame oil", "https://en.wikipedia.org/wiki/Sesame_oil")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Low-Carb Recipes",
            "title": "15-Minute Sesame Ginger Egg Roll in a Bowl Recipe (Better Than Takeout!)",
            "desc": "Savory caramelized ground pork, crunchy cabbage slaw, garlic, ginger, and sriracha mayo drizzle in one pan in 15 minutes! The ultimate low-carb weeknight dinner. Save this viral recipe now!",
            "tags": "#eggrollinabowl #crackslaw #15minutedinner #lowcarbrecipes #ketodinner #onepotmeals #asianstirfry"
        }
    },
    {
        "slug": "20-minute-creamy-spinach-stuffed-chicken",
        "title": "20-Minute Creamy Sun-Dried Tomato and Spinach Stuffed Chicken",
        "headline": "20-Minute Creamy Spinach and Mozzarella Stuffed Chicken (Juicy Skillet Masterpiece)",
        "badge": "30-Minute Meals &bull; High-Protein Comfort",
        "category": "30-Minute Meals",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/creamy-spinach-stuffed-chicken.jpg",
        "image_file": "creamy-spinach-stuffed-chicken.jpg",
        "excerpt": "Golden pan-seared chicken cutlets stuffed with gooey melted mozzarella, creamy ricotta, baby spinach, and sweet sun-dried tomatoes in a bubbling garlic butter pan sauce in 20 minutes.",
        "description": "Restaurant-worthy stuffed chicken made weeknight fast: tender chicken breasts packed with melted mozzarella, creamy ricotta, fresh spinach, and sun-dried tomatoes, seared in garlic herb pan juices.",
        "keywords": "stuffed chicken breast, spinach stuffed chicken, creamy mozzarella stuffed chicken, 20 minute chicken dinner, easy weeknight chicken, low carb skillet dinner",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian-American",
        "calories": "480 kcal",
        "protein": "44g",
        "fat": "26g",
        "carbs": "8g",
        "fiber": "2g",
        "sodium": "590mg",
        "ratingValue": "4.9",
        "reviewCount": "184",
        "quick_answer": "To make 20-minute creamy spinach stuffed chicken, mix 1/2 cup ricotta, 1/2 cup shredded mozzarella, 1 cup chopped baby spinach, 1/4 cup chopped sun-dried tomatoes, and 1 minced garlic clove. Cut a horizontal pocket into 4 chicken breasts and stuff with cheese filling; secure with toothpicks. Season with Italian herbs, paprika, salt, and pepper. Sear in 2 tbsp oil and 1 tbsp butter over medium heat for 6–7 minutes per side with the pan covered until chicken is golden brown, cheese is melted, and internal temp reaches 165°F. Spoon pan juices over cutlets and serve.",
        "takeaways": [
            ("Cheese Steam Pocket", "Stuffing the cheese filling inside thick chicken breasts steams the meat from the inside out, guaranteeing juicy, tender chicken without drying."),
            ("Toothpick Anchor Technique", "Two wooden toothpicks per cutlet seal the pocket edges and keep 95% of the molten cheese inside the chicken."),
            ("Pan-Cover Sear Method", "Covering the skillet during searing traps convective heat, cooking thick stuffed breasts through in just 14 minutes.")
        ],
        "matrix_title": "Cheese Fillings for Stuffed Chicken Breasts",
        "matrix_headers": ["Cheese Blend", "Melt Quality", "Moisture Level", "Richness", "Verdict"],
        "matrix_rows": [
            ["Mozzarella + Whole Milk Ricotta", "Gooey pull & velvety cream", "High (keeps chicken juicy)", "Balanced & luxurious", "Gold Standard Winner (Recommended)"],
            ["Cream Cheese + Parmesan", "Dense & rich creaminess", "Medium-High", "Very rich", "Great classic American alternative"],
            ["Crumbled Feta + Cream Cheese", "Tangy & briny melt", "Medium", "Sharp & bold", "Fabulous Mediterranean variation"],
            ["Cheddar Cheese Only", "Oily separation when baked", "Low", "Sharp", "Not recommended (leaks out of pocket)"]
        ],
        "ingredients": [
            "4 large boneless skinless chicken breasts (about 7–8 oz each)",
            "1/2 cup whole-milk ricotta cheese (or softened cream cheese)",
            "1/2 cup shredded low-moisture mozzarella cheese",
            "1 cup fresh baby spinach, finely chopped",
            "1/3 cup oil-packed sun-dried tomatoes, drained and finely chopped",
            "3 cloves garlic, minced (divided)",
            "1 tbsp Italian seasoning blend",
            "1 tsp smoked paprika",
            "2 tbsp extra virgin olive oil",
            "2 tbsp unsalted butter",
            "1/4 cup low-sodium chicken broth",
            "Fresh basil leaves & cracked black pepper",
            "8 wooden toothpicks"
        ],
        "instructions": [
            ("Mix Cheese Filling", "In a medium bowl, stir together ricotta cheese, shredded mozzarella, chopped baby spinach, chopped sun-dried tomatoes, 1 minced garlic clove, 1/2 tsp salt, and 1/4 tsp black pepper until well combined."),
            ("Cut Pockets & Stuff", "Pat chicken breasts dry. Lay flat and use a sharp knife to slice a horizontal pocket into the thick side of each breast, cutting about 3/4 of the way through (do not cut all the way). Spoon 2–3 tablespoons of cheese filling inside each pocket. Pin the openings shut with 2 toothpicks per breast."),
            ("Season Chicken Exterior", "Rub the outside of the chicken breasts with Italian seasoning, smoked paprika, 1 tsp salt, and 1/2 tsp pepper."),
            ("Sear in Skillet", "Heat olive oil and 1 tbsp butter in a large heavy skillet over medium heat. Add stuffed chicken breasts. Sear uncovered for 4 minutes until deeply golden. Flip carefully, reduce heat to medium-low, cover with a tight-fitting lid, and cook for 6–8 minutes until internal temperature registers 165°F."),
            ("Make Pan Jus & Serve", "Remove lid, slide in chicken broth, remaining 1 tbsp butter, and remaining minced garlic. Spoon simmering pan juices over the chicken for 1 minute. Discard toothpicks before serving, garnish with fresh basil, and serve immediately!")
        ],
        "pro_tip_title": "Elena’s Pocket Slicing Rule",
        "pro_tip": "Keep your knife blade parallel to the cutting board and press your non-cutting palm flat against the top of the chicken breast as you cut! Stop your blade about 1/2 inch from the back and side edges. Creating a deep internal envelope rather than a wide flap keeps all that luscious melted cheese trapped inside the meat rather than burning on the bottom of the pan.",
        "faqs": [
            ("How do I prevent the cheese from leaking out?", "Use toothpicks woven through the opening like safety pins, and avoid overstuffing beyond 3 tablespoons per breast."),
            ("Can I bake these in the oven instead?", "Yes! Sear in an oven-safe skillet for 3 minutes per side, then transfer to a 375°F oven for 12–15 minutes until 165°F."),
            ("What are the best side dishes?", "A crisp Caesar salad, garlic butter pasta, mashed potatoes, or roasted broccoli complement the rich cheese filling beautifully.")
        ],
        "wiki_entities": [
            ("Stuffed chicken", "https://en.wikipedia.org/wiki/Stuffed_chicken"),
            ("Mozzarella", "https://en.wikipedia.org/wiki/Mozzarella"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / Chicken Recipes",
            "title": "20-Minute Creamy Spinach and Mozzarella Stuffed Chicken Recipe (So Juicy!)",
            "desc": "Tender golden chicken breasts stuffed with melted mozzarella, creamy ricotta, spinach, and sun-dried tomatoes in a sizzling garlic herb pan sauce. Ready in 20 minutes! Save this dinner recipe now!",
            "tags": "#stuffedchicken #20minutedinner #creamychicken #lowcarbdinner #ketorecipes #easyweeknightdinner #chickenbreast"
        }
    },
    {
        "slug": "20-minute-sheet-pan-honey-mustard-pork-chops",
        "title": "20-Minute Sheet-Pan Honey Mustard Pork Chops and Roasted Asparagus",
        "headline": "20-Minute Sheet-Pan Honey Mustard Pork Chops (Juicy & Caramelized)",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/sheet-pan-honey-mustard-pork-chops.jpg",
        "image_file": "sheet-pan-honey-mustard-pork-chops.jpg",
        "excerpt": "Caramelized bone-in pork chops glazed in a sweet tangy honey Dijon rosemary sauce, roasted on one sheet pan with fresh asparagus spears and roasted baby potatoes in 20 minutes.",
        "description": "Tender juicy pork chops slathered in a tangy sweet honey Dijon rosemary glaze, roasted to golden perfection on a single baking sheet with tender asparagus and seasoned baby potatoes.",
        "keywords": "sheet pan pork chops, honey mustard pork chops, 20 minute pork dinner, easy sheet pan dinner, baked pork chops, weeknight pork recipes",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American Comfort",
        "calories": "450 kcal",
        "protein": "38g",
        "fat": "19g",
        "carbs": "28g",
        "fiber": "3g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "147",
        "quick_answer": "To make 20-minute sheet-pan honey mustard pork chops, preheat oven to 425°F (220°C). Whisk 3 tbsp Dijon mustard, 2 tbsp honey, 1 tbsp olive oil, 2 minced garlic cloves, 1 tsp chopped fresh rosemary, salt, and pepper. Arrange 4 bone-in or boneless pork chops and 1 lb trimmed asparagus on a parchment-lined baking sheet. Toss asparagus with 1 tbsp olive oil, and brush the honey mustard glaze generously over both sides of the pork chops. Roast for 14–16 minutes until pork reaches 145°F internal temperature, broiling the last 2 minutes for caramelized char.",
        "takeaways": [
            ("Dijon & Honey Glaze Lacquer", "High-heat roasting caramelizes honey sugars while Dijon mustard provides acidity that tenderizes pork cutlets."),
            ("145°F Internal Temp Rule", "Pulling pork at 145°F guarantees a juicy, tender, rosy interior rather than dry, overcooked pork."),
            ("Single Sheet Pan Convenience", "Synchronizing asparagus roasting with pork chop baking delivers dinner with zero multiple-pan sink cleanup.")
        ],
        "matrix_title": "Pork Chop Cuts for 20-Minute Sheet Pan Dinners",
        "matrix_headers": ["Pork Chop Cut", "Juiciness Level", "Caramelization", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Bone-in Center Cut (3/4-inch)", "Maximum moisture retention", "Deep roasted crust", "14–16 minutes", "Gold Standard Winner (Recommended)"],
            ["Boneless Pork Chops (1-inch)", "Lean & meaty", "Great glaze adhesion", "12–14 minutes", "Convenient & quick alternative"],
            ["Thick-Cut Rib Chops (1.5-inch)", "Ultra-juicy", "Caramelized edges", "20–24 minutes", "Slower, requires extra baking time"],
            ["Thin Breakfast Chops (1/4-inch)", "Dry quickly", "Fast sear", "6–8 minutes", "Not recommended for roasting"]
        ],
        "ingredients": [
            "4 bone-in or boneless pork chops (3/4-inch thick, about 7 oz each)",
            "1 lb fresh asparagus spears (woody ends snapped off)",
            "1/2 lb small baby creamer potatoes, halved (or pre-steamed)",
            "3 tbsp Dijon mustard (or coarse whole-grain mustard)",
            "2 tbsp pure clover honey",
            "2 tbsp extra virgin olive oil (divided)",
            "3 cloves garlic, finely minced",
            "1 tbsp fresh rosemary leaves, finely chopped",
            "1 tsp smoked paprika & onion powder",
            "Kosher salt & freshly cracked black pepper"
        ],
        "instructions": [
            ("Preheat Oven & Prep Sheet Pan", "Preheat oven to 425°F (220°C). Line a large rimmed baking sheet with parchment paper or heavy-duty foil."),
            ("Whisk Honey Mustard Glaze", "In a small bowl, whisk together Dijon mustard, honey, 1 tbsp olive oil, minced garlic, chopped rosemary, smoked paprika, 1 tsp salt, and 1/2 tsp black pepper until smooth and glossy."),
            ("Arrange Pork & Vegetables", "Place pork chops in the center of the baking sheet. Arrange asparagus spears and halved baby potatoes around the pork. Drizzle vegetables with remaining 1 tbsp olive oil and season with salt and pepper."),
            ("Brush Glaze Generously", "Brush half of the honey mustard glaze over the top and sides of the pork chops."),
            ("Roast & Caramelize", "Bake at 425°F for 10 minutes. Remove pan, brush remaining glaze over pork, and return to oven for 4–5 more minutes until an instant-read thermometer reads 145°F in the center. Switch to high broil for 90 seconds for bubbling caramelized edges."),
            ("Rest & Serve", "Rest pork chops on a warm platter for 3 minutes to allow juices to redistribute. Serve immediately with roasted asparagus and potatoes!")
        ],
        "pro_tip_title": "Elena’s 145°F Juicy Pork Rule",
        "pro_tip": "Forget the outdated advice to cook pork to 165°F! The USDA officially updated food safety guidelines to 145°F with a 3-minute rest. Pork cooked to 145°F maintains a delicate blush of pink in the center and is dripping with natural savory juices, completely shattering the myth of dry, chewy weeknight pork chops.",
        "faqs": [
            ("Can I use whole-grain mustard instead of Dijon?", "Yes! Whole-grain stone-ground mustard adds delightful popping texture and rustic flavor to the honey glaze."),
            ("Can I make this in the air fryer?", "Yes! Air fry pork chops at 390°F for 10–12 minutes, flipping and glazing halfway through."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 3 days. Reheat gently in a 325°F oven or covered skillet with a splash of broth so the meat doesn't dry out.")
        ],
        "wiki_entities": [
            ("Pork chop", "https://en.wikipedia.org/wiki/Pork_chop"),
            ("Dijon mustard", "https://en.wikipedia.org/wiki/Dijon_mustard"),
            ("Honey", "https://en.wikipedia.org/wiki/Honey")
        ],
        "pinterest": {
            "board": "Sheet Pan Meals / Quick Dinners",
            "title": "20-Minute Sheet-Pan Honey Mustard Pork Chops Recipe (Juicy & Easy!)",
            "desc": "Tender juicy bone-in pork chops slathered in sweet tangy honey Dijon rosemary glaze, roasted on one pan with fresh asparagus in 20 minutes! Save this easy weeknight dinner recipe now!",
            "tags": "#porkchops #sheetpanmeals #20minutedinner #honeymustard #bakedporkchops #easyweeknightdinner #dinnerideas"
        }
    },
    {
        "slug": "15-minute-garlic-butter-mushroom-gnocchi",
        "title": "15-Minute Creamy Garlic Butter Mushroom Gnocchi",
        "headline": "15-Minute Garlic Butter Mushroom Gnocchi (Rich Woodland Comfort)",
        "badge": "15-Minute Meals &bull; Cozy Vegetarian",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/garlic-butter-mushroom-gnocchi.jpg",
        "image_file": "garlic-butter-mushroom-gnocchi.jpg",
        "excerpt": "Golden skillet-toasted potato gnocchi tossed with deeply caramelized cremini mushrooms, minced garlic, fresh thyme, and a velvety white wine parmesan cream in 15 minutes.",
        "description": "Pan-seared potato dumplings crisped to golden perfection and enveloped in deeply browned mushrooms, aromatic thyme, foaming garlic butter, and aged parmesan.",
        "keywords": "mushroom gnocchi, garlic butter gnocchi, 15 minute gnocchi recipe, one skillet gnocchi, creamy mushroom pasta, easy vegetarian dinners",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian Comfort",
        "calories": "460 kcal",
        "protein": "12g",
        "fat": "22g",
        "carbs": "56g",
        "fiber": "4g",
        "sodium": "510mg",
        "ratingValue": "4.9",
        "reviewCount": "163",
        "quick_answer": "To make 15-minute garlic butter mushroom gnocchi, melt 2 tbsp butter with 1 tbsp olive oil in a large skillet over medium-high heat. Add 16 oz shelf-stable potato gnocchi straight from the pack (no pre-boiling needed); sauté undisturbed for 4 minutes until golden and crisp, then set aside. In the same skillet, melt 2 tbsp butter and sear 8 oz sliced cremini mushrooms undisturbed for 4 minutes until deeply browned. Add 4 minced garlic cloves and 1 tbsp fresh thyme; sauté 1 minute. Pour in 1/3 cup vegetable broth and 1/2 cup heavy cream, simmer 2 minutes, return gnocchi, and fold in 1/2 cup grated parmesan.",
        "takeaways": [
            ("Undisturbed Mushroom Sear", "Letting sliced mushrooms sit without stirring drives off moisture and caramelizes sugars into rich woodland fond."),
            ("Direct-to-Skillet Gnocchi", "Cooking vacuum-packed gnocchi directly in foaming butter creates a crispy shell while steaming the pillowy potato interior."),
            ("White Wine / Broth Deglaze", "Deglazing pan juices with dry wine or broth lifts savory mushroom fond into a velvety sauce.")
        ],
        "matrix_title": "Mushroom Variety Comparison for Creamy Gnocchi",
        "matrix_headers": ["Mushroom Variety", "Earthiness Level", "Moisture Content", "Texture Bite", "Verdict"],
        "matrix_rows": [
            ["Cremini / Baby Bella", "Rich, savory & earthy", "Medium", "Meaty & firm", "Gold Standard Everyday Choice (Recommended)"],
            ["Shiitake Mushrooms", "Deep woodland umami, woodsy", "Low-Medium", "Velvety & tender", "Exceptional gourmet flavor upgrade"],
            ["White Button Mushrooms", "Mild & delicate", "High (takes longer to brown)", "Soft", "Good budget pantry backup"],
            ["Chanterelle or Morels", "Nutty, peppery & decadent", "Low", "Delicate & meaty", "Luxury date-night choice"]
        ],
        "ingredients": [
            "16 oz shelf-stable or vacuum-packed potato gnocchi (uncooked)",
            "8 oz cremini (baby bella) mushrooms, cleaned and sliced 1/4-inch thick",
            "4 tbsp unsalted butter (divided)",
            "1 tbsp extra virgin olive oil",
            "4 cloves garlic, finely minced",
            "1 tbsp fresh thyme leaves (or 1 tsp dried thyme)",
            "1/3 cup dry white wine or low-sodium vegetable broth",
            "1/2 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "1/4 tsp crushed red pepper flakes",
            "Flaky sea salt & freshly cracked black pepper"
        ],
        "instructions": [
            ("Sear Gnocchi", "Heat 2 tbsp butter and 1 tbsp olive oil in a large 12-inch skillet over medium-high heat. Add uncooked gnocchi in a single layer. Cook undisturbed for 4 minutes until bottoms are deeply golden and crisp. Toss and sear 2 more minutes. Transfer gnocchi to a plate."),
            ("Caramelize Mushrooms", "In the same skillet, melt 1 tbsp butter over high heat. Add sliced mushrooms in an even layer. Cook completely undisturbed for 3–4 minutes until deeply browned on the bottom. Toss and cook 2 more minutes."),
            ("Sauté Aromatics", "Reduce heat to medium. Add remaining 1 tbsp butter, minced garlic, fresh thyme leaves, and red pepper flakes. Sauté for 45 seconds until fragrant without scorching garlic."),
            ("Deglaze & Simmer Sauce", "Pour in white wine (or broth), scraping up all the savory browned mushroom fond from the skillet bottom. Simmer for 1 minute until reduced by half. Stir in heavy cream and simmer 2 minutes until glossy and thickened."),
            ("Combine & Serve", "Return crisped gnocchi to the skillet. Toss gently for 1 minute over low heat until sauce clings to each dumpling. Remove from heat, fold in grated Parmigiano-Reggiano, and season with flaky sea salt and lots of cracked black pepper. Serve piping hot!")
        ],
        "pro_tip_title": "Elena’s Golden Mushroom Browning Rule",
        "pro_tip": "Never crowd or salt your mushrooms right away! Mushrooms are 90% water. If you stir constantly or salt them immediately, they release liquid and boil in their own juices. Let them sit motionless in a screaming-hot skillet with foaming butter for 4 full minutes. They will develop a deeply caramelized, savory brown crust that tastes like it came from a Michelin-star kitchen.",
        "faqs": [
            ("Can I make this dairy-free or vegan?", "Yes! Use olive oil or vegan butter, and substitute full-fat canned coconut milk or cashew cream for the heavy cream, finishing with nutritional yeast."),
            ("Can I add spinach or kale?", "Yes! Toss in 2 cups of baby spinach or chopped Tuscan kale during the final 60 seconds of simmering; it wilts beautifully into the cream sauce."),
            ("Can I use homemade or frozen gnocchi?", "Homemade or frozen gnocchi should be boiled for 2 minutes first until they float, then pan-seared in butter to develop that irresistible golden crust.")
        ],
        "wiki_entities": [
            ("Gnocchi", "https://en.wikipedia.org/wiki/Gnocchi"),
            ("Agaricus bisporus", "https://en.wikipedia.org/wiki/Agaricus_bisporus"),
            ("Parmigiano Reggiano", "https://en.wikipedia.org/wiki/Parmigiano_Reggiano")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / One-Pot Dinners",
            "title": "15-Minute Creamy Garlic Butter Mushroom Gnocchi Recipe (One-Pan Comfort!)",
            "desc": "Crispy pan-seared potato gnocchi tossed with caramelized cremini mushrooms, garlic butter, fresh thyme, and a velvety parmesan cream sauce in 15 minutes! Save this easy weeknight dinner recipe now!",
            "tags": "#mushroomgnocchi #15minutedinner #onepotmeals #gnocchirecipe #vegetariancomfortfood #easyrecipes #creamypasta"
        }
    },
    {
        "slug": "15-minute-creamy-tuscan-white-beans",
        "title": "15-Minute Creamy Tuscan Garlic White Bean and Tomato Skillet",
        "headline": "15-Minute Creamy Tuscan White Beans (Cozy Italian Skillet Supper)",
        "badge": "One-Pot Dinners &bull; 15 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all 30-minute-meals one-pot-dinners comfort-food",
        "read_time": "15 min cook",
        "date": "2026-09-25",
        "image": "./assets/images/creamy-tuscan-white-beans.jpg",
        "image_file": "creamy-tuscan-white-beans.jpg",
        "excerpt": "Plump creamy cannellini white beans simmered in a velvety garlic sun-dried tomato parmesan cream sauce with baby spinach, fresh basil, and toasted crusty bread in 15 minutes.",
        "description": "Rich Tuscan comfort made fast: tender cannellini beans simmered in a velvety parmesan garlic herb cream sauce with sweet sun-dried tomatoes and tender baby spinach, served with crusty bread.",
        "keywords": "tuscan white beans, creamy cannellini beans, 15 minute vegetarian dinner, one skillet white beans, easy pantry dinner, sun dried tomato cream beans",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Tuscan / Italian",
        "calories": "390 kcal",
        "protein": "15g",
        "fat": "18g",
        "carbs": "44g",
        "fiber": "9g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "158",
        "quick_answer": "To make 15-minute creamy Tuscan white beans, heat 1 tbsp olive oil and 2 tbsp butter in a large skillet over medium heat. Sauté 4 minced garlic cloves, 1/2 cup chopped oil-packed sun-dried tomatoes, and 1 tsp Italian herbs for 2 minutes. Add 2 cans (15 oz each) rinsed cannellini beans, 1/2 cup vegetable broth, and 1/2 cup heavy cream. Simmer for 5 minutes, lightly mashing a spoonful of beans to thicken. Stir in 3 cups baby spinach and 1/2 cup grated parmesan until wilted and velvety. Serve with toasted garlic sourdough.",
        "takeaways": [
            ("Pantry Bean Simplicity", "Canned cannellini beans provide instantaneous creaminess and rich plant protein without soaking or long boiling."),
            ("Natural Starch Thickener", "Mashing a small handful of beans directly into simmering cream creates a cohesive, spoon-coating gravy."),
            ("Sun-Dried Tomato Acid Balance", "Sweet and tart sun-dried tomatoes cut through rich dairy cream for an authentic Tuscan flavor profile.")
        ],
        "matrix_title": "Bean Selection for Tuscan Cream Skillets",
        "matrix_headers": ["Bean Variety", "Creaminess", "Skin Thickness", "Simmer Speed", "Verdict"],
        "matrix_rows": [
            ["Cannellini (White Kidney)", "Ultra-creamy & velvety", "Very thin & tender", "5 minutes", "Gold Standard Winner (Recommended)"],
            ["Great Northern Beans", "Soft & mild", "Thin", "5 minutes", "Excellent everyday alternative"],
            ["Navy Beans", "Small & firm", "Medium", "6–8 minutes", "Acceptable but smaller bite"],
            ["Chickpeas (Garbanzo)", "Chewy & dense", "Firm skin", "8–10 minutes", "Heartier, different texture profile"]
        ],
        "ingredients": [
            "2 cans (15 oz each) cannellini beans (white kidney beans), rinsed and drained",
            "1/2 cup oil-packed sun-dried tomatoes, drained and sliced (reserve 1 tbsp oil)",
            "4 cloves garlic, finely minced",
            "2 tbsp unsalted butter",
            "1 tbsp reserved sun-dried tomato oil (or extra virgin olive oil)",
            "1/2 cup low-sodium vegetable or chicken broth",
            "1/2 cup heavy whipping cream",
            "3 cups fresh baby spinach leaves",
            "1/2 cup freshly grated Parmigiano-Reggiano",
            "1 tsp Italian seasoning (oregano, basil, thyme)",
            "1/4 tsp crushed red pepper flakes",
            "Kosher salt & freshly cracked black pepper",
            "Crusty artisan sourdough or baguette slices (for dipping)"
        ],
        "instructions": [
            ("Sauté Aromatics in Tomato Oil", "In a large 12-inch skillet, melt butter with 1 tbsp reserved sun-dried tomato oil over medium heat. Add minced garlic, sliced sun-dried tomatoes, Italian seasoning, and red pepper flakes. Sauté for 2 minutes until fragrant and oil turns vibrant orange."),
            ("Simmer White Beans", "Add rinsed cannellini beans, vegetable broth, and heavy cream to the skillet. Stir to combine and bring to a gentle simmer over medium heat. Cook for 5 minutes, stirring occasionally."),
            ("Crush for Instant Creaminess", "Take the back of a wooden spoon or potato masher and lightly crush about 1/4 cup of the beans against the pan bottom. Stir into the simmering sauce to instantly create a velvety, thick gravy."),
            ("Fold Spinach & Cheese", "Reduce heat to low. Add fresh baby spinach and grated Parmigiano-Reggiano. Toss gently for 1–2 minutes until spinach is just wilted and cheese is completely melted into the sauce."),
            ("Season & Serve", "Season with a pinch of flaky sea salt and lots of freshly cracked black pepper. Spoon into shallow bowls and serve immediately with thick slices of toasted garlic sourdough bread for dipping!")
        ],
        "pro_tip_title": "Elena’s Bean Mash Emulsion Trick",
        "pro_tip": "You never need flour or cornstarch to thicken creamy bean dishes! Simply take the back of your wooden spoon and crush 15 to 20 cannellini beans directly against the bottom of your skillet. The released bean starch acts as an all-natural binding agent, turning the cream and broth into a luscious, glossy, restaurant-caliber sauce in seconds.",
        "faqs": [
            ("Can I add meat to this skillet?", "Yes! Brown 1/2 lb of mild or hot Italian ground sausage or crispy bacon before adding the aromatics for an incredible protein addition."),
            ("Can I make this dairy-free or vegan?", "Yes! Replace heavy cream with full-fat canned coconut milk or cashew cream, and swap the parmesan for nutritional yeast or vegan parmesan."),
            ("What can I do with leftovers?", "Store in an airtight container in the fridge for up to 4 days. Reheat in a saucepan over medium-low heat with a splash of broth. It makes an incredible warm lunch!")
        ],
        "wiki_entities": [
            ("Phaseolus vulgaris", "https://en.wikipedia.org/wiki/Phaseolus_vulgaris"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato"),
            ("Parmigiano Reggiano", "https://en.wikipedia.org/wiki/Parmigiano_Reggiano")
        ],
        "pinterest": {
            "board": "Quick Weeknight Dinners / One-Pot Dinners",
            "title": "15-Minute Creamy Tuscan Garlic White Beans Recipe (Cozy Skillet!)",
            "desc": "Tender cannellini beans simmered in a velvety garlic sun-dried tomato parmesan cream sauce with baby spinach, served with crusty bread for dipping. Ready in 15 minutes! Save this cozy dinner recipe now!",
            "tags": "#tuscanbeans #whitebeans #15minutedinner #onepotmeals #meatlessmonday #vegetarianrecipes #easydinnerrecipes"
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 3) ===")
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
