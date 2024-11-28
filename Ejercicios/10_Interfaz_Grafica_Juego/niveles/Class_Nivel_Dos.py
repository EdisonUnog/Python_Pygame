import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_monedas import*
from niveles.configuraciones import*
from niveles.Diccionarios import*
from niveles.modo import*
from niveles.nivel import*

class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("niveles/fondo_space.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        #_Personaje ANCHO - 300
        mi_personaje = Personaje((75, 85) , diccionario_personaje, (ALTO/2 - 300, 650), 10)
        
        ############################################
        #___Plataforma
        mis_plataformas = [Plataforma((ANCHO - 40, 20), piso_dos ,(20, mi_personaje.lados["main"].bottom)), #piso
                            Plataforma((400, 75),   plataforma_dos, (500, 620)),
                            Plataforma((300, 75), plataforma_dos, (1000, 500)),
                            Plataforma((200, 55), plataforma_dos, (200, 500)),
                            Plataforma((200, 55), plataforma_dos, (700, 300)),
                            Plataforma((150, 40), plataforma_dos, (500, 400))]
        
        super().__init__(pantalla, mi_personaje, mis_plataformas, fondo)

    def nombre_nivel(self, pantalla):
        fuente = pygame.font.SysFont("Arail", 25)
        texto = fuente.render("Nivel Dos", True, Colores.VERDE)
        texto_rect = texto.get_rect() #obtengo rectangulo para posiscionar el texto
        texto_rect.topleft = (5,5)
        pantalla.blit(texto, texto_rect)
