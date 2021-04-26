#Carolina Elizabeth Guerra Mota
#Ing. informática
#Desarrollo de Aplicaciones Web con Python
#Ejercicio de Evaluación Corte 2

#Crear clase caja
class Caja:
    #Constructores
    def __init__(self, ancho, largo, alto):
        self.ancho=ancho
        self.largo=largo
        self.alto=alto

    #Método para mostrar contenido de la caja
    def mostrar(self):
        return "Alto: ", self.alto, "Ancho: ", self.ancho, "Largo: ", self.largo
    
    #Método para calcular el volumen de la caja
    def calcularVolumen(self):
        r=(self.alto * self.ancho * self.largo)
        return r
    
    #Método para calcular el área frontal
    def areaFrontal(self):
        return self.ancho * self.alto

    #Método para calcular el área lateral
    def areaLateral(self):
        return self.largo * self.alto

    #Método para calcular el área suoerior
    def areaSuperior(self):
        return self.largo * self.ancho

    #Método para calcular el área total
    def calcularAreaTotal(self):
        r=(2 * self.areaFrontal() + 2 * self.areaLateral() + 2 * self.areaSuperior())
        return r

    #Método para crear un clon de si misma
    def clon(self):
        c= Caja(self.ancho, self.alto, self.largo)
        return c

    #Método para crear una caja el 25% más grande
    def crearCajaGrande(self):
        nuevoAlto=self.alto * 1.25
        nuevoAncho=self.ancho * 1.25
        nuevoLargo=self.largo * 1.25

        cajaNueva = Caja(nuevoAncho, nuevoLargo, nuevoAlto)
        return cajaNueva

    #Método para comparar las cajas
    def cabe1DentroDe2(self, c, cajaNueva):
        #se comparan todas las dimensiones
        if c.ancho < cajaNueva.ancho and c.alto < cajaNueva.alto and c.largo < cajaNueva.largo:
            return "Sí Cabe"

        else:
            return "No Cabe"
