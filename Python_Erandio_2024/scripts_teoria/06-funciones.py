# -*- coding: utf-8 -*-

#############
# FUNCIONES #
#############

"""
**¿Qué es una función en Python?**

Una función en Python es un bloque de código reutilizable que realiza una tarea 
específica. 
Puedes pensar en una función como una especie de máquina que toma ciertos 
valores de entrada, realiza un conjunto de acciones con esos valores y 
luego devuelve un resultado. 

Las funciones son una parte fundamental de la programación porque nos permiten 
dividir nuestro código en partes más pequeñas y manejables, lo que facilita la 
lectura, la depuración y la reutilización del código.

**¿Por qué son importantes las funciones?**

Las funciones son importantes por varias razones:

1. **Reutilización de código:** Puedes escribir una función una vez y usarla 
muchas veces en tu programa. Esto ahorra tiempo y evita la repetición de código.

2. **Facilitan la lectura:** Dividir tu programa en funciones más pequeñas hace 
que sea más fácil de entender y mantener. Cada función se enfoca en una tarea 
específica.

3. **Modularidad:** Las funciones permiten dividir un programa en módulos más 
pequeños, lo que facilita el desarrollo colaborativo. Diferentes programadores 
pueden trabajar en funciones diferentes.

4. **Depuración:** Si tienes un error en tu programa, las funciones te ayudan a 
aislar y solucionar problemas más fácilmente, ya que puedes probar cada función 
por separado.
"""

# Las funciones pueden requerir argumentos o no
def dime_algo():
    print("Algo")


# Aunque no haya argumentos los paréntesis son obligatorios para que se ejecute
dime_algo
dime_algo()
variable = dime_algo()
type(variable)

# Los argumentos son tuplas que contienen los datos que se van a utilizar en el bloque de la función. Sus elementos van entre paréntesis.
def dime(mensaje):
    mensaje = mensaje.upper()
    print(mensaje)
    return mensaje

dime("Buenos días")
dime("Buenas tardes")

# Las funciones pueden devolver un valor o no
# Las funciones anteriores no devuelven ningún valor
resultado = dime("Buenos días")
# resultado es un objeto NoneType. Es decir, no es nada
type(resultado)

# Creamos una funcion que sume + 1 y devuelva el valor.
def suma1(x):
    y = x + 1
    return y

suma1("34")
type(suma1(34))
saludo_may = dime(str(34))
# El resultado se devuelve en la consola porque es el comportamiento de spyder,
# pero lo normal es guardarlo para usarlo después...
resultado = suma1(233.4)

resultado*2


# Función para comprobar si un número es par o impar
def es_par(num):
    comprobacion = num % 2 == 0
    return comprobacion


# Puedo ver el "return"
es_par(124)
es_par(1987)
# o guardarlo
paridad = es_par(124)

lista_numeros = [1,2,3,5,4,4,8]
lista_paridad = []
for numero in lista_numeros:
    lista_paridad.append(es_par(numero))

# El valor devuelto puede ser utilizado sin ser guardado.
def imprime_si_es_par(num):
    if es_par(num):
        print("Es par")
    else:
        print("Es impar")
    return es_par(num)


def es_par_lista(lista_num):
    lista_paridad = []
    for numero in lista_num:
        lista_paridad.append(imprime_si_es_par(numero))
    return lista_paridad

lista_paridad = es_par_lista(lista_numeros)


imprime_si_es_par(129)

def suma1_doc(x: (float, int)) -> (float, int):
    """
    Suma una unidad al parámetro recibido
    """
    y = x + 1
    return y

suma1_doc(30)


# Función para comprobar si un número es par o impar
def es_par_doc(num: int) -> bool:
    """
    Entrada: num, número entero positivo. 
    Devuelve True si el número es par, 
    de otra manera devuelve False.
    """
    return num % 2 == 0

es_par_doc(12.0)

# Función para multiplicar con dos argumentos
# En lugar de multiplicar, estamos sumando 'a', 'b' veces
def multiplicacion(a, b):
    resultado = 0
    while b > 0:
        resultado = resultado + a
        print(resultado, b)
        b = b - 1
    return resultado

