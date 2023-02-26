import json
from deepl import deepl

# Gets the newest menue/output
with open("../outputs/output.json", "r", encoding="utf-16") as file:
    untranslatedfile = json.loads(file.read())

dayarray = [] # Array of the menue | was in a dict with date as key
# Dict with date as key, that gives the index of a specific Date in the datearray
# Takes the old dict, so that the structure and dates are still there, and the index can just replace the content
indexdict = untranslatedfile

for day in untranslatedfile:
    # Adds the date of the day as the last item
    daycontent = untranslatedfile[day] # Gets the content/menue of the day
    daycontent.append(day) # Appends after the menue and weekday in pos 0 the date for correction ig
    # Puts the contents of the menue dict in the Array
    dayarray.append(daycontent)


# Function to sort the contect of datearray by date
def sorter(dateofday):
    # Should come in as a String, bc Key of Dict = String
    # Gets as pramater the date
    date = dateofday[-1].split(".")
    # Gives the year the most importance, then the month | day is least important
    # The factors are so high, bc otherwise day and month would be too big to be compensated by the higher importance parts
    return int(date[0]) + int(date[1])*100 + int(date[2])*10000

# Sorts the dayarray with the function above
dayarray = sorted(dayarray, key=sorter)

# Replaces the menue of the day with the index in the datearray where the menue is stored
for index, day in enumerate(dayarray):
    # day[-1] is the date of the day, wich is stored in last position of contentlist
    # see line 20
    indexdict[day[-1]] = index  # Value in the dict with key = date from this day --> is now the index of this day


# Creates another Array, so that the original one stays intact for the second translation
# --> 1. translation => german/DE
# --> 2. translation => english/EN
DEarray = []
# Goes trough every element/day in the original array and joins them with ¤ in between so it can be split again after
for day in dayarray:
    daystring = ""
    for thing in day:
        daystring += str(thing) + "¤"
    # Removes the ¤ at the end of the String
    daystring = daystring[0:-1]
    # Puts the joint contents in the new array
    DEarray.append(daystring)

# Second loop to join all the joint strings in the new array
DEstring = ""
for daystring in DEarray:
    DEstring += daystring + "§"
# Removes the last § from the string
DEstring = DEstring[0:-1]

# Translation using the DeeplCLI at https://github.com/eggplants/deepl-cli
translator = deepl.DeepLCLI("fr", "de")

translatedstr = translator.translate(DEstring)

# Here is the process for getting the string that was needed for it to be translated back to an array of arrays
DEtranslatedstringarray = translatedstr.split("§")  # First split to get an array of strings
# Second split to get an array of arrays
DEtranslatedarray = []
for daystring in DEtranslatedstringarray:
    dayarray = daystring.split("¤")
    # Removes the whitespaces that appear in the date | Don't know why, but better get them out
    dayarray[-1] = dayarray[-1].replace(" ", "")
    DEtranslatedarray.append(dayarray)  # Adds the array of the menue in the big array

# Prints the final translated array for debugging | can be removed
print(DEtranslatedarray)

# After here comes saved for later code and debugging stuffs
exit()

# Test | Should give the same result as the original array, except other language
# print(DEtranslatedarray[indexdict['28.02.2023']])
# print(dayarray[indexdict['28.02.2023']])

# Test of sorter
#print(dayarray)
# print(dayarray[indexdict['28.02.2023']])
