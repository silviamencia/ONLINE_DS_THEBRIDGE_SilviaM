# -*- coding: utf-8 -*-
"""
Al interactuar con un navegador web a través de Selenium, pueden ocurrir errores

Es importante manejar las excepciones que pueden surgir al interactuar con elementos,
como cuando un elemento no se encuentra, no es interactuable o un clic es interceptado

Es una buena práctica envolver el código de Selenium en bloques try/except para manejar
estas excepciones y evitar que el script se detenga inesperadamente

Algunas excepciones comunes en Selenium incluyen:
- NoSuchElementException: Elemento no encontrado
- TimeoutException: Expiró el tiempo de espera
- ElementNotInteractableException: Elemento no es interactuable
- ElementClickInterceptedException: Clic interceptado por otro elemento
- StaleElementReferenceException: Elemento ya no es válido en el DOM
- WebDriverException: Error inesperado en el WebDriver
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    WebDriverException,
)
import time

# Inicializa el WebDriver
driver = webdriver.Chrome()

try:
    # Navega a una página
    driver.get("http://example.com")
    
    # Espera explícita para que un elemento esté presente
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "element-id"))
        )
        print("Elemento encontrado:", element.text)
    except TimeoutException:
        print("Error: El elemento no apareció dentro del tiempo especificado")
    
    # Intentar hacer clic en un elemento
    try:
        button = driver.find_element(By.ID, "button-id")
        button.click()
    except NoSuchElementException:
        print("Error: No se encontró el elemento para hacer clic")
    except ElementNotInteractableException:
        print("Error: El elemento no es interactuable en este momento")
    except ElementClickInterceptedException:
        print("Error: El clic fue interceptado por otro elemento")

    # Interactuar con un campo de texto (por ejemplo, un input de búsqueda)
    try:
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Selenium")
        search_box.submit()
    except NoSuchElementException:
        print("Error: No se encontró el campo de búsqueda")
    except ElementNotInteractableException:
        print("Error: No se puede interactuar con el campo de búsqueda")

    # Espera a que un elemento esté visible antes de interactuar
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "visible-element-id"))
        )
        element.click()
    except TimeoutException:
        print("Error: El elemento no se hizo visible a tiempo")
    except StaleElementReferenceException:
        print("Error: El elemento ya no es válido en el DOM")

except WebDriverException as e:
    print(f"Error inesperado en el WebDriver: {e}")

finally:
    # Cierra el navegador al finalizar
    time.sleep(2)
    driver.quit()
