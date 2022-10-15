import pandas as pd
import json
import os

allweeks = os.listdir("menues")
"""
a = allweeks[0]
b = allweeks[1]
c = allweeks[2]
d = allweeks[3]

allweeks = [d,c,b,a]
"""

os.remove("octobre.json")

f = open("octobre.json", "w")
f.write('{')
f.close()

i = 1
for file in allweeks:
    print(file)

    excel_data_df = pd.read_excel("menues/" + file)

    json_str = excel_data_df.to_json()

    jsondict = json_str

    f = open("zwischenspeicher.json", "w")
    f.write(json_str)
    f.close()

    f = open("zwischenspeicher.json", "r")
    jsondict = json.loads(f.read())
    f.close()

    f = open("octobre.json", "a")

    jsondict[f"Plat{i}"] = jsondict["Plat"]
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

    dictstring = json.dumps(jsondict)
    dictstring = dictstring[1:-1]
    if i != len(allweeks):
        dictstring += ","

    f.write(dictstring)
    f.close()
    i += 1

f = open("octobre.json", "a")
f.write("}")
f.close()


"""

Datum müsste man halt mal noch machen ka mit kalender oder so

names = [
"Semaine-40-03-octo-2022-07-octo-2022.xlsx",
"Semaine-41-10-octo-2022-14-octo-2022.xlsx",
"Semaine-42-17-octo-2022-21-octo-2022.xlsx",
"Semaine-43-24-octo-2022-28-octo-2022.xlsx"
]
for name in names:
    name = name[11:-10]
    name = [name[0:2], name[13:15]]
    name = [name[0], name[0]+1, name[1]-1, name[1]]
    print(name)
"""
