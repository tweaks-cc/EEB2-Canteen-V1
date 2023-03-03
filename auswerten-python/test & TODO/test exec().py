import os
vardec = "myvar = 'Hello world'"
varchange = "myvar = 'oh my god!!!'"
exec(vardec)
exec(varchange)
print(myvar)

with open("toread.txt") as file:
    readexec = file.read()

exec(readexec)
print(readvar)
print(readvar[1])

# Kann benutzt werden um das alte JS Menü als var einzulesen und zu benutzen
# Muss so, da länge ja dynamisch, mit Index geht also nicht