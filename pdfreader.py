import pdfplumber
import os

#Debbuging
try: os.system("cls")
except: os.system("clear")
filename = os.listdir("menues")
print(filename)

monate = {
  "octobre": True
}

def processrawtext(rawtext):
  #print("Converting... beep boop")
  splittext = rawtext.split()
  print(splittext)
  dates = []
  i = 0
  for item in splittext:
    if item == filename[0].replace(".pdf", ""):
      date = " ".join(splittext[i-2: i+1])
      dates.append(date)
    i += 1

  print(dates)
  print(soups)

with pdfplumber.open(f"menues/{filename[0]}") as rawpdf:
  rawtext = rawpdf.pages[0].extract_text()
  processedtext = processrawtext(rawtext)
