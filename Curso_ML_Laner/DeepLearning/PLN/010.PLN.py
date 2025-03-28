#!/usr/bin/env python
# coding: utf-8

# # PLN (Procesamiento del lenguaje natural) con Python - Recetas
#   
# **Requisitos: Será necesario instalar la librería NLTK, además de descargar el 
# corpus para las stopwords. Por defecto Conda incluye el paquete NLTK así como 
# Google Colab.  En el caso de que no estuviera instalado NLTK, ejecutar el siguiente chunk**

# In[1]:


# Ejecutar este chunk sólo si no está instalado NLTK
# Descomentar la siguiente línea para instalar la libraría:

#!conda install nltk 


# In[1]:


import nltk


# In[3]:


nltk.download_shell() # abre una interfaz interactiva para descargar recursos de NLTK
#d) DOwnload:
#stopwords


# ######################## 1.DESCARGA DE UN CORPUS EXTERNO #################################

# Descargaremos el set de datos de películas Cornell CS Movie.  
# Incluye valoraciones positivas y negativas de diferentes películas. 
# Los datos pueden descargarse desde:
# http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens_cleaned.zip

# In[2]:


from nltk.corpus import CategorizedPlaintextCorpusReader 
# para cargar un corpus de texto previamente categorizado


# El corpus ya está categorizado por múltiples ficheros de texto con revisiones 
# positivas y negativas), por eso usamos **CategorizedPlaintextCorpusReader** en este caso. 
# Más adelante trabajaremos con datos que no lo están. La clase CategorizedPlainCorpusReader, 
# nos permite cargar los datos manteniendo la categorización.

# In[3]:


reader = CategorizedPlaintextCorpusReader(r'C:\Users\LENOVO\Documents\DataVM\Cursos\DL_BED_2024-20241218T074932Z-001\DL_BED_2024\scripts\datos\movies\tokens', r'.*\.txt', cat_pattern=r'(\w+)/*', encoding='cp1252')
# (\w+)/*: extrae la categoría desde la estructura de carpetas
#reader = CategorizedPlaintextCorpusReader(r'C:\Users\german\Documents\00.Trabajo\01.C2B\41.Bootcamp Cámara Comercio - C2B 2023 (220h)\Módulo DL\scripts\datos\movies\tokens', r'.*\.txt', cat_pattern=r'(\w+)/*', encoding='cp1252')
print(reader.categories()) # devuelve las categorías extraídas de la estructura del corpus
print(reader.fileids()[1:50]) # devuelve la lista de archivos cargados


# Generamos los datos con revisión positiva y negativa

# In[4]:


posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')


# In[5]:


posFiles [1:10]


# Vamos a extraer de manera aleatoria los nombres de 2 ficheros 
# (uno con revisión negativa y otro positiva).

# In[6]:


from random import randint
fileP = posFiles[randint(0,len(posFiles)-1)]
fileN = negFiles[randint(0, len(posFiles) - 1)]
print(fileP)
print(fileN)


# Imprimimos cada fichero...

# In[7]:


for w in reader.words(fileP):
    print(w + ' ', end='')
    if (w is '.'):
        print()


# In[8]:


for w in reader.words(fileN):
    print(w + ' ', end='')
    if (w is '.'):
        print()


# ####################### 2.CONTANDO TODAS LAS PALABRAS 'wh' ##############################
# 
# Usaremos en este caso el corpus 'Brown' incluido en el paquete NLTK.  
# Contiene aproximadamente 500 textos categorizados en 15 diferentes géneros y 
# categorías (noticias, humor, ...).

# In[9]:


import nltk
from nltk.corpus import brown


# Descargamos el set de datos.

# In[10]:


nltk.download('brown')


# Las categorías existentes en el set de datos son:

# In[11]:


print(brown.categories())


# Seleccionamos 3 géneros, así como las palabras que queremos contar.

# In[12]:


generos = ['fiction', 'humor', 'romance']
palabraswh = ['what', 'which', 'how', 'why', 'when', 'where', 'who']


# In[14]:


for i in range(0,len(generos)):
    genero = generos[i]
    print()
    print("Analizando "+ genero)
    texto_generos = brown.words(categories = genero) 
    # Se extraen todas las palabras (tokens) del género especificado
    print (texto_generos)


# Hemos extraído para cada género los textos en brown.  Ahora comprobaremos la 
# distribución de frecuencias, para cada categoría seleccionada.

# In[16]:


for i in range(0,len(generos)):
    genero = generos[i]
    print()
    print("Analizando '"+ genero)
    texto_generos = brown.words(categories = genero)
    print (texto_generos)
    fdist = nltk.FreqDist(texto_generos) 
    # distribución de frecuencia de las palabras en ese género
    print (fdist)


