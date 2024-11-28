import pygame
from pygame.locals import *
from Class_Colores import *

pygame.init()

WIDTH = 600
HEIGHT = 600
screen_size = (WIDTH, HEIGHT)
FPS = 60
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(screen_size)

img = pygame.image.load("Monedas/moneda3.png")
img = pygame.transform.scale(img, (30, 30))
rect = img.get_rect()




run = True
while (run):
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False

    PANTALLA.fill(Colores.NEGRO)

    #for i in img:
    pygame.transform.flip(img, True, False)

    PANTALLA.blit(img, rect)

    pygame.display.flip()

pygame.quit()

