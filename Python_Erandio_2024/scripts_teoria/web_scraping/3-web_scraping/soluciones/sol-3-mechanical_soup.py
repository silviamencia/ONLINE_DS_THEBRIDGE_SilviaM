# -*- coding: utf-8 -*-

# EJERCICIO 1 #

import mechanicalsoup
import time
import random
import re

# Crear el objeto navegador de MechanicalSoup
browser = mechanicalsoup.Browser()

# 1.1 Realizar el inicio de sesión
login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
form = login_page.soup.select("form")[0]
form.select("input")[0]["value"] = "zeus"          # Usuario: zeus
form.select("input")[1]["value"] = "ThunderDude"   # Contraseña: ThunderDude

# Enviar el formulario para iniciar sesión
response = browser.submit(form, login_url)

# 1.2 Comprobar el código de respuesta de la nueva página
response.status_code 
# Si fuese distinto de 200, podríamos mostrar un error y finalizar el script

# También podemos verificar si el inicio de sesión fue exitoso mirando la url
if "profiles" in response.url:
    print("Inicio de sesión exitoso.")
else:
    print("Error en el inicio de sesión.")

# 1.3 Navegar a los perfiles de usuario
profile_urls = [
    "http://olympus.realpython.org/profiles/dionysus",
    "http://olympus.realpython.org/profiles/poseidon",
    "http://olympus.realpython.org/profiles/apollo" # <- va a fallar con 404
]

# 1.4 Extraer y mostrar información de cada perfil con espera entre solicitudes
for url in profile_urls:        
    print(f"\nNavegando a: {url}")
    profile_page = browser.get(url)
    
    if profile_page.status_code != 200:
        print(f"Error al obtener la página, código: {profile_page.status_code}")
        continue
    
    # Extraer datos del perfil
    profile_soup = profile_page.soup
    
    title = profile_soup.title.string.replace("Profile: ", "").strip()
    name = profile_soup.find(string=re.compile(r"Name:")).string.replace("Name: ", "").strip()
    hometown = profile_soup.find(string=re.compile(r"Hometown:")).string.replace("Hometown: ", "").strip()
    favorite_animal = profile_soup.find(string=re.compile(r"Favorite animal:")).string.replace("Favorite animal: ", "").strip()
    
    # Mostrar los datos extraídos
    print(f"Perfil: {title}")
    print(f"Nombre: {name}")
    print(f"Lugar de origen: {hometown}")
    print(f"Animal favorito: {favorite_animal}")
    
    # Aplicamos la espera sólo si no es el último enlace
    if url != profile_urls[-1]:
        # Espera aleatoria entre 2 y 3 segundos
        wait_time = random.uniform(2, 3)
        print(f"\nEsperando {wait_time:.2f} segundos...")
        time.sleep(wait_time)
        

# -----------------------------------------------------------------------------
# EJERCICIO 2 #

import mechanicalsoup
import pandas as pd
import time
import random

# Crear el navegador y la URL inicial
browser = mechanicalsoup.Browser()
url = "http://books.toscrape.com/"
page = browser.get(url)
soup = page.soup

# 2.1 y 2.2 Extraer Título, Precio, Calificación y Disponibilidad de cada libro
books = soup.find_all("article", class_="product_pod")
data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
    data.append({"Título": title, "Precio": price, "Disponibilidad": availability, "Calificación": rating})

# 2.3 Guardar en un DataFrame
df = pd.DataFrame(data)
print(df)

# 2.4 Acceder a las categorías
categories = soup.find("ul", class_="nav-list").find("ul").find_all("a")
MAX_CATEGORIES = 5
for i, category in enumerate(categories):
    if i >= MAX_CATEGORIES:
        print("Se ha alcanzado el máximo de categorías que se quería recorrer.")
        break
    
    category_name = category.text.strip()
    category_url = url + category["href"]
    category_page = browser.get(category_url)
    
    # Espera aleatoria entre 1 y 2 segundos
    time.sleep(random.uniform(1, 2))

    category_soup = category_page.soup
    books_count = len(category_soup.find_all("article", class_="product_pod"))
    print(f"Categoría: {category_name} - Número de libros: {books_count}")

