'''
Edison Francisco Uñog Valencia...

Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)

'''
######################################################################
from os import system

system("cls")

acumulador_edad = 0
contador = 0 
contador_votos = 0

edad_minima = 0
flag_edad = True

acumulador_nacho = 0
acumulador_julieta = 0
acumulador_marcos = 0
contador_nacho = 0
contador_julieta = 0
contador_marcos = 0

######################################################################
while True:

    nombre_votante = str(input("Ingrese su nombre: "))

    edad = int(input("Ingrese su edad mayor a 13: "))
    while edad<13 !=True :
        print("DEBE SER MAYOR A 13 AÑOS")
        edad = int(input("Ingrese su edad mayor a 13: "))

    genero = str(input("Ingrese genero : masculino , femenino , otro:  "))
    while genero != "masculino" and genero != "femenino" and genero != "otro" !=True:
        print("ERROR INGRESE UN GENERO")
        genero = str(input("Ingrese un genero: "))


    voto = str(input("Ingrese su voto : marcos , julieta , nacho: "))
    while voto != "marcos" and voto != "julieta" and voto != "nacho" !=True:
        print("ERROR INGRESE EL VOTO")
        voto = str(input("Ingrese un voto: "))
        
    #El promedio de edad de las votantes de género femenino
    if genero == "femenino":
        acumulador_edad = acumulador_edad + edad
        contador += 1

    #masculino edad entre 25 y 40, que voten nacho y julieta
    if genero == "masculino":
        if edad < 25 or edad > 40:
            if voto == "nacho" or voto == "julieta":
                contador_votos +=1

    #votante mas joven a nacho
    if voto == "nacho":
         if flag_edad == True or edad < edad_minima:
            edad_minima = edad
            nombre_minimo = nombre_votante
            flag_edad = False

    ######################################################################
    #votos totales y quien gano 
    match voto:
        case "nacho":
            acumulador_nacho += acumulador_nacho
            contador_nacho += contador_nacho
            
        case "julieta":
            acumulador_julieta += acumulador_julieta
            contador_julieta += contador_julieta

        case "marcos":
            acumulador_marcos += acumulador_marcos
            contador_marcos += contador_marcos
    ######################################################################

    seguir = input("\n Deseas continuar si / no:")
    if seguir != "si":
        break
    ########################_FIN DEL WHILE_#############################

#Total de los votos
Total_votos = contador_nacho + contador_julieta + contador_marcos
porcentaje = 100 / Total_votos

#opcion A
promedio = float(acumulador_edad)/contador

#opcion D
porcentaje_nacho = porcentaje * contador_nacho
porcentaje_julieta = porcentaje * contador_julieta
porcentaje_marcos = porcentaje * contador_marcos

#opcion e
if contador_nacho > contador_julieta and contador_nacho > contador_marcos:
    ganador = "nacho"
elif contador_marcos > contador_julieta:
    ganador = "marcos"
else:
    ganador = "julieta"

#################################_RESPUESTAS_##############################
#opcion A
print(f" promedio femeninos: {promedio}")

#opcion B
print(f"\n Votos masculinos a favor de nacho y juelieta: {contador_votos}")

#opcion C
print(f"\n Edad del votante mas joven: {nombre_minimo} edad: {edad_minima}")

#opcion D
print(f"el porcentaje de nacho fue: {porcentaje_nacho}")
print(f"el porcentaje de julieta fue: {porcentaje_julieta}")
print(f"el porcentaje de marcos fue: {porcentaje_marcos}")

#opcion E
print(f"el ganador de gh 2022 es: {ganador}")

############################################################################

