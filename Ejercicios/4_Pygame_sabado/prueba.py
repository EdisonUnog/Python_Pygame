import pygame
from pygame.locals import * 
import sys

pygame.init

#creamos reloj
RELOJ = pygame.time.Clock()
FPS = 60

ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO,ALTO))

#creamos una superficie por cada rectangulo
superficie_rectangulo = pygame.Surface((50,50))
superficie_rectangulo.fill("Red")#le agregamos un color
#rectangulo
rectangulo = superficie_rectangulo.get_rect()#crear un rectangulo sobre una superficie que ya habia
#centramos el rectangulo porque el get_rect()lo posiciona en la posicion 0
rectangulo.center = (ANCHO/2,ALTO/2)


#otro rectangulo sentido contrario
otro_rectangulo = pygame.Rect(ANCHO/2 ,500, 50 ,50)
otro_rectangulo.center = (ANCHO/2,ALTO/2)


#movemos el rectangulo
def mover_rectangulo(rectangulo , velocidad_y, alto_pantalla):
    rectangulo.y += velocidad_y
    if rectangulo.top > alto_pantalla: #si top pasa el algo
        rectangulo.bottom = 0 #botom lo vuelve para arriba, lo volemos 0 para que vuelva 0 de la pantalla
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

def verificar_colision(rectangulo: pygame.Rect,otro_rectangulo):
    if rectangulo.colliderect(otro_rectangulo):
        pass

while True:
    #reloj
    RELOJ.tick(FPS)#agregamos el reloj y su velocidad
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #pintamos fondo negro asi dps pintamos el rectangulo asi lo podemos ver 
    pantalla.fill("Black")
    #movemos el rectangulo
    mover_rectangulo(rectangulo, 5,ALTO)
    
    mover_rectangulo(otro_rectangulo,-5,ALTO)
    
    verificar_colision(rectangulo,otro_rectangulo)
    
    #///////////////////////////////////////////////////////////////////
    pantalla.blit(superficie_rectangulo,rectangulo) # superponemos una imagen sobre otra
    pantalla.blit(superficie_rectangulo, otro_rectangulo)
    
    #para mostrar el rectangulo
    pygame.draw.rect(pantalla,"Blue",rectangulo)#a partir de un rectangulo genera una superficie
    pygame.draw.rect(pantalla,"red", otro_rectangulo)
    #actulizamos el contenido de la pantalla
    pygame.display.flip()