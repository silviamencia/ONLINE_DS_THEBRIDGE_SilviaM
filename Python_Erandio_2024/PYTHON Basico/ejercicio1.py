# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:28:43 2024

@author: LANER
"""

22.8 + 35.3
25-10
3.14*5
50/4
import math
math.sqrt(25)
25**(1/2)
a= 22,8 + 35,3
b=25-10
c=3.14*5
d= 50/4
e=25**(1/-2)
f=math.sqrt(25)
type(a)
type(b)
type(c)
type(d)
type(e)
type(f)
Nombre_apellidos="Pepito Perez Gonzalez" 
lugar_nacimiento="Cadiz"
lugar_residencia="Madrid"
type(Nombre_apellidos)
type(lugar_nacimiento)
type(lugar_residencia)

formateado = "Mi nombre es {0},he nacido en {1}y vivo en {2}".format(Nombre_apellidos, lugar_nacimiento, lugar_residencia)
formateado = f"Mi nombre es {Nombre_apellidos},he nacido en {lugar_nacimiento}y vivo en {lugar_residencia}"
len(formateado)
print(formateado)
formateado[0]
formateado[13:19]
formateado[13,21,26]

formateado1 = formateado.lower()
print(formateado1)
"Pepito" in (formateado)
"a" in (formateado)
formateado.count("a")

lista_separada = formateado.split(" ")
formateado2 = formateado.upper()
dias_mes="Lunes, Martes, Miercoles, Jueves, Viernes"
print(dias_mes)
