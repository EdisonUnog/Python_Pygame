import pygame
from niveles.Class_Colores import* 
from niveles.configuraciones import *
import random

pygame.init()

class Monedas:
    def __init__(self, tamaño, lista: list, pos_inicial) -> None:
        #_confeccion de personaje
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #_animaciones
        self.monedas = lista
        self.reescalar_animaciones()

        #RECTANGULOS
        self.rectangulo = self.monedas[0].get_rect()
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        #movimiento_IMG
        self.indice_img = 0
        #_puntaje
        self.score = 0

    def reescalar_animaciones(self):
        for i in range(len(self.monedas)):
            self.monedas[i] = pygame.transform.scale(self.monedas[i], (self.ancho, self.alto))

    def girar_moneda(self, pantalla):
        pantalla.blit(self.monedas[self.indice_img], (self.rectangulo.x, self.rectangulo.y))
        self.indice_img = (self.indice_img + 1) % len(self.monedas)

    def update_moneda(self, pantalla, personaje, moneda): #collicion
        if personaje.lados["main"].colliderect(moneda.lados["main"]):
            self.score += 10
            self.desaparecer_moneda()
        self.puntaje(pantalla)

        self.girar_moneda(pantalla)
        
    def desaparecer_moneda(self):
        self.rectangulo.x = random.randrange(0,740,60)
        self.rectangulo.y = random.randrange(-1000,0,60)

    def puntaje(self, pantalla):
        fuente = pygame.font.SysFont("Arail", 25)
        cadena = "Puntos: " + str(self.score).zfill(5)
        texto = fuente.render(cadena, True, Colores.VERDE)
        texto_rect = texto.get_rect() #obtengo rectangulo para posiscionar el texto
        texto_rect.topleft = (5,5)
        pantalla.blit(texto, texto_rect)

        













lista_prueba = ["dell", "must", "zeta"]

for i in range(len(lista_prueba)):
    print(i)

# 0, 1, 2
