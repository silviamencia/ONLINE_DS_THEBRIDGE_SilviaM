#!/usr/bin/env python
# coding: utf-8

# # PLN (Procesamiento del lenguaje natural) con Python
#   
# **Requisitos: Será necesario instalar la librería NLTK, además de descargar el corpus para las stopwords. Por defecto Conda incluye el paquete NLTK así como Google Colab.  En el caso de que no estuviera instalado NLTK, ejecutar el siguiente chunk**

# In[11]:


# Ejecutar este chunk sólo si no está instalado NLTK
# Descomentar la siguiente línea para instalar la libraría:

#!conda install nltk 


# In[12]:


import nltk


# In[13]:


nltk.download_shell() 
#d) DOwnload:
#stopwords


# In[14]:


nltk.download_gui()


# ## Obtener los datos

# Para el presente ejercicio, usaremos un dataset de [UCI datasets](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection).  
# Este dataset está en la carpeta **data**.  El conjunto de datos está en inglés 
# y cuenta con más de 5000 SMS.  Para información ampliada sobre el conjunto de datos, 
# consultar el fichero **readme**.

# Comprobamos primero el total de mensajes del conjunto de datos.  Usaremos rstrip() para eliminar 'espacios' al final de cada línea (o retornos de carro):

# In[15]:


#mensajes = [line.rstrip() for line in open('datos/SMSSpamCollection')]
mensajes = [line.rstrip() for line in open('C:\\Users\\LENOVO\\Documents\\DataVM\\Cursos\\DL_BED_2024-20241218T074932Z-001\\DL_BED_2024\\scripts\\datos\\SMSSpamCollection')]
print(len(mensajes))


# In[16]:


type (mensajes)


# In[17]:


mensajes [0:20]


# Una colección de textos se suele denominar "corpus". Podemos imprimir mensajes, 
# mostrando además el número de SMS, usando **enumerate**:

# In[18]:


for num_mensaje, mensajes in enumerate(mensajes[:20]):
    print(num_mensaje, mensajes)
    #print('\n')


# El set de datos, tiene como separador \t (es un TSV), donde la primera columna 
# nos indica si el mensaje es spam o no.  La segunda columna contiene el cuerpo del SMS.
# 
# A través de Machine Learning, vamos a entrenar un modelo para aprender a discriminar 
# automáticamente cuando un SMS es span o no.  El modelo lo podremos usar para clasificar
# SMS sin la variable clase.
# 
# Podemos ver el proceso seguido, a través de la documentación oficial de SciKit Learn:

# <img src='https://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/_images/plot_ML_flow_chart_1.png' width=600/>

# In[19]:


import pandas as pd


# In[20]:


mensajes = pd.read_csv('C:\\Users\\LENOVO\\Documents\\DataVM\\Cursos\\DL_BED_2024-20241218T074932Z-001\\DL_BED_2024\\scripts\\datos\\SMSSpamCollection', 
                       sep='\t', names=["clase", "mensajes"])
mensajes.head()


# ##################### Análisis exploratorio inicial ###########################

# In[21]:


mensajes.describe()


# Agrupamos los datos en base a la clase y vemos que devuelve describe().

# In[22]:


mensajes.groupby('clase').describe()


# Para continuar, realizamos un análisis exploratorio para conocer los datos con 
# los que estamos trabajando.  Cuanto mayor sea el conocimiento que tengamos de 
# los datos, mayor capacidad tendremos para  el [feature engineering](https://en.wikipedia.org/wiki/Feature_engineering) (ingeniería de datos o factores).
# 
# El enriquecimiento de los datos, puede ser mejorar de manera reseñable la 
# capacidad predictiva de nuestro modelo, frente a un set de datos dado.

# In[23]:


mensajes['tamaño'] = mensajes['mensajes'].apply(len)
mensajes.head()


# In[24]:


mensajes.sort_values('tamaño', ascending=False)


# ################ Visualización de los datos.

# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


plt.figure(figsize=(12,8))
mensajes['tamaño'].plot(bins=200, kind='hist') 
# el rango de valores se divide en 200 intervalos, y la altura de cada barra 
# representa la cantidad de datos que caen dentro de cada intervalo

# In[27]:


plt.figure(figsize=(12,8))
mensajes['tamaño'].plot.hist(bins=500) 


# Podemos jugar con el argumento bin que nos permite definir la granularidad o 
# resolución del eje X.  Para estos datos bins representa la longitud de los 
# mensajes ¿Qué pasa cuando bins se acerca a 1000?  Tenemos registros (mensajes)

# In[28]:


mensajes.sort_values('tamaño', ascending=False)


