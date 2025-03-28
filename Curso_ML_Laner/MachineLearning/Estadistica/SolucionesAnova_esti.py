# -*- coding: utf-8 -*-

import os
import pandas as pd
os.chdir(r"C:\Users\LENOVO\Documents\DataVM\CursoPythonCompleto\Ejercicios y Soluciones ANOVA")
data = pd.read_csv("trainmod.csv")

data.columns


# MSZoning

# ANÁLISIS GRÁFICO
import matplotlib.pyplot as plt
import seaborn as sns
ax = sns.boxplot(x='MSZoning', y='SalePrice', data=data, color='#99c2a2')
plt.show()

'''
Analizando los boxplot se observa por ejemplo que las medianas de los precios varían 
entre los diferentes grupos de MSZoning, sugieriendo que el grupo de MSZoning tiene 
un impacto en los precios de las viviendas. 
'''
# Tabla ANOVA

# H0: Las medias de los precios son iguales entre todos los grupos de MSZoning.
# Ha: Al menos una de las medias de los precios es diferente.

from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=data, res_var='SalePrice', anova_model='SalePrice ~ C(MSZoning)')
res.anova_summary

# Calcular el valor crítico de F
from scipy.stats import f
alpha = 0.05
df1 = 4       
df2 = 1455    

F_critico = f.ppf(1 - alpha, df1, df2)
F_critico


# COTRASTE DE TUKEY

datos2 = pd.concat([data["SalePrice"],data["MSZoning"]], axis = 1)

# PARA CADA PAR DE GRUPOS:
    # H0: Las medias de los dos grupos que se comparan son iguales.
    # Ha: Las medias de los dos grupos que se comparan no son iguales.

from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog=datos2['SalePrice'], groups=datos2['MSZoning'], alpha=0.05)
print(tukey)

#########################################################################

# Crisis 

# ANÁLISIS GRÁFICO
import matplotlib.pyplot as plt
import seaborn as sns
ax = sns.boxplot(x='Crisis', y='SalePrice', data=data, color='#99c2a2')
plt.show()

'''
En este caso, analizando por ejemplo la mediana de los precios para el grupo "Sí" 
es bastante similar a la del grupo "No", sugieriendo que, a pesar de la existencia
de una crisis, el precio medio de las viviendas en ambos grupos no difiere sustancialmente.
'''

# Tabla ANOVA
from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=data, res_var='SalePrice', anova_model='SalePrice ~ C(Crisis)')
res.anova_summary


# COTRASTE DE TUKEY
datos3 = pd.concat([data["SalePrice"],data["Crisis"]], axis = 1)

from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog=datos3['SalePrice'], groups=datos3['Crisis'], alpha=0.05)
print(tukey)

####################################################################

# Crisis y MSZoning

# Análisis Gráfico

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.boxplot(x='MSZoning', y='SalePrice', hue='Crisis', data=data, palette='Set2')
plt.xlabel('MSZoning')
plt.ylabel('SalePrice')
plt.legend(title='Crisis')
plt.show()


# Tabla ANOVA
datos4 = pd.concat([data["SalePrice"],data["MSZoning"], data["Crisis"]], axis = 1)
from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=datos4, res_var='SalePrice', anova_model='SalePrice~C(MSZoning)+C(Crisis)+C(MSZoning):C(Crisis)')
res.anova_summary

'''
No hay interacción significativa entre las variables MSZoning y Crisis en relación con 
SalePrice. Es decir, si MSZoning tiene un efecto significativo sobre SalePrice, este 
efecto es consistente sin importar si estamos en una "Crisis" o no. Y de la misma forma,
si la variable Crisis afecta o no a SalePrice, ese efecto es el mismo para todas las 
categorías de MSZoning.
'''
