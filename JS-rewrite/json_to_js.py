import json

# --Französisch--


# Liest den bereits vorhandenen Dict aus
with open("javascript/essensdict_fr.js", "r", encoding="UTF-16") as outputfile:
    alterdict = outputfile.read()

# Liest den neuen Dict, welcher frisch aus dem xlsx-Leser kommt, aus 
with open("..//auswerten-python//outputs//output.json", "r", encoding="UTF-16") as outputjson:
    neuerdict = json.loads(outputjson.read())

# Entfernt den Kommentar und das 'const =' aus dem String aus der JS Datei und wandelt ihn zum Dict um
alterdict = json.loads(alterdict[69:-1] + "}")

# Checkt ob der alte und der neue übereinstimmen
if alterdict != neuerdict:

    # Wenn sie nicht übereinstimmen wird über jedes objekt im neuen dict geloopt
    # Es wird jeweils gecheckt ob der Key/Tag schon vorhanden ist
    for tag in neuerdict:
        if tag in alterdict:
            # Wenn ja: wird gecheckt ob die Keys übereinstimmen
            # Wenn nicht dann wird der alte mit dem neuen ersetzt
            if  alterdict[tag] != neuerdict[tag]:
                alterdict[tag] =  neuerdict[tag]
            # Wenn ja passiert nix
        else:
            alterdict[tag] = neuerdict[tag]

    # Zum Schluss wird der aktualisierte Dict wieder in die .js gedrückt
    with open("javascript/essensdict_fr.js", "w", encoding="UTF-16") as outputfile:
        outputfile.write("// Ist halt der Dict mit all dem Essen\nconst importedessensdict_fr = ")
    with open("javascript/essensdict_fr.js", "a", encoding="UTF-16") as outputfile:
        outputfile.write(json.dumps(alterdict))


# --Deutsch--


# Liest den bereits vorhandenen Dict aus
with open("javascript/essensdict_de.js", "r", encoding="UTF-16") as outputfile:
    alterdict = outputfile.read()

# Liest den neuen Dict, welcher frisch aus dem xlsx-Leser kommt, aus 
with open("..//auswerten-python//outputs//output_de.json", "r", encoding="UTF-16") as outputjson:
    neuerdict = json.loads(outputjson.read())  

# Entfernt den Kommentar und das 'const =' aus dem String aus der JS Datei und wandelt ihn zum Dict um
alterdict = json.loads(alterdict[69:-1] + "}")

# Checkt ob der alte und der neue übereinstimmen
if alterdict != neuerdict:
        
    # Wenn sie nicht übereinstimmen wird über jedes objekt im neuen dict geloopt
    # Es wird jeweils gecheckt ob der Key/Tag schon vorhanden ist
    for tag in neuerdict:
        if tag in alterdict:
            # Wenn ja: wird gecheckt ob die Keys übereinstimmen
            # Wenn nicht dann wird der alte mit dem neuen ersetzt
            if  alterdict[tag] != neuerdict[tag]:
                alterdict[tag] =  neuerdict[tag]
            # Wenn ja passiert nix
        else:
            alterdict[tag] = neuerdict[tag]

    # Zum Schluss wird der aktualisierte Dict wieder in die .js gedrückt
    with open("javascript/essensdict_de.js", "w", encoding="UTF-16") as outputfile:
        outputfile.write("// Ist halt der Dict mit all dem Essen\nconst importedessensdict_de = ")
    with open("javascript/essensdict_de.js", "a", encoding="UTF-16") as outputfile:
        outputfile.write(json.dumps(alterdict))


# --Englisch--


# Liest den bereits vorhandenen Dict aus
with open("javascript/essensdict_en.js", "r", encoding="UTF-16") as outputfile:
    alterdict = outputfile.read()

# Liest den neuen Dict, welcher frisch aus dem xlsx-Leser kommt, aus 
with open("..//auswerten-python//outputs//output_en.json", "r", encoding="UTF-16") as outputjson:
    neuerdict = json.loads(outputjson.read())  

# Entfernt den Kommentar und das 'const =' aus dem String aus der JS Datei und wandelt ihn zum Dict um
alterdict = json.loads(alterdict[69:-1] + "}")

# Checkt ob der alte und der neue übereinstimmen
if alterdict != neuerdict:
        
    # Wenn sie nicht übereinstimmen wird über jedes objekt im neuen dict geloopt
    # Es wird jeweils gecheckt ob der Key/Tag schon vorhanden ist
    for tag in neuerdict:
        if tag in alterdict:
            # Wenn ja: wird gecheckt ob die Keys übereinstimmen
            # Wenn nicht dann wird der alte mit dem neuen ersetzt
            if  alterdict[tag] != neuerdict[tag]:
                alterdict[tag] =  neuerdict[tag]
            # Wenn ja passiert nix
        else:
            alterdict[tag] = neuerdict[tag]

    # Zum Schluss wird der aktualisierte Dict wieder in die .js gedrückt
    with open("javascript/essensdict_en.js", "w", encoding="UTF-16") as outputfile:
        outputfile.write("// Ist halt der Dict mit all dem Essen\nconst importedessensdict_en = ")
    with open("javascript/essensdict_en.js", "a", encoding="UTF-16") as outputfile:
        outputfile.write(json.dumps(alterdict))
