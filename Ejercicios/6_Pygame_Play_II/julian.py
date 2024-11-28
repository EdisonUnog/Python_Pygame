import pygame ,sys
from configuraciones import * 
from pygame.locals import *
from modo import * 



######################################################################################

#OBTENGO RECTANGULOS
def obtener_rectangulos(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario



#APLICAR GRAVEDAD
def aplicar_gravedad(pantalla, personaje_accion, lados_personaje, lados_plataformas: pygame.rect):
    global desplazamiento_y, esta_saltando
    
    if esta_saltando:
        animar_personaje(personaje_accion, pantalla ,lados_personajes["main"])#HAGO LA ANIMACION DE SALTO
        #lados_personajes["main"].y += desplazamiento_y #ESTO VA HACER QUE PEGUE EL SALTO
        
        
        for lado in lados_personaje:#EL LADOS_PERSONAJE PRINCIPAL ACOMPAÑEA A LO DEMAS RECTANGULO A SI NO CAEN
            lados_personaje[lado].y += desplazamiento_y
        
        if desplazamiento_y + gravedad < limite_velocidad_caida: #SI LA SUMA ES MENOR ES PORQUE TOCO EL PISO
            desplazamiento_y += gravedad
        
    for pisos in lados_plataformas:#VERIFICAMOS CADA PISO , SI O ES PISO O LA PLATAFORMA PERO EL PERSONAJE HAGA COLISION SI O SI
        if lados_personajes["bottom"].colliderect(pisos["top"]):
            #RESETEAMOS LOS VALORES BASICAMENTE
            lados_personajes["main"].bottom = pisos["main"].top +5#EL BOTTOM DEL RECTANGULO PRINCIPAL VA A CONINCIDIR CON EL TOP DEL RECTANGULO PRINCIPAL DE LA PLATAFORMA
            esta_saltando = False
            desplazamiento_y = 0 #PARA QUE EL PERSONAJE NO SIGA CAYENDO
            break#SI COLISIONO YA NO ESTA SALTANDO
        else:#SI NO ESTA COLISIONANDO ESTA SALTANDO
            esta_saltando = True

#MOVEMOS REGTANGULO DEL PERSONAJE
def mover_personaje(lados_personajes,velocidad):
    for lado in lados_personajes:
        lados_personajes[lado].x += velocidad



#ANIMAR PERSONAJES , RECOREMOS UNA SECUENCIA DE IMAGENES DE CADA UNA DE LAS LISTA QUE TENEMOS Y BLITEAR ESAS IMAGENES
def animar_personaje(acciones_personaje, pantalla, rectangulo_personaje):
    global contador_pasos #ESTA VARIABLE PUEDE SER MODIFICADA 
    
    #DEFINIMSO EL LARGO DE LA ACCION
    largo = len(acciones_personaje)#EL LARGO VA HACER EL LEN DE LA LISTA
    
    
    #CONTADOR DE PASOS, NECESITAMOS SABES SI DIO MAS PASOS DE LO QUE PERMITE LA ANIMACION
    if contador_pasos >=largo:#SI SUPERA EL LARGO DE LA LISTA VUELVE A 0 
        contador_pasos = 0
    
    pantalla.blit(acciones_personaje[contador_pasos],rectangulo_personaje)#CONTADOR PARA QUE SE BLITEE CADA ANIMACION
    contador_pasos +=1



#ACTUALIZAR PANTALLA
def actualizar_pantalla(pantalla ,que_hace ,velocidad,lista_plataformas):
    global esta_saltando
    global desplazamiento_y
    
    
    pantalla.blit(fondo,(0,0))#BLIT DEL FONDO DEL JUEGO
    #RECORRER LA LISTA DEP LATAFORMAS PARA UBICAR MAS DE UNA ('''HACER DESPUES''')
    pantalla.blit(plataforma,(lista_plataformas[1]["main"].x,lista_plataformas[1]["main"].y))#PRIMER PLATAFORMA Y POSICION 0 ES EL PISO Y MAIN ES EL PRINCIPAL
    
    match que_hace:
        case "derecha":#TENEMOS QUE MOVER PERSONAJE HACIA LA DERECHA DE DAMOS ANIMACION Y MOVIMIENTO
            if not esta_saltando:   #PARA QUE NO SE MUEVA HACIA LA DERECHA MIENTRA SALTO    
                animar_personaje(personaje_camina, pantalla , lados_personajes["main"])
            mover_personaje(lados_personajes, velocidad)
        case "izquierda":
            if not esta_saltando:   #PARA QUE NO SE MUEVA  HACIA LA IZQUIERDA MIENTRA SALTO    
                animar_personaje(personaje_camina_izquierda, pantalla , lados_personajes["main"])
            mover_personaje(lados_personajes, velocidad*-1)#si la velocidad viene *10 el *-10 lo cambia y se mueve hacia la izquierda
        case "salta":
            if not esta_saltando:#SI NO ESTA SALTANDO (PARA NO HACER DOBLE SALTO)
                esta_saltando =  True
                desplazamiento_y = potencia_salto
        case "quieto":#COMO ESTA QUIETO SOLO LO ANIMAMOS
            if not esta_saltando: 
                animar_personaje(personaje_quieto, pantalla, lados_personajes["main"])
    
    
    aplicar_gravedad(pantalla, personaje_salta, lados_personajes, lista_plataformas)



#######################################################################################



W,H = 1900,900
TAMAÑO_PANTALLA = (W,H)
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))


