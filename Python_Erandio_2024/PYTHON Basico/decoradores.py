# -*- coding: utf-8 -*-

# Ejercicio 1: Creación básica de un decorador
# Escribe un decorador básico llamado mi_decorador que imprima "Llamando a la función" 
# antes de ejecutar la función decorada y "Función ejecutada" después de que la función decorada haya terminado.
# def mi_decorador(func):
#     # Completa aquí el decorador
#     pass

# @mi_decorador
# def saludar():
#     print("¡Hola!")

# # Llamada a la función decorada
# saludar()


def mi_decorador(func):
    def decorada():
        print ("Llamando a la función")
        func()
        print ("Función ejecutada")
    return decorada
@mi_decorador
def saludar():
    print("Hola")

saludar()


# Ejercicio 2: Decorador con argumentos
# Modifica el decorador mi_decorador para que sea capaz de decorar una función con cualquier número de argumentos. 
# (Empieza con 2 argumentos, usando la función sumar(a, b) como ejemplo de función decorada.)
# def mi_decorador(func):
#     # Completa el decorador para aceptar funciones con argumentos
#     pass

# @mi_decorador
# def sumar(a, b):
#     return a + b

# # Llamada a la función decorada
# resultado = sumar(3, 4)
# print(f"Resultado de la suma: {resultado}")

def mi_decorador(func):
    def decorada():
        print ("Llamando a la función")
        resultado = func(3, 4)
        print ("Función ejecutada")
        print(f"Resultado de la suma: {resultado}")
    return decorada
    
@mi_decorador
def sumar(a, b):
    return a + b

sumar()

# Ejercicio 3: Decorador con retorno modificado
# Crea un decorador llamado duplicar_resultado que modifique la función decorada para que su resultado se duplique.
# Usa la función multiplicar(a, b) para probar el decorador.
# def duplicar_resultado(func):
#     # Completa el decorador para duplicar el resultado de la función 
#     pass

# @duplicar_resultado
# def multiplicar(a, b):
#     return a * b

# # Llamada a la función decorada
# resultado = multiplicar(5, 3)
# print(f"Resultado duplicado: {resultado}")

def duplicar_resultado(func):
    def decorada(a,b):
        resultado = func(a,b)
        duplicado = resultado * 2
        print(f"Resultado duplicado: {duplicado}")
        return duplicado
    return decorada
        
@duplicar_resultado
def multiplicar(a, b):
    return a * b

multiplicar(2,3)


# Ejercicio 4: Decorador anidado
# Crea dos decoradores: decorador1 y decorador2. 
# El primero imprimirá "Primero" antes de ejecutar la función decorada, y el segundo imprimirá "Segundo". 
# Luego, aplica ambos decoradores a la función mi_funcion.

def decorador1(func):
    def decorada():
        print ("Primero")
        func()
    return decorada

def decorador2(func):
    def decorada2():
        print ("Segundo")
        func()
    return decorada2

@decorador1
@decorador2
def mi_funcion():
  print("¡Hola desde la función!")


mi_funcion()


# Ejercicio 5: Aplicación práctica (autenticación)
# Imagina que estás desarrollando una aplicación y necesitas controlar el acceso a ciertas funciones 
# según si el usuario está autenticado o no. Crea un decorador llamado requiere_autenticacion que verifique 
# si una variable global usuario_autenticado es True antes de permitir la ejecución de una función. 
# Si el usuario no está autenticado, imprime un mensaje de error.
# usuario_autenticado = False

usuario_autenticado = False

def requiere_autenticacion(func):
    def decorada():
        
        if usuario_autenticado:
            func()
        else:
            print("Usuario no autenticado")
    return decorada

@requiere_autenticacion
def ver_perfil():
    
    print("Perfil del usuario")


ver_perfil()

Simula la autenticación del usuario
# usuario_autenticado = True
# ver_perfil()


# Ejercicio 6: Decorador que limita el tiempo
# Objetivo: Crear un decorador con parámetros que simule un "timeout" o tiempo límite.
# Implementa un decorador llamado timeout(segundos) que limite la ejecución de una función a un máximo de n segundos. Si la función tarda más de ese tiempo en ejecutarse, debe devolver un mensaje como "Tiempo de espera excedido".
# import time

# def timeout(segundos):
#     # Implementa aquí el decorador que limite el tiempo de ejecución
#     pass

# @timeout(3)
# def tarea_larga():
#     time.sleep(5)
#     print("¡Tarea completada!")

# # Llamada a la función decorada
# tarea_larga()

No hay que hacerlo


# Ejercicio 6: Modificar el resultado según un parámetro
# Objetivo: Manipular el resultado de una función con un decorador que acepte parámetros.
# Crea un decorador llamado multiplica_resultado(factor) que multiplique el resultado de la función 
# decorada por un valor dado.

def multiplica_resultado(factor):
    def decoradora(func):
        def decorada():
            resultado =  func()
            print = (f"El resultado es {resultado}")
            return resultado * factor
        return decorada
    return decoradora

@multiplica_resultado(10)
def obtener_numero():
    return 7

# Llamada a la función decorada
print(obtener_numero()) 





