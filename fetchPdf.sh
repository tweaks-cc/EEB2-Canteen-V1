#!/bin/bash

# Wie die PDF heißen soll, nachdem sie heruntergeladen wurde.

danach=input.pdf

# Definitionen der Farben

BGreen='\033[1;32m' # Bold Green
BRed='\033[1;31m' # Bold Red
NC='\033[0m' # No Color

# Falls es schon eine input.pdf im Ordner gibt, muss sie gelöscht werden, sonst wird das Skript nicht funktionieren.

rm $danach

# Die Kantine hat immer mehrere Version von dem Menu, meistens zwischen 1 und 10, deswegen gehe ich durch verschieden Versionen von 10 aus runter bis ich die aktuellste Version finde.

if [ -f "$danach" ];
then
    :
else
    echo
    echo -e "${BRed}VERSUCHE V.10${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-10.pdf
    mv -v Menu-du-mois-de-2022-10.pdf $danach && echo -e "${BGreen}V.10 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.9${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-9.pdf
    mv -v Menu-du-mois-de-2022-9.pdf $danach && echo -e "${BGreen}V.9 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.8${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-8.pdf
    mv -v Menu-du-mois-de-2022-8.pdf $danach && echo -e "${BGreen}V.8 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.7${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-7.pdf
    mv -v Menu-du-mois-de-2022-7.pdf $danach && echo -e "${BGreen}V.7 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.6${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-6.pdf
    mv -v Menu-du-mois-de-2022-6.pdf $danach && echo -e "${BGreen}V.6 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.5${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-5.pdf
    mv -v Menu-du-mois-de-2022-5.pdf $danach && echo -e "${BGreen}V.5 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.4${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-4.pdf
    mv -v Menu-du-mois-de-2022-4.pdf $danach && echo -e "${BGreen}V.4 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.3${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-3.pdf
    mv -v Menu-du-mois-de-2022-3.pdf $danach && echo -e "${BGreen}V.3 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.2${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-2.pdf
    mv -v Menu-du-mois-de-2022-2.pdf $danach && echo -e "${BGreen}V.2 ERFOLGREICH${NC}" && echo
fi

if [ -f "$danach" ];
then
    :
else
    echo 
    echo -e "${BRed}VERSUCHE V.1${NC}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/2022/$(date '+%m')/Menu-du-mois-de-2022-1.pdf
    mv -v Menu-du-mois-de-2022-1.pdf $danach && echo -e "${BGreen}V.1 ERFOLGREICH${NC}" && echo
fi

