import os

with open("output.js", "w") as outputfile:
    with open("..//Auswerten-Python//octobre.json", "r") as outputjson:
        outputfile.write("const essensdict = " + outputjson.read())