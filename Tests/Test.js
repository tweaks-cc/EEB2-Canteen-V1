function checkdate(date, backforth, numberdate, recursiondepth, originalesdatum) {
    // Checkt ob Datum valide/im Essensdict
    // Bekommt das Datum als Array [Tag, Monat]
    // Wenn Datum nicht valide dann sucht es nach dem nächsten validen Datum solange nicht zu lange (rekursiv) gesucht wurde
    recursiondepth += 1
    // Sobald zu tief gesucht wurde wird gecheckt ob es auch einfach zum nächsten Monat geht
    if (recursiondepth == 30) {
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