# -*- coding: utf-8 -*-

# --------- Listas ---------
%reset -f

# Una lista es una colección ordenada y modificable de elementos
lista = [1, 2, "Python", True, 3.14]

# Añadir elementos
lista.append("nuevo_elemento")  # Añade al final
lista.insert(1, "en_medio")     # Inserta en la posición 1

# Acceder a elementos
primer_elemento = lista[0]  # Primer elemento
segundo_elemento = lista[1]  # Segundo elemento
ultimo_elemento = lista[-1]  # Último elemento

# Modificar elementos
lista[0] = 100  # Cambia el primer elemento de 1 a 100
lista[2] = "Python Avanzado"  # Modifica un elemento de texto

# Eliminar elementos
lista.remove("nuevo_elemento")  # Elimina por valor
elemento_eliminado = lista.pop(2)  # Elimina por índice y lo guarda
del lista[0]  # Elimina el primer elemento

# Slicing: Extraer una parte de la lista (sublista)
sublista = lista[1:3]  # Extraer del índice 1 al 2 (el 3 no se incluye)

# Clonar la lista (copiarla completamente)
copia_lista = lista[:]  # Copia superficial
copia_lista[0] = "Modificado en la copia"  # Modificar en la copia

# Mostrar diferencias entre la lista original y la copia
print("Lista original:", lista)
print("Copia modificada:", copia_lista)

# Convertir lista a cadena de texto (usando solo elementos de texto)
lista_textos = ["Daniel", "Nahikari", "Borja"]
cadena = ", ".join(lista_textos)
print("Lista convertida a cadena:", cadena)

# Convertir lista en tupla
lista_a_tupla = tuple(lista)
print("Lista convertida a tupla:", lista_a_tupla)

# Convertir lista en conjunto (elimina duplicados si hay)
lista_a_conjunto = set(lista)
print("Lista convertida a conjunto:", lista_a_conjunto)


# --------- Tuplas ---------
%reset -f

# Las tuplas son colecciones ordenadas e inmutables
tupla = (1, 2, "Python", True, 3.14)

# Acceder a elementos
primer_tupla = tupla[0]
ultimo_tupla = tupla[-1]

# Desempaquetar tupla
a, b, c = tupla[0:3]  # Extraer los tres primeros elementos

# Conversión de tupla a lista para modificarla
lista_desde_tupla = list(tupla)
lista_desde_tupla.append("nuevo_elemento")
tupla_modificada = tuple(lista_desde_tupla)

# Clonar una tupla
copia_tupla = tupla[:]  # Se clona igual que una lista

# Convertir tupla en lista
tupla_a_lista = list(tupla)
print("Tupla convertida a lista:", tupla_a_lista)

# Convertir tupla en conjunto (elimina duplicados)
tupla_a_conjunto = set(tupla)
print("Tupla convertida a conjunto:", tupla_a_conjunto)


# --------- Diccionarios ---------
%reset -f

# Los diccionarios almacenan pares clave-valor
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Añadir o modificar elementos
diccionario["profesión"] = "Ingeniero"  # Añadir un nuevo par clave-valor
diccionario["edad"] = 26  # Modificar un valor existente

# Acceder a valores
nombre = diccionario["nombre"]
profesion = diccionario.get("profesión", "No especificada")

# Eliminar elementos
del diccionario["ciudad"]
profesion_eliminada = diccionario.pop("profesión", "No especificada")  # Elimina y guarda el valor

# Alias y clonación
alias_diccionario = diccionario  # Alias
copia_diccionario = diccionario.copy()  # Clonación superficial

# Modificación de la copia sin afectar al original
copia_diccionario["nombre"] = "Carlos"
print("Diccionario original:", diccionario)
print("Diccionario copiado y modificado:", copia_diccionario)


# --------- Conjuntos ---------
%reset -f

# Los conjuntos son colecciones no ordenadas de elementos únicos
conjunto = {1, 2, 3, "Python", True}

# Añadir elementos
conjunto.add(4)

# Eliminar elementos
conjunto.discard(1)  # No lanza error si el elemento no existe
conjunto.discard("Elemento que no está")  # No hace nada si no está presente

# Operaciones de conjuntos
conjunto2 = {3, 4, 5}

# Unión: Todos los elementos de ambos conjuntos
union = conjunto.union(conjunto2)

# Intersección: Elementos comunes en ambos conjuntos
interseccion = conjunto.intersection(conjunto2)

# Diferencia: Elementos en el primer conjunto que no están en el segundo
diferencia = conjunto.difference(conjunto2)

# Diferencia simétrica: Elementos que están en uno u otro conjunto pero no en ambos
diferencia_simetrica = conjunto.symmetric_difference(conjunto2)

# Alias y clonación
alias_conjunto = conjunto  # Alias
copia_conjunto = conjunto.copy()  # Clonación superficial

# Modificación en la copia
copia_conjunto.add(10)
print("Conjunto original:", conjunto)
print("Conjunto copiado y modificado:", copia_conjunto)

# Convertir conjunto en lista
conjunto_a_lista = list(conjunto)
print("Conjunto convertido en lista:", conjunto_a_lista)

# Convertir conjunto en tupla
conjunto_a_tupla = tuple(conjunto)
print("Conjunto convertido en tupla:", conjunto_a_tupla)


# --------- Listas Anidadas ---------
%reset -f

# Las listas anidadas son listas que contienen otras listas como elementos
lista_anidada = [
    [1, 2, 3],        # Primera sublista
    [4, 5, 6],        # Segunda sublista
    [7, 8, 9]         # Tercera sublista
]

# Acceder al primer elemento de la lista anidada
primer_elemento_lista = lista_anidada[0]  # [1, 2, 3]

# Acceder a un elemento dentro de la sublista
elemento_anidado = lista_anidada[0][1]  # Segundo elemento de la primera sublista -> 2

# Modificar un elemento dentro de una sublista
lista_anidada[1][2] = 60  # Cambia el tercer elemento de la segunda sublista de 6 a 60

# Añadir una nueva sublista
lista_anidada.append([10, 11, 12])

print("Lista anidada modificada:", lista_anidada)


# --------- Diccionarios Anidados ---------
%reset -f

# Los diccionarios anidados son diccionarios que contienen otros diccionarios como valores
diccionario_anidado = {
    "estudiante1": {
        "nombre": "Juan",
        "edad": 21,
        "cursos": ["Matemáticas", "Historia"]
    },
    "estudiante2": {
        "nombre": "Ana",
        "edad": 22,
        "cursos": ["Biología", "Química"]
    }
}

# Acceder a un diccionario dentro de otro diccionario
info_estudiante1 = diccionario_anidado["estudiante1"]  # Diccionario del primer estudiante

# Acceder a un valor dentro de un diccionario anidado
nombre_estudiante1 = diccionario_anidado["estudiante1"]["nombre"]  # "Juan"

# Añadir un nuevo campo al diccionario de un estudiante
diccionario_anidado["estudiante1"]["calificación"] = 8.5

# Añadir un nuevo estudiante al diccionario principal
diccionario_anidado["estudiante3"] = {
    "nombre": "Luis",
    "edad": 23,
    "cursos": ["Física", "Geografía"]
}

# Modificar un valor dentro del diccionario anidado
diccionario_anidado["estudiante2"]["edad"] = 23  # Cambia la edad de Ana

print("Diccionario anidado modificado:", diccionario_anidado)

# Acceder a un curso de un estudiante dentro del diccionario
curso_estudiante2 = diccionario_anidado["estudiante2"]["cursos"][0]  # Primer curso de Ana -> "Biología"

