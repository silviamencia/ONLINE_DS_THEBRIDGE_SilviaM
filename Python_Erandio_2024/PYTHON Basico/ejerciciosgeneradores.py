# -*- coding: utf-8 -*-
Created on Fri Oct 18 12:07:26 2024
# Crear un generador que busca en un archivo cualquiera, líneas que contengan una subcadena coincidente:
# Usar ese generador para leer El Quijote, cuando el generador encuentre la palabra Quijote,
# imprime la línea y para hasta que el usuario le da a "intro" (con un input vacío)

import os
import csv
    
def generador_palabras():
    with open("./archivos/quijote.txt", "r",encoding="utf8") as lectura:
        Lineas = lectura.readlines() 
    palabra =str( input("Por favor, introduzca la palabra a buscar:"))
    for linea in Lineas:
        if palabra in linea:
            yield linea
generador = generador_palabras()        
next(generador)        


for linea in generador:
    print(linea)
    if input("para cancelar pulse c") == "c":
        break

    
    
 generador_palabras()
 next(generador_palabras)   
    

#Si entrada está vacio, se ejecuta el if
if not entrada:
print("ingrese algo mas largo")


