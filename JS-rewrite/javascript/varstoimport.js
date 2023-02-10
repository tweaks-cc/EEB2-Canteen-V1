// Gönnt sich das aktuelle Datum des Computers
const datum = new Date();
var monat = datum.getMonth() + 1
if (String(monat).length == 1) {monat = "0" + String(monat)}
var tagdatum = datum.getDate()
if (String(tagdatum).length == 1) { tagdatum = "0" + String(tagdatum) }
var aktuellesdatum = [tagdatum, monat]
console.log("created:", aktuellesdatum)
var wochentag = datum.getDay()
// Zu Testzwecken, weil gerade das heutige Datum nicht in der JSON ist
//var aktuellesdatum = ["01", "01"]

const übersetzung_de = {
    "le":             "der ",
    "wiki":           "de",
    "Mittwoch":       "Mittwoch",
    "customnotfound": "Dieses Datum ist nicht im Menü.",
    "dateempty":      "Gib bitte zuerst ein valides Datum ein.",
    "wikisearcherror":"Ein Fehler ist beim Suchen aufgetreten.<br>Dieser Begriff konnte nicht gefunden werden.<br>Bitte versuchen sie einen anderen."
}
const übersetzung_en = {
    "le":             "the ",
    "wiki":           "en",
    "Mittwoch":       "Wednesday",
    "customnotfound": "This date is not in the menu.",
    "dateempty":      "Please enter a valid date first.",
    "wikisearcherror":"An error occured while searching.<br>This term could not be found.<br>Please search another item."
}
const übersetzung_fr = {
    "le":             "le ",
    "wiki":           "fr",
    "Mittwoch":       "Mercredi",
    "customnotfound": "Cette date n'est pas dans le menu.",
    "dateempty":      "Veuillez d'abord entrer une date valide.",
    "wikisearcherror":"Un erreur est survenue.<br>Malheureusement, ce terme de recherche est introuvable.<br>Veuillez chercher quelques chose d'autre."
}

function tostringdate(datumint) {
    console.log(datumint)
    // Nimmt ein Datum als Zahlenarray
    // [Tag, Monat]
    // Macht aus dem Array einen String
    datumstr = datumint[0] + "." + datumint[1]
    console.log("dstr",datumstr)
    return datumstr // Returnt das Datum als String: zahl.zahl
}

function tostringdate1char(datumint) {
    console.log("1char", datumint)
    // Nimmt ein Datum als Zahlenarray
    // [Tag, Monat]
    // Macht aus dem Array einen String
    datumstr = datumint[0] + "." + datumint[1]
    if ((datumint[1])[0] == "0") {
        datumint[1] = (datumint[1])[1]
    }
    console.log("dstr", datumstr)
    return datumstr // Returnt das Datum als String: zahl.zahl
}