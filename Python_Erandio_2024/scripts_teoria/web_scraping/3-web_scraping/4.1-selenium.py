# -*- coding: utf-8 -*-

"""
Selenium es una herramienta de automatización de navegadores utilizada para
realizar pruebas de software y también para web scraping.

Permite controlar un navegador real (Chrome, Firefox, etc) a través de código
y ejecutar comandos simulando el comportamiento de un usuario (clics, scrolls,
enviar formularios, etc).

A diferencia de librerías como BeautifulSoup o MechanicalSoup que solo parsean
el contenido, Selenium ejecuta JavaScript y permite interactuar con elementos
o acciones que dependen de eventos en el navegador.
Por ejemplo: menús desplegables, popups, formularios de varios pasos, etc
"""

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el WebDriver para Chrome

driver = webdriver.Chrome()  # Usa webdriver.Firefox() si usas Firefox
# https://www.selenium.dev/documentation/webdriver/browsers/

"""
Es posible que el navegador no se inicialice correctamente porque no encuentra
el driver necesario, podemos descargarlo e indicar la ruta para que lo utilice:
- Chrome https://sites.google.com/chromium.org/driver/
- Firefox https://github.com/mozilla/geckodriver/releases
- Edge https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Ejemplo:
driver = webdriver.Chrome(executable_path="ruta/del/driver/chromedriver.exe")

Pero también podemos utilizar el paquete webdriver_manager para gestionar los
drivers automáticamente:
- pip install webdriver_manager

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
"""

# Abrir una página web
url = "https://www.scrapethissite.com/pages/forms/?per_page=1000"
driver.get(url)
print("Página abierta:", driver.title)  # Muestra el título de la página

# Esperar unos segundos para cargar (en uso real, usa WebDriverWait)
time.sleep(2)

# Encontrar elementos y realizar acciones comunes
# Encontrar un elemento por etiqueta o por ID
header = driver.find_element(By.TAG_NAME, "h1")
print("Encabezado h1 de la página:", header.text)  # Obtiene y muestra el texto del primer elemento <h1>

# Encontrar un elemento por su enlace y hacer clic
link = driver.find_element(By.LINK_TEXT, "http://www.opensourcesports.com/hockey/")  # Encuentra el enlace por su texto visible
link.click()

# Esperar un momento para cargar la nueva página
time.sleep(2)

# Comprobar el número de pestañas abiertas
print("Número de pestañas abiertas:", len(driver.window_handles))

# Cambiar a la nueva pestaña
driver.switch_to.window(driver.window_handles[-1])  # Cambia a la última pestaña abierta
print("Nueva página:", driver.title)

driver.switch_to.window(driver.window_handles[0])  # Cambia a la última pestaña abierta
print("Página:", driver.title)

driver.switch_to.window(driver.window_handles[-1])  # Cambia a la última pestaña abierta
print("Página:", driver.title)


# Cerrar la pestaña actual y volver a la anterior
driver.close()  # Cierra la pestaña actual
print("Página:", driver.title) # Lanza un error, hay que volver a seleccionar la primera pestaña

driver.switch_to.window(driver.window_handles[0]) # Volver a seleccionar la primera
print("Página:", driver.title)

# Comprobar de nuevo el número de pestañas abiertas
print("Número de pestañas abiertas:", len(driver.window_handles))

try:
    element_non_existent = driver.find_element(By.LINK_TEXT, "Non-existent")  # Genera una excepción si no existe el enlace
except Exception as e:
    print("Error al encontrar el elemento:", e)

# Esperar un momento para cargar la nueva página
time.sleep(2)


# EJECUTAR CÓDIGO JAVASCRIPT
# Vamos a desplazarnos por la página, utilizaremos el método scrollTo
# Documentación método scrollTo: https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Baja al final de la página
time.sleep(2)
driver.save_screenshot("screenshot_bottom.png")  # Captura de pantalla al final de la página

# Desplazar lentamente hacia arriba
driver.execute_script("""window.scrollTo({
    top: 0,
    left: 0,
    behavior: 'smooth'
})""")  # Sube al inicio de la página
    
time.sleep(2)

driver.save_screenshot("screenshot_top.png") # Captura de pantalla de vuelta en la parte superior


# VOLVER ATRÁS EN EL HISTORIAL
driver.get("https://example.com")
time.sleep(1)
driver.back()


# FORMULARIOS
# Navegamos a una página con un formulario de login
driver.get("http://olympus.realpython.org/login")
print("Página abierta:", driver.title)  # Muestra el título de la página
time.sleep(2)

login_form = driver.find_element(By.NAME, "login")
username = driver.find_element(By.NAME, "user")
password = driver.find_element(By.NAME, "pwd")

# Llenar el formulario
username.send_keys("zeus")
password.send_keys("ThunderDude")

# Enviar el formulario (3 formas diferentes)
# 1. Enviar con la tecla Enter
# - password.send_keys(Keys.RETURN)
#
# 2. Enviar con el método submit() del formulario
# - login_form.submit()
#
# 3. Enviar haciendo clic en el botón de enviar
# - driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

password.send_keys(Keys.RETURN)

# Esperar a que cargue la página
time.sleep(2)

# Verificar si el login fue exitoso
print("Página después de enviar el formulario:", driver.title)


# Cerrar el navegador
driver.quit()
