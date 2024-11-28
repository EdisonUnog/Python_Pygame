import pygame, sys
from configuraciones import*
import random

pygame.init()

def crear_bala(ancho,alto):
    imagen_bala = pygame.image.load("laser.png")
    imagen_bala = pygame.transform.scale(imagen_bala,(ancho,alto))
    rect_bala = imagen_bala.get_rect()
    dict_bala = {}
    dict_bala["surface"] = imagen_bala
    dict_bala["rect"] = rect_bala
    dict_bala["visible"] = True
    dict_bala["speed"] = random.randrange (10, 20, 1)
    dict_bala["trayectoria"] = [0, 0]
    return dict_bala

def crear_lista_balas(pos_player):
    lista_bala = []
    for i in range(15):
        lista_bala.append(crear_bala(10, 10))
    return lista_bala

def calcular_trayectoria(bala, player):
    x, y = pygame.mouse.get_pos()
    rx = (x-player["rect"][0]) / 100
    ry = (y-player["rect"][1]) / 100
    bala["trayectoria"] = [rx, ry]
    bala["rect"][0] = player["rect"][0] + 50
    bala["rect"][1] = player["rect"][1] + 50
    return bala

def update(lista_balas_visibles, ventana_principal):
    for bala in lista_balas_visibles:
        bala["rect"][0] = bala["rect"][0] + bala["trayectoria"][0]
        bala["rect"][1] = bala["rect"][1] + bala["trayectoria"][1]
        bala["rect"][0] = bala["rect"][0] + (bala["trayectoria"][0] * 3)
        bala["rect"][1] = bala["rect"][1] + (bala["trayectoria"][1] * 3)
        ventana_principal.blit(bala["surface"], (bala["rect"][0], bala["rect"][1]))
