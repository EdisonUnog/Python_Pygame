import pygame
from niveles.Class_Auxiliar import*
from niveles.constantes import*

class Plataforma:
    def __init__(self, x, y, w, h, velocidad, left, right, top, index, posicion_up=None) -> None:

        self.image_list = Auxiliar.cargarImagen2("Recursos/Plataformas/plat{0}.png", 4, False,1,1,w,h)
        self.image = self.image_list[index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.lados = obtener_rectangulo(self.rect)
        self.collition_rect = pygame.Rect(self.rect)
        self.rect_collition_bala_r = pygame.Rect(self.rect)
        self.rect_principal = self.lados["main"]
        self.collision_rect_top = self.lados["top"]
        self.collision_rect_bottom = self.lados["bottom"]
        self.collision_rect_l = self.lados["left"]
        self.collision_rect_r = self.lados["right"]

        self.velocidad = velocidad
        self.left = left
        self.right = right
        self.altura_top = top
        self.posicion_up = posicion_up

        self.mover_x = 0
        self.mover_y = 0
        self.mover_up = False
        self.mover_down = False
        self.mover_l = False
        self.mover_r = True

        self.alto = 640
        
        #_Collision bala
        self.impacto = False


    def draw(self, screen):
        screen.blit(self.image, self.lados["main"])
    
    def animar_x(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def animar_y(self, velocidad):
        for lado in self.lados:
            self.lados[lado].y += velocidad

    def mover_plataforma_x(self):
        if self.mover_r:
            self.mover_x = self.velocidad
            self.animar_x(self.mover_x)
        elif(self.mover_l):
            self.mover_x = -self.velocidad
            self.animar_x(self.mover_x)

    def mover_plataforma_y(self):
        if self.mover_up:
            self.mover_y = -self.velocidad
            self.animar_y(self.mover_y)
        elif(self.mover_down):
            self.mover_y = self.velocidad
            self.animar_y(self.mover_y)

    def l_r(self):
        if(self.posicion_up == 0):
            if self.rect.x >= self.right and self.rect.y >= self.alto:
                self.mover_r = False
                self.mover_l = True
                self.mover_down = False
            elif(self.rect.x <= self.left and self.rect.y >= self.alto):
                self.mover_r = False
                self.mover_l = False
                self.mover_up = True
                self.mover_down = False

            if(self.rect.y <= self.altura_top):
                self.mover_up = False
                self.mover_down = True
        
        elif(self.posicion_up == 1):
            if self.rect.x >= self.right and self.rect.y >= self.alto:
                self.mover_r = False
                self.mover_l = False
                self.mover_up = True
            elif(self.rect.x <= self.left and self.rect.y >= self.alto):
                self.mover_r = False
                self.mover_l = False
                self.mover_up = True
                self.mover_down = False

            if(self.rect.y <= self.altura_top):
                self.mover_up = False
                self.mover_down = True

        elif(self.posicion_up == 2):           
            if self.rect.x >= self.right and self.rect.y >= self.alto:
                self.mover_r = False
                self.mover_l = True
            elif(self.rect.x <= self.left and self.rect.y >= self.alto):
                self.mover_r = True
                self.mover_l = False

    def update(self):
        self.mover_plataforma_x()
        self.mover_plataforma_y()
        self.l_r()

    def is_collision_bala(self):
        if(self.impacto):
            self.impacto = False