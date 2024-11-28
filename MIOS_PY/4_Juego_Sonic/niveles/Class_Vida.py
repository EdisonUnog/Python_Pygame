import pygame 
from  niveles.Class_Colores import *

class Vida:
    def __init__(self, max_vida, pos_inicial:tuple):
        self.max_vida = max_vida
        self.vida_actual = max_vida

        self.pos_x = pos_inicial[0]
        self.pos_y = pos_inicial[1]

        self.ancho = 300
        self.alto = 30
        self.color_fondo = (50, 50, 50)
        self.color_vida = (0, 255, 0)
        self.vida_maxima = max_vida

    def actualizar_vida(self, danio=0):
        # Actualizar la vida según el daño recibido
        self.vida_actual -= danio
        if self.vida_actual < 0:
            self.vida_actual = 0

    def reiniciar_vida(self):
        if self.vida_actual == 0:
            self.max_vida = self.vida_maxima

    def draw(self, pantalla):
        # Dibujar la barra de fondo
        pygame.draw.rect(pantalla, self.color_fondo, (self.pos_x , self.pos_y , self.ancho, self.alto))

        #Dibujar la barra de vida actual
        porcentaje_vida = self.vida_actual / self.max_vida
        ancho_vida = int(self.ancho * porcentaje_vida)
        pygame.draw.rect(pantalla, self.color_vida, (self.pos_x , self.pos_y , ancho_vida, self.alto))
