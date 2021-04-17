#En este archivo se van a definir las funciones que usaremos.

def obtSumaEntradas(suma_entradas):
#variable en 0
    suma=0
#".values() sirve para regresar la lista de todos los valores disponibles de este caso será de suma_entradas"
    for v in suma_entradas.values():
#se sumarán todos los resultados a la variable
        suma+=v
#retorna el valor final de la variable suma
    return suma

#Se repite el procedimiento aterior pero ahora con la suma de los descuentos.
def obtSumaDescuentos(suma_descs):
    suma=0
    for v in suma_descs:
        suma+=v
    return suma