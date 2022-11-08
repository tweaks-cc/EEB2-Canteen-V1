import wikipediaapi
import json
from colorama import init, Fore, Back

init(autoreset=True)

wiki_wiki = wikipediaapi.Wikipedia('fr')

with open("../auswerten-python/dictionary_fr/haupt_deutsch.json") as file:
    haupt_deutsch = json.loads(file.read())

for seite in haupt_deutsch:
    print(seite, Fore.RED + str(wiki_wiki.page(seite).exists()))