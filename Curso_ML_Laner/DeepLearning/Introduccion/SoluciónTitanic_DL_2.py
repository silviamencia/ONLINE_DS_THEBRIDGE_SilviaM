# -*- coding: utf-8 -*-


import os
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import KFold
from sklearn import set_config
import multiprocessing
from keras.layers import Dense
import tensorflow as tf
from keras.models import Sequential
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from fancyimpute  import IterativeImputer 
import random
from keras.layers import Dropout
from keras.regularizers import l2

######################### 1.- CARGAMOS LOS DATOS

os.chdir(r"C:\Users\LENOVO\Documents\DataVM\Cursos\CursoPythonCompleto\17-Modelos\Titanic")

data = pd.read_csv("train.csv")

######################### 2.- PREPROCESAMIENTO

AnalisisNumericas=data.describe()
data.columns

data["Survived"].value_counts()/891
# Eliminamos las variables que no pueden incluirse en el modelo
del(data["PassengerId"])
del(data["Name"])
del(data["Ticket"])


# Anlizamos los valores perdidos.

Perdidos = data.isnull().sum()

# Vemos que la cabina tiene demasiados valores perdidos, por lo que la eliminamos

del(data["Cabin"])


# Con la edad podemos imputarla o eliminarla.
# Probamos las dos opciones a ver cual de mejor
data.dtypes


# Para obtener todos el mismo resultado debemos añadir una semilla
tf.random.set_seed(1)
np.random.seed(1)
random.seed(1)

######################### 2.1- ELIMINAMOS VALORES FALTANTES
datoscomp=data.dropna()



# División de los datos

X_train, X_test, y_train, y_test = train_test_split(
                                        datoscomp.drop('Survived', axis = 'columns'),
                                        datoscomp['Survived'],
                                        train_size   = 0.7,
                                        random_state = 123,
                                        shuffle      = True
                                    )


numeric_cols = X_train.select_dtypes(include=['float64', 'int'])
cat_cols = X_train.select_dtypes(include=['object', 'category'])

numeric_cols.dtypes

numeric_cols["Pclass"] = numeric_cols['Pclass'].astype(float) 
numeric_cols["SibSp"] = numeric_cols['SibSp'].astype(float) 
numeric_cols["Parch"] = numeric_cols['Parch'].astype(float) 


# Estandarizamos las variables numéricas

scaler = StandardScaler()
scaler.fit(numeric_cols)
datosNorm=scaler.transform(numeric_cols)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns

datosNorm.reset_index(drop=True, inplace=True)



# Binomializamos las categóricas

cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols


datosmodelar = pd.concat([datosNorm,cat_cols], axis = 1)


########################## 3.- PROBAMOS LOS MODELOS

model = Sequential()

model.add(Dense(110, input_dim=8, activation='relu'))
model.add(Dense(55, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              #loss="binary_crossentropy",
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False, # usar cuando valores de predicción sean [0,1]
                                                      label_smoothing=0.0,
                                                      axis=-1,
                                                      reduction=None,
                                                      name="binary_crossentropy"),
              metrics=['accuracy'])


model.fit(datosmodelar, y_train, epochs=150, batch_size=30)

_, accuracy = model.evaluate(datosmodelar, y_train)
print('Accuracy: %.2f' % (accuracy*100))



####################### 4.-  REALIZAMOS LAS PREDICCIONES

numeric_cols_test = X_test.select_dtypes(include=['float64', 'int'])
cat_cols = X_test.select_dtypes(include=['object', 'category'])

datosNorm=scaler.transform(numeric_cols_test)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns
datosNorm.reset_index(drop=True, inplace=True)

cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols

datostesteo = pd.concat([datosNorm,cat_cols], axis = 1)
datostesteo

Pred_Test = model.predict(datostesteo)

################################## 5.- EVALUAMOS EL MODELO

# La función sigmoide nos devueve los resultados en formato probabilidad.
# Convertimos los mismos a casos, tomando como umbral 0.5
y_pred = (Pred_Test > 0.5).astype(int)
y_pred


confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

###############################################################################
###############################################################################



######################### 2.2- IMPUTAMOS VALORES FALTANTES

datoNum1=data.loc[:, data.dtypes == np.float64]
datoNum2=data.loc[:, data.dtypes == np.int64]
datoNum = pd.concat([datoNum1, datoNum2], axis=1)

datoNoNum=data.loc[:, data.dtypes == object]

datoNum=pd.DataFrame(datoNum)
datoNoNum=pd.DataFrame(datoNoNum)

# variables numéricas

my_imputer = IterativeImputer()
datoNumcomp = my_imputer.fit_transform(datoNum)
datoNumcomp = pd.DataFrame(datoNumcomp)
datoNumcomp.columns = datoNum.columns

datoNumcomp = pd.DataFrame(datoNumcomp)

# variables categóricas

most_frequent_embarked = datoNoNum['Embarked'].mode()[0]
datoNoNum['Embarked'].fillna(most_frequent_embarked, inplace=True)

datos_completos= pd.concat([datoNoNum, datoNumcomp], axis=1)


#observamos que no hay valores faltantes 
datos_completos.isnull().sum()



# División de los datos
X = datos_completos.drop('Survived', axis = 'columns')
y = datos_completos['Survived']

X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        y,
                                        train_size   = 0.7,
                                        random_state = 123,
                                        shuffle      = True
                                    )


numeric_cols = X_train.select_dtypes(include=['float64', 'int'])
cat_cols = X_train.select_dtypes(include=['object', 'category'])

