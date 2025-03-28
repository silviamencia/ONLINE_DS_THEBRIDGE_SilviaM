# -*- coding: utf-8 -*-
import os
os.chdir(r"D:\CURSOS\DS\Machine_Learning\TITANIC")
import pandas as pd
import numpy as np

data =  pd.read_csv("train.csv", sep=",", encoding='latin-1')
data
# Comprobamos que no hay valores perdidos.

data.isnull().sum()

AnalisisNumericas=data.describe()
data.columns

# Eliminamos las variables que no pueden incluirse en el modelo
del(data["PassengerId"])
del(data["Name"])
del(data["Ticket"])

# Anlizamos los valores perdidos.

Perdidos = data.isnull().sum()
Perdidos

# Vemos que la cabina tiene demasiados valores perdidos, por lo que la eliminamos

del(data["Cabin"])

#Estimamos las edades faltantes

import pandas as pd
import numpy as np

datoNum1=data.loc[:, data.dtypes == np.float64]
datoNum2=data.loc[:, data.dtypes == np.int64]

datoNum = pd.concat([datoNum1, datoNum2], axis=1)


datoNoNum=data.loc[:, data.dtypes == object]
datoNoNum

datoNum=pd.DataFrame(datoNum)
datoNoNum=pd.DataFrame(datoNoNum)

from fancyimpute  import IterativeImputer 
my_imputer = IterativeImputer()
datoNumcomp = my_imputer.fit_transform(datoNum)
datoNumcomp = pd.DataFrame(datoNumcomp)
datoNumcomp.columns = datoNum.columns

datoNumcomp = pd.DataFrame(datoNumcomp)

datos_completos= pd.concat([datoNoNum, datoNumcomp], axis=1)
datos_completos.isnull().sum()

datos_completos = pd.get_dummies(datos_completos, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None)

y=datos_completos['Survived']
X = datos_completos.drop(['Survived'], axis = 1)