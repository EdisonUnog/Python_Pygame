import pygame
from Class_Colores import Colores

ANCHO = 800
ALTO = 500
screen_size = (ANCHO,ALTO)

pygame.init()

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Primeri Juego")

fuente = pygame.font.SysFont("Arail", 60)
texto = fuente.render("Game Over", False, Colores.VERDE, Colores.AZUL_CLARO)

flag = True 

while flag:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False
    PANTALLA.fill(Colores.BLANCO)
    PANTALLA.blit(texto, (300,200))

    pygame.display.update()
pygame.quit()