import pygame
import random
from Class_Colores import Colores

ANCHO = 800
ALTO = 800
FPS = 30
screen_size = (ANCHO,ALTO)

pygame.init()

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Primeri Juego")

#fuente = pygame.font.SysFont("Arail", 60)
#texto = fuente.render("hola estudiantes de 1D", False, Colores.VERDE, Colores.AZUL_CLARO)

#_creo posiciones aleatorias
circulos = []
for i in range(500):
    x = random.randint(1, ANCHO - 1)
    y = random.randint(1, ALTO - 1)
    circulos.append([x, y])

relog = pygame.time.Clock()

flag = True 
while flag:
    relog.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False

    PANTALLA.fill(Colores.NEGRO)
    #PANTALLA.blit(texto, (100,200))

    for c in circulos:
        c[0] += 1
        c[1] += 2
        if c[0] > ANCHO:
            c[0] = 0
        if c[1] > ALTO:
            c[1] = 0
    for c in circulos:
        pygame.draw.circle(PANTALLA, Colores.ROJO, (c[0], c[1]), 5, 10)

    pygame.display.update()
pygame.quit()