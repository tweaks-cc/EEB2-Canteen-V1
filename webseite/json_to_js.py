import json

# Liest den bereits vorhandenen Dict aus
with open("javascript/essensdict.js", "r") as outputfile:
    alterdict = outputfile.read()

# Liest den neuen Dict, welcher frisch aus dem xlsx-Leser kommt, aus 
with open("..//auswerten-python//output.json", "r") as outputjson:
    neuerdict = json.loads(outputjson.read())

# Entfernt den Kommentar und das 'const =' aus dem String aus der JS Datei und wandelt ihn zum Dict um
alterdict = json.loads(alterdict[66:-1] + "}")

# Liste der neuen Elemente/Tage, die sich nicht im alten Dict aus der JS befinden
neue_elemente = []

# Geht durch alle Elemente des neuen Dicts und guckt ob sie schon im alten vorhanden sind
for key in neuerdict:
    if key not in alterdict:
        # Wenn nicht vorhanden, added er den Key zur Liste
        neue_elemente.append(key)
    """
    else:
        # An sich nur für debuggen
        # Wenn vorhanden, printet er das
        print("fand", key)
    """

if len(neue_elemente) != 0:
    print("neue Elemente")
    # Geht durch die Liste der neuen Keys
    for newelement in neue_elemente:
        alterdict[newelement] = neuerdict[newelement]

    with open("javascript/essensdict.js", "w") as outputfile:
        outputfile.write("// Ist halt der Dict mit all dem Essen\nconst importedessensdict = ")
    with open("javascript/essensdict.js", "a") as outputfile:
        outputfile.write(json.dumps(alterdict))
else:
    print("Alles aktuell, oder neuer Dict aus dem xlsx leser veraltet")