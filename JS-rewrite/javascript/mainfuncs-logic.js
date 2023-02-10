// Alle wichtigen Variablen aus der vars.js Datei
// aktuellesdatum: aktuelles Datum des Computers im Format Tag.Monat
// essensdict:     // Dictionary mit dem ganzen Essen | Standard: Englisch
let essensdict = importedessensdict_en
// Sprache: Einfach alle Texte die übersetzt werden müssen
let sprache = übersetzung_en
// Wird benutzt für die Anzeige, dass Mittwoch ist
let startup = false

function main(datum) {
    aktuellesdatum = datum
    if (wochentag == 3 && startup) {
        // Formatiert das Datum damit es in die "Überschrift" kann
        let formatiertesdatum = sprache["Mittwoch"] + ", " + sprache["le"] + datum

        document.getElementById("Datum").style.fontWeight = "bold"
        document.getElementById("Datum").innerHTML = formatiertesdatum
        document.getElementById("Suppe").innerHTML = null
        document.getElementById("Haupt1").innerHTML = null
        document.getElementById("Haupt2").innerHTML = sprache["Mittwoch"]
        document.getElementById("Haupt3").innerHTML = null
        document.getElementById("Dessert").innerHTML = null
    }
    else {
        // Liste des Essens von Datum
        let eatlist = essensdict[datum]

        // Formatiert das Datum damit es in die "Überschrift" kann
        let formatiertesdatum = eatlist[0] + ", " + sprache["le"] + datum

        // Packt das Essen in die Liste #essensliste im Body
        document.getElementById("Datum").innerHTML = formatiertesdatum
        document.getElementById("Suppe").innerHTML = eatlist[1]
        document.getElementById("Haupt1").innerHTML = eatlist[2]
        document.getElementById("Haupt2").innerHTML = eatlist[3]
        document.getElementById("Haupt3").innerHTML = eatlist[4]
        document.getElementById("Dessert").innerHTML = eatlist[5]
    }
}

function checkweekend() {
    if (wochentag == 0 || wochentag == 6) {
        changeddate("forth")
    }
}

function getadate(aktuellesdatum, backforth) {
    let recursiondepth = 0
    let originalesdatum = aktuellesdatum
    // Jeweils checken ob das neue Datum valide ist
    if (backforth == "forth") {
        // Datum geht eins vor
        let datum = aktuellesdatum + 1
        return checkdate(backforth, datum, recursiondepth, originalesdatum)
    }
    else if (backforth == "back") {
        // Datum geht eins zurück
        let datum = aktuellesdatum - 1
        return checkdate(backforth, datum, recursiondepth, originalesdatum)
    }
}

function checkdate(backforth, datum, recursiondepth, originalesdatum, newmonth) {
    console.log(newmonth)
    // Bekommt das Datum als float: Tag.Monat
    // Checkt ob Datum valide/im Essensdict
    // Wenn Datum nicht valide dann wird nach dem nächsten validen Datum gesucht (bis valide oder max recursion)
    recursiondepth += 1
    // Sobald max recursion,         testet er nächsten Monat
    // Sobald max Tag in Monat (31), testet er nächsten Monat
    if (recursiondepth == 31 || String(datum).split(".")[0] == 33 || String(datum).split(".")[0] == -1) {
        if (newmonth == true) {
            newmonth = false
            return originalesdatum
        }
        // Wenn nach vorne Monat + 1
        if (backforth == "forth") {
            let split = String(datum).split(".")
            // Neues Datum jetzt Monat + 1 und Tag = 0 => Anfang des Monats
            let neuesdatum = "0" + "." + String(parseInt(parseInt(String(originalesdatum).split(".")[1])) + 1)
            return checkdate(backforth, neuesdatum, 0 /*Recursiondepth*/, originalesdatum, true)
        }
        // Wenn nach hinten Monat - 1
        else if (backforth == "back") {
            let split = String(datum).split(".")
            // Neues Datum jetzt Monat - 1 und Tag = 32 => Ende des Monats
            let neuesdatum = "32" + "." + String(parseInt(parseInt(String(originalesdatum).split(".")[1])) - 1)
            return checkdate(backforth, neuesdatum, 0 /*Recursiondepth*/, originalesdatum, true)
        }
    }
    // Das Suchen passiert durch das rekursive Rufen der Funktion checkdate()
    else if (essensdict[datum] == undefined) {
        // Macht Datum entweder neuer oder älter => backforth
        // Wenn nach vorne Tag + 1
        if (backforth == "forth") {
            let split = String(datum).split(".")
            let neuesdatum = (parseInt(split[0]) + 1) + "." + split[1]
            return checkdate(backforth, neuesdatum, recursiondepth, originalesdatum, newmonth)
        }
        // Wenn nach hinten Tag - 1
        else if (backforth == "back") {
            let split = String(datum).split(".")
            let neuesdatum = (parseInt(split[0]) - 1) + "." + split[1]
            return checkdate(backforth, neuesdatum, recursiondepth, originalesdatum, newmonth)
        }
    }
    else /*Datum sollte valide sein, wenn nicht Bug => Issue pls*/ {
        // Wenn Datum valide, returnt er das Datum und schliesst den recursion-loop
        newmonth = false
        return datum
    }
}

