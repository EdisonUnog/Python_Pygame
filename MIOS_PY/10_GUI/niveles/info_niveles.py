import pygame, sys
from niveles.constantes import*
from niveles.Class_Personaje import*
from niveles.Class_Piso import*
from niveles.Class_Plataforma import*
from niveles.Class_Monedas import*
from niveles.Class_trampa import*
from niveles.modo import*

class DataLevels:
    def __init__(self, pantalla, lvl) -> None:
        
        self.pantalla = pantalla
        self.lvl = lvl
        self.player = Personaje(self.pantalla, (60, 80), (40, ALTO - 180), 9, 50)
        self.puntos_maximo = 0

        self.lista_pisos = []
        self.lista_plataformas = []
        self.lista_monedas = []
        self.lista_trampas = []
        self.win = False

        self.crear_pisos()
        self.crear_plataformas()
        self.crear_trampas()
        self.crear_monedas()

        self.reloj = pygame.time.Clock()


        # #_Musica_fondo
        # pygame.mixer.music.load("Recursos/music/Vengeance.wav")
        # pygame.mixer.music.set_volume(0.1)
        # pygame.mixer.music.play(-1)

    def crear_pisos(self):
        if (self.lvl == "nivel_uno" or self.lvl == "nivel_dos" or self.lvl == "nivel_tres"):
            self.lista_pisos.append(Pisos((ANCHO, 25), 3, (0,0))) 
            self.lista_pisos.append(Pisos((ANCHO, 50), 2, (0, ALTO - 50)))
            self.lista_pisos.append(Pisos((20, 725), 0, (0, 25)))           
            self.lista_pisos.append(Pisos((20, 725), 0, (ANCHO - 20, 25)))


    def crear_plataformas(self):
        if (self.lvl == "nivel_uno"):
                                                        # x, y, w, h, velocidad, left, right, top, index, posicion_up=None)
            self.lista_plataformas.append(Plataforma(300, 640, 200, 20, 4, 200, 700, 300, 1, 0))
            #self.lista_plataformas.append(Plataforma(700, 640, 200, 20, 5, 300, 1000, 400, 2, 1))
            self.lista_plataformas.append(Plataforma(500, 640, 100, 20, 5, 500, 900, 0, 2, 2))
            self.lista_plataformas.append(Plataforma(520, 450, 100, 20, 0, 0, 0, 0, 3, None))

        elif (self.lvl == "nivel_dos"):
            self.lista_plataformas.append(Plataforma(700, 650, 200, 20, 5, 300, 1000, 400, 2, 1))

        elif (self.lvl == "nivel_tres"):
            self.lista_plataformas.append(Plataforma(700, 640, 100, 20, 5, 400, 900, 0, 2, 2))

    def crear_trampas(self):
        if (self.lvl == "nivel_uno"):
            self.lista_trampas.append(Trampa(400, ALTO - 110, 55, 55, 7, 400, 800))
        elif (self.lvl == "nivel_dos"):
            self.lista_trampas.append(Trampa(300, ALTO - 110, 55, 55, 5, 300, 500))
        elif (self.lvl == "nivel_tres"):
            self.lista_trampas.append(Trampa(500, ALTO - 110, 55, 55, 5, 400, 600))

    def crear_monedas(self):
        self.win = False
        if (self.lvl == "nivel_uno"):
            self.lista_monedas.append(Monedas((25, 25), (400, ALTO - 80)))
            # self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 80)))
            # self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 120)))
            # self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 160)))
            # self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 200)))

        elif (self.lvl == "nivel_dos"):
            self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 80)))
            self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 120)))
            self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 160)))
            self.lista_monedas.append(Monedas((25, 25), (800, ALTO - 200)))

            self.lista_monedas.append(Monedas((25, 25), (840, ALTO - 80)))
            self.lista_monedas.append(Monedas((25, 25), (840, ALTO - 120)))
            self.lista_monedas.append(Monedas((25, 25), (840, ALTO - 160)))
            self.lista_monedas.append(Monedas((25, 25), (840, ALTO - 200)))

        elif (self.lvl == "nivel_tres"):
            self.lista_monedas.append(Monedas((25, 25), (700, ALTO - 80)))
            self.lista_monedas.append(Monedas((25, 25), (740, ALTO - 100)))
            self.lista_monedas.append(Monedas((25, 25), (780, ALTO - 120)))
            self.lista_monedas.append(Monedas((25, 25), (820, ALTO - 100)))
            self.lista_monedas.append(Monedas((25, 25), (860, ALTO - 80)))

            self.lista_monedas.append(Monedas((25, 25), (900, ALTO - 80)))
            self.lista_monedas.append(Monedas((25, 25), (900, ALTO - 120)))
            self.lista_monedas.append(Monedas((25, 25), (900, ALTO - 160)))
            self.lista_monedas.append(Monedas((25, 25), (900, ALTO - 200)))

            self.lista_monedas.append(Monedas((25, 25), (940, ALTO - 80)))
            self.lista_monedas.append(Monedas((25, 25), (940, ALTO - 120)))
            self.lista_monedas.append(Monedas((25, 25), (940, ALTO - 160)))
            self.lista_monedas.append(Monedas((25, 25), (940, ALTO - 200)))


    def update(self):
        for piso in self.lista_pisos:
            piso.draw(self.pantalla)

        for plataforma in self.lista_plataformas:
            plataforma.draw(self.pantalla)
            plataforma.update()  

        for trampa in self.lista_trampas:
            trampa.draw(self.pantalla) 
            trampa.update()

        for moneda in self.lista_monedas:
            moneda.draw(self.pantalla)
            if(self.player.lados["main"].colliderect(moneda.lados["main"])):
                self.player.puntos_player += 50
                self.lista_monedas.remove(moneda)

            if(len(self.lista_monedas) <= 0):
                self.win=True

        # self.player.update(reloj, self.pantalla, self.lista_pisos, self.lista_plataformas)

        self.draw_rect()

    
    def draw_rect(self):

        if get_mode():
            for pisos in self.lista_pisos:
                for lado in pisos.lados:
                    pygame.draw.rect(self.pantalla, ROJO, pisos.lados[lado], 2)
            
            for i in range(len(self.lista_plataformas)):
                pygame.draw.rect(self.pantalla, ROJO, self.lista_plataformas[i].rect, 4)
            for plataforma in self.lista_plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self.pantalla, AQUA, plataforma.lados[lado], 2)

            for i in range(len(self.lista_monedas)):
                pygame.draw.rect(self.pantalla, ROJO, self.lista_monedas[i].rectangulo, 4)
            for moneda in self.lista_monedas:
                for lado in moneda.lados:
                    pygame.draw.rect(self.pantalla, AQUA, moneda.lados[lado], 2)

            for i in self.player.rectangulo:
                pygame.draw.rect(self.pantalla, ROJO, self.player.rectangulo, 4)
            for lado in self.player.lados:
                pygame.draw.rect(self.pantalla, BLANCO, self.player.lados[lado], 2)