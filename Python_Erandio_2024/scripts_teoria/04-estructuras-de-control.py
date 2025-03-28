# -*- coding: utf-8 -*-

# --------- Estructuras de Control en Python ---------
%reset -f

# Las estructuras de control permiten modificar el flujo de un programa.
# Las principales son:
# - Condicionales (if, elif, else)
# - Bucles (while, for)

# --------- Condicionales ---------
# La estructura básica es:
# if condición:
#     código si la condición es verdadera
# elif otra_condición:
#     código si la segunda condición es verdadera
# else:
#     código si ninguna condición se cumple

numero = 15

if numero > 10:
    print(f"{numero} es mayor que 10")
elif numero == 10:
    print(f"{numero} es igual a 10")
else:
    print(f"{numero} es menor que 10")

# --------- Condicionales anidados ---------
# Se pueden anidar condicionales dentro de otros para evaluar varias condiciones en secuencia.

edad = 25
if edad >= 18:
    if edad >= 65:
        print("Eres una persona mayor")
    else:
        print("Eres un adulto")
else:
    print("Eres menor de edad")

%reset -f

# --------- Bucles ---------

# Bucle while: Repite un bloque de código mientras una condición se cumpla.
# while condición:
#     código que se ejecuta mientras la condición sea verdadera

contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

# El bucle se detiene cuando la condición deja de ser verdadera.

# --------- Bucle while con break ---------
# Con la instrucción break podemos interrumpir el bucle antes de que la condición se vuelva falsa.

numero_secreto = 7
while True:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza == numero_secreto:
        print("¡Adivinaste!")
        break
    else:
        print("Intenta de nuevo.")

%reset -f

# --------- Bucle for ---------
# El bucle for se utiliza para iterar sobre una secuencia (lista, cadena, rango, etc.)
# for variable in secuencia:
#     código que se ejecuta por cada elemento

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# --------- Bucle for con rango ---------
# El bucle for puede usarse con la función range() para generar secuencias de números.

for i in range(1, 6):
    print(f"Número: {i}")

%reset -f

# --------- Uso de enumerate en bucles ---------
# La función enumerate nos permite obtener tanto el índice como el valor al recorrer una secuencia.

frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

%reset -f

# --------- Bucle anidado ---------
# Un bucle puede estar dentro de otro bucle. Esto se usa para recorrer estructuras más complejas.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea para separar las filas

%reset -f

# --------- For con else ---------
# Se puede usar un bloque else con el for. El código del else se ejecuta cuando el bucle termina normalmente (sin break).

for i in range(5):
    print(i)
else:
    print("El bucle ha terminado.")

%reset -f

# --------- Uso de break y continue ---------
# - break: Termina el bucle inmediatamente.
# - continue: Salta el resto del código en la iteración actual y continúa con la siguiente.

# Ejemplo de break:
for i in range(10):
    if i == 5:
        break  # Se detiene cuando i es 5
    print(i)

print("El bucle se ha detenido en el número 5")

# Ejemplo de continue:
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(f"Número impar: {i}")

%reset -f

# --------- Control de flujo adicional ---------
# - pass: No hace nada, se utiliza cuando se necesita un bloque de código vacío.

numero = 10

if numero > 10:
    pass  # No hacer nada si el número es mayor a 10
elif numero == 10:
    print("El número es igual a 10")
else:
    print("El número es menor a 10")

%reset -f

# --------- Extra: Bucles anidados con condiciones ---------
# Un ejercicio avanzado con bucles y condicionales dentro de bucles.

numeros = [10, 15, 20, 25, 30]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par")
        if numero % 5 == 0:
            print(f"{numero} también es divisible por 5")
    else:
        print(f"{numero} es impar")
