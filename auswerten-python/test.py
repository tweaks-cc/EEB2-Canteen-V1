import os
vardec = "myvar = 'Hello world'"
varchange = "myvar = 'oh my god!!!'"
exec(vardec)
exec(varchange)
print(myvar)

# Kann benutzt werden um das alte JS Menü als var einzulesen und zu benutzen
# Muss so, da länge ja dynamisch, mit Index geht also nicht