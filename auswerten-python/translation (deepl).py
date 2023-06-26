import json
from deepl import deepl

# Gets the newest menu/output
with open("outputs/output.json", "r", encoding="utf-16") as file:
    untranslatedFile = json.loads(file.read())

dayArray = [] # Array of the menu | was in a dict with date as key
# Dict with date as key, that gives the index of a specific Date in the datearray
# Takes the old dict, so that the structure and dates are still there, and the index can just replace the content
indexDict = untranslatedFile

for day in untranslatedFile:
    # Adds the date of the day as the last item
    dayContent = untranslatedFile[day] # Gets the content/menu of the day
    dayContent.append(day) # Appends after the menu and weekday in pos 0 the date for correction ig
    # Puts the contents of the menu dict in the Array
    dayArray.append(dayContent)


# Function to sort the contect of datearray by date
def sorter(dateOfDay):
    # Should come in as a String, bc Key of Dict = String
    # Gets as pramater the date
    date = dateOfDay[-1].split(".")
    # Gives the year the most importance, then the month | day is least important
    # The factors are so high, bc otherwise day and month would be too big to be compensated by the higher importance parts
    return int(date[0]) + int(date[1])*100 + int(date[2])*10000

# Sorts the dayArray with the function above
dayArray = sorted(dayArray, key=sorter)

savedArray = dayArray

# Replaces the menu of the day with the index in the datearray where the menu is stored
for index, day in enumerate(dayArray):
    # day[-1] is the date of the day, wich is stored in last position of contentlist
    # see line 20
    indexDict[day[-1]] = index  # Value in the dict with key = date from this day --> is now the index of this day


# Creates another Array, so that the original one stays intact for the second translation
# --> 1. translation => german/DE
# --> 2. translation => english/EN
deArray = []
# Goes trough every element/day in the original array and joins them with ¤ in between so it can be split again after
for day in dayArray:
    dayString = ""
    for thing in day:
        dayString += str(thing) + "¤"
    # Removes the ¤ at the end of the String
    dayString = dayString[0:-1]
    # Puts the joint contents in the new array
    deArray.append(dayString)

# Second loop to join all the joint strings in the new array
deString = ""
for dayString in deArray:
    deString += dayString + "§"
# Removes the last § from the string
deString = deString[0:-1]

# Translation using the DeeplCLI at https://github.com/eggplants/deepl-cli
translator = deepl.DeepLCLI("fr", "de")

try: translatedStr = translator.translate(deString)
except TimeoutError: exit("TimeoutError. Please repeat execution")

# Here is the process for getting the string that was needed for it to be translated back to an array of arrays
deTranslatedStringArray = translatedStr.split("§")  # First split to get an array of strings
# Second split to get an array of arrays
deTranslatedArray = []
for dayString in deTranslatedStringArray:
    dayTransArray = dayString.split("¤")
    # Removes the whitespaces that appear in the date | Don't know why, but better get them out
    dayTransArray[-1] = dayTransArray[-1].replace(" ", "")
    deTranslatedArray.append(dayTransArray)  # Adds the array of the menu in the big array

for index1, dayArr in enumerate(deTranslatedArray):
    for index2, dayPart in enumerate(dayArr):
        if dayPart == "Prüfungsmenü" or dayPart == "Menüprüfung": deTranslatedArray[index1][index2] = "Examensmenü"

# Prints the final translated array for debugging | can be removed
# for day in deTranslatedArray: print(day)
# print("\n")

# Reads the menu from the file and makes it into a real var that can be interacted with
# Name of the var won't be seen as valid, as it technically doesn't exist

with open("../JS-rewrite/menus/menu_de.js", encoding="UTF-16") as menuDeJS:
    DEtext = menuDeJS.read()
    # CharIndex 137 is the beginning of where we can put the data
    exec(DEtext[4:]) # Removes first 4 chars of string

