# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

# Inicializa el WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")

# 1. Esperar a que el título de la página contenga una palabra específica
try:
    WebDriverWait(driver, 10).until(EC.title_contains("Example"))
    print("La página contiene 'Example' en el título")
except TimeoutException:
    print("Error: El título de la página no contiene 'Example'")

# 2. Esperar a que un elemento sea visible en la página y luego interactuar con él
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visible-element-id"))
    )
    print("Elemento visible encontrado:", element.text)
    element.click()
except TimeoutException:
    print("Error: El elemento no se hizo visible a tiempo")

# 3. Esperar a que un elemento sea clicable antes de hacer clic
try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-id"))
    )
    print("Botón encontrado y listo para hacer clic")
    button.click()
except TimeoutException:
    print("Error: El botón no estuvo listo para ser clicado a tiempo")

# 4. Esperar a que un elemento esté presente en el DOM (sin importar si es visible)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "some-class"))
    )
    print("Elemento presente en el DOM:", element.get_attribute("outerHTML"))
except TimeoutException:
    print("Error: El elemento no está presente en el DOM")

# 5. Esperar hasta que un elemento desaparezca de la página (por ejemplo, un cargador de carga)
try:
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "loader"))
    )
    print("El cargador desapareció, la página parece estar cargada")
except TimeoutException:
    print("Error: El cargador no desapareció en el tiempo esperado")

# 6. Esperar una condición personalizada (por ejemplo, esperar que el número de elementos aumente)
try:
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.CLASS_NAME, "dynamic-element")) > 5
    )
    print("Más de 5 elementos 'dynamic-element' están presentes en la página")
except TimeoutException:
    print("Error: No se encontraron más de 5 elementos 'dynamic-element' en el tiempo esperado")

# 7. Esperar que un elemento se vuelva "estable" (no cambie en el DOM por un tiempo)
def wait_for_stability(driver, locator, timeout=10, stability_time=0.5):
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            element = driver.find_element(*locator)
            location = element.location
            time.sleep(stability_time)
            if location == element.location:  # Verifica si el elemento se ha movido
                return element
        except StaleElementReferenceException:
            pass
    raise TimeoutException("El elemento no se estabilizó a tiempo")

try:
    stable_element = wait_for_stability(driver, (By.ID, "stable-element-id"))
    print("Elemento encontrado y estable en el DOM")
except TimeoutException:
    print("Error: El elemento no se estabilizó a tiempo")

# 8. Esperar a que el texto de un elemento específico cambie a un valor esperado
try:
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "status-message"), "Success")
    )
    print("El mensaje de estado cambió a 'Success'")
except TimeoutException:
    print("Error: El mensaje de estado no cambió a 'Success'")

# 9. Simulación de eventos y movimiento del mouse
from selenium.webdriver.common.action_chains import ActionChains
driver.get("https://tailwindcss.com/docs/installation")
footer = driver.find_element(By.TAG_NAME, "footer")
github_link = footer.find_element(By.CSS_SELECTOR, 'a[href="https://github.com/tailwindlabs/tailwindcss"]')

actions = ActionChains(driver)
actions.move_to_element(github_link).perform()  # Mover el mouse sobre el elemento

# Simulación de clic y desplazamiento
actions.click(github_link).perform()
actions.move_by_offset(10, 10).perform()  # Mueve el mouse en un offset

# También puedes simular la entrada de teclas
actions.send_keys(Keys.TAB).perform()


# Cerrar el navegador
driver.quit()


## EJERCICIO 1: Interacción con la página
# Navega a https://www.scrapethissite.com/pages/forms/?per_page=5
# Importante: añadir "?per_page=5" al final de la URL para limitar los resultados
# y forzar la paginación
#
# 1.1 Utiliza el formulario para buscar:
#   - Colorado
#   - Ottawa
#   - Florida
# Utiliza KEYS para enviar la búsqueda y para navegar entre las páginas
# Utiliza WebDriverWait para esperar a que los resultados se carguen
#
# 1.2 De cada búsqueda saca el año que obtuvo más victorias, el año que obtuvo
#     más derrotas, y una media de cuántos goles marca a favor y cuántos en contra
# Si hay más de una página, navega a la siguiente y repite el proceso
# Navega utilizando WebDriverWait para esperar a que los resultados se carguen y
# haciendo clic en los enlaces de las páginas
