# Food-101 Dictionary: Class -> Label & Celiac Risk Assessment
food101_celiac_db = {
    "apple_pie": {
        "label": "Apple pie",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Crust typically contains wheat flour.",
        "server_questions": [
            "Do you offer a gluten-free apple pie option prepared separately?",
            "Is the gluten-free crust prepared using dedicated pans and utensils?"
        ]
    },
    "baby_back_ribs": {
        "label": "Baby back ribs",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Meat is gluten-free, but BBQ sauces and marinades often contain wheat or soy sauce.",
        "server_questions": [
            "Is the BBQ sauce or rub gluten-free (free of wheat or standard soy sauce)?",
            "Are the ribs finished on a grill shared with gluten-containing items?"
        ]
    },
    "baklava": {
        "label": "Baklava",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with phyllo dough containing wheat.",
        "server_questions": [
            "Do you offer a certified gluten-free baklava made with non-wheat pastry?"
        ]
    },
    "beef_carpaccio": {
        "label": "Beef carpaccio",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Raw beef, oil, and parmesan are gluten-free. Check for bread side dishes.",
        "server_questions": [
            "Can this dish be served without bread or croutons on the plate?",
            "Are any of the dressings or drizzles made with wheat or soy sauce?"
        ]
    },
    "beef_tartare": {
        "label": "Beef tartare",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Beef and raw egg are gluten-free. Caution with Worcestershire sauce or toast sides.",
        "server_questions": [
            "Does the seasoning contain Worcestershire sauce or soy sauce with wheat?",
            "Can you ensure toast or crackers are kept off the plate entirely?"
        ]
    },
    "beet_salad": {
        "label": "Beet salad",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Beets, greens, and cheese are naturally gluten-free. Check dressings.",
        "server_questions": [
            "Is the salad dressing free of malt vinegar, wheat thickeners, or soy sauce?",
            "Are there any candied nuts or toppings prepared with flour?"
        ]
    },
    "beignets": {
        "label": "Beignets",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Deep-fried dough made from wheat flour.",
        "server_questions": [
            "Do you have gluten-free beignets fried in a dedicated fryer?"
        ]
    },
    "bibimbap": {
        "label": "Bibimbap",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Gochujang paste almost always contains wheat. High risk from soy sauce marinades.",
        "server_questions": [
            "Is the Gochujang (chili paste) certified gluten-free?",
            "Are the meat or vegetables marinated in standard soy sauce containing wheat?"
        ]
    },
    "bread_pudding": {
        "label": "Bread pudding",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Main ingredient is wheat bread.",
        "server_questions": [
            "Do you make a gluten-free bread pudding option using gluten-free bread?"
        ]
    },
    "breakfast_burrito": {
        "label": "Breakfast burrito",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Wrapped in a wheat flour tortilla.",
        "server_questions": [
            "Can this be made into a bowl or served in a certified gluten-free tortilla?",
            "Is the filling prepared on a flat top grill shared with wheat tortillas or bread?"
        ]
    },
    "bruschetta": {
        "label": "Bruschetta",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served on toasted wheat bread.",
        "server_questions": [
            "Can the tomato topping be served on certified gluten-free bread?",
            "Is gluten-free bread toasted in a dedicated toaster or clean surface?"
        ]
    },
    "caesar_salad": {
        "label": "Caesar salad",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Contains wheat croutons; Caesar dressing often contains Worcestershire sauce.",
        "server_questions": [
            "Can I get this salad without croutons?",
            "Is the Caesar dressing made without Worcestershire sauce or wheat-based thickeners?"
        ]
    },
    "cannoli": {
        "label": "Cannoli",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Fried pastry shell made from wheat flour.",
        "server_questions": [
            "Do you offer gluten-free cannoli shells?"
        ]
    },
    "caprese_salad": {
        "label": "Caprese salad",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Tomatoes, mozzarella, basil, and olive oil are naturally gluten-free.",
        "server_questions": [
            "Is the balsamic glaze or dressing free of wheat-derived thickeners?",
            "Can you ensure the salad is prepared on a surface free of breadcrumbs?"
        ]
    },
    "carrot_cake": {
        "label": "Carrot cake",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Baked with wheat flour.",
        "server_questions": [
            "Is there a gluten-free carrot cake option baked in a separate environment?"
        ]
    },
    "ceviche": {
        "label": "Ceviche",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Raw fish cured in citrus juice. Check for added soy sauce.",
        "server_questions": [
            "Does the marinade or juice contain soy sauce or soy-derived seasonings?",
            "Are the tortilla chips served with it fried in a dedicated gluten-free fryer?"
        ]
    },
    "cheesecake": {
        "label": "Cheesecake",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Crust is usually made from graham crackers or wheat cookies.",
        "server_questions": [
            "Do you offer crustless or gluten-free crust cheesecake?"
        ]
    },
    "cheese_plate": {
        "label": "Cheese plate",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Cheese is gluten-free, but high cross-contamination risk from crackers/bread on the plate.",
        "server_questions": [
            "Can the crackers and bread be served on a separate plate entirely?",
            "Are all cheese varieties cut with clean knives away from bread crumbs?"
        ]
    },
    "chicken_curry": {
        "label": "Chicken curry",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Usually gluten-free, but some roux-based curries or thickeners use wheat flour.",
        "server_questions": [
            "Is the curry sauce thickened with wheat flour or roux?",
            "Are any ingredients (like soy sauce or chicken stock) made with wheat?"
        ]
    },
    "chicken_quesadilla": {
        "label": "Chicken quesadilla",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with wheat flour tortillas.",
        "server_questions": [
            "Can this be made using 100% corn tortillas?",
            "Is the quesadilla cooked on a dedicated clean surface away from flour tortillas?"
        ]
    },
    "chicken_wings": {
        "label": "Chicken wings",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Often breaded or fried in shared fryers with gluten items.",
        "server_questions": [
            "Are the wings coated or dusted in wheat flour?",
            "Are the wings fried in a dedicated fryer used only for gluten-free items?",
            "Is the wing sauce (e.g., teriyaki, BBQ) free of soy sauce or flour?"
        ]
    },
    "chocolate_cake": {
        "label": "Chocolate cake",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Baked with wheat flour.",
        "server_questions": [
            "Do you offer a flourless or gluten-free chocolate cake?"
        ]
    },
    "chocolate_mousse": {
        "label": "Chocolate mousse",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Chocolate, eggs, and cream are gluten-free. Verify thickeners.",
        "server_questions": [
            "Are there any flour-based thickeners, sponge cakes, or cookies added?",
            "Is the mousse prepared on equipment free from cross-contamination?"
        ]
    },
    "churros": {
        "label": "Churros",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Fried dough made from wheat flour.",
        "server_questions": [
            "Do you offer gluten-free churros cooked in a separate fryer?"
        ]
    },
    "clam_chowder": {
        "label": "Clam chowder",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Thickened with wheat flour roux.",
        "server_questions": [
            "Is the soup thickened with flour or cornstarch/potatoes?",
            "Are oyster crackers served on the side instead of on top?"
        ]
    },
    "club_sandwich": {
        "label": "Club sandwich",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with sliced wheat bread.",
        "server_questions": [
            "Can this be prepared on certified gluten-free bread?",
            "Is the bread toasted in a dedicated gluten-free toaster?"
        ]
    },
    "crab_cakes": {
        "label": "Crab cakes",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Breadcrumbs are used as a binder.",
        "server_questions": [
            "Are the crab cakes made with breadcrumbs or gluten-free fillers?",
            "Is real crab used, or imitation crab (surimi), which contains wheat?"
        ]
    },
    "creme_brulee": {
        "label": "Creme brulee",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Custard made of egg yolks, cream, sugar, and vanilla is naturally gluten-free.",
        "server_questions": [
            "Is the custard free of any flour or wheat thickeners?",
            "Is it served without cookies, wafers, or gluten garnishes?"
        ]
    },
    "croque_madame": {
        "label": "Croque madame",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with wheat bread and béchamel sauce (wheat flour).",
        "server_questions": [
            "Can this be made with gluten-free bread and a flour-free béchamel sauce?"
        ]
    },
    "cup_cakes": {
        "label": "Cup cakes",
        "celiac_risk": "High", "contains_gluten": True,
        "notes": "Baked with wheat flour.",
        "server_questions": [
            "Do you offer certified gluten-free cupcakes made in a separate facility?"
        ]
    },
    "deviled_eggs": {
        "label": "Deviled eggs",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Eggs, mayonnaise, and mustard are naturally gluten-free.",
        "server_questions": [
            "Does the filling contain Worcestershire sauce or soy sauce?",
            "Are any crunchy toppings (like fried onions) free of flour?"
        ]
    },
    "donuts": {
        "label": "Donuts",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Fried dough made from wheat flour.",
        "server_questions": [
            "Are there dedicated gluten-free donuts prepared in a gluten-free fryer?"
        ]
    },
    "dumplings": {
        "label": "Dumplings",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Wrapper is made from wheat flour.",
        "server_questions": [
            "Do you offer dumplings made with rice starch or gluten-free wrappers?",
            "Is the dipping sauce gluten-free Tamari or regular soy sauce?"
        ]
    },
    "edamame": {
        "label": "Edamame",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Steamed soybeans are naturally gluten-free. Avoid soy sauce seasoning.",
        "server_questions": [
            "Are the edamame seasoned only with sea salt?",
            "Are they boiled in water shared with wheat noodles?"
        ]
    },
    "eggs_benedict": {
        "label": "Eggs benedict",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served on an English muffin (wheat flour).",
        "server_questions": [
            "Can this be served on gluten-free bread or tomato slices instead of an English muffin?",
            "Is the Hollandaise sauce thickened with flour?"
        ]
    },
    "escargots": {
        "label": "Escargots",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Snails and garlic butter are gluten-free. Avoid side bread.",
        "server_questions": [
            "Is the garlic butter free of flour or roux?",
            "Can the dish be served without toasted bread slices on top or on the plate?"
        ]
    },
    "falafel": {
        "label": "Falafel",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Chickpea-based, but wheat flour is often added as a binder; high shared-fryer risk.",
        "server_questions": [
            "Is flour added to the chickpea falafel mixture as a binder?",
            "Is the falafel cooked in a dedicated fryer separate from pita or breaded items?"
        ]
    },
    "filet_mignon": {
        "label": "Filet mignon",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Plain meat is gluten-free. Verify accompanying sauces.",
        "server_questions": [
            "Is the meat seasoned with any flour or wheat-derived spice mixes?",
            "Is the accompanying sauce (demi-glace, au jus) thickened with flour?"
        ]
    },
    "fish_and_chips": {
        "label": "Fish and chips",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Fish is coated in beer batter made with wheat flour.",
        "server_questions": [
            "Do you offer gluten-free fried fish made with gluten-free batter?",
            "Are the fish and fries cooked in a dedicated gluten-free fryer?"
        ]
    },
    "foie_gras": {
        "label": "Foie gras",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Duck/goose liver is gluten-free. Often served with brioche (avoid).",
        "server_questions": [
            "Can this be served without brioche or bread?",
            "Is the fruit reduction sauce free of flour or malt-derived alcohol?"
        ]
    },
    "french_fries": {
        "label": "French fries",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Potatoes are gluten-free, but cross-contamination in shared fryers is very common.",
        "server_questions": [
            "Are the french fries fried in a dedicated fryer used only for potatoes?",
            "Are the fries coated in wheat flour for extra crispiness?"
        ]
    },
    "french_onion_soup": {
        "label": "French onion soup",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Topped with toasted wheat bread and broth is often thickened with flour.",
        "server_questions": [
            "Is the beef broth thickened with flour or flour-dusted onions?",
            "Can the soup be prepared without bread or with gluten-free bread?"
        ]
    },
    "french_toast": {
        "label": "French toast",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made by soaking wheat bread in egg batter.",
        "server_questions": [
            "Do you offer French toast made with certified gluten-free bread?",
            "Is it cooked on a clean griddle free of pancake batter and wheat bread?"
        ]
    },
    "fried_calamari": {
        "label": "Fried calamari",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Breaded with wheat flour before frying.",
        "server_questions": [
            "Is the calamari breaded with cornstarch/rice flour instead of wheat flour?",
            "Is it cooked in a dedicated gluten-free fryer?"
        ]
    },
    "fried_rice": {
        "label": "Fried rice",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Seasoned with standard soy sauce (contains wheat).",
        "server_questions": [
            "Can the fried rice be prepared using gluten-free Tamari instead of soy sauce?",
            "Is the wok thoroughly cleaned before preparing this dish?"
        ]
    },
    "frozen_yogurt": {
        "label": "Frozen yogurt",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Base is generally gluten-free. Watch out for cookie/granola toppings.",
        "server_questions": [
            "Are any gluten-containing ingredients present in the yogurt base?",
            "Are toppings kept in separate bins to avoid cookie crumb cross-contamination?"
        ]
    },
    "garlic_bread": {
        "label": "Garlic bread",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made from wheat bread.",
        "server_questions": [
            "Can you make garlic bread using certified gluten-free bread in a separate oven space?"
        ]
    },
    "gnocchi": {
        "label": "Gnocchi",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Potato dough is traditionally bound with wheat flour.",
        "server_questions": [
            "Are the gnocchi made with 100% potato starch/gluten-free flour?",
            "Are they boiled in a dedicated pot with fresh, uncontaminated water?"
        ]
    },
    "greek_salad": {
        "label": "Greek salad",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Cucumbers, tomatoes, olives, and feta cheese are naturally gluten-free.",
        "server_questions": [
            "Is the salad free of croutons or wheat pita toppings?",
            "Is the dressing free of malt vinegar or flour thickeners?"
        ]
    },
    "grilled_cheese_sandwich": {
        "label": "Grilled cheese sandwich",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with wheat bread.",
        "server_questions": [
            "Can this be made with gluten-free bread?",
            "Is it cooked on a clean pan/surface separate from wheat bread?"
        ]
    },
    "grilled_salmon": {
        "label": "Grilled salmon",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Plain fish is gluten-free. Check marinades for soy sauce.",
        "server_questions": [
            "Is the marinade or glaze free of soy sauce or wheat flour?",
            "Is the grill surface cleaned to prevent cross-contamination from breaded items?"
        ]
    },
    "guacamole": {
        "label": "Guacamole",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Avocados, lime, and seasonings are gluten-free. Pair with corn tortilla chips.",
        "server_questions": [
            "Are the accompanying tortilla chips 100% corn and fried in a dedicated fryer?"
        ]
    },
    "gyoza": {
        "label": "Gyoza",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Wrapper is made from wheat flour.",
        "server_questions": [
            "Do you offer gluten-free gyoza made with rice flour wrappers?"
        ]
    },
    "hamburger": {
        "label": "Hamburger",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served in a wheat flour bun.",
        "server_questions": [
            "Do you offer a gluten-free bun or lettuce wrap option?",
            "Are the hamburger patties seasoned with fillers or breadcrumbs?",
            "Is the patty cooked on a grill area separate from toasted wheat buns?"
        ]
    },
    "hot_and_sour_soup": {
        "label": "Hot and sour soup",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Contains soy sauce and is thickened with starch/flour.",
        "server_questions": [
            "Is the broth made with gluten-free Tamari instead of standard soy sauce?",
            "Is cornstarch or wheat flour used as the soup thickener?"
        ]
    },
    "hot_dog": {
        "label": "Hot dog",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served in a wheat flour bun.",
        "server_questions": [
            "Can this be served in a gluten-free bun or bunless?",
            "Are the hot dogs certified gluten-free (free of wheat fillers)?"
        ]
    },
    "huevos_rancheros": {
        "label": "Huevos rancheros",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Gluten-free if made with corn tortillas, high risk if flour tortillas are used.",
        "server_questions": [
            "Are the tortillas 100% corn (not flour or corn-wheat blend)?",
            "Are the tortillas fried in a dedicated fryer?"
        ]
    },
    "hummus": {
        "label": "Hummus",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Chickpeas and tahini are gluten-free. Avoid pita bread sides.",
        "server_questions": [
            "Can this be served with sliced vegetables instead of pita bread?",
            "Are any oil drizzles or seasonings mixed with soy sauce or wheat?"
        ]
    },
    "ice_cream": {
        "label": "Ice cream",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Plain ice cream is gluten-free. Avoid cookie dough, brownie mix-ins, or cones.",
        "server_questions": [
            "Is this flavor free of cookie crumbs, brownie bits, or malt?",
            "Can you use a clean scoop and scoop from a fresh tub to avoid cross-contamination?"
        ]
    },
    "lasagna": {
        "label": "Lasagna",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Pasta sheets contain wheat flour; béchamel sauce uses wheat flour.",
        "server_questions": [
            "Do you offer gluten-free lasagna made with gluten-free pasta and a wheat-free béchamel?"
        ]
    },
    "lobster_bisque": {
        "label": "Lobster bisque",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Thickened with wheat flour roux.",
        "server_questions": [
            "Is this bisque thickened with a flour roux or cream/rice flour?"
        ]
    },
    "lobster_roll_sandwich": {
        "label": "Lobster roll sandwich",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served in a toasted wheat bun.",
        "server_questions": [
            "Can the lobster salad be served in a gluten-free bun or on a bed of greens?",
            "Is the lobster filling mixed with any wheat-based thickeners or croutons?"
        ]
    },
    "macaroni_and_cheese": {
        "label": "Macaroni and cheese",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Wheat pasta with a cheese sauce thickened with flour.",
        "server_questions": [
            "Do you offer gluten-free mac and cheese prepared with gluten-free pasta?",
            "Is the cheese sauce made without a wheat flour roux?"
        ]
    },
    "macarons": {
        "label": "Macarons",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Traditionally made with almond flour, egg whites, and sugar.",
        "server_questions": [
            "Are these macarons 100% almond flour based (free of wheat flour additions)?",
            "Are they prepared in a bakery facility that handles gluten?"
        ]
    },
    "miso_soup": {
        "label": "Miso soup",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Miso paste can be fermented with barley or wheat (read labels carefully).",
        "server_questions": [
            "Is the miso paste made from rice/soybeans, or does it contain barley/wheat?",
            "Does the dashi broth contain soy sauce with wheat?"
        ]
    },
    "mussels": {
        "label": "Mussels",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Mussels and white wine broth are gluten-free. Do not eat with accompanying bread.",
        "server_questions": [
            "Is the broth free of flour or beer?",
            "Can the mussels be served without bread placed on top?"
        ]
    },
    "nachos": {
        "label": "Nachos",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Corn tortilla chips are gluten-free, but check cheese sauces and fryer contamination.",
        "server_questions": [
            "Are the tortilla chips fried in a dedicated fryer free of gluten items?",
            "Is the cheese sauce thickened with wheat flour?"
        ]
    },
    "omelette": {
        "label": "Omelette",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Eggs, cheese, and vegetables are naturally gluten-free.",
        "server_questions": [
            "Is pancake batter added to the egg mixture to make it fluffier?",
            "Is the omelette cooked on a clean surface free of toast crumbs?"
        ]
    },
    "onion_rings": {
        "label": "Onion rings",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Coated in wheat flour batter/breadcrumbs and deep-fried.",
        "server_questions": [
            "Do you offer gluten-free onion rings fried in a dedicated fryer?"
        ]
    },
    "oysters": {
        "label": "Oysters",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Raw oysters are gluten-free. Avoid fried or Rockefeller preparations.",
        "server_questions": [
            "Are the oysters served raw on ice?",
            "Are any sauces (e.g., mignonette) made with malt vinegar or soy sauce?"
        ]
    },
    "pad_thai": {
        "label": "Pad thai",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Uses rice noodles, but sauces may contain wheat-derived soy sauce.",
        "server_questions": [
            "Is the Pad Thai sauce free of standard soy sauce or wheat-based fish sauce?",
            "Are the rice noodles boiled in fresh, dedicated water?"
        ]
    },
    "paella": {
        "label": "Paella",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Rice, seafood, meat, and spices are naturally gluten-free.",
        "server_questions": [
            "Is the stock used free of wheat-based seasonings or flour?",
            "Are any chorizo sausages used certified gluten-free?"
        ]
    },
    "pancakes": {
        "label": "Pancakes",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Batter is made from wheat flour.",
        "server_questions": [
            "Do you offer gluten-free pancakes?",
            "Are the gluten-free pancakes cooked on a separate, dedicated griddle?"
        ]
    },
    "panna_cotta": {
        "label": "Panna cotta",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Gelatin-based dessert, naturally gluten-free.",
        "server_questions": [
            "Is this dessert set with gelatin and free of flour thickeners?",
            "Is it served without shortbread or wheat garnishes?"
        ]
    },
    "peking_duck": {
        "label": "Peking duck",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served with hoisin sauce and wheat flour pancakes.",
        "server_questions": [
            "Can the duck be served without the wheat pancakes and hoisin sauce?",
            "Was the duck marinated in standard soy sauce containing wheat?"
        ]
    },
    "pho": {
        "label": "Pho",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Made with rice noodles and broth. Avoid hoisin sauce topping.",
        "server_questions": [
            "Is the broth seasoned without soy sauce or wheat-based additives?",
            "Is hoisin sauce (which often contains wheat) served separately?"
        ]
    },
    "pizza": {
        "label": "Pizza",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Traditional crust is made from wheat flour.",
        "server_questions": [
            "Do you offer a gluten-free pizza crust?",
            "Is the gluten-free pizza prepared and baked in a separate area to prevent airborne flour contamination?"
        ]
    },
    "pork_chop": {
        "label": "Pork chop",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Plain meat is gluten-free. Check gravies or breadings.",
        "server_questions": [
            "Is the pork chop unbreaded?",
            "Is the gravy or pan sauce made without flour?"
        ]
    },
    "poutine": {
        "label": "Poutine",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Gravy is almost always thickened with wheat flour; shared fryer risk for fries.",
        "server_questions": [
            "Is the gravy made with a gluten-free stock and cornstarch binder?",
            "Are the french fries fried in a dedicated gluten-free fryer?"
        ]
    },
    "prime_rib": {
        "label": "Prime rib",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Meat is gluten-free. Ensure au jus is not thickened with flour.",
        "server_questions": [
            "Is the au jus sauce free of wheat flour or roux?",
            "Is the meat seasoned with flour-free rubs?"
        ]
    },
    "pulled_pork_sandwich": {
        "label": "Pulled pork sandwich",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Served in a wheat bun; BBQ sauce may contain gluten.",
        "server_questions": [
            "Can this be served in a gluten-free bun or bunless?",
            "Is the BBQ sauce free of wheat flour, beer, or soy sauce?"
        ]
    },
    "ramen": {
        "label": "Ramen",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Ramen noodles are made of wheat flour; broth contains soy sauce.",
        "server_questions": [
            "Do you offer gluten-free noodles (e.g., rice or shirataki noodles)?",
            "Is the broth made with gluten-free Tamari instead of standard soy sauce?"
        ]
    },
    "ravioli": {
        "label": "Ravioli",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Pasta dough is made from wheat flour.",
        "server_questions": [
            "Do you offer gluten-free ravioli boiled in a dedicated pot with fresh water?"
        ]
    },
    "red_velvet_cake": {
        "label": "Red velvet cake",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Baked with wheat flour.",
        "server_questions": [
            "Do you offer a gluten-free red velvet cake option?"
        ]
    },
    "risotto": {
        "label": "Risotto",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Arborio rice base is naturally gluten-free. Verify stock ingredients.",
        "server_questions": [
            "Is the broth/stock used free of wheat flour or gluten additives?",
            "Is the risotto finished without flour-dusted toppings?"
        ]
    },
    "samosa": {
        "label": "Samosa",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Pastry shell is made from wheat flour.",
        "server_questions": [
            "Do you have a gluten-free samosa option made with non-wheat flour?"
        ]
    },
    "sashimi": {
        "label": "Sashimi",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Raw sliced fish is naturally gluten-free. Use gluten-free tamari instead of soy sauce.",
        "server_questions": [
            "Do you offer gluten-free Tamari soy sauce?",
            "Can you ensure knives and cutting boards are clean of sushi roll rollings/tempura?"
        ]
    },
    "scallops": {
        "label": "Scallops",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Scallops are gluten-free. Ensure they aren't dusted with flour before searing.",
        "server_questions": [
            "Are the scallops dusted with flour prior to searing?",
            "Is the pan sauce free of roux or soy sauce?"
        ]
    },
    "seaweed_salad": {
        "label": "Seaweed salad",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Pre-made seaweed salad dressing almost always contains wheat soy sauce.",
        "server_questions": [
            "Is the seaweed salad dressed with standard soy sauce containing wheat?"
        ]
    },
    "shrimp_and_grits": {
        "label": "Shrimp and grits",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Grits (cornmeal) and shrimp are naturally gluten-free.",
        "server_questions": [
            "Is the shrimp gravy thickened with flour or cornstarch?",
            "Are the grits 100% cornmeal and free of added wheat?"
        ]
    },
    "spaghetti_bolognese": {
        "label": "Spaghetti bolognese",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with wheat pasta.",
        "server_questions": [
            "Do you offer gluten-free pasta?",
            "Is the gluten-free pasta cooked in a dedicated pot of clean water?"
        ]
    },
    "spaghetti_carbonara": {
        "label": "Spaghetti carbonara",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made with wheat pasta.",
        "server_questions": [
            "Do you offer gluten-free pasta options?",
            "Is gluten-free pasta boiled in a dedicated pot with fresh, uncontaminated water?",
            "Is the guanciale/pancetta seasoned with any soy sauce or flour-based coatings?",
            "Are the cheese and egg prepared on clean surfaces free of flour dust?"
        ]
    },
    "spring_rolls": {
        "label": "Spring rolls",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Wrappers are made from wheat flour.",
        "server_questions": [
            "Are the wrappers made of rice paper (Summer rolls) or wheat flour?",
            "Is the dipping sauce gluten-free?"
        ]
    },
    "steak": {
        "label": "Steak",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Plain grilled meat is naturally gluten-free.",
        "server_questions": [
            "Is the steak seasoned with any flour or wheat-based rubs?",
            "Are any butter toppers or steak sauces made with flour or soy sauce?"
        ]
    },
    "strawberry_shortcake": {
        "label": "Strawberry shortcake",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Shortcake or biscuit base is baked with wheat flour.",
        "server_questions": [
            "Do you offer a gluten-free shortcake base?"
        ]
    },
    "sushi": {
        "label": "Sushi",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Rice and fish are safe, but imitation crab (surimi), soy sauce, and tempura contain gluten.",
        "server_questions": [
            "Does the roll contain imitation crab (surimi) or tempura crunchies?",
            "Is the sushi rice vinegar seasoned with wheat ingredients?",
            "Do you offer gluten-free Tamari?"
        ]
    },
    "tacos": {
        "label": "Tacos",
        "celiac_risk": "Low",
        "contains_gluten": False,
        "notes": "Traditional corn tacos are gluten-free. Avoid wheat tortillas and spiced meat fillers with flour.",
        "server_questions": [
            "Are the tortillas 100% corn?",
            "Is the meat seasoning free of wheat flour binders?"
        ]
    },
    "takoyaki": {
        "label": "Takoyaki",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Octopus balls made from a wheat flour batter.",
        "server_questions": [
            "Do you offer a gluten-free batter option for the takoyaki?"
        ]
    },
    "tiramisu": {
        "label": "Tiramisu",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Contains ladyfinger biscuits made of wheat flour.",
        "server_questions": [
            "Do you have a gluten-free tiramisu option made with gluten-free biscuits?"
        ]
    },
    "tuna_tartare": {
        "label": "Tuna tartare",
        "celiac_risk": "Medium",
        "contains_gluten": None,
        "notes": "Tuna is gluten-free, but marinades frequently contain soy sauce.",
        "server_questions": [
            "Is the tuna marinated with standard wheat soy sauce or gluten-free Tamari?",
            "Can this be served without chips or crackers containing wheat?"
        ]
    },
    "waffles": {
        "label": "Waffles",
        "celiac_risk": "High",
        "contains_gluten": True,
        "notes": "Made from wheat flour batter.",
        "server_questions": [
            "Do you offer gluten-free waffles prepared in a dedicated waffle iron?"
        ]
    }
}


def get_dish_assessment(predicted_class: str) -> dict:
    """
    Return risk info for a predicted class, with a safe fallback.
    This returns a dict because the API needs JSON format.
    """
    return food101_celiac_db.get(
        predicted_class,
        {
            "label": predicted_class.replace("_", " ").title(),
            "celiac_risk": "Unknown",
            "contains_gluten": None,
            "notes": "No data available for this class.",
            "server_questions": []
        },
    )
