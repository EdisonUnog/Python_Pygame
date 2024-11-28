
import pygame, sys
from configuraciones import *
from pygame.locals import *
from Class_Personaje import *
from Class_Colores import *
import proyectil
from Diccionarios import *
from Class_monedas import *
from modo import *

################################################################################
def actualizar_pantalla(pantalla, personaje: Personaje, fondo, lista_plataformas, mis_plataformas, moneda_uno):
    pantalla.blit(fondo, (0,0))
    #_Plataformas
    update_plataformas(pantalla, mis_plataformas)
    moneda_uno.mostrar(pantalla)
    #moneda_uno.puntaje(pantalla)
    #_Personaje
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
posinicial = (ALTO/2 - 300, 650)
tama = (75, 85)
mi_personaje = Personaje(tama , diccionario_personaje, posinicial, 15)

############################################
#___Plataforma
pos_init_pla = (500, 620)
tamaño = (400, 75)

mi_plataforma_1 = Plataforma(tamaño,    plataforma_uno, pos_init_pla)
mi_plataforma_2 = Plataforma((300, 75), plataforma_uno, (1000, 500))
mi_plataforma_3 = Plataforma((200, 55), plataforma_uno, (200, 500))
mi_plataforma_4 = Plataforma((200, 55), plataforma_uno, (700, 300))
mi_plataforma_5 = Plataforma((150, 40), plataforma_uno, (500, 400))

mis_plataformas = [mi_plataforma_1, mi_plataforma_2, 
                    mi_plataforma_3, mi_plataforma_4, mi_plataforma_5]
#piso
piso = pygame.Rect(0,0, ANCHO, 20)
piso.top = mi_personaje.lados["main"].bottom
#obtengo rect
lados_piso = obtener_rectangulo(piso)

lista_plataformas = [lados_piso, mi_plataforma_1.lados, mi_plataforma_2.lados, 
                    mi_plataforma_3.lados, mi_plataforma_4.lados, mi_plataforma_5.lados]

moneda_uno = Monedas((25, 25), lista_monedas, (520, 580))

lista_balas = []


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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and mi_personaje.un_salto == False:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        mi_personaje.que_hace = "derecha"
        mi_personaje.direccion = 1
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        mi_personaje.que_hace = "izquierda"
        mi_personaje.direccion = -1
    elif keys[pygame.K_l]:
        mi_personaje.que_hace = "dispara"
    else:
        mi_personaje.que_hace = "quieto"

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataformas, mis_plataformas, moneda_uno)
    moneda_uno.collicion_moneda(PANTALLA,mi_personaje, moneda_uno)
    #bala.update(PANTALLA)
    # me muestra las lineas de los rectangulo
    if get_mode(): # dibuja rect piso y rect personaje

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, Colores.AZUL, lados_piso[lado], 2)

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
