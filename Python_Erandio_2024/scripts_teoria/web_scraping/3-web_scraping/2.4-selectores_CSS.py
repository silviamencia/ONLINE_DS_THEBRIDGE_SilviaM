# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

# Parseamos el HTML
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejemplo de Selectores CSS</title>
</head>
<body>

    <!-- Ejemplo de selectores básicos -->
    <p>Primer párrafo sin clase ni id</p>
    <p class="intro">Párrafo con clase 'intro'</p>
    <div id="main">
        <p>Segundo párrafo dentro de div con id 'main'</p>
    </div>
    
    <!-- Selectores combinados de etiqueta y clase -->
    <p class="intro">Otro párrafo con clase 'intro'</p>
    
    <!-- Selectores por atributo -->
    <a href="https://example.com">Enlace con href a example.com</a>
    <a href="https://another.com" class="link">Enlace con href a another.com</a>
    <a class="link">Enlace sin href</a>
    
    <!-- Selectores de descendientes y hijos -->
    <div>
        <p>Primer párrafo dentro de un <div> (descendiente)</p>
        <p class="class1 class2">Párrafo con múltiples clases 'class1' y 'class2'</p>
        <span>Texto dentro de un <span> (hijo directo)</span></span>
    </div>
    
    <!-- Selectores múltiples de etiquetas -->
    <h1>Encabezado 1</h1>
    <h2>Encabezado 2</h2>
    <h3>Encabezado 3</h3>
    
    <!-- Selectores de tipo -->
    <div class="intro">
        <p>Primer párrafo dentro de otro <div> (primer elemento de tipo 'p')</p>
        <p>Segundo párrafo dentro de otro <div> (segundo elemento de tipo 'p')</p>
        <p>Último párrafo dentro de otro <div> (último elemento de tipo 'p')</p>
    </div>

</body>
</html>
"""

soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify())

# Ejemplos de selecciones usando los selectores CSS más habituales
soup.select("p")                    # Todos los <p>
soup.select("#main")                # Elemento con id="main"
soup.select(".intro")               # Todos los elementos con class="intro"
soup.select("p.intro")              # Todos los <p> con class="intro"
soup.select("a[href]")              # Todos los <a> con atributo href
soup.select("a[href='https://example.com']")  # <a> con href específico
soup.select("div p")                # Todos los <p> dentro de un <div>
soup.select("div > p")              # Todos los <p> que son hijos directos de <div>
soup.select(".class1.class2")       # Elementos con ambas clases 'class1' y 'class2'
soup.select("h1, h2, h3")           # Todos los <h1>, <h2> y <h3>

# Algunos selectores CSS menos habituales pero también muy útiles
soup.select("p:first-of-type")      # Primer <p> de su contenedor
soup.select("p:last-of-type")       # Último <p> de su contenedor
soup.select("p:nth-of-type(2)")     # Segundo <p> de su contenedor
