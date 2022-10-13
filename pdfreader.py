import pdfplumber

with pdfplumber.open("document_path.PDF") as temp:
  first_page = temp.pages[0]
  print(first_page.extract_text())
