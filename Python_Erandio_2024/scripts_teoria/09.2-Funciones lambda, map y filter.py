#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:51:51 2023

@author: laptop
"""

#######################
# List comprehension  #
#######################
"""
La comprensión de listas en Python es una característica que permite construir listas 
de manera concisa y legible utilizando una sintaxis compacta. 

Permite crear una lista a partir de otra lista, una cadena, u otra secuencia de datos, 
aplicando una expresión a cada elemento de la secuencia. 

Esto se hace mediante una sintaxis que combina bucles for y condicionales de una manera 
más compacta que los enfoques tradicionales.

Por ejemplo, considera la siguiente comprensión de lista que genera una lista de los 
cuadrados de los números del 0 al 9:
"""
parabola = [x**2 for x in range(10)]
"""
Aquí, x**2 es la expresión que se aplica a cada elemento x en el rango de 0 a 9. 
La comprensión de lista luego crea una lista con los resultados de estas expresiones.

Las comprensiones de lista pueden incluir también condiciones, lo que permite filtrar 
elementos según ciertas condiciones. Por ejemplo:
"""
parabola_pares = [x**2 for x in range(10) if x % 2 == 0]
"""
Esta comprensión de lista crea una lista de los cuadrados de los números del 0 al 9 que son pares.

La función que apliquemos a los elementos de la lista la podemos definir aparte:
"""

def divide2(num):
    print(f"Divido {num} entre 2")
    return num/2

lista_num = [divide2(elemento) for elemento in list(range(0, 300, 15))]
"""
Desordenamos la lista de manera aleatoria. Esta lista de números será nuestro 
"conejillo de indias" para ver el funcionamiento de map y filter
"""
import random
random.shuffle(lista_num)

########
# Map  #
########
"""
`map` aplica una función cualquiera a un iterable de manera que se ejecuta elemento a elemento.

Por ejemplo, si creamos la función `duplica` que recibe un número y lo devuelve multiplicado por 2
"""
def duplica(numero):
    return 2 * numero

# Podemos hacer pasar por la función a todos los elementos de lista_num
generador = map(duplica, lista_num)

# map no se ejecuta inmediatamente sino que crea una función generadora
# que en cada petición "next" evalúa la función para un elemento del iterable.

# El uso de map equivale a esto:
"""
def mapeador(lista_cualquiera):
    for elemento in lista_cualquiera:
        yield duplica(elemento)

generador = mapeador(lista_num)     
"""

next(generador)
next(generador)
next(generador)

# Otro ejemplo, con una función que devuelve texto
def imprime(numero):
    return f"Este término está ocupado por el elemento {numero}"


generador2 = map(imprime, lista_num)
next(generador2)
next(generador2)
next(generador2)

# Puedo ejecutar la función en todos los elementos si creo una 
# lista para los resultados
lista_desde_generador = list(generador2)

lista_num2 = list(map(duplica, lista_num))

def conversor(cantidad_dolar):
    cantidad_euro = cantidad_dolar/1.085
    return cantidad_euro

lista_beneficio_dolar = [1200, 1500, 2000, 300, 600]

lista_beneficio_euro = list(map(conversor, lista_beneficio_dolar))

###########
# Filter  #
###########
"""
La sintaxis de `filter`, es como la de `map` , pero usando una función que devuelve `True` o `False`.

El resultado es una selección de los elementos que devuelven `True` al ser pasados por la función.
"""

def tiene_decimales(num):
    if num == int(num):
        return False
    else:
        return True

iterable_num_decimales = filter(tiene_decimales, lista_num)
next(iterable_num_decimales)

# Ejecutamos el filtrado de una sola vez
lista_num_decimales = list(iterable_num_decimales)
# Incluso podemos crear el generador en el momento de crear la lista
lista_num_decimales = list(filter(tiene_decimales, lista_num))


###########
# Lambda  #
###########
"""
Son funciones que pueden utilizar cualquier número de parámetros pero una única expresión. 
Esta expresión es evaluada y devuelta. 
Se pueden usar en cualquier lugar en el que una función sea requerida. 
"""
def doble(num):
    return num*2

# Lambda por reducción de una función sencilla
iterable2 = map(lambda num: num * 2, lista_num)

next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)
next(iterable2)

# Lambda con múltiples parámetros
iterable3 = map(lambda x, y: x + y, lista_num, lista_num2)

lista_num3 = list(iterable3)


#######################
# zip() y enumerate() #
#######################
"""
    ZIP = CREMALLERA
La función zip se utiliza para combinar dos o más iterables en una secuencia de 
tuplas, donde la i-ésima tupla contiene el i-ésimo elemento de cada uno de los 
iterables pasados.
Es decir, esta función agrupa los elementos de las listas, tuplas o cualquier 
otro iterable que se le pase como argumento.
"""

provincias = ["Bizkaia", "Gipuzkoa", "Álava"]
capitales = ['Bilbao', 'San Sebastián', 'Vitoria', "Pamplona"]
habitantes = [200000, 150000, 100000, 130000]
combinados = zip(provincias, capitales)
print(list(combinados))

for provincia, capital in zip(provincias, capitales):
    print(f"La capital de {provincia} es {capital}")


# La función enumerate se utiliza para agregar un contador a un iterable y devolverlo como un objeto enumerado.
print(list(enumerate(provincias)))

for indice, provincia in enumerate(provincias):
    print(f"La provincia número {indice} es {provincia}")
    print(capitales[indice])




# Lambda con múltiples parámetros
iterable3 = map(lambda x, y: x + y, lista_num, lista_num2)

lista_num3 = list(iterable3)


#___________#
# Ejercicio #
#-----------#

# Crear una lista con los números de 0 al 100.
lista100 = list(range(0, 101))

import random
random.shuffle(lista100)


# Dividirlos entre tres con map y una función lambda.
listatercios = list(map(lambda x: x/3, lista100))

# Sin función lambda
def divide3(x):
    return x/3

lista_mod_gen = map(divide3, lista100)
lista_mod = list(lista_mod_gen)


# Filtrar los que tienen parte decimal con una función lambda.
lista_dec_gen = filter(lambda x: x != int(x), lista_mod)
lista_dec = list(lista_dec_gen)

# Sin función lambda
def tiene_decimales(num):
    if num == int(num):
        return False
    else:
        return True

def tiene_decimales(num):
    return num != int(num)

lista_dec_gen = filter(tiene_decimales, lista_mod)
lista_dec = list(lista_dec_gen)


#___________#
# Ejercicio #
#-----------#
import random
# Creamos una lista de edades que por error contiene números negativos y excesivos
edades = [random.randint(-7, 130) for i in range(500)]
edades.count(-3)
edades.count(121)


# Usar filter para eliminar los valores
edades_correctas = list(filter(lambda x: x >= 0 and x <= 120, edades))

def es_correcto(edad):
    return edad >= 0 and edad <= 120

edades_correctas = list(filter(es_correcto, edades))

edades_correctas.count(-3)
edades_correctas.count(121)

len(edades_correctas)

# Usar map para sustituirlos por 120 o 0

def corrector(edad):
    if edad > 120:
        return 120
    elif edad < 0:
        return 0
    else:
        return edad


edades_correctas2 = list(map(corrector, edades))
edades_correctas2.count(-3)
edades_correctas2.count(121)
len(edades_correctas2)
