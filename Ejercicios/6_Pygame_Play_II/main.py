import pygame
from configuraciones import *
from pygame.locals import *
from modo import *

################################################################
# sueperficie asociado a un rect
def obtener_rectangulo(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2 , principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

#------------------------------

def aplicar_gravedad(acciones_personaje, pantalla, lados_personaje, lados_plataformas: pygame.rect):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(acciones_personaje, pantalla, lados_personaje["main"])
        #lados_personaje["main"].y += desplazamiento_y

        for lado in lados_personaje:
            lados_personaje[lado].y += desplazamiento_y

        if desplazamiento_y + gravedad < limit_velocidad_caida:
            desplazamiento_y += gravedad

    for piso in lados_plataformas:
        if lados_personaje["bottom"].colliderect(piso["top"]):
            esta_saltando = False
            desplazamiento_y = 0
            lados_personaje["main"].bottom = piso["main"].top + 5
            break
        else:
            esta_saltando = True

#------------------------------

def mover_personaje(lados_personaje, velocidad):
    for lado in lados_personaje:
        lados_personaje[lado].x += velocidad

#------------------------------

def animar_personaje(acciones_personaje, pantalla, rect_personaje):
    global contador_pasos # puede ser modificada
    largo = len(acciones_personaje)

    if contador_pasos >= largo: #cuenta los pasos permitidos
        contador_pasos = 0

    pantalla.blit(acciones_personaje[contador_pasos], rect_personaje)
    contador_pasos += 1

#------------------------------

def actualizar_pantalla(pantalla, que_hace, velocidad, lista_plataformas):   
    global esta_saltando, desplazamiento_y
    pantalla.blit(fondo,(0,0))

    pantalla.blit(plataforma, (lista_plataformas[1]["main"].x, lista_plataformas[1]["main"].y)) #primer plataforma

    match que_hace:
        case "derecha":
            if not esta_saltando:
                animar_personaje(personaje_camina, pantalla, lados_personaje["main"])
            mover_personaje(lados_personaje, velocidad)
        
        case "izquierda":
            if not esta_saltando:
                animar_personaje(personaje_camina_izquierda, pantalla, lados_personaje["main"])
            mover_personaje(lados_personaje, velocidad * -1) #decrementa en mover_pers

        case "salta":
            if not esta_saltando: # para que solo salta una vez en la misma gravedad
                esta_saltando = True
                desplazamiento_y = potencia_salto

        case "quieto":
            if not esta_saltando:
                animar_personaje(personaje_quieto, pantalla, lados_personaje["main"])

    aplicar_gravedad(personaje_salta, pantalla, lados_personaje, lista_plataformas)
            
################################################################

ANCHO = 1900
ALTO = 900
scren_size = (ANCHO, ALTO)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(scren_size)

#_Fondo
fondo = pygame.image.load("Principal/fondo_space.png")
fondo = pygame.transform.scale(fondo, scren_size)
PANTALLA.blit(fondo, (0,0))

################################################################
#_Variable de Salto
gravedad = 1
potencia_salto = -15
limit_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

#_Personaje
contador_pasos = 0
x_inicial = ALTO / 2 - 300
y_inicial = 650
pos_actual_x = 0
velocidad = 10

lista_animaciones = [personaje_quieto, personaje_camina, 
                    personaje_salta, personaje_camina_izquierda]

reescalar_imagenes(lista_animaciones, 75, 85)

rect_personaje = personaje_salta[0].get_rect()
rect_personaje.x = x_inicial
rect_personaje.y = y_inicial

lados_personaje = obtener_rectangulo(rect_personaje)

que_hace = "quieto"

#_Superficie piso donde se para el personaje
piso = pygame.Rect(0,0, ANCHO, 20)
piso.top = rect_personaje.bottom

rect_piso = obtener_rectangulo(piso) #funcion

#_Plataforma
plataforma = pygame.image.load("Principal/plataforma.png")
plataforma = pygame.transform.scale(plataforma, (400, 75))
rect_plataforma = plataforma.get_rect() #traigo un rectangulo
rect_plataforma.x = 500 #le doy una posicion en x e y
rect_plataforma.y = 620

lado_plataforma = obtener_rectangulo(rect_plataforma)

lista_plataformas = [rect_piso, lado_plataforma]

#-----------------------------------------------------------------------------------------------
run = True
while (run):
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    PANTALLA.blit(fondo, (0,0))
    keys = pygame.key.get_pressed()

    #dinamica del personaje
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        que_hace = "derecha"
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        que_hace = "izquierda"
    elif keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        que_hace = "salta"
    else:
        que_hace = "quieto"

    actualizar_pantalla(PANTALLA, que_hace, velocidad, lista_plataformas)
    # actualizar_pantalla(pantalla, que_hace, velocidad, piso, lista_plataformas)
    if get_mode() == True: # dibuja rect piso y rect personaje
        pygame.draw.rect(PANTALLA, "Blue" , rect_personaje, 2)
        pygame.draw.rect(PANTALLA, "green" , piso, 2)
        pygame.draw.rect(PANTALLA, "red" , rect_plataforma, 2)

    

    
    if keys[pygame.K_ESCAPE]:
        run = False

    pygame.display.update()
pygame.quit()