# Buscamenos el mensaje más extenso con 910 caracteres.

# In[29]:


mensajes[mensajes['tamaño'] == 910]['mensajes'].iloc[0]


# Olvidándonos del contenido del mensaje, nos centramos en la idea que ver si la 
# longitud del mensaje influye en si es spam o no.

# In[30]:


mensajes.hist(column='tamaño', by='clase', bins=50,figsize=(12,6))


# A través del análisis exploratorio inicial, hemos obtenido una conclusión 
# interesante, la tendencia a que un mensaje sea considerado spam aumenta con el 
# tamaño del mensaje.



# ################# Preprocesado del texto #####################################

# Los algoritmos de clasificación, implican convertir la conversión del set de datos 
# en algún tipo de dataframe numérico (conversión del corpus a formato vector).  
# La manera más sencilla es a través de una aproximación del tipo [bag-of-words](http://en.wikipedia.org/wiki/Bag-of-words_model) 
# donde una palabra se representa por un número.
# 
# Convertiremos por tanto mensajes en bruto (estado actual) en vectores (secuencias 
# de números).
# 
# Como primer paso separaremos a través de una funcion, cada mensaje en una lista de 
# palabras.  Posteriormente eliminaremos las palabras muy comunes (stopwords como 
# 'the', 'a', ...) a través de la librería NLTK (https://www.nltk.org/book/).  
# En este caso de uso usaremos las funciones básicas de la librería.
# 
# Stopwords: https://es.wikipedia.org/wiki/Palabra_vac%C3%ADa
# 
# Generamos una función que procese un mensaje y posteriormente a través de **apply()** 
# lo procesaremos para todo el DataFrame.
# 
# Eliminamos los signos de puntuación, para ello podemos usar el método **string**:

# In[31]:


import string

mens = 'Ejemplo mensaje! Atención: tiene un punto..'

# Comprobamos los caracteres para ver si son símbolos de puntuación
nopunc = [char for char in mens if char not in string.punctuation]

nopunc


# In[32]:


string.punctuation #elimina todo lo que sean puntuaciones


# In[33]:


# Juntamos los caracteres de nuevo para construir una cadena de texto.
nopunc = ''.join(nopunc)
nopunc


# In[34]:


mens


# Una vez eliminados los signos de puntuación, eliminamos las stopwords.  
# En este ejemplo, el set de datos está en inglés, por lo que deberemos eliminar 
# las stopwords inglesas. En la documentación de NLTF podemos encontrar las stopwords 
# para cada idioma.

# In[35]:


from nltk.corpus import stopwords
nltk.download('stopwords')


# In[36]:


stopwords.words('english')


# Las StopWords para castellano son:

# In[37]:


stopwords.words('spanish')


# In[38]:


nopunc.split()


# In[39]:


# Eliminamos stopwords
clean_mens = [word for word in nopunc.split() if word.lower() not in stopwords.words('spanish')]


# In[40]:


clean_mens


# In[41]:


# Otra manera de hacer lo mismo
clean_mens2 = []
for word in nopunc.split():
    if word.lower() not in stopwords.words('spanish'):
        clean_mens2.append (word)


# In[42]:


clean_mens2


# Este ejemplo está desarrollado para texto en castellano, pero el conjunto de datos
# está en inglés. Automatizamos el proceso para ejecutarlo sobre el total de datos en inglés.

# In[43]:


def procesado_texto(mens):
    """
    Acepta una cadena de texto, y ejecuta:
    1. Elimina todos los símbolos de puntuación
    2. Elimina las stopwords
    3. Devuelve una lista de texto limpio
    """
    # Comprobar caracteres para eliminar cualquier símbolo de puntuación
    nopunc = [char for char in mens if char not in string.punctuation]

    # Unir los caracteres para generar un string de nuevo.
    nopunc = ''.join(nopunc)
    
    # Eliminar las stopwords (en este caso de uso, inglesas)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


'''
def procesado_texto(mens):
    """
    Acepta una cadena de texto, y ejecuta:
    1. Convierte todo a minúsculas.
    2. Elimina todos los símbolos de puntuación.
    3. Elimina las stopwords.
    4. Devuelve una lista de texto limpio.
    """
    # Convertir todo el texto a minúsculas
    mens = mens.lower()

    # Eliminar cualquier símbolo de puntuación
    nopunc = [char for char in mens if char not in string.punctuation]

    # Unir los caracteres para generar un string limpio
    nopunc = ''.join(nopunc)
    
    # Eliminar las stopwords (en este caso de uso, en inglés)
    return [word for word in nopunc.split() if word not in stopwords.words('english')]
'''

# In[44]:


mensajes.head()


