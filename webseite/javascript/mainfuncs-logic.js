// Importiert die Variablen aus der js-Datei
var aktuellesdatum = [tostringdate(zahlendatum), zahlendatum]    // Heutiges Datum
var essensdict = importedessensdict_en      // Dictionary mit dem ganzen Essen | Standard: Englisch
var sprache = übersetzung_en               // Standard-sprache: Englisch
var startup = true

function main(datumliste) {
    if (wochentag == 3 && startup)  {
        startup = false
        var formatiertesdatum = sprache["Mittwoch"] + ", " + sprache["le"] + zahlendatum
    
        document.getElementById("Datum").style.fontWeight = "bold"
        document.getElementById("Datum").innerHTML   = formatiertesdatum
        document.getElementById("Suppe").innerHTML   = null
        document.getElementById("Haupt1").innerHTML  = null
        document.getElementById("Haupt2").innerHTML  = sprache["Mittwoch"]
        document.getElementById("Haupt3").innerHTML  = null
        document.getElementById("Dessert").innerHTML = null
        
    }
    else {
        document.getElementById("Datum").style.fontWeight = "normal"
        // Liste des Essens von Datum
        var eatlist = []
        // Geht einmal durch alle Teile der Liste des Datums aus dem Dict
        var essensliste = essensdict[datumliste[0]] // datumsliste[0] da [datumalsworte, datumalszahlen]
        for (index in essensliste) {
            eatlist.push(essensliste[index])
        }

        // Formatiert das Datum damit es in die "Überschrift" kann
        var formatiertesdatum = eatlist[0] + ", " + sprache["le"] + datumliste[1]

        // Packt das Essen in die Liste #essensliste im Body
        document.getElementById("Datum").innerHTML   = formatiertesdatum
        document.getElementById("Suppe").innerHTML   = eatlist[1]
        document.getElementById("Haupt1").innerHTML  = eatlist[2]
        document.getElementById("Haupt2").innerHTML  = eatlist[3]
        document.getElementById("Haupt3").innerHTML  = eatlist[4]
        document.getElementById("Dessert").innerHTML = eatlist[5]
    }

}


function getadate(aktuellesdatum, backforth) {
    var recursiondepth = 0
    var originalesdatum = aktuellesdatum
    // Jeweils checken ob dass neue datum valide ist 
    if (backforth == "custom" ) {
        console.log("custom")
        /* Datum geht dann halt zum angegebenen Datum */
    }

    if (backforth == "forth") {
        // Datum geht eins vor
        // Formatiert das angegebene Datum zuerst von zahl.zahl zu einem Array [Tag, Monat]
        var datumintsplit = aktuellesdatum[1].split(".")
        datumintsplit[0] = String(parseInt(datumintsplit[0]) + 1)
        // Nach dem verändern des Tages, Datumsarray wieder zum String zahlalswort.zahlalswort
        var datumwort = tostringdate(datumintsplit)
        // Guckt ob neues Datum valide
        return checkdate(datumwort, backforth, datumintsplit, recursiondepth, originalesdatum)
    }

    if (backforth == "back" )   {
        // Datum geht eins zurück
        // Formatiert das angegebene Datum zuerst von zahl.zahl zu einem Array [Tag, Monat]
        var datumintsplit = aktuellesdatum[1].split(".")
        datumintsplit[0] = String(parseInt(datumintsplit[0]) - 1)
        // Nach dem verändern des Tages, Datumsarray wieder zum String zahlalswort.zahlalswort
        var datumwort = tostringdate(datumintsplit)
        // Guckt ob neues Datum valide
        return checkdate(datumwort, backforth, datumintsplit, recursiondepth, originalesdatum)
    }
}


