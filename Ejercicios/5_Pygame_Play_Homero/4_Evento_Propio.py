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

timer_event = pygame.USEREVENT + 0
pygame.time.set_timer(timer_event, 1000) #dispara un evento cada cierto tiempo

flag = True 
while flag:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN: #preciono el boton del mouse
            print(event.pos)

        if event.type == timer_event:
            print("disparo")


    #PANTALLA.blit(texto, (100,200))

    pygame.display.update()
pygame.quit()