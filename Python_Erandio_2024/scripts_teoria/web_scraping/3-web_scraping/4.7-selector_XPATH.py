# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Aunque con los selectores CSS podemos localizar elementos de forma eficiente, XPath es otra
herramienta poderosa para seleccionar elementos en una página web.

XPath (XML Path Language) es un lenguaje de consulta utilizado para seleccionar nodos en un
documento XML o HTML. En Selenium, XPath se puede utilizar para localizar elementos basados
en su estructura, atributos, texto y otros criterios.

Nos permite trabajar con una jerarquía de elementos compleja y realizar selecciones más
específicas que con los selectores CSS.

Algunos ejemplos de selecciones XPath incluyen:
- Seleccionar elementos por etiqueta y texto específico
- Seleccionar elementos por atributo específico
- Seleccionar elementos dentro de una jerarquía específica
- Seleccionar elementos basados en múltiples condiciones

Estructura básica de una selección XPath:
//tagname[@attribute='value']

Ejemplos:
- //a[@href='/about'] selecciona un enlace <a> con atributo href igual a "/about"
- //input[@type='text'] selecciona un campo de entrada <input> con atributo type igual a "text"
- //div[@class='header']/span selecciona un <span> que es hijo de un <div> con clase "header"
- /body/div[1]/p[2] selecciona el segundo párrafo <p> dentro del primer <div> dentro del cuerpo <body>

Notas:
//: Busca en toda la estructura del DOM.
/: Selecciona un elemento hijo directo.
Condiciones: Puedes combinar condiciones con and o or.
Índices: [1], [2], etc., permiten seleccionar elementos específicos dentro de una lista de elementos.
"""

# Inicializa el WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")  # Cambia a la URL deseada

# Ejemplo 1: Seleccionar un elemento por etiqueta y texto específico usando XPath
# Esto selecciona un enlace <a> que contiene el texto "About Us"
about_link = driver.find_element(By.XPATH, "//a[text()='About Us']")
about_link.click()  # Haz clic en el enlace

# Ejemplo 2: Seleccionar un elemento por atributo específico
# Esto selecciona un elemento <button> que tiene un atributo id con valor "submit"
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()  # Haz clic en el botón

# Ejemplo 3: Seleccionar un elemento dentro de una jerarquía específica
# Esto selecciona un <span> que es hijo de un <div> con clase "header"
header_span = driver.find_element(By.XPATH, "//div[@class='header']/span")
print("Texto dentro del span:", header_span.text)

# Ejemplo 4: Seleccionar un elemento basado en múltiples condiciones
# Esto selecciona un <input> con clase "search" que también tiene un atributo "type" con valor "text"
search_input = driver.find_element(By.XPATH, "//input[@class='search' and @type='text']")
search_input.send_keys("Selenium XPath")  # Ingresa texto en el campo

# Ejemplo 5: Usar funciones de XPath
# Esto selecciona el primer <li> dentro de una lista <ul> con clase "menu"
first_menu_item = driver.find_element(By.XPATH, "//ul[@class='menu']/li[1]")
print("Primer elemento de menú:", first_menu_item.text)

# Espera a que un elemento específico esté presente en la página usando WebDriverWait y XPath
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome']"))
    )
    print("Encabezado encontrado:", element.text)
except Exception:
    print("El encabezado no se encontró en el tiempo esperado")

# Cerrar el navegador
driver.quit()
