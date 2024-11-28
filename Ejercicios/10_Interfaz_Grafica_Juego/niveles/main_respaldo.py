
import pygame, sys
from configuraciones import *
from pygame.locals import *
from Class_Personaje import *
from Class_Colores import *
from Diccionarios import *
from Class_monedas import *
from modo import *

################################################################################
def actualizar_pantalla(pantalla, personaje: Personaje, fondo, lista_plataformas):
    pantalla.blit(fondo, (0,0))
    #_Plataformas
    for plataforma in lista_plataformas:
        plataforma.update_plataformas(pantalla)
    
    personaje.update(pantalla, lista_plataformas)
################################################################################

ANCHO = 1900
ALTO = 900
scren_size = (ANCHO, ALTO)
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode(scren_size)

fondo = pygame.image.load("fondo_space.png")
fondo = pygame.transform.scale(fondo, scren_size)

#_Personaje
mi_personaje = Personaje((75, 85) , diccionario_personaje, (ALTO/2 - 300, 650), 10)

############################################
#___Plataforma
mis_plataformas = [Plataforma((ANCHO, 20), piso,(0, mi_personaje.lados["main"].bottom)), #piso
                    Plataforma((400, 75),    plataforma_uno, (500, 620)),
                    Plataforma((300, 75), plataforma_uno, (1000, 500)),
                    Plataforma((200, 55), plataforma_uno, (200, 500)),
                    Plataforma((200, 55), plataforma_uno, (700, 300)),
                    Plataforma((150, 40), plataforma_uno, (500, 400))]

moneda_uno = Monedas((25, 25), lista_monedas, (520, 580))

run = True
while (run):

    RELOJ.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    #PANTALLA.blit(fondo, (0,0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_SPACE]:
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"


    actualizar_pantalla(PANTALLA, mi_personaje, fondo, mis_plataformas)
    moneda_uno.update_moneda(PANTALLA, mi_personaje, moneda_uno)
    # me muestra las lineas de los rectangulo
    if get_mode(): # dibuja rect piso y rect personaje

        '''for lado in lados_piso:
            pygame.draw.rect(PANTALLA, Colores.AZUL, lados_piso[lado], 2)'''

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, Colores.VERDE, mi_personaje.lados[lado], 2)

        for i in range(len(mis_plataformas)):
                pygame.draw.rect(PANTALLA, Colores.ROJO, mis_plataformas[i].rectangulo, 4)

        for img in mis_plataformas:
            for i in img.lados:
                pygame.draw.rect(PANTALLA, Colores.VERDE, img.lados[i]  , 2)
        


    #_sale del bucle
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()
