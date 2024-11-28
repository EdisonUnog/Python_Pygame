import pygame, sys
from Class_Proyectil import*

class ListaProyectil:
    def __init__(self, pantalla, pos_xy, path_img, base) -> None:
        self.pos_xy = pos_xy
        self.surface = pantalla
        self.lista_balas = []
        self.tiempo_transcurrido = 0
        self.base = base
        self.path_img = path_img

    def generar_balas(self, velocidad, direccion, x, y, w, h):
        self.lista_balas.append(Proyectil(self.pos_xy.x + x, self.pos_xy.y + y, w, h,velocidad, direccion, self.path_img, self.base))

    def update(self, lista_objetivos):
        for proyectil in self.lista_balas:
            proyectil.update(lista_objetivos)
            proyectil.draw(self.surface)
            if(proyectil.impacto_objetivo):
                self.lista_balas.remove(proyectil)