# Devolviendo el valor en Out
multiplicacion(5, 80)
# Guardando el valor
valor = multiplicacion(5, 20)
valor

if type(valor) == int or type(valor) == float:
    print("Es un número")

if isinstance(valor, (float, int)):
    print("Es un número")

# Crear una función que reciba dos números y devuelva el mayor de ellos.

def devuelve_mayor(num1, num2):
    if num1 > num2:
        salida = num1
        print(num1)
    else:
        salida = num2
        print(num2)
    return salida

def devuelve_menor(num1, num2):
    if num1 < num2:
        salida = num1
        print(num1)
    else:
        salida = num2
        print(num2)
    return salida



numero_grande = 10
numero_pequeno = 1
devuelve_mayor(numero_grande, numero_pequeno)

# Ejercicio: Crear una función que reciba dos parámetros y 
# que compruebe si el primer número es divisible entre el segundo
def divisible(numerador, denominador):
    if denominador == 0:
        salida = False
    else:
        salida = numerador % denominador == 0
    return salida

divisible(8.0, 2.0)


def divisible(numerador, denominador):
    mayor = devuelve_mayor(numerador, denominador)
    menor = devuelve_menor(numerador, denominador)
    if menor == 0:
        salida = False
    
    elif not isinstance(mayor, (float, int)) or not isinstance(menor, (float, int)):
        print("No vale meter otra cosa que números")
        salida = False
    
    elif (mayor % menor) == 0:
        salida = True
    else:
        salida = False
    return salida

divisible(2, 8)

# Recordemos que esto es True:
0 == 0.0
True==1.0
True==1
0.0 == False
0 == False

True/5

# ÁREA DE UN CÍRCULO
from math import pi as PI

def area_circ():
    radio = float(input("Introduce el radio: "))
    area = PI * radio**2
    print("El área es", area)
    return area, radio
  
def area_circ2(radio):
    return PI * radio**2

area_circ()

def area_tri():
    altura = float(input("Introduce la altura: "))
    base = float(input("Introduce la base: "))
    area = base*altura/2
    return area
area_tri()

def area_tri2(altura,base):
    area = base*altura/2
    return area

alto = 3
abajo = 5
area_tri2(alto, abajo)


def datos_circ():
    area, radio = area_circ()
    perimetro = 2 * PI * radio
    return area, perimetro

area, longitud = datos_circ()
datos_circ()

# Se ejecutará así:
es_divisible = divisible(30.0, 0)
30.0 % 5

##################################################################
# Parámetros posicionales y parámetros con nombre en una función #
##################################################################

# Función que devuelve el valor de una ecuación de 2ºgrado

def evaluar_cuadratica(a, b, c, x):
    '''
    a, b, c: valores numéricos de los coeficientes de una ecuación
    de segundo grado
    x: valor de la variable x.
    '''
    solucion = a*x*x+b*x+c
    return solucion

evaluar_cuadratica(2, 2, 3, 8)  # f(x=8) = 2x² + 2x + 3

# El problema de invocar esta función así es que
# tengo que acordarme del orden de los coeficientes
evaluar_cuadratica(a = 2, b = 2, c = 3, x = 8)
evaluar_cuadratica(x = 8, c = 3, a = 2, b = 2)

# Así sí
evaluar_cuadratica(2, 2, x=8, c=3)

# Así no
# evaluar_cuadratica(a=2, 2, 3, 8)
# Siempre los keyword arguments AL FINAL

# Si quiero forzar que los argumentos sólo puedan introducirse por clave-valor
# puedo reescribir la función así (Sólo cambia el asterisco en los parámetros):
def evaluar_cuadratica(*, a, b, c, x):
    '''
    a, b, c: valores numéricos de los coeficientes de una ecuación
    de segundo grado
    x: valor de la variable x.
    '''
    solucion = a*x*x+b*x+c
    return solucion

# Si intentamos introducir ahora un argumento posicional obtendremos:
"""TypeError: evaluar_cuadratica() takes 0 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given"""
# Error:
evaluar_cuadratica(2, 2, 3, 8)
# Correcto:
evaluar_cuadratica(x = 8, c = 3, a = 2, b = 2)


# ¿Y si quiero calcular f(8) siendo f = x²+3?
evaluar_cuadratica(a=1, c=3, x=8)


