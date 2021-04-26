#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

#Creamos clase empleado
class Empleado:
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.sueldoBase=sueldo

    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos