import json
from deepl import deepl

# Gets the newest menue/output
with open("../outputs/output.json", "r", encoding="utf-16") as file:
    untranslatedfile = json.loads(file.read())

dayarray = [] # Array of the menue | was in a dict with date as key
indexdict = untranslatedfile # Dict with date as key, that gives the index of a specific Date in the datearray

# Function to sort the contect of datearray by date
def sorter(daylist):
    # Should come in as a String, bc Key of Dict = String
    date = daylist[-1].split(".")
    # Gives the year the most importance, then the month | day is least important
    # The factors are so high, bc otherwise day and month would be too big to be compensated by the higher importance parts
    return int(date[0]) + int(date[1])*100 + int(date[2])*10000

for index, day in enumerate(untranslatedfile):
    # Adds the date of the day as the last item
    daycontent = untranslatedfile[day]
    daycontent.append(day)
    # Puts the contents of the menue dict in the Array
    dayarray.append(daycontent)

# Sorts the dayarray with the function above
dayarray = sorted(dayarray, key=sorter)

# Replaces the menue of the day with the index in the datearray where the menue is stored
for index, day in enumerate(dayarray):
    # day[-1] is the date of the day, wich is stored in last position of contentlist
    # see line 20
    indexdict[day[-1]] = index


# Test of sorter
print(dayarray)
print(dayarray[indexdict['28.02.2023']])
