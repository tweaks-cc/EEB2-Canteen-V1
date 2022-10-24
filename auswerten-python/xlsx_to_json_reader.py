import json
import os
import pandas

# Screenclearing
try: os.system("cls")
except: "Linuxkek"
try : os.system("clear")
except: "ok"

# Listest alle dateien im Menüordner auf
filelist = os.listdir("menues")
# Sortiert die Dateien nach Name(Datum)
filelist.sort()

# Zum entfernen aus dict
zuentfernen = [
    "Gluten", "Crustacés",
    "Oeuf", "Poisson",
    "Arachides", "Soja",
    "Lait", "Fruits à coques",
    "Céleri", "Moutarde",
    "Graine de sésame", "Sulfite",
    "Mollusques", "Lupin", "Date"
]

# Entfernt die JSON falls existent
try: os.remove("output.json")
except FileNotFoundError: "Erstes mal, oder Datei nicht da"

# Schreibt öffnende Klammer für die JSON
with open("output.json", "w") as file: file.write("{")

# Monatsstring zu Zahl (bsp. Januar: 1)
months = {
    "januar":    1,
    "februar":   2,
    "märz":     3,
    "april":     4,
    "mai":       5,
    "juni":      6,
    "juli":      7,
    "august":    8,
    "september": 9,
    "oktober":   10,
    "november":  11,
    "dezember":  12,
}
# Nimmt einen Monat als String und return den Monat als Zahl
def monthtoint(monthstr):
	return months[monthstr.lower()]


# Wertet alle Excel-Tabellen aus
# Packt alle Tabellen in eine JSON

# Formatbeispiel:
# "3.10": [
#   "Lundi",
#   "Minestrone",
#   "Poëlee de poulet aux légumes",
#   "Cœur de blé",
#   null,       # null bedeutet, dass das Gericht aus weniger Teilen besteht als es maximal gibt  
#   "Fruit"     # Kann an dritter und fünfter Stelle der Liste passieren
# ],            # Entweder keine Vorspeise oder Beilage glaube ich

i = 1
for file in filelist:
    if file.endswith(".xlsx"):
        print(file) # Dateiname

        # Extrahiert text aus Datei
        # Macht es zu einem Dictionary
        excel_data_df = pandas.read_excel("menues/" + file)
        jsondict = json.loads(excel_data_df.to_json())


        # Formatiert den Dict
        # und entfernt unnötige Allergene
        jsondict[f"Week{i}"] = jsondict["Plat"]
        del jsondict["Plat"]

        for thing in zuentfernen: jsondict.pop(thing)

        # Packt die Daten jeweils in eine Liste und diese Listen dann in den Dict-Key Date1 - Date4
        # Zieht sich die Daten aus dem Namen der Datei
        # Bsp: ["Lundi", 13, "Oktober"]
        filename = file.split("-")
        jsondict[f"Date{i}"] = {
            "1": ["Lundi",   filename[1],filename[5][0:-5]],
            "2": ["Mardi",   filename[2],filename[5][0:-5]],
            "3": ["Jeudi",   filename[3],filename[5][0:-5]],
            "4": ["Vendredi",filename[4],filename[5][0:-5]]
        }

        # Formatiert die sachen zu handlichen Stücken (jeweils ein Tag)
        speicher, d = {}, 1
        for k in range(20):
            if k % 5 == 0:
                speicher[int(k/5)] = [
                jsondict[f"Date{i}"][str(int(k/5)+1)],      # Datums liste aus den drei Teilen, Bsp: ["Lundi", 13, "Oktober"] (siehe Zeile 87-94)
                jsondict[f"Date{i}"][str(int(k/5)+1)][0],   # Nur der Wochentag
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
        if i <= len(filelist): del jsondict[f"Date{i}"]

        # Geht nun einzeln durch die Tage und formatiert sie final
        for dayofweek in range(4):

            # Definiert den jeweiligen Tag und Monat des Tages
            day = jsondict[f"Week{i}"][dayofweek][0][1]                 # In Woche{x}, Tag x, Datumsliste [Wochentag, __Datum__, Monat], das Datum
            month = monthtoint(jsondict[f"Week{i}"][dayofweek][0][2])   # Datumsliste [Wochentag, Datum, __Monat__], den Monatsstring zur Zahl mit Funktion Z.50

            # Erstellt den Tag mit dem Namensformat Tag.Monat und packt den entsprechenden Tag rein
            jsondict[f"{day}.{month}"] = jsondict[f"Week{i}"][dayofweek]
            # Löscht dann die Liste mit den drei Teilen des Datums des jeweiligen Tages
            jsondict[f"Week{i}"][dayofweek].pop(0)

        # Nach dem finalen Formatieren der Tage wird dann die Woche, aus der die Daten genommen wurden, entfernt
        jsondict.pop(f"Week{i}")

        # Konvertiert den Dictionary zu einem String
        # Entfernt die schliessende Klammer
        # Fügt bei jeder Woche bis auf die Letzte ein Komma ans Ende an
        dictstring = json.dumps(jsondict)
        dictstring = dictstring[1:-1]
        if i != len(filelist):
            dictstring += ","

        # Fügt die Woche ans Ende der JSON an
        with open("output.json", "a") as file: file.write(dictstring)
        i += 1

# Schliesst JSON mit End-Klammer
with open("output.json", "a") as f:
    f.write("}")
