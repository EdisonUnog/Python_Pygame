import pygame, sys
from niveles.Configuraciones import*
from niveles.Diccionarios import*
from niveles.Class_Colores import* 
from niveles.Class_Vida import*

#================================================================================================
class Personaje:
    def __init__(self, tamanio:tuple, pos_inicial:tuple, velocidad, anchoP, altoP) -> None:
        #_Configuracion ancho alto
        self.ancho = tamanio[0]
        self.alto = tamanio[1]

        self.ancho_panatalla = anchoP
        self.alto_pantalla = altoP 

        #_Gravedad Personaje Salta
        self.gravedad = 1 #velocidad Caida
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.un_salto = False 

        #_Animaciones Personaje
        self.contador_pasos = 0
        self.que_hace = "quieto_der"
        self.animaciones = dict_Personaje # dict personaje
        self.reescalar_imagenes()

        #_Obtener Rectangulos y Lados
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect() 
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)

        #_Movimientos
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.direccion = 0

        self.hp = 100
        self.puntos_player = 0
        self.muerte = False
        self.live = True  

    def reescalar_imagenes(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_anima:str):
        animacion = self.animaciones[que_anima]
        largo = len(animacion)

        if(self.contador_pasos >= largo):
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, lista_pisos, lista_plataformas, lista_trampas):

        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)

            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * -1)

            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    #self.un_salto = True
                    self.desplazamiento_y = self.potencia_salto

            case "dispara":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "dispara_der")
                    else:
                        self.animar(pantalla, "dispara_izq")

            case "quieto":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "quieto_der")
                    else:
                        self.animar(pantalla, "quieto_izq") 
            
            case "agachar":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "agachado_der")
                    else:
                        self.animar(pantalla, "agachado_izq")

        self.aplicar_gravedad(pantalla, lista_pisos, lista_plataformas, lista_trampas)
        self.leer_inputs()
        self.colision_trampa(lista_trampas)  
 
    def colision_trampa(self, lista_trampas):
        for trampa in lista_trampas:
            if(self.lados["main"].colliderect(trampa.lados["main"])):
                print("print")
                self.hp -= 7
                self.death()

    def death(self):
        '''
        El player "muere" en caso de que su vida quede en 0
        '''
        if(self.hp <= 0):
            self.live = False
            self.muerte = True
            self.puntos_player = 0  

    def aplicar_gravedad(self, pantalla, lista_pisos, lista_plataformas, lista_trampas):
        #_Salto
        if self.esta_saltando:
            if self.direccion == 0:
                self.animar(pantalla, "salta_der")
            else:
                self.animar(pantalla, "salta_izq")

        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y
        
        #_Caida
        if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad

        #.....
        #_Caida en el piso
        self.un_salto = True

        for piso in lista_pisos:
            if self.lados["bottom"].colliderect(piso.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.un_salto = False
                self.lados["main"].bottom = piso.lados["main"].top + 5
                break
            else:
                self.esta_saltando = True

        for plat in lista_plataformas:
            if self.lados["bottom"].colliderect(plat.lados["top"]):
                self.desplazamiento_y = plat.move_y
                self.esta_saltando = False
                self.un_salto = False
                self.lados["main"].bottom = plat.lados["main"].top + 5
                break
            else:
                self.esta_saltando = False

    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.un_salto == False:
            self.que_hace = "salta"
        
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.que_hace = "derecha"
            self.direccion = 0

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.que_hace = "izquierda"
            self.direccion = 1

        elif keys[pygame.K_l] and self.un_salto == False:
            self.que_hace = "dispara"

        elif keys[pygame.K_s] and self.un_salto == False:
            self.que_hace = "agachar"

        else:
            self.que_hace = "quieto"

        if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            False


        if keys[pygame.K_l] == False:
            self.disparando = False


        # if keys[pygame.K_ESCAPE]:
        #         pygame.quit()
        #         sys.exit(0)