# Para procesar el set de datos, necesitamos 'tokenizar' los mensajes (convertir 
# un conjunto de textos, en una lista de 'tokens' que son las palabras que nos interesan).
# 
# Let's see an example output on on column:
# 
# **Atención:**
# Podemos obtener 'warnings' debido a símbolos que no hemos tenido en cuenta o 
# que no están en Unicode (como el símbolo de € o libra)

# In[45]:


# Comprobamos que funciona
mensajes['mensajes'].head(10).apply(procesado_texto)


# In[46]:


mensajes.head()


# ######################### Continuando con la Normalización #############################33
# 
# Existen diferentes maneras para continuar normalizando textos.  Una de ellas 
# es el [Stemming](https://es.wikipedia.org/wiki/Stemming) otra de ellas podría 
# ser la caracterización de cada palabra en función de si es un sustantivo, adjetivo, verbo, ...(http://www.nltk.org/book/ch05.html).
# 
# NLTK tiene numerosas herramientas (que están muy bien documentadas).  
# Tenemos que tener en cuenta, que en ocasiones el formato de las palabras y textos 
# pueden estár abreviados o no están correctamente construidas a nivel sintáctico.  
# Por ejemplo:
#     
# _'Nah dawg, IDK! Wut time u headin to da club?'_
#     
# vs.
# 
# _'No dog, I don't know! What time are you heading to the club?'_
#     
# Para esos casos será necesario hacer uso de los métodos avanzados disponibles 
# en [NLTK book online](http://www.nltk.org/book/).
# 


# ######################## Vectorización ########################################

# Hasta ahora, tenemos los mensajes como una lista de tokens (también conocidas 
# como [lemas](http://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)) 
# y tenemos que convertir esos mensajes en un vector que los algoritmos de SciKit learn puedan usar.
# 
# Convertiremos ahora cada mensaje (representado como una lista de tokens (lemas)), en un vector.  
# Pasos:
# 1. Contar cuántas veces aparece cada palabra en cada mensaje (frecuencia):
# 
# 2. Ponderar las apariciones, de manera que los tokens frecuentes 'pesen' menos 
# (inversa de la frecuencia)
# 
# 3. Normalizar los vectores
# 

# El resultado que queremos obtener es una matriz de este tipo:
# 
# <table border = “1“>
# <tr>
# <th></th> <th>Mensaje 1</th> <th>Mensaje 2</th> <th>...</th> <th>Mensaje N</th> 
# </tr>
# <tr>
# <td><b>Palabra 1 Count</b></td><td>0</td><td>1</td><td>...</td><td>0</td>
# </tr>
# <tr>
# <td><b>Palabra 2 Count</b></td><td>0</td><td>0</td><td>...</td><td>0</td>
# </tr>
# <tr>
# <td><b>...</b></td> <td>1</td><td>2</td><td>...</td><td>0</td>
# </tr>
# <tr>
# <td><b>Palabra N Count</b></td> <td>0</td><td>1</td><td>...</td><td>1</td>
# </tr>
# </table>
# 
# 
# En esta matriz, representamos por filas todos los tokens (únicos) detectados 
# y por columnas cada uno de los mensajes del conjunto de datos.  
# Haremos uso de **CountVectorizer** incluido en Scikit Learn.
# 
# Debido a que no todas los tokens aparecerán en todos los mensajes, obtendremos 
# una "matriz dispersa" donde el valor más habitual es el 0 -> [Matriz dispersa](https://en.wikipedia.org/wiki/Sparse_matrix).

# In[47]:


from sklearn.feature_extraction.text import CountVectorizer


# Hay muchos argumentos y parámetros que se pueden pasar al CountVectorizer. 
# En este caso sólo especificaremos que el **analizador** sea nuestra propia 
# función previamente definida.

# In[48]:


# Éste proceso puede llevar un tiempo...
nube_palabras = CountVectorizer(analyzer = procesado_texto).fit(mensajes['mensajes'])

# Total elementos en la nube de palabras
print(len(nube_palabras.vocabulary_))


# In[49]:


# Una pequeña muestra de lo obtenido
pd.Series(nube_palabras.vocabulary_)[1:50]
# vocabulary_ es el diccionario de las palabras del modelo, y al convertirlo a 
# una Serie de pandas, puedes ver las palabras con sus índices correspondientes.

# Extraemos la nube de palabras de un mensaje como vector...

# In[50]:


mensaje4 = mensajes['mensajes'][3]
print(mensaje4)

# En formato vector tendríamos...

# In[51]:

