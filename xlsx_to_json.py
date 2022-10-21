import pandas as pd
import pdfplumber
import json
import os

#Debbuging
try : os.system("clear")
except: "ok"
try: os.system("cls")
except: "what?"

filelist = os.listdir("menues")
filelist.sort()

months = {
    "janvier":   1,
    "février":   2,
    "mars":      3,
    "avril":     4,
    "mai":       5,
    "juin":      6,
    "juillet":   7,
    "août":      8,
    "septembre": 9,
    "octobre":   10,
    "novembre":  11,
    "décembre":  12
}

os.remove("aktuellermonat.json")

#Schreibt öffnende Klammer für die JSON
f = open("aktuellermonat.json", "w")
f.write('{')
f.close()

def processrawtext(rawtext):
  #Nimmt sich den text des ganzen PDFs und filtert Wochentag und Datum raus
  splittext = rawtext.split()
  dates = []
  i = 0
  #Geht durch alle Elemente des PDFtextes und holt sich die Datums raus
  for item in splittext:
    for month in months:
      if item == month:
        date = " ".join(splittext[i-2: i+1])
        dates.append(date)
    i += 1
  return dates


#Geht durch alle Dateien im Verzeichnis und verarbeitet nur die erste PDF
for file in filelist:
  if file.endswith(".pdf"):
    with pdfplumber.open(f"menues/{file}") as rawpdf:
      rawtext = rawpdf.pages[0].extract_text()
      datelist = processrawtext(rawtext)


#Wertet alle xlsx Tabellen aus
#Packt alle Tabellen in eine JSON
i = 1
for file in filelist:
    if file.endswith(".xlsx"):
        print(file) #Dateiname

        #Extrahiert text aus Datei
        #Macht es zu einem Dictionary
        excel_data_df = pd.read_excel("menues/" + file)

        jsondict = json.loads(excel_data_df.to_json())

        #Öffnet ZielJSON und formatiert den Dict
        #Entfernt unnötige Allergene
        f = open("aktuellermonat.json", "a")

        jsondict[f"Week{i}"] = jsondict["Plat"]
        del jsondict["Plat"]

        jsondict.pop("Gluten")
        jsondict.pop("Crustacés")
        jsondict.pop("Oeuf")
        jsondict.pop("Poisson")
        jsondict.pop("Arachides")
        jsondict.pop("Soja")
        jsondict.pop("Lait")
        jsondict.pop("Fruits à coques")
        jsondict.pop("Céleri")
        jsondict.pop("Moutarde")
        jsondict.pop("Graine de sésame")
        jsondict.pop("Sulfite")
        jsondict.pop("Mollusques")
        jsondict.pop("Lupin")

        jsondict.pop("Date")

        dates = {}
        jsondict[f"Date{i}"] = {}

        #Sorgt dafür das die verschiedenen Wochen/Tabellen/Dicts in eine JSON gehen (fehlerfrei)
        dictstring = json.dumps(jsondict)
        dictstring = dictstring[1:-1]
        if i != len(filelist)-1:
            dictstring += ","

        f.write(dictstring)
        f.close()
        i += 1

#Schliesst JSON mit End-Klammer
with open("aktuellermonat.json", "a") as f:
    f.write("}")

#Datums werden in die JSON eingetragen
with open("aktuellermonat.json", "r") as f:
    jsonfile = json.loads(f.read())

#Mantag = 1
#Dienstag = 2
#etc.
i = 0
for j in range(len(datelist)-3):
    if j % 4 == 0:
        i += 1
        jsonfile[f"Date{i}"] = {
            1: datelist[j],
            2: datelist[j+1],
            3: datelist[j+2],
            4: datelist[j+3]
        }

with open("aktuellermonat.json", "w") as f:
    f.write(json.dumps(jsonfile))

with open("aktuellermonat.json", "r") as f:
    jsonfile = json.loads(f.read())



#Formatiert die Infos in der JSON schöner
for k in range(4):
	speicher, d = {}, 1
	for i in range(20):
		if i % 5 == 0:
			speicher[int(i/5)] = [
            jsonfile[f"Date{k+1}"][str(d)].split(),
            jsonfile[f"Week{k+1}"][str(i)],
            jsonfile[f"Week{k+1}"][str(i+1)],
            jsonfile[f"Week{k+1}"][str(i+2)],
            jsonfile[f"Week{k+1}"][str(i+3)],
            jsonfile[f"Week{k+1}"][str(i+4)]]
			d += 1

	jsonfile[f"Week{k+1}"] = speicher
	if k <= 3: del jsonfile[f"Date{k+1}"]

def monthtoint(monthstr):
	return months[monthstr]

for wint in range(4):
	for dint in range(4):
		day = jsonfile[f"Week{wint+1}"][dint][0][1]
		month = monthtoint(jsonfile[f"Week{wint+1}"][dint][0][2])
		jsonfile[f"{day}.{month}"] = jsonfile[f"Week{wint+1}"][dint]
		jsonfile[f"Week{wint+1}"][dint].pop(0)
	
	del jsonfile[f"Week{wint+1}"]

with open("aktuellermonat.json", "w") as f:
	f.write(json.dumps(jsonfile))