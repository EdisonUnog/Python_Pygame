
import pygame, sys
from niveles.configuraciones import *
from pygame.locals import *
from niveles.Class_Personaje import *
from niveles.Class_Colores import *
from niveles.diccionario import *
from niveles.Class_Monedas import *
from niveles.modo import *

from niveles.Class_Nivel_Uno import NivelUno
from niveles.Class_Nivel_Dos import NivelDos

from gui.GUI_Form_Principal import*

from gui.GUI_form import*

ANCHO = 1900
ALTO = 900
scren_size = (ANCHO, ALTO) 
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode(scren_size)

#Nivel_actual = NivelUno(PANTALLA)
#Nivel_actual = NivelDos(PANTALLA)

form_principal = FormPrincipal(PANTALLA, 500, 250, 900, 350, "Gold", "Magenta", 5, True)



while True:
    RELOJ.tick(FPS)
    PANTALLA.fill(Colores.NEGRO)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    form_principal.update(eventos)
    #ivel_actual.update(eventos)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()
