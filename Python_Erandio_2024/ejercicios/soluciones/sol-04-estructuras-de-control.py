# -*- coding: utf-8 -*-

# --------- Ejercicio 1: Condicional simple ---------
numero = int(input("Ingresa un número: "))
if numero > 10:
    print("El número es mayor a 10")
elif numero == 10:
    print("El número es igual a 10")
else:
    print("El número es menor a 10")

%reset -f

# --------- Ejercicio 2: Condicional con elif y else ---------
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
else:
    print("Eres un adulto")

%reset -f

# --------- Ejercicio 3: Bucle while simple ---------
suma = 0
while True:
    numero = int(input("Ingresa un número (negativo para salir): "))
    if numero < 0:
        break
    suma += numero
print(f"Suma total: {suma}")

%reset -f

# --------- Ejercicio 4: Bucle for simple ---------
for i in range(1, 11):
    print(i)

%reset -f

# --------- Ejercicio 5: Uso de break en un bucle ---------
for i in range(1, 11):
    if i == 7:
        break
    print(i)

%reset -f

# --------- Ejercicio 6: Uso de continue en un bucle ---------
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

%reset -f

# --------- Ejercicio 7: Bucle for con else ---------
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("El bucle terminó sin encontrar un break")

%reset -f

# --------- Ejercicio 8: Condicional con operadores lógicos ---------
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 > 0 and numero2 > 0:
    print("Ambos números son positivos")
else:
    print("Hay al menos un número negativo")

%reset -f

# --------- Ejercicio 9: Bucle anidado simple (matriz) ---------
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

%reset -f

# --------- Ejercicio 10: if anidado ---------
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    if numero % 4 == 0:
        print("El número es par y divisible por 4")
    else:
        print("El número es par pero no divisible por 4")
else:
    print("El número es impar")

%reset -f

# --------- Ejercicio 11: Bucle while con validación ---------
contrasena = "1234"
entrada = ""
while entrada != contrasena:
    entrada = input("Introduce la contraseña: ")
print("Acceso concedido")

%reset -f

# --------- Ejercicio Extra 12: Bucle for anidado con condicional ---------
numeros = [6, 4, 9, 12, 15]
for numero in numeros:
    if numero % 2 == 0:
        if numero % 3 == 0:
            print(f"{numero} es divisible por 2 y 3")
        else:
            print(f"{numero} es divisible solo por 2")

%reset -f

# --------- Ejercicio Extra 13: Bucle for anidado: Tablas de multiplicar ---------
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

%reset -f

# --------- Ejercicio Extra 14: Adivina el número ---------
numero_secreto = 8
adivinanza = None
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza < numero_secreto:
        print("El número es muy bajo")
    elif adivinanza > numero_secreto:
        print("El número es muy alto")
print("¡Felicidades! Adivinaste el número")

%reset -f

# --------- Ejercicio Extra 15: Número primo ---------
numero = int(input("Ingresa un número: "))
es_primo = True
if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")

%reset -f

# --------- Ejercicio Extra 16: Bucle for y condicional con listas ---------
palabras = ["python", "bucles", "condicional", "anidado", "ejercicio"]
contador = 0
for palabra in palabras:
    if len(palabra) > 6:
        print(palabra)
        contador += 1
print(f"Palabras con más de 6 letras: {contador}")

%reset -f

