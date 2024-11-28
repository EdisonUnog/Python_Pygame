import pygame
from Class_Colores import * 
from pygame.locals import *
import unicodedata

#_Parametriza.
#_poscicionar el control, despues darle dimenciones y colores

class Widget:
    def __init__(self, screen, x, y, w, h, color_background = Colores.NEGRO, color_border = Colores.ROJO,border_size = -1) -> None:
        self._master = screen
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._color_background = color_background
        self._color_border = color_border
        self._slave = None
        self.slave_rect = None
        self.border_size = border_size

    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        self._master.blit(self._slave, self.slave_rect)
        pygame.draw.rect(self._master, self._color_border, self.slave_rect, self.border_size)
