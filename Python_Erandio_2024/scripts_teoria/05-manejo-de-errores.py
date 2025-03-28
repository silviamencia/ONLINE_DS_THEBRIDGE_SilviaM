# -*- coding: utf-8 -*-

# --------- Manejo de Errores en Python ---------

# El manejo de errores en Python se realiza mediante bloques try-except, 
# lo que permite capturar y manejar excepciones para que el programa no falle inesperadamente.

# --------- Try-Except Básico ---------
# En este ejemplo simple, intentamos convertir una cadena en un número, lo que puede generar un error si la cadena no es numérica.

try:
    numero = int("texto")  # Esto lanzará un ValueError
except ValueError:
    print("Error: No se puede convertir la cadena en un número.")
    print("Sigo en el except ValueError")
except:
    print("Except genérico, errores no contemplados en otros bloques except")
finally:
    print("Finally!")

print("Hola!")


# --------- Capturar Múltiples Excepciones ---------
# Es posible capturar diferentes tipos de errores usando varios bloques except.

try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero  # Esto puede lanzar un ZeroDivisionError si el usuario introduce 0
except ValueError:
    print("Error: Entrada inválida, debes introducir un número.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except:
    pass # Si ocurriera un error genérico, no hacemos nada y seguimos con la aplicación


# --------- Capturar Excepciones Genéricas ---------
# Si no sabemos qué tipo de error podría ocurrir, podemos usar un except sin especificar el tipo de excepción.
# ¡Pero ten cuidado! No es una buena práctica capturar todas las excepciones sin manejarlas correctamente.

try:
    resultado = 10 / int(input("Introduce un número: "))
except:
    print("Ocurrió un error, pero no estamos seguros de cuál.")


# --------- Bloque else ---------
# El bloque else se ejecuta si no ocurre ninguna excepción en el bloque try.

try:
    numero = int(input("Introduce un número válido: "))
except ValueError:
    print("Error: No has introducido un número.")
else:
    print(f"Has introducido el número {numero} correctamente.")


# --------- Bloque finally ---------
# El bloque finally se ejecuta siempre, ocurra o no una excepción. Es útil para liberar recursos (por ejemplo, cerrar archivos o conexiones).

try:
    f = open("archivo.txt", "r")
    contenido = f.read()
    print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")
finally:
    print("La operación ha terminado, el archivo (si existía) ha sido gestionado.")


# --------- Excepciones Anidadas ---------
# Podemos anidar bloques try-except para manejar errores en diferentes partes del código.

try:
    f = open("datos.txt", "r")
    
    try:
        contenido = f.read()
        numero = int(contenido)  # Intentamos convertir el contenido a un número
        print(f"El número en el archivo es: {numero}")
    except ValueError:
        print("Error: El archivo no contiene un número válido.")
    
    finally:
        f.close()
        print("El archivo ha sido cerrado.")
except FileNotFoundError:
    print("Error: El archivo no existe.")


# --------- Levantar Excepciones (raise) ---------
# Podemos generar nuestras propias excepciones utilizando la palabra clave 'raise'.

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: No se puede dividir entre cero.")
    
    return a / b

try:
    resultado = dividir(10, 0)  # Forzamos el error
    print(resultado)
except ZeroDivisionError as e:
    print("Error:")
    print(e)

print("La aplicación sigue")

# --------- Creación de Excepciones Personalizadas ---------
# También podemos crear nuestras propias excepciones definiendo clases que hereden de Exception.

class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

try:
    raise MiError("Este es un error personalizado.")
except MiError as e:
    print(f"Ha ocurrido un error: {e.mensaje}")


# --------- Buenas Prácticas ---------
# 1. Capturar únicamente las excepciones que se espera que ocurran.
# 2. Evitar el uso de except genéricos, excepto cuando sea necesario.
# 3. Usar finally para asegurar la limpieza de recursos, como cerrar archivos o conexiones.
