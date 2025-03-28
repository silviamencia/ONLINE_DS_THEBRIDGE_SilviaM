# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:44:39 2024

@author: LANER
"""

# Crear una función que reciba 2 números y devuelva el mayor de ellos

def numero_mayor ():
    numero1 = int(input("Introduce primer número:  ")) 
    numero2 = int(input("Introduce segundo número: "))
    if numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}")
        return numero1
    else:
        print("numero2 es mayor que numero1")
        return numero2
        
numero_mayor()

# Crea una fución que reciba 2 números y que compruebe si el primero es divisible por 2        
        
# Función que pida radio del círculo y devuelva el área  
# Área de un círculo = π r²

def area_circulo (r):
    pi = 3.1415
    area = pi * r * r
    print("El área es: ", {area})
       
area_circulo(25)


def area_circulo ():
    pi = 3.1415
    r = float (input("Mete el radio:  "))
    area = pi * r ** 2
    print("El área es: ", {area})
    return area

area_circulo()

#Área de un triangulo

def area_triangulo ():
    a = float (input ("Mete la altura: "))
    b = float (input("Mete la base: "))
    area =  a * b / 2
    print("El área del triángulo es", {area})
    return (area)

area_triangulo()

#Crear una función que reciba el radio de un círculo y devuelva el área y el perímetro.
from math import pi
def perimetro_area():
    r = float (input("Mete el radio:  "))
    area = pi * r ** 2
    perimetro = 2 * pi * r
    print("El área y perímetro son", {area},{perimetro})
    return (area, perimetro)

#Reutilizo la función area_circulo pero haciendo cambio, pidiendo que a parte de devolverme
#el área, me devuelva el radio para poder usarlo en la siguiente función.

def area_circulo ():
    pi = 3.1415
    r = float (input("Mete el radio:  "))
    area = pi * r ** 2
    print("El área es: ", {area})
    return (area, r)
    
    
perimetro_area()

def perimetro():
    #r = float (input("Mete el radio:  "))
    area, r = area_circulo()
    perimetro = 2 * pi * r
    print("El área y perímetro son", {area},{perimetro})
    return(area, perimetro)
    
perimetro()

# Crea una función que pueda realizar operaciones básicas como suma, resta, multiplicación y división. 
# Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.
# Utiliza funciones separadas para cada operación.

def insert_numeros():
    numero1 = float(input("Meta un numero:  "))
    numero2 = float(input("Meta otro número:  "))
    return numero1, numero2
    print({numero1, numero2})
    
def suma(tupla):
    numero1, numero2 = tupla
    sum = numero1 + numero2
    return sum
    
def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion (numero1, numero2):
    return numero1 * numero2

def division (numero1, numero2):
    return numero1 / numero2

def opciones ():
    #operacion = 0
    print("Menu.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Salir")
    operacion = int(input("Selecciona una operación: "))
    return operacion

def calculadora():
    while True:
        operacion = opciones()
        print ({operacion})
    
        if operacion == 1:
           return suma(insert_numeros())
        elif operacion == 2:
            return resta(*insert_numeros())
        elif operacion == 3:
            return multiplicacion(*insert_numeros())
        elif operacion == 4:
            return division(*insert_numeros())
        elif operacion == 5:
            print("Saliendo de la aplicación")
            break
        else:
            print("Operación no válida")
    
    calculadora()
    
# Escribe una función que determine si un número dado es primo o no. 
# Pedirá al usuario que ingrese un número y muestra un mensaje indicando si es primo o no.


def es_primo(numero):
  if numero < 2:
    return False
    
  for i in range (2, numero):
     if (numero % i) == 0:
        return False
        
  return True

el_numero_es_primo = es_primo(6)
if el_numero_es_primo:
    print("El número es primo")
else:
    print("El número NO es primo")
    
    
# Ejercicios Funciones
# Ejercicio 1: Función para verificar si una lista está ordenada
# Objetivo: Escribe una función que reciba una lista de números y determine si la lista está ordenada 
# de menor a mayor.
# Descripción:
# La función debe recibir una lista de números y devolver True si los números están en orden ascendente,
# y False en caso contrario. Si la lista tiene solo un elemento o está vacía, se considera que está 
# ordenada. No puedes usar la función sorted() ni ninguna función de Python que ordene listas directamente.
# Instrucciones:
# Utiliza un bucle for para recorrer la lista.
# En cada iteración del bucle, compara si el número actual es menor o igual al siguiente número.
# Si en algún momento encuentras un número mayor que el siguiente, la lista no está ordenada, 
# por lo que deberías retornar False inmediatamente.
# lista = [1, 2, 3, 4, 5]
# print(verificar_orden(lista))  # Salida esperada: True

# lista2 = [3, 2, 1]
# print(verificar_orden(lista2))  # Salida esperada: False


def insertar_lista_numeros(numero_de_valores):
    lista=[]
    
    for n in range (0, numero_de_valores):
        numero_nuevo = int(input("Introduce un número"))
        lista.append(numero_nuevo)
    
    return lista
    
    
lista = insertar_lista_numeros(5)    
# lista = insertar_lista_numeros()

def ordenar_lista():
    # Recoger lista
    lista = insertar_lista_numeros(5)
    
    # Comprobar si es ascendente
    es_ascendente = True
    n = len (lista)
    for i in range (1, n):
        if lista[i - 1] > lista[i]:
            es_ascendente = False
            break
         
    # Mostrar mensaje
    if es_ascendente == True:
        print ("la lista es ascendente")
    else:
        print ("la lista no es ascendente")
    
       # else:
       # print ("la lista no es ascendente")

ordenar_lista()
     
                   
        
     

# Ejercicio 2: Función para calcular el precio final con impuestos y descuentos
# Objetivo: Escribe una función llamada calcular_precio_final que calcule el 
# precio final de un producto aplicando un impuesto y un descuento opcional.
# Descripción:
# La función debe recibir los siguientes parámetros:
# precio (obligatorio): el precio base del producto.
# impuesto (nombrado, con valor por defecto del 21%): el porcentaje de impuestos 
# que se aplicarán al precio base.
# descuento (nombrado, con valor por defecto de 0): un descuento opcional que 
# se aplicará al precio después de añadir los impuestos.
# La función debe devolver el precio final después de aplicar los impuestos y 
# restar el descuento. 
# El cálculo sigue estos pasos:
# Se aplica el impuesto al precio base.
# Si hay un descuento, se resta del precio con impuestos.
# Si no hay descuento, se retorna el precio con los impuestos aplicados.
# Instrucciones: 
# La función debe usar parámetros nombrados con valores por defecto para el 
# impuesto y el descuento.
# Usa estructuras condicionales para verificar si se debe aplicar el descuento

# Se define el precio base
def precio_base ():
    precio_base = float(input("Introduzca el precio base: "))
    return precio_base
precio_base()
# Se define el impuesto
def impuesto ():
    impuesto_defecto = 0.21
    tasa = float(input("Cuál es el impuesto:  "))
    if tasa > 0.21:
        return tasa
    else:
        return impuesto_defecto

impuesto()
        
    

# Descuento aplicado
def descuento ():
    descuento = 0
    descuento = float(input("Indica descuento:"))
    if descuento > 0:
        return descuento
    return descuento    
   descuento() 
    
# Cálculo del precio final
def calculo_precio_final ():
    impuesto_final = impuesto()
    descuento_final = descuento()
    
    if descuento_final > 0:
        precio_final = precio_impuesto()-descuento()
    else:
        precio_final = precio_impuesto
    
  calculo_precio_final()  
    
    
    

