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
        #sonido
        self.sound_moneda = pygame.mixer.Sound("sonidos/soundMoneda.wav")

    def reescalar_animaciones(self):
        for i in range(len(self.monedas)):
            self.monedas[i] = pygame.transform.scale(self.monedas[i], (self.ancho, self.alto))

    def girar_moneda(self, pantalla):
        pantalla.blit(self.monedas[self.indice_img], (self.rectangulo.x, self.rectangulo.y))
        self.indice_img = (self.indice_img + 1) % len(self.monedas)


    def draw(self, pantalla, personaje, lista_monedas):
        for moneda in lista_monedas:
            if personaje.lados["main"].colliderect(moneda.lados["main"]):
                lista_monedas.remove(moneda)
                self.sound_moneda.play()
                personaje.score += 10
                personaje.contador_monedas += 1
                
        self.girar_moneda(pantalla)

