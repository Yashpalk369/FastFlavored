import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    {
        "slug": "20-minute-sheet-pan-chimichurri-steak-potatoes",
        "title": "20-Minute Sheet-Pan Crispy Garlic Chimichurri Steak and Baby Potatoes",
        "headline": "20-Minute Sheet-Pan Crispy Garlic Chimichurri Steak Bites and Baby Potatoes",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/sheet-pan-chimichurri-steak-potatoes.jpg",
        "image_file": "sheet-pan-chimichurri-steak-potatoes.jpg",
        "excerpt": "Tender, caramelized seared flank steak bites paired with golden, crispy halved baby potatoes on a single sheet pan, drizzled with vibrant emerald garlic herb chimichurri in 20 minutes.",
        "description": "Crispy roasted baby golden potatoes and juicy, deeply browned flank steak bites roasted on one sheet pan at 450°F, smothered in a scratch-made zesty chimichurri herb vinaigrette.",
        "keywords": "sheet pan steak and potatoes, chimichurri steak bites, 20 minute steak dinner, easy sheet pan suppers, garlic herb flank steak",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Argentine / American Steakhouse",
        "calories": "510 kcal",
        "protein": "38g",
        "fat": "26g",
        "carbs": "31g",
        "fiber": "4g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "178",
        "quick_answer": "To make 20-minute sheet-pan chimichurri steak and potatoes, microwave 1 lb halved baby gold potatoes for 3 minutes until fork-tender, then toss on a preheated baking sheet with 1 tbsp olive oil, salt, and pepper at 450°F (230°C) for 10 minutes. Cube 1.25 lbs flank or sirloin steak into 1-inch bites, season with smoked paprika and garlic powder, and add to the hot sheet pan. Roast for 5 to 6 minutes, switching to high broil for the final 90 seconds until steak edges are caramelized. Drizzle immediately with fresh chimichurri (finely chopped parsley, garlic, red wine vinegar, oregano, red pepper flakes, and olive oil).",
        "takeaways": [
            ("Pre-Steaming Potatoes Hack", "Microwaving halved baby potatoes for 3 minutes par-cooks their starchy interior, allowing them to crisp up deeply on the sheet pan in just 10 minutes."),
            ("Staggered Sheet Pan Timing", "Adding steak cubes during the final 6 minutes prevents overcooking, ensuring a juicy medium-rare center while the potatoes achieve golden brown edges."),
            ("Raw Herb Chimichurri Punch", "Never cook the chimichurri sauce—spooning it fresh over hot, resting steak allows the vinegar and herbs to bloom without losing bright color or grassy aromas.")
        ],
        "matrix_title": "Steak Cut Comparison for 20-Minute Sheet Pan Roasting",
        "matrix_headers": ["Beef Cut", "Sear / Crust Speed", "Tenderness", "Best Roasting Temp", "Verdict"],
        "matrix_rows": [
            ["Flank Steak", "Rapid (high surface area)", "Very tender (cut against grain)", "450°F (230°C)", "Top Pick for Fast Searing (Recommended)"],
            ["Top Sirloin", "Excellent browning", "Naturally tender & lean", "450°F (230°C)", "Great High-Protein Option"],
            ["Ribeye Cubes", "Ultra-crispy fat rendering", "Melt-in-mouth richness", "425°F (220°C)", "Decadent & juicy"],
            ["Stew Meat / Chuck", "Slow", "Tough without long braise", "N/A", "Avoid for quick sheet pans"]
        ],
        "ingredients": [
            "1.25 lbs flank steak (or top sirloin), cut into 1-inch cubes",
            "1 lb baby gold or fingerling potatoes, halved lengthwise",
            "3 tbsp extra virgin olive oil (divided: 1.5 tbsp for pan, 1.5 tbsp for sauce)",
            "4 cloves fresh garlic, finely minced (divided)",
            "1 tsp smoked paprika & 1/2 tsp onion powder",
            "1 tsp kosher salt & 1/2 tsp freshly cracked black pepper",
            "1 cup fresh flat-leaf Italian parsley, finely minced",
            "2 tbsp fresh oregano leaves (or 1 tsp dried oregano)",
            "2 tbsp red wine vinegar",
            "1/2 tsp crushed red pepper flakes"
        ],
        "instructions": [
            ("Par-Cook the Potatoes", "Preheat oven to 450°F (230°C) with a heavy rimmed baking sheet inside. Place halved baby potatoes in a microwave-safe bowl with 1 tbsp water; cover and microwave on high for 3 minutes until just tender."),
            ("Crisp Potatoes on Hot Sheet Pan", "Carefully remove the blazing-hot sheet pan from the oven. Toss drained potatoes with 1 tbsp olive oil, 1/2 tsp salt, and 1/4 tsp pepper. Arrange cut-side down on the hot pan and roast for 10 minutes until deeply golden and blistered."),
            ("Season & Add Steak Bites", "Toss cubed steak with 1/2 tbsp olive oil, smoked paprika, garlic powder, remaining salt, and pepper. Pull the sheet pan out, push potatoes to the sides, and scatter steak cubes in the center in a single spaced layer."),
            ("Flash Roast & High Broil", "Return sheet pan to oven and roast at 450°F for 4 minutes. Switch to HIGH BROIL for 90 to 120 seconds until steak cubes develop sizzling browned edges while remaining tender inside."),
            ("Whisk Chimichurri & Serve", "In a small bowl, whisk minced parsley, remaining garlic, oregano, red wine vinegar, crushed red pepper flakes, 1.5 tbsp olive oil, and a pinch of flaky salt. Spoon chimichurri generously over the hot steak and potatoes. Serve sizzling hot!")
        ],
        "pro_tip_title": "Elena’s Preheated Pan Searing Trick",
        "pro_tip": "Leaving your metal baking sheet inside the oven while it preheats to 450°F turns your sheet pan into a flat-top griddle! When your par-cooked potatoes and steak hit the piping hot metal, they immediately sizzle and build a dark caramelized crust without losing moisture.",
        "faqs": [
            ("Can I make this recipe in an air fryer?", "Yes! Air fry the potatoes at 400°F for 8 minutes, shake the basket, add the seasoned steak bites, and air fry together for another 5 minutes until crispy."),
            ("How do I make chimichurri ahead of time?", "Whisk the parsley, vinegar, garlic, and olive oil in a glass jar up to 24 hours in advance. Keep chilled in the fridge and let come to room temperature before drizzling."),
            ("What is the best way to reheat leftover steak and potatoes?", "Reheat in a dry skillet over medium-high heat or in the air fryer at 380°F for 3 minutes to keep the potatoes crisp and prevent steak from becoming rubbery.")
        ],
        "wiki_entities": [
            ("Chimichurri", "https://en.wikipedia.org/wiki/Chimichurri"),
            ("Flank steak", "https://en.wikipedia.org/wiki/Flank_steak"),
            ("Sheet pan", "https://en.wikipedia.org/wiki/Sheet_pan")
        ],
        "pinterest": {
            "board": "Sheet Pan Suppers / Easy Beef Dinners",
            "title": "20-Minute Sheet-Pan Chimichurri Steak and Potatoes (Crispy & Tender!)",
            "desc": "Crispy caramelized baby potatoes and juicy garlic flank steak bites roasted on one sheet pan in 20 minutes, drizzled with fresh scratch chimichurri herb sauce! Pin this weeknight dinner recipe now!",
            "tags": "#sheetpanmeals #steakandpotatoes #chimichurri #20minutedinner #easyweeknightdinner #dinnerideas #glutenfreerecipes"
        }
    },
    {
        "slug": "20-minute-coconut-red-curry-turkey-meatballs",
        "title": "20-Minute Creamy Coconut Red Curry Turkey Meatballs",
        "headline": "20-Minute Creamy Coconut Red Curry Turkey Meatball Skillet",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/coconut-red-curry-turkey-meatballs.jpg",
        "image_file": "coconut-red-curry-turkey-meatballs.jpg",
        "excerpt": "Juicy, golden seared ginger garlic turkey meatballs simmering in an aromatic lemongrass coconut red curry sauce with fresh Thai basil and lime in 20 minutes.",
        "description": "Tender ground turkey meatballs flash-seared and bathed in a luxurious coconut milk red curry sauce scented with ginger, garlic, fish sauce, and fresh Thai basil over steaming jasmine rice.",
        "keywords": "coconut curry meatballs, turkey meatballs curry, 20 minute thai dinner, one pot red curry, ground turkey recipes",
        "prepTime": "PT6M",
        "cookTime": "PT14M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Thai / Southeast Asian",
        "calories": "470 kcal",
        "protein": "34g",
        "fat": "24g",
        "carbs": "29g",
        "fiber": "2g",
        "sodium": "690mg",
        "ratingValue": "4.9",
        "reviewCount": "164",
        "quick_answer": "To make 20-minute creamy coconut red curry turkey meatballs, mix 1.25 lbs lean ground turkey with 2 tbsp panko, 1 grated garlic clove, 1 tsp grated ginger, 1 sliced scallion, and 1/2 tsp salt; roll into 12 meatballs. Sear in 1 tbsp avocado oil in a deep skillet over medium-high heat for 5 minutes until browned on all sides. Push meatballs aside, add 2 tbsp Thai red curry paste and 1 minced shallot, and fry for 1 minute until fragrant. Pour in 1 can (13.5 oz) full-fat coconut milk, 1 tbsp fish sauce, and 1 tsp brown sugar. Simmer gently for 7 minutes until meatballs reach 165°F and sauce thickens. Finish with lime juice and fresh Thai basil.",
        "takeaways": [
            ("Panko Moisture Sponge", "Adding just 2 tablespoons of panko breadcrumbs locks in the turkey juices, keeping lean ground poultry exceptionally tender and springy."),
            ("Frying the Curry Paste", "Blooming Thai red curry paste in hot oil before pouring in coconut milk releases essential chili oils and maximizes authentic fragrant depth."),
            ("Full-Fat Coconut Milk Body", "Always use full-fat canned coconut milk rather than light coconut milk to achieve a silky restaurant-quality curry sauce that coats the back of a spoon.")
        ],
        "matrix_title": "Meatball Protein Base Performance in Coconut Curry",
        "matrix_headers": ["Ground Meat", "Tenderness", "Flavor Absorption", "Simmer Time", "Verdict"],
        "matrix_rows": [
            ["Lean Ground Turkey (93/7)", "Super tender & light", "Absorbs red curry flawlessly", "7 minutes", "Best Balance of Lean Protein & Flavor (Recommended)"],
            ["Ground Chicken", "Soft & delicate", "High flavor uptake", "6–7 minutes", "Excellent alternative"],
            ["Ground Pork", "Rich & juicy", "Savory umami base", "8 minutes", "Decadent & traditional"],
            ["Plant-Based Meat", "Firm texture", "Moderate", "5 minutes", "Great vegetarian swap"]
        ],
        "ingredients": [
            "1.25 lbs lean ground turkey (93/7)",
            "1/4 cup panko breadcrumbs",
            "1 large egg, lightly beaten",
            "3 cloves garlic, grated (divided)",
            "1 tbsp fresh ginger, finely grated (divided)",
            "2 green onions, thinly sliced",
            "2 tbsp Thai red curry paste (such as Mae Ploy or Thai Kitchen)",
            "1 can (13.5 oz) full-fat unsweetened coconut milk",
            "1 tbsp fish sauce (or tamari soy sauce)",
            "1 tbsp brown sugar or coconut palm sugar",
            "Juice of 1 fresh lime",
            "1/2 cup fresh Thai basil leaves (or sweet Italian basil)",
            "Steamed jasmine rice, for serving"
        ],
        "instructions": [
            ("Shape the Turkey Meatballs", "In a mixing bowl, combine ground turkey, panko, beaten egg, half the grated garlic, half the ginger, sliced green onions, and 1/2 tsp salt. Gently mix until just incorporated. Roll into 12 golf-ball-sized meatballs."),
            ("Sear Meatballs to Golden Brown", "Heat 1 tbsp oil in a large deep skillet over medium-high heat. Add meatballs and sear undisturbed for 2 to 3 minutes, then turn and sear for another 2 to 3 minutes until browned on the exterior (they will finish cooking in the sauce)."),
            ("Bloom Curry Aromatics", "Reduce heat to medium. Slide meatballs to the edge of the skillet. Add the remaining garlic, ginger, and 2 tbsp Thai red curry paste to the center. Sauté for 60 seconds until the red chili oil blooms and smells deeply aromatic."),
            ("Simmer in Coconut Milk", "Pour in full-fat coconut milk, fish sauce, and brown sugar. Stir the sauce gently around the meatballs. Bring to a gentle bubbling simmer, reduce heat to low-medium, and cook uncovered for 7 to 8 minutes until meatballs reach 165°F and the sauce turns glossy and thick."),
            ("Finish with Basil & Lime", "Remove skillet from heat. Squeeze fresh lime juice over the skillet and fold in fresh Thai basil leaves until just wilted. Spoon over warm bowls of jasmine rice!")
        ],
        "pro_tip_title": "Elena’s Gentle Hand Meatball Secret",
        "pro_tip": "The secret to melt-in-your-mouth turkey meatballs is light handling: mix the ingredients with a fork or clean fingertips just until combined. Overworking lean ground turkey compacts the proteins and turns them rubbery. A gentle touch ensures a tender, juicy texture in every bite.",
        "faqs": [
            ("Is Thai red curry paste spicy?", "Most commercial red curry pastes have a mild to moderate warmth. If you prefer extra mild, start with 1.5 tablespoons. For more heat, toss in sliced fresh Thai bird's eye chilies."),
            ("Can I substitute ground chicken?", "Yes! Ground chicken works identically and stays exceptionally tender in the coconut curry broth with the exact same cook time."),
            ("Can I freeze these curry meatballs?", "Yes, freeze the cooked meatballs and sauce together in an airtight container for up to 3 months. Thaw overnight in the fridge and reheat gently in a saucepan.")
        ],
        "wiki_entities": [
            ("Red curry", "https://en.wikipedia.org/wiki/Red_curry"),
            ("Coconut milk", "https://en.wikipedia.org/wiki/Coconut_milk"),
            ("Thai basil", "https://en.wikipedia.org/wiki/Thai_basil")
        ],
        "pinterest": {
            "board": "One-Pot Meals / Asian Inspired Recipes",
            "title": "20-Minute Creamy Coconut Red Curry Turkey Meatballs (Easy Dinner!)",
            "desc": "Tender golden turkey meatballs simmering in an irresistible, velvety coconut red curry sauce with fresh Thai basil and lime juice in 20 minutes! Pin this easy skillet dinner for tonight!",
            "tags": "#currymeatballs #turkeyrecipes #thaicurry #onepotdinner #20minutemeals #quickdinner #healthyweeknightdinner"
        }
    },
    {
        "slug": "15-minute-garlic-butter-pan-seared-halibut",
        "title": "15-Minute Pan-Seared Garlic Butter Halibut with Blistered Tomatoes",
        "headline": "15-Minute Pan-Seared Garlic Butter Halibut Fillets with Blistered Cherry Tomatoes",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/garlic-butter-pan-seared-halibut.jpg",
        "image_file": "garlic-butter-pan-seared-halibut.jpg",
        "excerpt": "Thick, flaky pan-seared halibut fillets with a crisp golden crust basted in sizzling garlic herb butter with burst sweet cherry tomatoes and briny capers in 15 minutes.",
        "description": "Restaurant-worthy pan-seared Pacific halibut cooked in 15 minutes: crisp caramelized golden crust, tender milky flakes, basted in foaming garlic lemon thyme butter with sweet burst cherry tomatoes.",
        "keywords": "pan seared halibut, garlic butter halibut, 15 minute fish dinner, quick seafood recipes, halibut with tomatoes, easy white fish",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Mediterranean / Seafood",
        "calories": "390 kcal",
        "protein": "36g",
        "fat": "22g",
        "carbs": "8g",
        "fiber": "2g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "152",
        "quick_answer": "To make 15-minute pan-seared garlic butter halibut, pat 4 halibut fillets (6 oz each) completely dry with paper towels and season with sea salt and black pepper. Heat 1 tbsp olive oil in a heavy stainless steel skillet over medium-high heat until shimmering. Place fillets top-side down and sear undisturbed for 4 to 5 minutes until a deep golden crust forms. Flip fillets, add 3 tbsp unsalted butter, 4 smashed garlic cloves, 1 cup cherry tomatoes, 1 tbsp capers, and fresh thyme sprigs. Spoon the foaming garlic butter continuously over the fish for 3 to 4 minutes until tomatoes blister and fish flakes gently. Finish with fresh lemon juice.",
        "takeaways": [
            ("Paper Towel Moisture Removal", "Halibut must be blotted bone-dry before hitting the skillet; surface moisture steams the fish and prevents that signature golden restaurant crust."),
            ("Continuous Butter Arrosé (Basting)", "Spoon-basting foaming garlic thyme butter over the flipped fillets infuses rich flavor while cooking the delicate interior through gentle convection."),
            ("Sweet Burst Tomato Acidity", "Blistered cherry tomatoes burst under heat, releasing sweet acidic juices that cut through the richness of the butter sauce.")
        ],
        "matrix_title": "White Fish Selection for 15-Minute Pan-Searing",
        "matrix_headers": ["Fish Fillet", "Flake Texture", "Firmness / Sear Hold", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Pacific Halibut", "Large, succulent milky flakes", "Extremely firm & meaty", "7–8 minutes", "Gold Standard Restaurant Quality (Recommended)"],
            ["Chilean Sea Bass", "Buttery, meltingly tender", "Very firm & rich", "8–9 minutes", "Ultra-luxurious treat"],
            ["Cod Loins", "Delicate flakes", "Moderate (handle gently)", "6–7 minutes", "Great budget-friendly swap"],
            ["Mahi Mahi", "Dense & steaky", "Very firm", "7 minutes", "Excellent firm alternative"]
        ],
        "ingredients": [
            "4 fresh skinless halibut fillets (approx. 6 oz each, 1-inch thick)",
            "1 tbsp extra virgin olive oil",
            "3 tbsp unsalted butter",
            "4 cloves fresh garlic, smashed and peeled",
            "1.5 cups whole sweet cherry tomatoes (red and yellow)",
            "1 tbsp drained capers",
            "4 sprigs fresh thyme",
            "1 organic lemon, half sliced into wheels and half juiced",
            "1/2 tsp flaky sea salt & 1/4 tsp freshly ground black pepper",
            "2 tbsp fresh flat-leaf parsley, chopped"
        ],
        "instructions": [
            ("Prep & Dry Halibut", "Remove halibut fillets from refrigerator 10 minutes prior to cooking. Use paper towels to press and pat every side completely dry. Season generously with flaky sea salt and cracked black pepper."),
            ("Sear the Golden Crust", "Heat olive oil in a wide heavy skillet (stainless steel or cast iron) over medium-high heat until shimmering hot. Gently place fillets into the pan. Sear undisturbed for 4 to 5 minutes without moving until a golden-brown caramelized crust forms."),
            ("Flip & Add Aromatics", "Carefully flip each fillet with a thin fish spatula. Reduce heat to medium. Drop in unsalted butter, smashed garlic cloves, cherry tomatoes, capers, lemon slices, and thyme sprigs around the fish."),
            ("Baste with Foaming Butter", "As the butter melts and foams, tilt the pan slightly toward you. Use a large metal spoon to continuously scoop the hot foaming garlic-herb butter over the top of each fillet for 3 to 4 minutes until the tomatoes blister and burst."),
            ("Finish & Serve", "Check that halibut is just opaque and flakes easily with a fork (internal temperature 130°F–135°F). Squeeze fresh lemon juice over the pan, scatter with chopped parsley, and serve immediately with the burst tomatoes and pan juices!")
        ],
        "pro_tip_title": "Elena’s 'Don’t Touch That Fish' Rule",
        "pro_tip": "When you lay a cold fillet onto a smoking hot pan, the proteins immediately contract and grip the metal. Resist the urge to poke, shake, or nudge the fish! At the 4-minute mark, the Maillard browning naturally releases the fillet from the pan, giving you a restaurant-clean flip every single time.",
        "faqs": [
            ("Can I use frozen halibut?", "Yes! Thaw completely overnight in the refrigerator, and make sure to blot dry thoroughly with several paper towels to eliminate excess water before searing."),
            ("What can I substitute for halibut?", "Thick cod loins, sea bass, or grouper make fantastic direct substitutes with nearly identical cooking times."),
            ("What side dishes pair best with pan-seared halibut?", "Serve alongside roasted asparagus, garlic mashed potatoes, lemon herb rice, or a crisp shaved fennel arugula salad.")
        ],
        "wiki_entities": [
            ("Halibut", "https://en.wikipedia.org/wiki/Halibut"),
            ("Pan frying", "https://en.wikipedia.org/wiki/Pan_frying"),
            ("Caper", "https://en.wikipedia.org/wiki/Caper")
        ],
        "pinterest": {
            "board": "Quick & Easy Dinners / Seafood Recipes",
            "title": "15-Minute Pan-Seared Garlic Butter Halibut (Crisp & Flaky!)",
            "desc": "Crisp caramelized pan-seared halibut fillets basted in bubbling garlic thyme butter with burst cherry tomatoes and capers in 15 minutes! The ultimate weeknight luxury dinner. Pin it now!",
            "tags": "#halibut #seafooddinner #pansearedfish #15minutemeals #garlicbutter #easyweeknightdinner #healthyseafood"
        }
    },
    {
        "slug": "15-minute-crispy-honey-garlic-pork-bites",
        "title": "15-Minute Crispy Honey Garlic Butter Pork Tenderloin Bites",
        "headline": "15-Minute Crispy Pan-Seared Honey Garlic Butter Pork Tenderloin Bites",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/crispy-honey-garlic-pork-bites.jpg",
        "image_file": "crispy-honey-garlic-pork-bites.jpg",
        "excerpt": "Melt-in-your-mouth seared pork tenderloin bites with crispy caramelized edges coated in a sticky amber honey garlic butter glaze in 15 minutes.",
        "description": "Tender pork tenderloin medallions cut into bite-sized pieces, pan-seared to crispy golden perfection, and smothered in a bubbling 4-ingredient sticky honey garlic soy glaze.",
        "keywords": "honey garlic pork bites, pork tenderloin bites, 15 minute pork dinner, easy skillet pork, garlic butter pork, quick weeknight meals",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American / Asian Fusion",
        "calories": "430 kcal",
        "protein": "35g",
        "fat": "18g",
        "carbs": "31g",
        "fiber": "1g",
        "sodium": "660mg",
        "ratingValue": "4.9",
        "reviewCount": "195",
        "quick_answer": "To make 15-minute crispy honey garlic pork tenderloin bites, cut 1.25 lbs pork tenderloin into 1-inch cubes and toss with 1 tbsp cornstarch, 1/2 tsp salt, and 1/4 tsp black pepper. Heat 1 tbsp oil in a large cast iron skillet over high heat. Add pork bites in a single spaced layer and sear for 2 to 3 minutes per side until golden and crispy (145°F internal). Reduce heat to medium-low, add 2 tbsp unsalted butter, 4 minced garlic cloves, 1/4 cup honey, 2 tbsp low-sodium soy sauce, and 1 tbsp apple cider vinegar. Toss pork in the bubbling sauce for 60 seconds until a sticky glaze clings to every bite. Garnish with scallions and sesame seeds.",
        "takeaways": [
            ("Cornstarch Crisp Shield", "Lightly dusting pork cubes in cornstarch creates a microscopic crackly crust upon contact with high heat that holds up against sticky glazes."),
            ("Pork Tenderloin Tenderness", "Pork tenderloin is naturally as lean and tender as filet mignon—cooking it quickly at high heat keeps it juicy without the dryness of pork chops."),
            ("Acidic Honey Balance", "A tablespoon of apple cider vinegar prevents the sweet honey from becoming cloying, balancing the savory soy sauce and butter.")
        ],
        "matrix_title": "Pork Cut Performance for High-Speed Skillet Bites",
        "matrix_headers": ["Pork Cut", "Tenderness Level", "Sear Crispiness", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Pork Tenderloin", "Maximum (melt-in-mouth)", "Deep crispy crust with cornstarch", "5–6 minutes", "Superior Texture Winner (Recommended)"],
            ["Boneless Pork Chops", "Moderate (can dry out)", "Good crust", "6–7 minutes", "Watch timer closely"],
            ["Pork Shoulder Cubes", "Chewy unless braised", "High fat browning", "20+ minutes", "Too tough for quick skillets"],
            ["Pork Sirloin Roast", "Firm & lean", "Decent browning", "7 minutes", "Acceptable budget alternative"]
        ],
        "ingredients": [
            "1.25 lbs pork tenderloin, trimmed of silver skin and cut into 1-inch cubes",
            "1 tbsp cornstarch",
            "1 tbsp avocado or vegetable oil",
            "2 tbsp unsalted butter",
            "5 cloves fresh garlic, finely minced",
            "1/4 cup raw honey",
            "2 tbsp low-sodium soy sauce or tamari",
            "1 tbsp apple cider vinegar",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "2 green onions, thinly sliced",
            "1 tsp toasted white sesame seeds"
        ],
        "instructions": [
            ("Toss Pork with Cornstarch", "Pat pork tenderloin cubes dry with paper towels. In a mixing bowl, toss pork with cornstarch, salt, and black pepper until every piece is lightly and evenly coated."),
            ("High-Heat Sear", "Heat oil in a wide cast iron or heavy stainless skillet over medium-high heat until shimmering. Add pork cubes in a single layer with space between each piece (sear in two batches if pan is small)."),
            ("Crisp the Edges", "Sear undisturbed for 2.5 to 3 minutes until the underside is deep golden brown and crispy. Flip each piece and sear for another 2 minutes until just cooked through (145°F internal temperature)."),
            ("Glaze in Sticky Honey Butter", "Reduce heat to medium-low. Add butter and minced garlic to the skillet, sautéing for 30 seconds until fragrant. Pour in honey, soy sauce, and apple cider vinegar. Toss the crispy pork bites continuously as the sauce bubbles into a thick, glossy amber glaze (about 60 seconds)."),
            ("Garnish & Plate", "Remove from heat immediately. Scatter sliced green onions and toasted sesame seeds over the top. Serve over steaming white rice or steamed broccoli!")
        ],
        "pro_tip_title": "Elena’s 145°F Juicy Pork Rule",
        "pro_tip": "Forget the old overcooking myth: pork tenderloin does NOT need to be cooked well-done! Pull your pork bites off the heat at 145°F (with a faint blush of pink in the center). The residual heat of the bubbling honey butter glaze finishes cooking them to juicy, succulent perfection.",
        "faqs": [
            ("Can I make this in an air fryer?", "Yes! Air fry the cornstarch-coated pork bites at 400°F for 7–8 minutes, shaking halfway. Warm the honey garlic butter glaze in a skillet and toss the hot pork bites right in."),
            ("Can I use chicken breast instead?", "Absolutely! Cubed boneless chicken breast or thighs work beautifully with the exact same cook times and sauce measurements."),
            ("How do I store leftovers?", "Store in an airtight glass container in the fridge for up to 4 days. Reheat in a skillet over medium heat with a splash of water to loosen the glaze.")
        ],
        "wiki_entities": [
            ("Pork tenderloin", "https://en.wikipedia.org/wiki/Pork_tenderloin"),
            ("Honey garlic sauce", "https://en.wikipedia.org/wiki/Honey_garlic_sauce"),
            ("Corn starch", "https://en.wikipedia.org/wiki/Corn_starch")
        ],
        "pinterest": {
            "board": "Quick & Easy Dinners / Pork Recipes",
            "title": "15-Minute Crispy Honey Garlic Butter Pork Tenderloin Bites",
            "desc": "Crispy caramelized seared pork tenderloin bites smothered in a sticky amber honey garlic butter glaze in 15 minutes! Crazy delicious weeknight dinner everyone will love. Save this pin now!",
            "tags": "#porktenderloin #honeygarlic #15minutedinner #easyrecipes #quickdinner #porkrecipes #dinnerideas"
        }
    },
    {
        "slug": "20-minute-creamy-lemon-goat-cheese-asparagus-pasta",
        "title": "20-Minute Creamy Lemon Goat Cheese and Asparagus Fettuccine",
        "headline": "20-Minute Creamy Lemon Whipped Goat Cheese and Asparagus Fettuccine",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/creamy-lemon-goat-cheese-asparagus-pasta.jpg",
        "image_file": "creamy-lemon-goat-cheese-asparagus-pasta.jpg",
        "excerpt": "Twirled ribbons of fettuccine coated in a silky, tangy lemon goat cheese sauce with crisp-tender asparagus spears, toasted pine nuts, and cracked pepper in 20 minutes.",
        "description": "Velvety ribbons of al dente fettuccine folded with fresh creamy chèvre goat cheese, lemon zest, sautéed baby asparagus, garlic, and golden toasted pine nuts in 20 minutes.",
        "keywords": "goat cheese pasta, lemon asparagus fettuccine, 20 minute pasta, creamy vegetarian dinner, quick weeknight pasta, chevre pasta sauce",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "French-Italian / Vegetarian",
        "calories": "460 kcal",
        "protein": "16g",
        "fat": "20g",
        "carbs": "56g",
        "fiber": "4g",
        "sodium": "490mg",
        "ratingValue": "4.9",
        "reviewCount": "168",
        "quick_answer": "To make 20-minute creamy lemon goat cheese and asparagus fettuccine, boil 10 oz fettuccine in salted water until al dente (save 1 cup starchy pasta water before draining). While pasta cooks, heat 1.5 tbsp olive oil in a wide skillet, sauté 1 bunch sliced asparagus and 3 minced garlic cloves for 3 minutes until bright green and crisp-tender. Remove from heat, stir in 5 oz fresh creamy goat cheese (chèvre), 1/2 cup hot pasta water, zest and juice of 1 lemon, and 1/4 tsp salt. Whisk vigorously until the goat cheese melts into an ultra-creamy velvety sauce. Toss hot pasta through the sauce, adding more pasta water as needed. Garnish with crumbled goat cheese, toasted pine nuts, and black pepper.",
        "takeaways": [
            ("Emulsification via Starchy Pasta Water", "Hot starchy pasta cooking water acts as a natural emulsifier, melting crumbly chèvre goat cheese into a glossy restaurant-quality cream sauce without heavy cream."),
            ("Two-Texture Goat Cheese Secret", "Melting half the goat cheese into the sauce and crumbling the remaining half on top gives you both velvety creaminess and pockets of tangy brightness."),
            ("Crisp-Tender Asparagus Timing", "Sautéing asparagus for only 3 minutes preserves vibrant chlorophyll green color, crisp bite, and sweet spring flavors.")
        ],
        "matrix_title": "Soft Cheese Melting Properties for Quick Pasta Sauces",
        "matrix_headers": ["Cheese Variety", "Melt Texture", "Tang / Acidity", "Cream Need", "Verdict"],
        "matrix_rows": [
            ["Fresh Chèvre (Goat Cheese)", "Ultra-silky & velvety", "Bright, tangy & complex", "Zero heavy cream needed", "Top Vegetarian Pick (Recommended)"],
            ["Whole Milk Ricotta", "Grainy unless blended", "Mild & milky", "Needs parmesan & butter", "Great for baked bakes"],
            ["Mascarpone", "Rich & buttery", "Very mild & sweet", "Needs extra lemon juice", "Decadent cream sauce"],
            ["Feta Cheese", "Crumbly (melts slowly)", "Salty & sharp", "Needs pasta water blend", "Good Mediterranean option"]
        ],
        "ingredients": [
            "10 oz fettuccine (or tagliatelle or pappardelle)",
            "1 lb fresh asparagus, woody ends trimmed, cut into 1.5-inch pieces",
            "5 oz fresh plain goat cheese log (chèvre), softened",
            "2 tbsp extra virgin olive oil",
            "3 cloves fresh garlic, thinly sliced",
            "Zest and juice of 1 large organic lemon",
            "1/3 cup grated Parmigiano-Reggiano cheese",
            "3 tbsp toasted pine nuts",
            "1/2 tsp kosher salt & 1/2 tsp freshly cracked black pepper",
            "Fresh dill or flat-leaf parsley for garnish"
        ],
        "instructions": [
            ("Boil Pasta & Reserve Starch Water", "Bring a large pot of salted water to a rapid rolling boil. Add fettuccine and cook until al dente according to package instructions (about 9–10 minutes). Before draining, ladle out 1 cup of hot starchy pasta water. Drain pasta."),
            ("Sauté Asparagus & Garlic", "While pasta boils, heat olive oil in a wide skillet over medium heat. Add sliced asparagus and cook for 2 to 3 minutes until tender-crisp and bright green. Add sliced garlic and cook for 45 seconds until fragrant without browning."),
            ("Melt Goat Cheese into Creamy Sauce", "Turn off skillet heat. Crumble 4 oz of the goat cheese directly into the skillet with the asparagus. Pour in 1/2 cup of the hot reserved pasta water, lemon zest, lemon juice, grated parmesan, salt, and black pepper. Whisk gently until the cheese completely melts into an emulsified creamy sauce."),
            ("Toss Fettuccine", "Transfer hot drained fettuccine directly into the skillet. Toss continuously with tongs for 1 to 2 minutes, adding an extra splash of pasta water if needed until every strand is coated in a velvety lemon sheen."),
            ("Garnish & Serve", "Divide pasta into warm bowls. Top each serving with the remaining 1 oz crumbled goat cheese, toasted pine nuts, freshly cracked black pepper, and fresh dill sprigs. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Off-Heat Cheese Whisking Rule",
        "pro_tip": "Fresh goat cheese contains delicate milk proteins that will curdle or separate if boiled over direct flame! Always turn off the stove burner before adding the goat cheese and hot pasta water. The residual pan heat is plenty to melt the chèvre into silky, velvety perfection without separating.",
        "faqs": [
            ("Can I add protein to this pasta?", "Yes! Seared jumbo shrimp, sliced grilled chicken breast, or crispy crumbled prosciutto make delicious additions."),
            ("Can I use gluten-free pasta?", "Yes, any high-quality brown rice or corn-based gluten-free fettuccine or penne works wonderfully."),
            ("How do I toast pine nuts without burning?", "Toast pine nuts in a dry small skillet over medium-low heat for 2 to 3 minutes, swirling the pan continuously until golden brown and fragrant. Transfer immediately to a plate to stop the cooking.")
        ],
        "wiki_entities": [
            ("Goat cheese", "https://en.wikipedia.org/wiki/Goat_cheese"),
            ("Asparagus", "https://en.wikipedia.org/wiki/Asparagus"),
            ("Fettuccine", "https://en.wikipedia.org/wiki/Fettuccine")
        ],
        "pinterest": {
            "board": "Quick Pasta Recipes / Vegetarian Dinners",
            "title": "20-Minute Creamy Lemon Goat Cheese Asparagus Fettuccine",
            "desc": "Ribbons of fettuccine tossed in a silky lemon goat cheese cream sauce with tender sautéed asparagus and toasted pine nuts in 20 minutes! Luxurious weeknight dinner. Save the recipe!",
            "tags": "#goatcheesepasta #asparaguspasta #fettuccine #20minutemeals #vegetariandinner #quickpasta #dinnerideas"
        }
    },
    {
        "slug": "15-minute-korean-gochujang-chicken-bowls",
        "title": "15-Minute Spicy Korean Gochujang Ground Chicken Rice Bowls",
        "headline": "15-Minute Spicy Korean Gochujang Ground Chicken Rice Bowls with Jammy Egg",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/korean-gochujang-chicken-bowls.jpg",
        "image_file": "korean-gochujang-chicken-bowls.jpg",
        "excerpt": "Savory caramelized ground chicken glazed in spicy-sweet Korean gochujang chili paste, served over warm rice with quick-pickled cucumber ribbons and a jammy egg in 15 minutes.",
        "description": "Flavor-packed Korean street food at home: browned ground chicken smothered in spicy fermented gochujang, sesame, and ginger, piled over warm rice with crisp cucumber ribbons and sesame oil.",
        "keywords": "korean chicken bowls, gochujang ground chicken, 15 minute rice bowls, spicy korean chicken, easy weeknight bowls, quick asian dinner",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Korean / Asian Bowls",
        "calories": "480 kcal",
        "protein": "34g",
        "fat": "18g",
        "carbs": "44g",
        "fiber": "3g",
        "sodium": "710mg",
        "ratingValue": "4.9",
        "reviewCount": "184",
        "quick_answer": "To make 15-minute spicy Korean gochujang ground chicken rice bowls, whisk 2 tbsp Korean gochujang red pepper paste, 2 tbsp low-sodium soy sauce, 1.5 tbsp honey or brown sugar, 1 tbsp toasted sesame oil, 1 tbsp rice vinegar, and 1 tbsp water in a small bowl. Heat 1 tbsp oil in a skillet over medium-high heat. Add 1.25 lbs ground chicken, breaking it apart with a spatula, and cook for 5 minutes until browned and caramelized at the edges. Add 3 minced garlic cloves and 1 tsp grated ginger; cook for 1 minute. Pour in the gochujang sauce and simmer for 2 minutes until glossy and thick. Spoon over bowls of warm jasmine rice with sliced cucumbers, green onions, toasted sesame seeds, and a soft-boiled egg.",
        "takeaways": [
            ("High-Heat Ground Chicken Browning", "Letting the ground chicken sit undisturbed in the skillet for the first 2 minutes builds savory caramelized bits (fond) instead of boiling in its juices."),
            ("Fermented Gochujang Umami", "Korean gochujang contains fermented red chilies and glutinous rice that thickens into a rich, deep umami glaze naturally without added cornstarch."),
            ("Quick Tangy Cucumber Balance", "Thinly shaved Persian cucumber ribbons tossed with rice vinegar provide a cooling, refreshing crunch against the spicy glazed chicken.")
        ],
        "matrix_title": "Ground Meat Suitability for Korean Gochujang Bowls",
        "matrix_headers": ["Ground Meat", "Browning Flavor", "Juiciness", "Sauce Cling", "Verdict"],
        "matrix_rows": [
            ["Ground Chicken", "Savory & clean", "Juicy when cooked hot", "Glaze clings tightly", "Perfect Weeknight Profile (Recommended)"],
            ["Ground Turkey", "Mild & lean", "Lean", "Absorbs spicy sauce well", "Great high-protein swap"],
            ["Ground Beef (85/15)", "Rich & beefy", "Very juicy", "Classic bibimbap style", "Rich & indulgent"],
            ["Ground Pork", "Pork belly-like sweetness", "High juiciness", "Caramelizes deeply", "Savory street food style"]
        ],
        "ingredients": [
            "1.25 lbs lean ground chicken (or turkey)",
            "1 tbsp toasted sesame oil (plus more for drizzling)",
            "3 cloves fresh garlic, finely minced",
            "1 tbsp fresh ginger, grated",
            "2 tbsp Korean gochujang (fermented chili paste)",
            "2 tbsp low-sodium soy sauce or tamari",
            "1.5 tbsp honey or brown sugar",
            "1 tbsp rice vinegar",
            "4 cups cooked warm jasmine or sushi rice",
            "2 Persian cucumbers, shaved into ribbons",
            "4 soft-boiled or fried jammy eggs",
            "1 avocado, sliced",
            "2 green onions, thinly sliced",
            "1 tbsp toasted white and black sesame seeds"
        ],
        "instructions": [
            ("Whisk Gochujang Glaze", "In a small measuring cup or bowl, whisk together gochujang paste, soy sauce, honey, 1 tbsp sesame oil, rice vinegar, and 1 tbsp water until completely smooth."),
            ("Brown the Ground Chicken", "Heat 1 tbsp oil in a large skillet or wok over medium-high heat. Add ground chicken and spread across the pan. Let it sear undisturbed for 2 minutes to develop deep golden browning, then break apart with a wooden spoon and cook for another 3 minutes until no longer pink."),
            ("Add Aromatics", "Stir in minced garlic and grated ginger. Sauté for 60 seconds until fragrant and sizzling."),
            ("Simmer & Glaze", "Pour the gochujang sauce mixture over the browned chicken. Stir continuously over medium heat for 2 minutes as the sauce bubbles, thickens, and lacquers every morsel of chicken in a sticky, ruby-red glaze."),
            ("Assemble the Bowls", "Divide warm rice into four bowls. Top with generous scoops of the spicy gochujang chicken. Arrange cucumber ribbons, sliced avocado, green onions, and a halved jammy egg around the bowl. Drizzle with sesame oil and shower with toasted sesame seeds!")
        ],
        "pro_tip_title": "Elena’s 6-Minute Jammy Egg Trick",
        "pro_tip": "To get restaurant-quality eggs with set whites and a luscious custard yolk: lower cold large eggs directly into boiling water for exactly 6 minutes and 30 seconds. Transfer immediately to an ice bath for 3 minutes before peeling. Slice in half over your gochujang bowl for that viral Instagram-worthy egg yolk drip!",
        "faqs": [
            ("How spicy is gochujang?", "Gochujang has a sweet, earthy, fermented warmth rather than a sharp burning heat. If you are sensitive to spice, use 1 tablespoon of gochujang and an extra splash of soy sauce and honey."),
            ("Can I meal prep this?", "Yes! The cooked gochujang chicken stays delicious in the fridge for up to 4 days. Pack rice and chicken together, and keep the fresh cucumber and egg separate until serving."),
            ("What can I use if I don't have gochujang?", "In a pinch, mix 1.5 tbsp Sriracha with 1 tsp red miso paste and 1 tsp brown sugar to mimic the spicy-sweet fermented profile.")
        ],
        "wiki_entities": [
            ("Gochujang", "https://en.wikipedia.org/wiki/Gochujang"),
            ("Korean cuisine", "https://en.wikipedia.org/wiki/Korean_cuisine"),
            ("Sesame oil", "https://en.wikipedia.org/wiki/Sesame_oil")
        ],
        "pinterest": {
            "board": "Asian Bowls / Quick Weeknight Dinners",
            "title": "15-Minute Spicy Korean Gochujang Ground Chicken Rice Bowls",
            "desc": "Caramelized spicy-sweet Korean gochujang ground chicken served over warm rice with cucumber ribbons, avocado, and a jammy egg in 15 minutes! The ultimate viral bowl. Pin it now!",
            "tags": "#koreanbowls #gochujang #groundchicken #15minutedinner #ricebowl #asianfood #quickweeknightdinner"
        }
    },
    {
        "slug": "20-minute-creamy-greek-lemon-chicken-orzo-soup",
        "title": "20-Minute Creamy Greek Lemon Chicken Orzo Soup (Avgolemono)",
        "headline": "20-Minute Creamy Greek Lemon Chicken Orzo Soup (Quick Avgolemono)",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/creamy-greek-lemon-chicken-orzo-soup.jpg",
        "image_file": "creamy-greek-lemon-chicken-orzo-soup.jpg",
        "excerpt": "A comforting, restorative Greek avgolemono soup with tender shredded chicken and tender orzo pasta in a velvety lemon-egg broth with fresh dill in 20 minutes.",
        "description": "Cozy, silky authentic Greek chicken soup made in 20 minutes: tender orzo, shredded chicken breast, and fresh dill in a golden velvety lemon-egg broth without a drop of heavy cream.",
        "keywords": "avgolemono soup, greek lemon chicken soup, lemon orzo soup, 20 minute chicken soup, quick comfort food, easy greek soup",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Greek / Mediterranean",
        "calories": "380 kcal",
        "protein": "32g",
        "fat": "12g",
        "carbs": "36g",
        "fiber": "2g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "172",
        "quick_answer": "To make 20-minute creamy Greek lemon chicken orzo soup (avgolemono), bring 6 cups rich chicken bone broth to a boil in a Dutch oven. Add 1 cup dry orzo pasta and cook for 8 minutes until tender. Stir in 2.5 cups shredded rotisserie chicken. In a heatproof bowl, whisk 2 large eggs and 1 egg yolk with 1/3 cup fresh lemon juice until frothy. Slowly ladle 1 cup of hot broth into the egg mixture while whisking vigorously (this tempers the eggs so they don't curdle). Turn pot heat to low, pour the tempered egg mixture back into the soup, and stir constantly for 2 minutes until soup becomes creamy and golden. Fold in 3 tbsp chopped fresh dill and serve with crusty bread.",
        "takeaways": [
            ("Egg Tempering Emulsion", "Slowly streaming hot broth into whisked eggs warms them gradually, creating an ultra-velvety cream broth without needing a drop of heavy cream or flour."),
            ("Rotisserie Chicken Weeknight Shortcut", "Using pre-cooked rotisserie chicken breast slashes prep time while ensuring ultra-juicy, tender shredded meat in under 20 minutes."),
            ("Fresh Dill & Lemon Synergism", "Freshly squeezed lemon juice combined with generous chopped fresh dill cuts through the rich chicken broth, creating Greek comfort in a bowl.")
        ],
        "matrix_title": "Pasta & Grain Options for 20-Minute Greek Lemon Soup",
        "matrix_headers": ["Grain / Pasta", "Cooking Time", "Broth Starch Release", "Texture", "Verdict"],
        "matrix_rows": [
            ["Orzo Pasta (Risoni)", "8–9 minutes", "Releases silky starch", "Plump & tender spoonfuls", "Traditional Fast Favorite (Recommended)"],
            ["Ditalini", "8 minutes", "Moderate", "Cute tubular bite", "Fun substitute"],
            ["White Long-Grain Rice", "18–20 minutes", "High starch", "Classic Greek style", "Slightly slow for 20-min dinner"],
            ["Cauliflower Rice", "4 minutes", "Zero starch", "Very light & low carb", "Great keto option"]
        ],
        "ingredients": [
            "6 cups good quality chicken bone broth or low-sodium stock",
            "1 cup dry orzo pasta",
            "2.5 cups shredded cooked chicken breast (rotisserie chicken works perfectly)",
            "2 large whole eggs plus 1 egg yolk",
            "1/3 cup freshly squeezed lemon juice (from 2 juicy lemons)",
            "1 tbsp extra virgin olive oil",
            "1/2 tsp kosher salt & 1/2 tsp freshly cracked black pepper",
            "1/4 cup fresh dill, finely chopped",
            "Lemon slices and extra virgin olive oil for serving",
            "Crusty rustic sourdough bread, for dipping"
        ],
        "instructions": [
            ("Boil Broth & Cook Orzo", "In a Dutch oven or large soup pot, bring chicken bone broth and 1/2 tsp salt to a rapid rolling boil over high heat. Add dry orzo pasta, reduce heat to medium, and cook uncovered for 8 minutes, stirring occasionally so orzo doesn't stick to the bottom."),
            ("Add Shredded Chicken", "Stir shredded rotisserie chicken into the bubbling broth and orzo. Reduce heat to the lowest setting while you prepare the egg-lemon mixture."),
            ("Whisk & Froth Eggs with Lemon", "In a medium bowl, vigorously whisk the 2 whole eggs, 1 egg yolk, and 1/3 cup fresh lemon juice together for 60 seconds with a wire whisk until pale yellow and bubbly/frothy."),
            ("Temper the Egg Mixture", "While whisking the eggs constantly with one hand, use a ladle to slowly drizzle 1 cup of hot broth from the pot into the egg bowl in a thin, steady stream. This gently raises the egg temperature so they will not curdle."),
            ("Stir into Soup & Finish", "Slowly pour the warm tempered egg mixture into the soup pot while stirring continuously. Cook over low heat for 1 to 2 minutes (do NOT boil) until the soup magically thickens into a golden, silky, creamy velvet broth. Remove from heat, stir in fresh dill, and ladle into bowls with lemon wheels and cracked black pepper!")
        ],
        "pro_tip_title": "Elena’s 'Never Boil the Eggs' Golden Rule",
        "pro_tip": "The magic of authentic avgolemono lies in the low heat: once you stir the tempered lemon-egg mixture into the soup, NEVER allow the soup to come to a rolling boil! High heat will scramble the eggs. Keep the heat on low and stir gently—the eggs will thicken the broth into liquid silk in less than 90 seconds.",
        "faqs": [
            ("Can I reheat avgolemono soup?", "Yes, but reheat very gently over low heat on the stovetop, stirring constantly. Avoid high microwave heat which can curdle the egg emulsion."),
            ("Can I freeze this soup?", "We do not recommend freezing avgolemono, as the egg and orzo emulsion will separate upon thawing. It keeps beautifully in the fridge for up to 3 days."),
            ("Why add an extra egg yolk?", "The single extra egg yolk adds rich yellow color, silky emulsifying lecithin, and luxurious mouthfeel without any heaviness.")
        ],
        "wiki_entities": [
            ("Avgolemono", "https://en.wikipedia.org/wiki/Avgolemono"),
            ("Orzo", "https://en.wikipedia.org/wiki/Orzo"),
            ("Greek cuisine", "https://en.wikipedia.org/wiki/Greek_cuisine")
        ],
        "pinterest": {
            "board": "Cozy Soup Recipes / Greek Dinners",
            "title": "20-Minute Creamy Greek Lemon Chicken Orzo Soup (Avgolemono)",
            "desc": "Cozy, silky authentic Greek lemon chicken soup with orzo and fresh dill in 20 minutes! Made creamy with tempered lemon and eggs, no heavy cream needed. Save this restorative recipe!",
            "tags": "#avgolemono #chickensoup #greekfood #lemonorzosoup #20minutemeals #comfortfood #healthyrecipes"
        }
    },
    {
        "slug": "20-minute-brown-butter-butternut-squash-gnocchi",
        "title": "20-Minute Creamy Brown Butter Butternut Squash Gnocchi with Crispy Sage",
        "headline": "20-Minute Brown Butter Butternut Squash Gnocchi with Crispy Fried Sage",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/brown-butter-butternut-squash-gnocchi.jpg",
        "image_file": "brown-butter-butternut-squash-gnocchi.jpg",
        "excerpt": "Pillowy tender potato gnocchi coated in a velvety roasted butternut squash puree and nutty brown butter sauce with crisp fried sage leaves and pecans in 20 minutes.",
        "description": "The ultimate autumn weeknight dinner in 20 minutes: pillowy skillet-toasted gnocchi tossed in nutty hazelnut brown butter, roasted butternut squash puree, crisp sage leaves, and parmesan.",
        "keywords": "butternut squash gnocchi, brown butter gnocchi, crispy sage pasta, fall weeknight dinner, 20 minute vegetarian meal, easy gnocchi recipe",
        "prepTime": "PT4M",
        "cookTime": "PT16M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Italian / Autumn Comfort Food",
        "calories": "440 kcal",
        "protein": "11g",
        "fat": "19g",
        "carbs": "58g",
        "fiber": "5g",
        "sodium": "510mg",
        "ratingValue": "4.9",
        "reviewCount": "166",
        "quick_answer": "To make 20-minute creamy brown butter butternut squash gnocchi, melt 4 tbsp unsalted butter in a wide skillet over medium heat. Add 12 fresh sage leaves; fry for 2 minutes until dark green and crisp, then remove with a slotted spoon. Continue cooking the butter for 2 to 3 minutes until foamy, fragrant, and dotted with golden-brown flecks. Stir in 1 cup pureed roasted butternut squash (canned or pre-cooked), 1/2 cup vegetable broth, 1/4 cup heavy cream, 1/4 tsp ground nutmeg, and 1/2 tsp salt. Meanwhile, drop 1 lb potato gnocchi into boiling salted water for 3 minutes until they float. Transfer gnocchi directly into the bubbling brown butter squash sauce, toss for 1 minute with 1/3 cup grated parmesan, and garnish with the crispy fried sage and toasted pecans.",
        "takeaways": [
            ("Nutty Brown Butter Flavor Core", "Browning the milk solids in unsalted butter creates deep toffee-hazelnut notes that pair harmoniously with sweet autumnal squash."),
            ("Panned Butternut Puree Shortcut", "Using smooth canned or ready-steamed butternut squash puree cuts out 45 minutes of squash roasting without sacrificing silky flavor."),
            ("Whole Crispy Sage Garnish", "Frying fresh sage leaves in hot butter crisps them like savory herbal potato chips that shatter on your tongue.")
        ],
        "matrix_title": "Gnocchi Style Performance in Brown Butter Squash Sauce",
        "matrix_headers": ["Gnocchi Variety", "Boil / Skillet Time", "Texture", "Sauce Adhesion", "Verdict"],
        "matrix_rows": [
            ["Shelf-Stable Potato Gnocchi", "3 minutes (boil) or 5 min (pan fry)", "Pillowy & soft", "Excellent coating", "Top Fast Weeknight Choice (Recommended)"],
            ["Refrigerated Fresh Gnocchi", "2 minutes", "Ultra-tender & light", "Superb absorption", "Tender restaurant feel"],
            ["Cauliflower Gnocchi (Trader Joe's)", "8 minutes (pan sear only)", "Chewy & dense", "Good", "Great low-carb swap"],
            ["Ricotta Gnocchi", "3 minutes", "Melt-in-mouth soft", "Delicate", "Requires very gentle tossing"]
        ],
        "ingredients": [
            "1 lb store-bought potato gnocchi (shelf-stable or fresh)",
            "4 tbsp unsalted butter",
            "12 fresh sage leaves",
            "1 cup pure butternut squash puree (canned or fresh)",
            "1/2 cup low-sodium vegetable or chicken broth",
            "1/4 cup heavy cream or whole milk",
            "1/3 cup freshly grated Parmigiano-Reggiano cheese",
            "1/4 cup chopped pecans or walnuts, toasted",
            "1/4 tsp ground nutmeg & 1/2 tsp kosher salt",
            "1/4 tsp freshly cracked black pepper"
        ],
        "instructions": [
            ("Boil the Gnocchi", "Bring a large pot of salted water to a rolling boil. Drop in the potato gnocchi and boil for 2 to 3 minutes until they all float to the water's surface. Reserve 1/4 cup cooking water and drain."),
            ("Crisp the Sage Leaves", "Melt 4 tbsp butter in a wide deep skillet over medium heat. Once bubbling, add whole fresh sage leaves in a single layer. Fry for 90 to 120 seconds until leaves are dark green and crisp. Remove with a fork to a paper towel plate (leave the butter in pan)."),
            ("Brown the Butter", "Keep skillet over medium heat. Swirl pan continuously for 2 to 3 minutes as the butter foams and milk solids turn a rich amber brown with a nutty hazelnut aroma."),
            ("Build Velvety Squash Sauce", "Whisk butternut squash puree, vegetable broth, heavy cream, ground nutmeg, salt, and black pepper into the brown butter. Bring to a gentle simmer for 2 minutes until glossy and smooth."),
            ("Toss & Serve", "Tumble the drained gnocchi directly into the simmering sauce. Stir in grated parmesan cheese and toss gently for 1 minute until gnocchi is coated in golden velvet. Top with the crispy fried sage leaves and toasted pecans!")
        ],
        "pro_tip_title": "Elena’s Brown Butter Watch-Point",
        "pro_tip": "Butter transforms from melted to nutty brown to burned in less than 30 seconds! Keep your heat on medium and watch the foam: as soon as tiny amber-brown flecks settle at the bottom and you smell roasted hazelnuts, immediately stir in your butternut squash puree. The cool puree stops the cooking instantly and locks in that sublime nutty depth.",
        "faqs": [
            ("Can I pan-fry the gnocchi instead of boiling?", "Yes! Pan-searing gnocchi in olive oil until golden and crisp on the outside before tossing in the sauce gives a delightful crunch contrast."),
            ("Can I make this dairy-free / vegan?", "Yes! Use dairy-free vegan butter, coconut cream or oat cream, and nutritional yeast or vegan parmesan."),
            ("Where do I find butternut squash puree?", "Canned pure butternut squash puree is found in the canned vegetable aisle near canned pumpkin, or you can steam cubed squash and blend smooth.")
        ],
        "wiki_entities": [
            ("Gnocchi", "https://en.wikipedia.org/wiki/Gnocchi"),
            ("Beurre noisette", "https://en.wikipedia.org/wiki/Beurre_noisette"),
            ("Butternut squash", "https://en.wikipedia.org/wiki/Butternut_squash")
        ],
        "pinterest": {
            "board": "Fall Comfort Food / Easy Pasta Dinners",
            "title": "20-Minute Creamy Brown Butter Butternut Squash Gnocchi",
            "desc": "Pillowy potato gnocchi in a nutty brown butter butternut squash cream sauce with crispy fried sage leaves and toasted pecans in 20 minutes! The ultimate cozy autumn dinner. Pin it now!",
            "tags": "#butternutsquash #gnocchi #brownbutter #crispysage #fallrecipes #comfortfood #20minutemeals #vegetarianrecipes"
        }
    },
    {
        "slug": "15-minute-thai-basil-ground-beef",
        "title": "15-Minute Sweet and Spicy Thai Basil Ground Beef (Pad Krapow Neua)",
        "headline": "15-Minute Thai Basil Ground Beef (Street-Style Pad Krapow Neua)",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/thai-basil-ground-beef.jpg",
        "image_file": "thai-basil-ground-beef.jpg",
        "excerpt": "Savory caramelized ground beef stir-fried with fragrant holy basil, garlic, and fresh red chilies in a sweet-savory oyster soy sauce with a crispy fried runny egg in 15 minutes.",
        "description": "Authentic Bangkok street food made lightning fast: sizzling caramelized minced ground beef tossed with fiery Thai chilies, garlic, and sweet basil over hot rice with a lace-edged fried egg.",
        "keywords": "thai basil beef, pad krapow neua, 15 minute ground beef dinner, easy thai street food, spicy basil beef, quick weeknight stir fry",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Thai / Street Food",
        "calories": "490 kcal",
        "protein": "34g",
        "fat": "25g",
        "carbs": "33g",
        "fiber": "2g",
        "sodium": "720mg",
        "ratingValue": "4.9",
        "reviewCount": "198",
        "quick_answer": "To make 15-minute Thai basil ground beef (Pad Krapow Neua), whisk 2 tbsp oyster sauce, 1.5 tbsp low-sodium soy sauce, 1 tsp dark sweet soy sauce, 1 tbsp fish sauce, and 1 tsp brown sugar in a small bowl. Heat 1.5 tbsp high-smoke point oil in a wok or heavy skillet over high heat. Add 1.25 lbs lean ground beef (85/15), pressing flat and searing undisturbed for 2 minutes to caramelize. Break beef into crumbles and stir-fry for 3 minutes. Add 5 minced garlic cloves and 2 to 3 sliced red bird's eye chilies; cook for 60 seconds until fragrant. Pour in sauce and toss for 1 minute. Turn off heat and fold in 1.5 cups fresh Thai holy basil or sweet basil leaves until just wilted. Serve over hot jasmine rice with a crispy Thai fried egg.",
        "takeaways": [
            ("Undisturbed High-Heat Beef Sear", "Allowing ground beef to sear flat against blazing hot metal builds essential wok caramelization before breaking it into minced morsels."),
            ("Off-Heat Basil Wilt", "Folding in fresh Thai basil leaves after turning off the heat preserves the delicate herbal anise aromatics that high heat would otherwise burn away."),
            ("Lacy Thai Fried Egg Essential", "Frying the egg in hot oil creates crispy, bubbly golden lace edges while keeping the bright yolk liquid to mix through the spicy beef.")
        ],
        "matrix_title": "Cooking Oil Performance for High-Heat Thai Stir Fry",
        "matrix_headers": ["Oil Variety", "Smoke Point", "Flavor Neutrality", "Crispy Egg Blistering", "Verdict"],
        "matrix_rows": [
            ["Avocado Oil", "520°F (270°C)", "Completely neutral", "Explosive blistered edges", "Gold Standard for Wok Cooking (Recommended)"],
            ["Peanut Oil", "450°F (230°C)", "Subtle nutty finish", "Outstanding crispy char", "Traditional Thai street choice"],
            ["Canola / Vegetable Oil", "400°F (204°C)", "Neutral", "Good blistering", "Standard pantry standby"],
            ["Extra Virgin Olive Oil", "375°F (190°C)", "Strong olive notes", "Smokes too fast", "Avoid for wok stir-fries"]
        ],
        "ingredients": [
            "1.25 lbs lean ground beef (85/15 or 90/10)",
            "1.5 tbsp avocado or peanut oil",
            "5 cloves fresh garlic, finely minced",
            "2–4 fresh Thai bird's eye chilies (or red serrano), thinly sliced",
            "2 tbsp oyster sauce",
            "1.5 tbsp soy sauce",
            "1 tsp dark sweet soy sauce (Kecap Manis) or molasses",
            "1 tbsp fish sauce",
            "1 tsp brown sugar",
            "1.5 cups fresh Thai holy basil leaves (or sweet Italian basil)",
            "4 large eggs, for crispy frying",
            "4 cups steamed jasmine white rice"
        ],
        "instructions": [
            ("Mix Savory Stir-Fry Sauce", "In a small bowl, whisk together oyster sauce, soy sauce, dark sweet soy sauce, fish sauce, and brown sugar until sugar dissolves."),
            ("Sear the Ground Beef", "Heat 1 tbsp oil in a large wok or cast iron skillet over high heat until smoking hot. Add ground beef and flatten into a single layer. Let sear undisturbed for 2 full minutes to achieve deep brown wok caramelization."),
            ("Sauté Chilies & Garlic", "Break beef into crumbles and stir-fry for 2 minutes. Push beef to the perimeter and add minced garlic and sliced red chilies in the center; sauté for 45 to 60 seconds until fragrant."),
            ("Glaze & Fold in Basil", "Pour the sauce over the sizzling beef and toss continuously for 60 seconds until every bit is coated and shiny. Remove skillet from heat immediately. Toss in fresh basil leaves and stir for 30 seconds until just wilted."),
            ("Fry Crispy Eggs & Serve", "In a small separate skillet, heat 2 tbsp oil over high heat. Crack in an egg; it will bubble violently and puff up around the edges. Fry for 90 seconds until the edges are golden brown and crispy and the yolk is still runny. Top bowls of rice and spicy basil beef with the crispy egg!")
        ],
        "pro_tip_title": "Elena’s Authentic Pad Krapow Secret",
        "pro_tip": "If you can source authentic Thai Holy Basil (Bai Krapow) from an Asian grocer, use it! It has a distinct peppery, clove-like kick that defines genuine street food. If using standard Thai basil or Italian sweet basil, add a tiny pinch of freshly ground black pepper to mimic that authentic spicy herbal punch.",
        "faqs": [
            ("Can I use ground pork or chicken?", "Yes! Pad Krapow is traditionally made with pork (Moo), chicken (Gai), or beef (Neua). Cook times and sauce measurements remain exactly the same."),
            ("How do I adjust the heat level?", "Thai bird's eye chilies are fiery! For a mild dish, remove the seeds or substitute sliced red bell pepper with 1 deseeded red jalapeño."),
            ("Can I meal prep this dish?", "Yes, the beef reheats extraordinarily well in a skillet or microwave for up to 4 days. Cook the crispy fried egg fresh when ready to eat!")
        ],
        "wiki_entities": [
            ("Phat kaphrao", "https://en.wikipedia.org/wiki/Phat_kaphrao"),
            ("Oyster sauce", "https://en.wikipedia.org/wiki/Oyster_sauce"),
            ("Thai basil", "https://en.wikipedia.org/wiki/Thai_basil")
        ],
        "pinterest": {
            "board": "Quick Asian Dinners / Easy Ground Beef Recipes",
            "title": "15-Minute Sweet and Spicy Thai Basil Ground Beef (Pad Krapow)",
            "desc": "Caramelized savory ground beef stir-fried with fragrant holy basil, garlic, and chilies over jasmine rice with a crispy fried runny egg in 15 minutes! Save this viral street food dinner!",
            "tags": "#thaifood #padkrapow #thaibasilbeef #groundbeefrecipes #15minutemeals #quickdinner #asianstreetfood"
        }
    },
    {
        "slug": "15-minute-blackened-salmon-tacos",
        "title": "15-Minute Garlic Butter Blackened Salmon Tacos with Mango Slaw",
        "headline": "15-Minute Garlic Butter Blackened Salmon Tacos with Crisp Mango Slaw",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/blackened-salmon-tacos.jpg",
        "image_file": "blackened-salmon-tacos.jpg",
        "excerpt": "Flaky, smoky blackened wild salmon fillets tucked into warm charred corn tortillas, topped with vibrant mango cilantro slaw and creamy avocado lime crema in 15 minutes.",
        "description": "Crispy seasoned blackened salmon flaked into warm corn tortillas with crunchy mango cabbage slaw, sliced ripe avocado, and a tangy cilantro lime drizzle in 15 minutes.",
        "keywords": "blackened salmon tacos, fish tacos, 15 minute salmon dinner, mango slaw salmon, quick weeknight tacos, easy seafood tacos",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings (8 tacos)",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Baja / Mexican Seafood",
        "calories": "460 kcal",
        "protein": "32g",
        "fat": "20g",
        "carbs": "39g",
        "fiber": "5g",
        "sodium": "560mg",
        "ratingValue": "4.9",
        "reviewCount": "190",
        "quick_answer": "To make 15-minute blackened salmon tacos with mango slaw, rub 1.25 lbs skinless salmon fillets with 1 tbsp olive oil and 1.5 tbsp blackened seasoning (smoked paprika, garlic powder, onion powder, oregano, cumin, salt, and cayenne). Heat 1 tbsp butter in a cast iron skillet over medium-high heat. Sear salmon for 3 to 4 minutes per side until deeply blackened and flaky; break into bite-sized chunks. In a bowl, toss 1.5 cups shredded purple cabbage with 1 diced ripe mango, 1/4 cup chopped cilantro, and juice of 1 lime. Warm 8 small corn tortillas. Fill tortillas with the blackened salmon chunks, top with the mango slaw, sliced avocado, and a drizzle of lime crema.",
        "takeaways": [
            ("Cast Iron Crust Blackening", "Cooking spice-rubbed salmon in a smoking hot cast iron skillet chars the paprika and spices without drying out the rich salmon fat underneath."),
            ("Sweet Mango Acidic Contrast", "Diced sweet mango cuts through the smoky heat of the blackened crust, providing a juicy, bright tropical crunch in every bite."),
            ("Tortilla Charring Hack", "Charring corn tortillas directly over an open gas flame or in a hot dry skillet prevents them from tearing under juicy toppings.")
        ],
        "matrix_title": "Fish Taco Protein Performance Under Blackened Seasoning",
        "matrix_headers": ["Fish Variety", "Blackened Crust Char", "Fat Content & Moisture", "Cook Time", "Verdict"],
        "matrix_rows": [
            ["Wild Salmon Fillet", "Intense, deep caramelized crust", "High omega-3s (stays juicy)", "6–7 minutes", "Flavor Champion (Recommended)"],
            ["Pacific Cod", "Good crust", "Lean (mild & flaky)", "5–6 minutes", "Classic Baja fish taco swap"],
            ["Mahi Mahi", "Firm blackened exterior", "Moderate", "6 minutes", "Great tropical alternative"],
            ["Tilapia", "Moderate", "Low", "4–5 minutes", "Budget alternative"]
        ],
        "ingredients": [
            "1.25 lbs fresh skinless salmon fillets",
            "1.5 tbsp blackened Cajun seasoning (smoked paprika, garlic, onion, cayenne, oregano)",
            "1 tbsp olive oil & 1 tbsp unsalted butter",
            "8 small corn or flour tortillas",
            "1.5 cups shredded purple cabbage",
            "1 large ripe mango, peeled and finely diced",
            "1/4 cup fresh cilantro, finely chopped",
            "Juice of 2 fresh limes (divided)",
            "1 ripe Hass avocado, sliced",
            "1/3 cup sour cream or Mexican crema",
            "Flaky sea salt to taste"
        ],
        "instructions": [
            ("Toss Mango Slaw", "In a medium bowl, combine shredded purple cabbage, diced mango, chopped cilantro, juice of 1 lime, and a pinch of salt. Toss well and set aside to let flavors marry."),
            ("Season Salmon", "Pat salmon fillets dry with paper towels. Rub all sides with 1 tbsp olive oil, then coat generously with the blackened seasoning blend, pressing spices into the fish."),
            ("Blacken the Salmon", "Melt 1 tbsp butter in a large cast iron skillet over medium-high heat until sizzling. Add salmon fillets and sear undisturbed for 3.5 to 4 minutes until deeply browned and blackened. Flip and sear for another 2.5 to 3 minutes until salmon is cooked through and flakes easily."),
            ("Char Tortillas", "While salmon cooks, warm tortillas directly over a low gas stove burner for 15 seconds per side until lightly charred, or toast in a dry hot skillet."),
            ("Flake & Assemble Tacos", "Use two forks to break the blackened salmon into tender, bite-sized flakes. Distribute warm salmon across the charred tortillas. Top with generous spoonfuls of mango slaw, avocado slices, and a drizzle of crema. Serve with lime wedges!")
        ],
        "pro_tip_title": "Elena’s Tortilla Double-Stacking Rule",
        "pro_tip": "If you are using thin traditional corn tortillas, always double them up (two tortillas per taco)! The smoky salmon juices and fresh mango slaw release incredible moisture that will break a single thin corn tortilla. Double-stacking keeps your taco sturdy from first bite to last.",
        "faqs": [
            ("Can I use frozen salmon?", "Yes! Thaw completely in cold water or in the fridge, then pat thoroughly dry with paper towels so the blackening spices form a crisp crust rather than steaming."),
            ("Can I make this in the air fryer?", "Yes! Air fry seasoned salmon fillets at 400°F for 7–8 minutes until blackened and flaky, then flake into tortillas."),
            ("How do I make the quick lime crema?", "Simply whisk 1/3 cup sour cream or plain Greek yogurt with 1 tbsp fresh lime juice, 1/2 tsp garlic powder, and a pinch of salt until smooth and drizzle-ready.")
        ],
        "wiki_entities": [
            ("Fish taco", "https://en.wikipedia.org/wiki/Fish_taco"),
            ("Blackening (cooking)", "https://en.wikipedia.org/wiki/Blackening_(cooking)"),
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food")
        ],
        "pinterest": {
            "board": "Taco Tuesday / Easy Seafood Recipes",
            "title": "15-Minute Blackened Salmon Tacos with Mango Slaw",
            "desc": "Crispy blackened wild salmon flaked into warm charred tortillas with juicy mango cilantro slaw and avocado lime crema in 15 minutes! The ultimate viral fish taco. Pin it now!",
            "tags": "#salmontacos #fishtacos #blackenedsalmon #15minutedinner #tacotuesday #mangoslaw #healthyrecipes"
        }
    },
    {
        "slug": "20-minute-creamy-tuscan-white-bean-skillet",
        "title": "20-Minute Creamy Garlic Parmesan Tuscan White Bean Skillet",
        "headline": "20-Minute Creamy Tuscan Garlic Butter White Bean Skillet with Garlic Toast",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/creamy-tuscan-white-bean-skillet.jpg",
        "image_file": "creamy-tuscan-white-bean-skillet.jpg",
        "excerpt": "Velvety white cannellini beans simmering in a luxurious sun-dried tomato, garlic, tender baby spinach, and parmesan cream sauce with crusty garlic bread in 20 minutes.",
        "description": "High-protein Italian comfort food in 20 minutes: tender white cannellini beans simmered in a creamy garlic parmesan sauce with sun-dried tomatoes, fresh spinach, and crispy sourdough toast.",
        "keywords": "creamy tuscan white beans, cannellini bean skillet, 20 minute vegetarian dinner, tuscan beans and spinach, garlic parmesan beans, easy one pot dinner",
        "prepTime": "PT4M",
        "cookTime": "PT16M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Tuscan / Italian Vegetarian",
        "calories": "410 kcal",
        "protein": "18g",
        "fat": "21g",
        "carbs": "41g",
        "fiber": "9g",
        "sodium": "580mg",
        "ratingValue": "4.9",
        "reviewCount": "174",
        "quick_answer": "To make 20-minute creamy Tuscan white bean skillet, heat 1.5 tbsp olive oil from a jar of sun-dried tomatoes in a large skillet over medium heat. Sauté 4 minced garlic cloves and 1/3 cup chopped sun-dried tomatoes for 1 minute until fragrant. Add two 15-oz cans of drained and rinsed cannellini beans, 1/2 cup vegetable broth, and 1/2 tsp Italian seasoning; simmer for 5 minutes, lightly mashing 1/3 of the beans with a wooden spoon to naturally thicken the sauce. Pour in 1/2 cup heavy cream and 1/2 cup freshly grated parmesan cheese, stirring until melted. Fold in 3 cups fresh baby spinach and cook for 2 minutes until wilted. Garnish with fresh basil and serve with toasted garlic sourdough.",
        "takeaways": [
            ("Partial Bean Mashing Technique", "Gently crushing a third of the cannellini beans with the back of a spoon releases natural starches that thicken the sauce into creamy liquid silk."),
            ("Sun-Dried Tomato Oil Utilization", "Cooking aromatics directly in the infused oil from the sun-dried tomato jar injects immediate concentrated Mediterranean umami into the dish."),
            ("High-Fiber Plant Protein", "Cannellini beans deliver 9 grams of dietary fiber and 18 grams of clean protein per serving while feeling as comforting as alfredo pasta.")
        ],
        "matrix_title": "White Bean Selection for Creamy Skillet Simmering",
        "matrix_headers": ["Bean Variety", "Skin Delicacy", "Starch Release", "Simmer Time", "Verdict"],
        "matrix_rows": [
            ["Cannellini (White Kidney)", "Ultra-tender & thin skin", "High creamy starch", "5–6 minutes", "Gold Standard for Tuscan Skillets (Recommended)"],
            ["Great Northern Beans", "Moderate skin", "Medium starch", "6 minutes", "Excellent everyday alternative"],
            ["Navy Beans", "Small & firm", "Lower starch", "7–8 minutes", "Better for baked beans"],
            ["Butter Beans / Lima Beans", "Large & meaty", "Very creamy", "5 minutes", "Delicious rustic swap"]
        ],
        "ingredients": [
            "2 cans (15 oz each) cannellini beans, drained and rinsed",
            "1.5 tbsp olive oil (preferably oil from the sun-dried tomato jar)",
            "4 cloves fresh garlic, finely minced",
            "1/2 cup sun-dried tomatoes in oil, drained and chopped",
            "1/2 cup low-sodium vegetable broth",
            "1/2 cup heavy cream (or full-fat coconut milk)",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese",
            "3 packed cups fresh baby spinach leaves",
            "1 tsp dried Italian seasoning & 1/4 tsp crushed red pepper flakes",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "Fresh basil leaves for garnish",
            "Garlic-rubbed toasted sourdough bread slices, for serving"
        ],
        "instructions": [
            ("Sauté Aromatics", "Heat sun-dried tomato oil in a deep enameled cast iron or skillet over medium heat. Add minced garlic, chopped sun-dried tomatoes, and crushed red pepper flakes. Sauté for 60 to 90 seconds until garlic is fragrant and translucent."),
            ("Simmer & Mash Beans", "Add the drained cannellini beans, vegetable broth, Italian seasoning, salt, and black pepper to the skillet. Bring to a gentle simmer for 4 to 5 minutes. Use the back of a wooden spoon or potato masher to press and crush about one-third of the beans against the pan bottom to thicken the liquid."),
            ("Stir in Cream & Parmesan", "Pour in heavy cream and grated parmesan cheese. Stir continuously over medium-low heat for 2 minutes as the cheese melts and emulsifies into a luxurious, bubbly sauce."),
            ("Wilt Spinach", "Add fresh baby spinach to the skillet in handfuls. Fold gently into the hot bean cream for 1 to 2 minutes until just wilted and glossy."),
            ("Garnish & Serve with Toast", "Remove skillet from heat. Scatter fresh torn basil leaves and extra parmesan over the top. Serve hot in shallow bowls with thick slices of toasted sourdough dipped right into the creamy sauce!")
        ],
        "pro_tip_title": "Elena’s Garlic-Rubbed Toast Hack",
        "pro_tip": "Don't just toast your bread—take a warm, thick slice of toasted sourdough straight from the skillet or oven and rub a raw peeled clove of garlic firmly across the crusty surface! The rough bread acts like a microplane grater, leaving behind an intoxicating garlic oil layer that elevates every dip into the beans.",
        "faqs": [
            ("Can I make this dairy-free / vegan?", "Yes! Swap heavy cream for full-fat canned coconut milk or cashew cream, and use dairy-free vegan parmesan or 2 tbsp nutritional yeast."),
            ("Can I add meat to this?", "Browned sweet Italian sausage or diced crispy pancetta make phenomenal additions—simply brown the meat first before adding the garlic."),
            ("How long do leftovers last?", "Keep in an airtight container in the fridge for up to 5 days. Reheat on the stove over low heat with a splash of broth or cream to loosen.")
        ],
        "wiki_entities": [
            ("Cannellini", "https://en.wikipedia.org/wiki/Phaseolus_vulgaris"),
            ("Tuscan cuisine", "https://en.wikipedia.org/wiki/Tuscan_food"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato")
        ],
        "pinterest": {
            "board": "Vegetarian Dinners / One-Pot Comfort Meals",
            "title": "20-Minute Creamy Tuscan Garlic Parmesan White Bean Skillet",
            "desc": "Creamy white cannellini beans simmering in a rich sun-dried tomato, garlic, and parmesan cream sauce with spinach and garlic sourdough in 20 minutes! Cozy weeknight dinner. Save it now!",
            "tags": "#whitebeans #tuscanbeans #onepotdinner #vegetariandinner #20minutemeals #comfortfood #easyrecipes"
        }
    },
    {
        "slug": "15-minute-chili-crunch-garlic-udon",
        "title": "15-Minute Spicy Garlic Chili Crunch Udon Noodles",
        "headline": "15-Minute Spicy Garlic Chili Crunch Udon Noodles with Jammy Egg",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/chili-crunch-garlic-udon.jpg",
        "image_file": "chili-crunch-garlic-udon.jpg",
        "excerpt": "Thick, chewy Japanese sanuki udon noodles slicked in a spicy, savory garlic chili crunch sauce with baby bok choy and a runny fried egg in 15 minutes.",
        "description": "Chewy Japanese udon noodles tossed in sizzling garlic, scallions, soy sauce, and crispy chili oil crunch with blanched baby bok choy and a golden sunny-side egg.",
        "keywords": "chili crunch udon, spicy garlic noodles, 15 minute udon noodles, quick asian noodles, chili crisp udon, easy weeknight noodles",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Japanese / Pan-Asian",
        "calories": "450 kcal",
        "protein": "14g",
        "fat": "18g",
        "carbs": "60g",
        "fiber": "3g",
        "sodium": "740mg",
        "ratingValue": "4.9",
        "reviewCount": "186",
        "quick_answer": "To make 15-minute spicy garlic chili crunch udon noodles, drop 4 packs (approx. 200g each) of frozen Japanese Sanuki udon noodles and 2 halved baby bok choy into boiling water for 1 minute until noodles separate; drain well. In a large skillet or wok, heat 1 tbsp sesame oil over medium heat. Add 4 minced garlic cloves and the white parts of 3 sliced scallions; sauté for 45 seconds until aromatic. Whisk in 2.5 tbsp chili crunch / chili crisp, 3 tbsp low-sodium soy sauce, 1 tbsp dark soy sauce, 1.5 tbsp oyster sauce, 1 tsp rice vinegar, and 1 tsp brown sugar. Toss the drained hot udon noodles and bok choy into the bubbling sauce for 1 to 2 minutes until glossy and coated. Serve topped with a sunny-side egg, green scallion greens, and sesame seeds.",
        "takeaways": [
            ("Frozen Sanuki Udon Supremacy", "Frozen Japanese Sanuki udon cakes have superior chew and bounce (koshi) compared to shelf-stable dried udon, needing just 60 seconds in boiling water."),
            ("Chili Crunch Texture Burst", "Crispy fried garlic, shallot, and chili bits in chili crisp deliver texture and complex aromatic heat that cling to the rounded udon noodles."),
            ("Glossy Emulsified Noodle Coat", "Tossing the noodles directly in the hot savory sauce ensures every thick noodle absorbs the dark soy and chili crunch without pooling at the bottom.")
        ],
        "matrix_title": "Udon Noodle Format Comparison for Quick Skillet Tosses",
        "matrix_headers": ["Udon Type", "Prep / Thaw Time", "Chewiness / Bounce (Koshi)", "Sauce Grip", "Verdict"],
        "matrix_rows": [
            ["Frozen Sanuki Udon Cakes", "1 minute in boiling water", "Phenomenal chewy bounce", "Maximum glaze hold", "Best Texture Overall (Recommended)"],
            ["Fresh Vacuum-Packed Udon", "2 minutes in hot water", "Soft & tender", "Good", "Reliable weeknight backup"],
            ["Dried Udon Sticks", "8–10 minutes boiling", "Firmer, denser bite", "Moderate", "Too slow for 15 minutes"],
            ["Ramen / Chow Mein Noodles", "3 minutes", "Curly & springy", "High", "Fun substitution"]
        ],
        "ingredients": [
            "4 blocks (approx. 7 oz / 200g each) frozen Sanuki udon noodles",
            "2 heads baby bok choy, quartered lengthwise",
            "1 tbsp toasted sesame oil",
            "4 cloves fresh garlic, finely minced",
            "3 green onions, thinly sliced (whites and greens separated)",
            "2.5 tbsp store-bought spicy chili crunch (such as Momofuku, Lao Gan Ma, or Fly By Jing)",
            "3 tbsp low-sodium soy sauce",
            "1 tbsp dark soy sauce (for rich caramel color)",
            "1.5 tbsp oyster sauce (or vegetarian mushroom sauce)",
            "1 tsp rice vinegar & 1 tsp brown sugar",
            "4 sunny-side-up or jammy soft-boiled eggs",
            "1 tbsp toasted sesame seeds"
        ],
        "instructions": [
            ("Boil Udon & Bok Choy", "Bring a large pot of water to a boil. Drop in the frozen udon blocks and quartered baby bok choy. Gently nudge noodles with chopsticks; they will separate and cook in exactly 60 to 90 seconds. Drain immediately in a colander."),
            ("Sauté Aromatics", "Heat sesame oil in a wide skillet or wok over medium heat. Add minced garlic and sliced white scallion parts. Sauté for 45 to 60 seconds until fragrant and sizzling without burning."),
            ("Simmer Chili Crunch Sauce", "Add the chili crunch, soy sauce, dark soy sauce, oyster sauce, rice vinegar, and brown sugar to the skillet. Stir and let the sauce bubble and thicken for 30 to 45 seconds."),
            ("Toss Noodles", "Tumble the drained hot udon noodles and bok choy into the skillet. Toss vigorously with tongs for 1 to 2 minutes until every thick noodle ribbon is glistening and coated in chili garlic glaze."),
            ("Fry Eggs & Serve", "Fry 4 eggs sunny-side up in a separate oiled skillet until whites are set and edges are crisp. Divide spicy udon noodles into bowls, crown each with a fried egg, green scallion tops, and sesame seeds. Break the yolk over the noodles and enjoy!")
        ],
        "pro_tip_title": "Elena’s Frozen Udon Secret",
        "pro_tip": "Always head straight to the freezer aisle for frozen Sanuki udon! Unlike vacuum-sealed shelf-stable packages that can smell sour and break easily, frozen udon is flash-frozen right after kneading, preserving that bouncy, chewy, authentic Japanese noodle texture.",
        "faqs": [
            ("Can I make this vegetarian or vegan?", "Yes! Simply use vegetarian mushroom oyster sauce (stir-fry sauce) in place of traditional oyster sauce."),
            ("How do I control the heat?", "Adjust the chili crunch measurement: start with 1 tablespoon for mild warmth, or add 3+ tablespoons if you crave serious sweat-inducing chili heat!"),
            ("Can I add protein to these noodles?", "Sliced chicken breast, seared shrimp, or crispy browned ground pork or tofu toss into this sauce seamlessly.")
        ],
        "wiki_entities": [
            ("Udon", "https://en.wikipedia.org/wiki/Udon"),
            ("Chili oil", "https://en.wikipedia.org/wiki/Chili_oil"),
            ("Bok choy", "https://en.wikipedia.org/wiki/Bok_choy")
        ],
        "pinterest": {
            "board": "Noodle Recipes / 15-Minute Asian Dinners",
            "title": "15-Minute Spicy Garlic Chili Crunch Udon Noodles",
            "desc": "Chewy Japanese udon noodles tossed in a sizzling garlic chili crunch sauce with baby bok choy and a runny fried egg in 15 minutes! The ultimate weeknight noodle craving. Pin it now!",
            "tags": "#chilicrunch #udon #spicynoodles #15minutedinner #asiannoodles #easyrecipes #quickdinner #noodles"
        }
    },
    {
        "slug": "15-minute-white-cheddar-jalapeno-chicken",
        "title": "15-Minute Creamy White Cheddar Jalapeño Chicken Skillet",
        "headline": "15-Minute Creamy White Cheddar Jalapeño Popper Chicken Skillet",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-10-04",
        "image": "./assets/images/white-cheddar-jalapeno-chicken.jpg",
        "image_file": "white-cheddar-jalapeno-chicken.jpg",
        "excerpt": "Golden pan-seared chicken cutlets smothered in a rich, bubbly sharp white cheddar and charred jalapeño cream sauce with crispy bacon in 15 minutes.",
        "description": "Jalapeño popper flavors in an easy skillet dinner: golden seared chicken breasts bathed in a rich, bubbling sharp white cheddar cream sauce, charred jalapeños, and smoky bacon crumbles.",
        "keywords": "jalapeno popper chicken, white cheddar chicken, 15 minute chicken skillet, creamy jalapeno chicken, low carb chicken dinner, easy weeknight chicken",
        "prepTime": "PT4M",
        "cookTime": "PT11M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Southern American / Tex-Mex",
        "calories": "520 kcal",
        "protein": "42g",
        "fat": "34g",
        "carbs": "6g",
        "fiber": "1g",
        "sodium": "680mg",
        "ratingValue": "4.9",
        "reviewCount": "192",
        "quick_answer": "To make 15-minute creamy white cheddar jalapeño chicken, season 4 thin chicken cutlets (about 1.25 lbs) with garlic powder, smoked paprika, salt, and pepper. Heat 1 tbsp oil in a cast iron skillet over medium-high heat; sear chicken for 3 to 4 minutes per side until golden brown and cooked through (165°F), then transfer to a plate. In the same skillet drippings, sauté 2 thinly sliced jalapeños and 3 minced garlic cloves for 90 seconds until blistered. Lower heat to medium-low, pour in 3/4 cup heavy cream, 2 oz softened cream cheese, and 1 cup shredded sharp white cheddar cheese. Whisk until silky and bubbling. Return chicken to the skillet, spooning the cheese sauce over the top, and shower with 4 strips of crumbled crispy bacon and sliced scallions.",
        "takeaways": [
            ("Thin Cutlet Flash Sear", "Using horizontal thinly sliced chicken cutlets guarantees a golden crust and 165°F internal temperature in just 6 to 7 minutes without drying out."),
            ("Cream Cheese Emulsion Stabilizer", "Adding 2 ounces of softened cream cheese prevents the sharp white cheddar from breaking or getting oily when heated with heavy cream."),
            ("Charred Jalapeño Mellowing", "Sautéing fresh jalapeño rings in the chicken drippings softens their fiery pungency into a smoky, savory warmth.")
        ],
        "matrix_title": "Cheddar Variety Performance in Creamy Skillet Sauces",
        "matrix_headers": ["Cheese Variety", "Melt Smoothness", "Sharpness / Flavor", "Grease Separation", "Verdict"],
        "matrix_rows": [
            ["Sharp White Cheddar (Fresh Grated)", "Ultra-smooth with cream cheese", "Deep, punchy & tangy", "Very low when whisked gently", "Top Flavor Pick (Recommended)"],
            ["Yellow Medium Cheddar", "Smooth", "Mild cheddar flavor", "Low", "Good classic swap"],
            ["Pre-Shredded Bagged Cheddar", "Gritty & powdery (cellulose)", "Muted", "High risk of oil separation", "Avoid (grate from block)"],
            ["Pepper Jack Cheese", "Very melty", "Extra spicy & creamy", "Low", "Great extra-spicy alternative"]
        ],
        "ingredients": [
            "1.25 lbs boneless skinless chicken breasts, sliced horizontally into 4 thin cutlets",
            "1 tbsp olive oil",
            "1 tsp garlic powder & 1/2 tsp smoked paprika",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "2 medium fresh jalapeños, thinly sliced into rings (deseeded for milder heat)",
            "3 cloves fresh garlic, finely minced",
            "3/4 cup heavy whipping cream",
            "2 oz cream cheese, softened to room temperature",
            "1 cup sharp white cheddar cheese, freshly shredded from a block",
            "4 slices cooked bacon, crumbled",
            "2 green onions, sliced, and fresh cilantro for garnish"
        ],
        "instructions": [
            ("Season & Sear Chicken Cutlets", "Pat chicken cutlets dry. Season both sides with garlic powder, smoked paprika, salt, and black pepper. Heat olive oil in a wide cast iron skillet over medium-high heat. Add chicken cutlets and sear for 3.5 minutes per side until golden brown and cooked through (165°F). Transfer to a plate."),
            ("Sauté Jalapeños & Garlic", "Reduce skillet heat to medium. Add sliced jalapeño rings and minced garlic directly into the pan drippings. Sauté for 90 seconds until the jalapeños are softened and lightly blistered."),
            ("Build White Cheddar Sauce", "Reduce heat to low-medium. Pour in heavy cream and whisk in the softened cream cheese until smooth and incorporated. Gradually whisk in the shredded sharp white cheddar cheese in two batches, stirring continuously until the sauce is velvety, bubbling, and melted."),
            ("Return Chicken to Skillet", "Nestle the seared chicken cutlets back into the bubbling white cheddar sauce. Spoon the luxurious sauce over the chicken and simmer gently for 60 seconds to reheat through."),
            ("Garnish with Bacon & Herbs", "Remove from heat. Shower the skillet with crispy bacon crumbles, sliced scallions, and fresh cilantro. Serve hot with steamed rice, roasted broccoli, or crusty bread!")
        ],
        "pro_tip_title": "Elena’s Fresh Grating Mandate",
        "pro_tip": "Never use pre-shredded packaged cheddar cheese for skillet sauces! Store-bought shredded cheese is coated in potato starch and cellulose powder to prevent clumping in the bag, which prevents proper melting and turns your sauce gritty. Grate a block of sharp white cheddar on your box grater—it takes 45 seconds and melts into pure liquid velvet.",
        "faqs": [
            ("How spicy is this dish?", "With seeds and white ribs removed from the jalapeños, it has a mild-to-moderate warmth with savory pepper flavor. For serious heat, leave all the seeds in!"),
            ("Is this recipe keto / low carb friendly?", "Yes! At only 6g net carbs and 42g protein per serving, it is a magnificent high-protein keto dinner option."),
            ("What can I substitute for heavy cream?", "Half-and-half works, but simmer gently and whisk in an extra ounce of cream cheese to maintain the thick, luxurious coating texture.")
        ],
        "wiki_entities": [
            ("Cheddar cheese", "https://en.wikipedia.org/wiki/Cheddar_cheese"),
            ("Jalape%C3%B1o", "https://en.wikipedia.org/wiki/Jalape%C3%B1o"),
            ("Bacon", "https://en.wikipedia.org/wiki/Bacon")
        ],
        "pinterest": {
            "board": "Keto Recipes / Quick Chicken Dinners",
            "title": "15-Minute Creamy White Cheddar Jalapeño Chicken Skillet",
            "desc": "Golden seared chicken cutlets in a bubbling sharp white cheddar cream sauce with charred jalapeños and crispy bacon in 15 minutes! Insanely delicious weeknight comfort. Pin it now!",
            "tags": "#jalapenochicken #whitecheddar #chickenskillet #15minutedinner #ketorecipes #lowcarbdinner #easyrecipes"
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes (Batch 9) ===")
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
