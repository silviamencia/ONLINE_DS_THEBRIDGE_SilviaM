# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:56:41 2024

@author: borja
"""

import os
import pandas as pd
#os.chdir(r"C:\Users\borja\OneDrive\Documents\Formacion_Python")
os.chdir(r"C:\Users\LENOVO\Documents\DataVM\CursoPythonCompleto\Ejercicios y Soluciones ANOVA")
data = pd.read_csv("trainmod.csv")

data.columns


# MSZoning

# Tabla ANOVA
from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=data, res_var='SalePrice', anova_model='SalePrice ~ C(MSZoning)')
res.anova_summary



# COTRASTE DE TUKEY

datos2 = pd.concat([data["SalePrice"],data["MSZoning"]], axis = 1)

from bioinfokit.analys import stat
res = stat()
res.tukey_hsd(df=datos2, res_var='SalePrice', xfac_var='MSZoning', anova_model='SalePrice ~ C(MSZoning)')
res.tukey_summary



# Crisis 

# Tabla ANOVA
from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=data, res_var='SalePrice', anova_model='SalePrice ~ C(Crisis)')
res.anova_summary


# COTRASTE DE TUKEY
datos3 = pd.concat([data["SalePrice"],data["Crisis"]], axis = 1)

from bioinfokit.analys import stat
res = stat()
res.tukey_hsd(df=datos3, res_var='SalePrice', xfac_var='Crisis', anova_model='SalePrice ~ C(Crisis)')
res.tukey_summary



# Crisis y MSZoning

# Tabla ANOVA
datos4 = pd.concat([data["SalePrice"],data["MSZoning"], data["Crisis"]], axis = 1)
from bioinfokit.analys import stat
res = stat()
res.anova_stat(df=datos4, res_var='SalePrice', anova_model='SalePrice~C(MSZoning)+C(Crisis)+C(MSZoning):C(Crisis)')
res.anova_summary

# COTRASTE DE TUKEY
from bioinfokit.analys import stat
res = stat()
res.tukey_hsd(df=datos4, res_var='SalePrice', xfac_var=['MSZoning','Crisis'], anova_model='SalePrice ~ C(Crisis) + C(MSZoning) + C(Crisis):C(MSZoning)')
res.tukey_summary

