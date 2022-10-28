// Macht den ganzen Datumsmist
const date = new Date();
var monat = date.getMonth() + 1
var tagdatum = date.getDate()
var zahlendatum = tagdatum + "." + monat

const zahlen = {
    "1": "eins",
    "2": "zwei",
    "3": "drei",
    "4": "vier",
    "5": "fuenf",
    "6": "sechs",
    "7": "sieben",
    "8": "acht",
    "9": "neun",
    "10": "zehn",
    "11": "elf",
    "12": "zwoelf",
    "13": "dreizehn",
    "14": "vierzehn",
    "15": "fuenfzehn",
    "16": "sechzehn",
    "17": "siebzehn",
    "18": "achtzehn",
    "19": "neunzehn",
    "20": "zwanzig",
    "21": "einundzwanzig",
    "22": "zweiundzwanzig",
    "23": "dreiundzwanzig",
    "24": "vierundzwanzig",
    "25": "fuenfundzwanzig",
    "26": "sechsundzwanzig",
    "27": "siebenundzwanzig",
    "28": "achtundzwanzig",
    "29": "neunundzwanzig",
    "30": "dreissig",
    "31": "einunddreissig"
}
const zahlenworte = {
    "eins":             1,
    "zwei":             2,
    "drei":             3,
    "vier":             4,
    "fuenf":            5,
    "sechs":            6,
    "sieben":           7,
    "acht":             8,
    "neun":             9,
    "zehn":             10,
    "elf":              11,
    "zwoelf":           12,
    "dreizehn":         13,
    "vierzehn":         14,
    "fuenfzehn":        15,
    "sechzehn":         16,
    "siebzehn":         17,
    "achtzehn":         18,
    "neunzehn":         19,
    "zwanzig":          20,
    "einundzwanzig":    21,
    "zweiundzwanzig":   22,
    "dreiundzwanzig":   23,
    "vierundzwanzig":   24,
    "fuenfundzwanzig":  25,
    "sechsundzwanzig":  26,
    "siebenundzwanzig": 27,
    "achtundzwanzig":   28,
    "neunundzwanzig":   29,
    "dreissig":         30,
    "einunddreissig":   31 
}
const wtag_fr_to_de = {
    "Lundi": "Montag",
    "Mardi":"Dienstag",
    "Mercredi": "Mittwoch",
    "Jeudi": "Donnerstag",
    "Vendredi": "Freitag"
}

function monthinttostr(monthstr) {
    return zahlen[monthstr]
}
function monthstrtoint(monthint) {
    return zahlenworte[str(monthint)]
}

function zuwortdatum(datumint) {
    console.log(typeof datumint)
    if (typeof datumint == Array) { datumintsplit = datumint }
    else { var datumintsplit = datumint.split(".") }
    datumstr = monthinttostr(datumintsplit[0]) + "." + monthinttostr(datumintsplit[1])
    return datumstr
}
/*
const suppenli = document.getElementById("Suppe")
const haupt1li = document.getElementById("Haupt1")
const haupt2li = document.getElementById("Haupt2")
const haupt3li = document.getElementById("Haupt3")
const nachtischli = document.getElementById("Dessert")
*/

// Ist halt der Dict mit all dem Essen
var importedessensdict = {
    "drei.zehn": [
        "Lundi",
        "Minestrone",
        "Poëlee de poulet aux légumes",
        "Cœur de blé",
        null,
        "Fruit"
    ],
    "vier.zehn": [
        "Mardi",
        "Potage cerfeuil",
        "Veau marengo",
        "légumes oubliés",
        "Pommes vapeur",
        "Laitage"
    ],
    "sechs.zehn": [
        "Jeudi",
        "Potage champignons",
        "Nuggets végétarien",
        "Légumes grillés / riz",
        null,
        "Biscuit"
    ],
    "sieben.zehn": [
        "Vendredi",
        "Potage choux verts",
        "Mezze",
        "Baguette",
        null,
        "Fruit"
    ],
    "zehn.zehn": [
        "Lundi",
        "Potage potiron",
        null,
        "Pâtes veggie",
        null,
        "Fruit"
    ],
    "elf.zehn": [
        "Mardi",
        "Crème de volaille",
        "Carbonnade de bœuf",
        "Carottes",
        "Purées",
        "Fruit"
    ],
    "dreizehn.zehn": [
        "Jeudi",
        "Potage courgettes",
        "Sauté de veau",
        "Haricots verts tomatés",
        "Pépinettes",
        "Biscuit"
    ],
    "vierzehn.zehn": [
        "Vendredi",
        "Potage carottes",
        "Saucisse porc fromage",
        "Brocolis",
        "Quartier pdt",
        "Fruit"
    ],
    "siebzehn.zehn": [
        "Lundi",
        "Potage tomate mascarpone",
        "Burger de légumes",
        "Salade",
        null,
        "Fruit"
    ],
    "achtzehn.zehn": [
        "Mardi",
        "Potage épinards",
        null,
        "Gratin de pâtes",
        null,
        "Fruit"
    ],
    "zwanzig.zehn": [
        "Jeudi",
        "Potage à l'oignon",
        "Blanquette dinde",
        "Légumes assortis",
        "Riz",
        "Fruit"
    ],
    "einundzwanzig.zehn": [
        "Vendredi",
        "Potage de saison",
        "Lard",
        "Potiron",
        "Pomme vapeur",
        "Laitage"
    ],
    "vierundzwanzig.zehn": [
        "Lundi",
        "Potage andalou",
        null,
        "Penne fromage épinard",
        null,
        "Fruit"
    ],
    "fuenfundzwanzig.zehn": [
        "Mardi",
        "Potage thaï coco",
        "Boulette liégeoise",
        "purée carottes",
        null,
        "Laitage"
    ],
    "siebenundzwanzig.zehn": [
        "Jeudi",
        "Potage choux-fleurs",
        null,
        "Paëlla poulet",
        null,
        "Biscuit"
    ],
    "achtundzwanzig.zehn": [
        "Vendredi",
        "Potage céleri-rave",
        "Filet de poisson",
        "Ratatouille",
        "Pommes vapeur",
        "Fruit"
    ]
}