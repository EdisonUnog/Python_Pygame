
import pygame, sys
from pygame.locals import *

pygame.init()
screen_size = (1000,500)
PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("HOMEROLAND")

icono = pygame.image.load("Recursos/icono_homero.png")

#FONDO
fondo = pygame.image.load("Recursos/fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo, (0,0))

#MUSICA
pygame.mixer.music.load("Recursos/intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

pygame.display.set_icon(icono)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()