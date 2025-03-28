#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:40:26 2023

@author: laptop
"""

###############
# Decoradores #
###############
# Un decorador es una funcion que se dedica a modificar el resultado de otra función
# Tiene que recibir esa función como parámetro

def funcion_fea():
    return "deVUelVO aLgO FeO"

def funcion_camafeo():
    return "TENGO UN CAMAFEO"

def decoradora(funcion_poco_agraciada):
    def decorada():
        resultado_feo = funcion_poco_agraciada()
        resultado_bonito = resultado_feo.capitalize().replace("feo", "bonito")
        return resultado_bonito
    return decorada

funcion_fea()

funcion_fea_decorada = decoradora(funcion_fea)

funcion_fea_decorada()


funcion_camafeo_decorada = decoradora(funcion_camafeo)

funcion_camafeo_decorada()

funcion_fea()
funcion_camafeo()

# Lo bueno es que la función decoradora es reutilizable para cualquier otra 
# función que devuelva algo feo
@decoradora
def devuelvo_algo_feo():
    return "He hErEdaDO un CaMafeo mUy fEO"

devuelvelo_decorado = decoradora(devuelvo_algo_feo)
devuelvelo_decorado()

devuelvo_algo_feo()

# Representación compacta de una función decoradora
def decoradora(funcion_fea):
    def decorada():
        resultado_feo = funcion_fea()
        resultado_bonito = resultado_feo.capitalize().replace("feo", "bonito")
        return resultado_bonito
    return decorada


# Si declaro la decoradora inmediatamente sobre la definición de la funcion fea...
@decoradora
def funcion_fea():
    return "deVUelVO aLgO FeO"

# ésta se comporta siempre como la función decorada
funcion_fea()

# Lógicamente, las funciones decoradoras no están para modificar strings feos
# El objetivo es poder centrarse en operaciones en la "funcion_fea" y usar la
# decoradora para tratar entradas o salidas.


# Ejemplo, controlar la entrada a una función
# Ahora la función fea es esta división que devuelve error con y = 0

def division(x, y):
    return x/y

division(8,0)

def comprueba_entradas(func):
    def comprobacion(x, y):
        if y == 0:
            return "La entrada de datos no es correcta"
        else:
            resultado = func(x, y)
            return resultado
    return comprobacion


@comprueba_entradas
def division(x, y):
    return x/y

division(1,0)


def comprueba_entradas(func):
    def comprobacion(x, y, mensaje = "Me lo invento"):
        if y == 0:
            return "La entrada de datos no es correcta"
        else:
            resultado = func(x, y, mensaje)
            return resultado
    return comprobacion


@comprueba_entradas
def division_y_print(x, y, mensaje):
    print(mensaje)
    return x/y


division_y_print(2, 1)
division_y_print(2, 1, "Hola")

# La clave de definir bien un decorador es que reciba una función y devuelva
# otra función declarada dentro de ella y que añada algo a la recibida

# Función decoradora que se asegura de que una edad esté bien introducida
def corrige_datos(func):
    def corrector():
        edad = func()
        if not edad.isdigit():
            return "Error. Debes introducir un número"
        else:
            edad_entera = int(edad)
            if not (0 <= edad_entera <= 120):
                return("Edad fuera de los límites")
            else:
                return edad_entera
    return corrector


@corrige_datos
def introduce_edad():
    edad = input("Introduce tu edad: ")
    return edad

@corrige_datos
def introduce_area_garaje():
    edad = input("Introduce tu edad: ")
    return edad

introduce_edad()
introduce_area_garaje()


"""
def funcion_decoradora(funcion_a_decorar):
    def funcion_decorada(parametro_1, parametro_2):
        parametro_1 = transformacion_entrada(parametro_1)
        parametro_2 = transformacion_entrada(parametro_2)
        resultado = funcion_a_decorar(parametro_1, parametro_2)
        resultado = transformacion_salida(resultado)
        return resultado
    return funcion_decorada
