# -*- coding: utf-8 -*-


class Coche:
    def __init__(self, marca, modelo, longitud, precio, ruedas = 4):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
        self.ruedas = ruedas
        print(f"Has creado un coche {self}")
        
    def __str__(self):
        return f"{self.marca} {self.modelo} de {self.longitud}cm y {self.precio}€"
        
    def __del__(self):
        print(f"Has borrado un {self}")
        
    def __len__(self):
        return self.longitud
    
    def __lt__(self, otro):
        return self.precio < otro.precio
    
    def __gt__(self, otro):
        if self.precio != otro.precio:
            return self.precio > otro.precio
        else:
            return self.longitud > otro.longitud
        
    def __le__(self, otro):
        return self.precio <= otro.precio
    
    def __ge__(self, otro):
        return self.precio <= otro.precio 
    
    def __eq__(self, otro):
        if self.precio == otro.precio:
            return True
        else:
            return self.marca == otro.marca
    
    def comparacion_mayor(self, otro):
        if self.precio > otro.precio:
            return True
        else:
            return False
    
    def saluda(self):
        print(f"Hola soy un {self}")
        
    def rebaja(self, descuento):
        self.precio = self.precio * (100-descuento) / 100

# Crear objetos de la clase coche
# Atribuirles características que se creen al inicializar, basadas en datos
# introducidos al crear los objetos



coche1 = Coche("Toyota", "Corolla", 290, 2000)
coche2 = Coche("Renault", "Twingo", 220, 2000)
coche3 = Coche("Mercedes", "Vito", 310, 6000, 6)

coche3.ruedas
print(coche3)
coche2.saluda()

# Atribuirles métodos que permitan imprimir en la pantalla:
# Un mensaje al borrar el objeto
#del(coche3)

# un valor de longitud
len(coche2)

# un valor al hacer print()
print(coche1)


print(coche1)
# Crear métodos que permitan comparar los coches por el precio:

coche1 == coche2 
coche1 < coche2

# Estas dos son lo mismo
Coche.comparacion_mayor(coche1, coche2)
coche1.comparacion_mayor(coche2)


print(min(coche1, coche2, coche3))


"""
Crear un método que reduzca el precio del coche en un porcentaje 
introducido como argumento
"""
coche1.precio
coche1.rebaja(25)

print(coche1)
