# -*- coding: utf-8 -*-

# --------- Ejercicio 1: Listas ---------
lista = [10, "hola", True, 3.14, [1, 2, 3]]
print("Lista inicial:", lista)

# Añadir un nuevo elemento al final
lista.append("nuevo elemento")
print("Añadir un nuevo elemento:", lista)

# Insertar un elemento en la segunda posición
lista.insert(1, "segundo elemento")
print("Insertar un elemento en la segunda posición:", lista)

# Insertar en la penúltima posición
lista.insert(-1, "penúltimo elemento")

# Eliminar el último elemento
lista.pop() # Por defecto coge el último índice
print("Eliminar el último elemento:", lista)

# Eliminar por índice y recoger el valor eliminado
elemento = lista.pop(1)
print(elemento)

# Acceder al tercer elemento
print("Tercer elemento:", lista[2])

# Clonar la lista y modificar un elemento
copia_lista = lista[:]
copia_lista[0] = "modificado"
print("Lista clonada modificada:", copia_lista)
print("Lista original sin cambios:", lista)

# Extra: Convertir lista de nombres en una cadena de texto separada por comas
nombres = ["Ana", "Juan", "Pedro", "Lucía"]
cadena_nombres = ", ".join(nombres)
print("Cadena de nombres:", cadena_nombres)

%reset -f

# --------- Ejercicio 1.2: Listas avanzadas ---------
# 1. Crear una lista con al menos 6 elementos
lista = [1, 'texto', [3, 4], [True, False], 8.5, 'Python']

# 2. Añadir un nuevo elemento al final
lista.append('nuevo elemento')

# 3. Acceder al segundo elemento de la primera lista anidada y modificarlo
sublista = lista[2] # Creamos un alias para verlo después del del
lista[2][1] = 'modificado'

# 4. Eliminar el tercer elemento de la lista principal
del lista[2]
# del sublista
print(sublista)
lista.insert(2, sublista)

# 5. Clonar la lista con una copia superficial y modificar una lista anidada
lista_copia = lista.copy()
lista_copia[2].append('nuevo en anidada')

# 6. Extra: Unir las listas anidadas en una sola lista plana
lista_unida = lista[2] + lista[3]

%reset -f



# --------- Ejercicio 2: Tuplas ---------
tupla = (5, "Python", False, 8.9, [1, 2, 3])
print("Tupla:", tupla)

# Acceder al primer y último elemento
print("Primer elemento:", tupla[0])
print("Último elemento:", tupla[-1])

# Lanzar error
tupla[1] = "modificado"

# Intentar modificar el segundo elemento (esto fallará)
try:
    tupla[1] = "modificado"
except TypeError as e:
    print(f"Error al intentar modificar la tupla: {e}")

# Desempaquetar los tres primeros elementos
a, b, c = tupla[:3]
print("Desempaquetado:", a, b, c)

# Extra: Convertir la tupla en lista, modificar y volver a tupla
lista_tupla = list(tupla)
lista_tupla.append("nuevo elemento")
tupla_modificada = tuple(lista_tupla)
print("Tupla modificada:", tupla_modificada)

%reset -f

# --------- Ejercicio 2.2: Tuplas avanzadas ---------
# 1. Crear una tupla con una mezcla de tipos, incluyendo una tupla anidada
tupla = (5, 'texto', (3.14, 'anidado'), True, 'Python')

# 2. Acceder al primer elemento de la tupla anidada
primer_anidado = tupla[2][0]

# 3. Convertir la tupla en lista, modificar y volver a tupla
lista_tupla = list(tupla)
lista_tupla[1] = 'modificado'
tupla_modificada = tuple(lista_tupla)

# 4. Intentar eliminar un elemento de la tupla (error explicado)
# Esto generará un error ya que las tuplas son inmutables.

# 5. Extra: Desempaquetar la tupla, incluyendo la anidada
a, b, anidada, d, e = tupla
x, y = anidada

%reset -f

# --------- Ejercicio 3: Diccionarios ---------
diccionario = {"nombre": "Carlos", "edad": 30, "activo": True}
print("Diccionario inicial:", diccionario)

# Añadir una nueva clave-valor
diccionario["ciudad"] = "Madrid"
print("Añadir clave-valor:", diccionario)

