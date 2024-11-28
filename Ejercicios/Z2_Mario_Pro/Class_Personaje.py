import pygame, sys
from configuraciones import *
#================================================================================================
class Personaje:
    def __init__(self, tamaño:tuple, animaciones:dict, pos_inicial:tuple, velocidad:int) -> None:
        #CONFECCION ANCHO ALTO
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        #_Gravedad para saltar y caer
        self.gravedad = 1 #velocidad de caida
        self.potencia_salto = -15 #cuanto salta
        self.limite_velocidad_caida = 15 #cuanto cae
        self.esta_saltando = False # por defaul no esta saltando

        #_para las animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones #dict de imagenes
        self.reescalar_animaciones()

        #_obtengo rectangulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect() #obtengo rect del personaje
        self.rectangulo.x = pos_inicial[0]
        self.rectangulo.y = pos_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo) # creo rect asociados en el rect del personaje

        #_movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0

    #==================================================================================
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    #==================================================================================
    def animar(self, pantalla, que_animacion: str): #anima las imagenes recorriendo la lista, animacion generia para el momento
        animacion = self.animaciones[que_animacion]
        largo = len(animacion) #no se pase de largo en la lista, cuando termina empieza de vuelta con la animacion
        
        if self.contador_pasos >= largo: # cont_pasos._ atributo de la clase
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    #==================================================================================
    def mover(self, velocidad): # derecha izquierda
        for lado in self.lados: # esta funcion va en update__ derecha: velocidad, izquierda: velocidad *-1
            self.lados[lado].x += velocidad # fuera del for, solo mueve el rect principal

    #==================================================================================
    def update(self, pantalla,lados_piso, lista_plataformas_lados): # lo demas lo saca del objeto class
        
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

            case "agachar":
                if not self.esta_saltando:
                    self.animar(pantalla, "abajo")
        
        self.aplicar_gravedad(pantalla,lados_piso, lista_plataformas_lados)

    #==================================================================================
    def aplicar_gravedad(self, pantalla,lados_piso , lista_plataformas_lados): # salto, caida en el piso principal o las plataformas
        #_SALTO
        if self.esta_saltando:
            self.animar(pantalla, "salta")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            #_CAIDA
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        #......
        #caida en el piso pricipal

        for piso in lista_plataformas_lados:
            if self.lados["bottom"].colliderect(lados_piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = lados_piso["main"].top + 5   
                
            elif self.lados["bottom"].colliderect(piso.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = piso.lados["main"].top + 5   
                break
            else:
                self.esta_saltando =True

        #elif con el lados de las plataformas
        #mismo metodo

    def meta(self, pantalla):
        pass
