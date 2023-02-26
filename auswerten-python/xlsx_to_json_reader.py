import json
import os
import pandas
import datetime
#from colorama import init, Fore
#init(autoreset=True)

# Listest alle dateien im Menüordner auf
listedateien = os.listdir("menues")
# Sortiert die Dateien nach Name(Datum)
listedateien.sort()

# Zum entfernen aus dict
zuentfernen = [
    "Gluten", "Crustacés",
    "Oeuf", "Poisson",
    "Arachides", "Soja",
    "Lait", "Fruits à coques",
    "Céleri", "Moutarde",
    "Graine de sésame", "Sulfite",
    "Mollusques", "Lupin"
]

zahlenliste = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]

zahlzuwochentag = {
     0:	"Lundi",
     1:	"Mardi",
     2:	"Mercredi",
     3:	"Jeudi",
     4:	"Vendredi",
     5:	"Samedi",
     6:	"Dimanche"
}

# Schreibt öffnende Klammer für die JSON
with open("output.json", "w", encoding="utf-16") as file: file.write("{")

# Wertet alle Excel-Tabellen aus
# Packt alle Tabellen in eine JSON

# Formatbeispiel:
# "drei.zehn": [
#   "Lundi",
#   "Minestrone",
#   "Poëlee de poulet aux légumes",
#   "Cœur de blé",
#   null,       # null bedeutet, dass das Gericht aus weniger Teilen besteht als es maximal gibt  
#   "Fruit"     # Kann an dritter und fünfter Stelle der Liste passieren
# ],            # Entweder keine Vorspeise oder Beilage glaube ich

for file in listedateien:
    if file.startswith("~"):
        print()
        del listedateien[listedateien.index(file)]
        #listedateien.pop(file)

i = 1
for file in listedateien:
    if file.endswith(".xlsx"):
        print(file) # Dateiname

        # Extrahiert text aus Datei
        # Macht es zu einem Dictionary
        excel_data = pandas.read_excel("menues/" + file)
        jsondict = json.loads(excel_data.to_json())


        # Formatiert den Dict
        # und entfernt unnötige Allergene
        jsondict[f"Week{i}"] = jsondict["Plat"]
        del jsondict["Plat"]

        for thing in zuentfernen: jsondict.pop(thing)

        # Packt die Daten jeweils in eine Liste und diese Listen dann in den Dict-Key Date1 - Date4
        # Bsp: ["Lundi", 13, 10]
        jsondict[f"Date{i}"] = {}
        for x in range(16):
            if x % 5 == 0:
                # Nimmt sich den Unix Timestamp aus der Tabelle und verwandelt ihn zu nem gescheiten Datum
                unixdate = int(str(jsondict["Date"][str(x)])[0:-3])
                unixtodate = datetime.datetime.fromtimestamp(unixdate)
                
                # [Jahr, Monat, Tag] als Zahlen
                unxto_list = str(unixtodate)[0:10].split("-")

                # Nimmt sich die Liste [Jahr, Monat, Tag] und holt sich den Wochentag des jeweiligen Datums
                # Dieser ist aber als Zahl von 0 bis 6. Wird nun mit Hilfe des dicts zahlzuwochentag[] zum Wort
                weekday = zahlzuwochentag[datetime.datetime(int(unxto_list[0]), int(unxto_list[1]), int(unxto_list[2]), 0, 0, 0).weekday()]

                # Hier wird die Liste erstellt; bsp: ["Lundi", 13, 10, 2022]
                jsondict[f"Date{i}"][str((x/5) + 1)[0]] = [weekday, unxto_list[2], unxto_list[1], unxto_list[0]]
                
        # Entfernt den Key "Date", da nicht mehr gebraucht
        jsondict.pop("Date")

        # Formatiert die sachen zu handlichen Stücken (jeweils ein Tag)
        speicher, d = {}, 1
        for k in range(20):
            if k % 5 == 0:
                speicher[int(k/5)] = [
                jsondict[f"Date{i}"][str(k/5+1)[0]],        # Datums liste aus den vier Teilen, Bsp: ["Lundi", 13, 10, 2022] (siehe Zeile 93)
                jsondict[f"Date{i}"][str(k/5+1)[0]][0],     # Nur der Wochentag
                                                            # Die verschiedenen Teile des Essens:
                jsondict[f"Week{i}"][str(k)],               # Suppe
                jsondict[f"Week{i}"][str(k+1)],             # Hauptspeise
                jsondict[f"Week{i}"][str(k+2)],             # Hauptspeise
                jsondict[f"Week{i}"][str(k+3)],             # Hauptspeise
                jsondict[f"Week{i}"][str(k+4)]]             # Nachtisch
            d += 1

        # Packt die Tage zurück in die Woche
        jsondict[f"Week{i}"] = speicher
        # Entfernt den nun unnötigen Key "Date{x}"
        if i <= len(listedateien): del jsondict[f"Date{i}"]

        # Geht nun einzeln durch die Tage und formatiert sie final
        for dayofweek in range(4):

            # Definiert den jeweiligen Tag und Monat des Tages
            day = jsondict[f"Week{i}"][dayofweek][0][1]          # In Woche{x}, Tag x, Datumsliste [Wochentag, __Datum__, Monat, Jahr], das Datum
            month = jsondict[f"Week{i}"][dayofweek][0][2]        # Datumsliste [Wochentag, Datum, __Monat__, Jahr], den Monat
            year  = jsondict[f"Week{i}"][dayofweek][0][3]        # Datumsliste [Wochentag, Datum, Monat, __Jahr__], das Jahr

            # Erstellt den Tag mit dem Namensformat Tag.Monat und packt den entsprechenden Tag rein
            jsondict[f"{day}.{month}.{year}"] = jsondict[f"Week{i}"][dayofweek] # Löscht dann die Liste mit den drei Teilen des Datums des jeweiligen Tages
            jsondict[f"Week{i}"][dayofweek].pop(0)
            
            # Falls Tag während Examen, bewegen des Textes "Menu examen" zu einheitlichen Platz
            # Falls Tag keine Suppe hat und kein Examen, dann ist es ein Feiertag
            # --> Ersetzen des Feiertagsnamen mit "Jour férié"
            # tag[1] = Suppe
            # tag[0] müsste Wochentag sein
            if jsondict[f"{day}.{str(month)}.{year}"][2] == "Menu examen":
                jsondict[f"{day}.{str(month)}.{year}"][2] = None
                jsondict[f"{day}.{str(month)}.{year}"][3] = "Menu examen"
            elif jsondict[f"{day}.{str(month)}.{year}"][1] == None:
                jsondict[f"{day}.{str(month)}.{year}"][3] = "Jour férié"

        # Nach dem finalen Formatieren der Tage wird dann die Woche, aus der die Daten genommen wurden, entfernt
        jsondict.pop(f"Week{i}")

        # Konvertiert den Dictionary zu einem String
        # Entfernt die schliessende Klammer
        # Fügt bei jeder Woche bis auf die Letzte ein Komma ans Ende an
        dictstring = json.dumps(jsondict)
        dictstring = dictstring[1:-1]
        if i != len(listedateien):
            dictstring += ","

        # Fügt die Woche ans Ende der JSON an
        with open("output.json", "a", encoding="utf-16") as file:
            file.write(dictstring)
        i += 1

# Schliesst JSON mit End-Klammer
with open("output.json", "a", encoding="utf-16") as f:
    f.write("}")

try: os.system("mv output.json outputs/output.json")
except: "joa ka windows halt"
else: os.system("move output.json outputs/output.json")