# 2.5 Extraer Datos de Todas las Páginas de una Categoría
category_url = url + "catalogue/category/books/sequential-art_5/index.html"
page_num = 1
all_books = []

while True:
    page_url = f"{url}catalogue/category/books/sequential-art_5/page-{page_num}.html"
    
    try:
        category_page = browser.get(page_url)
        if (category_page.status_code != 200):
            raise Exception(f"Error: {category_page.status_code}")
        
        print(f"Visitando: {page_url}")
        category_soup = category_page.soup
        books = category_soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            rating = book.find("p", class_="star-rating")["class"][1]
            all_books.append({"Título": title, "Precio": price, "Disponibilidad": availability, "Calificación": rating})
        
        page_num += 1
        time.sleep(random.uniform(1, 2))  # Espera aleatoria entre solicitudes
    except:
        print("Ya no hay más páginas")
        break  # Terminar el bucle cuando no haya más páginas

# Guardar todos los datos de la categoría en un CSV
df_all_books = pd.DataFrame(all_books)
df_all_books.to_csv("science_books.csv", index=False)
print(df_all_books)
        


# -----------------------------------------------------------------------------
# EJERCICIO 3 #

import mechanicalsoup
import time
import random

# Crear navegador
browser = mechanicalsoup.Browser()
url = "https://www.scrapethissite.com/pages/forms/?per_page=5"
page = browser.get(url)
soup = page.soup

# 3.1 Búsquedas para cada equipo
teams = ["Colorado", "Ottawa", "Florida"]

for team in teams:
    page = 1
    num_pages = 1
    results = {
        "wins": {
            "years": [],
            "qt": 0,
        },
        "losses": {
            "years": [],
            "qt": 0,
        },
    }
    
    form = soup.select("form")[0]
    form.select("input[name='q']")[0]["value"] = team
    results_page = browser.submit(form, url)
    results_soup = results_page.soup

    print(f"\nBuscando resultados para: {team}")
    
    # Obtener el número de páginas
    pagination = results_soup.select("ul.pagination")
    if pagination:
        num_pages = len(pagination[0].find_all("li")) - 1 # Excluimos el botón "Siguiente"

    max_wins = 0
    max_losses = 0
    goals_for = 0
    goals_against = 0

    while page <= num_pages:
        if page > 1:
            wait_time = random.uniform(1, 2)
            print(f"Esperando {wait_time:.2f} segundos antes de la siguiente página...")
            time.sleep(wait_time)

            # Reemplazamos el valor del parámetro num_page o lo añadimos si no existe
            current_url = results_page.url
            if "page_num" in current_url:
                next_url = current_url.replace(f"page_num={page - 1}", f"page_num={page}")
            else:
                next_url = f"{current_url}&page_num={page}"

            results_page = browser.get(next_url)
            results_soup = results_page.soup
        
        print(f"Página {page}: {results_page.url}")
        page += 1 # Importante incrementar la página para evitar bucle infinito
        rows = results_soup.select("tr.team")

        for row in rows:
            year = row.find("td", class_="year").text.strip()
            wins = int(row.find("td", class_="wins").text.strip())
            losses = int(row.find("td", class_="losses").text.strip())
            goals_for += int(row.find("td", class_="gf").text.strip())
            goals_against += int(row.find("td", class_="ga").text.strip())
            
            # Calcular año con más victorias y derrotas
            if wins > max_wins:
                max_wins = wins
                max_wins_year = year
                results["wins"]["years"] = [year]
                results["wins"]["qt"] = wins
            elif wins == max_wins:
                results["wins"]["years"].append(year)
                
            if losses > max_losses:
                max_losses = losses
                max_losses_year = year
                results["losses"]["years"] = [year]
                results["losses"]["qt"] = wins
            elif losses == max_losses:
                results["losses"]["years"].append(year)

    # Calcular promedio de goles a favor y en contra
    avg_goals_for = goals_for / len(rows)
    avg_goals_against = goals_against / len(rows)

    # Mostrar resultados
    print(f"\nEquipo: {team}")
    if len(results["wins"]["years"]) == 0:
        print("Sin registros")
    else:
        print(f"Año(s) con más victorias: {", ".join(results["wins"]["years"])} ({results["wins"]["qt"]} victorias)")
        print(f"Año(s) con más derrotas: {", ".join(results["losses"]["years"])} ({results["losses"]["qt"]} derrotas)")
        print(f"Promedio de goles a favor: {avg_goals_for:.2f}")
        print(f"Promedio de goles en contra: {avg_goals_against:.2f}")

    if team != teams[-1]:
        wait_time = random.uniform(1, 2)
        print(f"\nEsperando {wait_time:.2f} segundos antes de la siguiente búsqueda...")
        time.sleep(wait_time)  # Espera entre búsquedas
    
    
    
