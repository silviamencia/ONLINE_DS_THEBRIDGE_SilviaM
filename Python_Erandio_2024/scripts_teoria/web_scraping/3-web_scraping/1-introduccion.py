# -*- coding: utf-8 -*-

from urllib.request import urlopen

# Lo primero que vamos a hacer es abrir una pagina
# http://olympus.realpython.org/profiles/aphrodite

url = "http://olympus.realpython.org/profiles/aphrodite"

# Abre la página y devuelve un objeto de archivo
page = urlopen(url)


# Sacamos la estructura del HTML
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

# Procedemos a extraer diferentes partes
# Buscamos el titulo
title_index = html.find("<title>")
title_index

# Seleccionamos donde comienza el contenido del titulo
start_index = title_index + len("<title>")
start_index

# Y el final con la barra ("/")
end_index = html.find("</title>")
end_index


# Sacamos el titulo
title = html[start_index:end_index]
title


# Si intentos repetir lo mismo para Poseidon hay problemas
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

# Vemos que el titulo sale mal.

# Pasamos a ver la pagina
print(html)
# Vemos que despues del titulo aparece un espacio.

html.find("<title>")
# Cuando buscamos el titulo devuelve un -1 porque no existe.

# El principio es 6
start_index

# Tendríamos que adaptar para buscar en base a la estructura de esta página en concreto
html.find("<title >")

"""El carácter en el índice 6 de la cadena html es un carácter de nueva 
línea (\ n) justo antes del corchete de ángulo de apertura (<) de 
la etiqueta <head>. Esto significa que html [start_index: end_index] 
devuelve todo el HTML comenzando con esa nueva línea y terminando justo antes
de la etiqueta </title>."""

# Este tipo de cosas hay que evitarlas para lo que utilizamos expresiones regulares
# Importamos la libreria
import re

# --- Ejemplo 1: Patrón con el asterisco (*) ---
# El asterisco (*) representa "cero o más repeticiones" del carácter inmediatamente anterior.

# Ejemplo básico: buscamos "ab*c", donde:
# - "a" es obligatorio
# - "b" puede repetirse 0 o más veces
# - "c" es obligatorio
print(re.findall("ab*c", "ac"))  # ["ac"] -> "b" no está presente, pero es válido.
print(re.findall("ab*c", "abc"))  # ["abc"] -> "b" está presente una vez.
print(re.findall("ab*c", "abbc"))  # ["abbc"] -> "b" está presente varias veces.
print(re.findall("ab*c", "ac abc abbc abbbc"))  # ["ac", "abc", "abbc", "abbbc"] -> Coincidencias múltiples.

# No hay coincidencias porque el patrón exige "a" al principio y "c" al final
print(re.findall("ab*c", "bc"))  # [] -> Falta "a".
print(re.findall("ab*c", "abdc"))  # [] -> Hay una "d" que rompe el patrón.

# --- Ejemplo 2: Sensibilidad a mayúsculas ---
# Por defecto, la búsqueda diferencia entre mayúsculas y minúsculas.
print(re.findall("ab*c", "ABC"))  # [] -> No coincide porque "ABC" está en mayúsculas.

# Usando `re.IGNORECASE` para ignorar la sensibilidad a mayúsculas:
print(re.findall("ab*c", "ABC", re.IGNORECASE))  # ["ABC"] -> Coincide aunque esté en mayúsculas.

# --- Ejemplo 3: Patrón con el punto (.) y el asterisco (*) ---
# El punto (.) representa "cualquier carácter", y el asterisco (*) indica "cero o más repeticiones".

# Patrón: "a.*c"
# - "a" es obligatorio
# - ".*" significa "cualquier carácter, repetido 0 o más veces"
# - "c" es obligatorio
print(re.findall("a.*c", "abc"))  # ["abc"] -> Coincide con todo el texto.
print(re.findall("a.*c", "abbc"))  # ["abbc"] -> Coincide desde "a" hasta "c".
print(re.findall("a.*c", "ac"))  # ["ac"] -> Coincide con "a" seguido directamente de "c".
print(re.findall("a.*c", "acc"))  # ["acc"] -> Coincide con "a" seguido de cualquier número de caracteres antes de "c".

# Casos donde no hay coincidencias:
print(re.findall("a.*c", "ab"))  # [] -> Falta "c".
print(re.findall("a.*c", "bc"))  # [] -> Falta "a".

# --- Ejemplo 4: Variaciones de ".*" ---
# El patrón "a.*c" captura la subcadena más larga que empieza con "a" y termina con "c".
print(re.findall("a.*c", "abcac"))  # ["abcac"] -> Captura toda la cadena desde el primer "a" hasta el último "c".
print(re.findall("a.*?c", "abcac"))  # ["abc", "ac"] -> Captura las coincidencias más cortas debido al operador `?`.

# --- Resumen de uso ---
# - `*` -> Cero o más repeticiones del carácter anterior.
# - `.` -> Cualquier carácter excepto el salto de línea.
# - `.*` -> Cualquier secuencia de caracteres.
# - `.*?` -> Cualquier secuencia de caracteres más corta posible (no codiciosa).
# - `re.IGNORECASE` -> Ignorar la sensibilidad a mayúsculas/minúsculas.

# A menudo, usa re.search() para buscar un patrón particular dentro de una cadena. 
# Esta función devuelve un objeto llamado MatchObject que almacena información
# sobre la **primera coincidencia encontrada**.
# Esto es diferente a re.findall(), que devuelve **todas las coincidencias** como una lista.

# Cadena de ejemplo
text = "abbbc abc ac adc"

# Buscar la primera coincidencia
match = re.search("ab*c", text)
if match:
    print("Resultado de re.search():", match.group())  # "abbbc"

# Buscar todas las coincidencias
matches = re.findall("ab*c", text)
print("Resultados de re.findall():", matches)  # ['abbbc', 'abc', 'ac']

# re.sub () permite reemplazar texto en una cadena que coincide con una 
# expresión regular con texto nuevo.
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
string

# En este caso solo cambia el string que mas se le parezca.
# Vemos que ocurre cambiando la palabra.
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "tac", string)
string

# Si queremos cambiar todas añadismos la interrogacion.
# Esto provoca que no busque el macheo
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
string


# Una vez visto esto vamos a probar la siguiente pagina.
# http://olympus.realpython.org/profiles/dionysus

import re
from urllib.request import urlopen

# Cargamos la pagina.
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

print(html)

# Vemos que presenta el mismo problema.
# Lo solucionamos con lo visto
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()

# Visualizamos el titulo
print(title)

# Eliminamos los marcadores
title = re.sub("<.*?>", "", title)
# Visualizamos el titulo
print(title)


# ----------------------------------------------------------------------------

# EJERCICIO 1
# Escribe un programa que tome el HTML completo de la siguiente URL
# url = "http://olympus.realpython.org/profiles/dionysus"
# Recoge todos los datos en un objeto y muéstralo por pantalla


# EJERCICIO 2
# Crear un DataFrame con Perfiles Extraídos
# Escribe un programa que acceda a tres perfiles diferentes
# y extraiga datos como nombre, ocupación y ubicación de cada uno.
#
# Si la página no existe, muestra un mensaje por pantalla y no añadas nada.
# Usa expresiones regulares para capturar esta información y almacenarla en un DataFrame.
# 
# Al final, guarda el DataFrame en un archivo CSV.
#
# URLs:
# - http://olympus.realpython.org/profiles/dionysus
# - http://olympus.realpython.org/profiles/poseidon
# - http://olympus.realpython.org/profiles/apollo


