#!/usr/bin/env python
# coding: utf-8

# # CNN para clasificación de imágenes CIFAR

# In[1]:


# Importamos librerías
import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

import os

from tensorflow.python.eager import context

_ = tf.Variable([1])


# In[2]:


context._context = None
context._create_context()

tf.config.threading.set_inter_op_parallelism_threads(1)


# El dataset CIFAR contiene, ya clasificadas en 10 clases, 60000 imágenes en color.  6000 imágenes de cada clase.  El dataset ya viene dividido en 50000 imágenes de entrenamiento y 10000 de test.
# Las clases no se solapan.  Son mutuamente excluyentes.

# In[3]:


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()


# In[4]:


# Rápida mirada a los datos
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


# In[5]:


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
    # Las etiquetas CIFAR son arrays, por eso necesitamos un índice extra
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()


# ### Creamos la CNN

# In[6]:


num_filtros = 32
kernel_size = 3
pool_size = 2


# In[7]:


os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'


# In[8]:


model = models.Sequential()
model.add(layers.Conv2D(num_filtros, kernel_size, activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D(pool_size))
model.add(layers.Conv2D(num_filtros*2, kernel_size, activation='relu'))
model.add(layers.MaxPooling2D(pool_size))
model.add(layers.Conv2D(num_filtros*2, kernel_size, activation='relu'))


# In[9]:


model.summary()  # sin añadir las capas finales de RNA


# In[10]:


# Añadimos las últimas etapas de la red
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))


# In[11]:


model.summary()


# Vemos como pasamos de una salida de 4x4x64 neuronas a otra de 1024 neuronas

# ### Compilamos y entrenamos el modelo

# In[12]:


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))


# ### Evaluamos el modelo

# In[13]:


plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)


# ### ¿Podemos mejorarlo?

# In[14]:


num_filtros = 64
kernel_size = 2
pool_size = 2


# In[15]:


# Añado una capa Dropout
model = models.Sequential()
model.add(layers.Conv2D(num_filtros, kernel_size, activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D(pool_size))
model.add(layers.Conv2D(num_filtros*2, kernel_size, activation='relu'))
model.add(layers.MaxPooling2D(pool_size))
model.add(layers.Conv2D(num_filtros*2, kernel_size, activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dropout(0.2))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))


# In[16]:


model.summary()


# In[17]:


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))


# In[18]:


plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

