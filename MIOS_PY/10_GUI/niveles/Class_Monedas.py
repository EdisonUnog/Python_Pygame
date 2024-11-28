import pygame, sys
from niveles.constantes import*
from niveles.Class_Auxiliar import*

class Monedas:
    def __init__(self, tamanio:tuple, pos_inicial:tuple) -> None:
        self.ancho = tamanio[0]
        self.alto = tamanio[1]
        self.collision = False
        
        #_animacion
        self.monedas = Auxiliar.cargarImagen("Recursos/Monedas/moneda{0}.png", 7, False, 1, self.ancho, self.alto)

        #_Rectangulos
        self.rectangulo = self.monedas[0].get_rect()
        self.rectangulo.x = pos_inicial[0] 
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)

        #_Movimiento
        self.indice_img = 0
    
    def girar_monedas(self, pantalla):
        pantalla.blit(self.monedas[self.indice_img], self.lados["main"])
        self.indice_img = (self.indice_img + 1) % len(self.monedas)

    def draw(self, pantalla):
        self.girar_monedas(pantalla)
