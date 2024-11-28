import pygame, sys

pygame.init()

width = 500
height = 400
size = (width, height)

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

PANTALLA = pygame.display.set_mode(size) #px
pygame.display.set_caption("miprimer juego")
PANTALLA.fill(ROJO)


poligono= pygame.draw.polygon(PANTALLA, VERDE, ((146,0), (291,106), (236,277), (26, 277), (0,106)))
rectangulo = pygame.draw.rect(PANTALLA, AZUL, (100,50,100,50)) #posicion y ancho
rectangulo = pygame.draw.rect(PANTALLA, AZUL, (250,100,25,100))

lineas = pygame.draw.line(PANTALLA, BLANCO, (100,105),(199,20),3)

circulo = pygame.draw.circle(PANTALLA, NEGRO, (120,300), 50, 1)

elipse = pygame.draw.ellipse(PANTALLA, BLANCO, (270, 105, 80, 80), 5)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()