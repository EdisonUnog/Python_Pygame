from data_stark import lista_personajes

def funct_imprimir_nombres():
    for personaje in lista_personajes:
        print("Nombre = {0}.".format(personaje["nombre"]))

def funct_imprimir_nombre_altura():
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        print("Nombre = {0} , Altura = {1:.2f} ".format(personaje["nombre"], personaje["altura"]))

def funct_heroe_mas_alto():
    superheroe_mas_alto = lista_personajes[0]

    for personaje in lista_personajes: 
        personaje["altura"] = float(personaje["altura"])
        if superheroe_mas_alto["altura"] < personaje["altura"]:
            superheroe_mas_alto = personaje
    print("Superheroe más alto es : {0} y mide {1:.2f}.".format(superheroe_mas_alto["nombre"], superheroe_mas_alto["altura"]))

def funct_heroe_mas_bajo():
    superheroe_mas_bajo = lista_personajes[0]

    for personaje in lista_personajes: 
        personaje["altura"] = float(personaje["altura"])
        if superheroe_mas_bajo["altura"] > personaje["altura"]:
            superheroe_mas_bajo = personaje
    print("Superheroe más bajo es : {0} y mide {1:.2f}.".format(superheroe_mas_bajo["nombre"], superheroe_mas_bajo["altura"]))

def funct_promedio_altura():
    acumulador_altura = 0

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        acumulador_altura += personaje["altura"]
    promedio_de_altura = acumulador_altura // len(lista_personajes)
    print("El promedio de altura de los personajes es : {0}.".format(promedio_de_altura))

def funct_heroe_mas_menos_peso():
    super_mas_pesado = lista_personajes[0]
    super_menos_pesado = lista_personajes[0]

    for personaje in lista_personajes: 
        personaje["peso"] = float(personaje["peso"])
        if super_mas_pesado["peso"] < personaje["peso"]:
            super_mas_pesado = personaje
        if super_menos_pesado["peso"] > personaje["peso"]:
            super_menos_pesado = personaje
    print("El heroe más pesado es {0}, pesa {1:.2f} y el menos pesado es {2} y pesa {3:.2f}."
            .format(super_mas_pesado["nombre"], super_mas_pesado["peso"], super_menos_pesado["nombre"], super_menos_pesado["peso"]))

def funct_impr_hero_m():
    for personaje in lista_personajes:
        if personaje ["genero"] == "M":
            print("Nombre: {0}".format(personaje["nombre"]))

def funct_impr_hero_f():
    for personaje in lista_personajes:
        if personaje ["genero"] == "F":
            print("Nombre: {0},".format(personaje["nombre"]))

def funct_hero_m_mas_alto():
    hero_m_mas_alto = {}
    flag = True
    for personaje in lista_personajes:
        if personaje ["genero"] == "M":
            personaje["altura"] = float(personaje["altura"])
            if flag == True:
                hero_m_mas_alto = personaje
                flag = False
            elif hero_m_mas_alto["altura"] < personaje["altura"]:
                hero_m_mas_alto = personaje
    print("El personaje másculino más alto es: {0} y mide {1:.2f}".format(hero_m_mas_alto["nombre"]
                                                                ,hero_m_mas_alto["altura"]))

def funct_hero_f_mas_alto():
    hero_f_mas_alto = {}
    flag = True
    for personaje in lista_personajes:
        if personaje ["genero"] == "F":
            personaje["altura"] = float(personaje["altura"])
            if flag == True:
                hero_f_mas_alto = personaje
                flag = False
            elif hero_f_mas_alto["altura"] < personaje["altura"]:
                hero_f_mas_alto = personaje
    print("El personaje másculino más alto es: {0} y mide {1:.2f}".format(hero_f_mas_alto["nombre"]
                                                                ,hero_f_mas_alto["altura"]))

def funct_hero_m_mas_bajo():
    heroe_m_mas_bajo = {}
    flag = True
    for personaje in lista_personajes:
        if personaje ["genero"] == "M":
            personaje["altura"] = float(personaje["altura"])
            if flag == True:
                heroe_m_mas_bajo = personaje
                flag = False
            elif heroe_m_mas_bajo["altura"] > personaje["altura"]:
                heroe_m_mas_bajo = personaje
    print("El personaje másculino más bajo es: {0} y mide {1:.2f}".format(heroe_m_mas_bajo["nombre"]
                                                                ,heroe_m_mas_bajo["altura"]))

