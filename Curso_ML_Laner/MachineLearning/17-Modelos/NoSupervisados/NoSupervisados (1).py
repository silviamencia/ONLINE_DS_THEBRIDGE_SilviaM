# Clusterizacion

%reset

import os
import pandas as pd
#os.chdir(r"C:\Users\borja\OneDrive\Documents\Formacion_Python\17-Modelos\NoSupervisados")
os.chdir(r"C:\Users\LENOVO\Documents\DataVM\CursoPythonCompleto\17-Modelos\NoSupervisados")
data = pd.read_csv("wholesale.csv")


# El primer paso es normalizar los datos.

from sklearn import preprocessing
datosNorm1=preprocessing.scale(data)
datosNorm1=pd.DataFrame(datosNorm1)
datosNorm1.columns=data.columns

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(data)
datosNorm=scaler.transform(data)
datosNorm =pd.DataFrame(datosNorm)
# guarda la media y la std de cada variable: scaler.mean_ o scaler.scale_

# Eliminamos las variables que no interesan

datosNorm1 = datosNorm1.drop(['Channel'], axis = 1)
datosNorm1 = datosNorm1.drop(['Region'], axis = 1)
  
from sklearn.cluster import KMeans

KNN = KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,n_clusters=4, n_init=10,random_state=None, tol=0.0001, verbose=0)

KNN.fit(datosNorm1)

centros = KNN.cluster_centers_
centros=pd.DataFrame(centros)
centros.columns=datosNorm1.columns

data["cluster"] = KNN.fit_predict(data)
datosNorm1["cluster"] = KNN.fit_predict(datosNorm1)


####################################################################
# Buscar el número ÓPTIMO de CLUSTERES en el conjunto de datos
####################################################################

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Generamos una lista de SSE para diferentes valores de K
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(datosNorm1) 
    sse.append(kmeans.inertia_)

plt.plot(range(1, 11), sse, marker='o')
plt.title('Método del Codo')
plt.xlabel('Número de Clústeres')
plt.ylabel('SSE')
plt.show()



#######################################
# ejemplo IRIS dataset
#######################################

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

iris_df = datasets.load_iris()

model = KMeans(n_clusters=3, random_state=42)
model.fit(iris_df.data)

# Predecir las etiquetas de los clústeres
predicted_labels = model.predict(iris_df.data)

# Seleccionar dos características del conjunto de datos
x = iris_df.data[:, 0]  # Longitud del sépalo 
y = iris_df.data[:, 2]  # Longitud del pétalo 

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=predicted_labels)
plt.title('Clusters generados por K-Means')
plt.xlabel('Longitud del sépalo')
plt.ylabel('Longitud del pétalo')
plt.show()






######################################################################
# Para datos categóricos
######################################################################

from kmodes.kmodes import KModes
import numpy as np
import pandas as pd

data = {
    'Color': ['Rojo', 'Azul', 'Verde', 'Rojo', 'Azul', 'Rojo'],
    'Tamaño': ['Pequeño', 'Grande', 'Mediano', 'Grande', 'Mediano', 'Pequeño'],
    'Forma': ['Círculo', 'Círculo', 'Cuadrado', 'Triángulo', 'Cuadrado', 'Círculo']
}


data_df = pd.DataFrame(data)

kmodes = KModes(n_clusters=2, init='Huang', random_state=42)
clusters = kmodes.fit_predict(data_df)

print("Etiquetas de los clusters:", clusters)
print("Centroides:", kmodes.cluster_centroids_)



#########
# Buscar el número ÓPTIMO de CLUSTERES 
#########

import matplotlib.pyplot as plt

# Convertir las categorías en números
data_encoded = data_df.apply(lambda x: pd.Categorical(x).codes)

'''
La clase Categorical de pandas es muy útil cuando trabajas con datos que tienen un 
número limitado de categorías y te permite aprovechar su eficiencia tanto en memoria 
como en tiempo de procesamiento. 

En los modelos supervisados usábamos "get_dummies" para asegurarnos que el modelo 
no asumiera ninguna relación ordinal entre las categorías.En caso contrario,
podrían asumir que hay una relación ordinal entre ellos, lo que no es cierto.
'''

# Lista para guardar el coste (suma de las distancias de Hamming) para cada número de clústeres
coste = []

for k in range(1, 7):
    kmodes = KModes(n_clusters=k, init='Huang', random_state=42)
    kmodes.fit(data_encoded)
    coste.append(kmodes.cost_)


plt.plot(range(1, 7), coste, marker='o')
plt.xlabel('Número de Clústeres (k)')
plt.ylabel('Coste Total (Distancia de Hamming)')
plt.show()






############################################
# Reglas de asociacion.
############################################
 %reset 
 

data = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
        ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
        ['Milk', 'Apple', 'Kidney Beans', 'Eggs'], 
        ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
        ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]


import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# convierte las listas en una matriz de formato binario
te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Buscamos conjuntos de items frecuentes, que aparezcan al menos en el 60% de las transacciones
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

from mlxtend.frequent_patterns import association_rules

# se generan reglas de asociación a partir de los conjuntos frecuentes
reglas = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)






####################################################
# EJEMPLO K-Means PARA TEXTOS
####################################################

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
    "El perro juega con la pelota",
    "El gato salta al tejado",
    "La pelota rueda en el parque",
    "El perro persigue al gato",
    "El gato observa desde el tejado",
    "El perro duerme en la casa"
]

# Vectorización TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()
X_df = pd.DataFrame(X_array, columns=feature_names)

'''
Inicialmente cada documento se representa como un vector de frecuencias de palabras.

En X_df los valores indican la importancia (TF-IDF) de cada palabra en el documento.
Los valores altos de TF-IDF identifican palabras que son importantes en un documento
pero no comunes en el conjunto. Valores bajos indican palabras poco relevantes o comunes.

TF-IDF combina dos métricas:
    1) TF (Term Frequency): 
        La frecuencia con la que aparece una palabra en un documento específico.
    2) IDF (Inverse Document Frequency):
        Mide qué tan común o rara es una palabra en todos los documentos del conjunto.
'''

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Predicciones de los clusters
labels = kmeans.labels_


######################################################

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
    "Football match results and highlights",
    "New smartphone technology and innovations",
    "World Cup qualifiers and football teams",
    "Advances in artificial intelligence technology"
]


vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Palabras más representativas de cada cluster
terms = vectorizer.get_feature_names_out()
clusters = kmeans.cluster_centers_.argsort()[:, ::-1]

# Interpretación manual de temas
for i, cluster in enumerate(clusters):
    print(f"Cluster {i}:")
    print(", ".join([terms[ind] for ind in cluster[:5]]))


# deporte y tecnología
'''
Las stop words son palabras comunes en un idioma que tienen poco o ningún valor para
el análisis de datos de texto. artículos, preposiciones, conjunciones...
suelen eliminarse para evitar ruido y centrar el análisis en palabras más significativas.

Los centroides son vectores, y los valores en este vector indican la importancia de 
cada palabra para ese cluster.
'''

