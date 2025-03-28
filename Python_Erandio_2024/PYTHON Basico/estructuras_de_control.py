# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:55:42 2024

@author: LANER
"""

# Ejercicios de Estructuras de Control
# Nivel Básico
# Condicional simple (if)
# Escribe un programa que pida al usuario un número e imprima si es mayor, menor o igual a 10.

print("Introduce tu edad:")
Edad = int(input())
if Edad <= 10: print(f"El número es menor de 10")
if Edad == 10: print(f"El número es igual a 10")
if Edad > 10:  print(f"El número es mayor a 10")

# Condicional con elif y else
# Pide al usuario su edad e imprime si es un niño (menor de 12 años), un adolescente (entre 12 y 17 años) o un adulto (18 años o más).

Edad = int(input('¿Qué edad tienes? '))
if Edad < 12: 
    print(f"Menor de 12 años")
elif Edad <= 17: 
    print(f"Adolescente")
else: 
    print(f"Adulto")

if Edad < 10:
    print("Menor que 10")

if Edad < 20:
    print("Menor que 20")

# Bucle while simple
# Escribe un programa que solicite al usuario ingresar un número. 
# El programa debe sumar todos los números que el usuario introduzca hasta que 
# el usuario ingrese un número negativo. Luego, muestra el total.

Suma_numero = 0

while True:
    Numero = int(input("Introduce un número(negativo para salir"))
    if Numero < 0:
        break
    Suma_numero =+ Numero 

# Bucle for simple
# Crea un programa que imprima los números del 1 al 10 usando un bucle for.

numeros =[1,2,3,4,5,6,7,8,9,10]
for i in numeros: 
    print(f"El número es", {i})

# Nivel Intermedio
# Uso de break en un bucle
# Escribe un programa que recorra los números del 1 al 10, pero que se detenga y salga del bucle cuando encuentre el número 7.

numeros =[1,2,3,4,5,6,7,8,9,10]
for i in numeros:
    if i == 7:
        break
    print(f"El numero es", {i})

# Uso de continue en un bucle
# Crea un programa que imprima todos los números del 1 al 10 excepto el número 5, 
# usando continue.
%reset -f
numeros =[1,2,3,4,5,6,7,8,9,10]
for i in numeros:
    if i == 5:
        continue
    print(f"El numero es", {i})


# Bucle for con else
# Escribe un programa que recorra los números del 1 al 5. 
# Si el número 3 no se encuentra en el recorrido, imprime "No se encontró el número 3". 
# Usa un bloque else junto con el for.

lista=[1,2,3,4,5]
for i in lista:
    if i != 3:
        print({i})
    else:
        print("No se encontró el número 3")
    if i!=3:
else 
    print("No se encontró el número 3")
    
    
# Condicional con operadores lógicos
# Pide al usuario dos números y verifica si ambos son positivos. 
# Si lo son, imprime "Ambos son positivos". 
# Si al menos uno es negativo, imprime "Hay al menos un número negativo".

Numero1 = int (input("Dime un numero"))
Numero2 = int (input("Dime otro número"))
if Numero1 > 0 and Numero2 > 0:
    print(f"Ambos positivos")
else:
    print(f"Hay al menos un número negativo")
        
# Ejercicios Avanzados de Estructuras de Control
# Introducción
# Normalmente no te dan los pasos a realizar indicados, 
# lo más habitual es tener que dar solución a un problema.
# Con estos ejercicios, vamos a intentar aprender cómo, 
# en base a un enunciado, tenemos que pararnos a pensar cómo estructurar nuestro código y plantearnos qué tipos de estructuras de datos y control necesito y cómo puedo llegar a conseguir el objetivo.

# Ejercicio 1: Clasificación de números en una lista
# Escribe un programa que solicite al usuario ingresar una lista de números enteros. 
# El programa debe procesar la lista y clasificar cada número en una de varias categorías:
# positivo, negativo, par, impar, y múltiplo de 3. 
# Al final, muestra cuántos números pertenecen a cada categoría. 
# Además, si un número cumple más de una condición, 
# indica todas las categorías a las que pertenece.

Positivos
Negativos
Par
Impar
Multiplo3

Numero1 = int()
Numero2 = int()
Numero3 = int()
Numero4 = int()
Numero5 = int()
Lista= list[Numero1, Numero2, Numero3, Numero4, Numero5] 
input("Ingresa una lista de 5 números enteros")
for i in Lista:
    if i > 0 and i % 2 == 0 and i % 3 == 0:
        print(f"El número es positivo, par y múltiplo de 3")

if Numero1 % 2 == 0 and Numero
    print("El número es par")
else: 
    print("El número es impar");
    lista
        
    
    


# Ejercicio 2: Sistema de evaluación de resultados
# Diseña un programa que simule un sistema de evaluación de resultados deportivos. 
# El usuario deberá ingresar los resultados de varios partidos en formato de goles de dos 
# equipos (por ejemplo, 2-1, 3-3, etc.). 
# El programa debe procesar cada resultado y determinar si fue una victoria, 
# derrota o empate. También debe identificar si se dieron condiciones especiales, como más de 3 goles en total o si algún equipo no marcó goles. Al final, muestra un resumen con las estadísticas.

   
