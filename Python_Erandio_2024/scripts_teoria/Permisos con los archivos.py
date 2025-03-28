# Verificamos que estamos trabajando en el directorio correcto
import os
os.getcwd()

# Error, nombres.txt no existe
fichero = open("datos/nombres.txt", "r")

# Añadir un nombre a un fichero de texto. Si no existe, se crea.
# El permiso "w" crea el archivo
fichero = open("datos/nombres.txt", "w")
fichero.write('Ekaitz' + '\n')
fichero.close()

# Puedo añadir datos al final con el permiso "a"
fichero = open("datos/nombres.txt", "a")
fichero.write('Aitor' + '\n')
fichero.close()

# Si intento escribir el archivo elimino el contenido
fichero = open("datos/nombres.txt", "w")
fichero.write('Begoña' + '\n')
fichero.close()


# Por ejemplo, podemos añadir la hora actual al archivo
from datetime import datetime

datetime.now()

with open("datos/nombres.txt", "a") as fichero:   
    fichero.write(f"Hola son las {datetime.now()}\n")

# Releemos el contenido
fichero = open("datos/nombres.txt", "r")
lineas = fichero.readlines()
# Al leer se coloca el puntero al final. 
# Si quiero que funciones el siguiente read tengo que recolocarlo
# fichero.seek(0)
contenido = fichero.read()
fichero.close()

print(contenido)
print(lineas)
# Ventaja de usar una estructura with al abrir un archivo
"""
Se asegura que el archivo se cerrará automáticamente al finalizar el bloque de código 
dentro de la estructura with, incluso si se produce un error o una excepción durante 
la ejecución del código. Esto evita que el archivo quede abierto accidentalmente, 
lo que podría causar problemas de rendimiento o corrupción de datos.
"""

with open('datos/quijote.txt', 'r', encoding="utf8") as archivo:
    contenido = archivo.read()

print(contenido[:300])

# Usando el puntero
with open('datos/nombres.txt', 'r', encoding="utf8") as archivo:
    archivo.seek(2)   # Puntero al principio
    contenido2 = archivo.read(7)

print(contenido2)

#########################
# Lectura con escritura #
#########################

# Se puede abrir un fichero en modo lectura con escritura,
# pero éste debe existir previamente.
# Además por defecto el puntero estará al principio y si escribimos algo
# sobreescribiremos el contenido actual

# Creamos un fichero de prueba con 4 líneas
fichero = open('datos/fichero2.txt', 'w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('datos/fichero2.txt', 'r+')
fichero.write("0123456789")
fichero.close()

with open('datos/fichero2.txt', 'r', encoding="utf8") as archivo:
    print(archivo.read())


# Volvemos a poner el puntero al inicio y leemos hasta el final
fichero = open('datos/fichero2.txt', 'r')   
fichero.seek(0)
print(fichero.read())
fichero.close()

########################
# Modificar una línea  #
########################
"""
Para lograr este fin lo mejor es 
    leer todas las líneas en una lista, 
    modificar la línea en la lista, 
    posicionar el puntero al principio y 
    reescribir de nuevo todas las líneas:
"""

fichero = open('datos/fichero2.txt', 'r+')
texto = fichero.readlines()

# Modificamos la línea que queramos a partir del índice
texto[2] = "Esta es la línea 3 modificada\n"

# Volvemos a poner el puntero al inicio y reescribimos
fichero.seek(0)
fichero.writelines(texto)
fichero.close()

# Leemos el fichero de nuevo
with open("datos/fichero2.txt", "r") as fichero:
    print(fichero.read())