# convierte el mensaje4 en un vector utilizando el vocabulario aprendido por el CountVectorizer.
# La salida es una matriz dispersa, donde cada elemento representa el número de veces que 
# aparece una palabra del vocabulario en el mensaje.
vector4 = nube_palabras.transform([mensaje4])
print(vector4)
print('\n')
print('Dimensiones: ',vector4.shape) # 1 mensaje, 11425 palabras en el vocabulario

# la matriz dispersa solo almacena los índices y valores de las celdas que no son cero. 
# Esto hace que sea mucho más eficiente en términos de memoria y tiempo de procesamiento.

# Vemos que en el mensaje4, hay 7 palabras únicas (tras eliminar las stop words).  
# 2 de ellas aparece dos veces, y el resto sólo una vez.  Comprobamos a qué términos 
# corresponden éstos elementos.
# Tenemos 11425 palabras únicas en la nube de palabras creada.

# In[52]:


print(nube_palabras.get_feature_names_out()[4068])
print(nube_palabras.get_feature_names_out()[9554])


# Ahora usaremos **.transform** en la nube de palabras obtenida y la convertimos en DataFrame

# In[53]:


mensajes_nube_palabras = nube_palabras.transform(mensajes['mensajes'])


# In[54]:


print('Dimensiones de la matriz dispersa: ', mensajes_nube_palabras.shape)
print('Total de elementos NO nulos: ', mensajes_nube_palabras.nnz)


# In[55]:


dispersion = (100.0 * mensajes_nube_palabras.nnz / (mensajes_nube_palabras.shape[0] * mensajes_nube_palabras.shape[1]))
print('dispersion: {}'.format(dispersion))

# Si el valor es bajo, significa que la matriz es bastante dispersa (con muchos ceros), 
# lo que es común en los análisis de texto debido a la alta dimensionalidad (muchas 
# palabras en el vocabulario, pero pocas aparecen en un solo mensaje)


# Después de obtener la matriz con la nube de palabras, necesitamos normalizar 
# lo obtenido.  El objetivo es comprobar cómo de importante es cada término respecto 
# del total y puede llevarse a cabo a través de [TF-IDF](http://en.wikipedia.org/wiki/Tf%E2%80%93idf), 
# usando `TfidfTransformer` de Scikit-learn.

# In[56]:

# TF-IDF (Term Frequency-Inverse Document Frequency): medida utilizada en NLP
# que evalúa la importancia de una palabra en un documento con respecto a todo el corpus

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer().fit(mensajes_nube_palabras)
tfidf4 = tfidf_transformer.transform(vector4)
print(tfidf4)


# ¿Cuál es el IDF (inverse document frequency) para las palabras "u" y "university"?

# In[57]:


print(tfidf_transformer.idf_[nube_palabras.vocabulary_['u']])
print(tfidf_transformer.idf_[nube_palabras.vocabulary_['university']])


# Transformamos la nube de palabras en un corpus TD-IDF de una vez:

# In[58]:


mensajes_tfidf = tfidf_transformer.transform(mensajes_nube_palabras)
print(mensajes_tfidf.shape)


# In[59]:


print(mensajes_tfidf)


# ########################## Entrenando el modelo ####################################

# Puesto que ya tenemos los mensajes reprentados como vectores, podemos entrenar 
# nuestro clasificador spam/ham. Podemos utilizar casi cualquier tipo de algoritmo 
# de clasificación.  Usaremos para este caso el clasificador Naive Bayes (http://www.inf.ed.ac.uk/teaching/courses/inf2b/learnnotes/inf2b-learn-note07-2up.pdf).
# 
# [Naive Bayes](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)

# In[60]:


from sklearn.naive_bayes import MultinomialNB
modelo_deteccion_spam = MultinomialNB().fit(mensajes_tfidf, mensajes['clase'])

# MultinomialNB() es un clasificador Naive Bayes específico para datos discretos. 
# Adecuado cuando los datos son contadores de ocurrencias o frecuencias de eventos 
# o palabras, como ocurre en la clasificación de texto 

# Ya tenemos el modelo, veamos cómo clasifica el mensaje 4:

# In[61]:


print('Predicho:', modelo_deteccion_spam.predict(tfidf4)[0])
print('Esperado:', mensajes.clase[3])


# Ya tenemos nuestro modelo clasificador de mensajes.
# 
# ###################### Evaluación del modelo ##############################3
# Comprobaremos ahora el desempeño de nuestro modelo con la predicción de todos 
# los mensajes. Tenemos que tener en cuenta que no podemos usar el mismo set de 
# datos para entrenar y testear el modelo.  Puesto que no hemos particionado los 
# datos al inicio, no podríamos comprobar el desempeño del modelo.

# ################### Train Test Split

