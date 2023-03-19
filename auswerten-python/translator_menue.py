# Nimmt sich das derzeitige Menü und übersetzt es

import json

# Liest als erstes den originalen Dict aus (Original ist auf Französisch)
with open("outputs/output.json", "r", encoding="utf-16") as file:
    originalerdict = json.loads(file.read())

# Alle Übersetzungsdateien für Deutsch
with open("dictionary_fr/haupt_deutsch.json",      "r", encoding="utf-16") as file: haupt_de     = json.loads(file.read())
with open("dictionary_fr/suppen_deutsch.json",     "r", encoding="utf-16") as file: suppen_de    = json.loads(file.read())
with open("dictionary_fr/nachtisch_deutsch.json",  "r", encoding="utf-16") as file: nachtisch_de = json.loads(file.read())
with open("dictionary_fr/misc_deutsch.json",       "r", encoding="utf-16") as file: misc_de      = json.loads(file.read())
# Ändert null (JS) zu None (Python)
haupt_de[None]     = None
suppen_de[None]    = None
nachtisch_de[None] = None

# Alle Übersetzungsdateien für Englisch
with open("dictionary_fr/haupt_englisch.json",     "r", encoding="utf-16") as file: haupt_en     = json.loads(file.read())
with open("dictionary_fr/suppen_englisch.json",    "r", encoding="utf-16") as file: suppen_en    = json.loads(file.read())
with open("dictionary_fr/nachtisch_englisch.json", "r", encoding="utf-16") as file: nachtisch_en = json.loads(file.read())
with open("dictionary_fr/misc_englisch.json",      "r", encoding="utf-16") as file: misc_en      = json.loads(file.read())
# Ändert null (JS) zu None (Python)
haupt_en[None]     = None
suppen_en[None]    = None
nachtisch_en[None] = None

#--Deutsch--

# Originaler Dict wird eingelesen
neuerdict_de = originalerdict

# Geht durch alle Tage des Menüs
for tag in neuerdict_de:
    # Temporäre Liste der übersetzten Teile des Essens
    templist = []
    i = 0
    for thing in neuerdict_de[tag]:
        # Wenn index = 0 (aka. Datum) nimmt er die Datumsübersetzungen
        if   i == 0:
            templist.append(misc_de[thing])
        # Wenn index = 1 (aka. Suppe) nimmt er die Suppenübersetzungen
        elif i == 1:
            templist.append(suppen_de[thing])
        # Wenn index = 5 (aka. Nachtisch) nimmt er die Nachtischübersetzungen
        elif i == 5:
            templist.append(nachtisch_de[thing])
        # Ansonsten (aka. Hauptgangteile) nimmt er die Hauptgangübersetzungen
        else:
            if thing == "jour férié":
                thing = "Feiertag"
            templist.append(haupt_de[thing])

            #print(thing)
        i += 1
    # Dann ersetzt die Liste der übersetzten Dinge die ursprüngliche (französische) Liste 
    neuerdict_de[tag] = templist


# Als letztes wird das neue Menü (übersetzt) in die JSON gepackt
with open("outputs/output_de.json", "w")as file:
    file.write(json.dumps(neuerdict_de))


#--Englisch--

# Originaler Dict wird eingelesen
with open("outputs/output.json", "r", encoding="utf-16") as file:
    originalerdict = json.loads(file.read())

neuerdict_en = originalerdict

# Geht durch alle Tage des Menüs
for tag in neuerdict_en:
    # Temporäre Liste der übersetzten Teile des Essens
    templist = []
    i = 0
    for thing in neuerdict_en[tag]:
        # Wenn index = 0 (aka. Datum) nimmt er die Datumsübersetzungen
        if   i == 0:
            templist.append(misc_en[thing])
        # Wenn index = 1 (aka. Suppe) nimmt er die Suppenübersetzungen
        elif i == 1:
            templist.append(suppen_en[thing])
        # Wenn index = 5 (aka. Nachtisch) nimmt er die Nachtischübersetzungen
        elif i == 5:
            templist.append(nachtisch_en[thing])
        # Ansonsten (aka. Hauptgangteile) nimmt er die Hauptgangübersetzungen
        else:
            if thing == "jour férié":
                thing = "Holiday"
            templist.append(haupt_en[thing])
            #print(thing)
        i += 1
    # Dann ersetzt die Liste der übersetzten Dinge die ursprüngliche (französische) Liste 
    neuerdict_en[tag] = templist

# Als letztes wird das neue Menü (übersetzt) in die JSON gepackt
with open("outputs/output_en.json", "w")as file:
    file.write(json.dumps(neuerdict_en))

# xD
exit("All done ;)")