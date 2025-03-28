# -*- coding: utf-8 -*-

# --------- Ejercicio 1: Tipos de datos ---------
# Definir variables de cada tipo
entero = 10
decimal = 3.14
texto = "Hola"
booleano = True

# Mostrar el valor y tipo de cada variable
print(entero, type(entero))      # 10 <class 'int'>
print(decimal, type(decimal))    # 3.14 <class 'float'>
print(texto, type(texto))        # Hola <class 'str'>
print(booleano, type(booleano))  # True <class 'bool'>

# Resetear variables
%reset -f

# --------- Ejercicio 2: Operaciones matemáticas ---------
# Definir dos números
a = 15
b = 4

# Realizar operaciones y mostrar resultados
print("Suma:", a + b)                 # 19
print("Resta:", a - b)                # 11
print("Multiplicación:", a * b)       # 60
print("División:", a / b)             # 3.75
print("División entera:", a // b)     # 3
print("Exponente:", a ** b)           # 50625
print("Módulo (resto):", a % b)       # 3

# Resetear variables
%reset -f

# --------- Ejercicio 3: Operadores comparativos y lógicos ---------
# Definir variables
x = 10
y = 20

# Comparaciones
print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x > y:", x > y)     # False
print("x < y:", x < y)     # True
print("x >= y:", x >= y)   # False
print("x <= y:", x <= y)   # True

# Operadores lógicos
print("x > 5 and y > 15:", x > 5 and y > 15)   # True
print("x > 15 or y > 15:", x > 15 or y > 15)   # True
print("not (x > y):", not (x > y))             # True

# Resetear variables
%reset -f

# --------- Ejercicio 4: Conversión de tipos ---------
# Pedir la edad al usuario
edad = input("Introduce tu edad: ")

# Convertir la edad a entero
edad = int(edad)

# Se puede hacer en un solo paso
edad = int(input("Introduce tu edad: "))

# Multiplicar la edad por 2
print("El doble de tu edad es:", edad * 2)

# Resetear variables
%reset -f

# --------- Ejercicio 5: Cadenas de texto ---------
# Definir la cadena
nombre = "Juan"
apellido = "Pérez"

# Concatenación usando +
nombre_completo_1 = nombre + " " + apellido
print("Concatenación con +:", nombre_completo_1)

# Concatenación usando f-strings
nombre_completo_2 = f"{nombre} {apellido}"
print("Concatenación con f-strings:", nombre_completo_2)

# Acceso a caracteres
print("Primera letra del nombre:", nombre[0])    # J
print("Última letra del apellido:", apellido[-1]) # z

# Longitud de la cadena completa
print("Longitud del nombre completo:", len(nombre_completo_1))

# Convertir a mayúsculas y eliminar espacios adicionales
nombre_mayusculas = nombre_completo_1.upper().strip()
print("Nombre completo en mayúsculas:", nombre_mayusculas)

# Resetear variables
%reset -f

# --------- Ejercicio 6: Formateo de cadenas y números ---------
# Definir el valor de pi
pi = 3.14159

# Mostrar con 2 decimales
print(f"Pi con 2 decimales: {pi:.2f}")

# Alinear a la derecha con 3 decimales en un espacio de 10 caracteres
print(f"Pi alineado a la derecha: {pi:>10.3f}")

# Resetear variables
%reset -f

# --------- Ejercicio 7: Comentarios ---------
# Definir dos números
a = 5
b = 3

# Sumar los dos números
suma = a + b

# Mostrar el resultado
print("La suma es:", suma)

# Resetear variables
%reset -f

# --------- Ejercicio 8: Ejercicio práctico final ---------
# Pedir el nombre y la edad al usuario
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

# Crear la frase
frase = f"Hola, me llamo {nombre} y tengo {edad} años."
print(frase)

# Condición mayor/menor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Convertir el nombre a mayúsculas
nombre_mayusculas = nombre.upper()
print("Tu nombre en mayúsculas es:", nombre_mayusculas)

# Contar cuántas veces aparece la letra "a"
conteo_a = nombre.lower().count('a')
print(f"La letra 'a' aparece {conteo_a} veces en tu nombre.")

