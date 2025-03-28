# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------
# OPCIONES DE ESPERA
# ----------------------------------------------------------------------------------
# 1: time.sleep() (espera fija) - ❌ NO RECOMENDADO
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://example.com")

time.sleep(5)  # Espera fija de 5 segundos

element = driver.find_element_by_id("my-element")
print(element.text)

driver.quit()

"""
Hasta ahora, para las esperas hemos utilizado time.sleep() para pausar la ejecución

Esto es una mala práctica porque no es escalable y requiere de un tiempo de
espera fijo, lo que puede llevar a errores si la página tarda más o menos en
cargar de lo esperado.

Es habitual que una página web tarde más en cargar por diversos motivos:
- Conexión a internet lenta
- Servidor sobrecargado
- Carga de recursos externos (imágenes, scripts, etc)
"""


# ----------------------------------------------------------------------------------
# 2: driver.implicitly_wait() (espera implícita) - ❌ NO RECOMENDADO
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Espera implícita de hasta 10 segundos

driver.get("http://example.com")
element = driver.find_element_by_id("my-element")  # Espera hasta 10 segundos
print(element.text)

driver.quit()

"""
Podemos configurar una espera implícita con driver.implicitly_wait() para que
Selenium espere un tiempo máximo antes de lanzar una excepción al buscar un
elemento.

Es más flexible y eficiente que time.sleep(), pero sigue siendo una espera
fija que puede llevar a errores si la página tarda más en cargar.
"""


# ----------------------------------------------------------------------------------
# 3: WebDriverWait() (espera explícita) - ✅ RECOMENDADO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://example.com")

# Espera explícita de hasta 10 segundos para que el elemento sea clicable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "my-element"))
    )
    print(element.text)
except Exception:
    print("El elemento no se hizo clicable a tiempo")

driver.quit()

"""
La mejor opción para las esperas en Selenium es WebDriverWait() con las
condiciones esperadas de expected_conditions.

Estructura:
WebDriverWait(driver, tiempo).until(expected_condition((By.METODO, "selector")))

Podemos esperar a que un elemento sea visible, clicable, presente, etc. con
una espera máxima de tiempo.

Lista de expected_conditions más comunes:
- element_to_be_clickable
- visibility_of_element_located
- presence_of_element_located
- text_to_be_present_in_element
- title_contains
Lista completa: https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html

Si el elemento no se encuentra en el tiempo especificado, se lanzará una
excepción que podemos capturar y manejar.
"""

