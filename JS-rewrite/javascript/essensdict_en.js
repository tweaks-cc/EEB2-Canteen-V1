// Ist halt der Dict mit all dem Essen
const importedessensdict_en = { "drei.zehn": ["Monday", "Minestrone", "Chicken stove with vegetables", "Heart of wheat", null, "Fruit"], "vier.zehn": ["Tuesday", " chervil soup", "Veal Marengo", "forgotten vegetables", "Boiled potatoes", "Dairy"], "sechs.zehn": ["Thursday", " mushroom soup", "Vegetarian nuggets", "Grilled vegetables, rice", null, "Cookie"], "sieben.zehn": ["Friday", " green cabbage soup", "Mezze", "Baguette", null, "Fruit"], "sieben.elf": ["Monday", null, null, " Feiertag", null, null], "acht.elf": ["Tuesday", " tomat\u00e9e lenses", "Cabeza", "Bouqueti\u00e8re, pdt", "Meat juice", "Fruit"], "zehn.elf": ["Thursday", " carrot soup", " Breaded cutlet Veal", " Basquaise", "Heart of wheat", "Dairy"], "elf.elf": ["Friday", " composed corn salad", " Quinoa burger", " Raw salad", null, "Fruit"], "zehn.zehn": ["Monday", " pumpkin soup", null, "Veggie pasta", null, "Fruit"], "elf.zehn": ["Tuesday", " poultry cream", "Beef carbonnade", "Carrots", "Puree", "Fruit"], "dreizehn.zehn": ["Thursday", " zucchini soup", "Sauteed veal", "Tomatated green beans", "P\u00e9pinettes", "Cookie"], "vierzehn.zehn": ["Friday", " carrot soup", " Cheese pork sausage", " Broccoli", " PDT district", "Fruit"], "vierzehn.elf": ["Monday", " curry leek soup", "Kokkinisto", "P\u00e9pinettes", null, "Fruit"], "fuenfzehn.elf": ["Tuesday", " Asian vegetable broth", "Semolina", "Oriental vegetables", null, "Cookie"], "siebzehn.elf": ["Thursday", " tabboulee", " Fish fillet", " Zucchini, rice", " Sauce Punter Fish", "Fruit"], "achtzehn.elf": ["Friday", "Minestrone", " Chipolata, compote", "Meat juice", "Mashed potatoes", "Dairy"], "siebzehn.zehn": ["Monday", " mascarpone tomato soup", "Vegetable burger", "Salad", null, "Fruit"], "achtzehn.zehn": ["Tuesday", " spinach soup", null, "Pasta gratin", null, "Fruit"], "zwanzig.zehn": ["Thursday", " onion soup", "Blanquette turkey", "Matching vegetables", "Rice", "Fruit"], "einundzwanzig.zehn": ["Friday", " seasonal soup", " Bacon", " Pumpkin", " Steam apple", "Dairy"], "einundzwanzig.elf": ["Monday", " cabbage soup-Fleur", "Cheese kibble", "Salad, vapor apple", null, "Fruit"], "zweiundzwanzig.elf": ["Tuesday", " white cabbage salad", "Lard farmer", "Lentils", "Wand, meat juice", "Ice"], "vierundzwanzig.elf": ["Thursday", " watercress soup", " Beef, peas", " Gratin dauphinois", " Meat juice", "Fruit"], "fuenfundzwanzig.elf": ["Friday", " cornstone", " Chicken fillet", " Wok vegetables curry sauce", "Rice", "Dairy"], "vierundzwanzig.zehn": ["Monday", " Andalusian soup", null, "Penne spinach cheese", null, "Fruit"], "fuenfundzwanzig.zehn": ["Tuesday", " Thai coconut soup", "Li\u00e8ge dumpling", "Carrots puree", null, "Dairy"], "siebenundzwanzig.zehn": ["Thursday", " choux-fleur soup", null, "Paella chicken", null, "Cookie"], "achtundzwanzig.zehn": ["Friday", " soupCelery-rave", " Fish fillet", " Ratatouille", "Boiled potatoes", "Fruit"], "achtundzwanzig.elf": ["Monday", " Saint-Germain soup", "Pasta", "Bolognese, tomato coulis", "Grated cheese", "Fruit"], "neunundzwanzig.elf": ["Tuesday", " chickpea salad", null, "Paella manner", null, "Dairy"], "eins.zwoelf": ["Thursday", " shell tacos", "Tex Mex sauce", "Chicken, garnishes", "Grated cheese", "Cookie"], "zwei.zwoelf": ["Friday", " onion soup", "Veal stew", "Matching vegetables", "Mashed potatoes", "Fruit"], "03.10": ["Monday", "Minestrone", "Chicken stove with vegetables", " Heart of wheat", null, "Fruit"], "04.10": ["Tuesday", " chervil soup", "Veal Marengo", " forgotten vegetables", "Boiled potatoes", "Dairy"], "06.10": ["Thursday", " mushroom soup", " Vegetarian nuggets", " Grilled vegetables, rice", null, "Cookie"], "07.10": ["Friday", " green cabbage soup", "Mezze", "Baguette", null, "Fruit"], "05.12": ["Monday", null, "Margherita Pizza", "Holiday", null, null], "06.12": ["Tuesday", " vegetable broth", "Ravioli Ricotta Epipnards", "Tomato coulis", null, "Saint Nicholas"], "08.12": ["Thursday", " parmentier soup", "Fish barrier", "Rice", null, "Apple cake"], "09.12": ["Friday", null, null, "Holiday", null, "Dairy"], "07.11": ["Monday", null, null, "Holiday", null, null], "08.11": ["Tuesday", " tomat\u00e9e lenses", "Cabeza", " Bouqueti\u00e8re, pdt", "Meat juice", "Fruit"], "10.11": ["Thursday", " carrot soup", " Breaded cutlet Veal", " Basquaise", " Heart of wheat", "Dairy"], "11.11": ["Friday", " composed corn salad", " Quinoa burger", " Raw salad", null, "Fruit"], "10.10": ["Monday", " pumpkin soup", null, " Veggie pasta", null, "Fruit"], "11.10": ["Tuesday", " poultry cream", " Beef carbonnade", "Carrots", " Puree", "Fruit"], "13.10": ["Thursday", " zucchini soup", " Sauteed veal", " Tomatated green beans", " P\u00e9pinettes", "Cookie"], "14.10": ["Friday", " carrot soup", " Cheese pork sausage", " Broccoli", " PDT district", "Fruit"], "12.12": ["Monday", null, "Examination menu", "Holiday", null, "Fruit"], "13.12": ["Tuesday", null, "Examination menu", "Holiday", null, "Dairy"], "15.12": ["Thursday", null, "Examination menu", "Holiday", null, "Fruit"], "16.12": ["Friday", null, "Examination menu", "Holiday", null, "Dairy"], "14.11": ["Monday", " curry leek soup", "Kokkinisto", " P\u00e9pinettes", null, "Fruit"], "15.11": ["Tuesday", " Asian vegetable broth", "Semolina", " Oriental vegetables", null, "Cookie"], "17.11": ["Thursday", " tabboulee", " Fish fillet", " Zucchini, rice", " Sauce Punter Fish", "Fruit"], "18.11": ["Friday", "Minestrone", " Chipolata, compote", "Meat juice", " Mashed potatoes", "Dairy"], "17.10": ["Monday", " mascarpone tomato soup", " Vegetable burger", "Salad", null, "Fruit"], "18.10": ["Tuesday", " spinach soup", null, " Pasta gratin", null, "Fruit"], "20.10": ["Thursday", " onion soup", "Blanquette turkey", " Matching vegetables", "Rice", "Fruit"], "21.10": ["Friday", " seasonal soup", " Bacon", " Pumpkin", " Steam apple", "Dairy"], "21.11": ["Monday", " cabbage soup-Fleur", "Cheese kibble", "Salad, vapor apple", null, "Fruit"], "22.11": ["Tuesday", " white cabbage salad", "Lard farmer", "Lentils", "Wand, meat juice", "Ice"], "24.11": ["Thursday", " watercress soup", " Beef, peas", " Gratin dauphinois", " Meat juice", "Fruit"], "25.11": ["Friday", " cornstone", " Chicken fillet", " Wok vegetables curry sauce", "Rice", "Dairy"], "24.10": ["Monday", " Andalusian soup", null, " Penne spinach cheese", null, "Fruit"], "25.10": ["Tuesday", " Coconut Thai soup", " Li\u00e8ge dumpling", " Carrots puree", null, "Dairy"], "27.10": ["Thursday", " choux-fleur soup", null, " Paella chicken", null, "Cookie"], "28.10": ["Friday", " soupCelery-rave", " Fish fillet", " Ratatouille", "Boiled potatoes", "Fruit"], "28.11": ["Monday", " Saint-Germain soup", "Pasta", "Bolognese, tomato coulis", " Grated cheese", "Fruit"], "29.11": ["Tuesday", " chickpea salad", null, " Paella manner", null, "Dairy"], "01.12": ["Thursday", " shell tacos", "Tex Mex sauce", "Chicken, garnishes", " Grated cheese", "Cookie"], "02.12": ["Friday", " onion soup", "Veal stew", " Matching vegetables", " Mashed potatoes", "Fruit"], "9.01": ["Monday", " vegetable broth", "Ravioli ricotta spinach", "Tomato coulis", null, "King cake"], "10.01": ["Tuesday", " chicken soup", "Chipolata", "Choux puree", "Meat juice", "Fruit"], "12.01": ["Thursday", " chicken nuggets", "Tex Mex sauce", "corn spi, salad", null, "Dairy"], "13.01": ["Friday", " carrot salad", " Sauteed veal", "Tomatated eggplant", " P\u00e9pinettes", "Fruit"], "16.01": ["Monday", " chickpea soup", "Vegetables quiche", "Salad", null, "Fruit"], "17.01": ["Tuesday", " mushroom velvety", " Fish fillet", "Beans, vapors", "Fish sauce", "Fruit"], "19.01": ["Thursday", "Minestrone", "Lard farmer", "Leek pot", "Meat juice", "Dairy"], "20.01": ["Friday", " hamburger", "Bun bread", "Salad, garnish", "Cheese", "Fruit"], "23.01": ["Monday", " chervil soup", "Pasta", "Bolognese, tomato coulis", null, "Fruit"], "24.01": ["Tuesday", " carrot soup", "Pressia, peas", " Mashed potatoes", "Iteragon meat juice", "Fruit"], "26.01": ["Thursday", " cabbage soup-Fleur", "Couscous", "Vegetables", null, "Fruit"], "27.01": ["Friday", " celery-rave salad", "Lamb stew", " Matching vegetables", "Rice", "Dairy"] }
