import json
import os
import pandas

# Screenclearing
try : os.system("clear")
except: "ok"
try: os.system("cls")
except: "what?"

# Listest alle dateien im Menüordner auf
filelist = os.listdir("menues")
filelist.sort() #  Sortiert die Dateien nach Name(Datum)

# Monatsstring Englisch/Französisch zu Zahl (bsp. Januar: 1)
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


# Cleart die Datei
try: os.remove("output.json")
except FileNotFoundError: "Erstes mal, oder Datei nicht da"

# Schreibt öffnende Klammer für die JSON
with open("output.json", "w") as file: file.write("{")



# Wertet alle xlsx Tabellen aus
# Packt alle Tabellen in eine JSON
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

        filename = file.split("-")
        jsondict[f"Date{i}"] = {
            "1": ["Lundi",   filename[1],filename[5][0:-5]],
            "2": ["Mardi",   filename[2],filename[5][0:-5]],
            "3": ["Jeudi",   filename[3],filename[5][0:-5]],
            "4": ["Vendredi",filename[4],filename[5][0:-5]]
        }

        # Sorgt dafür das die verschiedenen Wochen/Tabellen/Dicts in eine JSON gehen (fehlerfrei)
        dictstring = json.dumps(jsondict)
        dictstring = dictstring[1:-1]
        if i != len(filelist):
            dictstring += ","

        with open("output.json", "a") as file: file.write(dictstring)
        i += 1

# Schliesst JSON mit End-Klammer
with open("output.json", "a") as f:
    f.write("}")


with open("output.json", "r") as f:
    jsonfile = json.loads(f.read())


#Formatiert die Infos in der JSON schöner
for k in range(4):
	speicher, d = {}, 1
	for i in range(20):
		if i % 5 == 0:
			speicher[int(i/5)] = [
            jsonfile[f"Date{k+1}"][str(d)],
            jsonfile[f"Date{k+1}"][str(d)][0],
            jsonfile[f"Week{k+1}"][str(i)],
            jsonfile[f"Week{k+1}"][str(i+1)],
            jsonfile[f"Week{k+1}"][str(i+2)],
            jsonfile[f"Week{k+1}"][str(i+3)],
            jsonfile[f"Week{k+1}"][str(i+4)]]
			d += 1

	jsonfile[f"Week{k+1}"] = speicher
	if k <= 3: del jsonfile[f"Date{k+1}"]


with open("output.json", "w") as f:
	f.write(json.dumps(jsonfile))


def monthtoint(monthstr):
	return months[monthstr.lower()]

for wint in range(4):
    for dint in range(4):
        day = jsonfile[f"Week{wint+1}"][dint][0][1]
        month = monthtoint(jsonfile[f"Week{wint+1}"][dint][0][2])
        jsonfile[f"{day}.{month}"] = jsonfile[f"Week{wint+1}"][dint]
        jsonfile[f"Week{wint+1}"][dint].pop(0)
	
    del jsonfile[f"Week{wint+1}"]

with open("output.json", "w") as f:
	f.write(json.dumps(jsonfile))