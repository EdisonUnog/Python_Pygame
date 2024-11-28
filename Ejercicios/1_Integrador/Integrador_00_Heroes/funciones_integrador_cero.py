
from data_stark import lista_personajes
from os import system

#crear un menu
def menu_integrador_cero()->int: ## views -> vistas
    print("\n 1._Mostrar nombres heroes")
    print(" 2._Mostrar nombres y altura")
    print(" 3._Mostrar heroem con mas altao")
    print(" 4._Mostrar heroe con menos altura")
    print(" 5._Promedio de views")
    print(" 6._Heroe mas y menos pesado")
    print(" 7._Mas opciones...")
    print(" 8._salir")

    opcion = int(input("\n >>ELIGE UNA OPCION: "))
    while opcion <1 or opcion > 8:
        print(" Error..")
        opcion = int(input("\n >>ELIGE UNA OPCION: "))
    return opcion

#A. Analizar detenidamente el set de datos
print(type(lista_personajes))
print(type(lista_personajes[0]))

#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def mostrar_nombre_heroes():
    for x in lista_personajes:
        nombres = x['nombre']
        print(f" *Nombre de heroes: {nombres}")


#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def mostrar_nombre_altura():
    for x in lista_personajes:
        nombre = x['nombre']
        altura = x['altura']
        print(f"\n *Nombre de heroe: {nombre}, \n *Altura: {altura}")


#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def mortrar_heroe_max_alto():   
    flag_mas_alto = True

    for x in lista_personajes:
        if flag_mas_alto == True or float(x['altura']) > float(maxima_altura):
            maxima_altura = float(x['altura'])
            flag_mas_alto = False

    print(f"\n *Heroe con mayor alto: {maxima_altura}")
    for x in lista_personajes:
        if float(x['altura']) == float(maxima_altura):
            print(f" *Nombre de hero :{x['nombre']}")


#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def mostrar_heroe_min_altura():    
    flag_min_altura = True

    for x in lista_personajes:
        if flag_min_altura == True or float(x['altura']) < float(minima_altura):
            minima_altura = float(x['altura'])
            flag_min_altura = False

    print(f"\n *Heroe con menor altura: {minima_altura}")
    for x in lista_personajes:
        if float(x['altura']) == float(minima_altura):
            print(f" * Nombre de heroe: {x['nombre']}")


#F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def mostrar_promedio_altura():
    acumulador_altura = 0
    contador_altura = len(lista_personajes)

    for x in lista_personajes:
        acumulador_altura += float(x['altura'])

    promedio_altura = acumulador_altura / contador_altura
    print(f"\n *cantidad de alturas: {contador_altura}")
    print(f" *El promedio de las sltura es: {promedio_altura}")


#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
'''resuelto'''


#H. Calcular e informar cual es el superhéroe MAS y MENOS pesado.
def mostrar_heroe_mas_pesado():
    flag_mas_pesado = True

    for x in lista_personajes:
        if flag_mas_pesado == True or float(x['peso']) > float(maximo_peso):
            maximo_peso = float(x['peso'])
    
    print(f"\n *Maximo peso: {maximo_peso}")
    for x in lista_personajes:
        if float(x['peso']) == float(maximo_peso):
            print(f" *Nombre: {x['nombre']}")

def mostrar_heroe_menos_pesado():
    flag_min_peso = True

    for x in lista_personajes:
        if flag_min_peso == True or float(x['peso']) < float(minimo_peso):
            minimo_peso = float(x['peso'])
            flag_min_peso = False

    print(f"\n *Minimo peso: {minimo_peso}")
    for x in lista_personajes:
        if float(x['peso']) == float(minimo_peso):
            print(f" *Nombre: {x['nombre']}")

#I. Ordenar el código implementando una función para cada uno de los valores informados.
#J. Construir un menú que permita elegir qué dato obtener