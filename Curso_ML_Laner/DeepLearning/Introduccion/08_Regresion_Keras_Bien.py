#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('fivethirtyeight')

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

import warnings
warnings.filterwarnings('ignore')

import os


# In[2]:


os.chdir(r"C:\Users\borja\OneDrive\Documents\C2B\Bootcamp\Módulo 8\Módulo 8\scripts\datos")


# In[3]:


df = pd.read_csv("saratogaHousing.csv")


# In[4]:


df.columns = ["precio", "metros_totales", "antiguedad", "precio_terreno",
                 "metros_habitables", "universitarios", "dormitorios", 
                 "chimenea", "banyos", "habitaciones", "calefaccion",
                 "consumo_calefacion", "desague", "vistas_lago",
                 "nueva_construccion", "aire_acondicionado"]


# In[5]:


df.info()


# In[6]:


df.isna().sum().sort_values()


# In[7]:


# Comprobamos cómo se distruyen los datos de precio de venta

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 3))
sns.histplot(df, x='precio', kde=True,ax=ax)
sns.set_style("white")
ax.set_title("Distribución Precio")
ax.set_xlabel('precio');


# In[8]:


# Pintamos las variables numéricas

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20, 15))
axes = axes.flat
columnas_numeric = df.select_dtypes(include=['float64', 'int']).columns
columnas_numeric = columnas_numeric.drop('precio')

for i, colum in enumerate(columnas_numeric):
    sns.histplot(
        data    = df,
        x       = colum,
        stat    = "count",
        kde     = True,
        color   = (list(plt.rcParams['axes.prop_cycle'])*2)[i]["color"],
        line_kws= {'linewidth': 2},
        alpha   = 0.3,
        ax      = axes[i]
    )
    axes[i].set_title(colum, fontsize = 15, fontweight = "bold")
    axes[i].tick_params(labelsize = 15)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("")
    
    
fig.tight_layout()
plt.subplots_adjust(top = 0.9)
fig.suptitle('Distribución variables numéricas', fontsize = 10, fontweight = "bold");


# In[9]:


df.chimenea = df.chimenea.astype("str")
df.chimenea.value_counts()


# In[10]:


df.select_dtypes(include=['object']).describe()


# In[11]:


fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 5))
axes = axes.flat
columnas_object = df.select_dtypes(include=['object']).columns

for i, colum in enumerate(columnas_object):
    df[colum].value_counts().plot.barh(ax = axes[i])
    axes[i].set_title(colum, fontsize = 14)
    axes[i].set_xlabel("")

# Se eliminan los axes vacíos
for i in [7, 8]:
    fig.delaxes(axes[i])
    
fig.tight_layout()


# In[12]:


mapeo = {'2': "2_mas",
               '3': "2_mas",
               '4': "2_mas"}

df['chimenea'] = df['chimenea'] .map(mapeo).fillna(df['chimenea'])

df.chimenea.value_counts().sort_index()


# In[13]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
                                        df.drop('precio', axis = 'columns'),
                                        df['precio'],
                                        train_size   = 0.7,
                                        random_state = 123,
                                        shuffle      = True
                                    )


# In[14]:


numeric_cols = X_train.select_dtypes(include=['float64', 'int'])
cat_cols = X_train.select_dtypes(include=['object', 'category'])

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
scaler = StandardScaler()
scaler.fit(numeric_cols)
datosNorm=scaler.transform(numeric_cols)
datosNorm = pd.DataFrame(datosNorm)

datosNorm.columns=numeric_cols.columns

datosNorm.reset_index(drop=True, inplace=True)
cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

cat_cols



# In[15]:


datosNorm


# In[16]:


datosmodelar = pd.concat([datosNorm,cat_cols], axis = 1)
datosmodelar


# In[17]:


# Definiremos el modelo como una secuencia de capas.
# Usaremos el modelo secuencial de manera que podamos ir añadiendo capas hasta estar contentos con la arquitectura desarrollada.
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf

model = Sequential()

# Partimos de un sistema con 8 variables por lo que nuestra primera capa acomodará dichas variables
# En la primera capa oculta usaremos 12 neuronas y una función de activación ReLU
# En la segunda capa oculta usaremos 8 neuronas y una función de activación ReLU
# Finalmente en la de salida una neurona y función de activación sigmoide
model.add(Dense(190, input_dim=datosmodelar.shape[1], activation='relu'))
model.add(Dense(80, activation='relu'))
model.add(Dense(1))

# Nota: Fíjate que el total de neuronas de entrada, lo definimos en la primera capa con input_dim


# In[28]:


optimizer = optimizer=tf.keras.optimizers.Adam(learning_rate=0.01)

model.compile(loss='mse',
              optimizer=optimizer,
              metrics=['mae', 'mse'])


# In[29]:


model.fit(datosmodelar, y_train, epochs=150, batch_size=1000)


# In[30]:


model.evaluate(datosmodelar,y_train)


# In[31]:


Pred_Train = model.predict(datosmodelar)


# In[32]:


from sklearn.metrics import r2_score
r2_score(y_train,Pred_Train)


# In[46]:


# Repetimos el procesado para test

numeric_cols_Train = X_train.select_dtypes(include=['float64', 'int'])
numeric_cols = X_test.select_dtypes(include=['float64', 'int'])
cat_cols = X_test.select_dtypes(include=['object', 'category'])
numeric_cols = pd.DataFrame(numeric_cols)

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

for y in numeric_cols:
    print(y)
    mean_y = np.mean(numeric_cols_Train[y])
    stdev_y = np.std(numeric_cols_Train[y])
    numeric_cols[y] = numeric_cols[y] - mean_y
    numeric_cols[y] = numeric_cols[y]/stdev_y

datosNorm = numeric_cols


datosNorm.reset_index(drop=True, inplace=True)
cat_cols = pd.get_dummies(cat_cols, drop_first=True)
cat_cols.reset_index(drop=True, inplace=True)

#cat_cols
#numeric_cols


# In[34]:


datostesteo = pd.concat([datosNorm,cat_cols], axis = 1)
datostesteo


# In[35]:


Pred_Test = model.predict(datostesteo)


# In[36]:


r2_score(y_test,Pred_Test)


# In[27]:


datosmodelar.shape[1]


# In[37]:


X_train.describe()


# In[38]:


X_test.describe()


# In[ ]:




