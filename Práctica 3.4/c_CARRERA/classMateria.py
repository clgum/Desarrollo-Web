#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

from classCarrera import *

class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre=nombre
        self.profesor=profesor
        #no puede ser anterior a 2006
        self.fechaInicioDictado=fecha

    @property
    def fechaInicioDictado(self):
        return self._fechaInicioDictado
 
    @fechaInicioDictado.setter
    def fechaInicioDictado(self, fecha):
        if fecha<2006:
            self._fechaInicioDictado=2006
        else:
            self._fechaInicioDictado=fecha
