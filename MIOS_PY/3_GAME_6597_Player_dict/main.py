import pygame
from Class_Player_Dict import*
from Class_Plataformas import*
from Class_Colores import*
from matriz_mundo_1 import*

pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60
ANCHO = 1600
ALTO = 900
screen_size = (ANCHO, ALTO)

long_lineas = 20
long_columnas = 35.55555556

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption('personaje desde un dict')
#_Icono
icono = pygame.image.load("Recursos/icon.png")
pygame.display.set_icon(icono)

#dibujamos el mundo
player = Player(40, ALTO - 80, 32, 45, diccionario_personaje, 5, ALTO)
mundo = Mundo(world_data, long_lineas, long_columnas)

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

    PANTALLA.fill(Colores.NEGRO)

    mundo.draw(PANTALLA)
    player.update(PANTALLA, mundo, player)

    #draw_lineas(PANTALLA, long_lineas, long_columnas, ANCHO, ALTO)



    pygame.display.update()
pygame.quit()
