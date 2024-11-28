import pygame
from Donas import *

LARGO = 800
ALTO = 800
TAMAÑO_PANTALLA = (LARGO,ALTO)

pygame.init()
reloj = pygame.time.Clock()


DERECHA = 1
IZQUIERDA = 0

timer_event = pygame.USEREVENT + 0

#que se dispare dependiend oel tiempo que le pase
pygame.time.set_timer(timer_event,50)#que se dipare cada 50 milisegundos

reloj = pygame.time.Clock()

screen= pygame.display.set_mode(TAMAÑO_PANTALLA)

fondo = pygame.image.load("Recursos/fondo.png")
fondo_final = pygame.transform.scale(fondo,TAMAÑO_PANTALLA)
screen.blit(fondo_final,(0,0))

fuente = pygame.font.SysFont("Arail", 30)

imagen_homero_derecha = pygame.image.load("Recursos/derecha.png")
imagen_homero_derecha = pygame.transform.scale(imagen_homero_derecha,(200,250))

imagen_homero_izquierda = pygame.transform.flip(imagen_homero_derecha,True,False)

imagen_homero = imagen_homero_derecha

rectangulo_homero = imagen_homero.get_rect()
rectangulo_homero. x = 400
rectangulo_homero. y = 570
rectangulo_homero.width = 200
rectangulo_homero.height = 200

#boca de homero
x = 493
y = 658
z = 40

rectangulo_boca = pygame.Rect(x,y,z,z)
personaje = {"superficie ":imagen_homero,"rectangulo":rectangulo_homero,"score":0, "boca": rectangulo_boca}

#DONAS
lista_donas = crear_lista_donas(50)


flag=True
while flag:
    reloj.tick(60)
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False#cambia estado de la vandera           
        if evento.type == timer_event:
            update_donas(lista_donas)
            
    lista_teclas = pygame.key.get_pressed()
    
    if lista_teclas[pygame.K_RIGHT]:
        imagen_homero = imagen_homero_derecha
        nueva_x = rectangulo_homero.x + 10
        if nueva_x > 0 and nueva_x < LARGO - rectangulo_homero.width:
            #rectangulo_homero.x += 10
            personaje["rectangulo"].x += 10
            personaje["boca"].x += 10
    
    if lista_teclas[pygame.K_LEFT]:
        imagen_homero = imagen_homero_izquierda
        nueva_x = rectangulo_homero.x - 10
        if nueva_x > 0 :
            #rectangulo_homero.x -= 10
            personaje["rectangulo"].x -= 10
            personaje["boca"].x -= 10
    
    screen.blit(fondo,(0,0))
    screen.blit(imagen_homero,rectangulo_homero)
    
    for dona in lista_donas:
        screen.blit(dona["superficie"],dona["rectangulo"])
    
    verificar_collicion(lista_donas,personaje)
    texto = fuente.render(f"Score: {personaje['score']}", False, Colores.VERDE, Colores.AZUL_CLARO)
    screen.blit(texto, (0,0))

    pygame.draw.rect(screen,"Blue",personaje["rectangulo"],2)
    pygame.draw.rect(screen,"Green",personaje["boca"],2)
    
    pygame.display.update()
    
pygame.quit()