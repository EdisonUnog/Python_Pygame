import pygame
from configuraciones import *

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Plataforma:
    def __init__(self, tamaño, plataforma, pos_inicial) -> None:

        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.plataforma = plataforma
        self.plataforma = pygame.transform.scale(self.plataforma, (self.ancho, self. alto))

        self.rectangulo = self.plataforma.get_rect() #rectangulo de la imagen
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)

    def update_plataformas(self, pantalla):
        pantalla.blit(self.plataforma, self.lados["main"])
        '''for i in range(len(mis_plataformas)):
            pantalla.blit(mis_plataformas[i].plataforma, mis_plataformas[i].rectangulo)'''


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Bandera:
    def __init__(self, tamaño, bandera, pos_inicial) -> None:

        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.bandera = bandera
        self.bandera = pygame.transform.scale(self.bandera, (self.ancho, self. alto))

        self.rectangulo = self.bandera.get_rect() #rectangulo de la imagen
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)

    '''def update_bandera(self, pantalla):
        pantalla.blit(self.bandera, self.rectangulo)'''