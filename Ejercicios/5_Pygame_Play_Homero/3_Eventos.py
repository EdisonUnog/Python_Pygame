import pygame
from Class_Colores import Colores

ANCHO = 800
ALTO = 800
screen_size = (ANCHO,ALTO)

pygame.init()

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Primeri Juego")

#fuente = pygame.font.SysFont("Arail", 60)
#texto = fuente.render("hola estudiantes de 1D", False, Colores.VERDE, Colores.AZUL_CLARO)

flag = True 

while flag:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN: #preciono el boton del mouse
            print(event.pos)

        if event.type == pygame.MOUSEMOTION: #registra el movimiento del cursor
            print(event.pos)

    lista_teclas = pygame.key.get_pressed() #capturar la tecla que se preciona
    if lista_teclas[pygame.K_0]:
        print("0")
    if lista_teclas[pygame.K_LEFT]:
        print("izquierda")
    if lista_teclas[pygame.K_RIGHT]:
        print("derecha")
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    #PANTALLA.blit(texto, (100,200))

    pygame.display.update()
pygame.quit()