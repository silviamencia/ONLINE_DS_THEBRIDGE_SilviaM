# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:03:25 2023

@author: Aitor Donado
"""

###############################
# Paso por valor y referencia #
###############################
"""
Dependiendo del tipo de dato enviado a la función, veremos dos comportamientos:

Paso por valor: Se crea una copia local de la variable dentro de la función.
Paso por referencia: Se maneja directamente la variable, los cambios realizados 
    dentro de la función le afectarán también fuera.

Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...
"""
#___________________________
# Ejemplo de paso por valor
#___________________________
"""
Los números se pasan por valor y crean una copia dentro de la función, 
por eso no les afecta externamente lo que hagamos con ellos:
"""

def doblar_valor(numero):
    numero = numero * 2
    print("El valor de 'numero' dentro de la función es", numero)


numero = 10
doblar_valor(numero)
print("El valor de 'numero' fuera de la función es", numero)

#________________________________
# Ejemplo de paso por referencia
#________________________________
"""
Sin embargo las listas u otras colecciones, al ser tipos compuestos se pasan 
por referencia, y si las modificamos dentro de la función estaremos 
modificándolas también fuera:
"""

def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] = 2 * numeros[i]
    print("El valor de 'numeros' dentro de la función es", numeros)


numeros = [10, 50, 100]
doblar_valores(numeros)
print("El valor de 'numeros' fuera de la función es", numeros)


# ___________________________
# ¿Si necesito lo contrario?
# ___________________________

# Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:
def doblar_valor(numero):
    numero = numero * 2
    print("Valor dentro de la función", numero)
    return numero

numero = 10
numero = doblar_valor(numero)
print("El valor de 'numero' fuera de la función es", numero)


# Y en el caso de los tipos compuestos, podemos evitar la modificación enviando 
# una copia:
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
    print("El valor de 'numeros' dentro de la función es", numeros)


numeros = [10, 50, 100]
doblar_valores(numeros[:])  # Una copia al vuelo de una lista con [:]
doblar_valores(numeros.copy()) # o con la función copy
print("El valor de 'numeros' fuera de la función es", numeros)

# Podemos hacer la copia antes de enviar el valor o dentro de la función
# En este caso la hago dentro usando la comprensión de listas
def doblar_valores(numeros):
    """
    Comprensión de lista (List comprehension)
    """
    copia_numeros = [n for n in numeros]
    #copia_numeros = numeros[:]
    #copia_numeros = numeros.copy()
    print("El valor de 'numeros' dentro de la función es", copia_numeros)

doblar_valores(numeros)
print("El valor de 'numeros' fuera de la función es", numeros)


copia_numeros = [n * 2 for n in numeros if n > 10]

copia_numeros = []
for n in numeros:
    if n > 10:
        copia_numeros.append(2*n)


