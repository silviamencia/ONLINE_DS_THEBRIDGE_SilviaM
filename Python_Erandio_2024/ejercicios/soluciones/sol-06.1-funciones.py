# -*- coding: utf-8 -*-

# --------- Ejercicio 1: Función que devuelve el mayor de dos números ---------
def mayor_de_dos(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

# Prueba la función
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
resultado = mayor_de_dos(n1, n2)
print(f"El mayor número es: {resultado}")


# --------- Ejercicio 2: Función que verifica si un número es divisible entre otro ---------
def es_divisible(n1, n2):
    return n1 % n2 == 0

# Prueba la función
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
resultado = es_divisible(n1, n2)
if resultado:
    print(f"{n1} es divisible entre {n2}")
else:
    print(f"{n1} no es divisible entre {n2}")


# --------- Ejercicio 3: Función que calcula el área de un círculo ---------
import math
def area_circulo(radio):
    return math.pi * radio ** 2

# Prueba la función
radio = float(input("Ingresa el radio del círculo: "))
resultado = area_circulo(radio)
print(f"El área del círculo es: {resultado}")


# --------- Ejercicio 4: Función que calcula el área de un triángulo ---------
def area_triangulo(base, altura):
    return (base * altura) / 2

# Prueba la función
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
resultado = area_triangulo(base, altura)
print(f"El área del triángulo es: {resultado}")


# --------- Ejercicio 5: Función que calcula el área y el perímetro de un círculo ---------
def area_perimetro_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Prueba la función
radio = float(input("Ingresa el radio del círculo: "))
area, perimetro = area_perimetro_circulo(radio)
print(f"El área es: {area}, y el perímetro es: {perimetro}")


# --------- Ejercicio 1 (avanzado): Función que realiza operaciones básicas ---------
def suma(a, b):
    return a + b

# def suma(*valores):
#     # Con *valores recogemos todos los valores pasados en la variable valores
#     # y podemos desempaquetarlos
#     # Si hubiera más valores deberíamos desempaquetar
#     # solo las posiciones que nos interesa valores[0:2]
#     a, b = valores # Desempaquetar
#     return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"
    
def mostrar_menu():
    print("Menú de operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir") 
    
def seleccionar_opcion():
    opcion = -1
    
    while opcion < 1 or opcion > 5:
        try:
            opcion = int(input("Seleccionar opción: "))
            
            if opcion < 1 or opcion > 5:
                print("Opción no válida")
        except KeyboardInterrupt as e:
            print("Aplicación cancelada")
            opcion = 5
        except:
            opcion = -1
            print("Opción no válida")

    return opcion

def recoger_numero_valido(mensaje, mensaje_error = "Número no válido"):
    while True:
        try:
            return float(input(mensaje))
        except:
            print(mensaje_error)

def recoger_numeros():
    a = recoger_numero_valido("Ingresa el primer número: ")
    b = recoger_numero_valido("Ingresa el segundo número: ")
    
    return a, b

def calculadora():
    while True:
        mostrar_menu()
        opcion = seleccionar_opcion()
        
        if opcion != 5:
            a, b = recoger_numeros()
        
        if opcion == 1:
            print(f"Resultado: {suma(a, b)}")
        elif opcion == 2:
            print(f"Resultado: {resta(a, b)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == 4:
            print(f"Resultado: {division(a, b)}")
        elif opcion == 5:
            print("Saliendo de la aplicación")
            break
        else:
            print("Opción inválida")
        
        print()

# Prueba la función
calculadora()


# --------- Ejercicio 2 (avanzado): Función que determina si un número es primo ---------
def es_primo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Prueba la función
n = int(input("Ingresa un número: "))
if es_primo(n):
    print(f"{n} es un número primo")
else:
    print(f"{n} NO es un número primo")

