import pygame
from niveles.Configuraciones import*

class Pisos:
    def __init__(self, tamanio:tuple, i, pos_inicial:tuple) -> None:

        self.ancho = tamanio[0]
        self.alto = tamanio[1]

        self.piso = pisos_img
        
        self.img_piso = self.piso[i]
        self.img_piso = pygame.transform.scale(self.img_piso, (self.ancho, self.alto))

        self.rectangulo = self.img_piso.get_rect() #obtengo rect de la imagen
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo) #dibujo lados al rect

    def draw(self, pantalla): #dibujo piso
        pantalla.blit(self.img_piso, self.lados["main"])