import csv
import json
from clase05 import funct_imprimir_dato
import re

def funct_imprimir_menu_desafio_5():
    funct_imprimir_dato("\n{0}\n \nA) Imprimir los nombres de héroes género M.\n"
                            "B) Imprimir los nombres de héroes género F.\n"
                            "C) Héroe género M más alto.\nD) Héroe género F más alto.\n"
                            "E) Héroe género M más bajo.\nF) Héroe género F más bajo.\n"
                            "G) Altura promedio de género M.\nH) Altura promedio de género F."
                            "I) Nombre de los héroes de los items anteriores.\n"
                            "J) Cantidad de superhéroes con cada color de ojos.\n"
                            "K) Cantidad de superhéroes con cada color de pelo.\n"
                            "L) Cantidad de superhéroes con cada tipo de inteligencia.\n"
                            "M) Lista de superhéroes por cada color de ojos.\n"
                            "N) Lista de superhéroes por cada color de pelo.\n"
                            "O) Lista de superhéroes por cada tipo de inteligencia.\n"
                            "P) Para terminar el programa.".format("MENÚ".center(50,"-")))

def funct_stark_menu_principal_desafio_5()->str:
    funct_imprimir_menu_desafio_5()
    entrada = input("Ingrese una letra de las opciones para continuar.")
    entrada = entrada.upper()

    if re.search("[A-P]",entrada):
        return entrada
    else :
        return -1
    
def funct_stark_marvel_app_5(lista:list):
    entrada = funct_stark_menu_principal_desafio_5()

    if entrada == "A":
        pass
    elif entrada == "B":
        pass
    elif entrada == "C":
        pass
    elif entrada == "D":
        pass
    elif entrada == "E":
        pass
    elif entrada == "F":
        pass
    elif entrada == "G":
        pass
    elif entrada == "H":
        pass
    elif entrada == "I":
        pass
    elif entrada == "J":
        pass
    elif entrada == "K":
        pass
    elif entrada == "L":
        pass
    elif entrada == "M":
        pass
    elif entrada == "N":
        pass
    elif entrada == "O":
        pass
    elif entrada == "P":
        pass
    
    pass

def leer_archivo(archive:str)->list:

    with open(archive,"r") as archivo:
        data = json.load(archivo)
        data = list[dict](data["heroes"])
        return data

def guardar_archivo(nombre_archivo:str,contenido:str):

    if len(contenido) > 0 :
        with open(nombre_archivo+".csv","w") as archivo:
            archivo.write(contenido)
        print("Se creó el archivo {0}".format(nombre_archivo))
        return True
    else :
        return False