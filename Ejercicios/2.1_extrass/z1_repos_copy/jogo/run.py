import pygame
import player
import block
import niveles_data
import nivel

ANCHO_VENTANA = 1000
ALTO_VENTANA = 650

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("JOGO PRUEBA")


# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

map_to_draw = niveles_data.lvl1
level_1= nivel.Mapa
level_1.constructor(map_to_draw)


player_1 = player.Personaje(200,300,0.69)

flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

    lista_teclas = pygame.key.get_pressed()
    
    if lista_teclas[pygame.K_LEFT] :    
        player_1.update("x","left")
    if lista_teclas[pygame.K_RIGHT] :
        player_1.update("x","right")
    if lista_teclas[pygame.K_UP] :
        player_1.update("y","up")
    if lista_teclas[pygame.K_DOWN] :
       player_1.update("y","down")


    screen.fill((0,0,0))
    level_1.draw_map(screen)
    player_1.draw(screen)
    pygame.display.flip()
pygame.quit()