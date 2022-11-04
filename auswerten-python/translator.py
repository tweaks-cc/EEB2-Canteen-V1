# Lutscht sich alle neuen Teile des Monats/Woche und übersetzt alle erstmal auf Deutsch und Englisch



import json
from googletrans import Translator
from colorama import init, Fore, Back, Style
init(autoreset=True)
translator = Translator()


with open("output.json", "r") as file:
    originaledatei = json.loads(file.read())
    

Suppen   = []
Suppen_de = {}
Hauptspeisenteile   = []
Hauptspeisenteile_de = {}

for day in originaledatei:
    Suppen.append(originaledatei[day][1])
    Hauptspeisenteile.append(originaledatei[day][2])
    Hauptspeisenteile.append(originaledatei[day][3])
    Hauptspeisenteile.append(originaledatei[day][4])

Suppenstr = ""

for thing in Suppen:
    Suppenstr += thing + ";"


# print(Suppenstr)
Suppenstr_de = translator.translate(Suppenstr, src="fr", dest="de").text
Suppenlist_de = Suppenstr_de.split(";")
Suppenlist_de.pop()

if len(Suppenlist_de) != len(Suppen):
    fehlend = len(Suppen) - len(Suppenlist_de)
    neuesuppenliste = Suppen[-fehlend:len(Suppen)]
    Suppenstr = ""
    for thing in neuesuppenliste:
        Suppenstr += thing + ";"
    Suppenstr_de = translator.translate(Suppenstr, src="fr", dest="de").text
    Suppenlist_de += Suppenstr_de.split(";")
    Suppenlist_de.pop()
    
"""
print(len(Suppen))
print(Suppen)
print(len(Suppenlist_de))
print(Suppenlist_de)
"""

for x in range(len(Suppen)):
    Suppen_de[Suppen[x]] = Suppenlist_de[x]


Hauptspeisenteilestr = ""

for thing in Hauptspeisenteile:
    if thing == None:
        Hauptspeisenteilestr += "german; "
    elif thing.__contains__("/"):
        Hauptspeisenteilestr += thing.replace("/", ",") + "; "
    else:
        Hauptspeisenteilestr += thing + "; "

Hauptspeisenteilestr_de = translator.translate(Hauptspeisenteilestr, src="fr", dest="de").text
Hauptspeisenteilelist_de = Hauptspeisenteilestr_de.split(";")
Hauptspeisenteilelist_de.pop()

for x in range(len(Hauptspeisenteile)):
    # print(x)
    if Hauptspeisenteilelist_de[x] == "vertaalen":
        Hauptspeisenteile_de[Hauptspeisenteile[x]] = "_______"
    else:
        Hauptspeisenteile_de[Hauptspeisenteile[x]] = Hauptspeisenteilelist_de[x]

Hauptspeisenteile_de[None] = "     "
Hauptspeisenteile_de.pop(None, 1)
    
#print(Suppen_de)
#print("\n")
#print(Hauptspeisenteile_de)

with open("dictionary_fr/suppen_deutsch.json", "r") as file:
    altersuppendict = json.loads(file.read())

for neuesuppe in Suppen_de:
    if neuesuppe in altersuppendict:
        continue
    else:
        altersuppendict[neuesuppe] = Suppen_de[neuesuppe]

with open("dictionary_fr/suppen_deutsch.json", "w") as file:
    file.write(json.dumps(altersuppendict))


with open("dictionary_fr/haupt_deutsch.json", "r") as file:
    alterhauptdict = json.loads(file.read())

for neuesteil in Hauptspeisenteile_de:
    if neuesteil in alterhauptdict:
        continue
    else:
        alterhauptdict[neuesteil] = Hauptspeisenteile_de[neuesteil]

alterhauptdict.pop("none", 1)
with open("dictionary_fr/haupt_deutsch.json", "w") as file:
    file.write(json.dumps(alterhauptdict))

"""Englisch"""


Suppen   = []
Suppen_en = {}
Hauptspeisenteile   = []
Hauptspeisenteile_en = {}

for day in originaledatei:
    Suppen.append(originaledatei[day][1])
    Hauptspeisenteile.append(originaledatei[day][2])
    Hauptspeisenteile.append(originaledatei[day][3])
    Hauptspeisenteile.append(originaledatei[day][4])

Suppenstr = ""

for thing in Suppen:
    Suppenstr += thing + ","

Suppenstr_en = translator.translate(Suppenstr, src="fr", dest="en").text
Suppenlist_en = Suppenstr_en.split(",")
Suppenlist_en.pop()


for x in range(len(Suppenlist_en)):
    Suppen_en[Suppen[x]] = Suppenlist_en[x]




Hauptspeisenteilestr = ""

for thing in Hauptspeisenteile:
    if thing == None:
        Hauptspeisenteilestr += "german; "
    elif thing.__contains__("/"):
        Hauptspeisenteilestr += thing.replace("/", ",") + "; "
    else:
        Hauptspeisenteilestr += thing + "; "

Hauptspeisenteilestr_en = translator.translate(Hauptspeisenteilestr, src="fr", dest="en").text
Hauptspeisenteilelist_en = Hauptspeisenteilestr_en.split(";")
Hauptspeisenteilelist_en.pop()

lenmin1 = len(Hauptspeisenteilelist_en) - 1
for x in range(len(Hauptspeisenteile)):
    # print(x)
    if Hauptspeisenteilelist_en[x] == "vertaalen":
        Hauptspeisenteile_en[Hauptspeisenteile[x]] = "_______"
    else:
        Hauptspeisenteile_en[Hauptspeisenteile[x]] = Hauptspeisenteilelist_en[x]

Hauptspeisenteile_en[None] = "     "
Hauptspeisenteile_en.pop(None, 1)
    
#print(Suppen_en)
#print("\n")
#print(Hauptspeisenteile_en)

with open("dictionary_fr/suppen_englisch.json", "r") as file:
    altersuppendict = json.loads(file.read())

for neuesuppe in Suppen_en:
    if neuesuppe in altersuppendict:
        continue
    else:
        altersuppendict[neuesuppe] = Suppen_en[neuesuppe]

with open("dictionary_fr/suppen_englisch.json", "w") as file:
    file.write(json.dumps(altersuppendict))


with open("dictionary_fr/haupt_englisch.json", "r") as file:
    alterhauptdict = json.loads(file.read())

for neuesteil in Hauptspeisenteile_en:
    if neuesteil in alterhauptdict:
        continue
    else:
        alterhauptdict[neuesteil] = Hauptspeisenteile_en[neuesteil]

with open("dictionary_fr/haupt_englisch.json", "w") as file:
    file.write(json.dumps(alterhauptdict))


exit("Erfolgreich")