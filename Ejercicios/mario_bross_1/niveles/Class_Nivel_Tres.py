import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_Plataformas import*
from niveles.Class_Monedas import*
from niveles.Class_Enemigo import*
from niveles.configuraciones import*
from niveles.diccionario import*
from niveles.modo import*
from niveles.nivel import*

class NivelTres(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        #_Fondo
        fondo = pygame.image.load("Recursos/fondo_3.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        #_Personaje
        mi_personaje = Personaje((65, 85), diccionario_persona, (ALTO/2 - 350, 710), 10)

        ############################################
        #___Plataforma
        mis_plataformas = [Plataforma((ANCHO, 5), piso2 ,(0, mi_personaje.lados["main"].bottom)),
                            Plataforma((55, 45), plataformas_img[0], (400, 680)),
                            Plataforma((55, 45), plataformas_img[0], (250, 570)),
                            Plataforma((150, 45), plataformas_img[1], (50, 460)),
                            Plataforma((55, 45), plataformas_img[0], (250, 350)),
                            Plataforma((55, 45), plataformas_img[0], (150, 250)), #
                            Plataforma((225, 45), plataformas_img[2], (300, 140)),
                            Plataforma((55, 45), plataformas_img[0], (600, 570)), #
                            Plataforma((450, 45), plataformas_img[3], (700, 460)),
                            Plataforma((55, 45), plataformas_img[0], (1190, 350)),
                            Plataforma((55, 45), plataformas_img[0], (1260, 240)),
                            Plataforma((55, 45), plataformas_img[0], (1350, 240)),
                            Plataforma((150, 45), plataformas_img[1], (1500, 120))]
        
        lista_monedas = [Monedas((25, 25), mis_monedas, (550, 750)),##
                        Monedas((25, 25), mis_monedas, (590, 750)),
                        Monedas((25, 25), mis_monedas, (630, 750)),##
                        Monedas((25, 25), mis_monedas, (415, 650)),
                        Monedas((25, 25), mis_monedas, (265, 540)),
                        Monedas((25, 25), mis_monedas, (165, 220)),
                        Monedas((25, 25), mis_monedas, (615, 540)),

                        Monedas((25, 25), mis_monedas, (470, 100)),
                        Monedas((25, 25), mis_monedas, (430, 100)),
                        Monedas((25, 25), mis_monedas, (390, 100)),                        
                        Monedas((25, 25), mis_monedas, (350, 100)),

                        Monedas((25, 25), mis_monedas, (920, 430)),#
                        Monedas((25, 25), mis_monedas, (965, 430)),
                        Monedas((25, 25), mis_monedas, (1010, 430)),
                        Monedas((25, 25), mis_monedas, (1055, 430)),
                        Monedas((25, 25), mis_monedas, (1205, 320)),
                        Monedas((25, 25), mis_monedas, (1275, 210)),
                        
                        Monedas((25, 25), mis_monedas, (1350,660)),
                        Monedas((25, 25), mis_monedas, (1400,650)),
                        Monedas((25, 25), mis_monedas, (1450,640)),
                        Monedas((25, 25), mis_monedas, (1500,650)),
                        Monedas((25, 25), mis_monedas, (1550,660))] #
        
        lista_enemigos = [Enemigo((50, 50), diccionario_enemigo, (1200, 740), 5),
                            Enemigo((50, 50), diccionario_enemigo, (300, 740), 5),
                            Enemigo((50, 50), diccionario_enemigo, (310, 85), 5)]
                
        super().__init__(pantalla, mi_personaje, mis_plataformas, lista_monedas, lista_enemigos, self.ubicar, fondo)

    def ubicar(self, lista, ancho):
        if lista[0].rectangulo.x < ancho - 430:
            lista[0].direccion = "derecha"
        elif lista[0].rectangulo.x > ancho - 100:
            lista[0].direccion = "izquierda"

        if lista[1].rectangulo.x < ancho - 1400:
            lista[1].direccion = "derecha"
        elif lista[1].rectangulo.x > ancho - 1000:
            lista[1].direccion = "izquierda"
                    
        if lista[2].rectangulo.x < ancho - 1390:
            lista[2].direccion = "derecha"
        elif lista[2].rectangulo.x > ancho - 1240:
            lista[2].direccion = "izquierda"
    