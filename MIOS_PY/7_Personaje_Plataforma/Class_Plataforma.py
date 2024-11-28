import pygame
from Class_Auxiliar import*
from configuraciones import*

class Plataforma:
    def __init__(self, x, y,width, height, velocidad, movimiento_ms, left, right, velocidad_top_down, i, top, l_r=None):

        self.image_list = Auxiliar.cargarImagen2("Recursos/Plataformas/plat{0}.png", 4, False,1,1,w=width,h=height)
        self.image = self.image_list[i]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.static = 0
        self.move_y = 0
        self.l_r = l_r
        self.lados = obtener_rectangulo(self.rect)
        
        self.punto_volver_plat_l = left
        self.punto_volver_plat_r = right
        self.punto_volver_plat_up = top

        self.speed_up_down = velocidad_top_down

        self.move_up = False
        self.move_down = False

        self.move_l = False
        self.move_r = True

        self.speed = velocidad
        self.collition_rect = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 8)
        self.rect_collition_bala_r = pygame.Rect(self.rect)
        self.rect_principal = self.lados["main"]
        self.collision_rect_top = self.lados["top"]
        self.collision_rect_bottom = self.lados["bottom"]
        self.collision_rect_right = self.lados["right"]
        self.collision_rect_left = self.lados["left"]
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = movimiento_ms

        self.impacto = False

        self.speed_up_down = velocidad_top_down

    def draw(self,screen):
        '''
        Dibuja la plataforma y los rectagunlos en caso de ser necesario.
        Recibe por parametro la pantalla. 
        '''
        screen.blit(self.image, self.rect)
        if(False):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_ground_collition)

    def update(self, delta_x):   
        self.tiempo_transcurrido_move += delta_x
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.punto_volver()
            self.move_platform_x()
            self.move_platform_y()
            self.tiempo_transcurrido_move = 0

    def change_x(self, eje_x):
        '''
        El metodo produce el movimiento del rectangulo del mismo de manera horizontal y seguida de sus rectangulos correspondiente.
        Recibe por parametro el eje_x.
        '''
        '''self.rect.x += eje_x
        self.collition_rect.x += eje_x
        self.rect_ground_collition.x += eje_x
        self.rect_collition_bala_r.x += eje_x'''
        
        for lado in self.lados:
            self.lados[lado].x += eje_x

    def change_y(self,eje_y):
        '''
        El metodo produce el movimiento del rectangulo del mismo de manera vertical y seguida de sus rectangulos correspondiente.
        Recibe por parametro el eje_y.
        '''
        # self.rect.y += eje_y
        # self.collition_rect.y += eje_y
        # self.rect_ground_collition.y += eje_y
        # self.rect_collition_bala_r.y += eje_y
    
        for lado in self.lados:
            self.lados[lado].y += eje_y

    def move_platform_x(self):
        '''
        El metodo mueve la plataforma de manera horizontal dependiendo el speed ingresado.
        '''
        if(self.move_r):
            self.move_x = self.speed
            self.static = self.speed
            self.change_x(self.move_x)
        elif(self.move_l):
            self.move_x = -self.speed
            self.static = -self.speed
            self.change_x(self.move_x)

    def move_platform_y(self):
        '''
        El metodo mueve la plataforma de manera vertical dependiendo el speed ingresado.
        '''
        if(self.move_up):
            self.move_y = -self.speed_up_down
            self.change_y(self.move_y)
        elif(self.move_down):
            self.move_y = self.speed_up_down
            self.change_y(self.move_y)

    def punto_volver(self):
        '''
        El metodo verifica la posicion de la plataforma y dependiendo la ubicación del rect se produce los eventos.
        '''
        if(self.l_r == 0):
            if(self.rect.x >= self.punto_volver_plat_r and self.rect.y >= 630):
                self.move_r = False
                self.move_l = True
                self.move_down = False
            elif(self.rect.x <= self.punto_volver_plat_l and self.rect.y >= 630):
                self.move_x = 0
                self.move_r = False
                self.move_l = False
                self.move_up = True
                self.move_down = False
            
            if(self.rect.y <= self.punto_volver_plat_up):
                self.move_up = False
                self.move_down = True
                
        elif(self.l_r == 1):
        # plat permenece a la izquierda, sube y baja
            if(self.rect.x <= self.punto_volver_plat_r and self.rect.y >= 630):
                self.move_r = True
                self.move_l = False
                self.move_down = False
            elif(self.rect.x >= self.punto_volver_plat_l and self.rect.y >= 630):
                self.move_x = 0
                self.move_r = False
                self.move_l = False
                self.move_up = True
                self.move_down = False
            
            if(self.rect.y <= self.punto_volver_plat_up):
                self.move_up = False
                self.move_down = True

        #derecha a izquierda
        #Plataforma(700, 600, 100, 20, 10, 10, 300, 1000, 0, 2, 0, 2))
        elif(self.l_r == 2):
            if(self.rect.x >= self.punto_volver_plat_r and self.rect.y >= 400):
                self.move_r = False
                self.move_l = True
                self.move_down = False
            elif(self.rect.x <= self.punto_volver_plat_l and self.rect.y >= 400):
                self.move_x = 0
                self.move_r = True
                self.move_l = False
                self.move_up = True
                self.move_down = False
            
            if(self.rect.y <= self.punto_volver_plat_up):
                self.move_up = False
                self.move_down = True

    
    def is_collision_bala(self):
        '''
        El metodo verifica si la bala colision con la plataforma para luego poder removerla de la lista.
        '''
        if(self.impacto):
            self.impacto = False