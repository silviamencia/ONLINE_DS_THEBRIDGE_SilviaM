# -*- coding: utf-8 -*-

"""
Obtener datos de la API de GitHub utilizando los endpoints

Una API (Programming Application Interface) es un conjunto de reglas y
herramientas que permiten que diferentes aplicaciones se comuniquen entre sí.
Es como un "puente" que permite que dos aplicaciones interactuen.

Documentación: https://docs.github.com/es/rest
"""
import requests

# Variable para el nombre de usuario de GitHub
username = "octocat"

# URL de la API de GitHub para obtener información del usuario
url = f"https://api.github.com/users/{username}"

# Hacer la solicitud
response = requests.get(url)
response.status_code

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    user = response.json()
    
    # Mostrar información básica
    print(f"Username: {user['login']}")
    print(f"Nombre: {user.get('name', 'N/A')}")
    print(f"Bio: {user.get('bio', 'N/A')}")
    print(f"Repos públicos: {user['public_repos']}")
    print(f"Seguidores: {user['followers']}")
    print(f"Siguiendo: {user['following']}")
else:
    print(f"Error: No se pudo obtener la información del usuario. Código de estado: {response.status_code}")


# -----------------------------------------------------------------------------

"""
Obtener datos de la API de GitHub utilizando su SDK (Software Development Kit)

Un SDK es un conjunto de herramientas y bibliotecas para trabajar con un
servicio, en teste caso PyGithub nos permitirá desarrollar e interactuar con la
API de GitHub

Documentación: https://github.com/PyGithub/PyGithub
"""
# pip install PyGithub
from github import Github

# Variable para el nombre de usuario de GitHub
username = "octocat"

# Inicializar la API de GitHub (usando acceso público)
g = Github()

try:
    # Obtener la información del usuario
    user = g.get_user(username)

    # Mostrar información básica
    print(f"Username: {user.login}")
    print(f"Nombre: {user.name if user.name else 'N/A'}")
    print(f"Bio: {user.bio if user.bio else 'N/A'}")
    print(f"Repos públicos: {user.public_repos}")
    print(f"Seguidores: {user.followers}")
    print(f"Siguiendo: {user.following}")

except Exception as e:
    print(f"Error: No se pudo obtener la información del usuario. Detalles: {e}")