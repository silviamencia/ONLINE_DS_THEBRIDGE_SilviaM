# -*- coding: utf-8 -*-

# Reiniciar lista de variables
%reset -f

# --------- ¿Qué es una cadena de texto (string)? ---------
# Las cadenas en Python pueden ser definidas con comillas simples o dobles
cadena_simple = 'Hola'
cadena_doble = "Mundo"
cadena_multilinea = """Este es un texto
que ocupa varias líneas.
"""

print("Cadena simple:", cadena_simple)
print("Cadena doble:", cadena_doble)
print("Cadena multilinea:", cadena_multilinea)


# --------- Concatenación de cadenas ---------
%reset -f
# El operador + permite concatenar (unir) cadenas
nombre = "Lucía"
apellido = "Martínez"
nombre_completo = nombre + " " + apellido

print("Nombre completo:", nombre_completo)

# También puedes usar f-strings para concatenar más fácilmente
edad = 30
presentacion = f"Me llamo {nombre_completo} y tengo {edad} años."

print(presentacion)


# --------- Repetición de cadenas ---------
# Usando el operador * podemos repetir cadenas
advertencia = "¡Cuidado! " * 3

print(advertencia)


# --------- Acceder a caracteres de una cadena ---------
%reset -f
# Cada carácter de una cadena tiene un índice
fruta = "Manzana"
primera_letra = fruta[0]  # Primera letra
ultima_letra = fruta[-1]  # Última letra
letra_intermedia = fruta[3]  # Letra en el índice 3

print("Primera letra:", primera_letra)
print("Última letra:", ultima_letra)
print("Letra en el índice 3:", letra_intermedia)


# --------- Subcadenas (slicing) ---------
%reset -f
# Puedes extraer una subcadena usando slicing [inicio:fin]
frase = "Aprender Python es divertido"
parte_frase = frase[0:9]  # Extraer "Aprender"

print("Parte de la frase:", parte_frase)

# Si omites el índice inicial o final, se asume desde el principio o hasta el final
solo_python = frase[10:]  # Desde el índice 10 hasta el final

print("Solo 'Python':", solo_python)

# Slicing con un paso (saltando caracteres)
caracteres_alternos = frase[0:9:2]  # Saltar cada 2 caracteres

print("Caracteres alternos:", caracteres_alternos)


# --------- Longitud de una cadena ---------
%reset -f
# La función len() devuelve la longitud de una cadena
mensaje = "¡Bienvenido a Python!"
longitud = len(mensaje)

print("Longitud del mensaje:", longitud)


# --------- Métodos útiles de cadenas ---------
%reset -f
# Convertir a minúsculas
texto = "Hola MUNDO"
print("Minúsculas:", texto.lower())

# Convertir a mayúsculas
print("Mayúsculas:", texto.upper())

# Eliminar espacios al inicio y al final
espacio = "    ¡Hola!    "
print("Sin espacios:", espacio.strip())

# Reemplazar una parte del texto por otra
nuevo_texto = texto.replace("MUNDO", "Python")
print("Texto reemplazado:", nuevo_texto)

# Encontrar la primera aparición de una subcadena
indice_python = frase.find("Python")
print("Posición de 'Python':", indice_python)

# Verificar si una cadena empieza o termina con una subcadena
print("¿Empieza con 'Aprender'?", frase.startswith("Aprender"))
print("¿Termina con 'divertido'?", frase.endswith("divertido"))


# --------- Método count() ---------
%reset -f
# El método count() cuenta cuántas veces aparece una subcadena
parrafo = "Python es genial. Me encanta Python porque Python es fácil de aprender."
veces_python = parrafo.count("Python")

print("Número de veces que aparece 'Python':", veces_python)


# --------- Formateo de cadenas ---------
%reset -f
# Usar f-strings para formatear cadenas con variables
nombre = "Carlos"
edad = 25
pi = 3.14159

print(f"Me llamo {nombre} y tengo {edad} años.")
print(f"El valor de pi es aproximadamente {pi:.2f}")

# Usar el método format() para formatear cadenas
formato = "Me llamo {} y tengo {} años."
print(formato.format(nombre, edad))


# --------- Control de decimales ---------
%reset -f
pi = 3.14159

# Mostrar 2 decimales
print(f"Valor de pi con 2 decimales: {pi:.2f}")

# Mostrar 4 decimales
print(f"Valor de pi con 4 decimales: {pi:.4f}")

# Mostrar sin decimales
print(f"Valor de pi sin decimales: {pi:.0f}")


# --------- Alineación de cadenas ---------
%reset -f
# Alinear un número a la derecha
numero = 123.456
print(f"{numero:>10.2f}")  # Alinear a la derecha con 2 decimales

# Alinear un número a la izquierda
print(f"{numero:<10.2f}")  # Alinear a la izquierda

# Alinear un número centrado
print(f"{numero:^10.2f}")  # Alinear centrado

