import pdfplumber
import os

#Debbuging
try : os.system("clear")
except: os.system("cls")
filelist = os.listdir("menues")

months = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

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
      dates = processrawtext(rawtext)

for date in dates:
  print(date)