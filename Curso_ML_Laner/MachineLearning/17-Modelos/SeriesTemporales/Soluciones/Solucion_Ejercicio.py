# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:06:26 2023

@author: borja
"""

import pandas as pd
import os

os.chdir(r"C:\Users\borja\OneDrive\Documents\UNAV\Master_2023\Soluciones")
# Cargamos los datos
datos = pd.read_csv("DatosEjercicio.csv")

# Procesamos la fecha para que sea el indice
datos["Month"] = pd.to_datetime(datos["Month"], format="%Y-%m")

datos.index = datos["Month"]
del (datos["Month"])

import matplotlib.pyplot as plt

# Graficamos la serie
plt.plot(datos)

# Se observa que hay dos periodos diferenciados

# Descomponemos la serie para ver si el cambio de tendecia es asi.
from statsmodels.tsa.seasonal import seasonal_decompose

SerieDescompuesta = seasonal_decompose(datos, model='additive')

# La graficamos.
SerieDescompuesta.plot(observed=True, seasonal=True, trend=True, resid=True, weights=False)

# Seleccionamos los datos desde 1975, fecha en la que se da el cambio de tendencia
# Tambien observamos una estacioanlidad mensual en un ciclo anual

datos = datos.loc["1975-01-01 00:00:00":]

# Repetimos el grafico
plt.plot(datos)

# Parece que es mas constante

# Procedemos a analizar si es necesario diferenciar
import pmdarima

# Respecto a la observacion anterior
pmdarima.arima.ndiffs(datos)

# Estacionalmente con estacionalidad anual.
pmdarima.arima.nsdiffs(datos, m = 12)


# Indica que si, por lo que diferenciamos
datosdiff = pmdarima.utils.diff(datos,lag = 1, differences= 1)

# Comprobamos si hay que diferenciar
pmdarima.arima.ndiffs(datosdiff)



pmdarima.arima.nsdiffs(datosdiff, m = 12)

# Indica que no por lo que prodecemos a realizar los test de estacionariedad

from statsmodels.tsa.stattools import adfuller

# H0: No estacionario (raiz unitaria)

import pandas as pd
datosdiff = pd.DataFrame(datosdiff)
datosdiff = datosdiff.rename(columns={0: "Valor"})

ADF = adfuller(datosdiff["Valor"])

# Mostramos los resultados
print('ADF Statistic: %f' % ADF[0])
print('p-value: %f' % ADF[1])

# Rechazamos H0 -> Serie estacionaria


# KPSS
from statsmodels.tsa.stattools import kpss

# H0: Serie Estacionaria

KPSS = kpss(datosdiff["Valor"])

# Mostramos los valores
print('KPSS Statistic: %f' % KPSS[0])
print('p-value: %f' % KPSS[1])

# No tenemos suficiente evidencia estadistica para rechazar H0 -> Serie estacionaria


# PP
from arch.unitroot import PhillipsPerron as PP

# H0: Serie  NO Estacionaria

PP = PP(datosdiff["Valor"])

# Mostramos los valores
PP

# Rechazamos H0 -> Serie estacionaria


# ERS
from arch.unitroot import DFGLS

# H0: Serie  NO Estacionaria

ERS = DFGLS(datosdiff["Valor"])

# Mostramos los valores
ERS
# No tenemos suficiente evidencia estadistica para rechazar H0 -> Serie no estacionaria


# Tres de los cuatro test indican que la serie es estacionaria

# Procedemos a modelar con estos datos

# Analizamos la correlacion y la correlacion parcial
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(datosdiff)
plot_pacf(datosdiff)


# Dividimos los datos en train y test

train = datos.loc[:"1991-12-01 00:00:00"]
test = datos["1992-01-01 00:00:00":]


import statsmodels.api as sm

# Entrenamos el modelo
model = sm.tsa.statespace.SARIMAX(train.iloc[:,0], order=(2,1,2), seasonal_order=(1,0,2,12))

# Visualizamos el modelo
ArimaModel = model.fit()
print (ArimaModel.summary())

# Realizamos las predicciones
test["Predicciones"] = ArimaModel.forecast(len(test))


# Graficamos

plt.plot(test)

# Vemos que el modelo ajusta correctamente

# Analizamos los residuos

# Analizamos el correlograma y el correlograma parcial de los errores
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


plot_acf(ArimaModel.resid)
plot_pacf(ArimaModel.resid)

ArimaModel.plot_diagnostics(figsize = (14,10))


# Existe una cierta correlacion entre los errores
# Probamos con logaritmos

import numpy as np
datos["Value"] = datos["Value"].astype(float)
Log_Datos = pd.DataFrame(np.log(datos["Value"]))


# Comprobamos si hay que diferenciar esta nueva serie
# Respecto a la observacion anterior
pmdarima.arima.ndiffs(Log_Datos)

# Estacionalmente con estacionalidad anual.
pmdarima.arima.nsdiffs(datos, m = 12)


# Diferenciamos segun el resultado obtenido

datos_log_diff = pmdarima.utils.diff(Log_Datos,lag = 1, differences= 1)

# Lo pasamos a Data Frame
datos_log_diff = pd.DataFrame(datos_log_diff)
datos_log_diff = datos_log_diff.rename(columns={0: "Valor"})


# Analizamos si esta nueva serie es estacionaria

ADF = adfuller(datos_log_diff["Valor"])

# Mostramos los resultados
print('ADF Statistic: %f' % ADF[0])
print('p-value: %f' % ADF[1])

# Rechazamos H0 -> Serie estacionaria


# KPSS
from statsmodels.tsa.stattools import kpss

# H0: Serie Estacionaria

KPSS = kpss(datos_log_diff["Valor"])

# Mostramos los valores
print('KPSS Statistic: %f' % KPSS[0])
print('p-value: %f' % KPSS[1])

# No tenemos suficiente evidencia estadistica para rechazar H0 -> Serie estacionaria


# PP
from arch.unitroot import PhillipsPerron as PP

# H0: Serie  NO Estacionaria

PP = PP(datos_log_diff["Valor"])

# Mostramos los valores
PP

# Rechazamos H0 -> Serie estacionaria


# ERS
from arch.unitroot import DFGLS

# H0: Serie  NO Estacionaria

ERS = DFGLS(datos_log_diff["Valor"])

# Mostramos los valores
ERS

# Los resultados son similares a lo obtenido en la serie original, es decir es estacionaria


train = Log_Datos.loc[:"1991-12-01 00:00:00"]
test = Log_Datos["1992-01-01 00:00:00":]


import statsmodels.api as sm

# Entrenamos el modelo
model = sm.tsa.statespace.SARIMAX(train.iloc[:,0], order=(2,1,1), seasonal_order=(1,0,2,12))

# Visualizamos el modelo
ArimaModel = model.fit()
print (ArimaModel.summary())

# Realizamos las predicciones
test["Predicciones"] = ArimaModel.forecast(len(test))

# Calculamos la exponencial
test["Value"]  = np.exp(test["Value"])
test["Predicciones"]  = np.exp(test["Predicciones"])
# Graficamos

plt.plot(test)

# Vemos que el modelo ajusta correctamente

# Analizamos los residuos

# Analizamos el correlograma y el correlograma parcial de los errores
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


plot_acf(ArimaModel.resid)
plot_pacf(ArimaModel.resid)

ArimaModel.plot_diagnostics(figsize = (14,10))


# En este caso el modelo esta correctamente estimado por lo que este es el modelo final
