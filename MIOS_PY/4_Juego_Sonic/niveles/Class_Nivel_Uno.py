import pygame
from niveles.Class_Personaje import*
from niveles.Configuraciones import*
from niveles.Class_Plataformas import*
from niveles.Class_Piso import*
from niveles.Nivel import*
from niveles.Class_Monedas import*
from niveles.Class_Trampas import*

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("Recursos/Materiales/Fondos/fondo_level_1.png")
        fondo = pygame.transform.scale(fondo,(ANCHO,ALTO))#Tranformamos la imagen

        sonic = Personaje((60, 80), (20, ALTO - 200), 15, ANCHO, ALTO)
        
        mis_plat = [Plataforma(300,600,65,20,7,50,200,700,7,5,300, 0),
                    Plataforma(500,450,850,30,0,50,0,0,0,4,0)]

        mis_pisos = [Pisos((1700, 100), 0, (0, ALTO - 100))]
        
        mis_monedas = [Monedas((20,20),(600,410)),
                        Monedas((20,20),(633,410))]
        
        mis_trampas = [Trampas((45,45),(400,650), 5, 1100, 900)]

        super().__init__(pantalla,sonic, mis_pisos, mis_monedas, mis_plat, mis_trampas, fondo)


# Plataforma(500,271,850,30,0,50,0,0,0,4,0)
# Plataforma(950,147,500,30,0,50,0,0,0,6,0),
# Plataforma(30,155,200,30,0,50,0,0,0,6,0)
        
#Monedas((30,30),(100,115)),
# Monedas((30,30),(630,230)),
# Monedas((30,30),(750,230)),
# Monedas((30,30),(900,230)),
# Monedas((30,30),(1200,230)),
# Monedas((30,30),(1360,105)),
# Monedas((30,30),(1200,105)),
# Monedas((30,30),(633,410)),
# Monedas((30,30),(900,410)),
# Monedas((30,30),(1100,410)),
# Monedas((30,30),(670,660)),
# Monedas((30,30),(785,660)),
# Monedas((30,30),(1350,660))
        
# Trampas((45,45),(1030,95), 5, 550, 400)