#FONDO DEL JUEGO
fondo = pygame.image.load("Principal/fondo_space.png")
#TRANSFORMAMOS EL FONDO AL TAMAÑO QUE LE PASAMOS
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)


#VARIABLES SALTO
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15 
esta_saltando = False #necesitamos bandera para saber si esta saltando o no
desplazamiento_y = 0 #esto es para poder desplazar la imagen durante el salto 


#PERSONAJE
contador_pasos = 0 #LOS PASOS
x_inicial = H/2 - 300 #DONDE QUEREMOS QUE APAREZCA EL PERSONAJE
y_inicial = 650 #POSICION INICIAL DE Y
posicion_actual_x = 0 #POSICION ACTUAL DEL PERSONAJE
velocidad = 10 #VELOCIDAD DEL PERSONAJE


#CREAMOS UNA LISTA DE ANIMACIONES
lista_animaciones = [personaje_quieto , 
                    personaje_camina,
                    personaje_salta, 
                    personaje_camina_izquierda]#CARGAMOS LAS LISTA QUE ESTAN EN COFIGURACION

#REESCALO LAS IMAGENES ANTES DEL RECTANGULO PORQUE SINO TOMA LA LISTA_ANIMACIONES QUE CONTIENE LAS IMAGENES NOO REESCALADAS
reescalar_imagenes(lista_animaciones,75,85)



#RECTANGULO DEL PERSONAJE QUE SALTA
rectangulo_personaje = personaje_salta[0].get_rect()
rectangulo_personaje.x = x_inicial#ASGINAMOS ESTO PARA QUE EL PERSONAJE NO APAREZCA EN CUALQUIER LUGAR
rectangulo_personaje.y = y_inicial#ASGINAMOS ESTO PARA QUE EL PERSONAJE NO APAREZCA EN CUALQUIER LUGAR

lados_personajes = obtener_rectangulos(rectangulo_personaje)

#CREAMOS ESTA VARIABLE PARA SABER QUE HACE EL PERSONAJE Y A FUTURO NOS FACILITA MAS COSAS
que_hace = "quieto"


#CREAMOS UNA SUPERFICIE QUE VA A REPRESENTAR EL PISO '''PISO'''
#EL PISO VA A HACER UN RECTANGULO
piso = pygame.Rect(0,0,W,20)
#QUE COINDIDA EL ''TOP'' DEL PISO CON EL '''BOTTON''' DEL PERSONAJE
piso.top = rectangulo_personaje.bottom

lados_piso = obtener_rectangulos(piso)


#PLATFORMA
plataforma = pygame.image.load("Principal/plataforma.png")
#ECALAMOS EL TAMAÑAO QUE QUEREMOS
plataforma = pygame.transform.scale(plataforma,(400,75))
rectangulo_plataforma = plataforma.get_rect()
#DAMOS POSICION EN X,Y
rectangulo_plataforma.x = 500
rectangulo_plataforma.y = 620

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

#LISTA PLATAFORMAS
lista_plataformas = [lados_piso,lados_plataforma]

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # no agregaste el pygame
            pygame.quit()
            sys.exit(0)

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    PANTALLA.blit(fondo, (0, 0))

    keys = pygame.key.get_pressed()
    
    #SI LA TECLA DERECHA ESTA PRESIONADA
    if keys[pygame.K_RIGHT]:
        que_hace = "derecha" #SI PRESIONAMOS TECLA DERECHA LA VARIABLE QUE_HACE CAMBIA A DERECHA
    elif keys[pygame.K_LEFT]:
        que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        que_hace = "salta"
    else:
        que_hace = "quieto"
    
    actualizar_pantalla(PANTALLA, que_hace, velocidad,lista_plataformas)
    
    #DEFINIMOS EN QUE MODO TRABAJAMOS (CREADO EN LA FUNCION MODO.PY)
    #SI ESTA EN TRUE DIBUJA TODOS LOS RECTANGULO QUE TENGA
    if get_mode() == True:
        pygame.draw.rect(PANTALLA,"Blue",rectangulo_personaje ,2)
        pygame.draw.rect(PANTALLA,"Green",piso,2)
        pygame.draw.rect(PANTALLA,"Magenta",rectangulo_plataforma,2)
    
    pygame.display.update()

pygame.quit()