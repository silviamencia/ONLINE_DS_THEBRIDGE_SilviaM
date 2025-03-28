# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Configurar el WebDriver para Chrome usando webdriver_manager (o Firefox)
driver = webdriver.Chrome()

# FORMULARIOS
# Navegar a una página con un formulario de login
driver.get("http://olympus.realpython.org/login")
print("Página abierta:", driver.title)  # Muestra el título de la página
time.sleep(2)

login_form = driver.find_element(By.NAME, "login")
username = driver.find_element(By.NAME, "user")
password = driver.find_element(By.NAME, "pwd")

# Función avanzada de entrada simulada
def human_typing(element, text, min_delay=0.05, max_delay=0.2, error_chance=0.05):
    for char in text:
        # Simular error tipográfico con una pequeña probabilidad
        if random.random() < error_chance:
            element.send_keys(random.choice("abcdefghijklmnopqrstuvwxyz"))  # Tecla incorrecta
            time.sleep(random.uniform(min_delay, max_delay))
            element.send_keys(Keys.BACKSPACE)  # Simular corrección
            time.sleep(random.uniform(min_delay, max_delay))
        
        # Enviar el carácter correcto
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))  # Pausa aleatoria entre caracteres

# Llenar el formulario con la entrada simulada
human_typing(username, "zeus", min_delay=0.05, max_delay=0.1, error_chance=0.5)
human_typing(password, "ThunderDude", min_delay=0.1, max_delay=0.3, error_chance=0.1)

# Enviar el formulario (3 formas diferentes)
# 1. Enviar con la tecla Enter
# - password.send_keys(Keys.RETURN)
#
# 2. Enviar con el método submit() del formulario
# - login_form.submit()
#
# 3. Enviar haciendo clic en el botón de enviar
# - driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

password.send_keys(Keys.RETURN)  # Usando la tecla Enter en este ejemplo

# Esperar a que cargue la página
time.sleep(2)

# Verificar si el login fue exitoso
print("Página después de enviar el formulario:", driver.title)

# Cerrar el navegador
driver.quit()
