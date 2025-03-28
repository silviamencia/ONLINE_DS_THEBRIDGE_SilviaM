# -*- coding: utf-8 -*-

# Configuración de User-Agent y otros encabezados HTTP

"""
Para modificar el user-agent o añadir otros encabezados, debes configurar 
chromeOptions o firefoxOptions en Selenium. 

Modificar el user-agent permite simular diferentes dispositivos y navegadores, 
lo que ayuda a evitar la detección como bot.

Listas de user agents: 
- https://deviceatlas.com/blog/list-of-user-agent-strings
- https://developers.whatismybrowser.com/useragents/explore/
- https://gist.github.com/pzb/b4b6f57144aea7827ae4
"""
# Ejemplo en Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Configura otros encabezados mediante extensiones o configuraciones adicionales, pero no todos los encabezados HTTP pueden ser modificados directamente en Selenium
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://example.com")


# Ejemplo en Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Firefox(options=firefox_options)
driver.get("http://example.com")


# ----------------------------------------------------------------------------------
# Configurar carpeta de descargas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurar opciones de Chrome
chrome_options = Options()

# Cambiar carpeta de descargas
download_path = "/ruta/a/tu/carpeta/de/descargas"
prefs = {
    "download.default_directory": download_path,  # Carpeta de descarga
    "download.prompt_for_download": False,        # No preguntar dónde guardar
    "download.directory_upgrade": True,           # Sobreescribir la carpeta de descarga
    "safebrowsing.enabled": True                  # Desactiva las advertencias de descarga
}
chrome_options.add_experimental_option("prefs", prefs)

# Iniciar el navegador con la configuración
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://example.com")


# En Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Configurar opciones de Firefox
firefox_options = Options()

# Crear un perfil de Firefox para manejar las preferencias
profile = webdriver.FirefoxProfile()

# Cambiar carpeta de descargas
download_path = "/ruta/a/tu/carpeta/de/descargas"
profile.set_preference("browser.download.folderList", 2)  # 2 = Usar una ubicación personalizada
profile.set_preference("browser.download.dir", download_path) # Carpeta de descarga
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # MIME types
profile.set_preference("pdfjs.disabled", True)  # Desactivar el visor de PDF interno

# Iniciar el navegador con la configuración
driver = webdriver.Firefox(firefox_profile=profile, options=firefox_options)
driver.get("https://example.com")


# ----------------------------------------------------------------------------------
# Modificar la dimensión de la pantalla
from selenium import webdriver
driver = webdriver.Chrome()

# Configurar dimensiones personalizadas
driver.set_window_size(1920, 1080)  # Configuración para pantallas de escritorio
# o para dispositivos móviles
driver.set_window_size(375, 667)  # Ejemplo de iPhone X

# Puedes maximizar o minimizar la ventana
driver.maximize_window()
driver.minimize_window()


# ----------------------------------------------------------------------------------
# Modo de navegación headless (sin interfaz gráfica)
# Para Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # Especialmente útil para entornos Linux
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://example.com")

driver.title

# En Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(options=firefox_options)

"""
El modo headless es útil para ejecutar pruebas automatizadas en segundo plano.
Esto puede ser más rápido y eficiente que abrir una ventana del navegador visible.

Pero ten en cuenta que algunas páginas web pueden detectar y bloquear el modo headless.
O también, algunas funcionalidades pueden no estar disponibles en el modo headless.
"""


# ----------------------------------------------------------------------------------
# Deshabilitar extensiones y alertas de automatización
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")  # Oculta la barra de "Chrome está siendo controlado"
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)

"""
Estas configuraciones pueden ayudar a evitar la detección de bots y a mejorar la
experiencia de navegación en Selenium.
"""


# ----------------------------------------------------------------------------------
# Configurar un proxy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--proxy-server=http://IP-DE-TU-PROXY:PUERTO")

driver = webdriver.Chrome(options=chrome_options)

"""
Puedes configurar un proxy para navegar a través de una dirección IP específica.
Esto puede ser útil para simular diferentes ubicaciones geográficas o evitar
bloqueos de IP.
"""

# En Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "IP-DE-TU-PROXY:PUERTO"
proxy.ssl_proxy = "IP-DE-TU-PROXY:PUERTO"

firefox_options = Options()
firefox_profile = webdriver.FirefoxProfile()
proxy.add_to_capabilities(firefox_options.to_capabilities())

driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)


# ----------------------------------------------------------------------------------
# Deshabilitar caché y limpiar cookies	
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Deshabilitar caché
chrome_options = Options()
chrome_options.add_argument("--disk-cache-size=0")
chrome_options.add_argument("--disable-application-cache")

# Borrar cookies antes de empezar
driver = webdriver.Chrome(options=chrome_options)
driver.delete_all_cookies()  # Limpia todas las cookies


# ----------------------------------------------------------------------------------
# Activar modo móvil con Chrome DevTools y User-Agent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1")
chrome_options.add_argument("window-size=375,812")  # Tamaño de pantalla para iPhone X

driver = webdriver.Chrome(options=chrome_options)


# ----------------------------------------------------------------------------------
# Modo incógnito
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
