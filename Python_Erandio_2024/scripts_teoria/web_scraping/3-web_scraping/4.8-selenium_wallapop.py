# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Configuración de opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--window-size=1080,1080")  # Establece el tamaño de la ventana

# Inicializar el driver de Chrome (si el driver está en el PATH, no es necesario especificar la ruta)
driver = webdriver.Chrome(options=chrome_options)

# Visitar la página principal
driver.get("https://es.wallapop.com/")

# Aceptar las cookies
try:
    # Esperar a que aparezca el banner de cookies y aceptarlo
    btn_accept_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    btn_accept_cookies.click()
except Exception as e:
    print("No se encontró el banner de cookies o ya ha sido aceptado.", e)

# Navegar a la sección "Coches" mediante el texto del enlace
try:
    enlace_coches = driver.find_element(By.LINK_TEXT, "Coches")
    enlace_coches.click()
except Exception as e:
    print("No se encontró el enlace a 'Coches'.", e)

# Hacer clic en el botón ver más productos
try:
    boton_ver_mas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "seo-landing_SeoLandingPage__more-items-button__im9Nd")))
    boton_ver_mas.click()
except Exception as e:
    print("No se encontró el botón 'Ver más productos'.", e)

# Esperar 2 segundos y hacer múltiples clics para pasar la guía
time.sleep(2)
for _ in range(5):
    try:
        # clic en el body
        driver.find_element(By.TAG_NAME, "body").click()
        time.sleep(1)
    except Exception as e:
        print("No se encontró el botón 'Siguiente'.", e)

# Realizar una búsqueda de "Renault"
try:
    input_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SearchBox input[name='search']")))
    input_search.clear()  # Limpiar cualquier texto previo
    input_search.send_keys("Renault")
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.SearchBox input[name='search']"))).send_keys(Keys.ENTER)
except Exception as e:
    print("No se pudo realizar la búsqueda en la barra de búsqueda.", e)

time.sleep(2)

# Extraer precios y descripciones de los anuncios
precios = driver.find_elements(By.CLASS_NAME, "ItemCardWide__price")
for precio in precios:
    print(precio.text)  # Mostrar precio en consola
    abuelo = precio.find_element(By.XPATH, '../../..')
    try:
        descripcion = abuelo.find_element(By.CLASS_NAME, "ItemCardWide__title")
        print(descripcion.text)  # Mostrar descripción en consola
    except Exception as e:
        print("No se encontró la descripción del anuncio.", e)

    # Guardar captura de pantalla del elemento (primer anuncio)
    with open("abuelo.png", "wb") as file:
        file.write(abuelo.screenshot_as_png)

# Extraer URLs de los anuncios
enlaces = driver.find_elements(By.CLASS_NAME, "ItemCardList__item")
urls = [enlace.get_attribute("href") for enlace in enlaces]

# Recolectar información de cada anuncio
MAX_ANUNCIOS = 5
anuncios = []
for i, url in enumerate(urls):
    if i >= MAX_ANUNCIOS:
        print("Se ha alcanzado el máximo de anuncios a obtener")
        break
    
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "px-4")))

    # Extraer información del recuadro de datos del anuncio
    try:
        info_extra = [span.text for span in driver.find_elements(By.CLASS_NAME, "px-4")[0].find_elements(By.TAG_NAME, "span")]
        recuadro_datos = driver.find_elements(By.CLASS_NAME, "px-4")[1]
        datos = recuadro_datos.find_elements(By.CLASS_NAME, "item-detail-car-extra-info_ItemDetailCarExtraInfo__section__n4g_P")

        anuncio = {}
        for dato in datos:
            try:
                clave, valor = dato.text.split("\n")
                anuncio[clave] = valor
            except ValueError:
                print(f"Formato inesperado en datos: {dato.text}")

        anuncio["info_extra"] = info_extra
        anuncios.append(anuncio)
        print(anuncio)
    except Exception as e:
        print("Error al extraer información de un anuncio.", e)

# Guardar datos en un archivo CSV
datos_df = pd.DataFrame(anuncios)
datos_df.to_csv("renault.csv", index=False)
print("Datos guardados en renault.csv")

# Cerrar el navegador
driver.quit()
