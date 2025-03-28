# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

# HTML con formato inusual en las etiquetas
html_content = """
<html>
<head>
<TITLE >Profile: Dionysus</title  / >
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/dionysus.jpg" />
<h2>Name: Dionysus</h2>
<img src="/static/grapes.png"><br><br>
Hometown: Mount Olympus
<br><br>
Favorite animal: Leopard <br>
<br>
Favorite Color: Wine
</center>
</body>
</html>
"""

# Creamos un objeto BeautifulSoup a partir del HTML raw
soup = BeautifulSoup(html_content, "html.parser")
soup


# Observamos cómo BeautifulSoup normaliza las etiquetas
print("HTML parseado y normalizado por BeautifulSoup:")
print(soup.prettify())

# Buscamos la etiqueta title
title = soup.find("title")
print(title.string)

# Accedemos directamente a la etiqueta 'title' y mostramos su contenido
print("\nContenido de la etiqueta <title>:", soup.title.string)
