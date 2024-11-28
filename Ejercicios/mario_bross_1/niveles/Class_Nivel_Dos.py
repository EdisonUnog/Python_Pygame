import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_Plataformas import*
from niveles.Class_Monedas import*
from niveles.Class_Enemigo import*
from niveles.configuraciones import*
from niveles.diccionario import*
from niveles.modo import*
from niveles.nivel import*

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        #_Fondo
        fondo = pygame.image.load("Recursos/fondo_2.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        #_Personaje
        mi_personaje = Personaje((65, 85), diccionario_persona, (ALTO/2 - 350, 710), 10)

        ############################################
        #___Plataforma
        mis_plataformas = [Plataforma((ANCHO, 5), piso2 ,(0, mi_personaje.lados["main"].bottom)),
                            Plataforma((55, 45), plataformas_img[0], (200, 680)),
                            Plataforma((55, 45), plataformas_img[0], (150, 570)),
                            Plataforma((450, 45), plataformas_img[3], (270, 460)),
                            Plataforma((55, 45), plataformas_img[0], (150, 350)),
                            Plataforma((225, 45), plataformas_img[2], (250, 240)),
                            Plataforma((55, 45), plataformas_img[0], (700, 180)),
                            Plataforma((55, 45), plataformas_img[0], (45, 130)),
                            Plataforma((55, 45), plataformas_img[0], (105, 130)),
                            Plataforma((55, 45), plataformas_img[0], (165, 130)),
                            Plataforma((55, 45), plataformas_img[0], (850, 680)),
                            Plataforma((55, 45), plataformas_img[0], (1050, 680)),
                            Plataforma((55, 45), plataformas_img[0], (950, 570)),
                            Plataforma((225, 45), plataformas_img[2], (850, 300)),
                            Plataforma((55, 45), plataformas_img[0], (1120, 200)), #
                            Plataforma((55, 45), plataformas_img[0], (1240, 200)),
                            Plataforma((55, 45), plataformas_img[0], (1360, 200)),
                            Plataforma((55, 45), plataformas_img[0], (1560, 100))]
        
        lista_monedas = [Monedas((25, 25), mis_monedas, (215, 650)),
                        Monedas((25, 25), mis_monedas, (165, 540)),
                        Monedas((25, 25), mis_monedas, (440, 420)),##
                        Monedas((25, 25), mis_monedas, (485, 420)),
                        Monedas((25, 25), mis_monedas, (530, 420)),##

                        Monedas((25, 25), mis_monedas, (185, 100)),
                        Monedas((25, 25), mis_monedas, (145, 100)),
                        Monedas((25, 25), mis_monedas, (110, 100)),                        
                        Monedas((25, 25), mis_monedas, (70, 100)),

                        Monedas((25, 25), mis_monedas, (1045, 410)),#
                        Monedas((25, 25), mis_monedas, (1090, 410)),
                        Monedas((25, 25), mis_monedas, (1135, 410)),

                        Monedas((25, 25), mis_monedas, (715, 150)),#

                        Monedas((25, 25), mis_monedas, (1135, 170)),#
                        Monedas((25, 25), mis_monedas, (1255, 170)),
                        Monedas((25, 25), mis_monedas, (1375, 170)),

                        Monedas((25, 25), mis_monedas, (865, 650)),] #
        
        lista_enemigos = [Enemigo((50, 50), diccionario_enemigo, (840, 740), 5),
                            Enemigo((50, 50), diccionario_enemigo, (270, 410), 5),
                            Enemigo((50, 50), diccionario_enemigo, (45, 80), 5)]
                
        super().__init__(pantalla, mi_personaje, mis_plataformas, lista_monedas, lista_enemigos, self.ubicar, fondo)

    def ubicar(self, lista, ancho):
        if lista[0].rectangulo.x < ancho - 1000: #izzquierda 
            lista[0].direccion = "derecha"
        elif lista[0].rectangulo.x > ancho - 600:
            lista[0].direccion = "izquierda"

        if lista[1].rectangulo.x < ancho - 1430: #izzquierda 
            lista[1].direccion = "derecha"
        elif lista[1].rectangulo.x > ancho - 1050:
            lista[1].direccion = "izquierda"
                    
        if lista[2].rectangulo.x < ancho - 1655: #izzquierda 
            lista[2].direccion = "derecha"
        elif lista[2].rectangulo.x > ancho - 1550:
            lista[2].direccion = "izquierda"