# Modificar valor existente
diccionario["edad"] = 31
print("Modificar valor existente:", diccionario)

# Eliminar una clave
diccionario.pop("activo")
print("Eliminar clave:", diccionario)

# Acceder al valor de una clave con .get()
valor = diccionario.get("profesion", "Clave no encontrada")
print("Acceder a clave con .get():", valor)

%reset -f

# --------- Ejercicio 4: Conjuntos ---------
conjunto = {1, 2, 3, "Python", False}
print("Conjunto inicial:", conjunto)

# Añadir un nuevo elemento
conjunto.add("nuevo elemento")
print("Añadir nuevo elemento:", conjunto)

# Intentar añadir un elemento duplicado
conjunto.add(1)
print("Intentar añadir duplicado:", conjunto)

# Eliminar un elemento
conjunto.remove(False)
print("Eliminar elemento:", conjunto)

# Crear otro conjunto con elementos en común
conjunto2 = {2, 3, 4, "Python"}
print("Segundo conjunto:", conjunto2)

# Unión
union = conjunto.union(conjunto2)
print("Unión:", union)

# Intersección
interseccion = conjunto.intersection(conjunto2)
print("Intersección:", interseccion)

# Diferencia
diferencia = conjunto.difference(conjunto2)
print("Diferencia:", diferencia)

# Extra: Diferencia simétrica
diferencia_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferencia simétrica:", diferencia_simetrica)

%reset -f

# --------- Ejercicio 5: Filtrando con Listas y Conjuntos ---------
lista_duplicados = [1, 2, 3, 1, 4, 2]
print("Lista con duplicados:", lista_duplicados)

# Eliminar duplicados convirtiendo en conjunto
conjunto_sin_duplicados = set(lista_duplicados)
print("Conjunto sin duplicados:", conjunto_sin_duplicados)

# Ordenar el conjunto y convertir a lista
lista_ordenada = sorted(conjunto_sin_duplicados)
print("Lista ordenada:", lista_ordenada)

%reset -f

# --------- Ejercicio 6: Diccionarios Anidados ---------
estudiante = { 
    "nombre": "Laura",
    "edad": 22,
    "calificaciones": {"matemáticas": 8.5, "historia": 7.0}
}
print("Diccionario del estudiante:", estudiante)

estudiante.get("nombre", "Sin registrar")
estudiante.get("apellidos", "Sin registrar")
estudiante["nombre"]

calificaciones = estudiante["calificaciones"]
calificaciones["matemáticas"]

# Añadir nueva materia y calificación
estudiante["calificaciones"]["ciencias"] = 9.0
print("Añadir nueva materia:", estudiante)

# Modificar calificación existente
estudiante["calificaciones"]["historia"] = 8.0
print("Modificar calificación:", estudiante)

%reset -f

# --------- Ejercicio 7: Listas de Diccionarios ---------
libros = [
    {"título": "Libro1", "autor": "Autor1", "año": 1990},
    {"título": "Libro2", "autor": "Autor2", "año": 2000},
]
print("Lista de libros:", libros)

# Añadir nuevo libro
libro3 = {"título": "Libro3", "autor": "Autor3", "año": 2010}
libros.append(libro3)
print("Añadir nuevo libro:", libros)

%reset -f

# --------- Ejercicio 8: Operaciones Complejas con Conjuntos ---------
curso1 = {"Ana", "Juan", "Pedro"}
curso2 = {"Juan", "Lucía"}
curso3 = {"Pedro", "Ana", "Lucía"}

# Encontrar usuarios que completaron todos los cursos (intersección)
todos_los_cursos = curso1.intersection(curso2, curso3)
print("Usuarios que completaron todos los cursos:", todos_los_cursos)

# Encontrar usuarios que completaron al menos uno de los cursos (unión)
al_menos_un_curso = curso1.union(curso2, curso3)
print("Usuarios que completaron al menos un curso:", al_menos_un_curso)

%reset -f

# --------- Extra: Te atreves? ---------

# Recorrer una lista
numeros = [10, 20, 30, 40, 50]
for numero in numeros:
    print(f"Número: {numero}")

# Recorrer una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
for fila in matriz:
    for elemento in fila:
        print(elemento)
