
import pygame
from Class_Colores import*

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, lista, direccion, velocidad) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.list_proyectiles = lista
        self.reescalar_aniamcion()
        self.rect = self.list_proyectiles[0].get_rect()
        self.rect.x = x 
        self.rect.y = y -15

        self.indice = 0
        self.lados = obtener_rectangulo(self.rect)
        self.trayectoria_dala = direccion
        self.velocidad_Disparo = velocidad

    def mover(self):
        if self.trayectoria_dala == 0:
            self.rect.x += self.velocidad_Disparo
        if self.trayectoria_dala == 1:
            self.rect.x += self.velocidad_Disparo
        if self.trayectoria_dala == -1:
            self.rect.x -= self.velocidad_Disparo

    def update(self, pantalla):
        pantalla.blit(self.list_proyectiles[self.indice], (self.rect.x, self.rect.y))
        self.indice = (self.indice +1) % len(self.list_proyectiles)

    def reescalar_aniamcion(self):
        for i in range(len(self.list_proyectiles)):
            self.list_proyectiles[i] = pygame.transform.scale(self.list_proyectiles[i], (15, 15))


def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario

lista_proyectiles = [pygame.image.load("balas/1.png"),
                    pygame.image.load("balas/2.png"),
                    pygame.image.load("balas/3.png"),
                    pygame.image.load("balas/4.png"),
                    pygame.image.load("balas/5.png"),
                    pygame.image.load("balas/6.png"),
                    pygame.image.load("balas/7.png")]