
import pygame, sys
from niveles.constantes import*
from niveles.Class_Personaje import*
from niveles.Class_Piso import*
from niveles.Class_Plataforma import*
from niveles.Class_Monedas import*
from niveles.info_niveles import*


pygame.init()

PANTALLA = pygame.display.set_mode(scren_size)
reloj = pygame.time.Clock()

#juego = DataLevels(PANTALLA, "nivel_uno")
plataforma = Plataforma(300, 640, 200, 20, 4, 200, 700, 300, 1, 0)

run = True
while (run):

    delta= reloj.tick(FPS)
    eventos = pygame.event.get()
    kEYS = pygame.key.get_pressed()
    PANTALLA.fill(GRIS)

    for event in eventos:
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
        
    if kEYS[pygame.K_ESCAPE]:
        run = False
        
    plataforma.draw(PANTALLA)
    plataforma.update()
    #juego.update(delta)

    pygame.display.update()
pygame.quit()