numeric_cols.dtypes

numeric_cols["Pclass"] = numeric_cols['Pclass'].astype(float) 
numeric_cols["SibSp"] = numeric_cols['SibSp'].astype(float) 
numeric_cols["Parch"] = numeric_cols['Parch'].astype(float) 


# Estandarizamos las variables numéricas

scaler = StandardScaler()
scaler.fit(numeric_cols)
datosNorm=scaler.transform(numeric_cols)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns

datosNorm.reset_index(drop=True, inplace=True)



# Binomializamos las categóricas

cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols


datosmodelar = pd.concat([datosNorm,cat_cols], axis = 1)


########################## 3.- PROBAMOS LOS MODELOS

model = Sequential()

model.add(Dense(110, input_dim=8, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dropout(0.3)) 
model.add(Dense(55, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss="binary_crossentropy",
              metrics=['accuracy'])


model.fit(datosmodelar, y_train, epochs=150, batch_size=30)

_, accuracy = model.evaluate(datosmodelar, y_train)
print('Accuracy: %.2f' % (accuracy*100))


########################### 4.- REALIZAMOS LAS PREDICCIONES 

numeric_cols_test = X_test.select_dtypes(include=['float64', 'int'])
cat_cols = X_test.select_dtypes(include=['object', 'category'])

datosNorm=scaler.transform(numeric_cols_test)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns
datosNorm.reset_index(drop=True, inplace=True)

cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols

datostesteo = pd.concat([datosNorm,cat_cols], axis = 1)
datostesteo

Pred_Test = model.predict(datostesteo)


########################### 5.- EVALUAMOS EL MODELO

# La función sigmoide nos devueve los resultados en formato probabilidad.
# Convertimos los mismos a casos, tomando como umbral 0.5
y_pred = (Pred_Test > 0.5).astype(int)
y_pred


confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


###############################################################################
'''
Una vez que encontramos el mejor modelo, lo entrenamos de nuevo con todos los 
datos disponibles. Así aprovechamos al máximo la información para que el modelo 
esté lo mejor preparado antes de usarlo en producción.
'''
###############################################################################


### Entrenamiento definivo

y=datos_completos['Survived']
X = datos_completos.drop(['Survived'], axis = 1)


numeric_cols = X.select_dtypes(include=['float64', 'int'])
cat_cols = X.select_dtypes(include=['object', 'category'])

numeric_cols.dtypes

numeric_cols["Pclass"] = numeric_cols['Pclass'].astype(float) 
numeric_cols["SibSp"] = numeric_cols['SibSp'].astype(float) 
numeric_cols["Parch"] = numeric_cols['Parch'].astype(float) 


# Estandarizamos variables numéricas

scaler = StandardScaler()
scaler.fit(numeric_cols)
datosNorm=scaler.transform(numeric_cols)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns
datosNorm.reset_index(drop=True, inplace=True)


# Binomializamos variables categóricas

cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols

datosmodelar = pd.concat([datosNorm,cat_cols], axis = 1)


# Probamos el modelo

model = Sequential()

model.add(Dense(110, input_dim=8, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dropout(0.3)) 
model.add(Dense(55, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss="binary_crossentropy",
              metrics=['accuracy'])


model.fit(datosmodelar, y, epochs=150, batch_size=30)


# Evaluamos el modelo
_, accuracy = model.evaluate(datosmodelar, y)
print('Accuracy: %.2f' % (accuracy*100))




########################### Cargamos los DATOS DE TEST

test = pd.read_csv("test.csv")


# Eliminamos las variables sobrantes

del(test["PassengerId"])
del(test["Name"])
del(test["Ticket"])
del(test["Cabin"])

# Imputamos los valores perdidos

testNum1=test.loc[:, test.dtypes == np.float64]
testNum2=test.loc[:, test.dtypes == np.int64]

testNum = pd.concat([testNum1, testNum2], axis=1)


testNoNum=test.loc[:, test.dtypes == object]


testNum=pd.DataFrame(testNum)
testNoNum=pd.DataFrame(testNoNum)

 
my_imputer = IterativeImputer()
testNumcomp = my_imputer.fit_transform(testNum)
testNumcomp = pd.DataFrame(testNumcomp)
testNumcomp.columns = testNum.columns

testNumcomp = pd.DataFrame(testNumcomp)

test_completos= pd.concat([testNoNum, testNumcomp], axis=1)

#observamos que no hay valores faltantes 
test_completos.isnull().sum()


numeric_cols = test_completos.select_dtypes(include=['float64', 'int'])
cat_cols = test_completos.select_dtypes(include=['object', 'category'])

numeric_cols.dtypes

numeric_cols["Pclass"] = numeric_cols['Pclass'].astype(float) 
numeric_cols["SibSp"] = numeric_cols['SibSp'].astype(float) 
numeric_cols["Parch"] = numeric_cols['Parch'].astype(float) 



datosNorm=scaler.transform(numeric_cols_test)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns

datosNorm.reset_index(drop=True, inplace=True)
cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols


datostesteo = pd.concat([datosNorm,cat_cols], axis = 1)


Pred_Test = model.predict(datostesteo)


y_pred = (Pred_Test > 0.5).astype(int)
y_pred


###################################### Cargamos GENDER SUBMISION
submit = pd.read_csv("gender_submission.csv")

# Pegamos las predicciones.
submit["Survived"] = y_pred
submit["Survived"] = submit["Survived"].astype(int) 
# Guardamos el CSV
submit.to_csv("Subir_Keras.csv", index = False)