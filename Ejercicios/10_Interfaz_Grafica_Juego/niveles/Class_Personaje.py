import pygame
from niveles.Class_Colores import *
from niveles.configuraciones import reescalar_imagenes, obtener_rectangulo

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

    def update(self, pantalla, lista_plataformas):
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

            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")
        
        self.aplicar_gravedad(pantalla, lista_plataformas) #siempre va fuera del match
        

    #----------------------------------------------------------------

    def aplicar_gravedad(self, pantalla, lista_plataformas): #salto, caida
        #salto
        if self.esta_saltando:
            self.animar(pantalla, "salta")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        #caida en el piso pricipal

        for piso in lista_plataformas:                 
            if self.lados["bottom"].colliderect(piso.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = piso.lados["main"].top + 5   
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
    
    def update_plataformas(self, pantalla):
            pantalla.blit(self.animaciones, self.lados["main"])

    def draw(self, pantalla):
        #pygame.draw.rect(pantalla, Colores.ROJO, (self.rectangulo.x ,self.rectangulo.y, self.ancho, self.alto), 3)
        pantalla.blit(self.animaciones, self.lados["main"])




