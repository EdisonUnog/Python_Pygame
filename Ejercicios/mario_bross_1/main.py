import pygame, sys
from gui.GUI_Form_Principal import*

from niveles.Class_Nivel_Uno import*
from niveles.nivel import*

from niveles.Class_Enemigo import*
from niveles.diccionario import*

ANCHO = 1700
ALTO = 900
scren_size = (ANCHO, ALTO)
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(scren_size)

form_principal = FormPrincipal(PANTALLA, 410, 250, 900, 350, Colores.GRIS, Colores.BLANCO, 5, True)
#actual = NivelTres(PANTALLA)

#enemigo = Enemigo((50, 50), diccionario_enemigo, (1000, 740), 5)

while True:
    RELOJ.tick(FPS)
    PANTALLA.fill(Colores.NEGRO)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    form_principal.update(eventos)
    #ctual.update(eventos)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()

#Juuego de  Mario interfaz grafica


##