# Samples -> Total muestras en los datos con el género buscado. Número de palabras únicas
# Outcomes -> Total de elementos existentes en las muestras (tokens o palabras). Número total de palabras 
# 
# Podemos hacer lo mismo, para las palabras wh

# In[17]:


for wh in palabraswh:
    print(wh + ':', fdist[wh], end=' ')


# Estamos iterando palabraswb y obteniendo el total de ocurrencias de cada caso 
# (what aparece 121 veces en la categoría romance, which 104, ...).  
# Juntando todos los pasos...

# In[18]:


print(brown.categories())
for i in range(0,len(generos)):
    genero = generos[i]
    print()
    print("Analizando '"+ genero+"'")
    texto_generos = brown.words(categories = genero)
    fdist = nltk.FreqDist(texto_generos)
    for wh in palabraswh:
        print(wh + ':', fdist[wh], end=' ')



######## 3.ANALIZAR LA DISTRIBUCIÓN DE FRECUENCIAS DE CORPUSES EN LA WEB Y EN FICHEROS DE CHATS
# 
# Aprovecharemos el set de datos webtext de la librería NLTK

# In[19]:


import nltk
from nltk.corpus import webtext
nltk.download('webtext')
# un conjunto de textos recopilados de diversas fuentes web, como chats, foros y anuncios

# In[20]:


print(webtext.fileids())


# Analizamos el set singles.txt (mensajes de un sitio de citas), que va a ser 
# nuestro conjunto de datos "objetivo".

# In[21]:


fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)
print (fdist)


# Podemos extraer la palabra más común...

# In[22]:


print('Total de apariciones del token "',fdist.max(),'" : ', fdist[fdist.max()])


# Podemos extraer el total de tokens diferentes en nuestro corpus

# In[23]:


print('Total de tokens distintos en el corpus: ', fdist.N())


# In[26]:


fdist


# Extraemos los 10 tokens más habituales en el corpus

# In[24]:


print('Los 10 tokens más comunes del corpus:', fdist.most_common(10))


# Pintamos una gráfica con las frecuencias acumuladas de los 20 elementos más habituales.

# In[25]:


fdist.plot(20,cumulative=True)


# Hemos visto que el token más común es ',', seguido de '.' debido a que no hemos 
# preprocesado los datos (eliminación de stopwords, ...).



# ############## 4.EXTRACCIÓN DE TEXTOS A TRAVÉS DE BEAUTIFULSOUP ##################

# La librería BeautifulSoup tiene unas potentes funciones para el tratamiento de textos.  
# Vamos usarla para limpiar el texto descargado desde una web.

# In[27]:


import nltk
import urllib.request


# In[28]:


response = urllib.request.urlopen('http://php.net/')
html = response.read()
print (html)
# Imprime el contenido de la página, pero en bytes y con etiquetas HTML (estructuran 
# y dan formato a una página web) incluidas.
# Para una mejor visualización, conviene decodificarlo.

# HTML es un lenguaje de marcado, lo que significa que utiliza etiquetas para 
# indicar cómo se debe mostrar el contenido en un navegador.


# El resultado contiene muchas etiquetas HTML que deben limpiarse.  
# En este caso usaremos BeautifulSoup

# In[29]:


#pip install bs4


# In[29]:

from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('http://php.net/')
html = response.read()
#soup = BeautifulSoup(html,"html5lib")
# extraemos el texto sin etiquetas
soup = BeautifulSoup(html,"html.parser") 

text = soup.get_text(strip=True) # Extraer solo el texto visible

print (text)


# Hemos eliminado a través de BeautifulSoup aquellas referencias html del texto.  
# Seguimos.  Extraemos los tokens del texto.

# In[30]:


tokens = [t for t in text.split()]
tokens [1:20]


# Contamos la frecuencia de palabras...

# In[31]:


freq = nltk.FreqDist(tokens)

for key,val in freq.items():
    print (str(key) + ':' + str(val))


# ¿Cuáles son los token más frecuentes?

# In[32]:


freq.plot(20, cumulative=False) # frecuencia individual de cada palabra


# Eliminamos StopWords (palabras comunes en un idioma que no aportan mucho significado 
# o información relevante en el análisis de texto)

# In[33]:

nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')


# In[34]:


from nltk.corpus import stopwords
stopwords.words('spanish')


# Convertimos todo a minúsculas...

# In[35]:


tokens = [x.lower() for x in tokens]


# In[36]:


tokens_limpios = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        tokens_limpios.remove(token)


# Extraemos los tokens más habituales...

# In[37]:


freq = nltk.FreqDist(tokens_limpios)
for key,val in freq.items():
    print (str(key) + ':' + str(val))


# In[38]:


freq.plot(20,cumulative=False)



# ############### 5.LEER PDFS, DOCS Y TXT CON PYTHON Y GENERAR UN CORPUS ####################

