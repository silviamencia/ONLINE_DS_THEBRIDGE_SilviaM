# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:37:37 2024

@author: LANER
"""
#####Ejercicio 1
frase=str("PYTHON es un lenguaje GENIAL")
frasemay=str.lower(frase)
print(frase)
print(frasemay)
frasemin=str.upper(frase)
print(frasemin)
frasecapitalizada=frase.capitalize()
print(frasecapitalizada)
print(frase.capitalize())
fraseInvertida =frase[::-1]
print(fraseInvertida)

######Ejercicio 2
Nombre=str("Silvia")
Apellido=str("Mencia")
NombreCompleto=Nombre+Apellido
print(NombreCompleto)
Inicial_Nombre=Nombre[0]
print(Inicial_Nombre)
Inicial_Apellido=Apellido[0]
print(Inicial_Apellido)
Iniciales=NombreCompleto[0:10:6]
print(Iniciales)

######Ejercicio 3
producto=str("leche")
precio=int(10)
cantidad=int(15)
print(f"Compraste {cantidad} de {producto} a un precio de {precio} cada uno.")
costo_total=precio*cantidad
print(f"El costo total es de {costo_total} ")

######Ejercicio 4
frase1="la ciudad es bonita"
frase2="LA CIUDAD ES BONITA"
frases_iguales=frase1==frase2
print("son iguales",frases_iguales)
frase2=frase2.lower()
print(frase2)
frases_iguales=frase1==frase2
print("son iguales",frases_iguales)
print(frase2)
reset f

######Ejercicio 5
veces_a=frase1.count("a")
veces_e=frase1.count("e")
veces_i=frase1.count("i")
veces_o=frase1.count("o")
veces_u=frase1.count("u")

print(veces_a)
print(veces_e)
print(veces_i)
print(veces_o)
print(veces_u)


######Ejercicio 6
palabra = "Hola
primera_letra = palabra[0]

lista = ["Hola", "Adiós"]
primera_palabra = lista[0]
primera_letra = primera_palabra[0]

primera_letra = lista[0][0]

Frase="Asociación Internacional de Programadores"
Lista=Frase.split()
print(Lista)
print(Lista[0][0]+Lista[1][0]+Lista[3][0])

######Ejercicio 7

frase1="LA ciudad es bonita"
cambio=frase1.split()
frase2=frase1.replace("LA", "la")
print(frase2)

######Ejercicio 8
adjetivo="bonita"
print(adjetivo in frase1)

######Ejercicio 9
frase2="La ciudad es maravillosa"
lista=frase2.split()
print(frase2)
print(lista)
print(lista[3]+" "+lista[0]+" "+lista[2]+" "+lista[1])

######Ejercicio 10
pi=3.1415927
print(pi,round(3))

frase1="LA ciudad es bonita"
fr=frase1.split()
print(fr)
fr2=frase1.reversed(str)
list(reversed(fr))
