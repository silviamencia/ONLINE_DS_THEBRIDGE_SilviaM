from datetime import datetime
from datetime import timedelta

class Persona:
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.dni = dni
        
    def presentarse(self):
        print(f"Soy {self.nombre} {self.apellido1} {self.apellido2}")
       
    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"
    
    
def comprueba_dni(self):
    numero=int(dni[:-1])
    letra = dni[-1]
    letras ="TRWAGMYFPDXBNJZSQVHLCKE"
    if letras[numero%23]==letra:
        return dni
    else:
        raise ValueError ("La letra no coincide con el valor esperado")


class Empleado(Persona):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None, ubicacion = ""):
        super().__init__(nombre, apellido1, apellido2 = apellido2, dni = dni)
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.sueldo_hora = 20
        self.dietas = 0
        self.ubicacion = ubicacion

    def ficha(self):
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.now())
        self.dietas += 1.15
        if self.trabajando:
            print(f"Bienvenido al trabajo, {self.nombre}")
            
        else:
            print("Adiós")
        self.calcula_tiempo_trabajado()
             
    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} --> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion
        
    def muestra_fichajes(self):
        entradas, salidas = self.separa_entrada_salida()
        print("Entradas                        Salidas")
        for entrada, salida in zip(entradas, salidas):
            print(f"{entrada}     {salida}")
        return entradas, salidas

    def separa_entrada_salida(self):
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        return entradas, salidas

    def calcula_tiempo_trabajado(self):
        entradas, salidas = self.separa_entrada_salida()
        tiempo_acumulado = timedelta(0)
        for entrada, salida in zip(entradas, salidas):
            tiempo_jornada = salida - entrada
            tiempo_acumulado = tiempo_acumulado + tiempo_jornada
        self.tiempo_trabajado = tiempo_acumulado
        return tiempo_acumulado

    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_tiempo_trabajado()
        print(f"El tiempo trabajado calculado: {tiempo_trabajado}")
        tiempo_trabajado = tiempo_trabajado.total_seconds()
        print(f"El tiempo trabajado en segundos: {tiempo_trabajado}")
        sueldo_a_pagar = self.sueldo_hora*tiempo_trabajado/3600
        sueldo_a_pagar += self.dietas
        return sueldo_a_pagar



class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None, ubicacion = ""):
        super().__init__(nombre, apellido1, apellido2 = apellido2, dni = dni, ubicacion= ubicacion)
        self.guardias = 0
    
    def ficha(self):
        super().ficha()
        if datetime.now.hour() >= 22:
            self.guardias = self.guardias +1
            
    def calcula_sueldo(self):
        precio_guardia = 50
        sueldo_a_pagar = super().calcula_sueldo()
        sueldo_guardias =sueldo_a_pagar + (self.guardias*precio_guardia)
        return sueldo_guardias
        
             
class Oficinista(Empleado):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None, ubicacion = ""):
        super().__init__(nombre, apellido1, apellido2 = apellido2, dni = dni, ubicacion= ubicacion)
        self.bonus = 0
        
    def calcula_sueldo(self):
        sueldo_sin_bonus= super().calcula_sueldo()
        sueldo = sueldo_sin_bonus +self.bonus
        return sueldo
    
    def agrega_bonus(self, bonus):
        self.bonus =+ bonus 

class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None, ubicacion = ""):
        super().__init__(nombre, apellido1, apellido2 = apellido2, dni = dni, ubicacion= ubicacion)
        self.beneficios = 0
        self.coche_empresa = False


if __name__ == "__main__":
 
    import time
    print("Se ha cargado la clase Persona")
    
    director = Empleado('Juan', 'Pérez', 'López')
    # El secretario tiene el sueldo "por defecto"
    secretario = Empleado('Juanito', 'Pérez', 'García')

    secretario.sueldo_hora = 22


    secretario.ficha()
    time.sleep(1)
    secretario.trabajando
    secretario.ficha()
    time.sleep(1)
    secretario.trabajando
    secretario.ficha()
    time.sleep(1)
    secretario.trabajando
    secretario.ficha()
    time.sleep(1)
    secretario.trabajando
    
    secretario.calcula_sueldo()
    
  
if isinstance(Empleado, Peon):
    Peon.guardias()
