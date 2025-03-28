# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:09:18 2024

@author: LANER
"""

#############
# Ejercicio #
#___________#
# Si transferimos a nuestra aplicacion de personal, puedo crear la clase empleado
# y a partir de ella crear clases herederas según cargo.


# Las clases "hijo" serán Directivo, Oficinista, Peon

# El directivo, tiene coche de empresa, y métodos asociados a él.
# El oficinista tiene bonuses
# El peón tiene guardias... etc

import os
os.getcwd()

import sys
sys.path

from archivos.apps.personaapp import Persona
from archivos.apps.personaapp import Directivo

from archivos.apps.Coche import Coche
coche1 = Coche("Toyota", "Corolla", 290, 2000)

director = Directivo('Juan', 'Pérez', 'López', "12345678Z")
director.verifica_asignar_coche(coche1)
director.annadir_beneficios(56)
director.calcula_sueldo()


secretario.ficha()
secretario.trabajando
secretario.ficha()
secretario.trabajando
secretario.ficha()
secretario.trabajando
secretario.ficha()
secretario.trabajando

secretario.fichajes
secretario.muestra_fichajes()
secretario.separa_entrada_salida()

secretario.calcula_tiempo_trabajado()
secretario.tiempo_trabajado







