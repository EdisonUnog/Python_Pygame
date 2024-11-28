import pygame
from pygame.locals import *
from Class_Colores import *
from GUI_form_prueba import *

pygame.init()

WIDTH = 1200
HEIGHT = 600
screen_size = (WIDTH, HEIGHT)
FPS = 60
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(screen_size)

form_prueba = FormPrueba(PANTALLA, 150, 125, 900, 350, Colores.GRIS, Colores.ROJO, 5, True)

run = True
while (run):
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False

    PANTALLA.fill(Colores.NEGRO)

    form_prueba.update(lista_eventos)

    
    
    pygame.display.flip()
pygame.quit()