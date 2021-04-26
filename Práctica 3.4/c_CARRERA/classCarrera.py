#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.materias={}

    def agregarMateria(self, materia, codigo):
        self.materias[codigo]=materia
        