# Here the new menu is inserted into the JS-file
# --Notes--
# importedEssensDictDE = ["Index 0 = Info |-| Index 1 = Date-Index-Dict |-| Index 2 = Menu-Array", "", ""]
# CharIndex 137 is the beginning of where we can put the data
# Vars to be inserted:
# deTranslatedArray is the array of the menu
# indexDict should be the dict for the Date-Index relation
# Text to be inserted should be something like this:
#    Has to be a formattable string for easy insertion of data
# importedEssensDictDE[1]  = {indexDict} \n
# importedEssensDictDe[2]  = {deTranslatedDe}
# For writing file[137:] to replace all text from 137 is the best, because old things don't need to be remembered | already got checked by the read

# Actual Code
arrayStructure = 'var importedEssensDictDE = ["Index 0 = Info |-| Index 1 = Date-Index-Dict |-| Index 2 = Menu-Array", "", ""]'
with open("../JS-rewrite/menus/menu_de.js", "w", encoding="UTF-16") as menuJsDe:
    newContent = f"{arrayStructure}\nimportedEssensDictDE[1]  = {indexDict}\nimportedEssensDictDE[2]  = {deTranslatedArray}"
    menuJsDe.write(newContent)

# ---Englisch translation

enArray = []


# Goes trough every element/day in the original array and joins them with ¤ in between so it can be split again after
for day in savedArray:
    dayString = ""
    for thing in day:
        dayString += str(thing) + "¤"
    # Removes the ¤ at the end of the String
    dayString = dayString[0:-1]
    # Puts the joint contents in the new array
    enArray.append(dayString)

# Second loop to join all the joint strings in the new array
enString = ""
for dayString in enArray:
    enString += dayString + "§"
# Removes the last § from the string
enString = enString[0:-1]

# Translation using the DeeplCLI at https://github.com/eggplants/deepl-cli
translator = deepl.DeepLCLI("fr", "en")

try: translatedStr = translator.translate(enString)
except TimeoutError: exit("TimeoutError. Please repeat execution")

# Here is the process for getting the string that was needed for it to be translated back to an array of arrays
enTranslatedStringArray = translatedStr.split("§")  # First split to get an array of strings
# Second split to get an array of arrays
enTranslatedArray = []
for dayString in enTranslatedStringArray:
    dayArray = dayString.split("¤")
    # Removes the whitespaces that appear in the date | Don't know why, but better get them out
    dayArray[-1] = dayArray[-1].replace(" ", "")
    enTranslatedArray.append(dayArray)  # Adds the array of the menu in the big array


for index1, dayArr in enumerate(enTranslatedArray):
    for index2, dayPart in enumerate(dayArr):
        if dayPart == "Prüfungsmenü" or dayPart == "Menüprüfung": enTranslatedArray[index1][index2] = "Exammenu"

# Reads the menu from the file and makes it into a real var that can be interacted with
# Name of the var won't be seen as valid, as it technically doesn't exist

with open("../JS-rewrite/menus/menu_en.js", encoding="UTF-16") as menuENJS:
    ENtext = menuENJS.read()
    # CharIndex 137 is the beginning of where we can put the data
    exec(ENtext[4:])

# Here the new menu is inserted into the JS-file
# --Notes--
# importedEssensDictDE = ["Index 0 = Info |-| Index 1 = Date-Index-Dict |-| Index 2 = Menu-Array", "", ""]
# CharIndex 137 is the beginning of where we can put the data
# Vars to be inserted:
# deTranslatedArray is the array of the menu
# indexDict should be the dict for the Date-Index relation
# Text to be inserted should be something like this:
#    Has to be a formattable string for easy insertion of data
# importedEssensDictDE[1]  = {indexDict} \n
# importedEssensDictDE[2]  = {deTranslatedDE}
# For writing file[137:] to replace all text from 137 is the best, because old things don't need to be remembered | already got checked by the read

# Actual Code
arrayStructure = 'var importedEssensDictEN = ["Index 0 = Info |-| Index 1 = Date-Index-Dict |-| Index 2 = Menu-Array", "", ""]'
with open("../JS-rewrite/menus/menu_en.js", "w", encoding="UTF-16") as menuJsEN:
    newContent = f"{arrayStructure}\nimportedEssensDictEN[1]  = {indexDict}\nimportedEssensDictEN[2]  = {enTranslatedArray}"
    menuJsEN.write(newContent)
