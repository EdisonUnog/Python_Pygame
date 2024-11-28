import pygame, sys
from Class_Personaje import*
from Constantes import*
from Class_Piso import*
from Class_Plataforma import*
from modo import*

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(scren_size)

#_fondo_pantall
fondo = pygame.image.load("Recursos/Fondos/fondo_space.png")
fondo = pygame.transform.scale(fondo, scren_size)

#_Player y Piso
player = Personaje(PANTALLA, (60, 80), (350, ALTO - 180), 10)


lista_Pisos = []
lista_Pisos.append(Pisos((ANCHO, 25), 3, (0,0))) 
lista_Pisos.append(Pisos((ANCHO, 50), 2, (0, ALTO - 50)))
lista_Pisos.append(Pisos((20, 725), 0, (0, 25)))           
lista_Pisos.append(Pisos((20, 725), 0, (ANCHO - 20, 25)))

lista_plataformas = []
lista_plataformas.append(Plataforma(300, 640, 200, 20, 5, 10, 200, 700, 5, 1, 300, 0))
lista_plataformas.append(Plataforma(700, 640, 200, 20, 5, 10, 300, 1000, 5, 2, 400, 1))
lista_plataformas.append(Plataforma(700, 600, 100, 20, 5, 10, 400, 900, 0, 2, 0, 2))
lista_plataformas.append(Plataforma(520, 450, 100, 20, 0, 10, 0, 0, 0, 3, 0, None))

#_Musica_fondo
pygame.mixer.music.load("Recursos/music/Vengeance.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

while True:

    delta = RELOJ.tick(FPS)
    PANTALLA.blit(fondo, (0,0))

    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    for piso in lista_Pisos:
        piso.draw(PANTALLA)

    
    for plataforma in lista_plataformas:
        plataforma.update(delta)
        plataforma.draw(PANTALLA)

    player.update(PANTALLA, lista_Pisos, lista_plataformas)



    if get_mode(): # dibuja rect piso y rect personaje
        for pisos in lista_Pisos:
            for lado in pisos.lados:
                pygame.draw.rect(PANTALLA, NEGRO, pisos.lados["main"], 3)
                pygame.draw.rect(PANTALLA, ROJO, pisos.lados["top"], 2)
                pygame.draw.rect(PANTALLA, ROJO, pisos.lados["bottom"], 2)
                pygame.draw.rect(PANTALLA, ROJO, pisos.lados["right"], 2)
                pygame.draw.rect(PANTALLA, ROJO, pisos.lados["left"], 2)

        for plataformas in lista_plataformas:
            for lado in plataformas.lados:
                pygame.draw.rect(PANTALLA, VERDE, plataformas.lados[lado], 2)

        for lado in player.lados:
            # pygame.draw.rect(PANTALLA, NEGRO, player.lados[lado], 2)
            pygame.draw.rect(PANTALLA, NEGRO, player.lados["main"], 3)
            pygame.draw.rect(PANTALLA, BLANCO, player.lados["top"], 2)
            pygame.draw.rect(PANTALLA, BLANCO, player.lados["bottom"], 2)
            pygame.draw.rect(PANTALLA, BLANCO, player.lados["right"], 2)
            pygame.draw.rect(PANTALLA, BLANCO, player.lados["left"], 2)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()

