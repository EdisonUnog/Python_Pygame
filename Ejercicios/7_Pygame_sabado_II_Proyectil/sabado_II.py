
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
FPS = 30

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
diccionario_animaciones["quieto_iz"] = personaje_quieto_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["salta_iz"] = personaje_salta_izquierda
diccionario_animaciones["camina_derecha"] =  personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["disparar"] = personaje_dispara
diccionario_animaciones["disparar_iz"] = personaje_dispara_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, lista_proyectiles, pos_inicial, 15)

#piso
piso = pygame.Rect(0,0, ANCHO, 20)
piso.top = mi_personaje.lados["main"].bottom

#obtengo rect
lados_piso = obtener_rectangulo(piso)

#piso
cuadro = pygame.Rect(900,0, 400, 60)
cuadro.bottom = lados_piso["main"].top

#obtengo rect
lados_cuadro = obtener_rectangulo(cuadro)

diccionario_enemigo = {}
diccionario_enemigo["derecha"] = mis_enemigos
diccionario_enemigo["izquierda"] = mis_enemigo_izquierda

'''lista_enemigos = [Enemigo((50, 50), diccionario_enemigo, (1200, 740), 5),
                            Enemigo((50, 50), diccionario_enemigo, (970, 490), 5),
                            Enemigo((50, 50), diccionario_enemigo, (50, 80), 5)]'''

mis_enemigo = [Enemigo((50, 50), diccionario_enemigo, (905, 685), 5)]

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
        mi_personaje.direccion = 1
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        mi_personaje.que_hace = "izquierda"
        mi_personaje.direccion = -1
    elif keys[pygame.K_SPACE]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_l]:
        mi_personaje.que_hace = "dispara"
        x,y = mi_personaje.rectangulo.center
        mi_personaje.disparar((x, y), mi_personaje.direccion)
    else:
        mi_personaje.que_hace = "quieto"

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lados_piso)

    if len(mi_personaje.lista_disparos) > 0:
        for x in mi_personaje.lista_disparos:
            x.dibujar(PANTALLA)
            x.trayectorio()

            if x.rect.right < 50:
                mi_personaje.lista_disparos.remove(x)


    for mi_enemigo in mis_enemigo:
        mi_enemigo.update(PANTALLA)
        if mi_enemigo.lados["right"].colliderect(lados_cuadro["right"]):
            mi_enemigo.direccion = "izquierda"
        elif mi_enemigo.lados["left"].colliderect(lados_cuadro["left"]):
            mi_enemigo.direccion = "derecha"

        if mi_personaje.lados["main"].colliderect(mi_enemigo.lados["main"]):
            mis_enemigo.remove(mi_enemigo)
            print("colli")

    mi_personaje.kill(mi_personaje, mis_enemigo)

    # me muestra las lineas de los rectangulo
    if get_mode(): # dibuja rect piso y rect personaje

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "blue", lados_piso[lado], 2)
        for lado in lados_cuadro:
            pygame.draw.rect(PANTALLA, "Black", lados_cuadro[lado], 2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "red", mi_personaje.lados[lado], 2)

        for lista in mi_personaje.lista_disparos:
            for lado in lista.lados:
                pygame.draw.rect(PANTALLA, "red", lista.lados[lado], 2)



    #_sale del bucle
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()

