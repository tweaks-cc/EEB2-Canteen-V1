with open("main.html", "r") as html:
    htmlcontent = html.read()

htmlcontent = htmlcontent.replace("<!--to replace-->","<!--Hello from Python-->")
with open("main.html", "w") as html:
    html.write(htmlcontent)