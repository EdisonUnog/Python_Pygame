import pygame,sys
from Constantes import*

def obtener_lados_rect_uno(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["top"] = pygame.Rect(rect_principal.x  , rect_principal.y , rect_principal.w , 5)
    diccionario["bottom"] = pygame.Rect(rect_principal.x , rect_principal.y + rect_principal.h - 5, rect_principal.w, 5)
    diccionario["right"] = pygame.Rect(rect_principal.x + rect_principal.w - 5, rect_principal.y + 10, 5, rect_principal.h - 20)
    diccionario["left"] = pygame.Rect(rect_principal.x, rect_principal.y + 10 , 5, rect_principal.h - 20)
    return diccionario

def obtener_lados_rect_dos(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 10 , rect_principal.top + 15, 10, rect_principal.height - 35)
    diccionario["left"] = pygame.Rect(rect_principal.left , rect_principal.top + 15, 10, rect_principal.height - 35)
    return diccionario


def obtener_lados_rect_tres(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right -2 , rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left , rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario



pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((1100, 450))

img = pygame.image.load("Recursos/Personaje/Salta/1.png")
img = pygame.transform.scale(img ,(200, 200))
img_rect = img.get_rect()
img_rect.x = 370
img_rect.y = 50
lados = obtener_lados_rect_uno(img_rect)


img2 = pygame.image.load("Recursos/Personaje/Salta/1.png")
img2 = pygame.transform.scale(img2 ,(200, 200))
img_rect2 = img2.get_rect()
img_rect2.x = 590
img_rect2.y = 50
lados2 = obtener_lados_rect_dos(img_rect2)

img3 = pygame.image.load("Recursos/Personaje/Salta/1.png")
img3 = pygame.transform.scale(img3 ,(200, 200))
img_rect3 = img3.get_rect()
img_rect3.x = 810
img_rect3.y = 50
lados3 = obtener_lados_rect_tres(img_rect3)

while True:
    RELOJ.tick(FPS)
    PANTALLA.fill(VERDE)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    #----------------------------------------------------------------
    superficie = pygame.draw.rect(PANTALLA, BLANCO, pygame.Rect(50,50, 300, 300), 10)
    arriba = pygame.draw.rect(PANTALLA, ROJO, pygame.Rect(superficie.left , superficie.top, superficie.width, 30), 3)
    abajo = pygame.draw.rect(PANTALLA, ROJO, pygame.Rect(superficie.left , superficie.bottom - 30, superficie.width, 30), 3)
    izquierda = pygame.draw.rect(PANTALLA, ROJO, pygame.Rect(superficie.left , superficie.top, 30, 300), 3)
    derecha = pygame.draw.rect(PANTALLA, ROJO, pygame.Rect(superficie.right - 30, superficie.top, 30, 300), 3)


    #----------------------------------------------------------------
    PANTALLA.blit(img, img_rect)  
    pygame.draw.rect(PANTALLA, BLANCO, img_rect, 4)
    for lado in lados:
        pygame.draw.rect(PANTALLA, ROJO, lados[lado], 2)

    #----------------------------------------------------------------
    PANTALLA.blit(img2, img_rect2)
    # for lado2 in lados2:
    #     pygame.draw.rect(PANTALLA, ROJO, lados2[lado2], 2)
    pygame.draw.rect(PANTALLA, ROJO, img_rect2, 4)
    pygame.draw.rect(PANTALLA, NEGRO, lados2["top"], 3)
    pygame.draw.rect(PANTALLA, NEGRO, lados2["bottom"], 3)
    pygame.draw.rect(PANTALLA, NEGRO, lados2["left"], 3)
    pygame.draw.rect(PANTALLA, NEGRO, lados2["right"], 3)

    #----------------------------------------------------------------
    PANTALLA.blit(img3, img_rect3)
    pygame.draw.rect(PANTALLA, BLANCO, img_rect3, 4)
    pygame.draw.rect(PANTALLA, ROJO, lados3["top"], 3)
    pygame.draw.rect(PANTALLA, ROJO, lados3["bottom"], 3)
    pygame.draw.rect(PANTALLA, ROJO, lados3["left"], 3)
    pygame.draw.rect(PANTALLA, ROJO, lados3["right"], 3)


    pygame.display.update() # actualiza mi pantalla
pygame.quit()