
import pygame, sys
from configuraciones import *
from pygame.locals import *
from Class_Personaje import *
from modo import *

################################################################################
def actualizar_pantalla(pantalla, personaje: Personaje, fondo, lados_piso):
    pantalla.blit(fondo, (0,0))
    #plataformas
    personaje.update(pantalla, lados_piso)
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
#pos_inicial = (650, ALTO//2 - 300)
pos_inicial = (ALTO/2 - 300, 650)
tamaño = (75, 85)

diccionario_animaciones = {} # va en la funcion reescalar_animacion("aqui")
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] =  personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, pos_inicial, 10)

#piso
piso = pygame.Rect(0,0, ANCHO, 20)
piso.top = mi_personaje.lados["main"].bottom

#obtengo rect
lados_piso = obtener_rectangulo(piso)

run = True
while (run):

    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()

    for event in lista_eventos:
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

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lados_piso)

    # me muestra las lineas de los rectangulo
    if get_mode(): # dibuja rect piso y rect personaje

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "blue", lados_piso[lado], 2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "red", mi_personaje.lados[lado], 2)



    #_sale del bucle
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()

