import pygame
from niveles.Class_Auxiliar import*
from niveles.constantes import*

class Trampa:
    def __init__(self, x, y, w, h,velocidad, left, right) -> None:
        self.image_list = Auxiliar.cargarImagen2("Recursos/Trampas/{0}.png", 4, False,1,1,w,h)
        self.image = self.image_list
        self.rect = self.image[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = 0

        self.velocidad = velocidad
        self.left = left
        self.right = right

        self.mover_l = False
        self.mover_r = True
        self.mover_x = 0

        self.lados = obtener_rectangulo(self.rect)

    def draw(self, screen):
        screen.blit(self.image[self.index], (self.rect.x, self.rect.y))
        self.index = (self.index - 1) % len(self.image)

    def animar_x(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def mover_trampa_x(self):
        if self.mover_r:
            self.mover_x = self.velocidad
            self.animar_x(self.mover_x)
        elif(self.mover_l):
            self.mover_x = -self.velocidad
            self.animar_x(self.mover_x)

    def l_r(self):
        if self.rect.x >= self.right and self.rect.y :
                self.mover_r = False
                self.mover_l = True
        elif(self.rect.x <= self.left and self.rect.y ):
                self.mover_r = True
                self.mover_l = False

    def update(self):
        self.mover_trampa_x()
        self.l_r()