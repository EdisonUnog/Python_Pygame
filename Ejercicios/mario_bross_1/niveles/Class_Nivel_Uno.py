import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_Plataformas import*
from niveles.Class_Monedas import*
from niveles.Class_Enemigo import*
from niveles.configuraciones import*
from niveles.diccionario import*
from niveles.modo import*
from niveles.nivel import*

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()


        #_Fondo
        fondo = pygame.image.load("Recursos/fondo_1.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        #_Personaje
        mi_personaje = Personaje((65, 85), diccionario_persona, (ALTO/2 - 350, 710), 10)

        self.cont = mi_personaje.contador_monedas

        ############################################
        #___Plataforma                 tamaño      path               posicion
        mis_plataformas = [Plataforma((ANCHO, 5), piso1 ,(0, mi_personaje.lados["main"].bottom)),
                            Plataforma((150, 45), plataformas_img[1], (250, 680)),
                            Plataforma((55, 45), plataformas_img[0], (170, 570)), 
                            Plataforma((55, 45), plataformas_img[0], (290, 450)),
                            Plataforma((55, 45), plataformas_img[0], (470, 450)),
                            Plataforma((55, 45), plataformas_img[0], (670, 450)),
                            
                            Plataforma((55, 45), plataformas_img[0], (770, 330)),
                            Plataforma((55, 45), plataformas_img[0], (610, 230)),
                            Plataforma((450, 45), plataformas_img[3], (30, 130)),
                            Plataforma((225, 45), plataformas_img[2], (950, 540)),
                            Plataforma((55, 45), plataformas_img[0], (1200, 420)),
                            Plataforma((55, 45), plataformas_img[0], (1300, 300)),
                            Plataforma((150, 45), plataformas_img[1], (1100, 200)),###
                            
                            Plataforma((150, 110), plataformas_img[4], (1490, 30)),
                            Plataforma((250, 45), plataformas_img[2], (1440, 140))]

        lista_monedas = [Monedas((25, 25), mis_monedas, (295, 650)), 
                        Monedas((25, 25), mis_monedas, (330, 650)),
                        Monedas((25, 25), mis_monedas, (185, 540)),
                        Monedas((25, 25), mis_monedas, (305, 420)),
                        Monedas((25, 25), mis_monedas, (485, 420)),
                        Monedas((25, 25), mis_monedas, (685, 420)),
                        Monedas((25, 25), mis_monedas, (185, 100)),
                        Monedas((25, 25), mis_monedas, (145, 100)),
                        Monedas((25, 25), mis_monedas, (110, 100)),
                        Monedas((25, 25), mis_monedas, (70, 100)),
                        Monedas((25, 25), mis_monedas, (1045, 510)),
                        Monedas((25, 25), mis_monedas, (1090, 510)),
                        Monedas((25, 25), mis_monedas, (1135, 510)),
                        Monedas((25, 25), mis_monedas, (1215, 390)),
                        Monedas((25, 25), mis_monedas, (1200, 170)),
                        Monedas((25, 25), mis_monedas, (1165, 170)),
                        Monedas((25, 25), mis_monedas, (1125, 170)),

                        Monedas((25, 25), mis_monedas, (1490, 680)),
                        Monedas((25, 25), mis_monedas, (1535, 680)),
                        Monedas((25, 25), mis_monedas, (1580, 680))]
        
        lista_enemigos = [Enemigo((50, 50), diccionario_enemigo, (1200, 740), 5),
                            Enemigo((50, 50), diccionario_enemigo, (970, 490), 5),
                            Enemigo((50, 50), diccionario_enemigo, (50, 80), 5)]

                
        super().__init__(pantalla, mi_personaje, mis_plataformas, lista_monedas, lista_enemigos, self.ubicar, fondo)

    def ubicar(self, lista, ancho):
        if lista[0].rectangulo.x < ancho - 430:
            lista[0].direccion = "derecha"
        elif lista[0].rectangulo.x > ancho - 100:
            lista[0].direccion = "izquierda"

        if lista[1].rectangulo.x < ancho - 700:
            lista[1].direccion = "derecha"
        elif lista[1].rectangulo.x > ancho - 600:
            lista[1].direccion = "izquierda"
                    
        if lista[2].rectangulo.x < ancho - 1650:
            lista[2].direccion = "derecha"
        elif lista[2].rectangulo.x > ancho - 1300:
            lista[2].direccion = "izquierda"





