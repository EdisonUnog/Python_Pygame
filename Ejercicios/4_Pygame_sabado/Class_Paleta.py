import pygame
import pygame.locals 
from Class_Colores import Colores

class Paleta:
    def __init__(self, pos_inicial, tamaño, velocidad, color) -> None:
        self.surface = pygame.Surface(tamaño)
        self.surface.fill(color)
        self.rectangulo = self.surface.get_rect()
        self.rectangulo.center = pos_inicial
        self.velocidad = velocidad

    def mover_y(self, alto_pantalla):
        self.rectangulo.y += self.velocidad

        if self.rectangulo.top > alto_pantalla:
            self.rectangulo.bottom = 0
        elif self.rectangulo.bottom < 0:
                self.rectangulo.top = alto_pantalla 

    def verificar_collicion(self, otra_paleta):
        if self.rectangulo.colliderect(otra_paleta.rectangulo):
            self.surface.fill(Colores.VERDE)
            otra_paleta.surface.fill(Colores.ROJO)

    def draw(self, pantalla):
        pantalla.blit(self.surface, self.rectangulo)

    def update(self, pantalla):
        #self.mover_y(pantalla.get_height())
        self.draw(pantalla)

#---------------------------------------------------------------------------------
class Pelota:
    def __init__(self, tamaño, velocidad, color, tamaño_pantalla) -> None:
        self.surface = pygame.Surface(tamaño)
        self.surface.fill(color)
        self.pos_inicial = (tamaño_pantalla[0]//2 , tamaño_pantalla[1]//2)
        self.rectangulo = self.surface.get_rect()
        self.rectangulo.center = self.pos_inicial
        self.velocidad = velocidad
        self.orientacion_x = 1

    def mover_x(self, alto_pantalla):
        self.rectangulo.x += self.velocidad * self.orientacion_x
        if(self.rectangulo.left > alto_pantalla or self.rectangulo.right < 0):
            self.rectangulo.center = self.pos_inicial

    def verificar_collicion(self, paletas):
        for paleta in paletas:
            if self.rectangulo.colliderect(paleta.rectangulo):
                self.orientacion_x = self.orientacion_x * -1
                #self.velocidad += 2 #incrementa velocidad

    def draw(self, pantalla):
        pantalla.blit(self.surface, self.rectangulo)

    def update(self, pantalla: pygame.Surface, paletas):
        #self.mover_y(pantalla.get_height())    
        self.mover_x(pantalla.get_width())
        self.verificar_collicion(paletas)
        self.draw(pantalla)

