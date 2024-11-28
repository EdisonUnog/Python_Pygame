import re
import json
import random
import datetime

def imprimir_dato(dato:str):
    print(f"{dato}")


def generar_codigo_personaje(personaje):

    '''
    Brief: genera codigos para los personajes
    Parametro: personaje
    Return: codigo

    '''

    nombre = str(personaje['nombre'])
    raza = str(personaje['raza'])
    poder_de_ataque = int(personaje['poder_de_pelea'])
    poder_de_pelea = int(personaje['poder_de_pelea'])
    id_personaje = int(personaje['id'])

    if poder_de_ataque > poder_de_pelea:
        ganador = 'A'
        valor_mas_alto = poder_de_ataque
    elif poder_de_pelea > poder_de_ataque:
        ganador = 'P'
        valor_mas_alto = poder_de_pelea
    else:
        ganador = 'AP'
        valor_mas_alto = poder_de_ataque

    codigo = f"{nombre[0]}-{ganador}-{valor_mas_alto}-{str(id_personaje).zfill(9)}"
    return codigo



def agregar_codigos_personajes(lista_personajes):

    '''
    Brief: agrega los codigos a la lista
    Parametro: lista_personajes
    Return: return lista_personajes

    '''

    for p in lista_personajes:
        p['codigo'] = generar_codigo_personaje(p)
    return lista_personajes

'''personajes_actualizados = agregar_codigos_personajes(lista_dbz)
                    for personaje in personajes_actualizados:
                        print(personaje)'''