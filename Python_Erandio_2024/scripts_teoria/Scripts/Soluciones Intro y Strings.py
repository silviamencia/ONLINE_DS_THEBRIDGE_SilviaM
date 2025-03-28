# Operaciones basicas
22.8+35.3
25-10
3.14*5
50/4
125**0.5
import math
math.sqrt(125)


# Crear variables.
suma = 22.8+35.3
resta = 25-10
multiplicacion = 3.14*5
division = 50/4
raiz2 = 125**0.5


# Comprobar la clase
type(suma)
type(resta)
type(multiplicacion)
type(division)
type(raiz2)


# Creacion de cadenas
nombre = "Borja Balparda de Marco"
lug_nacimiento = "Bilbao"
lug_vivienda = "Vitoria"

type(nombre)
type(lug_nacimiento)
type(lug_vivienda)


# Concatenacion de cadenas
DatosPersonales = "Me llamo " + nombre + " nací en " + lug_nacimiento + " pero vivo en " + lug_vivienda
DatosPersonales

# Extraccion de elementos de una cadena
len(DatosPersonales)


inicio_lg_nacimiento = DatosPersonales.find("nací en ") + len("nací en ")
fin_lg_nacimiento = DatosPersonales.find(" pero vivo en")

DatosPersonales[inicio_lg_nacimiento:fin_lg_nacimiento]

DatosPersonales[9:16:6]
DatosPersonales[9],DatosPersonales[15]


# Poner todo en minusculas.
DatosPersonalesMin = DatosPersonales.lower()


# Comprobar si existen ciertos elementos

"Borja" in DatosPersonales

DatosPersonales.count("a")
# No hace falta usar un for pero, si quisiéramos, quedaría así
contador = 0
for letra in DatosPersonales:
    if letra == "a":
        contador += 1


# Separar una cadena
DatosSeparados = DatosPersonales.split(" ")


# Transformar una cadena.
Datostransoformados = DatosPersonales.replace("Borja", "BORJA")
Datostransoformados = Datostransoformados.replace("Balparda", "BALPARDA")
Datostransoformados = Datostransoformados.replace(lug_nacimiento, lug_nacimiento.upper())
Datostransoformados = Datostransoformados.replace("Vitoria", "VITORIA")

