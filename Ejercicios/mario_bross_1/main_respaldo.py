import pygame
from niveles.configuraciones import *
from pygame.locals import *

from niveles.Class_Personaje import *
from niveles.Class_Plataformas import *
from niveles.Class_Monedas import *

from niveles.Listas_All import *
from niveles.Class_Colores import *
from niveles.modo import *

################################################################
#actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_Plataformas_lados, mis_plataformas)
def actualizar_pantalla(pantalla, mi_personaje: Personaje, fondo, lados_piso, lista_plataformas, lista_monedas):
    pantalla.blit(fondo, (0,0))
    #plataformas

    for plataforma in lista_plataformas:
        plataforma.update_plataformas(pantalla)

    for moneda in lista_monedas:
        moneda.update_moneda(pantalla, mi_personaje, lista_monedas)

    mi_personaje.update(pantalla,lados_piso, lista_plataformas)
    #actualizar mi personaje: que esta haciendo "quieto"

################################################################
ANCHO = 1700
ALTO = 900
scren_size = (ANCHO, ALTO)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(scren_size)

#_Fondo
fondo = pygame.image.load("Recursos/fondo_mario.png")
fondo = pygame.transform.scale(fondo, scren_size)
#_Titulo
titulo = pygame.display.set_caption("Replica_Mario")
#_Icono
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

#_PERSONAJE
diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["abajo"] = personaje_abajo

pos_inicial = (ALTO/2 - 350, 710)
tamaño = (65, 85)
velocidad = 10

mi_personaje = Personaje(tamaño, diccionario_animaciones, pos_inicial, velocidad)

#_PISO
piso = pygame.Rect(0,0, ANCHO, 20)
piso.top = mi_personaje.lados["main"].bottom
lados_piso = obtener_rectangulo(piso)
################################################################

#-----------------------------------------------------------------------------------------------
run = True
while (run):
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_s]:
        mi_personaje.que_hace = "agachar"
    else:
        mi_personaje.que_hace = "quieto"

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lados_piso, lista_plataformas, lista_monedas)

    PANTALLA.blit(bandera_1.bandera, bandera_1.rectangulo)

    if get_mode():
        
        pygame.draw.rect(PANTALLA, Colores.NEGRO, piso, 5)
        for lado in lados_piso: #_Piso_
            pygame.draw.rect(PANTALLA, Colores.ROJO, lados_piso[lado], 2)

        pygame.draw.rect(PANTALLA, Colores.NEGRO, mi_personaje.rectangulo, 5)
        for lado in mi_personaje.lados: #MArio_Bross
            pygame.draw.rect(PANTALLA, Colores.BLANCO, mi_personaje.lados[lado], 2)

        for i in range(len(lista_plataformas)): #print rect imagen
                pygame.draw.rect(PANTALLA, Colores.AZUL, lista_plataformas[i].rectangulo, 5)

        for img in lista_plataformas: #print rect asociados al rectangulo principal
            for i in img.lados:
                pygame.draw.rect(PANTALLA, Colores.BLANCO, img.lados[i], 2)

        pygame.draw.rect(PANTALLA, Colores.BLANCO, bandera_1.rectangulo, 3)
            

    pygame.display.update()
pygame.quit()