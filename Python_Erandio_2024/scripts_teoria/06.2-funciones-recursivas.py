# -*- coding: utf-8 -*-

#############
# FUNCIONES #
#############

"""
La función iterativa usa un bucle para hacer el mismo trabajo que la recursiva, 
calculando el resultado a medida que avanza por cada iteración del bucle.

Ejemplo:
"""
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Prueba
numero = 5
resultado = factorial_iterativo(numero)
print(f"Factorial iterativo de {numero} es: {resultado}")


"""
La función recursiva llama a sí misma hasta que alcanza una condición base, 
y luego vuelve "resolviendo" el problema desde el último llamado hasta 
el primero.

Visualizarlo al principio puede ser complejo, este vídeo expone un ejemplo
de manera visual: https://youtu.be/YwRjEOFxvO0?si=AcElgzg9GeZZPYUM

Ejemplo:
"""
def factorial_recursivo(n):
    # Condición base
    if n == 0:
        return 1
    else:
        # Llamada recursiva
        return n * factorial_recursivo(n - 1)

# Prueba
numero = 5
resultado = factorial_recursivo(numero)
print(f"Factorial recursivo de {numero} es: {resultado}")


"""
Comparación:
- Recursiva: 
    Es más elegante y concisa, pero si el valor de n es muy grande, 
    puede resultar en un error de "recursión máxima" (RecursionError), 
    ya que Python limita la cantidad de llamadas recursivas que puede manejar.
- Iterativa: 
    Generalmente es más eficiente en cuanto a uso de memoria y no tiene 
    el riesgo de alcanzar el límite de recursión, pero puede resultar más 
    difícil de leer en problemas complejos.

Por lo general, una lógica iterativa es mejor que la recursiva.
"""