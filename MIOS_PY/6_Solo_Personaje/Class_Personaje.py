import pygame, sys
from Constantes import*
from Class_Lista_Proyectil import*
from Class_Auxiliar import*
from configuraciones import reescalar_imagenes, obtener_rectangulo

class Personaje:
    def __init__(self, pantalla, tamaño, pos_inicial, velocidad) -> None:
        #_confeccion de personaje
        self.tiempo_transcurrido = 0
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #_PERSONAJE _Dict
        self.dict_persona = {}
        self.dict_persona["quieto"] = Auxiliar.cargarImagen("Recursos/Personaje/Quieto/{0}.png",4, False,1, self.ancho, self.alto)
        self.dict_persona["quieto_iz"] = Auxiliar.cargarImagen("Recursos/Personaje/Quieto/{0}.png",4, True,1, self.ancho, self.alto)
        self.dict_persona["camina_derecha"] = Auxiliar.cargarImagen("Recursos/Personaje/Camina/{0}.png",4, False,1, self.ancho, self.alto)
        self.dict_persona["camina_izquierda"] = Auxiliar.cargarImagen("Recursos/Personaje/Camina/{0}.png",4, True,1, self.ancho, self.alto)
        self.dict_persona["salta"] = Auxiliar.cargarImagen("Recursos/Personaje/Salta/{0}.png",1, False,1, self.ancho, self.alto)
        self.dict_persona["salta_iz"] = Auxiliar.cargarImagen("Recursos/Personaje/Salta/{0}.png",1, True,1, self.ancho, self.alto)
        #gravedad para el salto
        self.gravedad = 1 #velocidad de caida
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False #por defaul no esta saltando
        self.un_salto = True 

        #_animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = self.dict_persona
        #self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        #_lados a donde va a colisionar
        self.rect_principal = self.lados["main"]
        self.collision_rect_top = self.lados["top"]
        self.collision_rect_bottom = self.lados["bottom"]
        self.collision_rect_right = self.lados["right"]
        self.collision_rect_left = self.lados["left"]
        self.collision_l = False
        self.collision_r = False
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.desplazamiento_x = 0

        self.mover_x = 0
        self.mover_y = 0

        #_unbicacion del personaje
        self.direccion = 0

        #_condiciones para sabes si muere
        self.hp = 100
        self.muerte = False
        self.live = True 
        self.caminando = False

        #_Score
        self.puntos_player = 0

        #_Dispara
        self.lista_proyectiles = ListaProyectil(pantalla, self.rectangulo, "Recursos/bala/Bullet.png", self)
        #sonidos
        self.laser_sound = pygame.mixer.Sound("Recursos/music/laser5.ogg")

    #----------------------------------------------------------------

    #_clave._ salta, camina_derecha, camina_izquierda
    # def reescalar_animaciones(self):
    #     for clave in self.animaciones:
    #         reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    #----------------------------------------------------------------
    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

    #----------------------------------------------------------------
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad  #lado = main del dict

    #----------------------------------------------------------------

    def update(self, pantalla, lista_piso):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.mover_x)


            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.mover_x * -1)

            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto

            case "quieto":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "quieto")
                    else:
                        self.animar(pantalla, "quieto_iz")


        self.leer_inputs()
        self.aplicar_gravedad(pantalla, lista_piso) #siempre va fuera del match
        #self.pared(lista_piso)
            
        self.lista_proyectiles.update(lista_piso)
            
    #----------------------------------------------------------------
    def aplicar_gravedad(self, pantalla, lista_objetos): #salto, caida
        #salto
        if self.esta_saltando:
            if self.direccion == 0:
                self.animar(pantalla, "salta")
            else:
                self.animar(pantalla, "salta_iz")

        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y

        if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad
        
        self.un_salto = True
        self.esta_saltando = False

        #caida en el piso pricipal

        for objeto in lista_objetos:
            if self.collision_rect_bottom.colliderect(objeto.collision_rect_top):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.un_salto = False
                self.rect_principal.bottom = objeto.rect_principal.top 
                break
            #_Collision techo
            elif self.collision_rect_top.colliderect(objeto.collision_rect_bottom):
                self.desplazamiento_y = self.velocidad 
                self.desplazamiento_y += self.gravedad
                self.esta_saltando = False
                self.un_salto = False
                break
            else:
                self.esta_saltando = True
                self.un_salto = True

        self.collision_l = False
        self.collision_r = False

        #_Collision paredes 
        for objeto in lista_objetos:
            if (self.collision_rect_left.colliderect(objeto.collition_rect)) and not self.collision_l:
                self.rect_principal.x += self.velocidad
                self.collision_rect_top.x += self.velocidad
                self.collision_rect_bottom.x += self.velocidad
                self.collision_rect_right.x += self.velocidad
                self.collision_rect_left.x += self.velocidad
                self.collision_l = True
                print("collision left")
                break
                    
            if (self.collision_rect_right.colliderect(objeto.collition_rect)) and not self.collision_r:
                self.rect_principal.x -= self.velocidad
                self.collision_rect_top.x -= self.velocidad
                self.collision_rect_bottom.x -= self.velocidad
                self.collision_rect_right.x -= self.velocidad
                self.collision_rect_left.x -= self.velocidad
                self.collision_r = True
                print("collisicion right")
                break
                
            self.collision_l = False
            self.collision_r = False

    #----------------------------------------------------------------
    def camina(self, direccion):
        self.direccion = direccion
        if(self.direccion == 0):
            if(not self.collision_r):
                self.que_hace = "derecha"
                self.mover_x = self.velocidad
        else:
            if(not self.collision_l):
                self.que_hace = "izquierda"
                self.mover_x = self.velocidad

        self.caminando = True

    #----------------------------------------------------------------
                
    def pared(self, lista_objetos):

        pass

    #----------------------------------------------------------------                 
    def disparar(self):
        #:genero las balas a la direccion que marca
        if(self.direccion == 0):
            self.lista_proyectiles.generar_balas(20, self.direccion, 50, 15, 30, 30)
        else:
            self.lista_proyectiles.generar_balas(20, self.direccion, -10, 15, 30, 30)

    #----------------------------------------------------------------           
    def death(self):
        '''
        El player "muere" en caso de que su vida quede en 0
        '''
        if(self.hp <= 0):
            self.live = False
            self.muerte = True
            self.puntos_player = 0 
    
    #----------------------------------------------------------------
    def leer_inputs(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.un_salto == False:
            self.que_hace = "salta"

        elif keys[pygame.K_l]:
            self.laser_sound.set_volume(0.4)
            self.laser_sound.play()
            self.disparar()
        
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.camina(0)

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.camina(1)

        else:
            self.que_hace = "quieto"

        if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            False

        if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)