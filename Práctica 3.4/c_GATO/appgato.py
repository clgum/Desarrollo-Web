#Carolina Elizabeth Guerra Mota
#Ing. INformática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

#Importamos la clase necesaria
from classgato import *
#Con los parámetros que hemos dado mandaremos llamar los atributos, el nombre y edad del gato
p = Gato("Pelusa",1)
print("El nombre del gato 1 es: ", p.nombre)
#Agregamos elementos a la lista alimentos,que previamente estaba vacía
p.alimentos = ["pescado", "leche"]
#Mediante los métodos, mandaremos llamar la edad y alimento favorito del gato
p.verEtapaDeVida()
print("La edad de este gato es: ", p.edad)
print(p.esAlimentoFavorito("leche"))
print()

#Repetimos los pasos para un segundo gato
g = Gato("Cleo",5)
print("El nombre del gato 2 es: ", g.nombre)
g.alimentos = ["leche", "galletas"]
g.verEtapaDeVida()
print("La edad de este gato es: ", g.edad)
print(g.esAlimentoFavorito("galletas"))
