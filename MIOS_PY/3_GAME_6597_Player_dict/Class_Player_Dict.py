import pygame
from Class_Colores import*
from Class_Proyectil import*
from configuraciones import*

class Player():
    def __init__(self, x, y, w, h, animacion:dict, velocidad, alto) -> None:
        
        self.alto_p = alto

        self.ancho = w
        self.alto = h

        #animacion 
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animacion
        self.reescalar_animaciones()

        #rectangulos
        self.rect = self.animaciones["camina_derecha"][0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lados = obtener_rectangulo(self.rect)

        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0

        #gravedad de salto
        self.gravedad = 1
        self.salto = -13
        self.caida_salto = 13
        self.esta_saltando = False # por defecto no esta saltando
        self.un_salto = True

        self.direccion = 0
        
        #lista de proyectiles
        self.lista_disparos = []
        self.disparando = False
        self.velocidad_disparos = 10

    #----------------------------------------------------------------
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_img(self.animaciones[clave], (self.ancho, self.alto))

    #----------------------------------------------------------------
    def animar(self, panatalla, que_anima: str):
        animacion = self.animaciones[que_anima]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        panatalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    #----------------------------------------------------------------
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    #----------------------------------------------------------------
    def teclas(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.un_salto == False:
            self.que_hace = "salta"

        elif keys[pygame.K_d]:
            self.que_hace = "derecha"
            self.direccion = 1

        elif keys[pygame.K_a]:
            self.que_hace = "izquierda"
            self.direccion = -1 
        
        elif keys[pygame.K_l]:
            self.que_hace = "dispara"
            x, y = self.rect.center
            self.disparos(x, y, self.direccion, self.velocidad_disparos)
            self.disparando = True

        else:
            self.que_hace = "quieto"

        if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            False

    #----------------------------------------------------------------
    def update(self, pantalla, mundo, jugador):
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
                    self.desplazamiento_y = self.salto

            case "dispara":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "dispara")
                    if self.direccion == 1:
                        self.animar(pantalla, "dispara")
                    if self.direccion == -1:
                        self.animar(pantalla, "dispara_iz")
                #self.mover(self.velocidad)

            case "quieto":
                if not self.esta_saltando:
                    if self.direccion == 0:
                        self.animar(pantalla, "quieto")
                    if self.direccion == 1:
                        self.animar(pantalla, "quieto")
                    if self.direccion == -1:
                        self.animar(pantalla, "quieto_iz")


        self.teclas()
        self.cantidad_disparos(pantalla, jugador)
        self.aplicar_gravedad(pantalla, mundo)

    #----------------------------------------------------------------
    def aplicar_gravedad(self, pantalla, mundo): #salto, caida
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

            if self.desplazamiento_y + self.gravedad < self.caida_salto:
                self.desplazamiento_y += self.gravedad       

        self.un_salto = True

        for linea in mundo.bloque_lista:
            lados_piso = obtener_rectangulo(linea[1])
            if self.lados["bottom"].colliderect(lados_piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.un_salto = False
                self.lados["main"].bottom = lados_piso["main"].top
                break

            else:
                self.esta_saltando = True


    def disparos(self, x, y, direccion, velocidad):
        mi_proyectil = Proyectil(x, y, lista_proyectiles, direccion, velocidad)
        self.lista_disparos.append(mi_proyectil)

    def cantidad_disparos(self, pantalla, jugador):
        if len(jugador.lista_disparos) > 0:
            for x in jugador.lista_disparos:
                x.update(pantalla)
                x.mover()

                if x.rect.x < 10:
                    jugador.lista_disparos.remove(x)

