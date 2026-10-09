import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
DB_PATH = os.path.join(BASE_DIR, "articles_database.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

NEW_RECIPES = [
    # 1. Mummy Hot Dog Crescent Bites
    {
        "slug": "20-minute-mummy-hot-dog-crescent-bites",
        "title": "20-Minute Mummy Hot Dog Crescent Bites",
        "headline": "20-Minute Mummy Hot Dog Crescent Bites",
        "badge": "Quick & Easy &bull; 20 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/mummy-hot-dog-crescent-bites.jpg",
        "image_file": "mummy-hot-dog-crescent-bites.jpg",
        "excerpt": "Golden buttery crescent dough wrapped around juicy smoked beef franks to look like adorable Halloween mummies, baked until flaky and finished with mustard dot eyes in 20 minutes.",
        "description": "Adorable and crispy 20-minute mummy hot dog crescent bites baked to golden perfection with flaky pastry strips and finished with tiny mustard eyes. The ultimate crowd-pleasing Halloween appetizer.",
        "keywords": "mummy hot dogs, halloween crescent appetizers, 20 minute halloween snacks, easy party bites, halloween party food",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "16 mummy bites (4-6 servings)",
        "recipeCategory": "Appetizer",
        "recipeCuisine": "American Party Food",
        "calories": "285 kcal",
        "protein": "11g",
        "fat": "18g",
        "carbs": "20g",
        "fiber": "1g",
        "sodium": "520mg",
        "ratingValue": "4.9",
        "reviewCount": "164",
        "quick_answer": "To make 20-minute mummy hot dog crescent bites, unroll 1 can of refrigerated crescent dough, press the perforations together, and slice into thin 1/4-inch strips using a pizza wheel. Wrap 8 bun-length all-beef hot dogs (halved crosswise) with strips in an overlapping spiral, leaving a 1/2-inch gap near the top for the face. Brush with melted butter and bake on a parchment-lined sheet pan at 375°F (190°C) for 13 to 15 minutes until deep golden brown and flaky. Dot with yellow mustard or ketchup for eyes before serving hot.",
        "takeaways": [
            ("Pizza Cutter Speed Hack", "Use a rolling pizza wheel rather than a knife to slice crescent sheet dough into uniform strips in under 30 seconds without tearing."),
            ("Face Gap Precision", "Leave a distinct 1/2-inch bare gap near the upper third of each frank so the mummy face shows clearly after baking."),
            ("Melted Butter Wash", "Brushing the dough lightly with melted butter before baking guarantees a glossy, deeply golden, flaky pastry crust.")
        ],
        "matrix_title": "Hot Dog & Sausage Selection for Crescent Mummy Bites",
        "matrix_headers": ["Meat Type", "Juiciness", "Bake Puff Time", "Skin Crispness", "Best Fit"],
        "matrix_rows": [
            ["All-Beef Franks", "High & savory", "13-15 Mins", "Excellent snap", "Top Pick for Classic Party Flavor (Recommended)"],
            ["Cocktail Smokies (Lit'l Smokies)", "Tender bite-sized", "12-14 Mins", "Soft bite", "Great for Finger-Food Platter"],
            ["Turkey Dogs", "Leaner moisture", "13-15 Mins", "Mild snap", "Light Protein Alternative"],
            ["Cheddar Jalapeño Sausage", "Ultra-juicy & spicy", "15 Mins", "Caramelized edges", "Grown-Up Halloween Twist"]
        ],
        "ingredients": [
            "8 bun-length all-beef hot dogs (or 16 cocktail smokies), halved crosswise",
            "1 can (8 oz) refrigerated crescent dinner roll dough (or crescent sheet)",
            "1.5 tbsp unsalted butter, melted",
            "1 tbsp yellow mustard or spicy brown mustard (for piping eyes)",
            "1/4 cup ketchup or smoky barbecue sauce (for dipping)",
            "Pinch of flaky sea salt (optional for pastry tops)"
        ],
        "instructions": [
            ("Preheat & Prep Sheet Pan", "Preheat oven to 375°F (190°C). Line a large rimmed baking sheet with parchment paper or silicone baking mat."),
            ("Cut Dough Strips", "Unroll crescent dough onto a clean cutting board; pinch seams firmly to seal. Using a pizza cutter or sharp chef's knife, cut lengthwise into 32 thin ribbons approximately 1/4-inch wide."),
            ("Wrap Mummy Dogs", "Halve the hot dogs crosswise. Wrap 2 strips of dough around each half frank, crisscrossing to simulate bandages and leaving an open 1/2-inch window near the top for the mummy eyes."),
            ("Bake to Flaky Golden", "Place wrapped mummies onto the prepared sheet pan spaced 1 inch apart. Lightly brush pastry strips with melted butter. Bake for 13 to 15 minutes until crescent dough is puffed and golden brown."),
            ("Dot Eyes & Serve", "Remove from oven and let rest 2 minutes. Dip a toothpick into yellow mustard and dot two eyes onto each mummy's exposed face. Serve warm with ketchup, mustard, or BBQ dip.")
        ],
        "pro_tip_title": "Elena’s Toothpick Mustard Dot Trick",
        "pro_tip": "Never squeeze mustard directly from the bottle onto the hot dog—it creates giant blobs. Pour a spoonful into a ramekin and use a round wooden toothpick as a paintbrush to stamp pinpoint, cartoonish yellow eyes onto each mummy bite!",
        "faqs": [
            ("Can I make mummy hot dog crescent bites ahead of time?", "Yes! You can assemble and wrap the unbaked mummies up to 6 hours in advance, cover them tightly on the sheet pan, and chill in the fridge. Bake directly from cold, adding 2 extra minutes."),
            ("What is the best dough to use?", "Refrigerated seamless crescent dough sheets are ideal because they require zero seam-pinching. Standard perforated crescent rolls work equally well when pinched smooth."),
            ("How do I keep leftover mummy dogs crispy?", "Store leftovers in an airtight container for up to 3 days. Reheat in an air fryer at 350°F for 3 minutes or toaster oven at 375°F for 5 minutes to restore the flaky crispness.")
        ],
        "about_entities": [
            ("Hot dog", "https://en.wikipedia.org/wiki/Hot_dog"),
            ("Crescent roll", "https://en.wikipedia.org/wiki/Croissant"),
            ("Hors d'oeuvre", "https://en.wikipedia.org/wiki/Hors_d%27oeuvre")
        ]
    },

    # 2. Spiderweb Taco Dip Skillet
    {
        "slug": "15-minute-spiderweb-taco-dip-skillet",
        "title": "15-Minute Spiderweb Taco Dip Skillet",
        "headline": "15-Minute Spiderweb Taco Dip Skillet",
        "badge": "One-Pot Dinners &bull; 15 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners quick-and-easy 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/spiderweb-taco-dip-skillet.jpg",
        "image_file": "spiderweb-taco-dip-skillet.jpg",
        "excerpt": "A warm, bubbling skillet layered with seasoned taco beef, refried black beans, and melted Mexican cheese, topped with an intricately piped sour cream spiderweb and olive spider in 15 minutes.",
        "description": "Fun, viral, and outrageously cheesy 15-minute spiderweb taco dip skillet baked in a cast-iron skillet with seasoned taco beef, black beans, and melted cheese, finished with a piped sour cream web.",
        "keywords": "spiderweb taco dip, halloween taco dip skillet, 15 minute party dip, warm cast iron dip, easy halloween appetizers",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "6-8 party servings",
        "recipeCategory": "Appetizer / Party Dip",
        "recipeCuisine": "Tex-Mex",
        "calories": "340 kcal",
        "protein": "19g",
        "fat": "22g",
        "carbs": "17g",
        "fiber": "4g",
        "sodium": "640mg",
        "ratingValue": "4.9",
        "reviewCount": "182",
        "quick_answer": "To make a 15-minute spiderweb taco dip skillet, brown 1 lb lean ground beef in a 10-inch oven-safe skillet with 2 tbsp taco seasoning for 5 minutes. Stir in 1 can warm refried beans and 1/2 cup chunky salsa. Spread smooth, top with 2 cups shredded Mexican cheese blend, and broil on HIGH for 3 to 4 minutes until bubbling and melted. Spoon sour cream into a zip-top bag with the corner snipped; pipe 4 concentric circles on the melted cheese and drag a toothpick outward from center to rim to form a spiderweb. Top with an olive spider and serve immediately with tortilla chips.",
        "takeaways": [
            ("Oven-Safe Cast Iron Advantage", "Cooking the beef and melting the cheese directly in a cast iron skillet retains piping heat at the party table for over 30 minutes."),
            ("Toothpick Drag Technique", "Pipe circles of sour cream while the cheese is warm, then pull a toothpick lightly outward from center to edge at 8 radial angles to create instant spiderweb webbing."),
            ("Pitted Olive Spider Hack", "Halve one black olive lengthwise for the spider body, slice another olive into thin slivers for 8 spider legs, and arrange right in the web center.")
        ],
        "matrix_title": "Taco Dip Base & Cheese Melting Performance",
        "matrix_headers": ["Layering Style", "Melt Uniformity", "Scoop Sturdiness", "Warmth Retention", "Best Pick"],
        "matrix_rows": [
            ["Cast-Iron Baked Ground Beef & Cheddar", "Bubbling & gooey", "Excellent heavy scoop", "30+ Mins in Skillet", "Top Pick for Warm Crowd Dip (Recommended)"],
            ["Chilled Refried Bean & Guacamole", "No melt", "Moderate", "Cold party dip", "Best for Summertime BBQ"],
            ["Spicy Chorizo & Pepper Jack", "Spicy oil rendering", "High scoop strength", "25 Mins in Skillet", "Bold Punchy Flavor"],
            ["Black Bean & Corn Vegetarian", "Soft & melty", "Good with thick chips", "20 Mins in Skillet", "Wholesome Meatless Option"]
        ],
        "ingredients": [
            "1 lb 90/10 lean ground beef (or ground turkey)",
            "1 packet (2 tbsp) low-sodium taco seasoning",
            "1 can (15 oz) refried black beans or traditional pinto beans",
            "1/2 cup thick restaurant-style chunky salsa",
            "2 cups shredded Mexican 4-cheese blend (or sharp cheddar and Monterey Jack)",
            "1/2 cup sour cream (at room temperature)",
            "2 whole pitted jumbo black olives (for the olive spider)",
            "2 tbsp chopped fresh cilantro & 1 jalapeño, seeded and diced",
            "1 bag sturdy corn tortilla chips for serving"
        ],
        "instructions": [
            ("Brown Taco Beef", "Preheat oven broiler to HIGH. Heat a 10-inch cast-iron skillet over medium-high heat. Add ground beef, break apart with a wooden spoon, and sear for 5 minutes until browned. Drain excess fat, stir in taco seasoning and 3 tbsp water, and simmer 1 minute."),
            ("Layer Beans & Salsa", "Stir refried beans and chunky salsa directly into the seasoned beef skillet until smoothly combined and warmed through. Smooth surface flat with an offset spatula."),
            ("Melt Cheese Under Broiler", "Scatter 2 cups shredded Mexican cheese blend evenly over the entire surface. Transfer skillet to the top oven rack and broil 3 to 4 minutes until cheese is completely melted and bubbly."),
            ("Pipe Sour Cream Spiderweb", "Transfer sour cream into a small ziplock bag and snip a tiny corner hole. Pipe 4 concentric circles on the melted cheese. Take a toothpick and drag lines from the center ring outwards to the edge in 8 spokes to reveal a sharp spiderweb pattern."),
            ("Assemble Olive Spider & Garnish", "Cut 1 olive in half lengthwise to create the spider head and oval abdomen. Slice the second olive into 8 thin strips for spider legs. Assemble the spider in the center of the web. Sprinkle cilantro and jalapeños around the perimeter. Serve hot with tortilla chips!")
        ],
        "pro_tip_title": "Elena’s Room-Temperature Crema Tip",
        "pro_tip": "If sour cream is ice cold straight from the fridge, it will seize and chill the melted cheese instantly upon contact. Let your sour cream sit on the counter for 10 minutes, stir in 1 tsp milk or lime juice to thin it out, and piping smooth spiderweb lines will be effortless!",
        "faqs": [
            ("Can I make this taco dip vegetarian?", "Easily! Replace ground beef with a can of seasoned pinto or black beans tossed with taco seasoning, or use plant-based ground crumbles."),
            ("How do I stop the spiderweb from melting away?", "Let the skillet sit for 2 minutes after broiling before piping the sour cream. When the cheese is warm (rather than boiling hot), the sour cream retains razor-sharp linework."),
            ("Can I reheat this dip skillet?", "Yes! Place the entire cast iron skillet in a 350°F oven for 7 to 8 minutes until heated through. You can re-pipe sour cream lines if needed.")
        ],
        "about_entities": [
            ("Taco", "https://en.wikipedia.org/wiki/Taco"),
            ("Cast-iron cookware", "https://en.wikipedia.org/wiki/Cast-iron_cookware"),
            ("Spiderweb", "https://en.wikipedia.org/wiki/Spider_web")
        ]
    },

    # 3. Mini Pumpkin Cheese Ball Bites
    {
        "slug": "20-minute-mini-pumpkin-cheese-ball-bites",
        "title": "20-Minute Mini Pumpkin Cheese Ball Bites",
        "headline": "20-Minute Mini Pumpkin Cheese Ball Bites",
        "badge": "Quick & Easy &bull; 20 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/mini-pumpkin-cheese-ball-bites.jpg",
        "image_file": "mini-pumpkin-cheese-ball-bites.jpg",
        "excerpt": "Adorable bite-sized sharp cheddar cheese balls rolled in smoky crushed tortilla chips, shaped into mini pumpkins with pretzel stems and fresh parsley leaves in 20 minutes.",
        "description": "Charming, no-bake 20-minute mini pumpkin cheese ball bites made with sharp cheddar, cream cheese, and garlic herb seasoning, rolled in vibrant crunchy nacho coating with pretzel stems.",
        "keywords": "mini pumpkin cheese balls, halloween cheese ball bites, 20 minute fall appetizers, mini party pumpkins, easy finger food",
        "prepTime": "PT20M",
        "cookTime": "PT0M",
        "totalTime": "PT20M",
        "recipeYield": "12 mini pumpkins (6 servings)",
        "recipeCategory": "Appetizer",
        "recipeCuisine": "American Autumn Appetizer",
        "calories": "195 kcal",
        "protein": "7g",
        "fat": "16g",
        "carbs": "6g",
        "fiber": "1g",
        "sodium": "280mg",
        "ratingValue": "4.9",
        "reviewCount": "147",
        "quick_answer": "To make 20-minute mini pumpkin cheese ball bites, beat 8 oz softened cream cheese with 1.5 cups finely shredded sharp cheddar, 2 tbsp minced scallions, 1/2 tsp garlic powder, 1/4 tsp smoked paprika, and a pinch of cayenne. Scoop into 12 rounded balls (about 1.5 tbsp each). Roll each ball in 1 cup finely crushed nacho cheese tortilla chips combined with smoked paprika for vivid orange color. Press 4 rubber bands or use a toothpick to indent 6 to 8 vertical ridges into each ball to create pumpkin grooves. Insert a broken pretzel stick into the top for the stem and tuck a flat parsley leaf beside it. Serve chilled with crackers.",
        "takeaways": [
            ("Nacho Chip Crush Color", "Crushing Doritos or nacho cheese tortilla chips with smoked paprika provides a naturally vibrant orange crust that stays ultra-crisp without food coloring."),
            ("Toothpick Ridge Grooving", "Gently pressing the side of a wooden skewer or toothpick vertically around the sphere creates instant realistic pumpkin lobes in seconds."),
            ("Pretzel & Herb Stems", "Snap standard pretzel sticks into 1-inch lengths and pair each with a flat parsley leaf for a rustic autumnal edible stem.")
        ],
        "matrix_title": "Coating Texture & Color Comparison for Mini Pumpkin Cheese Bites",
        "matrix_headers": ["Coating Type", "Orange Color Intensity", "Crunch Factor", "Holding Power", "Verdict"],
        "matrix_rows": [
            ["Crushed Nacho Tortilla Chips + Paprika", "Vivid natural orange", "High crunch", "Holds 6+ hours", "Top Pick for Flavor & Visuals (Recommended)"],
            ["Toasted Finely Chopped Pecans", "Golden rustic brown", "Buttery crunch", "Holds overnight", "Best for Sophisticated Wine Pairing"],
            ["Crushed Cheddar Crackers (Goldfish)", "Bright cheerful orange", "Tender crisp", "Holds 4 hours", "Fun Kid-Friendly Option"],
            ["Smoked Paprika & Breadcrumbs", "Deep brick orange", "Light dust", "Softens faster", "Mild & Subtle"]
        ],
        "ingredients": [
            "8 oz cream cheese, softened to room temperature",
            "1.5 cups sharp cheddar cheese, very finely shredded",
            "2 green scallions, white and tender green parts finely minced",
            "1/2 tsp garlic powder & 1/4 tsp onion powder",
            "1/2 tsp smoked paprika (divided: 1/4 tsp inside, 1/4 tsp in coating)",
            "1/4 tsp kosher salt & pinch of cayenne pepper",
            "1 cup nacho cheese tortilla chips, finely crushed into crumbs",
            "6 pretzel sticks, snapped in half (for 12 stems)",
            "12 small flat-leaf Italian parsley leaves",
            "Assorted gourmet seed crackers or pita chips for serving"
        ],
        "instructions": [
            ("Mix Cheese Base", "In a medium mixing bowl, beat softened cream cheese, finely shredded cheddar, minced scallions, garlic powder, onion powder, 1/4 tsp smoked paprika, salt, and cayenne using a fork or hand mixer until thoroughly blended and creamy."),
            ("Portion Spheres", "Using a 1.5-tablespoon cookie scoop, portion the mixture into 12 even mounds onto a parchment-lined tray. Roll gently between clean palms to form smooth round spheres."),
            ("Roll in Crunchy Orange Coating", "In a shallow bowl, combine finely crushed nacho chips and remaining 1/4 tsp smoked paprika. Roll each cheese ball in the mixture, pressing gently so the crumbs adhere completely."),
            ("Indent Pumpkin Grooves", "Using the smooth edge of a wooden toothpick or butter knife, press gently into the sides from bottom to top to create 6 to 8 indented vertical lobes around each sphere."),
            ("Stem & Garnish", "Press a 1-inch snapped pretzel stick firmly into the top center of each pumpkin bite. Tuck a small parsley leaf right next to the pretzel stem. Chill in the fridge until ready to serve alongside artisan crackers.")
        ],
        "pro_tip_title": "Elena’s 5-Minute Freezer Firming Trick",
        "pro_tip": "If your hands warm up the cream cheese while rolling, pop the portioned cheese balls into the freezer for exactly 5 minutes before pressing the ridges. They will become firm enough to carve sharp pumpkin lobes without getting smudged!",
        "faqs": [
            ("Can I make mini pumpkin cheese balls ahead of time?", "Yes! Shape the cheese balls and coat them up to 24 hours in advance and keep refrigerated in an airtight container. Insert pretzel stems right before serving so the pretzels stay crunchy."),
            ("Can I use goat cheese or white cheddar?", "Absolutely. You can swap half the cream cheese for goat cheese or sharp white cheddar for a tangier, upscale flavor profile."),
            ("How long do leftovers last?", "Keep in an airtight container in the refrigerator for up to 5 days. Crackers and leftover pretzels can be kept separately.")
        ],
        "about_entities": [
            ("Cheese ball", "https://en.wikipedia.org/wiki/Cheese_ball"),
            ("Cheddar cheese", "https://en.wikipedia.org/wiki/Cheddar_cheese"),
            ("Pumpkin", "https://en.wikipedia.org/wiki/Pumpkin")
        ]
    },

    # 4. Crispy Buffalo Chicken Meatballs
    {
        "slug": "15-minute-crispy-buffalo-chicken-meatballs",
        "title": "15-Minute Crispy Buffalo Chicken Meatballs",
        "headline": "15-Minute Crispy Buffalo Chicken Meatballs",
        "badge": "Quick & Easy &bull; 15 Mins",
        "category": "Quick & Easy",
        "categories_str": "all quick-and-easy 30-minute-meals comfort-food",
        "read_time": "15 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/crispy-buffalo-chicken-meatballs.jpg",
        "image_file": "crispy-buffalo-chicken-meatballs.jpg",
        "excerpt": "Crispy pan-seared ground chicken meatballs drenched in zesty amber-red buffalo glaze, drizzled with cool ranch and crumbled blue cheese in 15 minutes.",
        "description": "Golden, caramelized, and intensely flavorful 15-minute crispy buffalo chicken meatballs tossed in zesty garlic butter hot sauce, finished with cool ranch crema and blue cheese.",
        "keywords": "buffalo chicken meatballs, 15 minute party meatballs, crispy chicken bites, easy buffalo glaze, weeknight dinner meatballs",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings (approx. 16 meatballs)",
        "recipeCategory": "Main Course / Appetizer",
        "recipeCuisine": "American Game Day",
        "calories": "385 kcal",
        "protein": "32g",
        "fat": "24g",
        "carbs": "8g",
        "fiber": "1g",
        "sodium": "790mg",
        "ratingValue": "4.9",
        "reviewCount": "193",
        "quick_answer": "To make 15-minute crispy buffalo chicken meatballs, mix 1 lb ground chicken with 1/3 cup panko breadcrumbs, 1 egg, 2 cloves minced garlic, 1/2 tsp onion powder, and 1/2 tsp salt. Shape into 16 golf ball-sized meatballs. Sear in a hot skillet with 1 tbsp olive oil over medium-high heat for 6 to 8 minutes, rolling frequently until deeply browned and cooked through to 165°F (74°C). Lower heat, pour in 1/3 cup Frank's RedHot sauce whisked with 2 tbsp melted butter, and toss until glossy and caramelized. Transfer to a platter, drizzle with ranch or blue cheese dressing, and top with sliced scallions.",
        "takeaways": [
            ("Panko Moisture Sponge", "Using panko breadcrumbs with one egg prevents lean ground chicken from drying out, keeping the interior juicy while developing a crispy outer sear."),
            ("Butter-Mellowed Buffalo Glaze", "Whisking melted butter into cayenne hot pepper sauce emulsifies the glaze into a velvety sauce that clings tightly to hot meatball crusts."),
            ("Rolling Sear Technique", "Swirl the pan gently every 90 seconds so the round meatballs develop an all-over golden crust without flattening.")
        ],
        "matrix_title": "Ground Poultry & Sear Performance for Fast Meatballs",
        "matrix_headers": ["Meat Type", "Sear Speed", "Interior Juiciness", "Sauce Cling", "Best Fit"],
        "matrix_rows": [
            ["Ground Chicken Thigh (92/8)", "Fast golden browning", "Ultra-juicy & tender", "Maximum cling", "Top Pick for Restaurant-Style Juiciness (Recommended)"],
            ["Ground Chicken Breast (98/2)", "Moderate browning", "Lean & dense", "Great with butter glaze", "Healthy High-Protein Pick"],
            ["Ground Turkey (93/7)", "Rapid caramelized crust", "Moist & firm", "Excellent cling", "Readily Available Substitute"],
            ["Plant-Based Ground Poultry", "Gentle browning", "Tender", "Good cling", "Vegetarian Adaptation"]
        ],
        "ingredients": [
            "1 lb ground chicken (preferably 92/8 dark/white blend)",
            "1/3 cup panko breadcrumbs",
            "1 large egg, lightly beaten",
            "3 cloves fresh garlic, finely minced",
            "1/2 tsp onion powder & 1/2 tsp kosher salt",
            "1/4 tsp freshly cracked black pepper",
            "1.5 tbsp olive oil or neutral oil (for pan searing)",
            "1/3 cup Frank's RedHot pepper sauce (or favorite cayenne hot sauce)",
            "2 tbsp unsalted butter, melted",
            "3 tbsp cool ranch dressing or blue cheese crema (for drizzling)",
            "2 tbsp crumbled Gorgonzola or blue cheese",
            "2 green scallions, thinly sliced"
        ],
        "instructions": [
            ("Mix Meatball Mixture", "In a medium bowl, combine ground chicken, panko, beaten egg, minced garlic, onion powder, salt, and pepper. Gently mix with hands or a fork just until incorporated (do not over-compact)."),
            ("Shape Meatballs", "Moisten hands slightly with water and roll mixture into 16 evenly sized round meatballs (about 1.5-inch diameter)."),
            ("Crisp in Hot Skillet", "Heat olive oil in a large 12-inch nonstick or cast-iron skillet over medium-high heat. Add meatballs in a single layer. Sear for 7 to 8 minutes, turning every 2 minutes with tongs until all sides are deeply browned and internal temp reaches 165°F (74°C)."),
            ("Glaze in Buffalo Butter", "Reduce skillet heat to low. Whisk hot sauce and melted butter together, then pour directly over the meatballs. Shake the pan vigorously for 60 to 90 seconds until the sauce bubbles into a sticky, glossy lacquer coating every meatball."),
            ("Garnish & Serve", "Transfer meatballs onto a warm serving platter. Drizzle with cool ranch dressing, scatter crumbled blue cheese, and top with fresh scallions. Serve sizzling hot with toothpicks!")
        ],
        "pro_tip_title": "Elena’s Wet Hands Rolling Secret",
        "pro_tip": "Ground chicken is naturally much stickier than beef. Keep a small bowl of cold water beside you and dip your fingers before shaping each meatball. The meat will glide effortlessly between your palms into perfectly smooth spheres without clinging to your skin!",
        "faqs": [
            ("Can I bake these meatballs in the oven?", "Yes! Preheat oven to 425°F (220°C). Place meatballs on a greased baking sheet and bake for 10 to 12 minutes until cooked through. Toss in hot buffalo butter sauce right before serving."),
            ("Can I make these in an air fryer?", "Air fry at 400°F (200°C) for 8 to 9 minutes, shaking the basket halfway through. Transfer to a bowl and toss with the warm buffalo sauce."),
            ("What can I serve with these meatballs for a complete meal?", "Pair with steamed Jasmine rice, a crisp celery and romaine salad, or tuck into mini brioche slider rolls with slaw for 15-minute game-day sliders!")
        ],
        "about_entities": [
            ("Buffalo wing", "https://en.wikipedia.org/wiki/Buffalo_wing"),
            ("Meatball", "https://en.wikipedia.org/wiki/Meatball"),
            ("Blue cheese", "https://en.wikipedia.org/wiki/Blue_cheese")
        ]
    },

    # 5. Sheet-Pan BBQ Chicken Nachos
    {
        "slug": "20-minute-sheet-pan-bbq-chicken-nachos",
        "title": "20-Minute Sheet-Pan BBQ Chicken Nachos",
        "headline": "20-Minute Sheet-Pan BBQ Chicken Nachos",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals comfort-food",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/sheet-pan-bbq-chicken-nachos.jpg",
        "image_file": "sheet-pan-bbq-chicken-nachos.jpg",
        "excerpt": "Loaded sheet-pan nachos with crunchy corn tortilla chips, shredded smoky BBQ chicken, melted sharp cheddar, black beans, sweet corn, and pickled jalapeños in 20 minutes.",
        "description": "An epic 20-minute sheet-pan dinner featuring crispy corn tortilla chips piled high with smoky pulled barbecue chicken, sweet corn, black beans, double melted cheese, and creamy drizzle.",
        "keywords": "sheet pan bbq chicken nachos, 20 minute sheet pan dinner, loaded nachos, easy party nachos, bbq chicken sheet pan",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4-6 servings",
        "recipeCategory": "Main Course / Party Food",
        "recipeCuisine": "American Barbecue Fusion",
        "calories": "520 kcal",
        "protein": "34g",
        "fat": "26g",
        "carbs": "41g",
        "fiber": "5g",
        "sodium": "780mg",
        "ratingValue": "4.9",
        "reviewCount": "171",
        "quick_answer": "To make 20-minute sheet-pan BBQ chicken nachos, preheat oven to 400°F (200°C). Toss 2 cups shredded rotisserie chicken with 1/2 cup smoky barbecue sauce. Spread 1 bag (10 oz) thick restaurant-style tortilla chips across a large parchment-lined rimmed sheet pan. Scatter half of 2.5 cups shredded Monterey Jack and sharp cheddar cheese over chips. Top evenly with the BBQ chicken, 1/2 cup rinsed black beans, 1/2 cup sweet corn, and thin red onion rings. Cover with remaining cheese. Bake for 10 to 12 minutes until cheese is bubbly and edges are toasted. Drizzle with sour cream crema and extra BBQ sauce, then top with pickled jalapeños and fresh cilantro.",
        "takeaways": [
            ("Two-Tier Cheese Blanket Strategy", "Layer cheese both underneath and on top of the shredded chicken to lock the chips into an unbreakable, crisp foundation that never gets soggy."),
            ("Rotisserie Chicken Speed", "Using pre-cooked rotisserie chicken breast shredded and tossed in sweet hickory BBQ sauce eliminates all meat prep time."),
            ("Sturdy Restaurant Chips", "Always select thick-cut corn tortilla chips; light airy chips will bend and break under generous melted cheese and toppings.")
        ],
        "matrix_title": "Tortilla Chip Structure for Loaded Sheet Pan Nachos",
        "matrix_headers": ["Chip Style", "Thickness", "Soggy Resistance", "Salsa/Dip Scooping", "Verdict"],
        "matrix_rows": [
            ["Thick-Cut Stone Ground Corn Chips", "Heavy gauge", "High resistance (stays crisp)", "Superior scoop strength", "Top Pick for Sheet Pan Suppers (Recommended)"],
            ["Cantina / Restaurant Thin Chips", "Delicate", "Moderate to low", "Prone to snapping", "Best for light salsa dipping only"],
            ["Blue Corn Tortilla Chips", "Medium-heavy", "High resistance", "Hearty nutty crunch", "Striking visual contrast"],
            ["Grain-Free / Cassava Chips", "Thin", "Low under heavy cheese", "Gentle scoop", "Great for specialty diets"]
        ],
        "ingredients": [
            "1 bag (10-12 oz) thick restaurant-style corn tortilla chips",
            "2 cups cooked shredded chicken breast (rotisserie works wonderfully)",
            "1/2 cup smoky sweet barbecue sauce (plus 2 tbsp for drizzling)",
            "1.5 cups shredded Monterey Jack cheese",
            "1 cup shredded sharp cheddar cheese",
            "1/2 cup canned black beans, rinsed and drained",
            "1/2 cup sweet corn kernels (fresh or thawed frozen)",
            "1/3 cup red onion, thinly sliced into rings",
            "1/4 cup pickled sliced jalapeños",
            "1/4 cup sour cream mixed with 1 tsp lime juice (crema drizzle)",
            "1/4 cup fresh cilantro leaves, roughly chopped"
        ],
        "instructions": [
            ("Preheat & Prep Pan", "Preheat oven to 400°F (200°C). Line a large 18x13-inch rimmed half sheet pan with parchment paper."),
            ("Sauce the Chicken", "In a medium bowl, toss shredded chicken with 1/2 cup barbecue sauce until thoroughly coated and glossy."),
            ("Layer Chips & Base Cheese", "Spread tortilla chips in an even layer across the sheet pan, slightly overlapping. Scatter half of the combined shredded cheeses (1.25 cups) evenly over the chips."),
            ("Distribute Toppings & Top Cheese", "Evenly spoon sauced chicken, drained black beans, sweet corn, and red onion over the cheesy chips. Cover with the remaining 1.25 cups of cheese to bind the toppings."),
            ("Bake to Melt & Garnish", "Bake for 10 to 12 minutes until cheese is completely melted, bubbling, and the chip tips are lightly toasted golden. Remove from oven. Drizzle with sour cream crema and extra BBQ sauce; top with pickled jalapeños and chopped cilantro. Serve hot right from the pan!")
        ],
        "pro_tip_title": "Elena’s Center-Heat Layering Secret",
        "pro_tip": "Avoid dumping all toppings into the center mound! Arrange chips in a wide single layer with toppings spread edge-to-edge. This ensures every individual chip gets an equal ratio of melted sharp cheese, smoky chicken, and sweet corn without any naked chips left behind.",
        "faqs": [
            ("How do I prevent sheet-pan nachos from getting soggy?", "Bake at 400°F (high heat) and never add wet cold toppings (like guacamole, sour cream, or salsa) before baking. Add cold sauces as fresh drizzles right before eating!"),
            ("Can I make this with leftover pulled pork?", "Absolutely! Leftover pulled pork or smoked brisket works spectacularly well in place of chicken with zero changes to baking time."),
            ("Can I re-crisp leftover nachos?", "Yes! Spread leftovers back onto a sheet pan and bake in a 375°F oven or air fryer for 4 to 5 minutes to regain their original snap.")
        ],
        "about_entities": [
            ("Nachos", "https://en.wikipedia.org/wiki/Nachos"),
            ("Barbecue chicken", "https://en.wikipedia.org/wiki/Barbecue_chicken"),
            ("Sheet pan", "https://en.wikipedia.org/wiki/Sheet_pan")
        ]
    },

    # 6. Roasted Butternut Squash Pasta with Brown Butter Sage
    {
        "slug": "20-minute-roasted-butternut-squash-pasta-brown-butter-sage",
        "title": "20-Minute Roasted Butternut Squash Pasta with Brown Butter Sage",
        "headline": "20-Minute Roasted Butternut Squash Pasta with Brown Butter Sage",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners comfort-food 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/roasted-butternut-squash-pasta-brown-butter-sage.jpg",
        "image_file": "roasted-butternut-squash-pasta-brown-butter-sage.jpg",
        "excerpt": "Tender rigatoni pasta bathed in a silky roasted butternut squash puree infused with nutty hazelnut-brown butter, crispy fried sage, and toasted pecans in 20 minutes.",
        "description": "Luxurious 20-minute autumn pasta featuring al dente rigatoni tossed in velvety brown butter butternut squash cream with crispy fried sage leaves and shaved Parmigiano-Reggiano.",
        "keywords": "butternut squash pasta, brown butter sage pasta, 20 minute fall dinner, creamy squash pasta, easy autumn weeknight meals",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCuisine": "Northern Italian Autumn",
        "recipeCategory": "Main Course",
        "calories": "475 kcal",
        "protein": "14g",
        "fat": "21g",
        "carbs": "61g",
        "fiber": "5g",
        "sodium": "440mg",
        "ratingValue": "4.9",
        "reviewCount": "188",
        "quick_answer": "To make 20-minute roasted butternut squash pasta with brown butter sage, boil 12 oz rigatoni or paccheri pasta in salted water for 10 minutes until al dente, reserving 3/4 cup starchy pasta water. Meanwhile, melt 4 tbsp unsalted butter in a wide skillet over medium heat until nutty and foaming with amber brown specks (3 minutes); fry 10 whole fresh sage leaves for 45 seconds until crisp, then set aside. Whisk 1.5 cups smooth butternut squash puree, 1/3 cup heavy cream, 2 cloves minced garlic, a pinch of freshly grated nutmeg, and 1/2 cup pasta water into the brown butter. Simmer 2 minutes, toss with hot pasta and 1/2 cup grated Parmigiano-Reggiano, and garnish with crispy sage and toasted pecans.",
        "takeaways": [
            ("Canned Squash Shortcut", "Using 100% pure canned butternut squash puree cuts out 40 minutes of squash roasting while maintaining deeply rich sweet flavor."),
            ("Nutty Brown Butter Emulsion", "Allowing butter to foam until milk solids turn golden amber releases aromatic hazelnut aromas that elevate squash puree to restaurant caliber."),
            ("Starchy Pasta Water Magic", "Reserved starchy pasta cooking water emulsifies the cream and squash puree into a glossy, clingy sauce that coats every pasta ridge.")
        ],
        "matrix_title": "Pasta Shapes for Clinging Velvety Squash Puree",
        "matrix_headers": ["Pasta Shape", "Sauce Cling Rating", "Chew Profile", "Pocket Capacity", "Verdict"],
        "matrix_rows": [
            ["Rigatoni (Rigati ridges)", "10/10 (Superb)", "Firm al dente tubular chew", "Holds puree inside & outside", "Top Pick for Brown Butter Squash (Recommended)"],
            ["Fettuccine / Pappardelle", "9/10 (High)", "Silky ribbon mouthfeel", "Wide flat coating surface", "Elegant Dinner Party Classic"],
            ["Orecchiette (Little Ears)", "9/10 (High)", "Dense satisfying bite", "Scoops puree like little bowls", "Rustic Country Style"],
            ["Penne Rigate", "8/10 (Very Good)", "Standard bite", "Good internal hold", "Dependable Pantry Staple"]
        ],
        "ingredients": [
            "12 oz rigatoni, penne rigate, or pappardelle pasta",
            "4 tbsp unsalted European-style butter",
            "10-12 fresh whole sage leaves",
            "1.5 cups pure butternut squash puree (canned or fresh pre-steamed)",
            "1/3 cup heavy whipping cream or full-fat coconut milk",
            "2 cloves fresh garlic, finely minced",
            "1/4 tsp freshly grated whole nutmeg",
            "1/2 cup freshly grated Parmigiano-Reggiano cheese (plus more for serving)",
            "1/3 cup chopped pecans or walnuts, toasted",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper"
        ],
        "instructions": [
            ("Boil Pasta", "Bring a large pot of salted water to a rolling boil. Add rigatoni and cook 10 minutes until al dente. Reserve 3/4 cup starchy pasta cooking water, then drain pasta."),
            ("Crisp Sage & Brown Butter", "While pasta cooks, melt butter in a large deep skillet over medium heat. Add whole sage leaves and sizzle for 45 seconds until crisp and fragrant. Transfer crispy sage leaves with a fork to a paper towel. Continue swirling butter in skillet for another 1 to 2 minutes until milk solids turn golden brown with a nutty hazelnut aroma."),
            ("Build Velvety Sauce", "Lower heat to medium-low. Add minced garlic and cook 30 seconds until fragrant. Whisk in butternut squash puree, heavy cream, nutmeg, salt, black pepper, and 1/2 cup of reserved hot pasta water. Simmer gently for 2 minutes until hot and velvety."),
            ("Toss & Emulsify", "Add cooked rigatoni and grated Parmigiano-Reggiano to the skillet. Toss vigorously over low heat for 1 minute until sauce clings glossily to every noodle, adding remaining splash of pasta water if needed."),
            ("Garnish & Serve", "Divide pasta into warm shallow bowls. Top with crispy fried sage leaves, toasted pecans, and extra freshly grated Parmesan. Serve immediately!")
        ],
        "pro_tip_title": "Elena’s Fresh Nutmeg Finishing Secret",
        "pro_tip": "Always grate fresh whole nutmeg with a microplane directly over the simmering squash sauce rather than using pre-ground bottled nutmeg. The essential oils in fresh nutmeg cut through the rich butter and illuminate the natural sweetness of the squash!",
        "faqs": [
            ("Can I make this dairy-free or vegan?", "Yes! Substitute butter with plant-based butter (like Miyoko's), use full-fat canned coconut milk for heavy cream, and finish with nutritional yeast or vegan Parmesan."),
            ("Can I add protein to this dish?", "Crispy pancetta cubes, crumbled Italian sausage, or pan-seared chicken breast pair exquisitely with the brown butter squash sauce."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 4 days. Reheat on the stovetop with 2 tbsp of milk or water over medium-low heat to loosen the sauce back to velvety smoothness.")
        ],
        "about_entities": [
            ("Butternut squash", "https://en.wikipedia.org/wiki/Butternut_squash"),
            ("Beurre noisette", "https://en.wikipedia.org/wiki/Beurre_noisette"),
            ("Rigatoni", "https://en.wikipedia.org/wiki/Rigatoni")
        ]
    },

    # 7. Creamy Butternut Squash Soup
    {
        "slug": "15-minute-creamy-butternut-squash-soup",
        "title": "15-Minute Creamy Butternut Squash Soup",
        "headline": "15-Minute Creamy Butternut Squash Soup",
        "badge": "One-Pot Dinners &bull; 15 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners comfort-food 30-minute-meals",
        "read_time": "15 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/creamy-butternut-squash-soup.jpg",
        "image_file": "creamy-butternut-squash-soup.jpg",
        "excerpt": "Velvety smooth, golden butternut squash soup simmered with warm ginger, nutmeg, and rich cream, finished with crunchy pepitas and fried sage in 15 minutes.",
        "description": "Ultra-comforting and silky 15-minute creamy butternut squash soup infused with sautéed shallots, warm ground ginger, and velvety cream, topped with roasted pepitas and crisp sage.",
        "keywords": "creamy butternut squash soup, 15 minute squash soup, quick fall soup, easy blended soup, butternut squash bisque",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "recipeYield": "4 servings",
        "recipeCategory": "Soup",
        "recipeCuisine": "American Autumn Comfort",
        "calories": "260 kcal",
        "protein": "5g",
        "fat": "15g",
        "carbs": "29g",
        "fiber": "5g",
        "sodium": "490mg",
        "ratingValue": "4.9",
        "reviewCount": "159",
        "quick_answer": "To make 15-minute creamy butternut squash soup, sauté 1 minced shallot and 2 cloves garlic in 2 tbsp butter in a medium pot for 2 minutes. Stir in two 15-oz cans pure butternut squash puree, 2.5 cups low-sodium vegetable or chicken broth, 1/4 tsp ground ginger, 1/4 tsp cinnamon, and 1/8 tsp nutmeg. Simmer for 6 to 8 minutes over medium heat. Stir in 1/2 cup heavy cream (or coconut cream) and 1 tbsp pure maple syrup until silky and steaming. Ladle into bowls and garnish with a cream swirl, toasted pepitas, and fried sage leaves.",
        "takeaways": [
            ("No-Peel Puree Shortcut", "Starting with organic canned butternut squash puree avoids the dangerous struggle of peeling, seeding, and cubing raw rock-hard squash."),
            ("Ginger & Maple Balance", "A touch of ground ginger and real maple syrup cuts the earthy squash starch and brings vibrant warmth to the broth."),
            ("Crunchy Pepitas Contrast", "Toasted salted pumpkin seeds (pepitas) provide the crucial textural contrast against the ultra-silky pureed broth.")
        ],
        "matrix_title": "Butternut Squash Soup Liquid Bases & Creaminess",
        "matrix_headers": ["Liquid Base", "Texture Profile", "Richness Level", "Flavor Depth", "Best For"],
        "matrix_rows": [
            ["Vegetable Broth + Heavy Cream", "Silky & velvety", "Luxurious classic", "Warm balanced savory-sweet", "Top Pick for Traditional Bisque (Recommended)"],
            ["Chicken Bone Broth + Heavy Cream", "Deep & savory", "High protein richness", "Robust savory undertone", "Hearty Autumn Dinner"],
            ["Coconut Milk + Curry Broth", "Thick & tropical", "Plant-based indulgence", "Fragrant sweet-spicy kick", "Thai-Inspired Autumn Twist"],
            ["Almond Milk + Olive Oil", "Light & brothy", "Low calorie", "Delicate squash flavor", "Light Clean-Eating Starter"]
        ],
        "ingredients": [
            "2 cans (15 oz each) 100% pure butternut squash puree",
            "2.5 cups low-sodium vegetable broth (or chicken broth)",
            "2 tbsp unsalted butter or extra virgin olive oil",
            "1 large shallot, finely diced",
            "2 cloves fresh garlic, minced",
            "1/2 cup heavy whipping cream (or full-fat canned coconut milk)",
            "1 tbsp pure amber maple syrup",
            "1/4 tsp ground ginger & 1/4 tsp ground cinnamon",
            "1/8 tsp freshly grated nutmeg",
            "1/2 tsp kosher salt & 1/4 tsp white pepper (or black pepper)",
            "3 tbsp roasted salted pumpkin seeds (pepitas) for garnish",
            "4 fresh sage leaves fried in olive oil (optional)"
        ],
        "instructions": [
            ("Aromatics Sauté", "Melt butter in a medium Dutch oven or soup pot over medium heat. Add diced shallot and cook 2 minutes until translucent and soft. Stir in minced garlic and cook 30 seconds until aromatic."),
            ("Simmer Broth & Squash", "Whisk in butternut squash puree, vegetable broth, maple syrup, ginger, cinnamon, nutmeg, salt, and pepper. Bring to a lively simmer, reduce heat to medium-low, and simmer gently for 6 to 7 minutes to meld flavors."),
            ("Stir in Cream", "Stir in heavy cream until completely integrated into a luminous golden-orange velvet bisque. Simmer 1 additional minute until piping hot (do not boil hard)."),
            ("Immersion Blend (Optional)", "For restaurant-level silkiness, pulse an immersion blender in the pot for 30 seconds to emulsify the shallots and butter completely."),
            ("Garnish & Serve", "Ladle hot soup into warm bowls. Drizzle with a swirl of heavy cream, scatter crunchy pepitas, and top with a fried sage leaf. Serve with crusty sourdough bread.")
        ],
        "pro_tip_title": "Elena’s Maple-Cider Splash Trick",
        "pro_tip": "If your squash puree tastes slightly flat or earthy, add 1 teaspoon of apple cider vinegar right alongside the maple syrup! That tiny hit of malic acid makes the soup taste like fresh-harvested autumn orchard squash.",
        "faqs": [
            ("Can I freeze this butternut squash soup?", "Yes! Let cool completely and store in freezer-safe containers for up to 3 months. If using dairy cream, reheat gently over low heat while whisking so the dairy doesn't separate."),
            ("How do I make this completely vegan?", "Swap butter for olive oil and use full-fat canned coconut cream in place of heavy whipping cream. It adds a subtle nutty sweetness that tastes amazing!"),
            ("Can I use frozen squash chunks?", "Yes. Microwave frozen butternut squash cubes for 5 minutes until soft, then blend with broth before adding to the pot.")
        ],
        "about_entities": [
            ("Butternut squash", "https://en.wikipedia.org/wiki/Butternut_squash"),
            ("Soup", "https://en.wikipedia.org/wiki/Soup"),
            ("Pepita", "https://en.wikipedia.org/wiki/Pepita")
        ]
    },

    # 8. One-Pot Lasagna Soup
    {
        "slug": "20-minute-one-pot-lasagna-soup",
        "title": "20-Minute One-Pot Lasagna Soup",
        "headline": "20-Minute One-Pot Lasagna Soup",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners comfort-food 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/one-pot-lasagna-soup.jpg",
        "image_file": "one-pot-lasagna-soup.jpg",
        "excerpt": "All the rich flavors of classic baked lasagna made in one pot in 20 minutes: savory herb beef tomato broth, wavy lasagna noodles, and melted dollops of ricotta.",
        "description": "Rich, comforting, and hearty 20-minute one-pot lasagna soup cooked in a robust herb-tomato beef broth with broken lasagna noodles, finished with melting ricotta and mozzarella.",
        "keywords": "one pot lasagna soup, 20 minute lasagna soup, easy weeknight soup, italian beef soup, comfort food lasagna",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4-6 servings",
        "recipeCategory": "Main Course Soup",
        "recipeCuisine": "Italian-American Comfort",
        "calories": "495 kcal",
        "protein": "36g",
        "fat": "21g",
        "carbs": "42g",
        "fiber": "4g",
        "sodium": "780mg",
        "ratingValue": "4.9",
        "reviewCount": "210",
        "quick_answer": "To make 20-minute one-pot lasagna soup, brown 1 lb lean ground beef (or Italian sausage) in a large pot with 1 diced onion and 3 minced garlic cloves for 5 minutes. Stir in 1 tbsp tomato paste, 1 tbsp Italian seasoning, 1 jar (24 oz) marinara sauce, 4 cups chicken or beef broth, and 1/2 tsp salt. Bring to a rolling boil, break 8 dry lasagna noodles into 2-inch pieces, and drop them into the pot. Cook uncovered for 9 to 10 minutes until pasta is tender. Remove from heat, stir in 1/2 cup heavy cream, ladle into bowls, and top with a big dollop of whole-milk ricotta, shredded mozzarella, and fresh torn basil.",
        "takeaways": [
            ("Noodles Cook Directly in Broth", "Simmering broken lasagna noodles straight in the marinara broth releases starch, naturally thickening the soup into a rich, stew-like consistency."),
            ("Ricotta Cheese Crown", "Dolloping cool seasoned ricotta and mozzarella directly on top of piping hot soup mimics the golden baked cheese layer of traditional lasagna."),
            ("Tomato Paste Caramelization", "Cooking tomato paste in the browned beef fat before adding liquid builds deep, slow-simmered umami in under 60 seconds.")
        ],
        "matrix_title": "Ground Meat Blend for 20-Minute Lasagna Soup",
        "matrix_headers": ["Meat Selection", "Fat Rendering", "Flavor Profile", "Broth Body", "Best Pick"],
        "matrix_rows": [
            ["Half Italian Sausage & Half Lean Ground Beef", "Ideal balanced fat", "Fennel & garlic rich", "Savory & robust", "Top Pick for Authentic Bakery Flavor (Recommended)"],
            ["100% Lean Ground Beef (90/10)", "Low grease", "Classic savory beef", "Clean broth", "Quick High-Protein Option"],
            ["Sweet Mild Ground Italian Sausage", "Juicy & fragrant", "Herby pork sweetness", "Glossy finish", "Ultra Comforting"],
            ["Ground Turkey Breast", "Very low fat", "Mild poultry base", "Lighter soup", "Lean Healthy Swap"]
        ],
        "ingredients": [
            "1 lb lean ground beef or sweet Italian pork sausage",
            "1 medium yellow onion, finely diced",
            "4 cloves fresh garlic, minced",
            "2 tbsp tomato paste",
            "1 tbsp dried Italian seasoning (basil, oregano, thyme)",
            "1 jar (24 oz) quality marinara sauce (such as Rao's)",
            "4 cups low-sodium chicken or beef broth",
            "8 curly dry lasagna noodles, broken into 2-inch bite-sized pieces",
            "1/3 cup heavy whipping cream (optional, for silkiness)",
            "3/4 cup whole-milk ricotta cheese",
            "1 cup shredded low-moisture mozzarella cheese",
            "1/3 cup grated Parmigiano-Reggiano",
            "1/4 cup fresh basil leaves, torn"
        ],
        "instructions": [
            ("Brown Meat & Aromatics", "Heat a large Dutch oven or heavy soup pot over medium-high heat. Add ground beef and diced onion; cook 5 minutes until meat is browned, breaking into crumbles. Add minced garlic and cook 1 minute. Drain excess fat if needed."),
            ("Build Rich Tomato Broth", "Stir tomato paste and Italian seasoning into the meat, stirring constantly for 1 minute until darkened. Pour in marinara sauce and broth, stirring up any browned bits from the pan bottom. Bring to a rolling boil."),
            ("Simmer Broken Noodles", "Add broken lasagna noodle pieces into the boiling soup. Reduce heat to medium, stirring occasionally to prevent noodles from sticking together. Simmer uncovered for 9 to 10 minutes until pasta is tender and cooked through."),
            ("Season & Add Cream", "Remove pot from heat. Stir in heavy cream and season with salt and freshly ground black pepper to taste."),
            ("Garnish & Serve", "Ladle steaming soup into large bowls. Crown each bowl with a heaping dollop of creamy ricotta, a handful of shredded mozzarella, grated Parmesan, and fresh basil leaves. The cheeses will melt into gooey ribbons as you eat!")
        ],
        "pro_tip_title": "Elena’s Staggered Noodle Stirring Secret",
        "pro_tip": "When snapping dried lasagna noodles, break them randomly into 2-inch rough pieces and drop them into the boiling pot a few at a time while stirring vigorously. This prevents the flat noodle pieces from stacking on top of each other and forming gummy clumps!",
        "faqs": [
            ("Can I cook the noodles separately?", "If you plan on having leftovers, yes! Boiling noodles separately prevents them from soaking up all the broth in the fridge. Drop cooked noodles into individual bowls and ladle hot soup over top."),
            ("What can I substitute for lasagna noodles?", "Campanelle, mafaldine, rotini, or farfalle pasta make wonderful substitutes that cook in the exact same 9 to 10 minute window."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 4 days. When reheating, add 1/2 cup of broth or water as the pasta naturally absorbs liquid while chilling.")
        ],
        "about_entities": [
            ("Lasagna", "https://en.wikipedia.org/wiki/Lasagne"),
            ("Soup", "https://en.wikipedia.org/wiki/Soup"),
            ("Ricotta", "https://en.wikipedia.org/wiki/Ricotta")
        ]
    },

    # 9. One-Pot Creamy Chicken and Wild Rice Soup
    {
        "slug": "20-minute-creamy-chicken-wild-rice-soup",
        "title": "20-Minute One-Pot Creamy Chicken and Wild Rice Soup",
        "headline": "20-Minute One-Pot Creamy Chicken and Wild Rice Soup",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners comfort-food 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/creamy-chicken-wild-rice-soup.jpg",
        "image_file": "creamy-chicken-wild-rice-soup.jpg",
        "excerpt": "Cozy, rustic chicken soup loaded with tender pulled chicken breast, nutty wild rice, aromatic herbs, and a velvety cream broth in just 20 minutes.",
        "description": "Panera-style copycat 20-minute creamy chicken and wild rice soup made in one pot with shredded chicken, earthy wild rice blend, celery, carrots, and silky cream broth.",
        "keywords": "creamy chicken and wild rice soup, 20 minute chicken soup, panera copycat wild rice soup, one pot soup, cozy weeknight chicken soup",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4-6 servings",
        "recipeCategory": "Main Course Soup",
        "recipeCuisine": "American Midwest Comfort",
        "calories": "390 kcal",
        "protein": "29g",
        "fat": "18g",
        "carbs": "28g",
        "fiber": "3g",
        "sodium": "620mg",
        "ratingValue": "4.9",
        "reviewCount": "197",
        "quick_answer": "To make 20-minute one-pot creamy chicken and wild rice soup, melt 3 tbsp butter in a Dutch oven over medium heat and sauté 1 diced onion, 2 diced carrots, and 2 sliced celery ribs for 4 minutes. Whisk in 1/4 cup flour and cook for 1 minute to form a roux. Slowly whisk in 4 cups chicken broth, 1 cup half-and-half, 1 tsp dried thyme, and 1/2 tsp garlic powder until smooth. Stir in 2 cups shredded cooked chicken breast and 1.5 cups pre-cooked wild rice blend (such as microwavable Uncle Ben's Ready Rice). Simmer for 8 minutes until thick and velvety. Season with salt and black pepper and serve warm.",
        "takeaways": [
            ("Pre-Cooked Wild Rice Secret", "Real raw wild rice takes 45 to 50 minutes to simmer. Using pre-cooked ready-to-heat wild rice pouches unlocks the exact same nutty texture in just 8 minutes."),
            ("Roux Velvet Foundation", "Cooking equal parts butter and flour creates a smooth blond roux that thickens the broth into a rich Panera-style velvety chowder."),
            ("Mirepoix Base Aromatics", "Sautéing onion, carrot, and celery in butter builds the foundational French mirepoix aromatic profile essential for homestyle chicken soup.")
        ],
        "matrix_title": "Rice Selection for 20-Minute Creamy Chicken Soup",
        "matrix_headers": ["Rice Product", "Cook Speed", "Nutty Chew", "Starch Thickening", "Best Fit"],
        "matrix_rows": [
            ["Pre-Cooked Long Grain & Wild Rice Pouch", "Ready in 5 mins", "High nutty bite", "Gentle thickening", "Top Pick for Weeknight Speed (Recommended)"],
            ["Parboiled Quick-Cooking Wild Rice", "15 mins simmer", "Moderate chew", "Good starch release", "Traditional Stove Prep"],
            ["Raw Unprocessed Black Wild Rice", "45-55 mins", "Dense rustic hull", "Heavy broth tint", "Too slow for 20-minute dinners"],
            ["Brown Jasmine Rice Blend", "Ready in 5 mins", "Mild floral chew", "Silky broth", "Delicate Alternative"]
        ],
        "ingredients": [
            "2 cups cooked shredded chicken breast (rotisserie chicken)",
            "1.5 cups pre-cooked wild rice blend (1 pouch microwave ready-rice, unheated)",
            "3 tbsp unsalted butter",
            "1 medium yellow onion, finely diced",
            "2 medium carrots, peeled and sliced into thin coins",
            "2 stalks celery, thinly sliced",
            "3 cloves garlic, minced",
            "1/4 cup all-purpose flour",
            "4 cups low-sodium chicken broth",
            "1 cup half-and-half or heavy cream",
            "1 tsp dried thyme leaves",
            "1/2 tsp poultry seasoning & 1/2 tsp onion powder",
            "1 tsp kosher salt & 1/2 tsp freshly cracked black pepper",
            "2 tbsp fresh flat-leaf parsley, chopped"
        ],
        "instructions": [
            ("Sauté Mirepoix", "Melt butter in a large soup pot or Dutch oven over medium heat. Add diced onion, carrots, and celery. Cook for 4 to 5 minutes until vegetables begin to soften. Add minced garlic and cook 30 seconds."),
            ("Form Roux", "Sprinkle flour over the vegetables and stir continuously for 1 to 2 minutes to cook off raw flour taste and coat the vegetables in a blond paste."),
            ("Whisk Liquids & Season", "Gradually pour in chicken broth in a steady stream while whisking vigorously to dissolve flour with no lumps. Pour in half-and-half, dried thyme, poultry seasoning, salt, and pepper. Bring to a gentle boil, stirring frequently as the broth thickens."),
            ("Add Chicken & Rice", "Stir in shredded chicken and pre-cooked wild rice. Reduce heat to medium-low and simmer gently for 7 to 8 minutes until carrots are tender and the soup is thick, creamy, and bubbling."),
            ("Season & Garnish", "Taste and adjust seasoning with salt and pepper. Ladle into warm bowls and garnish with fresh parsley. Serve hot alongside warm buttered sourdough rolls.")
        ],
        "pro_tip_title": "Elena’s Lemon Zest Finish Secret",
        "pro_tip": "Right before ladling into bowls, stir in 1/2 teaspoon of fresh lemon zest and 1 teaspoon of lemon juice. The acidity cuts through the heavy cream and butter, bringing vibrant balance to the earthy wild rice!",
        "faqs": [
            ("Can I make this dairy-free?", "Yes! Swap butter for olive oil and use unsweetened full-fat oat milk or canned coconut cream in place of half-and-half."),
            ("How do I keep the rice from absorbing all the soup?", "Pre-cooked wild rice holds its structure much better than white rice. If reheating the next day, simply splash in 1/4 cup of chicken broth to restore the desired consistency."),
            ("Can I freeze this soup?", "Soups thickened with a flour roux and dairy freeze moderately well. To freeze best, cool completely and freeze for up to 2 months; reheat gently on low heat while stirring.")
        ],
        "about_entities": [
            ("Wild rice", "https://en.wikipedia.org/wiki/Wild_rice"),
            ("Chicken soup", "https://en.wikipedia.org/wiki/Chicken_soup"),
            ("Mirepoix", "https://en.wikipedia.org/wiki/Mirepoix")
        ]
    },

    # 10. Creamy Apple Cider Chicken Skillet
    {
        "slug": "20-minute-creamy-apple-cider-chicken-skillet",
        "title": "20-Minute Creamy Apple Cider Chicken Skillet",
        "headline": "20-Minute Creamy Apple Cider Chicken Skillet",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners comfort-food 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/creamy-apple-cider-chicken-skillet.jpg",
        "image_file": "creamy-apple-cider-chicken-skillet.jpg",
        "excerpt": "Golden pan-seared chicken cutlets simmering in a luscious spiced apple cider cream reduction with caramelized Honeycrisp apples and fresh sage in 20 minutes.",
        "description": "Sensational 20-minute fall dinner featuring crispy golden chicken cutlets bathed in a silky apple cider Dijon cream sauce with caramelized crisp apples and fragrant fresh sage.",
        "keywords": "apple cider chicken skillet, creamy fall chicken dinner, 20 minute chicken skillet, one pan apple chicken, autumn chicken recipes",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American Autumn Farmhouse",
        "calories": "440 kcal",
        "protein": "38g",
        "fat": "22g",
        "carbs": "21g",
        "fiber": "2g",
        "sodium": "490mg",
        "ratingValue": "4.9",
        "reviewCount": "173",
        "quick_answer": "To make 20-minute creamy apple cider chicken skillet, season 1.25 lbs thin chicken cutlets with garlic powder, salt, and pepper; sear in 1.5 tbsp olive oil in a skillet over medium-high heat for 3 to 4 minutes per side until golden (165°F), then set aside. In the same skillet, melt 1 tbsp butter and sauté 1 sliced Honeycrisp apple and 1 sliced shallot for 3 minutes until tender. Pour in 3/4 cup unfiltered apple cider, scraping up browned bits, and reduce by half (3 minutes). Stir in 1/2 cup heavy cream, 1 tbsp Dijon mustard, and 1 tbsp chopped fresh sage; simmer 2 minutes until sauce is glossy and velvety. Return chicken to pan to coat and serve hot.",
        "takeaways": [
            ("Unfiltered Fresh Cider Reduction", "Using unfiltered spiced apple cider reduced by half concentrates natural apple sugars, creating an intensely autumnal sweet-savory glaze."),
            ("Dijon Mustard Emulsion", "Whisking Dijon mustard into the cider reduction bridges sweet fruit notes and savory cream, preventing the sauce from becoming cloyingly sweet."),
            ("Firm Honeycrisp Apple Slices", "Honeycrisp or Pink Lady apples hold their crisp shape during skillet sautéing without dissolving into applesauce.")
        ],
        "matrix_title": "Apple Varieties for Skillet Sautéing with Poultry",
        "matrix_headers": ["Apple Variety", "Texture Retention", "Sweet/Tart Balance", "Caramelization", "Verdict"],
        "matrix_rows": [
            ["Honeycrisp", "Superior crisp hold", "Juicy honey sweetness", "Quick amber edges", "Top Pick for Apple Cider Chicken (Recommended)"],
            ["Pink Lady (Cripps Pink)", "Firm dense flesh", "Tart effervescent punch", "Golden caramelization", "Excellent Tart Contrast"],
            ["Granny Smith", "Firm hold", "Very tart & acidic", "Moderate browning", "Great if you prefer tangy sauces"],
            ["Red Delicious", "Mealy & soft", "Bland sweetness", "Breaks down fast", "Avoid for skillet sautéing"]
        ],
        "ingredients": [
            "1.25 lbs boneless skinless chicken breasts (cut into thin cutlets)",
            "1 medium Honeycrisp or Pink Lady apple, cored and thinly sliced into wedges",
            "1 large shallot, thinly sliced",
            "2 tbsp olive oil (divided)",
            "1 tbsp unsalted butter",
            "3/4 cup unfiltered pure apple cider (not apple cider vinegar)",
            "1/2 cup heavy whipping cream",
            "1 tbsp Dijon mustard (preferably whole-grain or smooth)",
            "1 tbsp fresh sage leaves, finely chopped (plus whole leaves for garnish)",
            "1/2 tsp garlic powder & 1/2 tsp onion powder",
            "3/4 tsp kosher salt & 1/2 tsp freshly cracked black pepper"
        ],
        "instructions": [
            ("Season & Sear Cutlets", "Pat chicken cutlets dry. Season both sides with garlic powder, onion powder, 1/2 tsp salt, and 1/4 tsp pepper. Heat 1.5 tbsp olive oil in a large 12-inch cast-iron skillet over medium-high heat. Sear chicken 3 to 4 minutes per side until golden brown and internal temp reaches 165°F (74°C). Transfer chicken to a warm plate."),
            ("Caramelize Apples & Shallot", "Reduce heat to medium. Add butter and sliced apples and shallots to the skillet. Sauté for 3 minutes until apples begin to caramelize and edges are golden and crisp-tender. Remove half the apple slices to plate with chicken for plating."),
            ("Deglaze with Apple Cider", "Pour apple cider into the skillet, scraping up all browned fond from the bottom with a wooden spoon. Let boil vigorously for 3 to 4 minutes until cider reduces by half into a syrupy amber glaze."),
            ("Whisk Cider Cream Sauce", "Lower heat to medium-low. Whisk in heavy cream, Dijon mustard, chopped fresh sage, remaining 1/4 tsp salt, and pepper. Simmer gently for 2 minutes until sauce is glossy and lightly coats the back of a spoon."),
            ("Reheat & Serve", "Return seared chicken cutlets and reserved apple slices into the skillet. Spoon creamy cider sauce generously over the chicken to reheat for 1 minute. Garnish with fresh sage leaves and cracked pepper. Serve hot over mashed potatoes or buttered egg noodles!")
        ],
        "pro_tip_title": "Elena’s Fond Deglazing Flavor Trick",
        "pro_tip": "Those golden-brown crispy bits stuck to the bottom of the skillet after searing chicken are pure umami gold! When you pour in the cold apple cider, scrape vigorously with a flat wooden spatula—the browned chicken juices dissolve right into the cider reduction for unmatched savory depth.",
        "faqs": [
            ("Can I use hard apple cider?", "Yes! Dry hard cider or dry white wine works wonderfully. It will result in a slightly crisper, less sweet pan sauce."),
            ("What are the best side dishes for this chicken?", "Garlic mashed Yukon Gold potatoes, roasted green beans, or buttered pappardelle egg noodles are ideal to soak up every drop of the cider cream sauce."),
            ("Can I use chicken thighs instead of cutlets?", "Yes! Boneless skinless chicken thighs work brilliantly. Sear thighs for 5 to 6 minutes per side until internal temperature reaches 175°F.")
        ],
        "about_entities": [
            ("Apple cider", "https://en.wikipedia.org/wiki/Apple_cider"),
            ("Chicken breast", "https://en.wikipedia.org/wiki/Chicken_as_food"),
            ("Cast-iron cookware", "https://en.wikipedia.org/wiki/Cast-iron_cookware")
        ]
    },

    # 11. Sheet-Pan Sausage with Apples and Brussels Sprouts
    {
        "slug": "20-minute-sheet-pan-sausage-apples-brussels-sprouts",
        "title": "20-Minute Sheet-Pan Sausage with Apples and Brussels Sprouts",
        "headline": "20-Minute Sheet-Pan Sausage with Apples and Brussels Sprouts",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers comfort-food 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/sheet-pan-sausage-apples-brussels-sprouts.jpg",
        "image_file": "sheet-pan-sausage-apples-brussels-sprouts.jpg",
        "excerpt": "Caramelized smoked kielbasa sausage, crispy charred Brussels sprouts, and tender sweet apples roasted together on a sheet pan with a tangy maple Dijon glaze in 20 minutes.",
        "description": "Crispy, savory, and sweet 20-minute sheet-pan sausage supper featuring sliced smoked kielbasa, charred halved Brussels sprouts, caramelized apples, and red onions in a maple mustard glaze.",
        "keywords": "sheet pan sausage and apples, brussels sprouts sausage sheet pan, 20 minute sheet pan dinner, maple dijon kielbasa, easy autumn sheet pan",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "American Autumn Sheet Pan",
        "calories": "460 kcal",
        "protein": "21g",
        "fat": "27g",
        "carbs": "33g",
        "fiber": "6g",
        "sodium": "740mg",
        "ratingValue": "4.9",
        "reviewCount": "165",
        "quick_answer": "To make 20-minute sheet-pan sausage with apples and Brussels sprouts, preheat oven to 450°F (230°C) with a rimmed baking sheet inside. Slice 14 oz smoked kielbasa into 1/2-inch bias rounds; halve 1 lb small Brussels sprouts, cut 2 crisp sweet apples into wedges, and cut 1 red onion into wedges. Toss all ingredients on a large tray with 2 tbsp olive oil, 1.5 tbsp maple syrup, 1 tbsp Dijon mustard, 1/2 tsp garlic powder, salt, and black pepper. Spread across the hot preheated sheet pan in a single layer with sprouts cut-side down. Roast for 12 to 14 minutes, then broil on high for 2 minutes until sausage edges are caramelized and sprouts are deeply charred and crispy.",
        "takeaways": [
            ("Hot Pan Sprouts Charring", "Preheating the baking sheet creates instant sear when halved Brussels sprouts hit the metal, producing crispy charred leaves in half the usual roasting time."),
            ("Sweet-Savory Maple Dijon Glaze", "Tossing everything with maple syrup and Dijon mustard caramelizes under high heat, coating the salty smoked sausage and tart apples in an amber glaze."),
            ("Bias Cut Sausage Surface Area", "Slicing kielbasa on a steep diagonal (bias) exposes 30% more surface area for maximum crispy edge browning.")
        ],
        "matrix_title": "Sausage Selections for High-Heat Sheet Pan Roasting",
        "matrix_headers": ["Sausage Style", "Pre-Cooked Status", "Charring Speed", "Juiciness", "Best Fit"],
        "matrix_rows": [
            ["Smoked Polish Kielbasa (Pork/Beef)", "Fully cooked", "Blistering in 12 mins", "Ultra juicy & smoky", "Top Pick for Autumn Sweet-Savory Glaze (Recommended)"],
            ["Smoked Turkey Kielbasa", "Fully cooked", "Crisp in 12 mins", "Lean & savory", "Great Low-Fat Protein"],
            ["Chicken Apple Sausage", "Fully cooked", "Caramelized in 10 mins", "Sweet fruity notes", "Double-Apple Flavor Harmony"],
            ["Raw Italian Sausage Links", "Raw meat", "Requires 22-25 mins", "High grease release", "Too slow for 20-minute dinners"]
        ],
        "ingredients": [
            "14 oz smoked Polish kielbasa or smoked sausage, sliced on a bias into 1/2-inch rounds",
            "1 lb small Brussels sprouts, trimmed and halved lengthwise",
            "2 crisp sweet apples (such as Honeycrisp, Gala, or Fuji), cored and cut into 1/2-inch wedges",
            "1 medium red onion, cut into 1/2-inch wedges",
            "2 tbsp extra virgin olive oil",
            "1.5 tbsp pure maple syrup",
            "1 tbsp Dijon mustard",
            "1/2 tsp garlic powder & 1/2 tsp smoked paprika",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper",
            "1 tbsp fresh thyme leaves or chopped fresh parsley for garnish"
        ],
        "instructions": [
            ("Preheat Blazing Sheet Pan", "Place an 18x13-inch rimmed metal baking sheet on the center oven rack and preheat oven to 450°F (230°C)."),
            ("Chop & Prep Ingredients", "Slice kielbasa into 1/2-inch diagonal rounds. Trim and halve Brussels sprouts. Cut apples and red onion into wedges."),
            ("Toss with Maple Mustard Glaze", "In a large bowl, whisk olive oil, maple syrup, Dijon mustard, garlic powder, smoked paprika, salt, and pepper. Add sliced sausage, sprouts, apples, and onions; toss until evenly coated."),
            ("Spread Cut-Side Down on Hot Pan", "Carefully pull the smoking-hot sheet pan from the oven. Pour the mixture onto the pan (listen to that immediate sizzle!). Quickly use tongs to flip most Brussels sprouts cut-side down against the hot metal in a single layer."),
            ("Roast & Broil to Crisp", "Roast at 450°F for 12 to 14 minutes. Switch oven to HIGH BROIL for 90 to 120 seconds until sausage edges are caramelized and sprout edges are deeply charred. Garnish with fresh thyme and flaky salt; serve hot straight from the sheet pan!")
        ],
        "pro_tip_title": "Elena’s Cut-Side Down Sizzle Secret",
        "pro_tip": "Taking 60 seconds to flip halved Brussels sprouts cut-side down against the blazing metal sheet pan makes the difference between soggy boiled sprouts and shattering, caramelized restaurant-style roasted sprouts!",
        "faqs": [
            ("Should I peel the apples?", "No! Leaving the skin on keeps apple slices firm and structurally intact while adding gorgeous autumn color to your dinner platter."),
            ("Can I make this in an air fryer?", "Yes! Air fry in two batches at 400°F (200°C) for 9 to 10 minutes, shaking the basket halfway through."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 4 days. Reheat in a dry skillet over medium-high heat or air fryer at 380°F for 3 minutes to regain crisp edges.")
        ],
        "about_entities": [
            ("Kielbasa", "https://en.wikipedia.org/wiki/Kielbasa"),
            ("Brussels sprout", "https://en.wikipedia.org/wiki/Brussels_sprout"),
            ("Sheet pan", "https://en.wikipedia.org/wiki/Sheet_pan")
        ]
    },

    # 12. Sheet-Pan Maple Dijon Salmon and Sweet Potatoes
    {
        "slug": "20-minute-sheet-pan-maple-dijon-salmon-sweet-potatoes",
        "title": "20-Minute Sheet-Pan Maple Dijon Salmon and Sweet Potatoes",
        "headline": "20-Minute Sheet-Pan Maple Dijon Salmon and Sweet Potatoes",
        "badge": "Sheet Pan Suppers &bull; 20 Mins",
        "category": "Sheet Pan Suppers",
        "categories_str": "all sheet-pan-suppers 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/sheet-pan-maple-dijon-salmon-sweet-potatoes.jpg",
        "image_file": "sheet-pan-maple-dijon-salmon-sweet-potatoes.jpg",
        "excerpt": "Flaky wild-caught salmon fillets brushed with sweet and tangy maple Dijon mustard, roasted alongside thin crispy sweet potato rounds and crisp green beans in 20 minutes.",
        "description": "Healthy, colorful, and restaurant-quality 20-minute sheet-pan dinner featuring flaky roasted salmon fillets glazed in maple Dijon mustard, alongside caramelized sweet potato coins and green beans.",
        "keywords": "sheet pan maple dijon salmon, 20 minute salmon dinner, salmon sweet potatoes sheet pan, healthy weeknight seafood, maple glazed salmon",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Pacific Northwest Seafood",
        "calories": "480 kcal",
        "protein": "37g",
        "fat": "22g",
        "carbs": "35g",
        "fiber": "5g",
        "sodium": "510mg",
        "ratingValue": "4.9",
        "reviewCount": "184",
        "quick_answer": "To make 20-minute sheet-pan maple Dijon salmon and sweet potatoes, preheat oven to 425°F (220°C). Slice 1 large sweet potato into thin 1/4-inch rounds and toss with 1 tbsp olive oil, salt, and pepper; microwave for 2 minutes to par-cook. Spread sweet potato rounds and 8 oz trimmed green beans on a parchment-lined sheet pan and roast for 7 minutes. Whisk 2 tbsp pure maple syrup, 1.5 tbsp whole grain Dijon mustard, 1 minced garlic clove, and 1 tsp soy sauce. Place 4 salmon fillets (6 oz each) in the center of the pan and brush generously with glaze. Roast together for 8 to 10 minutes until salmon flakes with a fork and edges are caramelized.",
        "takeaways": [
            ("2-Minute Sweet Potato Par-Steam", "Sweet potatoes normally take 35 minutes to roast. Microwaving thin rounds for 2 minutes softens starches so they caramelize on the sheet pan in just 15 minutes."),
            ("Whole Grain Dijon Glaze Balance", "Coarse whole grain mustard seeds toast under high heat, providing crunchy pops of acidity that cut through rich salmon fats."),
            ("Staggered Roasting Timing", "Roasting vegetables for 7 minutes first ensures tender caramelization without drying out tender salmon fillets.")
        ],
        "matrix_title": "Salmon Varieties & Glaze Performance for Sheet Pan Roasting",
        "matrix_headers": ["Salmon Type", "Fat Content", "Flake Texture", "Glaze Caramelization", "Verdict"],
        "matrix_rows": [
            ["Atlantic Salmon (Farmed or Wild)", "High rich omega-3 fat", "Buttery silky flakes", "Deep mahogany caramel", "Top Pick for Juicy Tender Finish (Recommended)"],
            ["Wild Sockeye Salmon", "Moderate lean fat", "Firm dense ruby flakes", "Rapid sear (pull at 8 mins)", "Vibrant Bold Flavor"],
            ["Wild Coho Salmon", "Medium fat", "Delicate tender chew", "Balanced golden glaze", "Mild & Elegant"],
            ["Steelhead Trout", "High healthy fat", "Tender pink flake", "Excellent glaze hold", "Superb Value Alternative"]
        ],
        "ingredients": [
            "4 skin-on salmon fillets (approx. 6 oz each)",
            "1 large sweet potato, scrubbed and sliced into thin 1/4-inch round coins",
            "8 oz fresh green beans, trimmed",
            "2 tbsp olive oil (divided)",
            "2 tbsp pure amber maple syrup",
            "1.5 tbsp whole-grain Dijon mustard (or smooth Dijon)",
            "1 tbsp low-sodium soy sauce or tamari",
            "2 cloves fresh garlic, finely minced",
            "1/2 tsp kosher salt & 1/4 tsp black pepper",
            "Fresh dill sprigs & lemon wedges for serving"
        ],
        "instructions": [
            ("Preheat & Par-Cook Potatoes", "Preheat oven to 425°F (220°C). Line a large rimmed sheet pan with parchment paper. Place sliced sweet potato coins in a microwave-safe bowl with 1 tbsp water; cover and microwave on high for 2 minutes to par-cook."),
            ("Roast Veggies First", "Toss drained sweet potatoes and green beans with 1 tbsp olive oil, 1/4 tsp salt, and pepper. Arrange sweet potatoes in a single layer on one side of the sheet pan and green beans on the other. Roast in oven for 7 minutes."),
            ("Whisk Maple Dijon Glaze", "In a small bowl, whisk maple syrup, Dijon mustard, soy sauce, minced garlic, and remaining olive oil until glossy."),
            ("Add Salmon & Brush Glaze", "Remove sheet pan from oven. Push vegetables slightly aside and place salmon fillets skin-side down in the center. Season salmon lightly with salt, then brush tops generously with the maple Dijon glaze."),
            ("Bake to Tender Flakiness", "Return pan to oven and roast at 425°F for 8 to 10 minutes until salmon reaches 130-135°F and flakes easily with a fork, with glaze bubbly and sweet potatoes tender. Garnish with fresh dill and serve with lemon wedges!")
        ],
        "pro_tip_title": "Elena’s 1/4-Inch Mandoline Slicing Secret",
        "pro_tip": "Cut sweet potato rounds uniformly to exactly 1/4-inch thickness using a mandoline or sharp chef's knife. If slices are thicker than 1/4-inch, they won't cook in rhythm with the salmon; if thinner, they turn into potato chips!",
        "faqs": [
            ("How do I know when salmon is perfectly cooked?", "Gently press the center of a fillet with a fork—it should yield easily and separate into clean, moist flakes. An instant-read thermometer inserted into the thickest part should read 130°F (medium)."),
            ("Can I use frozen salmon fillets?", "Yes, but thaw completely overnight in the refrigerator and pat thoroughly dry with paper towels so the glaze adheres without steaming."),
            ("Can I swap green beans for asparagus?", "Yes! Asparagus spears or broccolini florets cook in the exact same 8 to 10 minute window alongside the salmon.")
        ],
        "about_entities": [
            ("Salmon as food", "https://en.wikipedia.org/wiki/Salmon_as_food"),
            ("Sweet potato", "https://en.wikipedia.org/wiki/Sweet_potato"),
            ("Dijon mustard", "https://en.wikipedia.org/wiki/Dijon_mustard")
        ]
    },

    # 13. Creamy Tuscan Sausage and Kale Pasta
    {
        "slug": "20-minute-creamy-tuscan-sausage-kale-pasta",
        "title": "20-Minute Creamy Tuscan Sausage and Kale Pasta",
        "headline": "20-Minute Creamy Tuscan Sausage and Kale Pasta",
        "badge": "One-Pot Dinners &bull; 20 Mins",
        "category": "One-Pot Dinners",
        "categories_str": "all one-pot-dinners comfort-food 30-minute-meals",
        "read_time": "20 min cook",
        "date": "2026-10-09",
        "image": "./assets/images/creamy-tuscan-sausage-kale-pasta.jpg",
        "image_file": "creamy-tuscan-sausage-kale-pasta.jpg",
        "excerpt": "Al dente penne pasta tossed with browned Italian sausage crumbles, earthy baby kale, sweet sun-dried tomatoes, and a velvety garlic Parmesan cream sauce in 20 minutes.",
        "description": "Irresistible 20-minute Tuscan pasta loaded with spicy browned Italian sausage, sweet sun-dried tomatoes, tender baby kale, and penne ribbons in a silky garlic Parmesan cream reduction.",
        "keywords": "creamy tuscan sausage pasta, 20 minute tuscan pasta, sausage and kale pasta, sun dried tomato pasta, easy weeknight italian pasta",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "recipeYield": "4 servings",
        "recipeCategory": "Main Course",
        "recipeCuisine": "Tuscan-American Italian",
        "calories": "560 kcal",
        "protein": "26g",
        "fat": "31g",
        "carbs": "46g",
        "fiber": "4g",
        "sodium": "780mg",
        "ratingValue": "4.9",
        "reviewCount": "205",
        "quick_answer": "To make 20-minute creamy Tuscan sausage and kale pasta, boil 10 oz penne or rigatoni pasta in salted water for 10 minutes until al dente, reserving 1/2 cup pasta water. In a large skillet over medium-high heat, brown 1 lb sweet or spicy Italian sausage crumbles for 5 minutes until crispy; remove sausage to a plate. In the rendered pan drippings, sauté 3 minced garlic cloves and 1/3 cup oil-packed chopped sun-dried tomatoes for 1 minute. Pour in 3/4 cup chicken broth and 3/4 cup heavy cream; simmer 3 minutes until bubbling. Stir in 3 cups baby kale until wilted (2 minutes), then toss with cooked penne, browned sausage, and 1/2 cup grated Parmesan until silky and glossy.",
        "takeaways": [
            ("Sausage Dripping Sauté", "Sautéing sun-dried tomatoes and garlic in the savory rendered sausage drippings infuses the cream sauce with intense smoky-sweet flavor."),
            ("Baby Kale Tenderness", "Baby kale wilts into tender, velvety greens in just 90 seconds without the tough fibrous stems of mature curly kale."),
            ("Sun-Dried Tomato Oil Umami", "Using sun-dried tomatoes packed in olive oil and Italian herbs adds instant concentrated Mediterranean sweetness.")
        ],
        "matrix_title": "Pasta Shapes for Tuscan Cream Sauces",
        "matrix_headers": ["Pasta Cut", "Ridge Profile", "Sausage Crumb Hold", "Sauce Cling", "Best Fit"],
        "matrix_rows": [
            ["Penne Rigate (Ridged)", "Deep exterior grooves", "Crumbles nestle inside tubes", "10/10 cling", "Top Pick for Tuscan Sausage Sauces (Recommended)"],
            ["Rigatoni", "Wide ridged cylinders", "Sausage pieces fit inside", "10/10 cling", "Heavy Hearty Comfort"],
            ["Campanelle (Ruffled Cones)", "Fluted cone shape", "Catches chopped kale & tomatoes", "9/10 cling", "Visually Stunning Presentation"],
            ["Fettuccine", "Smooth flat ribbon", "Silky cream coating", "Moderate crumb hold", "Classic Tuscan Bistro Style"]
        ],
        "ingredients": [
            "10 oz penne rigate or rigatoni pasta",
            "1 lb mild sweet or hot Italian pork sausage (casings removed)",
            "1/3 cup oil-packed sun-dried tomatoes, drained and sliced into strips",
            "3 cups fresh baby kale or baby spinach leaves, packed",
            "4 cloves fresh garlic, finely minced",
            "3/4 cup low-sodium chicken broth",
            "3/4 cup heavy whipping cream",
            "1/2 cup freshly grated Parmigiano-Reggiano or Pecorino Romano cheese",
            "1/2 tsp crushed red pepper flakes",
            "1/2 tsp kosher salt & 1/4 tsp freshly cracked black pepper"
        ],
        "instructions": [
            ("Boil Pasta", "Bring a large pot of salted water to a rolling boil. Add penne and cook 10 minutes until al dente. Reserve 1/2 cup starchy pasta cooking water, then drain pasta."),
            ("Brown Italian Sausage", "Heat a wide deep skillet over medium-high heat. Add sausage, breaking it into bite-sized crumbles with a wooden spoon. Cook 5 to 6 minutes until browned and crispy. Transfer cooked sausage with a slotted spoon to a plate, leaving 1 tbsp drippings in the skillet."),
            ("Sauté Aromatics", "Reduce heat to medium. Add minced garlic and sun-dried tomatoes to the skillet drippings. Sauté for 1 minute until fragrant. Pour in chicken broth, scraping up browned bits from the pan bottom."),
            ("Build Tuscan Cream Sauce", "Whisk in heavy cream, red pepper flakes, salt, and pepper. Bring to a gentle simmer for 3 minutes until slightly thickened. Add baby kale and toss for 90 seconds until leaves are wilted and tender."),
            ("Toss, Emulsify & Serve", "Add cooked penne, browned sausage, and grated Parmesan cheese to the skillet. Toss vigorously over low heat for 1 minute until sauce becomes glossy and coats every noodle, splashing in reserved pasta water as needed. Serve hot with extra grated cheese and cracked pepper!")
        ],
        "pro_tip_title": "Elena’s Baby Kale vs. Curly Kale Secret",
        "pro_tip": "Always grab pre-washed baby kale from the greens section instead of mature curly kale bunches. Baby kale leaves are tender, mild, and melt directly into hot cream sauce in under 90 seconds with zero stem-stripping required!",
        "faqs": [
            ("Can I substitute spinach for kale?", "Absolutely! Fresh baby spinach wilts even faster (around 45 seconds) and provides a delicate, tender texture."),
            ("Can I make this with Italian turkey sausage?", "Yes! Italian turkey sausage works wonderfully. Add 1 tbsp olive oil to the skillet when browning since turkey sausage is leaner."),
            ("How do I store and reheat leftovers?", "Store in an airtight container for up to 4 days. Reheat on the stove over medium-low heat with a splash of milk or chicken broth to bring the cream sauce back to silky life.")
        ],
        "about_entities": [
            ("Italian sausage", "https://en.wikipedia.org/wiki/Italian_sausage"),
            ("Kale", "https://en.wikipedia.org/wiki/Kale"),
            ("Sun-dried tomato", "https://en.wikipedia.org/wiki/Sun-dried_tomato")
        ]
    }
]

def generate_article_html(r):
    # Ingredients HTML
    ing_html = ""
    for idx, ing in enumerate(r["ingredients"], 1):
        ing_id = f"ing_{r['slug'][:4]}_{idx}"
        ing_html += f'<li><input type="checkbox" id="{ing_id}"><label for="{ing_id}">{ing}</label></li>\n'

    # Instructions HTML
    inst_html = ""
    for title, text in r["instructions"]:
        inst_html += f"<li><strong>{title}:</strong> {text}</li>\n"

    # Takeaways HTML
    takeaways_html = ""
    for title, desc in r["takeaways"]:
        takeaways_html += f"<li><strong>{title}:</strong> {desc}</li>\n"

    # Matrix Table HTML
    matrix_headers_html = "".join([f"<th>{h}</th>" for h in r["matrix_headers"]])
    matrix_rows_html = ""
    for row in r["matrix_rows"]:
        tds = "".join([f"<td>{cell if idx != 0 and idx != len(row)-1 else f'<strong>{cell}</strong>'}</td>" for idx, cell in enumerate(row)])
        matrix_rows_html += f"<tr>{tds}</tr>\n"

    # FAQs HTML
    faqs_html = ""
    faq_schema_entities = []
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
        faq_schema_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    # Instructions Schema
    instructions_schema = []
    for title, text in r["instructions"]:
        instructions_schema.append({
            "@type": "HowToStep",
            "name": title,
            "text": text
        })

    # About schema
    about_schema = []
    for name, wiki_url in r["about_entities"]:
        about_schema.append({
            "@type": "Thing",
            "name": name,
            "sameAs": wiki_url
        })

    # JSON-LD Graph
    schema_graph = {
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
                    "proteinContent": r["protein"],
                    "carbohydrateContent": r["carbs"],
                    "fiberContent": r["fiber"],
                    "sodiumContent": r["sodium"]
                },
                "recipeIngredient": r["ingredients"],
                "recipeInstructions": instructions_schema,
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": r["ratingValue"],
                    "reviewCount": r["reviewCount"]
                },
                "about": about_schema
            },
            {
                "@type": "FAQPage",
                "@id": f"https://fastflavored.com/articles/{r['slug']}.html#faq",
                "mainEntity": faq_schema_entities
            }
        ]
    }

    schema_json_str = json.dumps(schema_graph, indent=2)

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
{schema_json_str}
  </script>

  <!-- Stylesheets -->
  <link rel="stylesheet" href="../css/style.css?v=2.1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="https://quge5.com/88/tag.min.js" data-zone="291667" async data-cfasync="false"></script>
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
        {r['excerpt']}
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
                {matrix_headers_html}
              </tr>
            </thead>
            <tbody>
              {matrix_rows_html}
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
    print(f"=== Publishing {len(NEW_RECIPES)} New Recipes from PDF Topics ===")
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
        if os.path.exists(recipe_data_path):
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
