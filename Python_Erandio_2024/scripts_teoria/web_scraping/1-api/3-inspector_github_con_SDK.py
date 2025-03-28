# -*- coding: utf-8 -*-
"""
Creamos una aplicación de consola interactiva para recoger datos de la API
de GitHub utilizando su SDK: PyGithub

Documentación: https://github.com/PyGithub/PyGithub
"""

# pip install PyGithub
from github import Github
import pandas as pd
import os

# Configurar el directorio de trabajo
# Nota: solo funciona si ejecutamos el script entero, si vamos línea a línea tendríamos que especificar la ruta
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Inicializar la API de GitHub (usando acceso público)
g = Github()

# Archivos CSV genéricos
generic_user_info_file = "github_users_info_sdk.csv"
generic_repos_info_file = "github_repos_info_sdk.csv"

def get_user_info(username):
    try:
        user = g.get_user(username)
        data = {
            "Username": user.login,
            "Nombre": user.name,
            "Bio": user.bio,
            "Repos públicos": user.public_repos,
            "Seguidores": user.followers,
            "Siguiendo": user.following
        }
        df = pd.DataFrame([data])

        # Guardar en el archivo genérico, reemplazando si ya existe el usuario
        if os.path.exists(generic_user_info_file):
            df_existing = pd.read_csv(generic_user_info_file)
            df_existing = df_existing[df_existing["Username"] != username]
            df = pd.concat([df_existing, df], ignore_index=True)

        df.to_csv(generic_user_info_file, index=False)
        print(f"Información de {username} guardada en {generic_user_info_file}")

    except Exception as e:
        print(f"Error al obtener la información del usuario: {e}")

def get_user_repos(username):
    try:
        user = g.get_user(username)
        repos = [{"Username": username, "Nombre repositorio": repo.name, "Descripción": repo.description, "Favoritos": repo.stargazers_count} for repo in user.get_repos()]
        
        #repos = []
        #for repo in user.get(repos):
        #    datos = {"Username": ............ }
        #    repos.append(datos)
        
        df = pd.DataFrame(repos)

        # Guardar en el archivo genérico, reemplazando si ya existen repositorios del usuario
        if os.path.exists(generic_repos_info_file):
            df_existing = pd.read_csv(generic_repos_info_file)
            df_existing = df_existing[df_existing["Username"] != username]
            df = pd.concat([df_existing, df], ignore_index=True)

        df.to_csv(generic_repos_info_file, index=False)
        print(f"Lista de repositorios de {username} guardada en {generic_repos_info_file}")

    except Exception as e:
        print(f"Error al obtener los repositorios del usuario: {e}")

def main_menu():
    while True:
        print("\n--- Menú Interactivo de Inspector de GitHub ---")
        print("1. Obtener información de un usuario")
        print("2. Obtener lista de repositorios públicos de un usuario")
        print("3. Salir")
        
        option = input("Elige una opción: ")

        if option == '1':
            username = input("Introduce el nombre de usuario de GitHub: ")
            get_user_info(username)
        elif option == '2':
            username = input("Introduce el nombre de usuario de GitHub: ")
            get_user_repos(username)
        elif option == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú principal
main_menu()
