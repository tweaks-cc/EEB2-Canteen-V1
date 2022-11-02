import json
from googletrans import Translator
translator = Translator()

with open("outputs/output.json", "r") as file:
    originaledatei = file.read()
    originaledatei = json.loads(originaledatei)
    print(type(originaledatei))


print(type(originaledatei["vier.zehn"]))

i = 0
for tag in originaledatei:
    print(tag)
    for index in range(5):
        teil = originaledatei[tag][index + 1]
        # print(teil)
        if teil == None:
            continue
        originaledatei[tag][index + 1] = translator.translate(teil, src="fr", dest="de").text
    i += 1
    if i == 3:
        break
        exit()

print(originaledatei)
exit()


for tag in originaledatei:
    print("tag: ", tag)
    for teil in tag:
        print("teil: ", teil)
        translations = translator.translate(teil, src="fr", dest="de") 
        print(translations.origin, ' -> ', translations.text)




"""
for teil in ['Lundi', 'Minestrone', 'Poelee de poulet aux legumes', 'Cœur de blé', 'Fruit']:
    translations = translator.translate(teil, dest='de') 
    print(translations.origin, ' -> ', translations.text)

print("----------------")

for teil in ['Lundi', 'Minestrone', 'Poelee de poulet aux legumes', 'Cœur de blé', 'Fruit']:
    translations = translator.translate(teil, dest='en') 
    print(translations.origin, ' -> ', translations.text)
"""