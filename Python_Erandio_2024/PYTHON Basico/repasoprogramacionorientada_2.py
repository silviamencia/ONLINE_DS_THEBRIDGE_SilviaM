# -*- coding: utf-8 -*-

#Ejercicio de repaso de Programación Orientada a Objetos
#Crear un sistema de clases que permita gestionar los documentos de una biblioteca. 
#Se debe poder gestionar la adquisición, el alquiler y la baja de los documentos. 
#Se usarán documentos de distintos tipos como, Libros, Revistas, DVDs…
# Se deben utilizar los conceptos de Herencia, Polimorfismo, Encapsulamiento y Abstracción.


#genera códigos únicos aleatorios
import uuid

class Documento:
    def __init__(self, titulo, identificador="", unidades=""):
        self.titulo = titulo      
        #self.tipo_documento = [Libro,Revista,DVD]
        self.identificador = identificador
        self.unidades = unidades
        self.disponible = False
        self.unidades_alquiladas = 0
        
    def __str__(self):
        return f"self.titulo"
    
    def compra(self, unidades):
        #self.unidades = self.unidades + unidades
        print(f"Ahora tenemos {self.unidades} de {self.titulo}")
        lista_uuids = [str(uuid.uuid4()) for _ in range(unidades)]
        print(f"Lista de UUIDs: {lista_uuids}")


            

    
    def alquilar(self):
        if self.unidades == 0:
            self.disponible = False
            print (f"El libro no se puede alquilar")
        elif self.unidades > 0:
            #self.disponible = True
            print (f"El libro queda alquilado")
            self.unidades = self.unidades - 1
            self.unidades_alquiladas = self.unidades_alquiladas + 1
            print (f"Tenemos {self.unidades_alquiladas} alquiladas y quedan {self.unidades} para alquilar")
            return self.unidades_alquiladas, self.unidades
   
    def devolver(self):
        if self.unidades_alquiladas > 0:
            self.unidades_alquiladas -= 1
            self.unidades += 1
        else:
            print(f"No conozco ese libro")
        return self.unidades_alquiladas, self.unidades
    
    def __renovacion(self):
        
        if self.unidades > 0:
            print (f"El libro se renueva")
        else:
            print (f"El libro no se puede renovar")
    
    def verificar_renovacion(self):
        clave = input("Introduzca el password: ")
        if clave == "1234":
            self.__renovacion()
        
        

class Libro(Documento):
    def __init__(self, titulo,autor):
        super().__init__(titulo)
        self.autor = autor
        
    
class Revista(Documento):
    def __init__(self, titulo,tematica):
        super().__init__(tematica)
        self.tematica  = tematica
            
class DVD (Documento):
    def __init__(self, titulo, director):
        super().__init__(director)
        self.director = director
            
        
        
        
        
        
def __usuario(self, tipo_documento):
              
        if type(tipo_documento).__name__== "Libro":
            self.tipo_documento = coche
def usuario_verificado(self, titulo):
        clave = input("Introduzca el password: ")
        if clave == "1234":
            self.__asignar_coche(coche)
            
def __asignar_coche(self,coche):
                self.coche_empresa = coche
                print("{coche}")
            
def verifica_asignar_coche(self, coche):
                variable = input("introduzca un password")
                if variable == "1234":
                    self.__asignar_coche(coche)
   

documento1=Libro("Quijote","Miguel de Cervantes")
DVD1=DVD("Manolo", "Pájaros")
documento2= 
DVD1.compra(8)
documento1.compra(8)
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.alquilar()
documento1.devolver()   
documento1.__renovacion()
documento1.verificar_renovacion()
documento3 = Revista("Quijote","Viajar")



# for uuid in unidades:
#     print(f"Procesando item con UUID: {uuid}")
#     codigos_unicos = [str(uuid.uuid4()) for _ in range(unidades)]

import uuid

nuevo_uuid = str(uuid.uuid4())
print("Nuevo UUID:", nuevo_uuid)
lista_uuids = [str(uuid.uuid4()) for _ in range(5)]
print("Lista de UUIDs:", lista_uuids)



    