def funct_hero_f_mas_bajo():
    heroe_f_mas_bajo = {}
    flag = True
    for personaje in lista_personajes:
        if personaje ["genero"] == "F":
            personaje["altura"] = float(personaje["altura"])
            if flag == True:
                heroe_f_mas_bajo = personaje
                flag = False
            elif heroe_f_mas_bajo["altura"] > personaje["altura"]:
                heroe_f_mas_bajo = personaje
    print("El personaje femenino más bajo es: {0} y mide {1:.2f}".format(heroe_f_mas_bajo["nombre"]
                                                                ,heroe_f_mas_bajo["altura"]))

def funct_promedio_altura_m():
    acumulador_altura_m = 0
    contador_heroes_m = 0
    promedio_altura_m = 0
    for personaje in lista_personajes:
        if personaje ["genero"] == "M":
            personaje["altura"] = float(personaje["altura"])
            acumulador_altura_m += personaje["altura"]
            contador_heroes_m += 1
    promedio_altura_m = acumulador_altura_m / contador_heroes_m
    print("El promedio de altura de heroes másculinos es : {0:.2f}".format(promedio_altura_m))

def funct_promedio_altura_f():
    acumulador_altura_f = 0
    contador_heroes_f = 0
    promedio_altura_f = 0
    for personaje in lista_personajes:
        if personaje ["genero"] == "F":
            personaje["altura"] = float(personaje["altura"])
            acumulador_altura_f += personaje["altura"]
            contador_heroes_f += 1
    promedio_altura_f = acumulador_altura_f / contador_heroes_f
    print("El promedio de altura de heroes femeninos es : {0:.2f}".format(promedio_altura_f))

def funct_contador_color_ojos():
    dict_ojos = {}
    for personaje in lista_personajes:
        color = personaje["color_ojos"]
        if color not in dict_ojos:
            dict_ojos[color] = 1
        else :
            dict_ojos[color] += 1
    for color in dict_ojos:
        print("La cantidad de heroes con ojos color {0} es {1}.".format(color,dict_ojos[color]))
        
def funct_contador_color_pelo():
    dict_pelo = {}
    for personaje in lista_personajes:
        pelo = personaje["color_pelo"]
        if pelo not in dict_pelo:
            dict_pelo[pelo] = 1
        else :
            dict_pelo[pelo] += 1
    for pelo in dict_pelo:
        print("La cantidad de heroes con pelo color {0} es {1}.".format(pelo,dict_pelo[pelo]))

def funct_contador_intelig():
    dict_intelig = {}
    for personaje in lista_personajes:
        intelig = personaje["inteligencia"]
        if intelig not in dict_intelig:
            if intelig == "":
                dict_intelig["No tiene"] = 1
            else:
                dict_intelig[intelig] = 1
        else :
            if intelig == "":
                dict_intelig["No tiene"] += 1
            else:
                dict_intelig[intelig] += 1
    for intelig in dict_intelig:
        print("La cantidad de heroes con inteligencia {0} es {1}.".format(intelig,dict_intelig[intelig]))
    
def funct_nombres_por_color_ojos():
    dict_ojos_nombres = {}
    for personaje in lista_personajes:
        color = personaje["color_ojos"]
        if color not in dict_ojos_nombres.keys():
            nombres = []
            nombres.append(personaje["nombre"])
            dict_ojos_nombres[color] = nombres
        else :
            list(dict_ojos_nombres[color])
            dict_ojos_nombres[color].append(personaje["nombre"])

    for color in dict_ojos_nombres:
       mensaje = (" | ".join(dict_ojos_nombres[color])) 
       print("Los heroes con ojos color {0} son {1}.".format(color,mensaje))

def funct_nombres_por_pelo():
    dict_pelo_nombres = {}
    for personaje in lista_personajes:
        color = personaje["color_pelo"]
        if color not in dict_pelo_nombres.keys():
            nombres = []
            nombres.append(personaje["nombre"])
            dict_pelo_nombres[color] = nombres
        else :
            list(dict_pelo_nombres[color])
            dict_pelo_nombres[color].append(personaje["nombre"])

    for color in dict_pelo_nombres:
       mensaje = (" | ".join(dict_pelo_nombres[color]))
       print("Los heroes con pelo color {0} son {1}.".format(color,mensaje))