function changeddate(backforth) {
    // Wird gerufen, beim drücken der Backforth buttons
    // Holt sich das neue datum, entweder neuer oder älter
    let tempdate = getadate(aktuellesdatum, backforth)
    aktuellesdatum = tempdate
    main(aktuellesdatum)
}

function searchcustomdate(whatfor) {
    // Wenn reload oder load dann Datumsinput leeren
    if (whatfor == "reset") { document.getElementById("customdate").value = ""; return }
    // Wenn Sprache gewechselt und keine Fehlermeldung einfach nüscht machen, weil nur load
    if (whatfor == "langchange" && document.getElementById("fehlermeldung").innerHTML == "") { return }
    // Falls aber Fehlermeldung da steht, und Sprache gewechselt, dann übersetzen
    if (whatfor == "langchange" && document.getElementById("fehlermeldung").innerHTML != "") {
        // Nimmt sich die Fehlermeldung und splittet sie
        let fehlermeldung = document.getElementById("fehlermeldung").innerHTML
        // Nimmt sich das erste Wort der Fehlermeldung und holt sich damit die Übersetzte version
        // Nimmt sich den Fehlermeldungscode mithilfe des ersten Wortes und des customfehler-Dicts
        // Mit dem Fehlercode holt er sich dann die neue Übersetzung mit der aktuellen Sprache
        document.getElementById("fehlermeldung").innerHTML = sprache[customfehler[fehlermeldung.split(" ")[0]]]
    }

    // Wenn ein custom Datum gesucht wird, welches als bsp. 2022-11-14 ankommt, wird es gesplittet und das Jahr entfernt
    // => Jahr = erstes Element | mit .shift() entfernt
    customdate = document.getElementById("customdate").value.split("-")
    // Fehlermeldung anzeigen, wenn kein Datum eingegeben ist
    if (customdate == "") { document.getElementById("fehlermeldung").innerHTML = sprache["dateempty"]; return }
    customdate.shift()
    // Dann vertauscht er Tag und Monat wegen der Schreibweise: 11,14 => 14, 11 (richtige Schreibweise)
    let temp = customdate[1]
    customdate[1] = customdate[0]
    customdate[0] = temp
    // Macht Datum aus Array zu Float Tag.Monat mit .join(".") und guckt of im essensdict
    customdate = customdate.join(".")
    if (essensdict[customdate]) {
        // Fehlermeldung entfernen, egal ob vorhanden oder nicht
        document.getElementById("fehlermeldung").style.display = "none"
        // Stellt die Seite auf das Datum hier um
        main(customdate)
    }
    // Falls nicht im Essensdict => Fehlermeldung: "customnotfound"
    else {
        document.getElementById("fehlermeldung").style.display = "block"
        document.getElementById("fehlermeldung").innerHTML = sprache["customnotfound"]
    }

}