from data_stark import lista_personajes
from os import system

#menu de inicio
def menu_integrador_uno()->int:
    print("\n 1._Heroes genero masculino")
    print(" 2._Heroes genero femenino")
    print(" 3._Masculino mas alta")
    print(" 4._Femenina mas alto")
    print(" 5._Masculino mas bajo")
    print(" 6._Femenino mas bajo")
    print(" 7._Promedio altura, género Masculino")
    print(" 8._Promedio altura, género Femenino") #H
    print(" 9._Cantidad de heroes con los mismos color de ojos")
    print(" 10._Cantidad de heroes con el mismo color de pelo")
    print(" 11._Cantidad de heroes con la misma inteligencia y los que no tienen._")
    print(" 12._Listar a los super heroes por su color de ojos")
    print(" 13._Listar a los super heroes por su color de pelo")
    print(" 14._Listar a los super heroes por su tipo inteligencia")

    opcion = int(input("\n >>ELIGE UNA OPCION: "))
    while opcion < 1 or opcion > 15:
        print(" Error..")
        opcion = int(input("\n >>ELIGE UNA OPCION: "))
    return opcion

print(type(lista_personajes))
print(type(lista_personajes[0]))

#####################################################################################
####################_Funciones_para_Imprimir_generos_M_F##########################

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
####sintaxis
def buscar_por_genero_sintaxis(lista:list, clave = None, valor = None):
    if clave is None:
        for x in lista:
            print(f"\n*nombre superheroe: {x['nombre']} ")
    else:
        for x in lista:
            if x[clave] == valor:
                print(f"\n *Nombre: {x['nombre']}, - *Genero: {x['genero']}")

####
def print_por_genero_masculino(lista:list):
    if type(lista) == list and len(lista) > 0:
        buscar_por_genero_sintaxis(lista,'genero','M')

#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
####
def print_por_genero_femenino(lista:list):
    if type(lista) == list and len(lista) > 0:
        buscar_por_genero_sintaxis(lista,'genero','F')
#####################################################################################
#####################################################################################
##Sintaxis
def calcular_maximo_flotante(lista:list, clave:str, clave_dos = None, valor = None)->float:
    flag_primero = True
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0):

        if clave_dos is None:
            for x in lista:
                if flag_primero == True or float(x[clave]) > float(maximo):
                    maximo = float(x[clave])
                    flag_primero = False
        else:
            for x in lista:
                if x[clave_dos] == valor:
                    if flag_primero == True or float(x[clave]) > float(maximo):
                        maximo = float(x[clave])
                        flag_primero = False
    return maximo

#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def print_max_alto_masculino(lista:list):
    maximo_m =calcular_maximo_flotante(lista,'altura','genero','M')
    print(f"\n *Estatura maxima M: {maximo_m}")
    print(type(maximo_m))
    max_len = str(maximo_m)
    print(type(max_len))

    buscar_por_genero_sintaxis(lista,'altura',max_len)
#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def print_max_alto_femenino(lista:list):
    maximo_f = calcular_maximo_flotante(lista,'altura','genero','F')
    print(f"\n *Estatura maxima F: {maximo_f}")
    print(type(maximo_f))
    max_len = str(maximo_f)
    print(type(max_len))
    buscar_por_genero_sintaxis(lista,'altura',max_len)

#####################################################################################
##Sintaxis
def calcular_minimo_flotante(lista:list, clave:str, clave_dos = None, valor = None)->float:
    flag_primero = True
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0):

        if clave_dos is None:
            for x in lista:
                if flag_primero == True or float(x[clave]) < float(maximo):
                    maximo = float(x[clave])
                    flag_primero = False
        else:
            for x in lista:
                if x[clave_dos] == valor:
                    if flag_primero == True or float(x[clave]) < float(maximo):
                        maximo = float(x[clave])
                        flag_primero = False
    return maximo
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def print_bajo_masculino(lista:list):
    minimo_m =calcular_minimo_flotante(lista,'altura','genero','M')
    print(f"\n *Estatura baja M: {minimo_m}")
    max_len = str(minimo_m)
    buscar_por_genero_sintaxis(lista,'altura',max_len)
#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def print_bajo_femenino(lista:list):
    minimo_f = calcular_minimo_flotante(lista,'altura','genero','F')
    print(f"\n *Estatura baja F: {minimo_f}")
    max_len = str(minimo_f)
    buscar_por_genero_sintaxis(lista,'altura',max_len)