def funct_inteligencia_nombres():
    dict_intelig = {}
    for personaje in lista_personajes:
        intelig = personaje["inteligencia"]
        if intelig not in dict_intelig.keys():
            nombres = []
            nombres.append(personaje["nombre"])
            dict_intelig[intelig] = nombres

        else :
            list(dict_intelig[intelig])
            dict_intelig[intelig].append(personaje["nombre"])

    for intelig in dict_intelig:
        mensaje = " | ".join(dict_intelig[intelig])        
        if intelig == "":
            intelig = "no tiene"
        print("Los heroes con inteligencia {0} son {1}.".format(intelig,mensaje))

while True:
    
    dato_a_obtener = input("¿Que desea saber? Ingrese: \n(1) Nombres.\n(2) Nombres y altura.\n"
                           "(3) Heroe más alto.\n(4) Heroe más bajo.\n(5) Promedio altura.\n"
                           "(6) Heroe más y menos pesado.\n(7) Nombres heroes masculinos.\n"
                           "(8) Nombres heroes femeninos.\n(9) Heroe másculino más alto.\n"
                           "(10) Heroe femenino más alto.\n(11) Heroe másculino más bajo.\n"
                           "(12) Heroe femenino más bajo.\n(13) Promedio de altura de heroes másculinos.\n"
                           "(14) Promedio de altura de heroes femeninos.\n(15) Cantidad de heroes"
                           " con cada color de ojos.\n(16) Cantidad de heroes con cada color de pelo.\n"
                           "(17) Cantidad de heroes con cada inteligencia.\n(18) Los heroes con cada color de"
                           "ojos.\n(19) Los heroes con cada color de pelo.\n(20) Los heroes con cada tipo de "
                           "inteligencia.\n")

    if dato_a_obtener == "1":
        funct_imprimir_nombres()
    elif dato_a_obtener == "2":
        funct_imprimir_nombre_altura()
    elif dato_a_obtener == "3":
        funct_heroe_mas_alto()
    elif dato_a_obtener == "4":
        funct_heroe_mas_bajo()
    elif dato_a_obtener == "5":
        funct_promedio_altura()
    elif dato_a_obtener == "6":
        funct_heroe_mas_menos_peso()
    elif dato_a_obtener == "7":
        funct_impr_hero_m()
    elif dato_a_obtener == "8":
        funct_impr_hero_f()
    elif dato_a_obtener == "9":
        funct_hero_m_mas_alto()
    elif dato_a_obtener == "10":
        funct_hero_f_mas_alto()
    elif dato_a_obtener == "11":
        funct_hero_m_mas_bajo()
    elif dato_a_obtener == "12":
        funct_hero_f_mas_bajo()
    elif dato_a_obtener == "13":
        funct_promedio_altura_m()
    elif dato_a_obtener == "14":
        funct_promedio_altura_f()
    elif dato_a_obtener == "15":
        funct_contador_color_ojos()
    elif dato_a_obtener == "16":
        funct_contador_color_pelo()
    elif dato_a_obtener == "17":
        funct_contador_intelig()
    elif dato_a_obtener == "18":
        funct_nombres_por_color_ojos()
    elif dato_a_obtener == "19":
        funct_nombres_por_pelo()
    elif dato_a_obtener == "20":
        funct_inteligencia_nombres()
    else:
        break

'''Desafío #01:
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos, utilizando un menú 
que permita acceder a cada uno de los puntos por separado.
   A Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
   B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
   C Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
   D Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
   E Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
   F Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
   G Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
   H Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
   I Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
   J Determinar cuántos superhéroes tienen cada tipo de color de ojos.
   K Determinar cuántos superhéroes tienen cada tipo de color de pelo.
   L Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, 
   M Inicializarlo con ‘No Tiene’). 
   N Listar todos los superhéroes agrupados por color de ojos.
   Ñ Listar todos los superhéroes agrupados por color de pelo.
   O Listar todos los superhéroes agrupados por tipo de inteligencia
'''