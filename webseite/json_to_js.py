import json
from colorama import init, Fore, Back

init(autoreset=True)

# Liest den bereits vorhandenen Dict aus
with open("javascript/essensdict_fr.js", "r") as outputfile:
    alterdict = outputfile.read()

# Liest den neuen Dict, welcher frisch aus dem xlsx-Leser kommt, aus 
with open("..//auswerten-python//outputs//output.json", "r", encoding="utf-8") as outputjson:
    neuerdict = json.loads(outputjson.read())  

# Entfernt den Kommentar und das 'const =' aus dem String aus der JS Datei und wandelt ihn zum Dict um
alterdict = json.loads(alterdict[66:-1] + "}")

print(Fore.MAGENTA + str(alterdict))

if alterdict == neuerdict:
    exit("Alles gleich")

for tag in neuerdict:
    if tag in alterdict:
        print("is in", end=" ")
        if neuerdict[tag] != alterdict[tag]:
            alterdict[tag] = neuerdict[tag]
            print("buts its not the same")
        else:
            print("")
    else:
        print("it isnt?")
        alterdict[tag] = neuerdict[tag]

print(Fore.GREEN + str(alterdict))

with open("")

exit("STOOOP")

for tag in alterdict:
    for thing in alterdict[tag]:
        # print(thing)
        if thing == None: continue
        if thing.__contains__("é"):
            print(Fore.CYAN + thing)
    continue

print("")

for tag in neuerdict:
    for thing in neuerdict[tag]:
        print(thing)
        if thing == None: continue
        if thing.__contains__("\u00e9"):
            print(Fore.RED + thing)
    continue

    alterstring: str = str(alterdict[tag])
    print(alterstring)
    neuerstring: str = str(neuerdict[tag])
    print(neuerstring)
    if alterstring == neuerstring:
        print("True")
    else:
        print("False")
    
    # print(alterdict[thing], neuerdict[thing])

if alterdict == neuerdict:
    print("Alles gleich")
    exit()

exit()

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