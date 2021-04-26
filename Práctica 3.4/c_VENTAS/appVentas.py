#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

#Importamos todas las clases necesarias
from classAgenteVentas import *
from classEmpleado import *
from classTripulante import *
from classGerente import *

p=AgenteVentas("Pedro Martínez", 32, "A120", 55000, 4)
print("El nombre del Agente de Ventas es: ", p.nombre)
print("Su sueldo final es de: ", p.calcularSueldo(100, 3000))
print()

l=Tripulante("Lucas Gutierrez", 40, "H618", 60000)
print("El tripulante es: ", l.nombre)
print(l.mostrarRenovacionLicencia())
print()

m=Empleado("Marcos Rios", 22, "H1N1", 30000)
print("El nombre del Empleado es: ", m.nombre)
print("El sueldo que gana: ",  m.calcularSueldo(1000,0))
print()

j=Gerente("Julia Campos", 35, "G100",60000)
print(j.nombre,"es la gerente.")
