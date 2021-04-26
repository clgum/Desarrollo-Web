#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

from classEmpleado import *

class Tripulante(Empleado):
    def mostrarRenovacionLicencia(self):
        if self.edad<50:
            print("Renueva su licencia cad 1 año")
        else:
            print("Renueva su licencia cada 6 meses")
