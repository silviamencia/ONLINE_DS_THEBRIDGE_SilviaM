# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:32:11 2023

@author: Garay Alcibar
"""

# Eliminamos todo lo anterior
%reset -f

# Importamos las librerias necesarias
import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\LENOVO\Documents\DataVM\CursoPythonCompleto\15- Valores Perdidos\EJERCICIOS")

#1. Cargar los datos generados en la practica numero 8.
data=pd.read_csv("datosprocesados2.csv",sep=",",encoding='latin-1')

#2. Comprobar el número de valores perdidos, total y por variable.
# Por Variable
nulos_por_variable=data.isnull().sum()
variables_con_nulos=nulos_por_variable[nulos_por_variable>0]
# Total
sum(data.isnull().sum())

#3. Realizar la misma operación en porcentajes.
# Porcentaje por variable
porcentaje_nulos=data.isnull().sum()/len(data.index)
porcentaje_nulos=porcentaje_nulos[porcentaje_nulos>0]
# Porcentaje total
sum(data.isnull().sum())/(len(data.index)*len(data.columns))*100
sum(data.isnull().sum())/(data.shape[0]*data.shape[1])*100 #cálculo alternativo

#4. Eliminar aquellas variables que tengan más de un 30% de valores perdidos.
data2=data[:]

for i in data2:
    #print(i)
    if data2[i].isnull().sum()/len(data2.index) >= 0.3:
        print(i)
        data2=data2.drop(columns=i)
# lógica alternativa en una sola línea
data3 = data.loc[:, data.isnull().sum() <= 0.3*data.shape[0]]
 
#5. Calcular el porcentaje de valores perdidos una vez eliminadas esas variables.
# Porcentaje por variable
data2.isnull().sum()/len(data2.index)
# Porcentaje total
sum(data2.isnull().sum())/(len(data2.index)*len(data2.columns))*100

#6. Eliminar de las tres primeras variables los NAs (sin incluir la Id).
data2.iloc[:,1:4].isnull().sum()
datoscomp=data2.iloc[:,1:4].dropna()
data4=data2[data2.index.isin(datoscomp.index)]

# Lógica alternativa en una sóla línea
data5=data2.dropna(subset=["MSZoning","LotFrontage","Street"])

#7. Eliminar de todas las variables los valores perdidos.
datoscomp=data2.dropna()

#8. Comprobar que no existen valores perdidos.
datoscomp.isnull().any().any()
sum(datoscomp.isnull().sum())

#9. Volver a cargar los datos.
# Eliminamos todo lo anterior
%reset -f

import pandas as pd
import numpy as np
data=pd.read_csv("datosprocesados2.csv",sep=",",encoding='latin-1')

#10. Eliminar aquellas variables que tengan más de un 30% de valores perdidos.
data2=data[:]
for i in data2:
    #print(i)
    if data2[i].isnull().sum()/len(data2.index) >0.3:
        print(i)
        data2=data2.drop(columns=i)
        
#11. Imputar la media para estimar los valores perdidos.
#data2=data2.fillna(data2.mean())        
data2 = data2.fillna(data2.select_dtypes(include=[float, int]).mean())
      
#12. Comprobar que no existen valores perdidos.
data2.isnull().any().any()
data2.isnull().sum()[data2.isnull().sum()>0]

#13. En caso de que no se haya eliminado explicar a qué puede deberse.
# Si que existen, pero no puede calcular la media porque es un dato no numerico,
#por lo que el programa no sabe calcularlo

#14. Volver a cargar los datos.
%reset -f

import pandas as pd
import numpy as np
data=pd.read_csv("datosprocesados2.csv",sep=",",encoding='latin-1')

#15. Eliminar aquellas variables que tengan más de un 30% de valores perdidos.
data2=data[:]
for i in data2:
    #print(i)
    if data2[i].isnull().sum()/len(data2.index) >0.3:
        print(i)
        data2=data2.drop(columns=i)
        
#16. Imputar los valores perdidos utilizando la imputación múltiple.
data2.corr() 

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# numerics2 = pd.DataFrame(numerics)
# numerics2.columns = ["Tipo"]

# a=pd.DataFrame(data2.dtypes)
# a.columns = ["Variable"]

# # a.dtypes
# # numerics2.dtypes

# datoNumNames=a[(a["Variable"]=="float64") | (a["Variable"]=="int64")]
# NoNumNames = a[(a["Variable"]!="float64") & (a["Variable"]!="int64")]
# ,columns=datoNumNames.index
# ,columns=NoNumNames.index
datoNum=pd.DataFrame(data2.select_dtypes(include=numerics))
datosNoNum=pd.DataFrame(data2.select_dtypes(exclude=numerics))

# Alternativa fácil y sencilla
datoNum2=pd.DataFrame(data2.select_dtypes(include=["int","float"]))
datosNoNum2=pd.DataFrame(data2.select_dtypes(exclude=["int","float"]))

import pandas as pd
import numpy as np
import fancyimpute 
from fancyimpute import IterativeImputer
import sklearn.preprocessing as sk
from sklearn.impute import SimpleImputer

#ORDENAMOS EL DATA FRAME POR TIPO

data_ordenado_dtypes = data2[data2.dtypes.sort_values().index]
data_ordenado_dtypes.info()

#SEPARAMOS EL DATA FRAME POR GRUPOS (esto no elimina los nombres de las columnas)

datosbool = data_ordenado_dtypes.select_dtypes(include = [bool])
datosbool.info()
datosbool.isnull().any()    #NO HAY NA

datosNum = data_ordenado_dtypes.select_dtypes(include = [float,int])
datosNum.info()
datosNum.isnull().any()     #HAY NA

datosObject = data_ordenado_dtypes.select_dtypes(include = [object])
datosObject.info()
datosObject.isnull().any()  #HAY NA


#RELLENAMOS NA DE NUMEROS CON ESTA COSA RARA QUE NO SE ENTIENDE PERO COPIA PEGA
#(elimina nombre de columnas)
mice_imputer = IterativeImputer()
df_numeros = mice_imputer.fit_transform(datosNum)

df_numeros = pd.DataFrame(df_numeros)   
df_numeros.info()
df_numeros.isnull().any().any()  #COMPROBAMOS QUE NO HAY NA
df_numeros.columns = datosNum.columns   #RECUPERAMOS NOMBRES DE LAS COLUMNAS

#RELLENAMOS NA DE OBJETOS CON LA MODA
#(elimina nombre de columnas)
imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent", copy=False)
imputer = imputer.fit(datosObject)
datosObject = imputer.transform(datosObject.values)

datosObject=pd.DataFrame(datosObject)
datosObject.isnull().any().any()  #COMPROBAMOS QUE NO HAY NA

#UNIMOS EN EL ORDEN QUE NOS MARCA EL PRIMER ORDENADO DE COLUMNAS POR TIPO
data_ordenado_dtypes.info()  #RECORDEMOS
datos_completos = pd.concat([datosbool, df_numeros ,datosObject], axis=1)

#CON EL ORDEN DE COLUMNAS DE FORMA CONCRETA LE VOLVEMOS A RELLENAR EL NOMBRE DE CADA COLUMNA
datos_completos.columns = data_ordenado_dtypes.columns
datos_completos.index = data_ordenado_dtypes.index

datos_completos.isnull().any().any()  #COMPROBAMOS QUE NO HAY NA
      
#17. Guardar los datos.
datos_completos.to_csv('tabla_sin_nulls.csv')