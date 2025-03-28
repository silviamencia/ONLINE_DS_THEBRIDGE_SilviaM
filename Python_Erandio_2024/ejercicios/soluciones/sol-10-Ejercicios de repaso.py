#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:12:55 2024

@author: laptop
"""

# 1. Cálculo de área y perímetro de un rectángulo
"""Crea una función que pida al usuario ingresar el ancho y la altura de un 
rectángulo, y que luego calcule y muestre su área y perímetro.
"""
def rectangulo(base, altura):
    area = base*altura
    perimetro = 2*(base+altura)
    return area, perimetro

base_rectangulo = 10
altura_rectangulo = 5
area_rect, perimetro_rect = rectangulo(base_rectangulo, altura_rectangulo)


# 2. Promedio de una lista de números
"""
# Escribe una función que tome una lista de números como parámetro y 
retorne el promedio de los números. Incluye la validación para que solo 
acepte listas que contengan al menos un número.
"""
lista = [12, 34, 6.6, "Bilbao", 5]

def promedio(lista_cosas):
    if len(lista_cosas) == 0:
        return "la lista está vacía"
    suma = 0
    numero_de_numeros = 0
    for elemento in lista_cosas:
        if type(elemento) == int or type(elemento) == float:
            suma += elemento
            numero_de_numeros += 1
    media = suma/numero_de_numeros
    return media
            

def promedio2(lista_cosas):
    if len(lista_cosas) == 0:
        return "la lista está vacía"
    suma = 0
    numero_de_numeros = 0
    for elemento in lista_cosas:
        if isinstance(elemento, (int, float)):
            suma += elemento
            numero_de_numeros += 1
    media = suma/numero_de_numeros
    return media


def promedio3(lista_cosas):
    if len(lista_cosas) == 0:
        return "la lista está vacía"
    lista_filtrada = []
    for elemento in lista_cosas:
        if isinstance(elemento, (int, float)):
            lista_filtrada.append(elemento)
    media = sum(lista_filtrada)/len(lista_filtrada)
    return media
    
from statistics import mean       
def promedio4(lista_cosas):
    if len(lista_cosas) == 0:
        return "la lista está vacía"
    lista_filtrada = []
    for elemento in lista_cosas:
        if isinstance(elemento, (int, float)):
            lista_filtrada.append(elemento)
    media = mean(lista_filtrada)
    return media

promedio4(lista)

# 3. Contar ocurrencias de una palabra
"""
# Escribe un programa que solicite al usuario ingresar una frase y una 
palabra, y luego cuente cuántas veces aparece la palabra en la frase, 
sin importar las mayúsculas o minúsculas.
"""
def consola():
    frase = input("Introduzca una frase: ")
    frase = frase.replace("!", "").replace("¡", "")
    frase = frase.replace("?", "").replace("¿", "")
    frase = frase.replace(",", "").replace(".", "")
    frase = frase.replace(";", "").replace(":", "")   
    palabra = input("Introduzca la palabra a buscar: ")
    return frase.lower(), palabra.lower()

def cuenta_palabras(frase = None, palabra = None):
    if not frase and not palabra:
        frase, palabra = consola()
    lista_palabras = frase.split(" ")
    veces = lista_palabras.count(palabra)
    return veces

cuenta_palabras(False, [])

# 4. Intercambiar valores de una tupla
"""
# Crea una función que reciba una tupla de dos elementos y retorne una 
nueva tupla con los valores intercambiados. Por ejemplo, para la 
tupla (5, 10), debe devolver (10, 5).
"""
def invierte(tupla):
    elemento1, elemento2 = tupla
    tupla2 = (elemento2, elemento1)
    return tupla2

def invierte(tupla):
    tupla2 = tupla[::-1]
    return tupla2

algo = (5,10, 15)

invierte(algo)

# 5. Divisores de un número
"""
# Crea un programa que solicite al usuario ingresar un número entero 
positivo y que luego imprima todos sus divisores.
"""
def factorizador(num):
    factores = [1]
    for factor in range(2, num):
        if num % factor == 0:
            factores.append(factor)
    factores.append(num)
    return factores

factorizador(100)

def pide_factores():
    numero = -1
    while numero < 0:
        numero = int(input("Dame un número entero: "))
    lista_factores = factorizador(numero)
    return lista_factores

pide_factores()


# 6. Filtrar números pares de una lista
"""
# Escribe una función que reciba una lista de números y devuelva una nueva 
lista que contenga solo los números pares. Usa un bucle for y operadores 
condicionales.
"""
def filtra_pares(lista_num):
    salida = []
    for numero in lista_num:
        if numero % 2 == 0:
            salida.append(numero)
    return salida

numeros = [1,2,3]

filtra_pares(numeros)

# 7. Manejo de excepciones en una calculadora
"""
# Crea una calculadora que permita sumar, restar, multiplicar y dividir dos 
números ingresados por el usuario. Asegúrate de manejar excepciones como la 
división por cero utilizando un bloque try-except.
"""


# 8. Suma de valores de un diccionario
"""
# Escribe un programa que tome un diccionario cuyos valores sean números y 
calcule la suma de todos los valores.
"""
diccionario = dict(hola = 3, Hasta_luego = 5)
diccionario = {"hola": 3, "Hasta luego": 5}

for pareja in diccionario.items():
    print(type(pareja))
    print("Clave: ", pareja[0])
    print("Valor = ", pareja[1])

for clave in diccionario.keys():
    print(type(clave))
    print("Clave = ", clave)
    
for valor in diccionario.values():
    print(type(valor))
    print("Valor = ", valor)


def suma_valores(diccionario):
    suma = 0
    for valor in diccionario.values():
        suma += valor
    return suma

suma_valores(diccionario)

sum(diccionario.values())

mean(diccionario.values())


# 9. Lectura y escritura en archivos
"""
# Crea un programa que lea el contenido de un archivo de texto llamado 
datos.txt y luego escriba una nueva versión del archivo donde cada línea 
está numerada. Utiliza el bloque with para gestionar los archivos.
"""

with open("datos/poema.txt", "r", encoding="latin1") as archivo:
    with open("datos/poema2.txt", "w", encoding="latin1") as archivo_con_indice:
        for indice, linea in enumerate(archivo):
            print(f"{indice} - {linea}")
            archivo_con_indice.write(f"{indice} - {linea}")
            
            
# 10. Generador de números pares
"""
# Escribe una función generadora que devuelva números pares entre 0 y un 
valor n proporcionado por el usuario. Luego, imprime todos los números 
generados.
"""

def pares(n):
    try:
        n = int(float(n))
        n = abs(n)
    except:
        print(f"No se ha podido convertir 'n'= {n} en un entero positivo")
    print(type(n))
    for valor in range(n+1):
        if valor % 2 == 0:
            yield valor

generador_pares = pares("-13.8")
next(generador_pares)

# Creando el objeto generador (generador_pares)
generador_pares = pares("-13.8")
for par in generador_pares:
    print(par)

generador_pares = pares("-13.8")
lista_pares = list(generador_pares)

generador_pares = pares("-13.8")
lista_pares = [par for par in generador_pares]


# sSaltándome la creación del objeto generador
for par in pares("-13.8"):
    print(par)

lista_pares = list(pares("-13.8"))

lista_pares = [par for par in pares("-13.8")]
