#!/bin/bash

# Wie die XLSX heißen soll, nachdem sie heruntergeladen wurde.

danach=../auswerten-python/menues/input.xlsx

# Definitionen der Farben.

BGreen='\033[1;32m' # Bold Green
BRed='\033[1;31m' # Bold Red
NC='\033[0m' # No Color

# Verändert die Variable "monat" zu den ersten 4 Buchstaben des aktuellen Monats auf Französisch und kleingeschrieben, wegen der komischen Formatierung der Excel-Dateien der Kantine.

if [ $(date '+%m') == '12' ]
then
    monat="déce"
fi

if [ $(date '+%m') == '11' ]
then
    monat="nove"
fi

if [ $(date '+%m') == '10' ]
then
    monat="octo"
fi

if [ $(date '+%m') == '09' ]
then
    monat="sept"
fi

if [ $(date '+%m') == '08' ]
then
    monat="août"
fi

if [ $(date '+%m') == '07' ]
then
    monat="juil"
fi

if [ $(date '+%m') == '06' ]
then
    monat="juin"
fi

if [ $(date '+%m') == '05' ]
then
    monat="mai"
fi

if [ $(date '+%m') == '04' ]
then
    monat="avri"
fi

if [ $(date '+%m') == '03' ]
then
    monat="mars"
fi

if [ $(date '+%m') == '02' ]
then
    monat="févr"
fi

if [ $(date '+%m') == '01' ]
then
    monat="janv"
fi

# Wie die XLSX heißt, bevor sie heruntergeladen wird.

davor=https://www.woluweparents.org/wp-content/uploads/2022/09/Semaine-$(date '+%W')-$(date --date="this Monday" +"%d")-$monat-$(date '+%Y')-$(date --date="this Friday" +"%d")-$monat-$(date '+%Y').xlsx

# Falls es schon eine input.xlsx im Ordner gibt, muss sie gelöscht werden, sonst wird das Skript nicht funktionieren.

rm $danach

# Die XLSX wird gefetcht.

if [ -f "$danach" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/09/$davor
    mv -v $davor $danach && echo -e "${BGreen}ERFOLGREICH${NC}"
    echo
fi
