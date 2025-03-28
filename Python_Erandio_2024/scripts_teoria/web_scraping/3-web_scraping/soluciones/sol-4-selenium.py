# -*- coding: utf-8 -*-

# EJERCICIO 1 #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Configuración inicial del WebDriver
driver = webdriver.Chrome()
url = "https://www.scrapethissite.com/pages/forms/?per_page=5"
driver.get(url)

# Equipos a buscar
teams = ["Colorado", "Ottawa", "Florida"]

for team in teams:
    # Diccionario para almacenar resultados
    results = {
        "wins": {
            "years": [],
            "qt": 0,
        },
        "losses": {
            "years": [],
            "qt": 0,
        },
    }
    
    # Esperar que el campo de búsqueda esté presente y buscar el equipo
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.clear()
    search_input.send_keys(team)
    search_input.send_keys(Keys.RETURN)  # Enviar la búsqueda con ENTER

    print(f"\nBuscando resultados para: {team}")

    max_wins = 0
    max_losses = 0
    goals_for = 0
    goals_against = 0
    page = 1

    while True:
        # Esperar que los resultados de la tabla se carguen
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.team"))
            )
        except Exception as e:
            print("Error: Los resultados no se cargaron a tiempo.", e)
            break

        print(f"Página {page}: {driver.current_url}")

        # Extraer filas de la tabla con los datos de los equipos
        rows = driver.find_elements(By.CSS_SELECTOR, "tr.team")
        for row in rows:
            year = row.find_element(By.CLASS_NAME, "year").text.strip()
            wins = int(row.find_element(By.CLASS_NAME, "wins").text.strip())
            losses = int(row.find_element(By.CLASS_NAME, "losses").text.strip())
            goals_for += int(row.find_element(By.CLASS_NAME, "gf").text.strip())
            goals_against += int(row.find_element(By.CLASS_NAME, "ga").text.strip())
            
            # Calcular año con más victorias y derrotas
            if wins > max_wins:
                max_wins = wins
                results["wins"]["years"] = [year]
                results["wins"]["qt"] = wins
            elif wins == max_wins:
                results["wins"]["years"].append(year)

            if losses > max_losses:
                max_losses = losses
                results["losses"]["years"] = [year]
                results["losses"]["qt"] = losses
            elif losses == max_losses:
                results["losses"]["years"].append(year)

        # Intentar encontrar y hacer clic en el botón de la siguiente página
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, str(page + 1)))
            )
            next_button.click()
            page += 1
            time.sleep(random.uniform(1, 2))  # Pausa para simular comportamiento humano
        except Exception:
            print("No hay más páginas de resultados o hubo un error en la navegación.")
            break

    # Calcular promedio de goles a favor y en contra
    if len(rows) > 0:
        avg_goals_for = goals_for / len(rows)
        avg_goals_against = goals_against / len(rows)
    else:
        avg_goals_for = 0
        avg_goals_against = 0

    # Mostrar resultados
    print(f"\nEquipo: {team}")
    if len(results["wins"]["years"]) == 0:
        print("Sin registros")
    else:
        print(f"Año(s) con más victorias: {', '.join(results['wins']['years'])} ({results['wins']['qt']} victorias)")
        print(f"Año(s) con más derrotas: {', '.join(results['losses']['years'])} ({results['losses']['qt']} derrotas)")
        print(f"Promedio de goles a favor: {avg_goals_for:.2f}")
        print(f"Promedio de goles en contra: {avg_goals_against:.2f}")

    # Pausa entre búsquedas para simular comportamiento humano
    if team != teams[-1]:
        time.sleep(random.uniform(1, 2))

# Cerrar el navegador
driver.quit()
