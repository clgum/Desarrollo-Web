#Carolina Elizabeth Guerra Mota
#Ing. Informática
#Desarrollo de Aplicaciones Web con Python
#Práctica 2.1 Votos

import random 
print("¿Por cuál partido votará?")
print ("""A = Amarillo 
B = Morado 
C = Rojo""")

print()
candidato=input("Candidato que fue seleccionado: ")
if candidato.lower()=="a":
    print("Votaste por el partido amarillo")
elif candidato.lower()=="b":
    print("Votaste por el partido morado")
elif candidato.lower()=="c":
    print("Votaste por el partido rojo")
else:
    print("Opción errónea.")

print()
print("CONTABILIZANDO TODOS LOS VOTOS...")
partidos=["A", "B", "C"]
partA=0
partB=0
partC=0

for i in range (2000000):
    votos=random.choice(partidos)
    if votos =="A":
        partA +=1
    elif votos =="B":
        partB +=1
    elif votos == "C":
        partC +=1
print()
if partA > partB and partC:
        print("El ganador es el partido AMARILLO con estos votos: ",partA)
elif partB > partA and partC:
        print("El ganador es el partido MORADO con estos votos: ",partB)
elif partC > partA and partB:
        print("El ganador es el partido ROJO con estos votos: ",partC)