# In[62]:


from sklearn.model_selection import train_test_split

msg_train, msg_test, clase_train, clase_test = train_test_split(mensajes['mensajes'], mensajes['clase'], test_size=0.2)

print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))


# Hemos elegido en este caso un tamaño de la muestra de test del 20% 
# (1115 mensajes de un total de 5572).

# ################################# Creación de un Pipeline
# 
# El Pipeline es el código común que generará un modelo para cualquier problema 
# de clasificación o regresión.  También generan códigos para entrenamiento y prueba , 
# transforma datos. [Pipeline](http://scikit-learn.org/stable/modules/pipeline.html)
# 
# La salida de todo el proceso es un objeto modelo, que es persistente, se puede 
# guardar y cargar para su análisis.
# 

# In[63]:


from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('nube', CountVectorizer(analyzer=procesado_texto)),  # convertir las cadenas de texto en tokens
    ('tfidf', TfidfTransformer()),  # recuento de repeticiones a puntuación TF-IDF ponderada.
    ('clasificador', MultinomialNB()),  # entrenamiento multinomial NaiveBayes
])


# 'Pasamos' ahora los mensajes de texto y pipeline realizará el preprocesamiento por nosotros:

# In[64]:


pipeline.fit(msg_train,clase_train)


# In[65]:


from sklearn.metrics import classification_report
predicciones = pipeline.predict(msg_test)


# In[66]:


cr1 = classification_report(clase_test,predicciones)

'''
El modelo tiene un buen rendimiento general, con una exactitud de 96%.
Para la clase no spam, el modelo tiene una excelente precisión y recall.
Para la clase spam, el modelo tiene una precisión perfecta (100%), pero un recall
relativamente bajo (68%). Esto significa que, aunque el modelo identifica 
correctamente los mensajes spam cuando los clasifica como spam, está perdiendo 
algunos mensajes spam que están clasificando como ham.
'''

# Si quisiéramos usar otro clasificador, es muy sencillo a través de pipeline. 
# En el siguiente ejemplo usaremos el clasficador RF

# In[67]:


from sklearn.ensemble import RandomForestClassifier
pipeline = Pipeline([
    ('nube', CountVectorizer(analyzer=procesado_texto)), 
    ('tfidf', TfidfTransformer()),  
    ('clasficador', RandomForestClassifier()),  
])


# In[68]:


pipeline.fit(msg_train,clase_train)


# In[69]:


predicciones = pipeline.predict(msg_test)


# In[70]:


cr2 = classification_report(clase_test,predicciones)

'''
Con una exactitud del 97%, el modelo tiene un buen desempeño general.
La precisión es bastante alta, especialmente para la clase spam.
El recall es perfecto para ham, pero el modelo tiene un recall relativamente 
bajo para spam (solo 77%), lo que indica que el modelo podría estar perdiendo 
algunos mensajes spam (es decir, está etiquetando algunos mensajes spam como ham).
'''
# ¿Puedes comprobar el desempeño del clasificador RF? ¿Es mejor o peor que el de NB?

# ## Más recursos
# 
# [NLTK Book Online](http://www.nltk.org/book/)
# 
# [Kaggle Walkthrough](https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words)
# 
# [SciKit Learn's Tutorial](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)


import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


# Inicializar y ajustar el vectorizador solo con los datos train
tfidf_vectorizer = TfidfVectorizer(analyzer=procesado_texto)
X_train = tfidf_vectorizer.fit_transform(msg_train)
# Transformar los datos test usando el mismo vectorizador ajustado con los datos train
X_test = tfidf_vectorizer.transform(msg_test)


# Codificar las etiquetas (spam/ham) 
le = LabelEncoder()
y_train = le.fit_transform(clase_train)  # Ajusta y transforma las etiquetas train
y_test = le.transform(clase_test)  # Solo transforma las etiquetas test usando el ajuste de entrenamiento

# Ver el mapping de las clases (orden alfabético)
print(le.classes_)

# Crear el modelo 
modelo = tf.keras.Sequential()
modelo.add(layers.Dense(64, activation='relu', input_dim=X_train.shape[1]))
modelo.add(layers.Dense(32, activation='relu'))
modelo.add(layers.Dense(1, activation='sigmoid'))


modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

modelo.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)


# Evaluamos el modelo
loss, accuracy = modelo.evaluate(X_test, y_test)
print(f"Precisión en el conjunto de prueba: {accuracy*100:.2f}%")

y_pred = (modelo.predict(X_test) > 0.5).astype("int32")

# Reporte de clasificación
cr3 = classification_report(y_test, y_pred)
print("Reporte de clasificación:\n", cr3)