#####################################################################################
#G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
def calcular_promedio_sintaxis(lista:list, clave:str, valor:str)->float:
    acumulador_altura = 0
    contador_altura = 0

    for x in lista:
        if x['genero'] == valor:
            acumulador_altura += float(x[clave])
            contador_altura += 1

    promedio = acumulador_altura / contador_altura
    
    return promedio

def print_promedio_m(lista:list):
    promedio = calcular_promedio_sintaxis(lista,'altura','M')
    print(promedio)

#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F

def print_promedio_f(lista:list):
    promedio = calcular_promedio_sintaxis(lista,'altura','F')
    print(promedio)

#####################################################################################
#I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
'''resuelto'''
#####################################################################################
#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def print_heroes_tipos_ojos(lista:list):
    contador = {}
    
    for x in lista:
        if x["color_ojos"] not in contador:
            contador[x["color_ojos"]] = 1
        else:
            contador[x["color_ojos"]] += 1

    for color, cantidad in contador.items():
        print(f"  {cantidad} superhéroes con color de ojos {color}")

#####################################################################################
#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def print_heroes_tipos_cabello(lista:list):
    contador = {}

    for x in lista:
        if x['color_pelo'] not in contador:
            contador [x['color_pelo']] = 1
        else:
            contador [x['color_pelo']] += 1

    for pelo, cantidad in contador.items():
        print(f"  {cantidad} superhéroes con el mismo color de cabello: {pelo}")

#####################################################################################
#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
def print_heroes_tipos_inteligencia(lista:list):
    contador = {}

    for x in lista:
        if x['inteligencia'] not in contador:
            contador [x['inteligencia']] = 1
        else:
            contador [x['inteligencia']] += 1

    for inteligencia, cantidad in contador.items():
        if inteligencia == "":
                inteligencia = "no tiene"
        print(f"  {cantidad} superhéroes con la misma inteligencia: {inteligencia}")


#####################################################################################
#####################################################################################
def colores_iguales(lista:list, clave:str):
    lista_colores = []
    for x in lista:
        color = x[clave]
        lista_colores.append(color)
    lista_filtrada = set(lista_colores)

    for color in lista_filtrada:
        if color == "":
            print(f"No tiene {clave}")
        else:
            print(f"{color}")

        for x in lista:
            if x[clave] == color:
                print(f"\t {x['nombre']}")
#M. Listar todos los superhéroes agrupados por color de ojos.
def print_heroes_mismos_ojos(lista:list):
    if type(lista) == list and len(lista) >0:
        colores_iguales(lista,'color_ojos')

#N. Listar todos los superhéroes agrupados por color de pelo.
def print_heroes_mismo_pelo(lista:list):
    if type(lista) == list and len(lista) >0:
        colores_iguales(lista,'color_pelo')

#O. Listar todos los superhéroes agrupados por tipo de inteligencia
def print_heroes_misma_inteligencia(lista:list):
    if type(lista) == list and len(lista) >0:
        colores_iguales(lista,'inteligencia')




'''def print_heroes_mismos_ojos(lista:list):
    contador = {}
    
    for x in lista:
        if x["color_ojos"] not in contador:
            contador[x["color_ojos"]] = 1
        else:
            contador[x["color_ojos"]] += 1

    for color, cantidad in contador.items():
        print(f"\n  {cantidad} superhéroes con color de ojos {color}")

        for x in lista:
            if x['color_ojos'] == color:
                print(f"\tnombre_color: {x['nombre']}")'''

'''
def print_heroes_mismo_pelo(lista:list):
    contador = {}
    
    for x in lista:
        if x["color_pelo"] not in contador:
            contador[x["color_pelo"]] = 1
        else:
            contador[x["color_pelo"]] += 1

    for pelo, cantidad in contador.items():
        print(f"\n  {cantidad} superhéroes con color de cabello: {pelo}")

        for x in lista:
            if x['color_pelo'] == pelo:
                print(f"\tnombre_color: {x['nombre']}")
'''

'''
def print_heroes_misma_inteligencia(lista:list):
    contador = {}
    
    for x in lista:
        if x["inteligencia"] not in contador:
            contador[x["inteligencia"]] = 1
        else:
            contador[x["inteligencia"]] += 1

    for inteligencia, cantidad in contador.items():
        if inteligencia == "":
            print(f"  {cantidad} no tiene")
        else:
            print(f"\n  {cantidad} superhéroes con la misma inteligencia: {inteligencia}")

        for x in lista:
            if x['inteligencia'] == inteligencia:
                print(f"\tnombre_color: {x['nombre']}")
            

'''