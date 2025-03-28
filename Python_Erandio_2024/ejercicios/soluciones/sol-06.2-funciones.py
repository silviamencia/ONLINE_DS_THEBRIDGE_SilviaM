# -*- coding: utf-8 -*-

# --------- Ejercicio 1: Verificar si una lista está ordenada ---------
def verificar_orden(lista):
    if len(lista) <= 1:
        return True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Pruebas de la función
lista = [1, 2, 3, 4, 5]
print(f"¿La lista {lista} está ordenada? {verificar_orden(lista)}")  # Salida esperada: True

lista2 = [3, 2, 1]
print(f"¿La lista {lista2} está ordenada? {verificar_orden(lista2)}")  # Salida esperada: False

# %reset -f

# --------- Ejercicio 2: Calcular el precio final con impuestos y descuentos ---------
def calcular_precio_final(precio, impuesto=21, descuento=0):
    # Calcular el precio con impuestos
    precio_con_impuesto = precio + (precio * (impuesto / 100))
    
    # Aplicar descuento si es mayor que 0
    if descuento > 0:
        precio_final = precio_con_impuesto - descuento
    else:
        precio_final = precio_con_impuesto

    return precio_final

# Ejemplo 1: Pasando todos los argumentos
precio1 = 100
impuesto1 = 10
descuento1 = 5
precio_final1 = calcular_precio_final(precio1, impuesto=impuesto1, descuento=descuento1)
print(f"Ejemplo 1 -> Precio base: {precio1}, Impuesto: {impuesto1}%, Descuento: {descuento1} -> Precio final: {precio_final1}")

# Ejemplo 2: Pasando solo el precio (se usarán los valores por defecto para impuesto y descuento)
precio2 = 150
precio_final2 = calcular_precio_final(precio2)
print(f"Ejemplo 2 -> Precio base: {precio2} -> Precio final con impuesto por defecto (21%) y sin descuento: {precio_final2}")

# Ejemplo 3: Pasando el precio y el impuesto (sin descuento)
precio3 = 200
impuesto3 = 15
precio_final3 = calcular_precio_final(precio3, impuesto=impuesto3)
print(f"Ejemplo 3 -> Precio base: {precio3}, Impuesto: {impuesto3}% -> Precio final: {precio_final3}")

# Ejemplo 4: Pasando el precio y un descuento (usando el impuesto por defecto)
precio4 = 80
descuento4 = 10
precio_final4 = calcular_precio_final(precio4, descuento=descuento4)
print(f"Ejemplo 4 -> Precio base: {precio4}, Descuento: {descuento4} -> Precio final con impuesto por defecto (21%): {precio_final4}")

# %reset -f