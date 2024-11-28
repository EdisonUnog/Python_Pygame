import pygame
from pygame.sprite import *
from configuraciones import reescalar_imagenes, obtener_rectangulo

class Personaje:
    def __init__(self, tamaño, animaciones: dict,lista_proyectiles, pos_inicial, velocidad) -> None:
        #_confeccion de personaje
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #gravedad para el salto
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False #por defaul no esta saltando
        #_animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0

        self.lista_disparos = []
        self.lista_proyectiles = lista_proyectiles

        self.direccion = 0


    #_clave._ salta, camina_derecha, camina_izquierda
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    #----------------------------------------------------------------

    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    #----------------------------------------------------------------

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad  #lado = main del dict

    #----------------------------------------------------------------

    def update(self, pantalla, piso):
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
                    self.desplazamiento_y = self.potencia_salto

            case "dispara":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "disparar")
                    if self.direccion == 1:
                        self.animar(pantalla, "disparar")
                    if self.direccion == -1:
                        self.animar(pantalla, "disparar_iz")

            case "quieto":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "quieto")
                    if self.direccion == 1:
                        self.animar(pantalla, "quieto")
                    if self.direccion == -1:
                        self.animar(pantalla, "quieto_iz")
                        
        
        self.aplicar_gravedad(pantalla, piso) #siempre va fuera del match
        

    #----------------------------------------------------------------

    def aplicar_gravedad(self, pantalla, piso): #salto, caida
        #salto
        if self.esta_saltando:
            if self.direccion == 0:
                self.animar(pantalla, "salta")
            if self.direccion == 1:
                self.animar(pantalla, "salta")
            if self.direccion == -1:
                self.animar(pantalla, "salta_iz")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        #caida en el piso pricipal
        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top

    #----------------------------------------------------------------
    def disparar(self, pos_inicial:tuple, direccion):
        miProyectil = Proyectil(self.lista_proyectiles, pos_inicial, direccion)
        self.lista_disparos.append(miProyectil)
    
    #----------------------------------------------------------------
    def kill(self, personaje_list_bala, lista_enemigos):
        for lista in personaje_list_bala.lista_disparos:
            for bala in lista.lados:
                for mi_enemigo in lista_enemigos:
                    if lista.lados[bala].colliderect(mi_enemigo.lados["main"]):
                        personaje_list_bala.lista_disparos.remove(lista)
                        lista_enemigos.remove(mi_enemigo)

###############################################################################

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,lista, pos_inicial:tuple, direccion) -> None:
        pygame.sprite.Sprite.__init__(self)

        #self.imageProyectil = pygame.image.load("Recursos/Proyectiles/1.png")
        self.imageProyectil = lista
        self.reescalar_animaciones()
        self.rect = self.imageProyectil[0].get_rect()

        self.velocidadDisparo = 20
        self.rect.right = pos_inicial[0] +35
        self.rect.top = pos_inicial[1] - 15

        self.indice_img = 0
        self.lados = obtener_rectangulo(self.rect)
        self.trayectoria_balas = direccion
    
    def trayectorio(self):
        if self.trayectoria_balas == 0:
            self.rect.right = self.rect.right + self.velocidadDisparo
        if self.trayectoria_balas == 1:
            self.rect.right = self.rect.right + self.velocidadDisparo

        if self.trayectoria_balas == -1:
            self.rect.right = self.rect.right - self.velocidadDisparo
    
    def dibujar(self, pantalla):
        pantalla.blit(self.imageProyectil[self.indice_img], (self.rect.x, self.rect.y))
        self.indice_img = (self.indice_img + 1) % len(self.imageProyectil)

    def reescalar_animaciones(self):
        for i in range(len(self.imageProyectil)):
            self.imageProyectil[i] = pygame.transform.scale(self.imageProyectil[i], (20,20))


class Enemigo:
    def __init__(self, tamaño, lista: dict, pos_inicial, velocidad) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #_animaciones
        self.enemigo = lista
        self.reescalar_animaciones()
        self.direccion = "derecha"

        #RECTANGULOS
        self.rectangulo = self.enemigo["derecha"][0].get_rect()
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        #movimiento_IMG
        self.movimiento = 0
        self.velocidad = velocidad

        #sonido enemigo
        #self.sound_enemigo = pygame.mixer.Sound("sonidos/soundEnemigo.wav")

    def reescalar_animaciones(self):
        for clave in self.enemigo:
            reescalar_imagenes(self.enemigo[clave], (self.ancho, self.alto))

    def animar_enemigo(self, pantalla, direccion):
        animar = self.enemigo[direccion]
        largo = len(animar)

        if self.movimiento >= largo:
            self.movimiento = 0

        pantalla.blit(animar[self.movimiento], self.lados["main"])
        self.movimiento += 1
        
    def mover(self, velocidad):
        for lado in self.lados: 
            self.lados[lado].x += velocidad

    def update(self, pantalla): ###
        match self.direccion:
            case "derecha":
                self.animar_enemigo(pantalla, "derecha")
                self.mover(self.velocidad)

            case "izquierda":
                self.animar_enemigo(pantalla, "izquierda")
                self.mover(self.velocidad * -1)

    def mover_y(self, velocidad):
        for lado in self.lados: 
            self.lados[lado].y += velocidad