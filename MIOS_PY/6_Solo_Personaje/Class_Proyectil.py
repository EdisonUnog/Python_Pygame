import pygame, sys
from Constantes import*
from configuraciones import*

class Proyectil:
    def __init__(self, x, y, w, h, velocidad, direccion, path_img, base) -> None:
        self.imagen_proyectil = pygame.image.load(path_img)
        self.imagen_proyectil = pygame.transform.scale(self.imagen_proyectil, (w,h))
        self.rect = self.imagen_proyectil.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mover_x = 0
        self.mover_y = 0
        self.daño = 10
        self.base = base
        self.velocidad_Disparo = velocidad
        self.impacto_objetivo = False
        self.tiempo_collision = 0
        self.tiempo_trayectoria = 0

        self.lados = obtener_rectangulo(self.rect)
        self.collision_rect = pygame.Rect(self.rect)
        #self.collision_rect = self.lados["main"]
        self.rect_collition_varios_r = self.lados["right"]
        self.rect_collition_varios_l = self.lados["left"]

        # self.rect_collition_varios_r = pygame.Rect(self.rect.x + 25,self.rect.y,self.rect.w - 27,self.rect.h)
        # self.rect_collition_varios_l = pygame.Rect(self.rect.x,self.rect.y,self.rect.w - 20,self.rect.h)
        self.direccion = direccion
        self.is_collision = False

    def trayectoria(self):
        if (self.direccion == 0):
            self.mover_x = self.velocidad_Disparo
            self.movimiento_x(self.mover_x)
        elif (self.direccion == 1):
            self.mover_x = -self.velocidad_Disparo
            self.movimiento_x(self.mover_x)

    def draw(self, pantalla):
        if(False):
            pygame.draw.rect(pantalla , ROJO, rect = self.collition_rect)
            pygame.draw.rect(pantalla , BLANCO, rect = self.rect_collition_varios_l)
            pygame.draw.rect(pantalla , NEGRO, rect = self.rect_collition_varios_r)

        if(self.impacto_objetivo == False):
            pantalla.blit(self.imagen_proyectil, self.rect)

    def movimiento_x(self, delta_x):
        self.rect.x += delta_x
        self.collision_rect.x += delta_x
        self.rect_collition_varios_l.x += delta_x
        self.rect_collition_varios_r.x += delta_x

    def movimiento_y(self, delta_y):
        self.rect.y += delta_y
        self.collision_rect.y += delta_y
        self.rect_collition_varios_l.y += delta_y
        self.rect_collition_varios_r.y += delta_y

    def update(self, lista_objetos):
        self.collision(lista_objetos)
        self.trayectoria()
        self.collision_fuera_mapa()

    def collision(self, lista_objetos):
        '''
        colision con las plataformas o los enemigos, segun la lista de objetos recibida por por parametro
        '''
        for objeto in lista_objetos:
            if self.rect_collition_varios_l.colliderect(objeto.lados["main"]):
                objeto.impacto = True
                #objeto.damage_generate = self.daño
                objeto.is_collision_bala()
                self.velocidad_Disparo = 0
                self.impacto_objetivo = True
                print("collision pared")

    def collision_fuera_mapa(self):
        if (self.rect.x <= 5 or self.rect.x >= ANCHO - 5):
            self.impacto_objetivo = True