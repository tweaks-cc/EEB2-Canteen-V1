import pdfplumber
import os

#Debbuging
os.system("clear")
filename = os.listdir("menues")
print(filename)

monate = {
  "octobre": True
}

def processrawtext(rawtext):
  print("Converting... beep boop")
  splittext = rawtext.split()
  dates = {}
  #print(splittext)
  i = 0
  for item in splittext:
    
    if item == i:
      dates.append(splittext[i:i-2])
    i += 1
    #print(dates)
 
with pdfplumber.open(f"menues/{filename[0]}") as rawpdf:
  rawtext = rawpdf.pages[0].extract_text()
  processedtext = processrawtext(rawtext)
