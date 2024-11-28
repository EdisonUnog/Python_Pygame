from data import lista_bzrp
from os import system

#A. Analizar detenidamente el set de datos con los alumnos
print(type(lista_bzrp))
print(type(lista_bzrp[0]))

#crear un menu
def menu_bzrp()->int: ## views -> vistas
    print("\n 1._Mostrar temas")
    print(" 2._Mostrar temas con views")
    print(" 3._Mostrar el maximo de views")
    print(" 4._mostrar el minimo de views")
    print(" 5._Promedio de views")
    print(" 6._salir")
    
    opcion = int(input("\n >>ELIGE UNA OPCION: "))
    while opcion <1 or opcion > 6:
        print(" Error")
        opcion = int(input("\n >>ELIGE UNA OPCION: "))
    return opcion

#B. Recorrer la lista imprimiendo por consola el título de cada video
def mostrar_lista_temas(lista:list):
    for x in lista:
        titulo = x['title']   
        print(f" *Titulo: {titulo}")


'''
for x in range(len(lista_bzrp)):
    print(f"\n Titulo: {lista_bzrp[x]['title']}")
'''
#C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
def mostrar_lista_temas_views():
    for x in lista_bzrp:
        titulo = x['title']
        views = x['views']
    print(f"\n *Titulo: {titulo}\n *Views: {views} \n ")

#D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)
def mostar_max_views():
    flag_maximo = True

    for x in lista_bzrp:
        if flag_maximo == True or x['views'] > maximo_views:
            maximo_views = x['views']
            flag_maximo = False

    print(f"\n *Cantidad maxima de reproducciones: {maximo_views}")
    for x in lista_bzrp:
        if x['views'] == maximo_views:
            print(f" Titulo: {x['title']}")

#E.Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones(MÍNIMO)
def mostrar_min_views():   
    flag_minimo = True

    for x in lista_bzrp:
        if flag_minimo == True or x['views'] < minimo_views:
            minimo_views = x['views']
            flag_minimo = False

    print(f"\n *Cantidad minima de reprodicciones: {minimo_views}")
    for x in lista_bzrp:
        if x['views'] == minimo_views:
            print(f" Titulo: {x['title']}")

#F. Recorrer la lista y determinar la cantidad total de reproducciones del canal(ACUMULADOR)
#G. Recorrer la lista y determinar la cantidad promedio de reproducciones que tiene un video (PROMEDIO)
def mostar_cantidad_promedio_views():
    acumulador_views = 0
    #contador_views = 0
    contador_views = len(lista_bzrp)

    for x in lista_bzrp:
        acumulador_views += x['views']
        #contador_views += 1

    promedio_views = acumulador_views / contador_views

    print(f"\n *total de reproducciones: {acumulador_views}")
    print(f" *Promedio de views: {promedio_views}")     



#H. Informar cual es el Título del vídeo asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO, ACUMULADOR y PROMEDIO)
 #estan en las arriba


#I. Calcular e informar cual es el video que más y el que menos dura.
 #en la lista es el dato 'leng' maximo y minimo

#J. Ordenar el código implementando una función para cada uno de los valores informados
'''resuelto'''

#K. Construir un menú que permita elegir qué dato obtener
'''resuelto'''

def mostrar_lista_temas(lista:list,clave=None,valor=None):
    if clave is None:
        for tema in lista:
            print(f"{tema['title']}")
    else:
        for tema in lista:
            if tema[clave] == valor:
                print(f"{tema['title']}")

def calcular_maximo(lista:list, clave:str)->int:
    '''
    Brief: Calcula el maximo calor numerico en base a una clave
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        clave: str -> la clave con la cual realizo la busqueda en la lista
    return: un entero que representa el maximo valor de la clave
    '''
    flag_primero = True
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0):
        for tema in lista:
            if flag_primero == True or tema[clave] > maximo:
                maximo = tema[clave]
                flag_primero = False
    return maximo

def buscar_temas_mas_largo(lista:list):
    maximo_len = calcular_maximo(lista,'length')
    print(f" Duracion maxima: {maximo_len}")
    mostrar_lista_temas(lista,'length',maximo_len)


def calcular_minimo(lista:list, clave:str)->int:
    flag_primero = True
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0):
        for tema in lista:
            if flag_primero == True or tema[clave] < maximo:
                maximo = tema[clave]
                flag_primero = False
    return maximo