function checkdate(date, backforth, numberdate, recursiondepth, originalesdatum) {
    // Checkt ob Datum valide/im Essensdict
    // Bekommt das Datum als Array [Tag, Monat]
    // Wenn Datum nicht valide dann sucht es nach dem nächsten validen Datum solange nicht zu lange (rekursiv) gesucht wurde
    recursiondepth += 1
    // Sobald zu tief gesucht wurde wird gecheckt ob es auch einfach zum nächsten Monat geht
    if (recursiondepth == 30){
        // Wenn man nach vorne gehen wollte geht er einen Monat höher (+)
        if (backforth == "forth") {
            // Prepariert erstmal das neue Datum
            date = date.split(".")
            // Addiert eins auf den alten Monat um ihn zu erhöhen
            var neuermonatmonat = parseInt(monthstrtoint(date[1])) + 1
            // Erstellt das neue Datum als Int-Array
            var neuermonatintdatum = [1, neuermonatmonat]
            // Erstellt das neue Datum als String
            var neuermonatdatum = tostringdate(neuermonatintdatum)
            return checknewmonthdate(neuermonatdatum, backforth, neuermonatintdatum, 0, originalesdatum)
        }
        // Wenn man nach hinten gehen wollte geht er einen Monat tiefer (-)
        else if (backforth == "back") {
            // Prepariert erstmal das neue Datum
            date = date.split(".")
            // Subtrahiert eins vom alten Monat um ihn zu senken
            var neuermonatmonat = parseInt(monthstrtoint(date[1])) - 1
            // Erstellt das neue Datum als Int-Array
            // Als Tag 32 für ein wenig Puffer
            var neuermonatintdatum = [32, neuermonatmonat]
            // Erstellt das neue Datum als String
            var neuermonatdatum = tostringdate(neuermonatintdatum)
            return checknewmonthdate(neuermonatdatum, backforth, neuermonatintdatum, 0, originalesdatum)
        }
    }
    // Das Suchen passiert durch das rekursive rufen der Funktion checkdate()
    else if (essensdict[date] == undefined) {
        // Checkt ob neues Datum älter oder neuer sein soll
        if (backforth == "forth") {
            numberdate[0] = String(parseInt(numberdate[0]) + 1)
            var worddate = tostringdate(numberdate)
        }
        else if (backforth == "back") {
            numberdate[0] = String(parseInt(numberdate[0]) - 1)
            var worddate = tostringdate(numberdate)
        }

        // Geht jetzt solange rekursiv weiter bis Datum valide
        return checkdate(worddate, backforth, numberdate, recursiondepth, originalesdatum)
    }

    else {
        // Wenn neues Datum valdie, gibt er das Datum aus und bricht aus dem rekursiven Loop
        numberdate = numberdate[0] + "." + numberdate[1]
        return [date, numberdate]
    }
}

function checknewmonthdate(date, backforth, numberdate, recursiondepth, originalesdatum) {
    // Checkt ob Datum valide/im Essensdict
    // Bekommt das Datum als Array [Tag, Monat]
    // Wenn Datum nicht valide dann sucht es nach dem nächsten validen Datum solange nicht zu lange (rekursiv) gesucht wurde
    recursiondepth += 1
    if (recursiondepth == 30) {
        return originalesdatum
    }
    // Das Suchen passiert durch das rekursive rufen der Funktion checknewmonthdate()
    else if (essensdict[date] == undefined) {
        // Checkt ob neues Datum älter oder neuer sein soll
        if (backforth == "forth") {
            numberdate[0] = String(parseInt(numberdate[0]) + 1)
            var worddate = tostringdate(numberdate)
        }
        else if (backforth == "back") {
            numberdate[0] = String(parseInt(numberdate[0]) - 1)
            var worddate = tostringdate(numberdate)
        }

        // Geht jetzt solange rekursiv weiter bis Datum valide
        return checknewmonthdate(worddate, backforth, numberdate, recursiondepth, originalesdatum)
    }

    else {
        // Wenn neues Datum valdie, gibt er das Datum aus und bricht aus dem rekursiven Loop
        numberdate = numberdate[0] + "." + numberdate[1]
        return [date, numberdate]
    }
}


function changeddate(backforth) {
    // Wird gerufen, beim drücken einer der beiden Buttons im body
    // Holt sich das neue Datum, entweder davor oder danach
    var neuesdatum = getadate(aktuellesdatum, backforth)
    aktuellesdatum = neuesdatum
    main(aktuellesdatum)
    }
