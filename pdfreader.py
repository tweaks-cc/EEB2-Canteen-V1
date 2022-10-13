import pdfplumber

with pdfplumber.open("menues/menu.pdf") as temp:
  first_page = temp.pages[0]
  print(first_page.extract_text())
