# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

# EJERCICIO 1
url_profiles = "http://olympus.realpython.org/profiles"
page_profiles = urlopen(url_profiles)
html_profiles = page_profiles.read().decode("utf-8")
soup_profiles = BeautifulSoup(html_profiles, "html.parser")

# Extraemos todos los enlaces (etiquetas <a>) y sus URLs
lista_hrefs = []
links = soup_profiles.find_all("a")

print("Lista de enlaces en la página de perfiles:")
for link in links:
    print(link["href"])
    lista_hrefs.append(link["href"])

lista_hrefs

# ----------------------------------------------------------------------------
# EJERCICIO 2

# URL de la página principal
url = "http://books.toscrape.com/"

# Abrir la URL y leer el contenido HTML
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# --- 2.1: Extraer Título y Precio de Cada Libro en la Página Principal ---
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Encuentra todos los elementos de libros en la página principal
books = soup.find_all("article", class_="product_pod")
# Otra opción: books = soup.select("article.product_pod")

# Extrae y muestra el título y el precio de cada libro
for book in books:
    # Otra opción: book_h3_a = book.find("h3 a")
    book_h3_a = book.h3.a
    book_title = book_h3_a["title"]
    book_price = book.find("p", class_="price_color").text
    print(f"Título: {book_title} - Precio: {book_price}")

# --- 2.2: Obtener Calificación y Disponibilidad de Cada Libro ---
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Encuentra todos los elementos de libros en la página principal
books = soup.find_all("article", class_="product_pod")

# Extrae y muestra el título, precio, disponibilidad y calificación de cada libro
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    
    availability = book.find("p", class_="availability").text.strip()
    # is_available = availability == 'In stock'
    
    rating = book.find("p", class_="star-rating")["class"][1]  # Segundo elemento representa la calificación
    
    print(f"Título: {title} - Precio: {price} - Disponibilidad: {availability} - Calificación: {rating}")

# --- 2.3: Guardar Información en un DataFrame ---
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Lista para almacenar datos de cada libro
data = []

# Encuentra todos los elementos de libros en la página principal
books = soup.find_all("article", class_="product_pod")

# Extrae datos y los almacena en una lista de diccionarios
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
    
    diccionario_datos_libro = {"Título": title, "Precio": price, "Disponibilidad": availability, "Calificación": rating}
    
    data.append(diccionario_datos_libro)

# Crear un DataFrame y guardar en un archivo CSV
df = pd.DataFrame(data)
df.to_csv("books_data.csv", index=False)
print(df)


# --- 2.4: Acceder a las Categorías y Contar los Libros ---

# Versión 1: contando los elementos de la primera página
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Encuentra las categorías en el menú lateral
categories = soup.find("ul", class_="nav-list").find("ul").find_all("a")

print("\nNúmero de libros en la primera página de cada categoría:")
# Recorre cada categoría para contar los libros en cada una
for category in categories:
    category_name = category.text.strip()
    category_url = "http://books.toscrape.com/" + category["href"]
    
    # Abre la URL de la categoría y cuenta los libros
    page = urlopen(category_url)
    html = page.read().decode("utf-8")
    category_soup = BeautifulSoup(html, "html.parser")
    
    # Contar el número de libros en la categoría (si hay más de una página, solo cuenta los de la primera)
    books_count = len(category_soup.find_all("article", class_="product_pod"))
    print(f"Categoría: {category_name} - Número de libros en la primera página: {books_count}")

# Versión 2: buscando el valor de un elemento
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Encuentra todas las categorías en el menú lateral
categories = soup.find("ul", class_="nav-list").find("ul").find_all("a")

print("\nNúmero de libros en cada categoría:")

# Recorre cada categoría para contar los libros en cada una
for category in categories:
    category_name = category.text.strip()
    category_url = url + category["href"]
    
    # Abre la URL de la categoría
    page = urlopen(category_url)
    html = page.read().decode("utf-8")
    
    # Buscar el número total de resultados usando una expresión regular
    # El patrón busca un número dentro de <strong> seguido de la palabra "results"
    match = re.search(r'<strong>(\d+)</strong>\s+result', html)
    if match:
        total_books = int(match.group(1))
        print(f"Categoría: {category_name} - Número de libros: {total_books}")
    else:
        print(f"Categoría: {category_name} - No se encontró el número de libros")


# --- 2.5: Extraer Datos de Todas las Páginas de una Categoría ---

# URL base de la categoría Science
# base_url = "http://books.toscrape.com/catalogue/category/books/science_22/"
base_url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/"
page_num = 1
all_books = []

while True:
    # Construimos la URL de la página actual
    if page_num == 1:
        url = base_url + "index.html"
    else:
        url = base_url + f"page-{page_num}.html"

    try:
        # Intentamos abrir la página
        page = urlopen(url)
        html = page.read().decode("utf-8")
    except:
        break  # Salir del bucle si la página no existe
    
    print(f"Visitando la página: {url}")
    
    # Parsear el HTML
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    # Extraer datos de cada libro en la página actual
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]
        all_books.append({"Título": title, "Precio": price, "Disponibilidad": availability, "Calificación": rating})

    # Verificar si hay una página siguiente
    if not soup.find("li", class_="next"):
        break  # Terminar el bucle si no hay más páginas
    
    # Pasamos a la siguiente página
    page_num += 1

# Crear un DataFrame con todos los datos y guardar en un archivo CSV
df_all_books = pd.DataFrame(all_books)
df_all_books.to_csv("science_books.csv", index=False)
print(df_all_books)
