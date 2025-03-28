# -*- coding: utf-8 -*-

## Interactuar con páginas web en tiempo real ##

"""
Una de las buenas prácticas cuando hacemos web scraping es añadir tiempos de espera
entre cada interacción o navegación por una página web.

De esta manera, estamos simulando un comportamiento humano (evitando así ser 
detectados y bloqueados automáticamente) y también estamos respetando la carga
de trabajo que le damos al servidor web.

Objetivo del ejemplo:
    Scrapear una página web en la que se simula la tirada de un dado.
    Recargar la página para obtener un nuevo resultado de la tirada.
"""


# Importamos MechanicalSoup para navegar en la web y simular solicitudes
import mechanicalsoup

# En primer lugar, identificamos el elemento HTML que contiene el resultado de la tirada
# En el código fuente de la página, encontramos el siguiente elemento:
# <h2 id="result">1</h2>
# Este elemento tiene un id="result", que usaremos para localizar el resultado


# Creamos el objeto Browser para interactuar con la página
browser = mechanicalsoup.Browser()

# Hacemos una solicitud a la URL deseada
page = browser.get("http://olympus.realpython.org/dice")

# Buscamos el elemento con id="result" que contiene el valor de la tirada
# Usamos un selector CSS (#) para especificar que buscamos un ID
tag = page.soup.select("#result")[0]  # Selecciona el primer (y único) elemento con id="result"
result = tag.text  # Extraemos el texto del elemento, que es el valor de la tirada

print(f"The result of your dice roll is: {result}")


# --- Ejemplo de uso de time.sleep() ---
# Si queremos hacer múltiples solicitudes a la página en intervalos de tiempo,
# podemos usar el módulo time.sleep() para pausar la ejecución entre solicitudes

import time

print("\nEjemplo de espera:")
print("Vamos a esperar 5 segundos...")
time.sleep(5)  # Pausa de 5 segundos
print("Hecho!")


# --- Bucle para realizar múltiples tiradas ---
# Para obtener varios resultados de la tirada, creamos un bucle que cargue la página repetidamente
# Añadimos una pausa entre cada tirada para simular un intervalo de tiempo entre solicitudes
print("\nSimulación de varias tiradas con espera:")

for i in range(4):  # Realizamos 4 tiradas
    # Realizamos una nueva solicitud a la página
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"Tirada {i + 1} | El resultado es: {result}")
    
    # Pausa de 10 segundos entre tiradas
    time.sleep(10)


# --- Optimización para no esperar después de la última tirada ---
# En el bucle anterior, la última tirada también espera 10 segundos.
# Para optimizar, modificamos el bucle para evitar la espera en la última iteración.

print("\nSimulación optimizada de varias tiradas:")

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"Tirada {i + 1} | El resultado es: {result}")
    
    # Solo esperamos si no es la última iteración
    if i < 3:
        time.sleep(10)


# --- Optimización sobre la optimización ---
# Definir una variable con el número de lanzamientos

print("\nSimulación con código más mantenible:")
LANZAMIENTOS = 10

for i in range(LANZAMIENTOS):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"Tirada {i + 1} | El resultado es: {result}")
    
    # Solo esperamos si no es la última iteración
    if i < LANZAMIENTOS - 1:
        time.sleep(1)


# --- Optimización sobre la optimización de la optimización ---
# Obtener un tiempo de espera variable, en lugar de X segundos fijos
import random

print("\nSimulación con comportamiento menos detectable:")
LANZAMIENTOS = 3

for i in range(LANZAMIENTOS):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"Tirada {i + 1} | El resultado es: {result}")
    
    # Solo esperamos si no es la última iteración
    if i < LANZAMIENTOS - 1:
        wait_time = random.uniform(3, 5)
        print(f"Esperando {wait_time:.2f} segundos antes de la siguiente solicitud")
        time.sleep(wait_time)
        print("Pasando a la siguiente solicitud\n")


## Ejercicio 1: Simulación de inicio de sesión y navegación en perfiles
# Dada la URL de inicio de sesión: `url = "http://olympus.realpython.org/login"`
# 1.1: Realizar el inicio de sesión utilizando las credenciales: Usuario: `zeus`, Contraseña: `ThunderDude`
# 1.2: Verificar que el inicio de sesión fue exitoso comprobando la redirección a la página de perfiles
# 1.3: Navegar a los perfiles de usuario en las siguientes URLs:
#    - http://olympus.realpython.org/profiles/dionysus
#    - http://olympus.realpython.org/profiles/poseidon
#    - http://olympus.realpython.org/profiles/apollo
# 1.4: Extraer y mostrar la siguiente información de cada perfil:
#    - Título de la página
#    - Nombre del usuario
#    - Lugar de origen (Hometown)
#    - Animal favorito
# 1.5: Añadir una espera de 2 segundos entre cada solicitud para simular un comportamiento humano
#
# Extra: genera tiempos de espera aleatorios

    

## Ejercicio 2: Books to Scrape (de nuevo)
# Reutiliza el ejercicio anterior de BeautifulSoup y añade tiempos de espera
# entre navegaciones
#
# Enunciado anterior:
# Dada la URL: url = "http://books.toscrape.com/"
# 2.1: Extraer Título y Precio de Cada Libro en la Página Principal
# 2.2: Obtener Calificación y Disponibilidad de Cada Libro
# 2.3: Guardar Información en un DataFrame
# 2.4: Acceder a las Categorías y Contar los Libros
# 2.5: Extraer Datos de Todas las Páginas de una Categoría


## Ejercicio 3: Interacción con la página
# Navega a https://www.scrapethissite.com/pages/forms/
# 3.1 Utiliza el formulario para buscar:
#   - Colorado
#   - Ottawa
#   - Florida
# 3.2 De cada búsqueda saca el año que obtuvo más victorias, el año que obtuvo
#     más derrotas, y una media de cuántos goles marca a favor y cuántos en contra


## Ejercicio 4: Recogida de datos
# De nuevo, navega a https://www.scrapethissite.com/pages/forms/
# 4.1 Muestra 100 elementos por página
# 4.2 Recorre todas las páginas (con pausa simulada)
# 4.3 Muestra el máximo de victorias y qué equipo lo consiguió
#
# Extra: ¿se pueden mostrar más de 100 elementos por página? ¿cómo?