# -*- coding: utf-8 -*-


####################################
# Programación Orientada a Objetos #
####################################
# Creamos una aplicación para gestionar el "Personal" de una empresa

#----------------------------------
# Etapa1: Creo una clase "Persona"
#----------------------------------
"""
Los atributos de una persona serán.
    Nombre
    Apellidos (1º y 2º)
    trabajando (booleano)
    Ubicación
    
La Persona podrá:
    Presentarse
    Fichar (modificando trabajando a True o False)
    Viajar (cambiando la ubicacion)

"""

class Persona:
    def __init__(self, Nombre, Apellido1, Apellido2="", ubicacion=""):
        self.Nombre= Nombre
        self.Apellido1=Apellido1
        self.Apellido2=Apellido2
        self.ubicacion= ubicacion
        self.trabajando=False
        
        
    def __str__(self):
        return f"Soy{self.Nombre} y {self.Apellido1} y {self.Apellido2}."
    
    def __del__(self):
        print(f"El usuario {self} se está borrando de la memoria")
    
    def presentarse(self):
        return f"Soy  {self.Nombre} {self.Apellido1} {self.Apellido2}"
        
    def ficha(self):
        self.trabajando = not self.trabajando
        if self.trabajando:
            print("Bienvenido")
        else: 
            print("Adiós")
            
    def viaja(self, nueva_ubicacion):
        print (f"self.ubicacion) --> (nueva_ubicacion)")
               self.ubicacion = nueva_ubicacion
        
    
        
        print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
        print(f"¿Dónde está el director? {director.ubicacion}")
        print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
        print(f"¿Dónde está el secretario? {secretario.ubicacion}")
        
    def ubicacion(self):
        
        if u
        print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
        print(f"¿Dónde está el director? {director.ubicacion}")
        print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
        print(f"¿Dónde está el secretario? {secretario.ubicacion}")
        
        
        
    

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

print(type(director))
print(type(secretario))

director.presentarse()
secretario.presentarse()


director.trabajando
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

director.viaja("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")


#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------


class Persona:
    def __init__(self, nombre, apellidos, trabajando=False, ubicacion=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.trabajando = trabajando
        self.ubicacion = ubicacion

    def presentarse(self):
        return f"Hola, soy {self.nombre} {self.apellidos}."

    def fichar(self):
        self.trabajando = not self.trabajando
        estado = "trabajando" if self.trabajando else "no trabajando"
        return f"Ahora estoy {estado}."

    def viajar(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        return f"Ahora estoy en {self.ubicacion}."

from datetime import datetime
from datetime import timedelta


#timedelta es el intervalo de tiempo entre dos tiempos

class Persona:
    def __init__(self, nombre, apellido1, apellido2 = "", ubicacion = ""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.ubicacion = ubicacion
        self.trabajando = False
        self.fichajes = []
        self.sueldohora = 20
        self.dietatransporte = 0
    def presentarse(self):
        print(f"Soy {self.nombre} {self.apellido1} {self.apellido2}")
        
    def ficha(self):
        self.trabajando = not self.trabajando
        if self.trabajando:
            
            print(f"Bienvenido al trabajo, {self.nombre}")
            dietatransporte +=1
            self.fichajes.append(datetime.now())
        else:
            print("Adiós")
    
    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} --> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion
        
    def muestra_fichajes(self):
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        print(f"Entradas: {entradas}" )   
        print(f"Salidas: {salidas}" )   
        
    def tiempo_trabajado(self):
        tiempo_acumulado = timedelta(0)
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        for entrada, salida in zip(entradas, salidas):
            tiempo_jornada= salida-entrada
            tiempo_acumulado+=tiempo_jornada
        return tiempo_acumulado
    
    def sueldo_hora(self):
        
        tiempo_acumulado= self.tiempo_trabajado()
        sueldo_a_pagar = self.sueldohora*(tiempo_acumulado.total_seconds())/3600
        sueldo_a_pagar+=dietatransporte
        return sueldo_a_pagar
    
   
           
        
        
               
director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')




secretario.ficha()
secretario.ficha()
secretario.ficha()
secretario.ficha()

secretario.muestra_fichajes()
secretario.tiempo_trabajado()
secretario.sueldo_hora()

#Calcular el tiempo trabajado






