exdate1 = '28.11.2022'
exdate2 = '29.11.2022'
exdate3 = '01.12.2022'
exdate4 = '01.01.2023'
ex1 = '31.12.2022'
ex2 = '01.01.2023'

def sorter(date):
    # Should come in as a String, bc Key of Dict = String
    date = date.split(".")
    # Gives the year the most importance, then the month | day is least important
    # The factors are so high, bc otherwise day and month would be too big to be compensated
    return int(date[0]) + int(date[1])*100 + int(date[2])*10000

# Should all be true
print(sorter(exdate1) < sorter(exdate2))
print(sorter(exdate2) < sorter(exdate3))
print(sorter(exdate3) < sorter(exdate4))
print(sorter(ex1) < sorter(ex2))

datearr = ["12.12.2022", "02.03.2023", '28.11.2022', "24.11.2022", "06.05.2023"]

print(sorted(datearr, key=sorter))
