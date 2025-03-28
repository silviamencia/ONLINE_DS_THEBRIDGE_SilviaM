# -*- coding: utf-8 -*-

"""
MechanicalSoup se basa en BeautifulSoup pero añade funcionalidad de navegación
web y manejo de formularios. 

Esto permite simular la interacción con páginas web, como rellenar y enviar 
formularios.
"""


# Instalación: pip install MechanicalSoup
import mechanicalsoup

# Creamos un objeto Browser
browser = mechanicalsoup.Browser()

# Solicitamos una página de internet
url = "http://olympus.realpython.org/login"
page = browser.get(url)

# Obtenemos un objeto que almacena la respuesta de la URL solicitada
print("Código de estado de la respuesta:", page.status_code)  # 200 significa éxito
# Otros códigos comunes:
# 404: La URL no existe
# 500: Error en el servidor

# Verificamos que MechanicalSoup utiliza BeautifulSoup para analizar el HTML obtenido
print("Tipo de objeto soup:", type(page.soup))  # Verifica que sea BeautifulSoup

# Podemos ver el HTML completo de la página mediante el atributo .soup
print("HTML de la página obtenida:")
print(page.soup)
print(page.soup.prettify())  # .prettify() facilita la lectura de HTML


# Enviar un formulario con MechanicalSoup
"""
La página tiene un formulario con campos para nombre de usuario y contraseña.
Credenciales para este ejemplo:
    Usuario: zeus
    Contraseña: ThunderDude
Al acceder con estas credenciales, nos redirige a la página /profiles
"""

# Seleccionamos el formulario y completamos los campos
# Seleccionamos la etiqueta <form>
form = page.soup.select("form")[0]

# Establecemos los valores para 'username' y 'password'
input_username = form.select("input")[0]
input_password = form.select("input")[1]

input_username["value"] = "zeus"
input_password["value"] = "ThunderDude"

# Enviamos el formulario
profiles_page = browser.submit(form, page.url)
profiles_page.url

# Comprobamos el estado de la petición y la URL resultante después de enviar el formulario
print("\nCódigo de estado después de enviar el formulario:", profiles_page.status_code)
print("URL después de enviar el formulario:", profiles_page.url)
print("Título de la página:", profiles_page.soup.title.text)

# Si el formulario fue enviado correctamente, deberíamos estar en la página de perfiles
print("\nHTML de la página de perfiles:")
print(profiles_page.soup.prettify())

"""
Nota de seguridad:
Esta técnica de automatización puede ser usada para ataques de fuerza bruta 
en intentos de autenticación. Muchas páginas web implementan medidas de 
seguridad para prevenir esto, como limitar los intentos de inicio de sesión.

Más info: https://www.fortinet.com/lat/resources/cyberglossary/brute-force-attack
"""


# Obtención de enlaces de perfiles en la página
# La estructura HTML muestra que los perfiles están dentro de elementos <a>
print("\nEnlaces a perfiles disponibles en la página de perfiles:")
links = profiles_page.soup.select("a")

# Iteramos sobre cada enlace y mostramos el texto y el atributo 'href'
for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")

# Las URLs en 'href' son relativas, así que las convertimos a URLs completas
base_url = "http://olympus.realpython.org"
print("\nEnlaces completos de perfiles:")
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")



"""
Parámetros de URL

Es habitual que al paginar, filtrar o aplicar ciertos parámetros de búsqueda,
estos parámetros sean enviados en la cabecera de la petición.

El servidor procesará estos parámetros y devolverá el contenido en base a ellos.
Los parámetros de cabecera no deberían contener información sensible o 
confidencial, se suelen utilizar para configuraciones de búsqueda.

Ejemplos (paginación):
    - https://openlibrary.org/search?subject=Science+fiction&page=1
    - https://openlibrary.org/search?subject=Science+fiction&page=2
    
Todo lo que haya a partir de la interrogación, serán parámetros de url
Se separan con &, de esta manera podemos mandar varios
url?parametro_uno=valor&parametro_dos=valor    

Valores típicos en paginación:
    - Página, indicado generalmente como p o page: page=num_pagina
    - Cantidad por página: per_page=cantidad
"""

