# -*- coding: utf-8 -*-

import os
os.chdir("/home/laptop/Proyectos Python/Introd_python/Introd_python/POO")

from personapp import Peon

empleado1 = Peon('Juan', 'Pérez', 'López')
# El secretario tiene el sueldo "por defecto"
empleado2 = Peon('Juanito', 'Pérez', 'García')

empleado2.nombre
print(empleado2)
empleado2.presentarse()


empleado2.ficha()

secretario.calcula_sueldo()
