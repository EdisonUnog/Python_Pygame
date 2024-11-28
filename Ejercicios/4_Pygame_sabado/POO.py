#__pygame

import pygame, sys
from Class_Paleta import Paleta, Pelota
from Class_Colores import Colores

pygame.init() #inciamos pygame

ANCHO = 1200
ALTO = 600
FPS = 30
FPS_P = 10
screen_size = (ANCHO, ALTO)# pixeles
#creamos una ventana
PANTALLA = pygame.display.set_mode(screen_size)# pixeles
# titulo de la ventana
pygame.display.set_caption("Mi primer juego...")

rectangulo_uno = Paleta((30, ALTO//2), (25, 150), 5, Colores.BLANCO)
rectangulo_dos = Paleta((ANCHO - 30 , ALTO//2), (25, 150), -5, Colores.BLANCO)

rectangulos = [rectangulo_uno, rectangulo_dos]

pelota = Pelota((25,25), FPS_P, Colores.ROJO, (ANCHO, ALTO))

reloj = pygame.time.Clock()

while True:
    reloj.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    PANTALLA.fill(Colores.NEGRO)

    rectangulo_uno.update(PANTALLA)
    rectangulo_dos.update(PANTALLA)
    #rectangulo_uno.mover_y(ALTO)
    #rectangulo_dos.mover_y(ALTO)
    rectangulo_dos.verificar_collicion(rectangulo_uno)

    pelota.update(PANTALLA, rectangulos)

    pygame.display.flip() ##actualiza todas las supercifies

