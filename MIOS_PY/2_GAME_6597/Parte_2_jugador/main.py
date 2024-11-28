import pygame, sys
from pygame.locals import*
from matriz_mundo_1 import*
from Class_Jugador import*
from mundo import*
from Class_Colores import*

pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60
ANCHO = 1600
ALTO = 900
screen_size = (ANCHO, ALTO)

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption('mundo matriz')

long_lineas = 20
long_alto = 35.55555556

#fondo = pygame.image.load('img/fondo.png')
#fondo = pygame.transform.scale(fondo, screen_size)

def draw_lineas():
    for line in range(0, 45):
        pygame.draw.line(PANTALLA, Colores.NEGRO, (0, line * long_lineas), (ANCHO, line * long_lineas)) #lineas horizontales
        pygame.draw.line(PANTALLA, Colores.NEGRO, (line * long_alto, 0), (line * long_alto, ALTO))

player = Player(215, ALTO - 42, 32, 45, ANCHO, ALTO)
mundo = Mundo(world_data, long_lineas, long_alto)

run = True
while (run):
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        
    PANTALLA.fill(Colores.GRIS)

    mundo.draw(PANTALLA)
    #draw_lineas()

    player.update(PANTALLA, mundo)



    pygame.display.update()
pygame.quit()