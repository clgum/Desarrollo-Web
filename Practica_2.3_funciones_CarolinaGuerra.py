#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de APlicaciones Web con Python
#Práctica 2.3

#Se importa librería
from random import randint
from funcionesAuditorio import *

#Definimos variables necesarias
PRECIO_ORIGINAL = 100
CAPACIDAD = 10000
monto_teorico = CAPACIDAD * PRECIO_ORIGINAL
suma_real_desc = 0
suma_percib = 0

#Agregamos categorías en 0
Categoria = {"PRIMERA":0, "SEGUNDA":0, "TERCERA":0, "CUARTA":0, "QUINTA":0}
descuentos = {
#Se hace la operación a cada categoría según el porcentaje
    "1":(PRECIO_ORIGINAL*0.30),
    "2":(PRECIO_ORIGINAL*0.10),
    "3":(PRECIO_ORIGINAL*0.15),
    "4":(PRECIO_ORIGINAL*0.25),
    "5":(PRECIO_ORIGINAL*0.35)
    }
#Agregamos listas para la suma de decuentos y entradas
suma_descs = [0, 0, 0, 0, 0]
suma_entradas = {"1":0, "2":0, "3":0, "4":0, "5":0}

#El rango será de la capacidad permitida
for i in range(10000):
#Tomará de forma aleatoria la edad según la indiquemos para cada categoría
    edad = randint(5,120)
#primera categoría
    if edad >= 5 and edad <= 14:
        Categoria["PRIMERA"] +=1
        suma_descs[0] += descuentos["1"]
        suma_entradas["1"] += PRECIO_ORIGINAL - descuentos["1"]
#segunda categoría
    elif edad >= 15 and edad <= 19:
        Categoria["SEGUNDA"] +=1
        suma_descs[1] += descuentos["2"]
        suma_entradas["2"] += PRECIO_ORIGINAL - descuentos["2"]
#tercera categoría
    elif edad >= 20 and edad <= 45:
        Categoria["TERCERA"] +=1
        suma_descs[2] += descuentos["3"]
        suma_entradas["3"] += PRECIO_ORIGINAL - descuentos["3"]
#cuarta categoría
    elif edad >= 46 and edad <= 65:
        Categoria["CUARTA"] +=1
        suma_descs[3] += descuentos["4"]
        suma_entradas["4"] += PRECIO_ORIGINAL - descuentos["4"]
#quinta categoría    
    else:
        Categoria["QUINTA"] +=1
        suma_descs[4] += descuentos ["5"]
        suma_entradas["5"] += PRECIO_ORIGINAL - descuentos["5"]

#Se indica función de la suma total 
suma_percib = obtSumaEntradas(suma_entradas)
print(f"La suma total percibida es $ {suma_percib:0.2f}")

#Sumatoria de los descuentos, se podría decir que es la "pérdida" de ganancias que hubo
suma_real_desc = obtSumaDescuentos(suma_descs)
print(f"Se dejó de percibir $ {suma_real_desc:0.2f}")

#La sumatoria anterior convertida en porcentaje
porcentaje1 = (suma_real_desc/monto_teorico) * 100
print(f"Lo que equivale a {porcentaje1:0.2f}% ")

#Lo que se hubiera ganado sin hacer descuentos
print(f"Se pudo haber obtenido {monto_teorico:00.2f}")

#Indicaremos los porcentajes que hubo segun su categoría 
porc1=(Categoria['PRIMERA'] / CAPACIDAD) * 100
porc2=(Categoria['SEGUNDA'] / CAPACIDAD) * 100
porc3=(Categoria['TERCERA'] / CAPACIDAD) * 100
porc4=(Categoria['CUARTA'] / CAPACIDAD) * 100
porc5=(Categoria['QUINTA'] / CAPACIDAD) * 100

#Convertimos a valores enteros
bar1=int(porc1)
bar2=int(porc2)
bar3=int(porc3)
bar4=int(porc4)
bar5=int(porc5)
print()
print("Entraron por rango de edad")
#RESULTADOS EN GRÁFICA DE BARRAS
print(f" 5-14: {Categoria['PRIMERA']:7.2f} : {porc1:5.2f}% : {('/' * bar1)}")
print(f"15-19: {Categoria['SEGUNDA']:7.2f} : {porc2:5.2f}% : {('/' * bar2)}")
print(f"20-45: {Categoria['TERCERA']:7.2f} : {porc3:5.2f}% : {('/' * bar3)}")
print(f"46-65: {Categoria['CUARTA']:7.2f} : {porc4:5.2f}% : {('/' * bar4)}")
print(f"65- >: {Categoria['QUINTA']:7.2f} : {porc5:5.2f}% : {('/' * bar5)}")


    