#Carolina Elizabeth Guerra Mota
#Ing. informática
#Desarrollo de Aplicaciones Web con Python
#Ejercicio de Evaluación corte 2

from classCaja import *

#Construimos un objeto con la clase caja
cajita= Caja(5,6,1.5)

#Usamos el método mostrar
print(cajita.mostrar())
print()

#Mostramos su volumen
print("Volumen: ", cajita.calcularVolumen())
print()

#Mostramos su area
print("Área Total: ", cajita.calcularAreaTotal())
print()

#Creamos clon
miClon= cajita.clon()
#Mostramos info del clon
print(miClon.mostrar())
print()

#Creamos una caja más gde. a partir del clon con ayuda de cajita
cajaGde= cajita.crearCajaGrande()
#Mostramos info de la caja más gde
print(cajaGde.mostrar())
print()

#Verificamos si la primer caja cabe en la segunda
Res= miClon.cabe1DentroDe2(cajita, cajaGde)
print("Más grande???: ", Res)
