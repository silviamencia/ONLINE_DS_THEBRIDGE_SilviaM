import os
os.chdir(r"/home/laptop/Descargas/Python Avanzado/Python Avanzado/2- Uniones/Ejercicios/")

import pandas as pd


#####################
# Utilzando Concat #
####################

SalePrice=pd.read_csv("SalePrice.csv")

# 1- Dividir el Dataset en tres grupos con usuarios comunes y diferentes y variables diferentes en cada caso.
# Filas comunes, columnas distintas
datos_inicio = SalePrice.iloc[:7, 0:4]
datos_centro = SalePrice.iloc[3:9, 4:8]
datos_fin = SalePrice.iloc[6:12, 8:12]

# 2- Dividir el Dataset en tres grupos con usuarios comunes y diferentes y variables comunes y diferentes en cada caso.
# Filas comunes, columnas comunes
datos_inicio_ = SalePrice.iloc[:7, 0:4]
datos_centro_ = SalePrice.iloc[3:9, 3:7]
datos_fin_ = SalePrice.iloc[6:12, 6:10]

# 3- Realizar uniones de los tres primeros grupos:
#     a. Incluyendo todas las variables y todas las observaciones, por el índice.
concat_vertical = pd.concat([datos_inicio, datos_centro, datos_fin])
concat_horiz = pd.concat([datos_inicio, datos_centro, datos_fin], axis = 1)

#     b. Incluyendo las observaciones comunes de las tres tablas y todas las variables, por el índice.
# Como no se repiten columnas, esto da índices vacíos
concat_vertical_inner = pd.concat([datos_inicio, datos_centro, datos_fin], join="inner")
# Sólo da los datos de la fila que esté en las 3 tablas
concat_horiz_inner = pd.concat([datos_inicio, datos_centro, datos_fin], axis = 1 ,join="inner")

#     c. Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por el índice.
enriqueciendo_centro = pd.concat([datos_centro, 
                   datos_inicio, 
                   datos_fin], axis=1).reindex(datos_centro.index)

# 4- Realizar uniones de los tres grupos creados en el punto 2:
#     a. Incluyendo todas las variables y todas las observaciones, por el índice.
concat_vertical = pd.concat([datos_inicio_, datos_centro_, datos_fin_])
concat_horiz = pd.concat([datos_inicio_, datos_centro_, datos_fin_], axis = 1)

#     b. Incluyendo las observaciones comunes de las tres tablas y todas las variables, por el índice.
# Como no se repiten columnas, esto da índices vacíos
concat_vertical_inner = pd.concat([datos_inicio_, datos_centro_], join="inner")
# Sólo da los datos de la fila que esté en las 3 tablas
concat_horiz_inner = pd.concat([datos_inicio_, datos_centro_, datos_fin_], axis = 1 ,join="inner")

#     c. Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por el índice.
enriqueciendo_centro = pd.concat([datos_centro_, 
                   datos_inicio_, 
                   datos_fin_], axis=1).reindex(datos_centro_.index)

# 5- Realizar dos grupos con observaciones comunes y variables únicas, incluyendo la Id en las dos tablas:
inicio_ = SalePrice.iloc[:6, 0:4]

lista = [0] + list(range(5,8))
fin_ = SalePrice.iloc[4:10, lista]

#     a. Incluyendo todas las variables y todas las observaciones, por la Id.
merge_out = pd.merge(inicio_, fin_, how='outer', on='Id')
#     b. Incluyendo las observaciones comunes de las tres tablas y todas las variables, por la Id.
merge_inn = pd.merge(inicio_, fin_, on='Id')
#     c. Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por la Id.
merge_right= pd.merge(inicio_, fin_, how='right', on='Id')
merge_left = pd.merge(inicio_, fin_, how='left', on='Id')


# 6- Realizar dos grupos con observaciones y variables comunes, incluyendo la Id en las dos tablas:
inicio_2 = SalePrice.iloc[:6, 0:5]

lista = [0] + list(range(4,8))
fin_2 = SalePrice.iloc[4:10, lista]
    
#     a. Incluyendo todas las variables y todas las observaciones, por la Id.
merge_out = pd.merge(inicio_2, fin_2, how='outer', on='Id')
#     b. Incluyendo las observaciones comunes de las tres tablas y todas las variables, por la Id.
merge_inn = pd.merge(inicio_2, fin_2, on='Id')
#     c. Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por la Id.
merge_right= pd.merge(inicio_2, fin_2, how='right', on='Id')
merge_left = pd.merge(inicio_2, fin_2, how='left', on='Id')




