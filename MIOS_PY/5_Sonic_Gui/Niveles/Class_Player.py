import pygame
from Niveles.Class_Auxiliar import *
from Niveles.constantes import *
from Niveles.Class_Lista_Proyectil import*
from Gui.gui_barra_vida import*
from Gui.gui_form import *

class Player:
    def __init__(self,x,y,speed_walk,speed_run,move_rate_ms,gravity,jump,vida,screen) -> None:
        self.stay_r = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Idle (32x32).png",11,1,False,1,2)
        self.stay_l = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Idle (32x32).png",11,1,True,1,2)
        self.walk_r = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Run (32x32).png",12,1,False,1,2)
        self.walk_l = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Run (32x32).png",12,1,True,1,2)
        self.jump_r = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Jump (32x32).png",1,1,False,1,2)
        self.jump_l = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Jump (32x32).png",1,1,True,1,2)
        self.fall_r = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Fall (32x32).png",1,1,False,1,2)
        self.fall_l = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Fall (32x32).png",1,1,True,1,2)
        self.hit_r = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Hit (32x32).png",7,1,False,1,2)
        self.hit_l = Auxiliar.get_img("Recursos/Main Characters/Mask Dude/Hit (32x32).png",7,1,True,1,2)
        self.jump_y = jump
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        self.move_rate_ms = move_rate_ms
        self.vida = vida
        self.screen = screen
        self.muerte = False
        self.puntos_player = 0
    
        self.gravity = gravity

        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.tiempo_transcurrido_move = 0
        self.direction = DIRECTION_R
        self.live = True
        self.impacto = False
        self.damage_generate = 0

        #sonidos
        self.laser_sound = pygame.mixer.Sound("Recursos/music/laser5.ogg")
        
        self.hit_sound = pygame.mixer.Sound("Recursos/music/golpe_de_coco.wav")
        self.hp = 100

        #_rectangulo de toda la animacion
        self.collition_rect = pygame.Rect(+x+self.rect.width/3,y,self.rect.width/2,self.rect.height)
        #_collision con el piso
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 2, GROUND_RECT_H)
        #_rect de la izquierda
        self.rect_collition_l = pygame.Rect(self.rect.x + 10,self.rect.y + 15,self.rect.w - 60,self.rect.h - 35)
        #_rect de la derecha
        self.rect_collition_bala_r = pygame.Rect(self.rect.x + 53,self.rect.y + 15,self.rect.w - 60,self.rect.h - 35)

        self.is_fall = False
        self.is_jump = False
        self.caminando = False
        self.is_on_platform = False
        self.limite_jump = self.rect.y * 2
        self.limite_jump_y = False
        self.lista_proyectiles = ListProyectil(screen,self.rect,"Recursos/Enemies/Plant/Bullet.png",self)
        self.collision_wall_r = False
        self.collision_wall_l = False
    
    def animation_frame(self,animation):
        '''
        El metodo vuelve lo frames a 0 en caso de que la animación sea mayor o menor. Para evitar el error de que se "pasó de len".
        '''
        if(self.animation != animation):
            self.frame = 0

    def walk(self,direction):
        '''
        El metodo produce el movimiento de caminar por el mapa.
        '''
        self.direction = direction
        if(self.direction == DIRECTION_R):
            if(not self.collision_wall_r):
                self.animation = self.walk_r
                self.move_x = self.speed_walk
        else:
            if(not self.collision_wall_l):
                self.animation = self.walk_l
                self.move_x = -self.speed_walk

        self.frame = 0
        self.caminando = True

    def stay(self):
        '''
        El metodo produce el stay en el player, dejandolo quieto en el lugar.
        '''
        self.caminando = False
        if(self.direction == DIRECTION_R):
            self.animation = self.stay_r
        else:
            self.animation = self.stay_l
        
        self.move_x = 0
        self.frame = 0

    def is_jumpping(self):
        '''
        El metodo verifica si el player está saltando o no.
        '''
        if(self.is_jump):
            if(self.rect.y <= self.limite_jump):
                self.fall()

    def jump(self):  
        '''
        El metodo verifica si estoy saltando o no.
        '''
        if(self.is_on_platform and self.is_jump == False):
            if(self.direction == DIRECTION_R):
                self.animation = self.jump_r
            else:
                self.animation = self.jump_l

            self.move_y = -self.jump_y
            self.frame = 0    
            self.is_fall = False  
            self.is_jump = True
            self.limite_jump = self.rect.y - 150

    def fall(self):
        '''
        El metodo genera el movimiento de caida en caso de que no se encuentre en una plataforma.
        '''
        if(not self.is_on_platform):
            if(self.direction == DIRECTION_R):
                self.animation = self.fall_r 
            else:
                self.animation = self.fall_l
                
            self.is_jump = False
            self.is_fall = True   
            self.frame = 0
            self.move_y = self.gravity

    def on_platform(self,platform_list):
        '''
        
        '''
        self.is_on_platform = False
        for platform in platform_list:
            if(self.rect_ground_collition.colliderect(platform.rect_ground_collition)):
                self.is_on_platform = True
                if(platform.move_l or platform.move_r):
                    if(self.caminando):
                        if(self.direction == DIRECTION_R):
                            if(not self.collision_wall_r):
                                self.move_x = self.speed_walk + platform.move_x
                        else:
                            if(not self.collision_wall_l):
                                self.move_x = -self.speed_walk + platform.move_x
                    else:
                        self.move_x = platform.move_x
                else:
                    self.move_y = platform.move_y
                    self.change_y(self.move_y)
                break
    
    def change_x(self,delta_x):
        '''
        El metodo produce el movimiento de manera horizontal de su rectangulo siguiendo también los rectagunlos generados.
        Recibe la velocidad.
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_collition_bala_r.x += delta_x
        self.rect_collition_l.x += delta_x

    def change_y(self,delta_y):
        '''
        El metodo produce el movimiento de su rectangulo de manera vertical siguiendo también los rectagunlos generados.
        Recibe la velocidad.
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_collition_bala_r.y += delta_y
        self.rect_collition_l.y += delta_y
  
    def colision_live(self,lista_enemigos,lista_trampas):
        '''
        El metodo verifica la colision del enemigo, bala, o plataforma con el player, en caso de producirse el player pierde vida.
        '''
        #_colision con enemigos
        for enemy in lista_enemigos:
            if(self.rect_collition_bala_r.colliderect(enemy.rect_collition_bala_l) or self.rect_collition_l.colliderect(enemy.rect_collition_bala_l)):
                self.animation_frame(self.hit_r)
                self.animation = self.hit_r
                self.hit_sound.set_volume(0.4)
                self.hit_sound.play()
                self.hp -= 7
                self.death()
        for trampa in lista_trampas:
            if(self.collition_rect.colliderect(trampa.collition_rect)):
                self.animation_frame(self.hit_r)
                self.animation = self.hit_r
                self.hit_sound.set_volume(0.4)
                self.hit_sound.play()
                self.hp -= 3
                self.death()    

    def death(self):
        '''
        El player "muere" en caso de que su vida quede en 0
        '''
        if(self.hp <= 0):
            self.live = False
            self.muerte = True
            self.puntos_player = 0

    def is_collision_bala(self):
        '''
        EL metodo verifica si la bala del enemigo colisiona con la del player.
        '''
        if(self.impacto):
            self.hp -= self.damage_generate
            self.impacto = False
            self.animation_frame(self.hit_r)
            self.animation = self.hit_r
            self.death()

    def disparar(self):  ########################
        '''
        El metodo genera las balas y las coloca en posición que quiera.
        '''
        if(self.direction == DIRECTION_R):
            self.lista_proyectiles.generar_balas(5,self.direction,50,20)
        else:
            self.lista_proyectiles.generar_balas(5,self.direction,-45,20)

    def draw(self):
        if(DEBUG):
            pygame.draw.rect(self.screen,color=(255,255,0),rect=self.rect_collition_bala_r)
            pygame.draw.rect(self.screen,color=(255,255,0),rect=self.rect_collition_l)

        if(self.live):
            self.image = self.animation[self.frame]
            self.screen.blit(self.image,self.rect)

    def collision_platform(self,platforms_list):
        '''
        El metodo verifica si mis rectangulos de ambos lados colisiona con una plataforma, para poder dejar el self.move_x en 0.
        Recibe por parametro la lista de plataformas.
        '''
        #_ limite de a donde va a llegar el personaje en el mapa
        self.collision_wall_l = False
        self.collision_wall_r = False
        for platform in platforms_list:
            if(self.rect_collition_l.colliderect(platform.collition_rect)) and not self.collision_wall_l:
                self.move_x = 0
                self.collision_wall_l = True
            if(self.rect_collition_bala_r.colliderect(platform.collition_rect)) and not self.collision_wall_r:
                self.move_x = 0
                self.collision_wall_r = True
                

    def update(self,delta_ms,platform_list,lista_enemigos,lista_eventos,lista_trampas):
        self.tiempo_transcurrido_move += delta_ms
        self.collision_platform(platform_list)
        self.control(lista_eventos)
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
            
            self.is_jumpping()
            self.change_y(self.move_y)
            self.on_platform(platform_list)
            self.change_x(self.move_x)
            self.is_collision_bala()

            if(not self.is_on_platform):
                if(not self.is_jump):
                    self.fall()
            else:
                self.is_fall = False
                self.move_y = 0
                self.is_jump = False 
            self.tiempo_transcurrido_move = 0
        self.colision_live(lista_enemigos,lista_trampas)
        self.lista_proyectiles.update(lista_enemigos)
        self.lista_proyectiles.update(platform_list)

        pygame.draw.rect(self.screen, ROJO, self.collition_rect, 2)
        pygame.draw.rect(self.screen, AQUA, self.rect_ground_collition, 2)
        pygame.draw.rect(self.screen, BLANCO, self.rect_collition_l, 3)
        pygame.draw.rect(self.screen, ROJO, self.rect_collition_bala_r, 2)

        pygame.draw.rect(self.screen, AMARILLO, self.rect, 3)
        
    def control(self,lista_eventos):

        '''
        El metodo verifica las teclas ingresadas y el tiempo de juego.
        '''
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_d):
                    self.walk("R")
                if(event.key == pygame.K_a):
                    self.walk("L")

                if(event.key == pygame.K_SPACE):
                    self.jump()
                if(event.key == pygame.K_l):
                    self.laser_sound.set_volume(0.4)
                    self.laser_sound.play()
                    self.disparar()
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.stay()
                    
                if event.key == pygame.K_a:
                    self.stay()
                    
                if event.key == pygame.K_SPACE:
                    self.fall()
