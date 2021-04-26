#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

from classEmpleado import *

class Gerente(Empleado):
    def calcularSueldo(self, descuentos, bonificaciones):
        return self.sueldoBase-descuentos+bonificaciones
        