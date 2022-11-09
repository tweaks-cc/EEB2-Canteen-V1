// Gönnt sich das aktuelle Datum des Computers
const datum = new Date();
var monat = datum.getMonth() + 1
var tagdatum = datum.getDate()
var zahlendatum = tagdatum + "." + monat
// Zu Testzwecken, weil gerade das heutige Datum nicht in der JSON ist
// var zahlendatum = "28.11"

var wochentag = datum.getDay()

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

function monthinttostr(monthstr) {
    return zahlen[monthstr]
}
function monthstrtoint(monthint) {
    return String(zahlenworte[monthint])
}

const übersetzung_de = {"le": "der ", "Mittwoch": "Mittwoch" }
const übersetzung_en = {"le": "the ", "Mittwoch": "Wednesday"}
const übersetzung_fr = {"le": "le " , "Mittwoch": "Mercredi" }

function tostringdate(datumint) {
    // Nimmt ein Datum als Zahlen, entweder als Array oder String
    // Entweder er splittet den String oder gibt das Array direkt weiter
    var datumintsplit = ""
    if (typeof datumint == "string" ) {
        datumintsplit = datumint.split(".")
    }
    if (typeof datumint == "object") {
        datumintsplit = datumint
    }
    // Macht aus den Zahlen, die entsprechenden Zahlen als Wörter
    datumstr = monthinttostr(datumintsplit[0]) + "." + monthinttostr(datumintsplit[1])
    return datumstr // Returnt das Datum als String: zahlwort.zahlwort
}