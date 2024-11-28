import pygame
from Class_Colores import Colores
from Donas import *

ANCHO = 800
ALTO = 800
screen_size = (ANCHO,ALTO)

pygame.init()

relog = pygame.time.Clock()
tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 100)

PANTALLA = pygame.display.set_mode(screen_size)

fondo = pygame.image.load("Recursos/fondo.png")
fondo_final = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo, (0,0))

fuente = pygame.font.SysFont("Arail", 30)

imagen_homero_derecha = pygame.image.load("Recursos/derecha.png")
imagen_homero_derecha = pygame.transform.scale(imagen_homero_derecha, (200, 250))

imagen_homero_izquierda = pygame.transform.flip(imagen_homero_derecha, True, False)
imagen_homero = imagen_homero_izquierda

rect_homero = imagen_homero.get_rect()
rect_homero.x = 400
rect_homero.y = 570
rect_homero.width = 200
rect_homero.height = 200

#_Personaje
x = 480
y = 658
z = 40

rect_boca = pygame.Rect(x,y,z,z)
personaje = {"superficie":imagen_homero, "rectangulo":rect_homero, "score":0, "boca":rect_boca}


#_Donas
lista_donas = crear_lista_donas(50)

flag = True 

while flag:
    relog.tick(60)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False  

        if event.type == tick:
            update_donas(lista_donas)

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_RIGHT] or lista_teclas[pygame.K_d]:
        imagen_homero = imagen_homero_derecha
        nueva_x = rect_homero.x + 10
        if nueva_x < ANCHO - rect_homero.width:
            personaje["rectangulo"].x += 10
            personaje["boca"].x += 10
    
    if lista_teclas[pygame.K_LEFT] or lista_teclas[pygame.K_a]:
        imagen_homero = imagen_homero_izquierda
        nueva_x = rect_homero.x - 10
        if nueva_x > 0:
            personaje["rectangulo"].x -= 10
            personaje["boca"].x -= 10

    
    PANTALLA.blit(fondo, (0,0))
    PANTALLA.blit(imagen_homero, rect_homero)

    for dona in lista_donas:
        PANTALLA.blit(dona["superficie"], dona["rectangulo"])
    
    verificar_collicion(lista_donas, personaje)
    
    texto = fuente.render(f"Score: {personaje['score']}", False, Colores.VERDE, Colores.AZUL_CLARO)
    PANTALLA.blit(texto, (0,0))

    pygame.draw.rect(PANTALLA,Colores.AZUL, personaje["rectangulo"], 2)
    pygame.draw.rect(PANTALLA,Colores.AZUL, personaje["boca"], 2)

    lista_teclas = pygame.key.get_pressed()    
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    pygame.display.update()
pygame.quit()





