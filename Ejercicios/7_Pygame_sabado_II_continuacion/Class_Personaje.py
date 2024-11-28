import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulo
from Diccionarios import *

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Personaje:
    def __init__(self, tamaño, animaciones: dict, pos_inicial, velocidad) -> None:
        #_confeccion de personaje
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #gravedad para el salto
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False #por defaul no esta saltando
        self.un_salto = True
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

        self.direccion = 0


    '''def update(self):
        self.rect.x += 10'''

    #----------------------------------------------------------------

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
                    self.animar(pantalla, "camina_iz")
                self.mover(self.velocidad * -1)

            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto

            case "dispara":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "dispara")
                    if self.direccion == 1:
                        self.animar(pantalla, "dispara")
                    if self.direccion == -1:
                        self.animar(pantalla, "dispara_iz")

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

    def aplicar_gravedad(self, pantalla, lista_plataformas: pygame.rect): #salto, caida
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
        self.un_salto = True

        for piso in lista_plataformas:
            if self.lados["bottom"].colliderect(piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.un_salto = False
                self.lados["main"].bottom = piso["main"].top + 5   
                break
            else:
                self.esta_saltando =True


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Plataforma:
    def __init__(self, tamaño, plataforma, pos_inicial) -> None:

        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.animaciones = plataforma
        self.animaciones = pygame.transform.scale(self.animaciones, (self.ancho, self. alto))

        self.rectangulo = self.animaciones.get_rect() #rectangulo de la imagen
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
    
def update_plataformas(pantalla, mis_plataformas):
    for i in range(len(mis_plataformas)):
        pantalla.blit(mis_plataformas[i].animaciones, mis_plataformas[i].rectangulo)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::