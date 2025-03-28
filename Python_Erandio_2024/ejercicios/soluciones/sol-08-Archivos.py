#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:22:01 2024

@author: laptop
"""
import os
os.getcwd()

# Ejercicio 1: Leer un fichero de texto
# Objetivo: Crea un script que lea el contenido de un fichero llamado poema.txt y muestre su contenido en la consola.
# Abre el fichero en modo lectura ("r").
# Lee todo el contenido del fichero.
# Muestra el contenido en pantalla.
# Pistas:
# Usa la función open() para abrir el fichero.
# Usa el método .read() para leer todo el contenido de una sola vez.

with open("datos/poema.txt", "r", encoding = "latin1") as file:
    poema = file.read()

file = open("datos/poema.txt", "r", encoding = "latin1")
poema = file.read()
file.close()

print(poema)
 

# Ejercicio 2: Escribir en un fichero de texto
# Objetivo: Crea un script que escriba un mensaje en un fichero llamado notas.txt.
# Abre el fichero en modo escritura ("w").
# Si el fichero no existe, debe crearse automáticamente.
# Escribe en el fichero: "Esta es mi primera nota en este archivo."
# Pistas:
# Recuerda que el modo "w" sobrescribe el contenido si el fichero ya existe.
# Usa el método .write() para escribir en el fichero.

texto = "Esta es mi primera nota en este archivo.\n"
with open("datos/notas.txt", "w", encoding = "utf8") as file:
    file.write(texto)


# Ejercicio 3: Añadir contenido a un fichero
# Objetivo: Modifica el script del Ejercicio 2 para que no sobrescriba el contenido, sino que añada texto al final del fichero.
# Abre el fichero notas.txt en modo añadir ("a").
# Añade el siguiente mensaje: "Esta es otra línea añadida al archivo."
# Pistas:
# Usa el modo "a" para añadir contenido al final del fichero sin eliminar lo anterior.

texto2 = "Esta es otra línea añadida al archivo."
with open("datos/notas.txt", "a", encoding = "utf8") as file:
    file.write(texto2)


# Ejercicio 4: Leer líneas de un fichero
# Objetivo: Crea un script que lea y muestre cada línea de un fichero de texto, línea por línea.
# Usa el fichero poema.txt del Ejercicio 1.
# Abre el fichero en modo lectura.
# Lee el contenido línea por línea y muestra cada línea por separado.
# Pistas:
# Usa un bucle for para recorrer cada línea del fichero.

with open("datos/poema.txt", "r", encoding = "latin1") as file:
    lista_poema = file.readlines()
    
for linea in lista_poema:
    print(linea)

# Ejercicio 5: Manejo de excepciones al leer un fichero
# Objetivo: Crea un script que intente leer un fichero llamado archivo_inexistente.txt 
# y capture el error si el fichero no existe.
# Usa un bloque try-except para manejar el error FileNotFoundError.
# Si el fichero no se encuentra, muestra el mensaje "Error: El archivo no existe.".
# Pistas:
# Usa try-except para manejar la excepción FileNotFoundError.

try:
    with open("datos/inexistente.txt", "r", encoding = "latin1") as file:
        lista_poema = file.readlines()
except Exception as e:
    print(f"Ha ocurrido un error {type(e).__name__}")


# Ejercicio 6: Leer y escribir en un fichero CSV
# Objetivo: Crea un script que lea un fichero CSV llamado alumnos.csv, muestre 
# su contenido y luego añada un nuevo alumno.
# Usa el fichero alumnos.csv con las columnas: Nombre, Edad, Email.
# Muestra el contenido de cada fila del fichero CSV.
# Añade un nuevo alumno al fichero: "Carlos, 24, carlos@mail.com".
# Pistas:
# Usa el módulo csv para manejar el fichero.
# Usa el método .writerow() para añadir nuevas filas.

import csv
try:
    with open("datos/alumnos.csv", "w") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Nombre", "Edad", "Email"])
        escritor_csv.writerow(["Ana", 28, "ana@mail.com"])
        escritor_csv.writerow(["Pedro", 35, "pedro@mail.com"])
        escritor_csv.writerows((["a",1,"b"],["c",2,"d"]))
    print("Se ha creado el archivo 'alumnos.csv'.")
except Exception as e:
    print(f"Error al escribir en el archivo CSV: {type(e).__name__} {e}")

try:
    with open("datos/alumnos.csv", "a") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Carlos", 24, "carlos@mail.com"])
    print("Se ha añadido un dato al archivo 'alumnos.csv'.")
except Exception as e:
    print(f"Error al escribir en el archivo CSV: {type(e).__name__} {e}")


# Ejercicio 7: Contar líneas y palabras en un fichero
# Objetivo: Crea un script que cuente el número de líneas y el número total de 
# palabras en un fichero llamado texto.txt.
# Abre el fichero en modo lectura.
# Recorre cada línea del fichero, contando el número de líneas.
# Para cada línea, cuenta cuántas palabras contiene y suma el total de palabras.
# Muestra el número total de líneas y el número total de palabras.
# Pistas:
# Usa el método .split() para dividir una línea en palabras.
# Utiliza un contador para sumar las palabras.

with open("datos/quijote.txt") as fichero:
    lineas = fichero.readlines()

len(lineas)
palabras = 0
for linea in lineas:
    palabras = palabras + len(linea.split(" "))

print(palabras)

with open("datos/quijote.txt") as fichero:
    contenido = fichero.read()

import re
palabras = re.split(r'\s+', contenido)
len(palabras)

# Ejercicio 8: Buscar y eliminar duplicados en un fichero CSV
# Objetivo: Crea un script que lea un fichero CSV llamado clientes.csv y elimine los registros duplicados basados en la columna Email.
# Abre el fichero en modo lectura.
# Almacena los registros en un diccionario usando el Email como clave para eliminar duplicados.
# Escribe los registros únicos en un nuevo fichero CSV llamado clientes_unicos.csv.
# Pistas:
# Usa un diccionario para evitar duplicados.
# Escribe los registros únicos en un nuevo CSV.

# Creación de los datos de clientes.csv
try:
    with open("datos/clientes.csv", "w") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Nombre", "Edad", "Email"])
        escritor_csv.writerow(["Ana", 28, "ana@mail.com"])
        escritor_csv.writerow(["Pedro", 35, "pedro@mail.com"])
        escritor_csv.writerow(["Juan", 44, "ana@mail.com"])
        escritor_csv.writerow(["Carlos", 24, "carlos@mail.com"])
        escritor_csv.writerows((["Luis",18,"luis@hotmail.com"],["Marcos",22,"marcos@mail.com"]))
    print("Se ha creado el archivo 'clientes.csv'.")
except Exception as e:
    print(f"Error al escribir en el archivo CSV: {type(e).__name__} {e}")

# Para leer las líneas vamos a usar DictReader, que las convierte en diccionarios
# Las claves son la primera fila
with open("datos/clientes.csv") as archivo:
    lector_dict = csv.DictReader(archivo)
    for row in lector_dict:
        print(row)

with open("datos/clientes_filtrados.csv", "w", newline='') as csvfile_f:
    escritor = csv.writer(csvfile_f)
    # Iniciamos clientes_filtrados.csv con las claves
    escritor.writerow(("Nombre", "Edad", "Email"))
    # Y empezamos a leer clientes.csv
    with open("datos/clientes.csv", newline='') as csvfile:
        # Guardamos los emails en una lista
        emails = []
        lector = csv.DictReader(csvfile)
        for row in lector:
            print(row["Nombre"], row["Edad"], row["Email"])
            # Si el email no está en la lista, lo añado a la lista y al csv
            if row["Email"] not in emails:
                emails.append(row["Email"])
                escritor.writerow((row["Nombre"], row["Edad"], row["Email"]))
                
# AVANCE
# ¿Cómo haremos esto con pandas?
import pandas as pd
datos = pd.read_csv("datos/clientes.csv")
# https://pandas.pydata.org/pandas-docs/version/2.2.0rc0/reference/api/pandas.DataFrame.drop_duplicates.html
datos.drop_duplicates("Email", keep='first', inplace=True, ignore_index=False)
datos.to_csv("datos/clientes_filtrados2.csv")


# Ejercicio 9: Leer un fichero y buscar una palabra
# Objetivo: Crea un script que lea un fichero llamado libro.txt y busque una palabra específica introducida por el usuario.
# Solicita al usuario que introduzca la palabra a buscar.
# Abre el fichero y recorre su contenido.
# Muestra cuántas veces aparece la palabra en el fichero.
# Pistas:
# Usa el método .count() para contar las apariciones de la palabra en cada línea.

with open("datos/quijote.txt") as fichero:
    contenido = fichero.read()

def contador_personajes(archivo):
    personaje = input("Introduzca su personaje favorito: ")
    with open(archivo) as fichero:
        lineas = fichero.readlines()
    contador_total = 0
    for linea in lineas:
        if personaje in linea:
            print(linea.count(personaje))
            contador_total += linea.count(personaje)
    return contador_total

contador_personajes("datos/quijote.txt")
