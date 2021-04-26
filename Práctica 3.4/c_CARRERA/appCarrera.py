#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

from classCarrera import *
from classMateria import *

ing=Carrera("Ingeniería")
algebra=Materia("Álgebra", "Ricardo Quinteros", 2010)
fisica=Materia("Física", "Margarita Gomez", 2006)
quimica=Materia("Quimica", "Lorena Rios", 2003)
ing.agregarMateria(algebra,466)

print("Algebra inició en: ", algebra.fechaInicioDictado)
print("Fisica inició en: ", fisica.fechaInicioDictado)
print("Quimica inició en: ", quimica.fechaInicioDictado)
