# cuando se choquen los rectangulos cambien de color, si colisionan 

import pygame, sys

pygame.init()

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 800
ALTO = 600
FPS = 30

SIZE = (ANCHO, ALTO)

PANTALLA = pygame.display.set_mode(SIZE) #px
pygame.display.set_caption("miprimer juego")

#PANTALLA.fill(ROJO)

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)

rectangulo_vertical = imagen_vertical.get_rect() #que me de un rectangulo
rectangulo_vertical.center= (ANCHO//2 , ALTO//2) #ubicar el rectandulo en un lugar de la pantalla


imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL_CLARO)

rectangulo_horizontal = imagen_vertical.get_rect() #que me de un rectangulo
rectangulo_horizontal.center= (ANCHO//2 , ALTO//2) #ubicar el rectandulo en un lugar de la pantalla

clock = pygame.time.Clock()

while True:

    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.fill(NEGRO)

    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0

    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)
    rectangulo_horizontal.x += 10
    if rectangulo_horizontal.left > ANCHO:
        rectangulo_horizontal.right = 0

    if rectangulo_vertical.colliderect(rectangulo_horizontal):# sise chocan los rectangulos
        imagen_horizontal.fill(ROJO)
        imagen_vertical.fill(BLANCO)
    else:
        imagen_vertical.fill(AZUL_CLARO)
        imagen_horizontal.fill(VERDE)

    pygame.draw.line(PANTALLA, AZUL,(400,0),(400,800),1)
    pygame.draw.line(PANTALLA, AZUL,(0,300),(800,300),1)

    pygame.display.flip()

#blit -> pone una superficie arriba de la pantalla
#fill -> pintar

#mañana -> los dos rectangulos vuelvan aparecer