#Carolina Elizabeth Guerra Mota
#Ing. INformática
#Desarrollo de Aplicaciones Web con Python
#Práctica 3.4

#Implementamos una clase llamada Gato
#Se darán 3 atributos: Nombre, Edad y Alimento favorito
class Gato:
    especie="mamifero"
#El constructor recibe dos valores, que serán nombre y edad
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[]
#Como métodos además del constructor, tendremos uno que nos permita ver la étapa de vida
    def verEtapaDeVida(self):
        if self.edad>2:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorrito")
#También como método determinaremos si un alimento es uno de los favoritos
    def esAlimentoFavorito(self, alimento):
        return alimento in self.alimentos
