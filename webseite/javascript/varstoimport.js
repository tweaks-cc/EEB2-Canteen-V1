// Gönnt sich das aktuelle Datum des Computers
const datum = new Date();
var monat = datum.getMonth() + 1
var tagdatum = datum.getDate()
var zahlendatum = tagdatum + "." + monat
var wochentag = datum.getDay()
// Zu Testzwecken, weil gerade das heutige Datum nicht in der JSON ist
// var zahlendatum = "28.11"

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
    // Nimmt ein Datum als Zahlen, entweder als Array oder String
    // [Tag, Monat]
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