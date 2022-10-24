#!/bin/bash

# Wie die XLSXs heißen sollen, nachdem sie heruntergeladen wurde.

danachWoche1=../auswerten-python/menues/inputWoche1.xlsx
danachWoche2=../auswerten-python/menues/inputWoche2.xlsx
danachWoche3=../auswerten-python/menues/inputWoche3.xlsx
danachWoche4=../auswerten-python/menues/inputWoche4.xlsx


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

# Wie die XLSXs heißen, bevor sie heruntergeladen werden.

davorWoche1=Semaine-$(date '+%W')-$(date --date="this Monday" +"%d")-$monat-$(date '+%Y')-$(date --date="this Friday" +"%d")-$monat-$(date '+%Y').xlsx
davorWoche2=Semaine-$(date --date="next Week" '+%W')-$(date --date="next Monday" +"%d")-$monat-$(date '+%Y')-$(date --date="next Friday" +"%d")-$monat-$(date '+%Y').xlsx
davorWoche3=Semaine-$(date --date="2 Weeks" '+%W')-$(date --date="2 Monday" +"%d")-$monat-$(date '+%Y')-$(date --date="2 Friday" +"%d")-$monat-$(date '+%Y').xlsx
davorWoche4=Semaine-$(date --date="3 Weeks" '+%W')-$(date --date="3 Monday" +"%d")-$monat-$(date '+%Y')-$(date --date="3 Friday" +"%d")-$monat-$(date '+%Y').xlsx

# Falls es schon mehrere inputWocheX.xlsx im Ordner gibt, mussen sie gelöscht werden, sonst wird das Skript nicht funktionieren.

rm $danachWoche1
rm $danachWoche2
rm $danachWoche3
rm $danachWoche4


# Die XLSXs werden gefetcht.

if [ -f "$danachWoche1" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE WOCHE 1${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$davorWoche1
    mv -v $davorWoche1 $danachWoche1 && echo -e "${BGreen}WOCHE 1 ERFOLGREICH${NC}"
    echo
fi

if [ -f "$danachWoche2" ];
then
    :
else
    echo -e "${BRed}VERSUCHE WOCHE 2${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$davorWoche2
    mv -v $davorWoche2 $danachWoche2 && echo -e "${BGreen}WOCHE 2 ERFOLGREICH${NC}"
    echo
fi

if [ -f "$danachWoche3" ];
then
    :
else
    echo -e "${BRed}VERSUCHE WOCHE 3${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$davorWoche3
    mv -v $davorWoche3 $danachWoche3 && echo -e "${BGreen}WOCHE 3 ERFOLGREICH${NC}"
    echo
fi

if [ -f "$danachWoche4" ];
then
    :
else
    echo -e "${BRed}VERSUCHE WOCHE 4${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$davorWoche4
    mv -v $davorWoche4 $danachWoche4 && echo -e "${BGreen}WOCHE 4 ERFOLGREICH${NC}"
    echo
fi
