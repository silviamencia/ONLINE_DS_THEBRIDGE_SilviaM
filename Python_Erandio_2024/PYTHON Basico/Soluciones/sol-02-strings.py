# --------- Ejercicio 1: Transformación de cadenas ---------
cadena = "PYTHON es un lenguaje GENIAL"

# Convertir a minúsculas
minusculas = cadena.lower()
print("Minúsculas:", minusculas)

# Convertir a mayúsculas
mayusculas = cadena.upper()
print("Mayúsculas:", mayusculas)

# Capitalizar cada palabra
capitalizado = cadena.title()
print("Capitalizado:", capitalizado)

# Invertir el orden de los caracteres
invertida = cadena[::-1]
print("Cadena invertida:", invertida)

%reset -f

# --------- Ejercicio 2: Extracción de iniciales ---------
nombre_completo = "Juan Pérez"
iniciales = nombre_completo[0] + nombre_completo[5]
print("Iniciales:", iniciales)

%reset -f

# --------- Ejercicio 3: Crear un mensaje dinámico ---------
producto = "Manzanas"
precio = 2.5
cantidad = 10

mensaje = f"Compraste {cantidad} unidades de {producto} a un precio de {precio} cada uno."
costo_total = precio * cantidad
mensaje_total = f"El costo total es: {costo_total}."
print(mensaje)
print(mensaje_total)

%reset -f

# --------- Ejercicio 4: Comparar dos frases ---------
frase_1 = "Me encanta Python"
frase_2 = "ME ENCANTA PYTHON"

# Comparar exactamente
iguales_exactos = frase_1 == frase_2
print("Son exactamente iguales:", iguales_exactos)

# Convertir a minúsculas y comparar
iguales_min = frase_1.lower() == frase_2.lower()
print("Son iguales ignorando mayúsculas/minúsculas:", iguales_min)

%reset -f

# --------- Ejercicio 5: Recuento de vocales ---------
frase = "Python es un lenguaje maravilloso"
conteo_a = frase.count("a")
conteo_e = frase.count("e")
conteo_i = frase.count("i")
conteo_o = frase.count("o")
conteo_u = frase.count("u")

print("Conteo de vocales:")
print(f"a: {conteo_a}, e: {conteo_e}, i: {conteo_i}, o: {conteo_o}, u: {conteo_u}")

%reset -f

# --------- Ejercicio 6: Crear un acrónimo ---------
frase = "Asociación Internacional de Programadores"
palabras = frase.split()  # Divide la frase en palabras
acronimo = "".join([palabra[0].upper() for palabra in palabras])
print("Acrónimo:", acronimo)

%reset -f

# --------- Ejercicio 7: Cambiar palabras en una frase ---------
frase = "Python es un lenguaje poderoso"
nueva_frase = frase.replace("poderoso", "versátil")
print("Nueva frase:", nueva_frase)

%reset -f

# --------- Ejercicio 8: Verificar si una palabra está contenida ---------
frase = "Estoy aprendiendo Python"
palabra = "Python"
esta_contenida = palabra in frase
print(f"¿La palabra '{palabra}' está en la frase?:", esta_contenida)

%reset -f

# --------- Ejercicio 9: Recortar y reorganizar una frase ---------
frase = "Estamos aprendiendo Python"
# Recortar las primeras tres palabras
recorte = frase.split()
print("Recorte:", recorte)

# Reorganizar las tres palabras
reorganizado = f"{recorte[2]} {recorte[1]} {recorte[0]}"
print("Reorganizado:", reorganizado)

%reset -f

# --------- Ejercicio 10: Formato de números y alineación ---------
numero = 123.456789

# Mostrar con 3 decimales
print(f"{numero:.3f}")

# Alinear el número
print(f"{numero:<12.3f}")  # Izquierda
print(f"{numero:>12.3f}")  # Derecha
print(f"{numero:^12.3f}")  # Centro
