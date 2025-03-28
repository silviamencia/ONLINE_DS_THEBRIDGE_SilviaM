from datetime import datetime
from datetime import timedelta

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.dni = self.comprueba_dni(dni)
    
    @staticmethod
    def comprueba_dni(dni):
        if len(dni) == 9:
            numero = int(dni[:-1])
            letra = dni[-1]
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            if letras[numero % 23] == letra:
                return dni
            else:
                raise ValueError("La letra no coincide con el valor esperado")
        else:
            raise ValueError("El número de caracteres del DNI es erróneo")      
    
    def presentarse(self):
        print(f"Soy {self}")
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"
    
    @abstractmethod
    def calcula_sueldo(self):
        pass

class Empleado(Persona):
    def __init__(self, nombre, apellido1, apellido2="", dni=None, ubicacion=""):
        super().__init__(nombre, apellido1, apellido2=apellido2, dni=dni)
        self.trabajando = False
        self.fichajes = []
        self.tiempo_trabajado = timedelta(0)
        self.__sueldo_hora = 20  # Cambiado a "semi-privado" usando un solo guion bajo
        self.dietas = 0
        self.ubicacion = ubicacion


    def imprime_sueldo(self):
        if input("Introduzca el password: ") == "1234":
            print(self.__sueldo_hora)
        else:
            print("Password erróneo")
    
    @abstractmethod
    def asigna_sueldo(self, nuevo_sueldo):
        if isinstance(nuevo_sueldo, (int, float)):
            if input("Introduzca el password: ") == "1234":
                self.__sueldo_hora = nuevo_sueldo
            else:
                print("Password erróneo")
                raise ValueError("Password erróneo")
        else:
            print("El valor introducido no es un número")

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
            tiempo_acumulado += tiempo_jornada
        self.tiempo_trabajado = tiempo_acumulado
        return tiempo_acumulado

    @abstractmethod
    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_tiempo_trabajado()
        print(f"El tiempo trabajado calculado: {tiempo_trabajado}")
        tiempo_trabajado = tiempo_trabajado.total_seconds()
        print(f"El tiempo trabajado en segundos: {tiempo_trabajado}")
        sueldo_a_pagar = self.__sueldo_hora * tiempo_trabajado / 3600
        sueldo_a_pagar += self.dietas
        return sueldo_a_pagar

    

class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None, ubicacion = ""):
        super().__init__(nombre, apellido1, apellido2 = apellido2, dni = dni, ubicacion= ubicacion)
        self.guardias = 0
        self.precio_guardia = 30
    
    """
    # Método alternativo de calcular el número de guardias
    def calcula_guardias(self):
        for fichaje in self.fichajes:
            if fichaje.hour >22:
                self.guardias += 1
    
    def calcula_tiempo_trabajado(self):
        super().calcula_tiempo_trabajado()
        self.calcula_guardias()
    """
    def asigna_sueldo(self, nuevo_sueldo):
        super().asigna_sueldo(nuevo_sueldo)
    
    
    def ficha(self):
        super().ficha()
        if datetime.now().hour >= 12:
            self.guardias += 1
    
    def calcula_sueldo(self):
        sueldo_sin_guardias = super().calcula_sueldo()
        sueldo = sueldo_sin_guardias + self.guardias * self.precio_guardia
        return sueldo
    
        
class Oficinista(Empleado):
    def __init__(self, nombre, apellido1, apellido2="", dni=None, ubicacion=""):
        super().__init__(nombre, apellido1, apellido2=apellido2, dni=dni, ubicacion=ubicacion)
        self.bonus = 0

    def annadir_bonus(self, bonus):
        self.bonus += bonus

    def calcula_sueldo(self):
        sueldo_sin_bonus = super().calcula_sueldo()
        sueldo = sueldo_sin_bonus + self.bonus
        return sueldo

    def asigna_sueldo(self, nuevo_sueldo):
        super().asigna_sueldo(nuevo_sueldo*1.1)

               

class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2 = "", dni = None, ubicacion = ""):
        super().__init__(nombre, apellido1, apellido2 = apellido2, dni = dni, ubicacion= ubicacion)
        self.beneficios = 0
        self.coche_empresa = False
    
    def annadir_beneficios(self, beneficios):
        self.beneficios += beneficios
    
    def calcula_sueldo(self):
        sueldo_sin_beneficios = super().calcula_sueldo()
        sueldo = sueldo_sin_beneficios + self.beneficios
        return sueldo
    
    def asigna_sueldo(self, nuevo_sueldo):
        super().asigna_sueldo(nuevo_sueldo*1.2)
    
    def __asignar_coche(self, coche):
        if type(coche).__name__== "Coche":
            self.coche_empresa = coche
        
    def asignar_coche_verificado(self, coche):
        clave = input("Introduzca el password: ")
        if clave == "1234":
            self.__asignar_coche(coche)