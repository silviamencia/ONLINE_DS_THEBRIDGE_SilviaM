# -*- coding: utf-8 -*-
"""t  9 14:42:57 2024

@author: LANER
"""
#Ejercicios Estructura de Datos
##Ejercicio 1
%reset -f
lista1=[True, False,"Amigo",0.25]
lista1.append("el viento")
print(lista1)
lista1.insert(1,25)
lista1.pop()
lista1.pop(3)
import copy as cp
lista2=cp.copy(lista1)
print(lista2)
lista2[0]=False

#Extra
lista2=["Ana","Belen","Catalina"]
lista3=",".join(lista2)
print(lista3)

# Ejercicio 1.2: Listas avanzadas (Python)
# Crea una lista en Python con al menos 6 elementos, donde al menos dos de esos elementos sean otras listas.
# Añade un nuevo elemento al final de la lista.
# Accede al segundo elemento de la primera lista anidada y modifícalo.
# Elimina el tercer elemento de la lista principal usando su índice.
# Clona la lista con una copia superficial usando copy() y luego intenta modificar una de las listas anidadas en la copia. Explica por qué la modificación afecta tanto a la copia como a la lista original.
# Extra: Une todas las listas anidadas en una sola lista plana (sin utilizar estructuras de control ni funciones avanzadas).

lista2=[True,False,["Sr","Sra"],["Pedro","Maria","Ana"],25,0.25]
lista2.append(35)
print(lista2)
lista2[2][1] = "Srta"
lista2.pop(2)
import copy as cp
lista3=cp.copy(lista2)
print(lista3)
lista3[2][2]="Domingo"
# lista4=lista3[2]
# print(lista4)
# lista5=",".join(lista4)
# print(lista5)
# lista6=

sublista = lista3[2]
sublista_unida = ", ".join(sublista)
lista3[2] = sublista_unida

##Ejercicio 2: Tuplas
# Crea una tupla con 5 elementos de cualquier tipo.
# Accede al primer y al último elemento de la tupla.
# Intenta modificar el segundo elemento y observa el resultado (explicar por qué no es posible).
# Desempaqueta los tres primeros elementos de la tupla en tres variables.
# Extra: Convierte la tupla en una lista, añade un nuevo elemento y vuelve a convertirla en tupla.

tupla1=(True,"Amigo",3,["Pepe", "Pili"])
print(tupla1[0],tupla1[3])
variable1, variable2, variable3=tupla1[0:3]
print(variable1, variable2, variable3)
lista=list(tupla1)
print(lista)
lista.append("hace viento")
print(lista)
tupla2=tuple(lista)
print(tupla2)



# Ejercicio 2.2: Tuplas avanzadas (Python)
# Crea una tupla en Python que contenga una mezcla de tipos, incluyendo otra tupla anidada.
# Accede al primer elemento de la tupla anidada.
# Convierte la tupla principal en una lista, modifica el segundo elemento, luego vuelve a convertirla en tupla.
# Intenta eliminar el último elemento de la tupla original y explica el resultado.
# Extra: Desempaqueta la tupla en variables, incluyendo la tupla anidada como una variable única, y luego desempaqueta la tupla anidada en variables por separado.

Tupla = (True,"Amigo",3,["Pepe", "Pili"])
Tupla[0]
Lista= list(Tupla)
Lista[2] = 5
Tupla_convertida = tuple(Lista)
Tupla_convertida_quitarultimoelemento= Tupla_convertida.pop()
variable1, variable2, variable3, variable4 = Tupla_convertida [0:4]
variable_desanidada = ",".join(variable4)
print(variable_desanidada)

# Ejercicio 3: Diccionarios
# Crea un diccionario con tres pares clave-valor. Usa cadenas de texto como claves y valores de diferentes tipos.
# Añade una nueva clave-valor al diccionario.
# Modifica el valor de una clave existente.
# Elimina una clave del diccionario.
# Accede al valor de una clave usando .get() para evitar un error si la clave no existe.

Diccionario = {
'Nombre' : 'Margarita',
'Edad' : 55,
'DNI':123456
}
print(Diccionario)  
Diccionario["Título"]="Srta"
Diccionario["Nombre"]="Pepita"
Diccionario.pop("Edad")
Diccionario.get("Edad","no existe")

# Ejercicio 4: Conjuntos
# Crea un conjunto con al menos 5 elementos.
# Añade un nuevo elemento al conjunto.
# Intenta añadir un elemento duplicado y observa qué sucede.
# Elimina un elemento del conjunto.
# Crea otro conjunto con algunos elementos en común con el primer conjunto y realiza las siguientes operaciones:
# Unión: Devuelve todos los elementos que están en cualquiera de los dos conjuntos.
# Intersección: Devuelve solo los elementos que están en ambos conjuntos.
# Diferencia: Devuelve los elementos que están en el primer conjunto, pero no en el segundo.

# Extra: Diferencia simétrica: Devuelve los elementos que están en uno u otro conjunto, pero no en ambos (investigar cómo hacerlo).

Conjunto = {True,"Amigo",3}
Conjunto.add(0.25)
print(Conjunto)
Conjunto.add("Amigo")
Conjunto.pop()
Conjunto.remove(3)
Conjunto_2={0.25,True, "Enemigo"}
Intersección = Conjunto.intersection(Conjunto_2)
print(Intersección)
Union = Conjunto.union(Conjunto_2)
print(Union)
Diferencia= Conjunto.difference(Conjunto_2)
print(Diferencia)
Diferencia_Simetrica = Conjunto ^ Conjunto_2
print(Diferencia_Simetrica)


# Ejercicio 5: Filtrando con Listas y Conjuntos
# Dada una lista con elementos duplicados, conviértela en un conjunto para eliminar los duplicados.
# Ordena los elementos del conjunto y conviértelos de nuevo en una lista.

lista1= [True, False,"Amigo",0.25, 0.25]
Conjunto_1 = set(lista1)
print(Conjunto_1)
Lista_nueva=list(Conjunto1)


# Ejercicio 6: Trabajando con Diccionarios Anidados
# Crea un diccionario que contenga información sobre un estudiante (nombre, edad, calificaciones en diferentes materias).
# Añade una nueva materia con su calificación al diccionario.
# Modifica la calificación de una materia existente.

%reset -f
Estudiante = {
"Nombre" : 'Margarita',
"Edad" : 55,
"Calificación": {"Math" : 8.9,"Física": 6.5}
}

Estudiante.calificacion


    

Diccionario("Lengua", "8")
