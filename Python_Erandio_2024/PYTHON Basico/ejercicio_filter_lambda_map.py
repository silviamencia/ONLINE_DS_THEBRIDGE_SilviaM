# -*- coding: utf-8 -*
#___________#
# Ejercicio #
#-----------#
# Crear una lista con los números de 0 al 100.
# Dividirlos entre tres con map y una función lambda.
# Filtrar los que tienen parte decimal con una función lambda.

#map(una_funcion, una_lista)
#lambda parámetros: expresión

lista = list(range(1, 101, 1))
divisor = 3
lista_2 = list(map(lambda x: x/divisor, lista))


lista_sin_decimales = list(filter(lambda x == float , lista_2)


filter(function, iterable)
map(function, iterable)

#___________#
# Ejercicio #
#-----------#
# Creamos una lista de edades que por error contiene números negativos y excesivos
import random
edades = [random.randint(-7, 130) for i in range(500)]
edades.count(-3)
edades.count(121)

def filtrado(edad):
    if edad < 0 or edad > 120:
            return False
    else:
        return True
filtrado(-2)

# Usar filter para eliminar los valores            
    
lista_limpia = list(filter(filtrado, edades))

# Usar map para sustituirlos por 120 o 0

def filtrado2(edad):
    if edad < 0:
       return 0
    elif edad > 120:
        return  100
    else:
        return edad
        

lista_sustituida = list(map(filtrado2, lista_limpia))

