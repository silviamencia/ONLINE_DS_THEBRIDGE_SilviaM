# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:57:17 2019

@author: Usuario
"""
# Eliminamos todo lo anterior
%reset -f

# Establecemos el directorio
import os
#os.chdir(r"C:\Users\borja\Documents\Formacion Python\7-Quality\Outlier\Soluciones")
os.chdir(r"C:\Users\LENOVO\Documents\DataVM\CursoPythonCompleto\14- OUTLIERS\EJERCICIOS")
# Importamos las librerias necesarias
import pandas as pd
import numpy as np


#1. Cargar los datos (trainmod).
df2=pd.read_csv("trainmod.csv",sep=",",encoding='latin-1')

df2.dtypes
#2. Seleccionar los datos numéricos
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

df2num = df2.select_dtypes(include=numerics)
df2num.dtypes

#3. Realizar un boxplot de dichos datos.

df2num.plot(kind='box')


#4. Determinar qué datos son realmente numéricos y pueden tener outliers y cuales son
#categóricos aunque con forma numérica y repetir el boxplot.

for i in df2num:
    print(df2[i].describe())
    
# id, OverallQual, OverallCond , YearBuilt, YearRemodAdd,   
# BsmtFullBath hasta GarageCars, EnclosedPorc,MoSold, YrSold

df2num2=df2num.drop(columns=['Id','OverallQual', 'OverallCond' , 'YearBuilt', 'YearRemodAdd','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','TotRmsAbvGrd','Fireplaces' ,'GarageYrBlt', 'GarageCars','MoSold','YrSold'])    


df2num2.plot(kind='box')

#5. Excluir variables distorsionantes y repetir el boxplot.

# Las variables distorsionantes son el ID y SalePrize y YearBuilt y YearRemodAdd
df2num3=df2num2.drop(columns=['SalePrice','LotArea'])
df2num3.plot(kind='box')

#6. Realizar el boxplot por grupos y en caso de ser necesario eliminar o modificar alguna
#variable hasta extraer conclusiones fiables.
b1=df2num3.iloc[:,0:6].plot(kind='box')
b2=df2num3.iloc[:,7:14].plot(kind='box')
b3=df2num3.iloc[:,15:21].plot(kind='box')

#7. Determinar en qué observaciones se encuentran los outliers, realizando para ello las
#modificaciones que sean necesarias.

import numpy as np

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))

datos=df2num.apply(outliers_iqr)
datos



#8. Visualizar las observaciones que tienen outliers de otra forma distinta.

import numpy as np

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))

datos=df2num.apply(outliers_iqr)
datos


#9. Transformar los outliers en NAs para poder procesarlos posteriormente. Aplicarlo a
#los datos numéricos (correctos) excepto la “Id” y “SalePrice”.

df2num4 = df2num2.drop(columns=['SalePrice'])

import numpy as np

def replace2(group):
    mean, std = group.mean(), group.std()
    outliers = (group - mean).abs() > 3*std
    group[outliers] = np.nan        
    return group


datos=df2num4.apply(replace2)

datos.head(n=40)

#10. Juntar el resto de los datos para volver a crear la tabla con todas las variables.

Diferentes=df2[(df2.columns.difference(datos.columns))]

datosFinal = pd.concat([Diferentes,datos], axis = 1)


#13. Guardar, con un nombre diferente, el data frame que se seleccione.
datosFinal.to_csv('ejercicios.csv')