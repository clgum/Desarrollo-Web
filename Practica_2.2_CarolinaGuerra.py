#Carolina Elizabeth Guerra Mota
#Ing. Informática.
#Desarrollo de Aplicaciones Web con Python
#Páctica 2.2 Prcaticando con condicionales Python

#Iniciaremos guardando las variables y covertiendo la fecha a mínusculas, 
#para que sean reconocidas en cualquier caso.
fecha=input("Fecha (formato 'día, DD/MM'): ").lower()
#Vamos a extraer las partes de la fecha por separado a través de variables.
diasem=fecha[0:fecha.find(',')]
dianum=int(fecha[fecha.find(' ')+1:fecha.find('/')])
mesnum=int(fecha[fecha.find('/')+1:])

#Evaluar que el número de día no supere el 31 y el número de mes no supere 12,
#en caso de que no se cumpla, se finaliza el programa.
if dianum>31 or mesnum>12:
    print("FECHA INCORRECTA")
#Se comenzará a dar las condiciones para cada día según el ejercicio, 
#a partir de la respuesta que de el usuario se tendrá un resultado diferente.
else:
    #Si el usuario da una respuesta de lunes, martes o miércoles, el programa 
    #le preguntará si se tomaron exámenes, si la respuesta es n, se termina ahí
    #pero si la respuesta es s, le pregunta cuántos fueron aprobados
    #y cuantos reprobados, de ese resultado da un porcentaje de aprobados.   
    if diasem in "lunes,martes,miércoles":
        respuesta=input("¿Se tomaron exámenes? S/N: ")
        if respuesta.lower()=="s":
            aprob=int(input("Cantidad de aprobados: "))
            reprob=int(input("Cantidad de reprobados: "))
            print("Porcentaje de aprobados: ", (aprob*100)/(aprob+reprob) ,"%") 

    #En caso que se de un jueves, preguntará cuál fue el porcentaje de asistencia,
    #en caso que se de un número mayor a 50 la respuesta será que asistió la mayoría,
    #si es menos a 50, será lo contrario.
    elif diasem == "jueves":
        asistencia=int(input("Porcentaje de asistencia: "))
        if asistencia>50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")

    #Si se da un viernes, el día 01 y mes 01 o 07, mandará un mensaje para indicar
    #que está comenzando un nuevo ciclo.
    #Preguntará cuantos alumnos ingresan, y cuál es el costo por alumno, para
    #indicar cual es el ingreso total.
    elif diasem == "viernes":
        if dianum==1 and (mesnum==1 or mesnum==7):
            print("Comienzo de nuevo ciclo")
            alumn=int(input("Cantidad de alumnos: "))
            costo=float(input("Costo por alumno: $"))
            print("Ingreso Total: $", alumn*costo)

    #Si no se da una fecha como lo indica, el programa termina        
    else:
        print("FECHA INCORRECTA")

print("FIN DEL PROGRAMA")