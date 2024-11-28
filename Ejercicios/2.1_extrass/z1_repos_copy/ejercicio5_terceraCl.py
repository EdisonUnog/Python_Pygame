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

while True:
    
    dato_a_obtener = input("¿Que desea saber? Ingrese: \n(1) Nombres.\n(2) Nombres y altura.\n"
                           "(3) Heroe más alto.\n(4) Heroe más bajo.\n(5) Promedio altura.\n"
                           "(6) Heroe más bajo y heroe mas alto.\n(7) Para cancelar.")

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
        break
