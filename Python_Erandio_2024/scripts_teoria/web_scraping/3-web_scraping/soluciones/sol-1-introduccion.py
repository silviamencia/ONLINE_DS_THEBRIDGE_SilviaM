# -*- coding: utf-8 -*-

# EJERCICIO 1
from urllib.request import urlopen

# URL del perfil
url = "http://olympus.realpython.org/profiles/dionysus"

try:
    # Abre la URL y lee el contenido HTML
    page = urlopen(url)
    html = page.read().decode("utf-8")
    
    center_index = html.find("<center>") + len("<center>")
    cender_close_index = html.find("</center>")
    
    center_content = html[center_index:cender_close_index]

    # Muestra el HTML completo por pantalla
    print(html)
    
    # Muestra por pantalla solo el contenido de la etiqueta center
    print(center_content)

except Exception as e:
    print("No se pudo acceder a la página:", e)


# EJERCICIO 2
import re
import pandas as pd
from urllib.request import urlopen

# URLs de los perfiles
urls = [
    "http://olympus.realpython.org/profiles/dionysus",
    "http://olympus.realpython.org/profiles/poseidon",
    "http://olympus.realpython.org/profiles/apollo"
]

# Lista para almacenar los datos extraídos
data = []

# Expresiones regulares para extraer la información
patterns = {
    "Title": r"<title.*?>(.*?)</title.*?>",
    "Name": r"Name:\s*([A-Za-z]+)",
    "Favorite animal": r"Favorite animal:\s*([A-Za-z]+)",
    "Favorite color": r"Favorite color:\s*([A-Za-z]+)",
    "Hometown": r"Hometown:\s*([A-Za-z]+)"
}

# Iteramos sobre cada URL para extraer la información
for url in urls:
    try:
        # Abre la URL y lee el contenido HTML
        page = urlopen(url)
        html = page.read().decode("utf-8")
        
        # Diccionario para almacenar los datos de cada perfil
        profile_data = {}

        # Extrae la información usando expresiones regulares
        for key, pattern in patterns.items():
            match = re.search(pattern, html, re.IGNORECASE)

            if match:
                profile_data[key] = match.group(1)
            else:
                profile_data[key] = None

        # Añade los datos al listado
        data.append(profile_data)

    except Exception as e:
        print(f"No se pudo acceder a la página {url}: {e}")

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv("perfiles.csv", index=False)

# Mostrar el DataFrame
print("\nDatos de perfiles extraídos:")
print(df)
