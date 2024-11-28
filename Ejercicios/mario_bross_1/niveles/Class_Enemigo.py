import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_Colores import* 
from niveles.configuraciones import *
import random


pygame.init()

class Enemigo:
    def __init__(self, tamaño, lista: dict, pos_inicial, velocidad) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #_animaciones
        self.enemigo = lista
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

        #sonido enemigo
        self.sound_enemigo = pygame.mixer.Sound("sonidos/soundEnemigo.wav")

        
        

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

    def update(self, pantalla): ###
        match self.direccion:
            case "derecha":
                self.animar_enemigo(pantalla, "derecha")
                self.mover(self.velocidad)

            case "izquierda":
                self.animar_enemigo(pantalla, "izquierda")
                self.mover(self.velocidad * -1)

        #self.collicion_enemigo(personaje, lista_enemigo)

    def collicion_enemigo(self, personaje, lista_enemigo):
        for enemigo in lista_enemigo:
            if personaje.lados["bottom"].colliderect(enemigo.lados["top"]):
                self.desaparecer_tortuga(enemigo)
                self.sound_enemigo.play()
                personaje.score += 100
            
                
    def pierde(self, personaje, lista_enemigo, pos_inicial:tuple):
        for enemigo in lista_enemigo:
            if personaje.lados["right"].colliderect(enemigo.lados["left"]):
                print("colli")
                self.desaparecer_tortuga(enemigo)
                personaje.sound_inicio.play()
                personaje.rectangulo.x= pos_inicial[0] 
                personaje.rectangulo.y= pos_inicial[1]
                personaje.vidas -= 1
                

    def desaparecer_tortuga(self, enemigo):
        enemigo.rectangulo.x = random.randrange(0,740,60)
        enemigo.rectangulo.y = random.randrange(-1000,0,60)
        enemigo.lados["main"].x = random.randrange(0,740,60)
        enemigo.lados["main"].y = random.randrange(-1000,0,60)
        

        #ANCHO = pantalla.get_width()
        #ALTO = pantalla.get_height()
        

