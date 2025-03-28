# -*- coding: utf-8 -*-

import os
# Conocer el camino/path del proyecto actual (y guardarlo)
path_proyecto = os.getcwd()

# path relativo del archivo
with open("datos/quijote.txt") as file:
    contenido = file.read()

# path absoluto del archivo
with open(r"/home/laptop/Proyectos Python/Ligas/resultados/laliga_24-25.csv") as file:
    contenido = file.read()

# Cambiar la ubicación por defecto en la que busca los archivos    
os.chdir("/home/laptop/Proyectos Python/Ligas/resultados/")
# Comprobar que el cambio se ha realizado
os.getcwd()

# Ahora ya podemos abrir archivos en la ubicación
with open("bundesliga_24-25.csv") as file:
    contenido = file.read()

# Reestablecemos la ubicación original
os.chdir(path_proyecto)


# 1. El bloque try-except se usa para manejar excepciones, como si el archivo no existe.
# 2. El bloque finally o 'with' asegura que el archivo siempre se cierre después de leer o escribir.
# 3. Los modos de apertura de archivos en Python ("r", "w", "a") permiten controlar si se leen, sobrescriben o añaden datos.
# 4. Para trabajar con CSV, utilizamos el módulo csv, que facilita la lectura y escritura de estos archivos de datos.

# --------- Contenido de prueba para los ficheros ---------
# Generar el archivo de ejemplo 'archivo_ejemplo.txt'
with open("./archivos/archivo_ejemplo.txt", "w") as archivo:
    archivo.write("Esta es la primera línea de ejemplo.\n")
    archivo.write("Aquí va la segunda línea.\n")
    archivo.write("Y esta es la tercera línea.\n")

# Generar el archivo de ejemplo 'personas.csv'
import csv
with open("./archivos/personas.csv", "w", newline="") as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(["Nombre", "Email", "Edad"])
    escritor_csv.writerow(["Ana María", "ana@mail.com", 28])
    escritor_csv.writerow(["Pedro", "pedro@mail.com", 35])
    escritor_csv.writerow(["Lucía", "lucia@mail.com", 22])


# --------- Ejemplo 1: Leer un fichero de texto ---------
%reset -f

# Este ejemplo muestra cómo leer el contenido de un fichero de texto en Python.

# Abrimos el fichero en modo lectura ("r")
try:
    with open("./archivos/archivo_ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print("Error: El fichero 'archivo_ejemplo.txt' no existe.")

%reset -f


# --------- Ejemplo 2: Escribir en un fichero de texto ---------
# Este ejemplo muestra cómo escribir contenido en un fichero. 
# Si el fichero no existe, Python lo creará automáticamente.

try:
    with open("./archivos/nuevo_archivo.txt", "w") as archivo:
        archivo.write("Esta es la primera línea del archivo.\n")
        archivo.write("Aquí está la segunda línea del archivo.\n")
    print("El archivo 'nuevo_archivo.txt' ha sido creado y escrito.")

except Exception as e:
    print(f"Error al escribir en el fichero: {e}")

%reset -f


# --------- Ejemplo 3: Añadir contenido a un fichero ---------
# En este ejemplo veremos cómo añadir texto a un archivo sin sobrescribir su contenido.
# Usamos el modo "a" (append) para añadir texto al final.

try:
    with open("./archivos/nuevo_archivo.txt", "a") as archivo:
        archivo.write("Esta línea se ha añadido al archivo.\n")
    print("Se ha añadido contenido al archivo 'nuevo_archivo.txt'.")

except Exception as e:
    print(f"Error al añadir contenido al fichero: {e}")

%reset -f


# --------- Ejemplo 4: Leer líneas de un fichero ---------
# Este ejemplo muestra cómo leer el archivo línea por línea usando un bucle.

try:
    with open("./archivos/archivo_ejemplo.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())  # .strip() elimina los saltos de línea al final

except FileNotFoundError:
    print("Error: El fichero 'archivo_ejemplo.txt' no existe.")

%reset -f


# --------- Ejemplo 5: Manejo de excepciones con ficheros ---------
# Este ejemplo combina la lectura de un fichero con manejo de excepciones.
# Veremos cómo manejar errores cuando el archivo no se encuentra.

try:
    with open("./archivos/archivo_no_existe.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no se encontró.")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")

%reset -f


# --------- Ejemplo 6: Leer y escribir un fichero CSV ---------
# Este ejemplo muestra cómo trabajar con ficheros CSV, tanto para leer como para escribir.
import csv

# Leer un archivo CSV
try:
    with open("./archivos/personas.csv", "r") as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            print(fila)
except FileNotFoundError:
    print("Error: El archivo 'personas.csv' no existe.")

# Escribir en un archivo CSV
try:
    with open("./archivos/nuevo_personas.csv", "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Nombre", "Email", "Edad"])
        escritor_csv.writerow(["Ana", "ana@mail.com", 28])
        escritor_csv.writerow(["Pedro", "pedro@mail.com", 35])
    print("Se ha creado el archivo 'nuevo_personas.csv'.")
except Exception as e:
    print(f"Error al escribir en el archivo CSV: {e}")

%reset -f


# --------- Ejemplo 7: Combinar leer y escribir para insertar solo si el email es único ---------
# Función para comprobar si un email ya existe en el archivo CSV
def email_existe(email, nombre_archivo="./archivos/personas.csv"):
    try:
        with open(nombre_archivo, "r") as archivo:
            lector_csv = csv.reader(archivo)
            # Saltamos la cabecera si existe
            next(lector_csv, None)
            for fila in lector_csv:
                if fila[1] == email:  # Compara con la columna del email (índice 1)
                    return True
        return False
    except FileNotFoundError:
        # Si el archivo no existe, retornamos False (como si no existiera el email)
        return False

# Función para insertar un nuevo registro solo si el email no existe
def insertar_persona(nombre, email, edad, nombre_archivo="./archivos/personas.csv"):
    if email_existe(email, nombre_archivo):
        print(f"Error: El email '{email}' ya existe en el archivo.")
    else:
        try:
            with open(nombre_archivo, "a", newline="") as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow([nombre, edad, email])
                print(f"Se ha añadido a '{nombre}' con email '{email}' al archivo.")
        except Exception as e:
            print(f"Error al escribir en el archivo CSV: {e}")

# Ejemplo de uso:
nombre = "Carlos Nuevo"
email = "carlos@mail.com"
edad = 40

insertar_persona(nombre, email, edad)

