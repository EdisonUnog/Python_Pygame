import pygame
from pygame.locals import*
from niveles.Class_Nivel_Uno import*
from niveles.Class_Colores import*

class Manejador_Niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno" : NivelUno}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)