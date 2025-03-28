# -*- coding: utf-8 -*-

#############
# Ejercicio #
#___________#

# Crear la clase coche que incluya los atributos 
# "marca", "modelo", "longitud" y "precio"

class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
    def __str__(self):
        return f"Soy un coche {self.marca} y {self.modelo} y {self.longitud}."
    
    def __del__(self):
        print(f"El coche {self} se está borrando de la memoria")
    def __len__(self):
            return self.longitud
    def comparacion_precio(self, otro):
        if self.precio > otro.precio:
            return f"El coche {otro.marca} es más barato"
        else:
            return f"El coche {self.marca} es más barato" 
    def __lt__(self, otro):
        return self.precio < otro.precio
    def __gt__(self, otro):
        return self.precio > otro.precio
    def __le__(self, otro):
        return self.precio <= otro.precio
    def __ge__(self, otro):
        return self.precio >= otro.precio
    def __eq__(self, otro):
        return self.precio 
    
    
    def porcentaje(self,por):
        self.precio -=self.precio*por/100
        return self.precio
        
        
comparacion_precio(Coche1, Coche2)
lista_coches = [Coche1, Coche2]
min(Coche1, Coche2)
print(min(Coche1, Coche2))
Coche1.porcentaje(25)
print(Coche1.precio)       
# Crear objetos de la clase coche
# Atribuirles características que se creen al inicializar, basadas en datos
# introducidos al crear los objetos

Coche1 = Coche("Seat", "Panda", 100, 2000)
Coche2 = Coche("Volkswagen", "Polo", 200, 3000)
Coche3 = Coche("Opel", "Corsa", 300, 4000)

# Atribuirles métodos que permitan imprimir en la pantalla:
    
    print(Coche1)
    str(Coche1)
    
# Un mensaje al borrar el objeto

    
    def __del__(self):
        print(f"El coche {self} se está borrando de la memoria")
        
        del(Coche1)
        
# un valor de longitud
len(coche1)

def __len__(self):
        return self.longitud

# un valor al hacer print()
print(coche1)
# Crear métodos que permitan comparar los coches por el precio:
# if coche1 > coche2:
#   pass
coche1 > coche2
coche1 != coche2
print(min(lista_coches))




"""
Crear un método que reduzca el precio del coche en un porcentaje 
introducido como argumento
"""
coche1.rebaja(25)



dir(min)
