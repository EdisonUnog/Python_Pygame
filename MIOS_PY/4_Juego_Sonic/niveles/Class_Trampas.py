import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_Colores import* 
from niveles.Configuraciones import *
import random

pygame.init()

class Trampas:
    def __init__(self, tamaño, pos_inicial, velocidad, izquierda, derecha) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #_animaciones
        self.enemigo = diccionario_cierra
        self.reescalar_animaciones()
        self.direccion = "derecha"

        #RECTANGULOS
        self.rectangulo = self.enemigo["derecha"][0].get_rect()
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        #movimiento_IMG
        self.movimiento = 0
        self.velocidad = velocidad

        self.izquierda = izquierda
        self.derecha = derecha


    def reescalar_animaciones(self):
        for clave in self.enemigo:
            reescalar_imagenes(self.enemigo[clave], (self.ancho, self.alto))

    def animar_enemigo(self, pantalla, direccion):
        animar = self.enemigo[direccion]
        largo = len(animar)

        if self.movimiento >= largo:
            self.movimiento = 0

        pantalla.blit(animar[self.movimiento], self.lados["main"])
        self.movimiento += 1
        
    def mover(self, velocidad):
        for lado in self.lados: 
            self.lados[lado].x += velocidad

    def draw(self, pantalla): ###
        match self.direccion:
            case "derecha":
                self.animar_enemigo(pantalla, "derecha")
                self.mover(self.velocidad)

            case "izquierda":
                self.animar_enemigo(pantalla, "izquierda")
                self.mover(self.velocidad * -1)

    def mover_x(self, ancho):        
        if self.rectangulo.x >= ancho - self.derecha:
            self.direccion = "izquierda"
        elif self.rectangulo.x <= ancho - self.izquierda:
            self.direccion = "derecha"
            