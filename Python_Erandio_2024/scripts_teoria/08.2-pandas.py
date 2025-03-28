# -*- coding: utf-8 -*-

import pandas as pd

# Leer el CSV original
df = pd.read_csv("./archivos/personas.csv")


# Mostrar el DataFrame original
print("Datos originales:")
print(df)


# Nuevos datos que queremos añadir (podría venir de otra fuente o ser creado manualmente)
nuevos_datos = {
    "Nombre": ["Ana", "Carlos", "Beatriz"],
    "Email": ["ana@mail.com", "carlos@mail.com", "beatriz@mail.com"],
    "Edad": [28, 34, 30]
}


# Crear un DataFrame con los nuevos datos
df_nuevos = pd.DataFrame(nuevos_datos)


# Concatenar ambos DataFrames (el original y los nuevos datos)
df_combinado = pd.concat([df, df_nuevos])


# Obtener la primera fila
print("\nDatos combinados con duplicados:")
print(df_combinado)


# Eliminar filas duplicadas basándonos en el campo 'Email'
df_sin_duplicados = df_combinado.drop_duplicates(subset="Email", keep="first")


# Mostrar el DataFrame final sin duplicados
print("\nDatos combinados sin duplicados:")
print(df_sin_duplicados)


# Guardar el DataFrame resultante en un nuevo CSV
df_sin_duplicados.to_csv("./archivos/personas_actualizado_con_pandas.csv", index=False)


# Obtener el primer elemento
primer_elemento = df_sin_duplicados.iloc[0]
print(primer_elemento)
print(type(primer_elemento["Edad"])) # numpy.int64
# Podríamos acceder a un valor concreto: primer_elemento["Nombre"]


# Recorrer todas las filas
for index, row in df.iterrows():
    print(f"Índice: {index}")
    print(f"Nombre: {row['Nombre']}, Email: {row['Email']}, Edad: {row['Edad']}")
    print("-" * 30)


# Acceder a través del valor de una columna
# Establecer una columna como índice
df_indexed = df_sin_duplicados.set_index("Email")

# Acceder a una fila por el valor del índice
fila_especifica = df_indexed.loc["ana@mail.com"]
print(fila_especifica)


# Convertir fila a lista o diccionario
fila_como_lista = df_sin_duplicados.iloc[0].tolist()
print(fila_como_lista)

fila_como_diccionario = df_sin_duplicados.iloc[0].to_dict()
print(fila_como_diccionario)