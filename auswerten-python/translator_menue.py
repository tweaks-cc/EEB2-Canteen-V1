# Nimmt sich das derzeitige Menü und übersetzt es

import json

with open("outputs/output.json", "r") as file:
    originalerdict = json.loads(file.read())

# Alle Übersetzungsdateien für Deutsch
with open("dictionary_fr/haupt_deutsch.json",      "r") as file: haupt_de     = json.loads(file.read())
with open("dictionary_fr/suppen_deutsch.json",     "r") as file: suppen_de    = json.loads(file.read())
with open("dictionary_fr/nachtisch_deutsch.json",  "r") as file: nachtisch_de = json.loads(file.read())
with open("dictionary_fr/misc_deutsch.json",       "r") as file: misc_de      = json.loads(file.read())
haupt_de[None] = "      "
del haupt_de["null"]

# Alle Übersetzungsdateien für Englisch
with open("dictionary_fr/haupt_englisch.json",     "r") as file: haupt_en     = json.loads(file.read())
with open("dictionary_fr/suppen_englisch.json",    "r") as file: suppen_en    = json.loads(file.read())
with open("dictionary_fr/nachtisch_englisch.json", "r") as file: nachtisch_en = json.loads(file.read())
with open("dictionary_fr/misc_englisch.json",      "r") as file: misc_en      = json.loads(file.read())
haupt_en[None] = "      "
del haupt_en["null"]

neuerdict_de= originalerdict

for tag in neuerdict_de:
    templist = []
    i = 0
    for thing in neuerdict_de[tag]:
        if   i == 0:
            templist.append(misc_de[thing])
        elif i == 1:
            templist.append(suppen_de[thing])
        elif i == 5:
            templist.append(nachtisch_de[thing])
        else:
            templist.append(haupt_de[thing])
        i += 1
    neuerdict_de[tag] = templist


with open("outputs/output_de.json", "w")as file:
    file.write(json.dumps(neuerdict_de))


with open("outputs/output.json", "r") as file:
    originalerdict = json.loads(file.read())

neuerdict_en = originalerdict

for tag in neuerdict_en:
    templist = []
    i = 0
    for thing in neuerdict_en[tag]:
        if   i == 0:
            templist.append(misc_en[thing])
        elif i == 1:
            templist.append(suppen_en[thing])
        elif i == 5:
            templist.append(nachtisch_en[thing])
        else:
            templist.append(haupt_en[thing])
        i += 1
    neuerdict_en[tag] = templist

with open("outputs/output_en.json", "w")as file:
    file.write(json.dumps(neuerdict_en))

exit("All done ;)")