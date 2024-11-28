# cuando se choquen los rectangulos cambien de color, si colisionan 
#_2_pygame

import pygame, sys
from Class_Imagen import Imagen
from Class_Colores import Colores

pygame.init()

ANCHO = 800
ALTO = 600
FPS = 30

SIZE = (ANCHO, ALTO)

PANTALLA = pygame.display.set_mode(SIZE) #px
pygame.display.set_caption("miprimer juego")

imagen_vertical = Imagen((100,100), (ANCHO//2, ALTO//2), (Colores.VERDE, Colores.ROJO))
imagen_horizontal = Imagen((100,100), (ANCHO//2, ALTO//2), (Colores.AZUL_CLARO, Colores.BLANCO))

clock = pygame.time.Clock()

while True:

    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.fill(Colores.NEGRO)

    PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.imagen, imagen_horizontal.rectangulo)
    
    imagen_vertical.mover_imagen("Vertical", 10, (ANCHO, ALTO))
    imagen_horizontal.mover_imagen("Horizontal", 10, (ANCHO, ALTO))

    imagen_vertical.detectar_colision(imagen_horizontal)

    pygame.draw.line(PANTALLA, Colores.AZUL,(400,0),(400,800),1)
    pygame.draw.line(PANTALLA, Colores.AZUL,(0,300),(800,300),1)

    pygame.display.flip()

#blit -> pone una superficie arriba de la pantalla
#fill -> pintar

#mañana -> los dos rectangulos vuelvan aparecer