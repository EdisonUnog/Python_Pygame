import pygame
from niveles.Class_Auxiliar import*

class Pisos:
    def __init__(self, tamanio:tuple, i, pos_inicial:tuple) -> None:

        self.ancho = tamanio[0]
        self.alto = tamanio[1]
        self.piso = Auxiliar.cargarImagen("Recursos/Pisos/piso{0}.png", 5, False,1,w=self.ancho, h=self.alto)       
        self.img_piso = self.piso[i]
        self.rectangulo = self.img_piso.get_rect() #obtengo rect de la imagen
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo) #dibujo lados al rect
        self.collition_rect = pygame.Rect(self.rectangulo)
        self.rect_collition_bala_r = pygame.Rect(self.rectangulo)
        #_lados a donde va a colisionar
        self.rect_principal = self.lados["main"]
        self.collision_rect_top = self.lados["top"]
        self.collision_rect_bottom = self.lados["bottom"]
        self.collision_rect_right = self.lados["right"]
        self.collision_rect_left = self.lados["left"]
        self.impacto = False

    def draw(self, pantalla): #dibujo piso
        pantalla.blit(self.img_piso, self.lados["main"])
    
    def is_collision_bala(self):
        '''
        El metodo verifica si la bala colision con la plataforma para luego poder removerla de la lista.
        '''
        if(self.impacto):
            self.impacto = False