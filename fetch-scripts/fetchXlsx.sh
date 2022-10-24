#!/bin/bash

# Wie die XLSXs heißen sollen, nachdem sie heruntergeladen wurde.

wocheMinus3Post=../auswerten-python/menues/input-$(date --date="Monday -3 Week" +"%d")-$(date --date="Tuesday -3 Week" +"%d")-$(date --date="Thursday -3 Week" +"%d")-$(date --date="Friday -3 Week" +"%d")-$(date "+%B").xlsx
wocheMinus2Post=../auswerten-python/menues/input-$(date --date="Monday -2 Week" +"%d")-$(date --date="Tuesday -2 Week" +"%d")-$(date --date="Thursday -2 Week" +"%d")-$(date --date="Friday -2 Week" +"%d")-$(date "+%B").xlsx
wocheMinus1Post=../auswerten-python/menues/input-$(date --date="Monday -1 Week" +"%d")-$(date --date="Tuesday -1 Week" +"%d")-$(date --date="Thursday -1 Week" +"%d")-$(date --date="Friday -1 Week" +"%d")-$(date "+%B").xlsx
woche0Post=../auswerten-python/menues/input-$(date --date="Monday +0 Week" +"%d")-$(date --date="Tuesday +0 Week" +"%d")-$(date --date="Thursday +0 Week" +"%d")-$(date --date="Friday +0 Week" +"%d")-$(date "+%B").xlsx
woche1Post=../auswerten-python/menues/input-$(date --date="Monday +1 Week" +"%d")-$(date --date="Tuesday +1 Week" +"%d")-$(date --date="Thursday +1 Week" +"%d")-$(date --date="Friday +1 Week" +"%d")-$(date "+%B").xlsx
woche2Post=../auswerten-python/menues/input-$(date --date="Monday +2 Week" +"%d")-$(date --date="Tuesday +2 Week" +"%d")-$(date --date="Thursday +2 Week" +"%d")-$(date --date="Friday +2 Week" +"%d")-$(date "+%B").xlsx
woche3Post=../auswerten-python/menues/input-$(date --date="Monday +3 Week" +"%d")-$(date --date="Tuesday +3 Week" +"%d")-$(date --date="Thursday +3 Week" +"%d")-$(date --date="Friday +3 Week" +"%d")-$(date "+%B").xlsx

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

wocheMinus3Prae=Semaine-$(date --date="-3 Week" +"%W")-$(date --date="Monday -3 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday -3 Week" +"%d")-$monat-$(date '+%Y').xlsx
wocheMinus2Prae=Semaine-$(date --date="-2 Week" +"%W")-$(date --date="Monday -2 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday -2 Week" +"%d")-$monat-$(date '+%Y').xlsx
wocheMinus1Prae=Semaine-$(date --date="-1 Week" +"%W")-$(date --date="Monday -1 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday -1 Week" +"%d")-$monat-$(date '+%Y').xlsx
woche0Prae=Semaine-$(date --date="+0 Week" +"%W")-$(date --date="Monday +0 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday +0 Week" +"%d")-$monat-$(date '+%Y').xlsx
woche1Prae=Semaine-$(date --date="+1 Week" +"%W")-$(date --date="Monday +1 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday +1 Week" +"%d")-$monat-$(date '+%Y').xlsx
woche2Prae=Semaine-$(date --date="+2 Week" +"%W")-$(date --date="Monday +2 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday +2 Week" +"%d")-$monat-$(date '+%Y').xlsx
woche3Prae=Semaine-$(date --date="+3 Week" +"%W")-$(date --date="Monday +3 Week" +"%d")-$monat-$(date '+%Y')-$(date --date="Friday +3 Week" +"%d")-$monat-$(date '+%Y').xlsx

# Falls es schon mehrere inputWocheX.xlsx im Ordner gibt, mussen sie gelöscht werden, sonst wird das Skript nicht funktionieren.

rm $wocheMinus3Post
rm $wocheMinus2Post
rm $wocheMinus1Post
rm $woche0Post
rm $woche1Post
rm $woche2Post
rm $woche3Post


# Die XLSXs werden gefetcht.

if [ -f "$wocheMinus3Post" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE VORVORLETZTE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$wocheMinus3Prae
    mv -v $wocheMinus3Prae $wocheMinus3Post && echo -e "${BGreen}VORVORLETZTE WOCHE ERFOLGREICH${NC}"
    echo
fi

if [ -f "$wocheMinus2Post" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE VORLETZTE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$wocheMinus2Prae
    mv -v $wocheMinus2Prae $wocheMinus2Post && echo -e "${BGreen}VORLETZTE WOCHE ERFOLGREICH${NC}"
    echo
fi

if [ -f "$wocheMinus1Post" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE LETZTE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$wocheMinus1Prae
    mv -v $wocheMinus1Prae $wocheMinus1Post && echo -e "${BGreen}LETZTE WOCHE ERFOLGREICH${NC}"
    echo
fi

if [ -f "$woche0Post" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE DIESE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$woche0Prae
    mv -v $woche0Prae $woche0Post && echo -e "${BGreen}DIESE WOCHE ERFOLGREICH${NC}"
    echo
fi

if [ -f "$woche1Post" ];
then
    :
else
    echo -e "${BRed}VERSUCHE NÄCHSTE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$woche1Prae
    mv -v $woche1Prae $woche1Post && echo -e "${BGreen}NÄCHSTE WOCHE ERFOLGREICH${NC}"
    echo
fi

if [ -f "$woche2Post" ];
then
    :
else
    echo -e "${BRed}VERSUCHE ÜBERNÄCHSTE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$woche2Prae
    mv -v $woche2Prae $woche2Post && echo -e "${BGreen}ÜBERNÄCHSTE WOCHE ERFOLGREICH${NC}"
    echo
fi

if [ -f "$woche3Post" ];
then
    :
else
    echo -e "${BRed}VERSUCHE ÜBERÜBERNÄCHSTE WOCHE${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date '+%Y')/$(date '+%m')/$woche3Prae
    mv -v $woche3Prae $woche3Post && echo -e "${BGreen}ÜBERÜBERNÄCHSTE WOCHE ERFOLGREICH${NC}"
    echo
fi
