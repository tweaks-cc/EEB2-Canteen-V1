import json
from deepl import deepl

# Gets the newest menue/output
with open("../outputs/output.json", "r", encoding="utf-16") as file:
    untranslatedFile = json.loads(file.read())

dayArray = [] # Array of the menue | was in a dict with date as key
# Dict with date as key, that gives the index of a specific Date in the datearray
# Takes the old dict, so that the structure and dates are still there, and the index can just replace the content
indexDict = untranslatedFile

for day in untranslatedFile:
    # Adds the date of the day as the last item
    dayContent = untranslatedFile[day] # Gets the content/menue of the day
    dayContent.append(day) # Appends after the menue and weekday in pos 0 the date for correction ig
    # Puts the contents of the menue dict in the Array
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

# Replaces the menue of the day with the index in the datearray where the menue is stored
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
    deTranslatedArray.append(dayTransArray)  # Adds the array of the menue in the big array

# Prints the final translated array for debugging | can be removed
print(deTranslatedArray, "\n")

# ---Englisch translation

enArray = []


# Goes trough every element/day in the original array and joins them with ¤ in between so it can be split again after
for day in dayArray:
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
    enTranslatedArray.append(dayArray)  # Adds the array of the menue in the big array

# Prints the final translated array for debugging | can be removed
print(enTranslatedArray)


# After here comes saved for later code and debugging stuffs
exit()

# Test | Should give the same result as the original array, except other language
# print(deTranslatedArray[indexdict['28.02.2023']])
# print(dayArray[indexdict['28.02.2023']])

# Test of sorter
#print(dayArray)
# print(dayArray[indexdict['28.02.2023']])