# Es necesario instalar para este caso, la librería PyPDF2 y la librería word

# In[41]:


#pip install docx2python


# In[41]:


#pip install PyPDF2
## pip install word
## pip install pdfminer.six


# In[42]:


#pip install pdfminer
#conda install pdfminer


# Importamos las clases que nos permiten leer pdf y docs

# In[42]:


import os
#import PyPDF2
import pdfminer as pdfm
from docx2python import docx2python
#from PyPDF2 import PdfFileReader
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


# Generamos una función que nos devuelva el contenido de texto de un fichero de texto.

# In[43]:


def obtener_texto(nombre_txt):
    archivo = open (nombre_txt, 'rb') # apertura del fichero en modo binario
    return archivo.read()
ruta = get_ipython().run_line_magic('pwd', '')
# se usa principalmente en Jupyter Notebooks para obtener y trabajar con la ruta del directorio de trabajo actual.


# In[44]:


ruta


# In[45]:


#txt1 = obtener_texto(ruta + '/datos/reading/ejemplo_feed.txt')
txt1 = obtener_texto(r'C:\Users\LENOVO\Documents\DataVM\Cursos\DL_BED_2024-20241218T074932Z-001\DL_BED_2024\scripts\datos\reading\ejemplo_feed.txt')

# In[46]:


txt1


# In[47]:


from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO() 
# Crea un objeto de memoria donde se va a guardar el texto extraído del PDF.
#with open(ruta +'/datos/reading/ejemplo-una-linea.pdf', 'rb') as in_file:
with open(r'C:\Users\LENOVO\Documents\DataVM\Cursos\DL_BED_2024-20241218T074932Z-001\DL_BED_2024\scripts\datos\reading\ejemplo-una-linea.pdf', 'rb') as in_file:
    parser = PDFParser(in_file) #Crea un parser para leer el contenido del archivo PDF
    doc = PDFDocument(parser) #te permite trabajar con el contenido del archivo PDF
    rsrcmgr = PDFResourceManager() #Manejo de recursos necesarios para procesar el documento
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams()) 
    #convertidor de texto que extrae el contenido de las páginas del PDF
    interpreter = PDFPageInterpreter(rsrcmgr, device) 
    #Interpretador que toma el contenido de las páginas y lo procesa usando el convertidor de texto
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page) #Procesa cada página y convierte su contenido en texto

txt2 = output_string.getvalue()

## Un parser es un componente que lee y analiza datos de entrada, transformándolos 
## en una estructura organizada para que pueda ser comprendida y manipulada por un programa.

# In[48]:


txt2


# In[49]:


# Ejecutar sólo en linux/mac
txt2 = txt2 [:-4]


# In[50]:


txt2


# In[51]:


#txt3 = docx2python(ruta + '/datos/reading/ejemplo-una-linea.docx')
txt3 = docx2python(r'C:\Users\LENOVO\Documents\DataVM\Cursos\DL_BED_2024-20241218T074932Z-001\DL_BED_2024\scripts\datos\reading\ejemplo-una-linea.docx')
txt3.body


# In[52]:


txt3=txt3.body[0][0][0][0]


# In[53]:


txt3


# Guardamos el resultado en nuestro equipo en una carpeta llamada _micorpus_.

# In[54]:


nuevocorpus = 'micorpus/'
if not os.path.isdir(nuevocorpus): # existe nuevocorpus?
    os.mkdir(nuevocorpus) #si no existe crea este directorio


# Guardamos los 3 ficheros cargados previamente.

# In[55]:


files = [txt1,txt2,txt3]  # Generación array con objetos a usar en la iteración.
files


# In[56]:


for idx, f in enumerate(files):  
    with open(nuevocorpus+str(idx)+'.txt', 'w') as fileout:
        fileout.write(str(f))

# Crea un archivo de texto nuevo en el directorio nuevocorpus con un nombre único, 
# basado en el índice del archivo (por ejemplo, "0.txt", "1.txt").
# Escribe el contenido de cada archivo en su respectivo archivo de texto en ese directorio.
print("Ruta actual de trabajo:", os.getcwd())

# Generamos el corpus.  Aquí se identifican internamente los párrafos, sentencias, palabras, ...

# In[57]:


#corpus = PlaintextCorpusReader (ruta +'/datos/reading/', '.*')
corpus = PlaintextCorpusReader(r'C:\\Users\\LENOVO\\Documents\\DataVM\\Cursos\\DL_BED_2024-20241218T074932Z-001\\DL_BED_2024\\scripts\\datos\\reading\\', '.*')

# In[58]:


print (corpus.words())


# Para poder extraer las sentencias del corpus, necesitamos instalar un paquete...

# In[59]:


import nltk
nltk.download('punkt') #punkt es un modelo para hacer la tokenizacion


# In[64]:


corpus.fileids()[0]


# In[65]:


print(corpus.paras(corpus.fileids()[0]))


# ################ 6. TOKENIZAR TEXTOS QUE NO ESTÁN EN INGLÉS ###################

# El proceso de TOKENIZACIÓN consiste en dividir un texto en unidades básicas de 
# análisis llamadas TOKENS.

# In[66]:


from nltk.tokenize import sent_tokenize
texto = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."

print(sent_tokenize(texto,"french")) 
# para dividir un texto en oraciones. El tokenizador usa un modelo entrenado en lengua francesa


# ################# 7. OBTENCIÓN DE SINÓNIMOS (Wordnet) ############################

# In[67]:

nltk.download('wordnet')
from nltk.corpus import wordnet 
# base de datos léxica que agrupa los sustantivos, verbos, adjetivos y adverbios 
# en sinónimos y otros grupos de palabras relacionadas

# WordNet es muy útil en procesamiento de lenguaje natural (NLP) para encontrar 
# sinónimos, antónimos y relaciones semánticas entre palabras. 

syn = wordnet.synsets("happy") #  lista de sinónimos 
print(syn[0].definition())
print(syn[0].examples())


# In[68]:


syn


# In[69]:


syn = wordnet.synsets("python") 
print(syn[0].definition())
print(syn[0].examples())


# In[70]:


syn


# In[71]:

# LEMATIZACIÓN: te devuelve la palabra en la forma base o canónica

sinonimos = []

for syn in wordnet.synsets('happy'):
    for lemma in syn.lemmas(): # obtener los lemas (formas base o canónicas) de un synset (conjunto de sinónimos)
        sinonimos.append(lemma.name())

print(sinonimos)

# Eliminamos duplicados
print([*set(sinonimos)])


# ################## 8. EXTRACCIÓN DE LEMAS USANDO WORDNET #########################

# In[72]:


from nltk.stem import WordNetLemmatizer

lema = WordNetLemmatizer()
print(lema.lemmatize('increases'))


# Puede suceder que una misma palabra sea un sustantivo o verbo en función del contexto.  
# Podemos indicarle al lematizador, que nos devuelva el lema para una palabra que sea un verbo.

# In[73]:


print(lema.lemmatize('playing', pos="v"))


# ¿Y si le pedimos que nos devuelva los lemas en función de los diferentes contextos?...

# In[74]:


print(lema.lemmatize('playing', pos="v")) # verbos
print(lema.lemmatize('playing', pos="n")) # sustantivos
print(lema.lemmatize('playing', pos="a")) # adjetivos
# no es un adjetivo, por lo que el lematizador lo conserva sin cambios




# ######## 9. EXTRACCIÓN DE STEMS (raices) para otro idioma distinto al inglés ##################

# En el procesamiento del lenguaje natural (NLP), un "stem" (o raíz) se refiere a 
# la forma básica o raíz de una palabra, que puede ser común a múltiples formas 
# flexionadas de la misma palabra. Por ejemplo, el stem de las palabras "corriendo", 
# "corrió" y "correrá" sería "corr".
# 
# El proceso de encontrar el stem de una palabra se llama "STEMMING". 
# El objetivo del stemming es reducir una palabra a su forma base o raíz para que 
# las palabras relacionadas puedan ser agrupadas bajo una única forma.
# 
# Es importante tener en cuenta que el stemming no siempre produce raíces válidas 
# o significativas. Puede generar resultados truncados o incompletos, ya que simplemente 
# corta o elimina sufijos o prefijos de las palabras sin tener en cuenta el contexto 
# o la semántica.

# In[75]:


from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)


# In[76]:


castellano = SnowballStemmer('english')
print(castellano.stem("palabrita"))


# No ha funcionado.

# In[77]:


castellano = SnowballStemmer('spanish')
print(castellano.stem("palabrite"))



# ############ 10. EXTRACCIÓN DE STEMS (raices) Y LEMAS (formas canónicas) ###############

# En NLP, un "lemma" (o lema) es la forma base o canónica de una palabra, es decir, 
# la forma en la que aparecería en un diccionario. A diferencia del stemming, 
# que simplemente trunca palabras para encontrar su raíz, el lemmatization busca 
# la forma base de una palabra teniendo en cuenta su significado y contexto en la oración.

# In[72]:


from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

steams = PorterStemmer()
lemas = WordNetLemmatizer()

print(steams.stem('stones'))
print(steams.stem('speaking'))
print(steams.stem('bedroom'))
print(steams.stem('jokes'))
print(steams.stem('lisa'))
print(steams.stem('purple'))
print('----------------------')
print(lemas.lemmatize('stones'))
print(lemas.lemmatize('speaking'))
print(lemas.lemmatize('bedroom'))
print(lemas.lemmatize('jokes'))
print(lemas.lemmatize('lisa'))
print(lemas.lemmatize('purple'))

