# -*- coding: utf-8 -*-

# Instalación: pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Crear un objeto BeautifulSoup para la web que queremos scrapear

# Podemos acceder a la URL para ver cómo es la estructura HTML de la web
url = "http://olympus.realpython.org/profiles/dionysus"
# Abrimos la URL
page = urlopen(url)
# Leemos y decodificamos el contenido HTML
html = page.read().decode("utf-8")

# Creamos el objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, "html.parser")
soup  # Este objeto representa toda la estructura de la página HTML

## Nota:
# Puede que el objeto `soup` no aparezca en el explorador de variables.
# Para visualizarlo en Spyder: Esquina superior derecha -> Desmarcar "Excluir objetos llamables y módulos".


##### Utilizando el objeto BeautifulSoup creado ####

# Podemos extraer todo el texto de la página eliminando las etiquetas HTML
print(soup.get_text())

# Eliminar las líneas en blanco puede hacer el texto más legible
noblanklines = soup.get_text().replace("\n", "")
print(noblanklines)

# Mejor aún, utilizamos expresiones regulares para reemplazar los saltos de línea
import re
# Usamos re.sub para reemplazar múltiples saltos de línea por un solo salto de línea
cleaned_text = re.sub(r"\n{2,}", "\n", soup.get_text()).strip()
print(cleaned_text)


# También podemos realizar búsquedas en el texto
findtext = soup.get_text().find('Wine')
print(findtext)  # Devuelve la posición de la primera ocurrencia


# Si necesitamos mantener las etiquetas HTML para buscar elementos específicos, como imágenes, podemos hacerlo:
images = soup.find_all("img")
print(images)  # Devuelve una lista con todas las etiquetas <img> en la página


# Extraer el contenido de cada imagen y almacenarlo en variables
image1, image2 = images[0], images[1]
print("Etiqueta HTML de la primera imagen:", image1)
print("Etiqueta HTML de la segunda imagen:", image2)

# Tipo de etiqueta HTML de cada imagen
print("Etiqueta de image1:", image1.name)
print("Etiqueta de image2:", image2.name)

# Acceso a atributos HTML de las etiquetas
# Podemos acceder a atributos como si fueran diccionarios
print("Fuente de la primera imagen:", image1["src"])
print("Fuente de la segunda imagen:", image2["src"])


# Extraer el título de la página usando la etiqueta <title>
print("Etiqueta HTML del título:", soup.title)  # Incluye la etiqueta <title>
print("Texto dentro de la etiqueta título:", soup.title.string)  # Solo el texto de la etiqueta


# Realizar búsquedas avanzadas para localizar atributos concretos en etiquetas
# Por ejemplo, encontrar todas las etiquetas <img> con un atributo src específico
result = soup.find_all("img", src="/static/dionysus.jpg")
print("Imagen específica encontrada:", result)


"""
Esta herramienta es útil cuando queremos scrapear partes específicas de una 
página o ciertos elementos contenidos en etiquetas. 

Si dedicamos un tiempo a examinar el documento HTML de un sitio web, es más 
fácil identificar etiquetas con atributos únicos que podemos usar para extraer 
datos específicos de manera precisa.
"""