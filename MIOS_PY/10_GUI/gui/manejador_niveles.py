import pygame
from gui.Gui_Nivel_Uno import*
from gui.Gui_Nivel_Dos import*
from gui.Gui_Nivel_Tres import*
from niveles.constantes import*


class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno" : LevelUno, "nivel_dos" : LevelDos, "nivel_tres" : LevelTres}

    def get_nivel(self, nombre_nivel):
        # (self, screen, x, y, w, h, color_background, color_border, border_size=-1, active=True)
        return self.niveles[nombre_nivel](self._slave, 0, 0, ANCHO, ALTO, None, ROJO, True)