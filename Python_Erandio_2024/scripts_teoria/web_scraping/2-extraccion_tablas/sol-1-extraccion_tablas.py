# -*- coding: utf-8 -*-

import pandas as pd

# URL de la página de Wikipedia
url = 'https://en.wikipedia.org/wiki/La_Liga'

# Extraer la tabla específica con los resultados del Barcelona y Real Madrid en el siglo XXI
tables = pd.read_html(url, match='Results of Barça and Real Madrid in the 21st century', encoding="utf-8")
df = tables[0] # Seleccionamos la primera tabla encontrada
len(df)

df
df.head() # Muchas columnas sin nombre y con valor NaN
df.info()

# Si quisiéramos trabajar con el texto de cada fila de una columna tipo texto:
# for index, row in df.head().iterrows():
#     print(f"{index} {row['Season'].replace('–', '/')}")

# df['Season'][0][0:4]
# df['Season'][0].replace("-", "/")
# df['Season'][0].replace("–", "/")

df['BAR']
df['RMA']

df.info()
# Convertimos las columnas 'bar' y 'rma' a valores numéricos
df['BAR'] = pd.to_numeric(df['BAR'], errors='coerce')
df['RMA'] = pd.to_numeric(df['RMA'], errors='coerce')
# coerce = aquellos valores que no puedan ser contenidos se considerarán NaN (Not a Number)
# raise = si no puede convertir la columna, lanza excepción
# ignore = si no puede convertir la columna, no la modifica y mantiene el valor original
# Por defecto: raise
# https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html

# Contamos cuántas veces aparece el número 1 en cada columna (Barcelona y Real Madrid)
barcelona_championships = (df['BAR'] == 1).sum()
real_madrid_championships = (df['RMA'] == 1).sum()

len(df[df['BAR']== 1])
len(df[df['RMA']== 1])

# Podemos ver cada fila si sería true o false
df['RMA'] == 1
df['BAR'] == 1

# Mostramos los resultados
print(f"El Barcelona ha quedado en primer lugar {barcelona_championships} veces en el siglo XXI.")
print(f"El Real Madrid ha quedado en primer lugar {real_madrid_championships} veces en el siglo XXI.")
