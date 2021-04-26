#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

from classEmpleado import *

class AgenteVentas(Empleado):
    def __init__(self, nombre, edad, legajo, sueldo, mostrador):
        self.numeroMostrador=mostrador
        super().__init__(nombre, edad, legajo, sueldo)
