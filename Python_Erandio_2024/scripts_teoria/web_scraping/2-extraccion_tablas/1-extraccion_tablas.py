# -*- coding: utf-8 -*-

# URL: https://en.wikipedia.org/wiki/Minnesota

# Instalar parsers para interpretar la estructura del HTML (pandas los utiliza por debajo)
# pip install html5lib lxml beautifulsoup4

import os

# Configurar el directorio de trabajo
# Esto asegura que los archivos se guarden en la misma ubicación que el script
# Nota: solo funciona si ejecutamos el script entero, si vamos línea a línea tendríamos que especificar la ruta
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Cargamos las librerías necesarias
import pandas as pd

# --- Importación y exploración de tablas en wikipedia ---

# Importamos todas las tablas de la web
table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')

# Mostramos el número de tablas detectadas
print(f'Total de tablas detectadas: {len(table_MN)}')

# Exploramos una de las tablas por índice
# Seleccionamos la tercera tabla y mostramos una vista previa
a = table_MN[2]
a.head()

# También podemos buscar una tabla específica por su contenido
# Aquí seleccionamos la tabla que contiene los resultados de elecciones en Minnesota
table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match='United States presidential election results for Minnesota')
print(f'Total de tablas coincidentes: {len(table_MN)}')

# Sacamos la tabla específica como un DataFrame
df = table_MN[0]
df.head()

# Exploramos la estructura de la tabla
df.info()


# --- Limpieza de datos ---

# Eliminamos los símbolos de porcentaje para convertir los valores en numéricos
df = df.replace({'%': ''}, regex=True)
df.head()

# Convertimos las columnas relevantes a valores numéricos
df[['Year']] = df[['Year']].apply(pd.to_numeric)
# Convertimos columnas con subcabeceras (multi indexes)
df[('Republican', '%')] = pd.to_numeric(df[('Republican', '%')])
df[('Democratic', '%')] = pd.to_numeric(df[('Democratic', '%')])

# Comprobamos que las columnas han sido convertidas correctamente
df.info()


# --- Ejemplo con otra página web ---

# Probamos otra URL para importar tablas en HTML
dfs = pd.read_html('http://www.contextures.com/xlSampleData01.html')
print(f'Total de tablas detectadas en esta página: {len(dfs)}')

# Exploramos la primera tabla (saca la cabecera incorrectamente)
dfs[0].head()

# Corregimos la cabecera con `header=0`, es decir, le indicamos que no tiene cabecera y que directamente recoja datos
dfs = pd.read_html('http://www.contextures.com/xlSampleData01.html', header=0)
dfs[0].head()
dfs[2].head()

# --- Ejemplo de autenticación en una página ---

# Intentamos acceder a una página que requiere autenticación (lanza error)
try:
    pd.read_html('https://httpbin.org/basic-auth/myuser/mypasswd')
except ValueError as e:
    print("Error de autenticación:", e)

import requests

# Hacemos una solicitud sin autenticación para ver el código de estado
r = requests.get('https://httpbin.org/basic-auth/myuser/mypasswd')
print(f"Estado de la solicitud sin autenticación: {r.status_code}")

# Ahora intentamos con autenticación
r = requests.get('https://httpbin.org/basic-auth/myuser/mypasswd', auth=('myuser', 'mypasswd'))
print(f"Estado de la solicitud con autenticación: {r.status_code}")



# --- Otro Ejemplo Completo en Wikipedia: Línea de tiempo de lenguajes de programación ---

# Obtenemos varias tablas de una página
dfs = pd.read_html('https://en.wikipedia.org/wiki/Timeline_of_programming_languages', header=0)
print(f'Total de tablas detectadas en esta página: {len(dfs)}')

# Exploramos la quinta tabla
dfs[4].head()

# Combinamos varias tablas en una sola
df = pd.concat(dfs[4:12], ignore_index=True)

# Limpiamos filas duplicadas de encabezado
df = df[df["Year"] != "Year"]

# Filtramos por un valor específico (Python) para ver si está en la tabla
print(df)
print(df[df["Name"] == "Python"])

# Guardamos el DataFrame resultante en un archivo CSV
df.to_csv("Programas.csv", index=False)
print("Archivo 'Programas.csv' guardado con éxito.")


# ----------------------------------------------------------------------------
# Eliminar tildes utilizando normalize (para estandarizar datos, útil para análisis de datos por ejemplo)
from unicodedata import normalize

# Lista de nombres con caracteres especiales
nombres = ["José", "Muñoz", "François", "Gödel", "Mårten"]

# Normalizar los nombres eliminando acentos y caracteres especiales
nombres_normalizados = [normalize('NFKD', nombre).encode('ASCII', 'ignore').decode('ASCII') for nombre in nombres]

# Mostrar los resultados
print("Nombres originales:", nombres)
print("Nombres normalizados:", nombres_normalizados)

# Se podría aplicar en los dataframes
df = pd.DataFrame({'Nombre': nombres})
df['Nombre_normalizado'] = df['Nombre'].apply(lambda x: normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII'))


# ----------------------------------------------------------------------------

# EJERCICIO 1

# Accede a: https://en.wikipedia.org/wiki/La_Liga
# Y obtén los datos de la tabla 'Results of Barça and Real Madrid in the 21st century'
# Indícame de cada equipo cuántos años quedaron primeros

