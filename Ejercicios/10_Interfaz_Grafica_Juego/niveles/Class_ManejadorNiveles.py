import pygame
from pygame.locals import*
from niveles.Class_Nivel_Uno import*
from niveles.Class_Nivel_Dos import*
from niveles.Class_Nivel_Tres import*

class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos":NivelDos,"nivel_tres":NivelTres}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
