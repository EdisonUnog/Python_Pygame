import pygame
import json
from Niveles.constantes import*

def cargar_json_data(path:str):
    with open(path, "r") as file:
        lista = json.load(file)
    return lista["levels"]