# A los coeficientes puedo darles un valor "por defecto"
# Pero los argumentos sin valor por defecto deben ir ANTES que los otros
def evaluar_cuadratica_incompleta( x, a = 0, b = 0, c = 0):
    '''
    a, b, c: valores numéricos de los coeficientes de una ecuación
    de segundo grado
    x: valor de la variable x.
    '''
    solucion = a*x*x+b*x+c
    return solucion

evaluar_cuadratica_incompleta(8, 2, 2, 3)
evaluar_cuadratica_incompleta() # Incorrecto. Falta x
evaluar_cuadratica_incompleta(3)
# Si quiero dar el valor x en otra posición debo añadirlo con nombre
evaluar_cuadratica_incompleta(a=1, c=3, x=8)
evaluar_cuadratica_incompleta(a=2, b=2, c=3, x=8)
evaluar_cuadratica_incompleta(8, 2, 2, 3)

evaluar_cuadratica_incompleta(3, b=2)


###########################
#    *args y **kwargs     #
###########################
# ¿Y si no sé el número de parámetros posicionales que voy a meter?
def imprime_lineas(primera_linea, *resto_lineas):
    print(primera_linea.upper())
    for linea in resto_lineas:
        print(linea.capitalize())

imprime_lineas("Puedo imprimir", "las líneas", "que quiera", "fin")
imprime_lineas("Hola")
imprime_lineas()


def imprime_lineas(*args):
    for linea in args:
        print(linea.capitalize())
        
imprime_lineas("Puedo imprimir", "las líneas", "que quiera", "fin")
imprime_lineas("Hola")
imprime_lineas()

# Podría hacerlo con una lista
def imprime_lineas_con_lista(primera_linea, resto_lineas):
    print(primera_linea.upper())
    for linea in resto_lineas:
        print(linea.capitalize())

lista_a_imprimir = ("Puedo imprimir", "las líneas", "que quiera")
imprime_lineas_con_lista(lista_a_imprimir)

imprime_lineas_con_lista("Puedo imprimir", ("las líneas", "que quiera"))

# Si los parámetros se introducen por clave-valor
def imprime_lineas2(**argumentos_por_clave):
    for clave, valor in argumentos_por_clave.items():
        print(f'{clave}= {valor}')

dicc = {"a": 0, "b":1}
dicc.items()

imprime_lineas2(nombre='Juan', edad=30, ciudad='Madrid', calle = "calle")

# Esto podríamos haberlo hecho con un diccionario

def imprime_lineas_con_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f'{clave}= {valor}')
  
# Usando un diccionario ya existente
diccionario = {"nombre":'Juan', "edad":30, "ciudad":'Madrid'}
imprime_lineas_con_diccionario(diccionario)
# Creando el diccionario en la llamada a la función
imprime_lineas_con_diccionario({"nombre":'Juan', "edad":30, "ciudad":'Madrid'})

###########################################
# Ejercicios de funciones hechos en clase #
###########################################

# 1. Calculadora Simple:
"""
Crea una función que pueda realizar operaciones básicas como suma, resta, 
multiplicación y división. 
Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.

Utiliza funciones separadas para cada operación.
"""

def suma(tupla):
    num1, num2 = tupla
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def pide_opcion():
    print("""
          1: Sumar
          2: Restar
          3: Multiplicar
          4: Dividir
          s: Salir     
          """)
    opcion = input("Elige una opción: ")
    return opcion

def pide_numeros():
    num1 = float(input("Introduzca el primer número: "))
    num2 = float(input("Introduzca el segundo número: "))
    return num1, num2

def calculadora():
    while True:
        opcion = pide_opcion()
        if opcion == "1":
            return suma(pide_numeros())
        elif opcion == "2":
            return resta(*pide_numeros())
        elif opcion == "3":
            return multiplica(*pide_numeros())
        elif opcion == "4":
            return divide(*pide_numeros())
        elif opcion == "s":
            print("Adios")
            break
        else:
            print("Opción inválida")

calculadora()



# 2. Número Primo:
"""
Escribe una función que determine si un número dado es primo o no. 
Pedirá al usuario que ingrese un número y muestra un mensaje 
indicando si es primo o no.
"""