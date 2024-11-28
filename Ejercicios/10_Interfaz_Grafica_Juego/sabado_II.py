import pygame, sys
from GUI_Form_Principal import*

ANCHO = 1500
ALTO = 800
scren_size = (ANCHO, ALTO) 
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(scren_size)
form_principal = FormPrincipal(PANTALLA, 300, 225, 900, 350, AQUA, BLANCO, 5, True)


while True:
    RELOJ.tick(FPS)
    PANTALLA.fill(GRIS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    form_principal.update(eventos)


    pygame.display.update() # actualiza mi pantalla
pygame.quit()