"""


def comprueba_params(func):
    def comprobadora(x, y):
        if type(x) is str:
            x_verificada = x
        else:
            return "La primera variable no es un string"
        if type(y) is int:
            y_verificada = y
        else:
            return "La segunda variable no es un entero"
        return func(x_verificada, y_verificada)
    return comprobadora


@comprueba_params
def multiplica_texto(texto, num):
    return num * texto


multiplica_texto("Hola", "Mundo")
multiplica_texto(2, "Mundo")
multiplica_texto("Hola", 3)


#Ejemplo: Decorador de Tiempo de Ejecución

# Puedo medir el tiempo transcurrido usando la librería `time`
import time
inicio = time.time()
fin = time.time()
tiempo_transcurrido = fin - inicio


# Normalmente, la ejecución de un print tarda muy poco
inicio = time.time()
print("Hola")
fin = time.time()
print(fin - inicio)

# Voy a crear una función decoradora que ejecute cualquier función 
# midiendo el tiempo que tarda
def medir_tiempo(func):
    def funcion_medida():
        inicio = time.time()
        salida = func()
        final = time.time()
        print(f"Tiempo de ejecución de la función {func.__name__}, {final - inicio} segundos")
        return salida
    return funcion_medida


# Modificando el `time.sleep(x)` puedo comprobar que mide bien el tiempo.
@medir_tiempo
def ejemplo2():
    time.sleep(2)
    return "Terminé"

ejemplo2()


def medir_tiempo(func):
    def funcion_medida(mensaje):
        mensaje = mensaje.replace("Hola", "Adiós")
        inicio = time.time()
        salida = func(mensaje)
        final = time.time()
        print(f"Tiempo de ejecución de la función {func.__name__}, {final - inicio} segundos")
        salida = salida.upper()
        return salida
    return funcion_medida


@medir_tiempo
def ejemplo2(mensaje):
    print(mensaje)
    salida = "Terminé"
    return salida


ejemplo2("Hola Mundo")

# Para evitar el problema de que no coincidan el número de argumentos de la 
# función decorada y de la decoradora puedo usar *args si son posicionales o 
# **kwargs si son clave-valor

def medir_tiempo(func):
    def funcion_medida(*mensaje):
        inicio = time.time()
        for elemento in mensaje:
            print(elemento)
        salida = func(*mensaje)
        final = time.time()
        print(f"Tiempo de ejecución de la función {func.__name__}, {final - inicio} segundos")
        return salida
    return funcion_medida

@medir_tiempo
def ejemplo3(mensaje):
    time.sleep(3)
    return mensaje

ejemplo3("Hola que tal")
ejemplo3("Hola como estás")


def medir_tiempo(func):
    def funcion_medida(**mensaje):
        inicio = time.time()
        for elemento in mensaje:
            print(elemento)
        salida = func(**mensaje)
        final = time.time()
        print(f"Tiempo de ejecución de la función {func.__name__}, {final - inicio} segundos")
        return salida
    return funcion_medida

@medir_tiempo
def ejemplo(m1, m2):
    time.sleep(1)
    return m2

ejemplo(m1 = "Hola", m2 = "Adios")


# Decoradores con parámetros
"""
Hasta ahora, hemos visto decoradores que transforman una función o sus 
resultados, pero a veces necesitamos un decorador más flexible que permita 
recibir parámetros adicionales. 
Esto es muy útil cuando queremos que el comportamiento del decorador varíe 
según el valor de esos parámetros.

Funciona envolviendo la función original en varias capas:

1. Primera capa: una función que recibe los parámetros del decorador.
2. Segunda capa: dentro de esta función, creamos el verdadero decorador, 
    que sigue el mismo esquema que ya hemos visto (recibiendo una función y 
    devolviendo una nueva función decorada).
"""
### Estructura básica de un decorador con parámetros
"""
Imagina que queremos crear un decorador llamado `repetir` que, al aplicarlo a 
una función, permita que esta se ejecute varias veces. 
Para esto, el decorador necesitará saber cuántas veces ejecutar la función, 
por lo que necesita un parámetro `n`.

La estructura general sería la siguiente:
"""

# Primera capa: recibe los parámetros del decorador
def repetir(n):
		# Segunda capa: es el decorador real que recibe la función a decorar
    def decorador(func): 
		    # Tercera capa: la función decorada que se ejecutará
        def decorada(*args, **kwargs):
		        # Ejecuta la función original `n` veces  
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return decorada
    return decorador

@repetir(3)  # Ejecutará la función 3 veces
def saludar():
    print("¡Hola!")

saludar()  # Imprimirá "¡Hola!" tres veces

