# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:11:38 2024

"""

#1. Cálculo de área y perímetro de un rectángulo
# Crea una función que pida al usuario ingresar el ancho y la altura de un rectángulo, y que luego calcule y muestre su área y perímetro.


def area_perimetro():
    ancho = float(input("Introduce ancho:"))
    alto = float(input("Introduce alto:"))
    Area = ancho * alto
    Perimetro = 2*ancho + 2*alto
    print ("El area es:" ,{Area})
    print ( "El perímetro es:", {Perimetro})
    
area_perimetro()


#2. Promedio de una lista de números
#Escribe una función que tome una lista de números como parámetro y retorne el promedio de los números. 
#Incluye la validación para que solo acepte listas que contengan al menos un número.

import math
def promedio(Numeros):
    suma = 0
    numero_de_numeros=0
    for numero in Numeros:
        if type(numero) == int or type(numero) == float:
            suma+=numero
            numero_de_numeros+=1
            
    media=suma/numero_de_numeros   
    print("El promedio es:", {media})
            
       
promedio(["h",3])


    
#3. Contar ocurrencias de una palabra
#scribe un programa que solicite al usuario ingresar una frase y una palabra, 
#y luego cuente cuántas veces aparece la palabra en la frase, sin importar las mayúsculas o minúsculas.

def ocurrencias_palabra(): 
    
    frase = input("Mete una frase " )
    frase_palabras = frase.split()
    numero_de_veces = len(frase_palabras)
    palabra = input("Mete una palabra: ")
    contador=0
    
    for palabra_de_frase in frase_palabras:
      if palabra in palabra_de_frase:
         contador+= 1
        
    print("El numero de veces que aparece es:",{contador} )

ocurrencias_palabra()    
    

#4. Intercambiar valores de una tupla
#Crea una función que reciba una tupla de dos elementos y 
#retorne una nueva tupla con los valores intercambiados. 
#Por ejemplo, para la tupla (5, 10), debe devolver (10, 5).

def intercambio(a,b):
    tupla = (a,b)
    lista = list(tupla)
    primero = lista[0]
    segundo = lista[1] 
    lista2 = (segundo, primero)
    tupla_intercambiada = tuple(lista2)
    return tupla_intercambiada
    
intercambio(5,10)
    
def intercambio(a,b):
    tupla = (b,a)
    
    return tupla
    
intercambio(5,10)

def intercambio(a,b):
    tupla = (a,b)
    lista = list(tupla)
    primero = lista[0]
    segundo = lista[1] 
    lista2 = (segundo, primero)
    tupla_intercambiada = tuple(lista2)
    return tupla_intercambiada



tupla=(3,6,9,12)
tupla[::-1]

tupla =(1,2)
tupla2 = (tupla[1], tupla[0])
    
# 5. Divisores de un número
# Crea un programa que solicite al usuario ingresar un número entero positivo 
# y que luego imprima todos sus divisores.

def divisores(num):
  
    factores = [1]
    for divisor in range(2,num):
        if num % divisor == 0:
            factores.append(divisor)
    factores.append(num)
    return factores      
            
       
divisores(30)
        


def pide_factores():
    numero = -1
    while numero < 0:
        numero = int(input("Dame un número entero: "))
    lista_factores = divisores(numero)
    return lista_factores

pide_factores() 
    
    

# 6. Filtrar números pares de una lista
# Escribe una función que reciba una lista de números y devuelva una nueva lista que contenga 
# solo los números pares. Usa un bucle for y operadores condicionales.

    
def filtra_pares(lista_num):
    salida = []
    for numero in lista_num:
        if numero % 2 == 0:
            salida.append(numero)
    return salida

filtra_pares([1,2,3,4,5,6])

# 7. NO HACER Manejo de excepciones en una calculadora
# Crea una calculadora que permita sumar, restar, multiplicar y dividir dos números ingresados por el usuario. Asegúrate de manejar excepciones como la división por cero utilizando un bloque try-except.

# 8. Suma de valores de un diccionario
# Escribe un programa que tome un diccionario cuyos valores sean números 
# y calcule la suma de todos los valores.


diccionario = {"valor1":1, "valor2":2, "valor3":3, "valor4":4}
suma = 0
#sum_total= diccionario.get("valor1") + diccionario.get("valor2") + diccionario.get("valor3")+diccionario.get("valor4")
for valor in diccionario.values():
    suma = suma + valor
print({suma})


# 9. Lectura y escritura en archivos
# Crea un programa que lea el contenido de un archivo de texto llamado datos.txt y 
# luego escriba una nueva versión del archivo donde cada línea está numerada. 
# Utiliza el bloque with para gestionar los archivos.

import os
with open ("./archivos/poema", "r", encoding="utf8") as lectura:
    Lineas = lectura.readlines()
    for i in range(len(Lineas)):
        print(f"{Lineas[i]}", [i])
        
    
    
# 10. Generador de números pares
# Escribe una función generadora que devuelva números pares entre 0 y 
# un valor n proporcionado por el usuario. Luego, imprime todos los números generados.
       
def filtra_pares(n):
   
    for numero in range(n+1):
        if numero % 2 == 0:
            print(numero)
            yield numero

filtra_pares(6)
generador = filtra_pares(6)
next(generador)
next(generador)
next(generador)
next(generador)
next(generador)

#next(generador)
    