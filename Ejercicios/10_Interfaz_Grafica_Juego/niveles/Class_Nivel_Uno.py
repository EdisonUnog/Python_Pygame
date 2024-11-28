import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_monedas import*
from niveles.configuraciones import*
from niveles.Diccionarios import*
from niveles.modo import*
from niveles.nivel import*

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        
        self.nombre_nivel(pantalla)
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("niveles/fondo_space.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        #_Personaje
        mi_personaje = Personaje((75, 85) , diccionario_personaje, (ALTO/2 - 300, 650), 10)

        ############################################
        #___Plataforma
        mis_plataformas = [Plataforma((ANCHO - 40, 20), piso,(20, mi_personaje.lados["main"].bottom)), #piso
                            Plataforma((400, 75),    plataforma_uno, (500, 620)),
                            Plataforma((300, 75), plataforma_uno, (1000, 500)),
                            Plataforma((200, 55), plataforma_uno, (200, 500)),
                            Plataforma((200, 55), plataforma_uno, (700, 300)),
                            Plataforma((150, 40), plataforma_uno, (500, 400))]
                
        super().__init__(pantalla, mi_personaje, mis_plataformas, fondo)


    def nombre_nivel(self, pantalla):
        fuente = pygame.font.SysFont("Arail", 25)
        texto = fuente.render("Nivel Uno", True, Colores.VERDE)
        texto_rect = texto.get_rect() #obtengo rectangulo para posiscionar el texto
        texto_rect.topleft = (5,5)
        pantalla.blit(texto, texto_rect)
