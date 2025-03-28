# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

# HTML de ejemplo
html_content = """
<html>
<head>
<title>Página de Ejemplo</title>
</head>
<body>
<h1 class="titulo">Bienvenidos</h1>
<p class="intro">Este es un párrafo introductorio.</p>
<p class="content">Contenido principal del texto.</p>
<a href="https://example.com" id="link1">Visita nuestro sitio</a>
<a href="https://another-example.com" id="link2" class="external">Otro enlace</a>
</body>
</html>
"""

# Creamos un objeto BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# 1. soup.prettify() - Muestra el contenido HTML con indentación, más legible
print(soup.prettify())

# 2. soup.find("tag") - Busca el primer elemento de una etiqueta específica
element = soup.find("h1dsd")
print("\nPrimer <h1> encontrado:", element)

# 3. soup.find_all("tag") - Encuentra todos los elementos de una etiqueta específica y devuelve una lista
all_paragraphs = soup.find_all("p")
print("\nTodos los <p> encontrados:", all_paragraphs)

# 4. soup.find("tag", class_="class_name") - Buscar una etiqueta específica con un atributo de clase
intro_paragraph = soup.find("p", class_="content")
intro_paragraph_con_css_selector = soup.select("p.content")[0]
print("\nPrimer <p> con clase 'content':", intro_paragraph)

# 5. soup.select("css_selector") - Seleccionar elementos usando selectores CSS
links_with_class = soup.select("a.external")  # Selecciona elementos <a> con clase "external"
print("\nEnlaces con clase 'external':", links_with_class)

# 6. element.text o element.get_text() - Extraer el texto de un elemento específico
print("\nTexto del primer <h1>:", element.get_text())

# 7. element["attribute"] - Obtener el valor de un atributo específico de un elemento
link_url = soup.find("a")["href"]
print("\nURL del primer enlace <a>:", link_url)

# 8. soup.get_text() - Extraer todo el texto de la página, sin etiquetas HTML
full_text = soup.get_text()
print("\nTexto completo del documento:", full_text)

# 9. element.find_next_sibling() - Encontrar el siguiente elemento en el mismo nivel
first_link = soup.find("a", id="link1")
next_link = first_link.find_next_sibling("a")  # Encuentra el siguiente <a>
print("\nSiguiente enlace después de link1:", next_link)

# 10. element.find_parent() - Encontrar el elemento padre de un elemento específico
parent_of_paragraph = intro_paragraph.find_parent()
print("\nElemento padre del párrafo con clase 'intro':", parent_of_paragraph)


## Ejercicio 1: Programa que saque el HTML completo de una URL
# URL: http://olympus.realpython.org/profiles
# Instrucciones:
# - Imprimir una lista de todos los enlaces buscando las etiquetas <a>,
# - Recuperar el valor de cada atributo 'href' y mostrarlo como una lista.


## Ejercicio 2: Books to Scrape
# Dada la URL: url = "http://books.toscrape.com/"
# 2.1: Extraer Título y Precio de Cada Libro en la Página Principal
# 2.2: Obtener Calificación y Disponibilidad de Cada Libro
# 2.3: Guardar Información en un DataFrame
# 2.4: Acceder a las Categorías y Contar los Libros
# 2.5: Extraer Datos de Todas las Páginas de una Categoría