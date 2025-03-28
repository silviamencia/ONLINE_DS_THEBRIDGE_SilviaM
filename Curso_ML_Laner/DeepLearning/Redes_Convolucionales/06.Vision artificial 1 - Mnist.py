#!/usr/bin/env python
# coding: utf-8

# # CNN en Dataset Mninst

# La base de datos MNIST es una gran base de datos de dígitos escritos a mano que se usa comunmente para entrenar varios sistemas de procesamiento de imágenes. La base de datos también se usa ampliamente para capacitación y pruebas en el campo del aprendizaje automático.

# ![title](img/MnistExamples.png)

# ### Cargamos librerías

# In[1]:


#pip install tensorflow


# In[2]:


import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os


# ### Preparamos los datos

# In[3]:


# Total de clases a predecir.
num_classes = 10

# Tamaño de las imágenes.  Todas las imágenes deben tener las mismas dimensiones.
input_shape = (28, 28, 1)


# In[4]:


df = keras.datasets.mnist.load_data()


# In[5]:


# Lo que cargamos son básicamente matrices de 28x28, con rangos de variación entre 0-255 que corresponden a la intensidad del gris.
# O es el blanco puro, 255 es el negro puro.
df


# In[6]:


df[0][0][0]


# In[7]:


# Para este caso particular, y por cómo están los datos en datasets, podemos usar este método de particionado.
(x_train, y_train), (x_test, y_test) = df


# ### Escalamos los datos

# In[8]:


# Escalamos los datos en el rango [0,1]
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255


# ### Comprobamos que todas las imágenes tengan las mismas dimensiones

# In[9]:


x_train.shape


# In[10]:


x_test.shape


# In[11]:


x_train = np.expand_dims(x_train, 3)
x_test = np.expand_dims(x_test, 3)


# In[12]:


x_train.shape


# In[13]:


# Variable clase a predecir
y_train


# In[14]:


y_train.shape


# In[15]:


y_test.shape


# ### Convertir la variable a predecir en una matriz binaria de clases

# In[16]:


# La transformación es similar a One Hot Encoding, pero con arrays
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# In[17]:


y_train


# ### Construimos el modelo

# In[18]:


os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'


# In[19]:


num_filtros = 32
kernel_size = 3
pool_size = 2

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),                            # Capa de entrada
        layers.Conv2D(num_filtros, kernel_size=kernel_size, activation="relu"),  # Total de kernels, tamaño de los mismos y función de activación a aplicar
        layers.MaxPooling2D(pool_size=pool_size),                     # Tamaño del muestreo a aplicar (devolverá número filas input / 2, número columnas input / 2)
        layers.Conv2D(num_filtros*2, kernel_size=kernel_size, activation="relu"),  # Segunda capa convolucional, puede tener el mismo tamaño
        layers.MaxPooling2D(pool_size=pool_size),                     # 2 segundo submuestreo
        layers.Flatten(),                                          # Aplanamiento de la salida convolucional
        layers.Dropout(0.5),                                       # Aplicamos dropout para mitigar el overfiting en nuestra CNN
                                                                   # Desactivamos de manera aleatoria un % de neuronas que no se tomarán en cuenta en el 
                                                                   # forwardpropagation, ni en el backwardpropagation
        #layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation="softmax"),
    ]
)


# * La razón de utilizar un Dropout, es que generalmente las neuronas cercanas suelen aprender patrones relacionados y estas relaciones pueden llegar a formar un patrón muy específico con los datos.
# * Al hacer el dropout, el total de neuronas de la red se reduce, por lo que las neuronas están "obligadas" a trabajar de forma "solitaria", sin depender de las demás.
# * Valores en el Dropout cercanos a 0, implica no desactivación de neuronas, cercanos a 1 implica la desactivación de casi todas las neuronas.
# * El Dropout, puede aplicarse por capa.  Aquí lo hemos aplicado al final de la red.
# * El Dropout NO SE APLICA en la capa de salida, ya que allí necesitamos todas la neuronas activas.
# * Sólo hemos usado una capa 'Dense', pero es habitual en CNN añadir más capas con más neuronas y funciones de activación ReLU
# 

# In[20]:


# Vemos qué tenemos
model.summary()


# ### Entrenamiento del modelo

# Keras incluye el argumento validation_split que nos permite utilizar una fracción de los datos de entrenamiento como datos de validación.  Esa fracción de datos no se usa para el entrenamiento y se reserva para evaluar la pérdida y cualquier otra métrica al final de cada ciclo.
# 

# In[21]:


batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy",  # tenemos más de 2 clases, si fuera una clasificación binaria usaríamos binary_crossentropy
              optimizer="adam", 
              metrics=["accuracy"])

model.fit(x_train, 
          y_train, 
          batch_size=batch_size, 
          epochs=epochs, 
          validation_split=0.1)


# ### Evaluamos el modelo

# In[22]:


score = model.evaluate(x_test, y_test, verbose=0)
print("Pérdida datos Test:", score[0])
print("Precisión datos Test:", score[1])

