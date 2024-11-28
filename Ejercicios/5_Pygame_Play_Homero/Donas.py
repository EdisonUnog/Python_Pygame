import pygame
import random
from Class_Colores import Colores

def crear_dona(x, y, ancho, alto, path):
    imagen_dona = pygame.image.load(path)
    imagen_dona = pygame.transform.scale(imagen_dona, (ancho, alto))
    rectangulo = imagen_dona.get_rect()
    rectangulo.x = x
    rectangulo.y = y

    dict_dona = {}
    dict_dona["superficie"] = imagen_dona
    dict_dona["rectangulo"] = rectangulo
    dict_dona["velocidad"] = random.randrange(8,15,1)

    return dict_dona

def crear_lista_donas(cantidad):
    lista = []
    for i in range(cantidad):
        x = random.randrange(0, 740, 60)
        y = random.randrange(-1000,0, 60)
        diccionario = crear_dona(x, y, 60, 60, "Recursos/dona.png")
        lista.append(diccionario)

    return lista

def update_donas(lista_donas):
    for dona in lista_donas:
        rect = dona["rectangulo"]
        rect.y += dona["velocidad"]

def verificar_collicion(lista_donas, personaje):
    for dona in lista_donas:
        #rectangulo = pygame.Rect(personaje["rectangulo"])
        if personaje["boca"].colliderect(dona["rectangulo"]):
            personaje["score"] += 10
            desaparecer_dona(dona)
        if dona["rectangulo"].y > 720:
            desaparecer_dona(dona)


def desaparecer_dona(dona):
    dona["rectangulo"].x = random.randrange(0,740,60)
    dona["rectangulo"].y = random.randrange(-1000,0,60)
