// Ist halt der Dict mit all dem Essen
const importedessensdict_fr = { "drei.zehn": ["Lundi", "Minestrone", "Po\u00eblee de poulet aux l\u00e9gumes", "C\u0153ur de bl\u00e9", null, "Fruit"], "vier.zehn": ["Mardi", "Potage cerfeuil", "Veau marengo", "l\u00e9gumes oubli\u00e9s", "Pommes vapeur", "Laitage"], "sechs.zehn": ["Jeudi", "Potage champignons", "Nuggets v\u00e9g\u00e9tarien", "L\u00e9gumes grill\u00e9s / riz", null, "Biscuit"], "sieben.zehn": ["Vendredi", "Potage choux verts", "Mezze", "Baguette", null, "Fruit"], "sieben.elf": ["Lundi", null, null, "Feiertag", null, null], "acht.elf": ["Mardi", "Soupe aux lentilles tomat\u00e9e", "Cabeza", "Bouqueti\u00e8re / pdt", "Jus de viande", "Fruit"], "zehn.elf": ["Jeudi", "Potage aux carottes", "Escalope de veau pan\u00e9e", "Basquaise", "C\u0153ur de bl\u00e9", "Laitage"], "elf.elf": ["Vendredi", "Salade de ma\u00efs compos\u00e9e", "Burger de quinoa", "Salade de crudit\u00e9", null, "Fruit"], "zehn.zehn": ["Lundi", "Potage potiron", null, "P\u00e2tes veggie", null, "Fruit"], "elf.zehn": ["Mardi", "Cr\u00e8me de volaille", "Carbonnade de b\u0153uf", "Carottes", "Pur\u00e9es", "Fruit"], "dreizehn.zehn": ["Jeudi", "Potage courgettes", "Saut\u00e9 de veau", "Haricots verts tomat\u00e9s", "P\u00e9pinettes", "Biscuit"], "vierzehn.zehn": ["Vendredi", "Potage carottes", "Saucisse porc fromage", "Brocolis", "Quartier pdt", "Fruit"], "vierzehn.elf": ["Lundi", "Potage poireaux curry", "Kokkinisto", "P\u00e9pinettes", null, "Fruit"], "fuenfzehn.elf": ["Mardi", "Bouillon l\u00e9gume asiatiques", "Semoule", "L\u00e9gumes orientaux", null, "Biscuit"], "siebzehn.elf": ["Jeudi", "Taboul\u00e9", "Filet de poisson", "Courgette / Riz", "Sauce poisson estragon", "Fruit"], "achtzehn.elf": ["Vendredi", "Minestrone", "Chipolata / compote", "Jus de viande", "Pur\u00e9e maison", "Laitage"], "siebzehn.zehn": ["Lundi", "Potage tomate mascarpone", "Burger de l\u00e9gumes", "Salade", null, "Fruit"], "achtzehn.zehn": ["Mardi", "Potage \u00e9pinards", null, "Gratin de p\u00e2tes", null, "Fruit"], "zwanzig.zehn": ["Jeudi", "Potage \u00e0 l'oignon", "Blanquette dinde", "L\u00e9gumes assortis", "Riz", "Fruit"], "einundzwanzig.zehn": ["Vendredi", "Potage de saison", "Lard", "Potiron", "Pomme vapeur", "Laitage"], "einundzwanzig.elf": ["Lundi", "Potage choux-fleur", "Croquettes fromages", "Salade / pomme vapeurs", null, "Fruit"], "zweiundzwanzig.elf": ["Mardi", "Salade de choux blanc", "Lard fermier", "Lentilles ", "Baguette / Jus de viande", "Glace"], "vierundzwanzig.elf": ["Jeudi", "Potage cresson", "B\u0153uf / petits pois", "Gratin dauphinois", "Jus viande", "Fruit"], "fuenfundzwanzig.elf": ["Vendredi", "Cr\u00e8me de ma\u00efs", "Filet de poulet", "L\u00e9gumes wok sauce curry", "Riz", "Laitage"], "vierundzwanzig.zehn": ["Lundi", "Potage andalou", null, "Penne fromage \u00e9pinard", null, "Fruit"], "fuenfundzwanzig.zehn": ["Mardi", "Potage tha\u00ef coco", "Boulette li\u00e9geoise", "pur\u00e9e carottes", null, "Laitage"], "siebenundzwanzig.zehn": ["Jeudi", "Potage choux-fleurs", null, "Pa\u00eblla poulet", null, "Biscuit"], "achtundzwanzig.zehn": ["Vendredi", "Potage c\u00e9leri-rave", "Filet de poisson", "Ratatouille", "Pommes vapeur", "Fruit"], "achtundzwanzig.elf": ["Lundi", "Potage Saint-germain", "Pates", "Bolognaise / coulis tomate", "Fromage r\u00e2p\u00e9", "Fruit"], "neunundzwanzig.elf": ["Mardi", "Salade de pois chiche", null, "Riz fa\u00e7on  pa\u00eblla", null, "Laitage"], "eins.zwoelf": ["Jeudi", "Tacos shell", "Sauce tex mex", "Poulet / garnitures", "Fromage r\u00e2p\u00e9", "Biscuit"], "zwei.zwoelf": ["Vendredi", "Potage \u00e0 l'oignon", "Blanquette de veau", "L\u00e9gumes assortis", "Pur\u00e9e maison", "Fruit"], "03.10": ["Lundi", "Minestrone", "Po\u00eblee de poulet aux l\u00e9gumes", "C\u0153ur de bl\u00e9", null, "Fruit"], "04.10": ["Mardi", "Potage cerfeuil", "Veau marengo", "l\u00e9gumes oubli\u00e9s", "Pommes vapeur", "Laitage"], "06.10": ["Jeudi", "Potage champignons", "Nuggets v\u00e9g\u00e9tarien", "L\u00e9gumes grill\u00e9s / riz", null, "Biscuit"], "07.10": ["Vendredi", "Potage choux verts", "Mezze", "Baguette", null, "Fruit"], "05.12": ["Lundi", null, "Pizza margherita", "Jour f\u00e9ri\u00e9", null, null], "06.12": ["Mardi", "Bouillon de l\u00e9gumes", "Ravioli ricotta \u00e9pipnards", "Coulis de tomate", null, "Saint Nicolas"], "08.12": ["Jeudi", "Potage parmentier", "Cassolette de poissons", "Riz", null, "Cake aux pommes"], "09.12": ["Vendredi", null, null, "Jour f\u00e9ri\u00e9", null, "Laitage"], "07.11": ["Lundi", null, null, "Jour f\u00e9ri\u00e9", null, null], "08.11": ["Mardi", "Soupe aux lentilles tomat\u00e9e", "Cabeza", "Bouqueti\u00e8re / pdt", "Jus de viande", "Fruit"], "10.11": ["Jeudi", "Potage aux carottes", "Escalope de veau pan\u00e9e", "Basquaise", "C\u0153ur de bl\u00e9", "Laitage"], "11.11": ["Vendredi", "Salade de ma\u00efs compos\u00e9e", "Burger de quinoa", "Salade de crudit\u00e9", null, "Fruit"], "10.10": ["Lundi", "Potage potiron", null, "P\u00e2tes veggie", null, "Fruit"], "11.10": ["Mardi", "Cr\u00e8me de volaille", "Carbonnade de b\u0153uf", "Carottes", "Pur\u00e9es", "Fruit"], "13.10": ["Jeudi", "Potage courgettes", "Saut\u00e9 de veau", "Haricots verts tomat\u00e9s", "P\u00e9pinettes", "Biscuit"], "14.10": ["Vendredi", "Potage carottes", "Saucisse porc fromage", "Brocolis", "Quartier pdt", "Fruit"], "12.12": ["Lundi", null, "Menu examen", "Jour f\u00e9ri\u00e9", null, "Fruit"], "13.12": ["Mardi", null, "Menu examen", "Jour f\u00e9ri\u00e9", null, "Laitage"], "15.12": ["Jeudi", null, "Menu examen", "Jour f\u00e9ri\u00e9", null, "Fruit"], "16.12": ["Vendredi", null, "Menu examen", "Jour f\u00e9ri\u00e9", null, "Laitage"], "14.11": ["Lundi", "Potage poireaux curry", "Kokkinisto", "P\u00e9pinettes", null, "Fruit"], "15.11": ["Mardi", "Bouillon l\u00e9gume asiatiques", "Semoule", "L\u00e9gumes orientaux", null, "Biscuit"], "17.11": ["Jeudi", "Taboul\u00e9", "Filet de poisson", "Courgette / Riz", "Sauce poisson estragon", "Fruit"], "18.11": ["Vendredi", "Minestrone", "Chipolata / compote", "Jus de viande", "Pur\u00e9e maison", "Laitage"], "17.10": ["Lundi", "Potage tomate mascarpone", "Burger de l\u00e9gumes", "Salade", null, "Fruit"], "18.10": ["Mardi", "Potage \u00e9pinards", null, "Gratin de p\u00e2tes", null, "Fruit"], "20.10": ["Jeudi", "Potage \u00e0 l'oignon", "Blanquette dinde", "L\u00e9gumes assortis", "Riz", "Fruit"], "21.10": ["Vendredi", "Potage de saison", "Lard", "Potiron", "Pomme vapeur", "Laitage"], "21.11": ["Lundi", "Potage choux-fleur", "Croquettes fromages", "Salade / pomme vapeurs", null, "Fruit"], "22.11": ["Mardi", "Salade de choux blanc", "Lard fermier", "Lentilles ", "Baguette / Jus de viande", "Glace"], "24.11": ["Jeudi", "Potage cresson", "B\u0153uf / petits pois", "Gratin dauphinois", "Jus viande", "Fruit"], "25.11": ["Vendredi", "Cr\u00e8me de ma\u00efs", "Filet de poulet", "L\u00e9gumes wok sauce curry", "Riz", "Laitage"], "24.10": ["Lundi", "Potage andalou", null, "Penne fromage \u00e9pinard", null, "Fruit"], "25.10": ["Mardi", "Potage tha\u00ef coco", "Boulette li\u00e9geoise", "pur\u00e9e carottes", null, "Laitage"], "27.10": ["Jeudi", "Potage choux-fleurs", null, "Pa\u00eblla poulet", null, "Biscuit"], "28.10": ["Vendredi", "Potage c\u00e9leri-rave", "Filet de poisson", "Ratatouille", "Pommes vapeur", "Fruit"], "28.11": ["Lundi", "Potage Saint-germain", "Pates", "Bolognaise / coulis tomate", "Fromage r\u00e2p\u00e9", "Fruit"], "29.11": ["Mardi", "Salade de pois chiche", null, "Riz fa\u00e7on  pa\u00eblla", null, "Laitage"], "01.12": ["Jeudi", "Tacos shell", "Sauce tex mex", "Poulet / garnitures", "Fromage r\u00e2p\u00e9", "Biscuit"], "02.12": ["Vendredi", "Potage \u00e0 l'oignon", "Blanquette de veau", "L\u00e9gumes assortis", "Pur\u00e9e maison", "Fruit"], "09.01": ["Lundi", "Bouillon de l\u00e9gumes", "Ravioli ricotta \u00e9pinard", "Coulis de tomate", null, "Galette des rois"], "10.01": ["Mardi", "potage aux chicons", "chipolata", "pur\u00e9e au choux", "Jus de viande", "Fruit"], "12.01": ["Jeudi", "Nuggets de poulet", "Sauce tex mex", "epis de ma\u00efs / salade", null, "Laitage"], "13.01": ["Vendredi", "Salade de carottes", "Saut\u00e9 de veau", "Aubergines tomat\u00e9es", "P\u00e9pinettes", "Fruit"], "16.01": ["Lundi", "Potage pois chiche", "Quiche aux l\u00e9gumes", "Salade", null, "Fruit"], "17.01": ["Mardi", "Velout\u00e9 aux champignons", "Filet de poisson", "Haricots / pdt vapeurs", "Sauce de poisson", "Fruit"], "19.01": ["Jeudi", "Minestrone", "Lard fermier", "Pot\u00e9e aux poireaux", "Jus de viande", "Laitage "], "20.01": ["Vendredi", "Hamburger", "Pain Bun", "Salade / garniture", "Fromage", "Fruit"], "23.01": ["Lundi", "Potage cerfeuil", "P\u00e2tes", "Bolognaise / coulis tomate", null, "Fruit"], "24.01": ["Mardi", "Potage aux carottes", "Presia / petits pois", "Pur\u00e9e maison", "Jus de viande \u00e0 l'estragon", "Fruit"], "26.01": ["Jeudi", "Potage choux-fleur", "Couscous", "L\u00e9gumes", null, "Fruit"], "27.01": ["Vendredi", "Salade de celeri-rave", "Navarin d'agneau", "L\u00e9gumes assortis", "Riz", "Laitage"] }
