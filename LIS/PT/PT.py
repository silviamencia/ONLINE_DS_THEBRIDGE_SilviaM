# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:10:36 2025

@author: silvi
"""
import os
import pandas as pd
os.chdir(r"C:\Users\silvi\Documents\DATA_SCIENCE\LIS\PT\DS")
df = pd.read_csv("vuelos.csv")

#Importo el módulo random
import random

#Creo la función matriz aleatoria
# def matriz_aleatoria(filas, columnas):
#    for i in range(filas):
#       for j in range(columnas):
#           print(round(random.uniform(1, 100), 2), end=" ")
#       print() 

# def matriz_aleatoria(filas, columnas):
#     matriz = []
#     for i in range(filas):
#         fila = []  # Crea una nueva fila
#         for j in range(columnas):
#             fila.append(round(random.uniform(1, 100), 2))  # Añade un número aleatorio a la fila
#         matriz.append(fila)  # Añade la fila a la matriz
#     return matriz

# #Ejecuto la función y le asigno el nombre MA
# ma=matriz_aleatoria(10,7)


# #Importo librería numpy
# import numpy as np
# #Utilizo la biblioteca scikit-learn e importo MinMaxScaler para hacer la normalización de la matriz
# from sklearn.preprocessing import MinMaxScaler

# #Creo el objeto MinMaxScaler
# scaler = MinMaxScaler()

# #Ajusto y transformo los datos
# MA_normalizada = scaler.fit_transform(MA)
# #Muestro en pantalla la matriz normalizada
# print(MA_normalizada)

# len(MA_normalizada)

# #Defino Matriz aleatoria normalizada filtrada vacía para guardar el resultado

# MA_normalizada_filtrada = []

# #Hago bucles para recorrer la matriz

# for i in range(len(MA_normalizada)):
#     for j in range(len(MA_normalizada[i])):
#         if MA_normalizada[i][j] > 0.90 or MA_normalizada[i][j] < 0.10:
#             MA_normalizada[i][j] = 0
#         else:
#             MA_normalizada_filtrada.append(MA_normalizada[i][j])

# MA_normalizada_filtrada_ordenada=sorted(MA_normalizada_filtrada, reverse=True)
# #Muestro en pantalla la matriz normalizada filtrada
# print(MA_normalizada_filtrada_ordenada)


df.info()


df.loc[df["RetrasoSalida"] > 15, "SalidaTarde"] = 1
df.loc[df["RetrasoSalida"]  <=  15, "SalidaTarde"] = 0
#Si es mayor de 15 "SalidaTarde" tendrá un 1 y si es menor o igual tendrá un 0

df.loc[df["RetrasoSalida"] > 15, "SalidaTarde"] = 1
df.loc[df["RetrasoSalida"]  <= 15, "SalidaTarde"] = 0
#Cambio el tipo de "SalidaTarde" a entero
df["SalidaTarde"] = df["SalidaTarde"].astype(int)

import matplotlib.pyplot as plt
distribucion_salida_tarde = df["SalidaTarde"].value_counts()
distribucion_salida_tarde.plot(x="SalidaTarde",ylabel="Quantity",kind='bar', color='red')
plt.title('Distribucion SalidaTarde')
plt.show()


df_sin = df[['RetrasoLlegada', 'RetrasoSalida']]
df_sin.to_csv('nombre_del_archivo.csv', index=False)

# Calcular los cuartiles
Q11= df['RetrasoLlegada'].quantile(0.25)
Q31 = df['RetrasoLlegada'].quantile(0.75)
IQR1 = Q31 - Q11

# Definir los límites para los outliers
limite_inferior = Q11 - 1.5 * IQR1
limite_superior = Q31 + 1.5 * IQR1

Q12= df['RetrasoSalida'].quantile(0.25)
Q32 = df['RetrasoSalida'].quantile(0.75)
IQR2 = Q32 - Q12

limite_inferior1 = Q12 - 1.5 * IQR2
limite_superior2 = Q32 + 1.5 * IQR2



# Filtrar los outliers
df_sin_outliers = df[(df['RetrasoLlegada'] >= limite_inferior) & (df['RetrasoLlegada'] <= limite_superior)]
df_sin_outliers2 = df[(df['RetrasoSalida'] >= limite_inferior1) & (df['RetrasoLlegada'] <= limite_superior2)]

print(df_sin_outliers)


retrasos_por_aeropuerto = df_sinoutliers_2.groupby("AeropuertoOrigen")["RetrasoSalida"].sum()
retrasos = retrasos_por_aeropuerto.sort_values(ascending=False)