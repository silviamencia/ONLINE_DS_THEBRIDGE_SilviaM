# -*- coding: utf-8 -*-

import requests

# Token de acceso personal
token = "TU_TOKEN_DE_ACCESO"

# URL de la API de GitHub para obtener información del usuario autenticado
url = "https://api.github.com/user"

# Headers con el token para autenticación
headers = {
    "Authorization": f"token {token}"
}

# Hacer la solicitud con autenticación
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    user = response.json()

    # Mostrar información básica
    print(f"Username: {user['login']}")
    print(f"Nombre: {user.get('name', 'N/A')}")
    print(f"Bio: {user.get('bio', 'N/A')}")
    print(f"Repos públicos: {user['public_repos']}")
    print(f"Repos privados: {user.get('total_private_repos', 'No tienes permiso')}")
    print(f"Seguidores: {user['followers']}")
    print(f"Siguiendo: {user['following']}")
else:
    print(f"Error: No se pudo obtener la información del usuario. Código de estado: {response.status_code}")
    
# Códigos de estado de petición:
# 200 Success (éxito)
# 401 Unauthorized (sin autenticar)
# 403 Forbidden (sin permisos)
# 404 Not found (no existe)
# 429 Too many requests (demasiadas peticiones)

# -----------------------------------------------------------------------------

from github import Github

# Token de acceso personal
token = "TU_TOKEN_DE_ACCESO"

# Inicializar la API de GitHub con el token para autenticación
g = Github(token)

try:
    # Obtener la información del usuario autenticado
    user = g.get_user()
    # repos = user.get_repos()

    # Mostrar información básica
    print(f"Username: {user.login}")
    print(f"Nombre: {user.name if user.name else 'N/A'}")
    print(f"Bio: {user.bio if user.bio else 'N/A'}")
    print(f"Repos públicos: {user.public_repos}")
    print(f"Repos privados: {user.total_private_repos}")
    print(f"Seguidores: {user.followers}")
    print(f"Siguiendo: {user.following}")

except Exception as e:
    print(f"Error: No se pudo obtener la información del usuario. Detalles: {e}")
    
# Códigos de estado de petición:
# 200 Success (éxito)
# 401 Unauthorized (sin autenticar)
# 403 Forbidden (sin permisos)
# 404 Not found (no existe)
# 429 Too many requests (demasiadas peticiones)