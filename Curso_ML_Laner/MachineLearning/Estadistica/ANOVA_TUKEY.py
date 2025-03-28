# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:38:09 2021

@author: borja
"""

import pandas as pd

df = pd.read_csv("https://reneshbedre.github.io/assets/posts/anova/onewayanova.txt", sep="\t")

df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['A', 'B', 'C', 'D'])

df_melt.columns = ['index', 'treatments', 'value']

import matplotlib.pyplot as plt
import seaborn as sns
ax = sns.boxplot(x='treatments', y='value', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="treatments", y="value", data=df_melt, color='#7d0013')
plt.show()

# Sacamos los P-valor
import scipy.stats as stats
fvalue, pvalue = stats.f_oneway(df['A'], df['B'], df['C'], df['D'])
print(fvalue, pvalue)

# H0: Todos los tratamientos iguales
# H1: Alguno Diferente

# Mostramos la tabla ANOVA

import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('value ~ C(treatments)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table

1- 0.000026
# ANOVA BIOINFOKIT
from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(treatments)')
res.anova_summary


# COTRASTE DE TUKEY

# H0: M(A) = M(B)
# H1: M(A) != M(B)

from bioinfokit.analys import stat
res = stat()
res.tukey_hsd(df=df_melt, res_var='value', xfac_var='treatments', anova_model='value ~ C(treatments)')
res.tukey_summary


# QQ PLOT
import statsmodels.api as sm
import matplotlib.pyplot as plt
sm.qqplot(res.anova_std_residuals, line='45')



# HISTOGRAMA
plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 



# SHAPYRO TEST (Normalidad)
import scipy.stats as stats
w, pvalue = stats.shapiro(model.resid)
print(w, pvalue)

# HOMOGENEIDAD DE LAS VARIANZAS (H0)
import scipy.stats as stats
w, pvalue = stats.bartlett(df['A'], df['B'], df['C'], df['D'])
print(w, pvalue)


from bioinfokit.analys import stat 
res = stat()
res.bartlett(df=df_melt, res_var='value', xfac_var='treatments')
res.bartlett_summary



# ANOVA 2 VARIABLES
# Graficamente
import pandas as pd
import seaborn as sns
d = pd.read_csv("https://reneshbedre.github.io/assets/posts/anova/twowayanova.txt", sep="\t")
d_melt = pd.melt(d, id_vars=['Genotype'], value_vars=['1_year', '2_year', '3_year'])
d_melt.columns = ['Genotype', 'years', 'value']
d_melt.head()
sns.boxplot(x="Genotype", y="value", hue="years", data=d_melt, palette="Set3") 

# ANOVA
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('value ~ C(Genotype) + C(years) + C(Genotype):C(years)', data=d_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table


from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=d_melt, res_var='value', anova_model='value~C(Genotype)+C(years)+C(Genotype):C(years)')
res.anova_summary


# Grafico lineas
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
fig = interaction_plot(x=d_melt['Genotype'], trace=d_melt['years'], response=d_melt['value'], 
    colors=['#4c061d','#d17a22', '#b4c292'])



# TUKEY
from bioinfokit.analys import stat

res = stat()

res.tukey_hsd(df=d_melt, res_var='value', xfac_var='Genotype', anova_model='value~C(Genotype)+C(years)+C(Genotype):C(years)')
res.tukey_summary


# Efecto de los años
res.tukey_hsd(df=d_melt, res_var='value', xfac_var='years', anova_model='value ~ C(Genotype) + C(years) + C(Genotype):C(years)')
res.tukey_summary


# Genotipos y años
res.tukey_hsd(df=d_melt, res_var='value', xfac_var=['Genotype','years'], anova_model='value ~ C(Genotype) + C(years) + C(Genotype):C(years)')
res.tukey_summary
tukey = res.tukey_summary
res.tukey_summary.head()



# QQ-plot
import statsmodels.api as sm
import matplotlib.pyplot as plt
sm.qqplot(res.anova_std_residuals, line='45')
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Standardized Residuals")


# histograma
plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 



# Shapiro-Wilk test (Normalidad)
import scipy.stats as stats
w, pvalue = stats.shapiro(res.anova_model_out.resid)
print(w, pvalue)

# Homogeneidad (h0)
from bioinfokit.analys import stat 
res = stat()
res.levene(df=d_melt, res_var='value', xfac_var=['Genotype', 'years'])
res.levene_summary
