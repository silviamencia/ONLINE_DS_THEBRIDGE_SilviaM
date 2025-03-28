# -*- coding: utf-8 -*-
Created on Thu Oct 17 11:22:17 2024

# Ejercicios Ficheros
# Recuerda marcar como directorio de trabajo el script donde estés ejecutando el fichero. También puedes crear una subcarpeta “archivos” donde meter todos los ficheros, para ello puedes usar rutas relativas: "./archivos/nombre_archivo.txt"
# Ejercicio 1: Leer un fichero de texto
# Objetivo: Crea un script que lea el contenido de un fichero llamado poema.txt y muestre su contenido en la consola.
# Abre el fichero en modo lectura ("r").
# Lee todo el contenido del fichero.
# Muestra el contenido en pantalla.
# Pistas:
# Usa la función open() para abrir el fichero.
# Usa el método .read() para leer todo el contenido de una sola vez.


# Marcar el directorio de trabajo actual
import os
"./archivos/nombre_archivo.txt"
print(os.getcwd())
poema = open ("./archivos/poema", "x")
poema = open("./archivos/poema", "r")

# Ejercicio 2: Escribir en un fichero de texto
# Objetivo: Crea un script que escriba un mensaje en un fichero llamado notas.txt.
# Abre el fichero en modo escritura ("w").
# Si el fichero no existe, debe crearse automáticamente.
# Escribe en el fichero: "Esta es mi primera nota en este archivo."
# Pistas:
# Recuerda que el modo "w" sobrescribe el contenido si el fichero ya existe.
# Usa el método .write() para escribir en el fichero.

notas = open ("./archivos/notas", "w")
notas.write ("Esta es mi primera nota en este archivo.\n")
notas.close ()


# Ejercicio 3: Añadir contenido a un fichero
# Objetivo: Modifica el script del Ejercicio 2 para que no sobrescriba el contenido, 
# sino que añada texto al final del fichero.
# Abre el fichero notas.txt en modo añadir ("a").
# Añade el siguiente mensaje: "Esta es otra línea añadida al archivo."
# Pistas:
# Usa el modo "a" para añadir contenido al final del fichero sin eliminar lo anterior.

with open ("./archivos/notas", "a") as notas:
    notas.write ("Esta es otra línea añadida al archivo.\n")

# Ejercicio 4: Leer líneas de un fichero
# Objetivo: Crea un script que lea y muestre cada línea de un fichero de texto, línea por línea.
# Usa el fichero poema.txt del Ejercicio 1.
# Abre el fichero en modo lectura.
# Lee el contenido línea por línea y muestra cada línea por separado.
# Pistas:
# Usa un bucle for para recorrer cada línea del fichero.

with open ("./archivos/poema", "r", encoding="utf8") as lectura:
    Lineas = lectura.readlines()
    for i, linea in enumerate(Lineas):
        print(linea)
        print(i)
    
    
with open ("./archivos/poema", "r", encoding="utf8") as lectura:
    Lineas = lectura.readlines()
    for i in range(len(Lineas)):
        print(f"{Lineas[i]}")
        print(i)     
        
# Ejercicio 5: Manejo de excepciones al leer un fichero
# Objetivo: Crea un script que intente leer un fichero llamado archivo_inexistente.txt y capture el error si el fichero no existe.
# Usa un bloque try-except para manejar el error FileNotFoundError.
# Si el fichero no se encuentra, muestra el mensaje "Error: El archivo no existe.".
# Pistas:
# Usa try-except para manejar la excepción FileNotFoundError.

with open ("./archivos/", "r", encoding="utf8") 


# Ejercicio 6: Leer y escribir en un fichero CSV
# Objetivo: Crea un script que lea un fichero CSV llamado alumnos.csv, muestre su contenido y luego añada un nuevo alumno.
# Usa el fichero alumnos.csv con las columnas: Nombre, Edad, Email.
# Muestra el contenido de cada fila del fichero CSV.
# Añade un nuevo alumno al fichero: "Carlos, 24, carlos@mail.com".
# Pistas:
# Usa el módulo csv para manejar el fichero.
# Usa el método .writerow() para añadir nuevas filas.

import csv

try:
    with open("./archivos/alumnos.csv", "a", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Carlos", 24, "carlos@mail.com"])

    print("Se ha añadido al archivo 'alumnos.csv'.")
except Exception as e:
    print(f"Error al escribir en el archivo CSV: {e}")
    
# Ejercicio 7: Contar líneas y palabras en un fichero
# Objetivo: Crea un script que cuente el número de líneas y el número total de palabras en un fichero llamado texto.txt.
# Abre el fichero en modo lectura.
# Recorre cada línea del fichero, contando el número de líneas.
# Para cada línea, cuenta cuántas palabras contiene y suma el total de palabras.
# Muestra el número total de líneas y el número total de palabras.
# Pistas:
# Usa el método .split() para dividir una línea en palabras.
# Utiliza un contador para sumar las palabras.

with open ("./archivos/poema", "r", encoding="utf8") as lectura:
    Lineas = lectura.readlines()
    numero_lineas  = len(Lineas)
    numero_palabras2 = 0
    for i, linea in enumerate(Lineas):
        #print(i,linea)
        palabras = linea.split()
        numero_palabras = len(palabras)
        numero_palabras2 = numero_palabras + numero_palabras2
        print("El número de palabras en esta línea es: ", {numero_palabras})
        
    print("El número de líneas es: ", {numero_lineas})
    print("El número total de palabras es: ", {numero_palabras2})
      


# Ejercicio 8: Buscar y eliminar duplicados en un fichero CSV
# Objetivo: Crea un script que lea un fichero CSV llamado clientes.csv y elimine los registros duplicados basados en la columna Email.
# Abre el fichero en modo lectura.
# Almacena los registros en un diccionario usando el Email como clave para eliminar duplicados.
# Escribe los registros únicos en un nuevo fichero CSV llamado clientes_unicos.csv.
# Pistas:
# Usa un diccionario para evitar duplicados.
# Escribe los registros únicos en un nuevo CSV.

import csv
with open("./archivos/alumnos.csv", "r") as archivo:
    reader = csv.reader(alumnos.csv, delimiter = "/n")

encabeza    
    

# Ejercicio 9: Leer un fichero y buscar una palabra
# Objetivo: Crea un script que lea un fichero llamado libro.txt y 
# busque una palabra específica introducida por el usuario.
# Solicita al usuario que introduzca la palabra a buscar.
# Abre el fichero y recorre su contenido.
# Muestra cuántas veces aparece la palabra en el fichero.
# Pistas:
# Usa el método .count() para contar las apariciones de la palabra en cada línea.


with open ("./archivos/poema", "r", encoding="utf8") as lectura:
    Lineas = lectura.readlines()
    palabra = input("Por favor, introduzca la palabra a buscar:     ")
    contador = 0
    for i in enumerate(Lineas):
        
        
        coincidencia = lectura.find ("palabra")
        lectura.count = "palabra"
    
    
    
    
    