# -----------------------------------------------------------------------------
# EJERCICIO 4 #
    
import mechanicalsoup
import time
import random
import pandas

# Crear navegador de MechanicalSoup
browser = mechanicalsoup.Browser()

# URL base con el parámetro per_page configurado a 100 (puedes cambiarlo a cualquier valor)
base_url = "https://www.scrapethissite.com/pages/forms/?per_page=100"
next_url = base_url + "&page_num=1"

# Variables para almacenar datos y hacer seguimiento del equipo con más victorias
max_wins = 0
team_with_max_wins = ""
all_teams_data = []

# Recorrer todas las páginas con la configuración de per_page
while True:
    page = browser.get(next_url)
    soup = page.soup
    
    print(f"Visitando {page.url}")
    
    # Seleccionar todas las filas de equipos
    rows = soup.select("tr.team")

    # Extraer y analizar los datos de cada equipo en la página actual
    for row in rows:
        team_name = row.find("td", class_="name").text.strip()
        year = row.find("td", class_="year").text.strip()
        wins = int(row.find("td", class_="wins").text.strip())
        losses = int(row.find("td", class_="losses").text.strip())
        
        # Guardar cada equipo y sus datos en una lista
        all_teams_data.append({
            "Equipo": team_name,
            "Año": year,
            "Victorias": wins,
            "Derrotas": losses
        })
        
        # Calcular el equipo con más victorias
        if wins > max_wins:
            max_wins = wins
            team_with_max_wins = team_name

    # Buscar el botón de "Siguiente" para avanzar a la siguiente página (a con aria-label="Next")
    next_button = soup.select_one("a[aria-label='Next']")
    if not next_button:
        print("No hay más páginas que visitar")
        break  # Terminar el bucle si no hay botón de "Siguiente"

    # Construir la URL de la siguiente página
    next_url = "https://www.scrapethissite.com" + next_button["href"]

    # Esperar un tiempo aleatorio entre 1 y 2 segundos para simular comportamiento humano
    time.sleep(random.uniform(1, 2))

# Mostrar los resultados finales
print(f"\nEl equipo con más victorias es {team_with_max_wins} con {max_wins} victorias.")
print("\nDatos de todos los equipos extraídos:")
df = pandas.DataFrame(all_teams_data)
print(df)

print("\nPrimeros 5 equipos con más victorias:")
df_sorted = df.sort_values(by="Victorias", ascending=False)
print(df_sorted.head())

print("\nÚltimos 5 equipos con más derrotas:")
df_sorted = df.sort_values(by="Derrotas", ascending=False)
print(df_sorted.head())

# Extra: ¿se pueden mostrar más de 100 elementos por página? ¿cómo?
# Sí, podemos hacerlo modificando el parámetro de url per_page, esto nos permite indicar un número
# distinto a los preestablecidos en el seleccionador
#
# Como el servidor web no valida la entrada, podemos indicarle que busque 1000, y recogerá 1000
#
# Otras páginas web sí que validarán estas modificaciones asegurando que no se carguen más de X registros
# para evitar cierta carga en el servidor.
