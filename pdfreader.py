import pdfplumber
import os

#Debbuging
try: os.system("cls")
except: os.system("clear")
filename = os.listdir("menues")

months = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]


def processrawtext(rawtext):
  #print("Converting... beep boop")
  splittext = rawtext.split()
  dates = []
  i = 0
  for item in splittext:
    for month in months:
      if item == month:
        date = " ".join(splittext[i-2: i+1])
        dates.append(date)
    i += 1
  return dates

for file in filename:
  if file.endswith(".pdf"):
    with pdfplumber.open(f"menues/{filename[0]}") as rawpdf:
      rawtext = rawpdf.pages[0].extract_text()
      dates = processrawtext(rawtext)

for date in dates:
  print(date)