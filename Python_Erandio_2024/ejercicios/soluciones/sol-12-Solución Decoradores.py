#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:39:18 2024

@author: laptop
"""

# Ejercicio 1: Creación básica de un decorador
# Escribe un decorador básico llamado mi_decorador que imprima "Llamando a la 
# función" antes de ejecutar la función decorada y "Función ejecutada" 
# después de que la función decorada haya terminado.
def mi_decorador(func):
    
    def decorada(m):
        print("Llamada a la función")
        salida = func(m)
        print("Función ejecutada")
        # En este caso la salida es None
        return salida

    return decorada
      
@mi_decorador
def saludar(m):
    print("¡Hola!")

# # Llamada a la función decorada
saludar("m")


# Ejercicio 2: Decorador con argumentos
# Modifica el decorador mi_decorador para que sea capaz de decorar una función 
# con cualquier número de argumentos. (Empieza con 2 argumentos, usando la 
# función sumar(a, b) como ejemplo de función decorada.)
def mi_decorador(func):
    def decorada(a, b):
        salida = func(a, b)
        return salida
    return decorada

@mi_decorador
def sumar(a, b):
    return a + b

# # Llamada a la función decorada
resultado = sumar(3, 4)
print(f"Resultado de la suma: {resultado}")


def mi_decorador(func):
    def decorada(*argumentos):
        salida = func(*argumentos)
        return salida
    return decorada

# Ahora el decorador funciona con cualquier función tenga el número de 
# parámetros que tenga
@mi_decorador
def sumar(a):
    return a

@mi_decorador
def sumar(a, b):
    return a + b


@mi_decorador
def sumar(a, b, c):
    return a + b + c

# # Llamada a la función decorada
# Aquí le tengo que dar el número de parámetros de def sumar
resultado = sumar(3, 4, 5)
print(f"Resultado de la suma: {resultado}")


# Ejercicio 3: Decorador con retorno modificado
# Crea un decorador llamado duplicar_resultado que modifique la función decorada 
# para que su resultado se duplique. 

# Usa la función multiplicar(a, b) para probar el decorador.
def duplicar_resultado(func):
    def decorada(a, b):
        resultado = func(a, b)
        resultado = 2 * resultado
        return resultado
    return decorada

@duplicar_resultado
def multiplicar(a, b):
    return a * b

# # Llamada a la función decorada
resultado = multiplicar(5, 3)
print(f"Resultado duplicado: {resultado}")


# Ejercicio 4: Decorador anidado
# Crea dos decoradores: decorador1 y decorador2. El primero imprimirá "Primero" 
# antes de ejecutar la función decorada, y el segundo imprimirá "Segundo". 
# Luego, aplica ambos decoradores a la función mi_funcion.
def decorador1(func):
    def decorada():
        func()
        print("Primero")
    return decorada

def decorador2(func):
    def decorada():
        func()
        print("Segundo")
    return decorada

@decorador2
@decorador1
def mi_funcion():
    print("¡Hola desde la función!")

# # Llamada a la función decorada
mi_funcion()


# Ejercicio 5: Aplicación práctica (autenticación)
"""
Imagina que estás desarrollando una aplicación y necesitas controlar el acceso 
a ciertas funciones según si el usuario está autenticado o no. Crea un decorador 
llamado requiere_autenticacion que verifique si una variable global 
usuario_autenticado es True antes de permitir la ejecución de una función. 

Si el usuario no está autenticado, imprime un mensaje de error.
"""
usuario_autenticado = False


def requiere_autenticacion(func):
    def decorada():
        if usuario_autenticado:
            func()
        else:
            print("No puedes ver esto")
    return decorada
    
    
@requiere_autenticacion
def ver_perfil():
    print("Perfil del usuario")

# Intenta ejecutar la función decorada
ver_perfil()

# Simula la autenticación del usuario
usuario_autenticado = True
ver_perfil()



# Ejercicio 6: Modificar el resultado según un parámetro
# Objetivo: Manipular el resultado de una función con un decorador que acepte parámetros.
# Crea un decorador llamado multiplica_resultado(factor) que multiplique el resultado de la función decorada por un valor dado.
# def multiplica_resultado(factor):
#     # Implementa aquí el decorador con parámetros
#     pass

# @multiplica_resultado(10)
# def obtener_numero():
#     return 7

# # Llamada a la función decorada
# print(obtener_numero())  # Debería imprimir 70


def multiplica_resultado(factor):
    def decorador_de_funcion(func):
        def decorada():
            resultado = func()
            resultado = factor*resultado
            return resultado
        return decorada
    return decorador_de_funcion
    

@multiplica_resultado(10)
def obtener_numero():
    return 7

# Llamada a la función decorada
print(obtener_numero())  # Debería imprimir 70



