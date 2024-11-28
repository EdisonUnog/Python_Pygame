import pygame
from Class_Colores import*
from configuraciones import*

class Mundo():
    def __init__(self, data, long_lineas, long_alto) -> None:
        
        self.column = long_alto #x
        self.lineas = long_lineas #y

        self.bloque_lista = []

        bloque_1 = pygame.image.load('Recursos/plataformas/1.png')
        bloque_2 = pygame.image.load('Recursos/plataformas/2.png')
        bloque_3 = pygame.image.load('Recursos/plataformas/3.png')

        cont_linea = 0

        for fila in data:
            cont_col = 0
            for num_bloque in fila:

                if num_bloque == 1:
                    img = pygame.transform.scale(bloque_1, (self.column, self.lineas))
                    img_rect = img.get_rect()
                    img_rect.x = cont_col * self.column
                    img_rect.y = cont_linea * self.lineas
                    lados = obtener_rectangulo(img_rect)
                    bloque = (img, img_rect)
                    self.bloque_lista.append(bloque)

                if num_bloque == 2:
                    img = pygame.transform.scale(bloque_2, (self.column, self.lineas))
                    img_rect = img.get_rect()
                    img_rect.x = cont_col * self.column
                    img_rect.y = cont_linea * self.lineas
                    lados = obtener_rectangulo(img_rect)
                    bloque = (img, img_rect)
                    self.bloque_lista.append(bloque)
                    
                if num_bloque == 3:
                    img = pygame.transform.scale(bloque_3, (self.column, self.lineas))
                    img_rect = img.get_rect()
                    img_rect.x = cont_col * self.column
                    img_rect.y = cont_linea * self.lineas
                    lados = obtener_rectangulo(img_rect)
                    bloque = (img, img_rect)
                    self.bloque_lista.append(bloque)
                
                cont_col += 1
            cont_linea += 1

    def draw(self, pantalla):
        for bloque in self.bloque_lista:
            pantalla.blit(bloque[0], bloque[1])

#######################################################################################
# LINEAS QUE DIVIDEN LA PANTALLA

def draw_lineas(pantalla, long_lineas, long_columnas, ancho, alto):
    for line in range(0, 45):
        pygame.draw.line(pantalla, Colores.GRIS, (0, line * long_lineas), (ancho, line * long_lineas))
        pygame.draw.line(pantalla, Colores.GRIS, (line * long_columnas, 0), (line * long_columnas, alto))