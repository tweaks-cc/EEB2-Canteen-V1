// Importiert die Variablen aus der js-Datei
var eatdict = importedessensdict                     // Dictionary mit dem ganzen Essen
var aktuellesdatum = [zuwortdatum(zahlendatum), zahlendatum]    // Heutiges Datum


function main(datumliste) {
    // Liste des Essens von Datum
    var eatlist = []
    // Geht einmal durch alle Teile der Liste des Datums aus dem Dict
    var essensliste = eatdict[datumliste[0]] // datumsliste[0] da [datumalsworte, datumalszahlen]
    for (index in essensliste) {
        // Wenn null, also wenn weniger Teile als max; einfach Leerzeichen statt null/dem Element selber
        if (essensliste[index] == null) {
            eatlist.push(" ")
        }
        // ansonsten den Teil selber hinzufügen
        else {
            eatlist.push(essensliste[index])
        }
    }

    // Formatiert das Datum damit es in die "Überschrift kann"
    var formatiertesdatum = wtag_fr_to_de[eatlist[0]] + ", der " + datumliste[1]

    // Packt das Essen in die Liste #essensliste im Body
    document.getElementById("Datum").innerHTML   = formatiertesdatum
    document.getElementById("Suppe").innerHTML   = eatlist[1]
    document.getElementById("Haupt1").innerHTML  = eatlist[2]
    document.getElementById("Haupt2").innerHTML  = eatlist[3]
    document.getElementById("Haupt3").innerHTML  = eatlist[4]
    document.getElementById("Dessert").innerHTML = eatlist[5]
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
        var datumwort = zuwortdatum(datumintsplit)
        // Guckt ob neues Datum valide
        return checkdate(datumwort, backforth, datumintsplit, recursiondepth, originalesdatum)
    }

    if (backforth == "back" )   {
        // Datum geht eins zurück
        // Formatiert das angegebene Datum zuerst von zahl.zahl zu einem Array [Tag, Monat]
        var datumintsplit = aktuellesdatum[1].split(".")
        datumintsplit[0] = String(parseInt(datumintsplit[0]) - 1)
        // Nach dem verändern des Tages, Datumsarray wieder zum String zahlalswort.zahlalswort
        var datumwort = zuwortdatum(datumintsplit)
        // Guckt ob neues Datum valide
        return checkdate(datumwort, backforth, datumintsplit, recursiondepth, originalesdatum)
    }
}


function checkdate(date, backforth, numberdate, recursiondepth, originalesdatum) {
    // Checkt ob Datum valide/im Essensdict
    // Bekommt das Datum als Array [Tag, Monat]
    // Wenn Datum nicht valide dann sucht es nach dem nächsten validen Datum solange nicht zu lange (rekursiv) gesucht wurde
    recursiondepth += 1
    if (recursiondepth == 4) {
        return originalesdatum
    }
    // Das Suchen passiert durch das rekursive rufen der Funktion checkdate()
    else if (eatdict[date] == undefined) {
        // Checkt ob neues Datum älter oder neuer sein soll
        if (backforth == "forth") {
            numberdate[0] = String(parseInt(numberdate[0]) + 1)
            var worddate = zuwortdatum(numberdate)
        }

        if (backforth == "back") {
            numberdate[0] = String(parseInt(numberdate[0]) - 1)
            var worddate = zuwortdatum(numberdate)
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


function datumsänderung(backforth) {
    // Wird gerufen, beim drücken einer der beiden Buttons im body
    // Holt sich das neue Datum, entweder davor oder danach
    var neuesdatum = getadate(aktuellesdatum, backforth)
    aktuellesdatum = neuesdatum
    main(aktuellesdatum)
    }