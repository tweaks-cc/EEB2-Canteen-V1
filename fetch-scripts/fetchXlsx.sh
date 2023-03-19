#!/bin/bash

# Definitionen der Farben.

FGruen='\033[1;32m' # Fettes Grün
FRot='\033[1;31m'   # Fettes Rot
FBlau='\033[1;34m'  # Fettes Blau
KF='\033[0m'        # Keine Farbe

# Wie die XLSXs heißen, bevor sie heruntergeladen werden.

wocheMinus4Prae=Semaine-$(date --date="-4 Week" +%W)-$(date --date="Sunday -6 Day -4 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day -4 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day -4 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day -4 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
wocheMinus3Prae=Semaine-$(date --date="-3 Week" +%W)-$(date --date="Sunday -6 Day -3 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day -3 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day -3 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day -3 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
wocheMinus2Prae=Semaine-$(date --date="-2 Week" +%W)-$(date --date="Sunday -6 Day -2 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day -2 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day -2 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day -2 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
wocheMinus1Prae=Semaine-$(date --date="-1 Week" +%W)-$(date --date="Sunday -6 Day -1 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day -1 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day -1 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day -1 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
woche0Prae=Semaine-$(date --date="+0 Week" +%W)-$(date --date="Sunday -6 Day +0 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day +0 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day +0 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day +0 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
woche1Prae=Semaine-$(date --date="+1 Week" +%W)-$(date --date="Sunday -6 Day +1 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day +1 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day +1 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day +1 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
woche2Prae=Semaine-$(date --date="+2 Week" +%W)-$(date --date="Sunday -6 Day +2 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day +2 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day +2 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day +2 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
woche3Prae=Semaine-$(date --date="+3 Week" +%W)-$(date --date="Sunday -6 Day +3 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day +3 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day +3 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day +3 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx
woche4Prae=Semaine-$(date --date="+4 Week" +%W)-$(date --date="Sunday -6 Day +4 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -6 Day +4 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date --date="Sunday -2 Day +4 Week" +%d)-$(env LC_TIME=fr_FR.UTF-8 date --date="Sunday -2 Day +4 Week" +%B | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx

verzeichnis=../auswerten-python/menues

# Wie die XLSXs heißen sollen, nachdem sie heruntergeladen wurden.

wocheMinus4Post=$verzeichnis/input-$(date --date="Sunday -6 Day -4 Week" +%d)-$(date --date="Sunday -5 Day -4 Week" +%d)-$(date --date="Sunday -4 Day -3 Week" +%d)-$(date --date="Sunday -2 Day -4 Week" +%d)-$(date +%B).xlsx
wocheMinus3Post=$verzeichnis/input-$(date --date="Sunday -6 Day -3 Week" +%d)-$(date --date="Sunday -5 Day -3 Week" +%d)-$(date --date="Sunday -3 Day -3 Week" +%d)-$(date --date="Sunday -2 Day -3 Week" +%d)-$(date +%B).xlsx
wocheMinus2Post=$verzeichnis/input-$(date --date="Sunday -6 Day -2 Week" +%d)-$(date --date="Sunday -5 Day -2 Week" +%d)-$(date --date="Sunday -3 Day -2 Week" +%d)-$(date --date="Sunday -2 Day -2 Week" +%d)-$(date +%B).xlsx
wocheMinus1Post=$verzeichnis/input-$(date --date="Sunday -6 Day -1 Week" +%d)-$(date --date="Sunday -5 Day -1 Week" +%d)-$(date --date="Sunday -3 Day -1 Week" +%d)-$(date --date="Sunday -2 Day -1 Week" +%d)-$(date +%B).xlsx
woche0Post=$verzeichnis/input-$(date --date="Sunday -6 Day +0 Week" +%d)-$(date --date="Sunday -5 Day +0 Week" +%d)-$(date --date="Sunday -3 Day +0 Week" +%d)-$(date --date="Sunday -2 Day +0 Week" +%d)-$(date +%B).xlsx
woche1Post=$verzeichnis/input-$(date --date="Sunday -6 Day +1 Week" +%d)-$(date --date="Sunday -5 Day +1 Week" +%d)-$(date --date="Sunday -3 Day +1 Week" +%d)-$(date --date="Sunday -2 Day +1 Week" +%d)-$(date +%B).xlsx
woche2Post=$verzeichnis/input-$(date --date="Sunday -6 Day +2 Week" +%d)-$(date --date="Sunday -5 Day +2 Week" +%d)-$(date --date="Sunday -3 Day +2 Week" +%d)-$(date --date="Sunday -2 Day +2 Week" +%d)-$(date +%B).xlsx
woche3Post=$verzeichnis/input-$(date --date="Sunday -6 Day +3 Week" +%d)-$(date --date="Sunday -5 Day +3 Week" +%d)-$(date --date="Sunday -3 Day +3 Week" +%d)-$(date --date="Sunday -2 Day +3 Week" +%d)-$(date +%B).xlsx
woche4Post=$verzeichnis/input-$(date --date="Sunday -6 Day +4 Week" +%d)-$(date --date="Sunday -5 Day +4 Week" +%d)-$(date --date="Sunday -3 Day +4 Week" +%d)-$(date --date="Sunday -2 Day +4 Week" +%d)-$(date +%B).xlsx

# Falls es schon mehrere inputWocheX.xlsx im Ordner gibt, müssen sie gelöscht werden, sonst wird das Skript nicht funktionieren.

echo ; echo -e "${FBlau}ENTFERNE EXISTIERENDE DATEIEN${KF}"
rm -v $verzeichnis/*
echo

# Die XLSXs werden gefetcht.

# Vorvorvorletzte Woche

echo -e "${FBlau}SUCHE VORVORVORLETZTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-4 Week -1 Month" +%Y)/$(date --date="-4 Week -1 Month" +%m)/$wocheMinus4Prae
mv -v $wocheMinus4Prae $wocheMinus4Post && echo -e "${FGruen}VORVORVORLETZTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}VORVORVORLETZTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$wocheMinus4Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE VORVORVORLETZTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-4 Week" +%Y)/$(date --date="-4 Week" +%m)/$wocheMinus4Prae
    mv -v $wocheMinus4Prae $wocheMinus4Post && echo -e "${FGruen}VORVORVORLETZTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}VORVORVORLETZTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Vorvorletzte Woche

echo -e "${FBlau}SUCHE VORVORLETZTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-3 Week -1 Month" +%Y)/$(date --date="-3 Week -1 Month" +%m)/$wocheMinus3Prae
mv -v $wocheMinus3Prae $wocheMinus3Post && echo -e "${FGruen}VORVORLETZTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}VORVORLETZTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$wocheMinus3Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE VORVORLETZTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-3 Week" +%Y)/$(date --date="-3 Week" +%m)/$wocheMinus3Prae
    mv -v $wocheMinus3Prae $wocheMinus3Post && echo -e "${FGruen}VORVORLETZTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}VORVORLETZTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Vorletzte Woche

echo -e "${FBlau}SUCHE VORLETZTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-2 Week -1 Month" +%Y)/$(date --date="-2 Week -1 Month" +%m)/$wocheMinus2Prae
mv -v $wocheMinus2Prae $wocheMinus2Post && echo -e "${FGruen}VORLETZTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}VORLETZTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$wocheMinus2Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE VORLETZTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-2 Week" +%Y)/$(date --date="-2 Week" +%m)/$wocheMinus2Prae
    mv -v $wocheMinus2Prae $wocheMinus2Post && echo -e "${FGruen}VORLETZTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}VORLETZTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Letzte Woche

echo -e "${FBlau}SUCHE LETZTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-1 Week -1 Month" +%Y)/$(date --date="-1 Week -1 Month" +%m)/$wocheMinus1Prae
mv -v $wocheMinus1Prae $wocheMinus1Post && echo -e "${FGruen}LETZTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}LETZTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$wocheMinus1Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE LETZTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="-1 Week" +%Y)/$(date --date="-1 Week" +%m)/$wocheMinus1Prae
    mv -v $wocheMinus1Prae $wocheMinus1Post && echo -e "${FGruen}LETZTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}LETZTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Diese Woche

echo -e "${FBlau}SUCHE DIESE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+0 Week -1 Month" +%Y)/$(date --date="+0 Week -1 Month" +%m)/$woche0Prae
mv -v $woche0Prae $woche0Post && echo -e "${FGruen}DIESE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}DIESE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$woche0Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE DIESE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+0 Week" +%Y)/$(date --date="+0 Week" +%m)/$woche0Prae
    mv -v $woche0Prae $woche0Post && echo -e "${FGruen}DIESE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}DIESE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Nächste Woche

echo -e "${FBlau}SUCHE NÄCHSTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+1 Week -1 Month" +%Y)/$(date --date="+1 Week -1 Month" +%m)/$woche1Prae
mv -v $woche1Prae $woche1Post && echo -e "${FGruen}NÄCHSTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}NÄCHSTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$woche1Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE NÄCHSTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+1 Week" +%Y)/$(date --date="+1 Week" +%m)/$woche1Prae
    mv -v $woche1Prae $woche1Post && echo -e "${FGruen}NÄCHSTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}NÄCHSTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Übernächste Woche

echo -e "${FBlau}SUCHE ÜBERNÄCHSTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+2 Week -1 Month" +%Y)/$(date --date="+2 Week -1 Month" +%m)/$woche2Prae
mv -v $woche2Prae $woche2Post && echo -e "${FGruen}ÜBERNÄCHSTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}ÜBERNÄCHSTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$woche2Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE ÜBERNÄCHSTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+2 Week" +%Y)/$(date --date="+2 Week" +%m)/$woche2Prae
    mv -v $woche2Prae $woche2Post && echo -e "${FGruen}ÜBERNÄCHSTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}ÜBERNÄCHSTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Überübernächste Woche

echo -e "${FBlau}SUCHE ÜBERÜBERNÄCHSTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+3 Week -1 Month" +%Y)/$(date --date="+3 Week -1 Month" +%m)/$woche3Prae
mv -v $woche3Prae $woche3Post && echo -e "${FGruen}ÜBERÜBERNÄCHSTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}ÜBERÜBERNÄCHSTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$woche3Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE ÜBERÜBERNÄCHSTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+3 Week" +%Y)/$(date --date="+3 Week" +%m)/$woche3Prae
    mv -v $woche3Prae $woche3Post && echo -e "${FGruen}ÜBERÜBERNÄCHSTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}ÜBERÜBERNÄCHSTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi

# Überüberübernächste Woche

echo -e "${FBlau}SUCHE ÜBERÜBERÜBERNÄCHSTE WOCHE IM LETZTEN MONAT${KF}"
wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+4 Week -1 Month" +%Y)/$(date --date="+4 Week -1 Month" +%m)/$woche4Prae
mv -v $woche4Prae $woche4Post && echo -e "${FGruen}ÜBERÜBERÜBERNÄCHSTE WOCHE IM LETZTEN MONAT GEFUNDEN${KF}" || echo -e "${FRot}ÜBERÜBERÜBERNÄCHSTE WOCHE IM LETZTEN MONAT NICHT GEFUNDEN${KF}"
echo

if [ -f "$woche4Post" ];
then
    :
else
    echo -e "${FBlau}SUCHE ÜBERÜBERÜBERNÄCHSTE WOCHE${KF}"
    wget -nv https://www.woluweparents.org/wp-content/uploads/$(date --date="+4 Week" +%Y)/$(date --date="+4 Week" +%m)/$woche4Prae
    mv -v $woche4Prae $woche4Post && echo -e "${FGruen}ÜBERÜBERÜBERNÄCHSTE WOCHE GEFUNDEN${KF}" || echo -e "${FRot}ÜBERÜBERÜBERNÄCHSTE WOCHE NICHT GEFUNDEN${KF}"
    echo
fi