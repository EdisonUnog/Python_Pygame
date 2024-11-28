import pygame
from niveles.Class_Plataformas import*
from niveles.Class_Monedas import*
from niveles.Class_Trampas import*
from niveles.Class_Personaje import*
from niveles.Class_Piso import*
from niveles.constantes import*
from niveles.modo import*

class Datalevels:
    def __init__(self, pantalla, lvl) -> None:
        
        self.pantalla = pantalla
        self.lvl = lvl
        self.player = Personaje((60, 80), (20, ALTO - 200), 15, ANCHO, ALTO)

        self.lista_pisos = []
        self.lista_plataformas = []
        self.lista_monedas = []
        self.lista_trampas = []
        self.win = False

        self.crear_pisos()
        self.crear_plataforma()
        self.crear_monedas()
        self.crear_trampa()
        
    def crear_pisos(self):
        if(self.lvl == "nivel_uno"):
            self.lista_pisos.append(Pisos((1700, 100), 0, (0, ALTO - 100)))

        elif(self.lvl == "nivel_dos"):
            self.lista_pisos.append(Pisos((1700, 100), 1, (0, ALTO - 100)))

        elif(self.lvl == "nivel_tres"):
            self.lista_pisos.append(Pisos((1700, 100), 2, (0, ALTO - 100)))

    def crear_plataforma(self):
        if(self.lvl == "nivel_uno"):
            self.lista_plataformas.append(Plataforma(300, 600, 65, 20, 7, 50, 200, 700, 7, 5, 300, 0))
            self.lista_plataformas.append(Plataforma(500, 450, 850, 30, 0, 50, 0, 0, 0, 4, 0))
            self.lista_plataformas.append(Plataforma(500, 271, 850, 30, 0, 50, 0, 0, 0, 4, 0, None))
            self.lista_plataformas.append(Plataforma(950, 147, 500, 30, 0, 50, 0, 0, 0, 6, 0, None))
            self.lista_plataformas.append(Plataforma(30, 155, 200, 30, 0, 50, 0, 0, 0, 6, 0, None))

        elif(self.lvl == "nivel_dos"):
            self.lista_plataformas.append(Plataforma(1150, 600, 100, 35, 7, 50, 0, 0,7, 7,200, 1))
            self.lista_plataformas.append(Plataforma(450, 180, 605, 45, 0, 50, 0, 0, 0, 9, 0, None))
            self.lista_plataformas.append(Plataforma(1335, 503, 150, 35, 0, 50, 0, 0, 0, 5, 0, None))
            self.lista_plataformas.append(Plataforma(700, 408, 350, 35, 0, 50, 0, 0, 0, 5, 0, None))
            self.lista_plataformas.append(Plataforma(350, 350, 300, 35, 0, 50, 0, 0, 0, 5, 0, None))
            self.lista_plataformas.append(Plataforma(20, 250, 250, 35, 0, 50, 0, 0, 0, 9, 0, None))
            self.lista_plataformas.append(Plataforma(1350, 150, 120, 35, 0, 50, 0, 0, 0, 9, 0, None))
            self.lista_plataformas.append(Plataforma(460, 600, 250, 35, 0, 50, 0, 0, 0, 5, 0, None))
            
        elif(self.lvl == "nivel_tres"):
            self.lista_plataformas.append(Plataforma(1000, 600, 100, 35, 7, 50, 270, 1000, 7, 14, 300, 0))
            self.lista_plataformas.append(Plataforma(1000, 600, 100, 35, 7, 50, 1000, 1125, 7, 14, 300, 1))
            self.lista_plataformas.append(Plataforma(0,280, 250, 35, 0, 50, 0, 0, 0, 20, 0, None))
            self.lista_plataformas.append(Plataforma(400, 475,700, 50, 0, 50, 0, 0, 0, 15, 0, None))
            self.lista_plataformas.append(Plataforma(400, 330, 250, 35, 0, 50, 0, 0, 0, 20, 0, None))
            self.lista_plataformas.append(Plataforma(500, 170, 550, 50, 0, 50, 0, 0, 0, 15, 0, None))
            self.lista_plataformas.append(Plataforma(945, 330, 150, 35, 0, 50, 0, 0, 0, 20, 0, None))
            self.lista_plataformas.append(Plataforma(0, 500, 150, 35, 0, 50, 0, 0, 0, 20, 0, None))
            self.lista_plataformas.append(Plataforma(1250, 155, 240, 35, 0, 50, 0, 0, 0, 15, 0, None))
            self.lista_plataformas.append(Plataforma(1325, 330, 170, 35, 0, 50, 0, 0, 0, 20, 0, None))
            self.lista_plataformas.append(Plataforma(1260, 550, 230, 35, 0, 50, 0, 0, 0, 20, 0, None))

    def crear_monedas(self):
        self.win = False
        if(self.lvl == "nivel_uno"):
            self.lista_monedas.append(Monedas((30,30),(100,115)))
            self.lista_monedas.append(Monedas((30,30),(630,230)))
            self.lista_monedas.append(Monedas((30,30),(750,230)))
            self.lista_monedas.append(Monedas((30,30),(900,230)))
            self.lista_monedas.append(Monedas((30,30),(1200,230)))
            self.lista_monedas.append(Monedas((30,30),(1360,105)))
            self.lista_monedas.append(Monedas((30,30),(1200,105)))
            self.lista_monedas.append(Monedas((30,30),(633,410)))
            self.lista_monedas.append(Monedas((30,30),(900,410)))
            self.lista_monedas.append(Monedas((30,30),(1100,410)))
            self.lista_monedas.append(Monedas((30,30),(670,660)))
            self.lista_monedas.append(Monedas((30,30),(785,660)))
            self.lista_monedas.append(Monedas((30,30),(1350,660)))

        elif(self.lvl == "nivel_dos"):
            self.lista_monedas.append(Monedas((30,30),(450,150)))
            self.lista_monedas.append(Monedas((30,30),(500,150)))
            self.lista_monedas.append(Monedas((30,30),(900,150)))
            self.lista_monedas.append(Monedas((30,30),(960,150)))
            self.lista_monedas.append(Monedas((30,30),(1450,470)))
            self.lista_monedas.append(Monedas((30,30),(700,375)))
            self.lista_monedas.append(Monedas((30,30),(750,375)))
            self.lista_monedas.append(Monedas((30,30),(350,318)))
            self.lista_monedas.append(Monedas((30,30),(600,318)))
            self.lista_monedas.append(Monedas((30,30),(20,218)))
            self.lista_monedas.append(Monedas((30,30),(80,218)))
            self.lista_monedas.append(Monedas((30,30),(1380,120)))
            self.lista_monedas.append(Monedas((30,30),(650,568)))
            self.lista_monedas.append(Monedas((30,30),(680,568)))
            self.lista_monedas.append(Monedas((30,30),(980,668)))
            self.lista_monedas.append(Monedas((30,30),(940,668)))
            self.lista_monedas.append(Monedas((30,30),(900,668)))
            self.lista_monedas.append(Monedas((30,30),(1020,668)))

        elif(self.lvl == "nivel_tres"):
            self.lista_monedas.append(Monedas((35,35),(665,660)))
            self.lista_monedas.append(Monedas((35,35),(710,660)))
            self.lista_monedas.append(Monedas((35,35),(755,660)))
            self.lista_monedas.append(Monedas((35,35),(800,660)))
            self.lista_monedas.append(Monedas((35,35),(850,660)))
            self.lista_monedas.append(Monedas((35,35),(5,460)))
            self.lista_monedas.append(Monedas((35,35),(50,460)))
            self.lista_monedas.append(Monedas((35,35),(100,460)))
            self.lista_monedas.append(Monedas((35,35),(4,240)))
            self.lista_monedas.append(Monedas((35,35),(45,240)))
            self.lista_monedas.append(Monedas((35,35),(410,290)))
            self.lista_monedas.append(Monedas((35,35),(600,290)))
            self.lista_monedas.append(Monedas((35,35),(1450,290)))
            self.lista_monedas.append(Monedas((35,35),(1400,290)))
            self.lista_monedas.append(Monedas((35,35),(1350,290)))
            self.lista_monedas.append(Monedas((35,35),(1450,510)))
            self.lista_monedas.append(Monedas((35,35),(952,135)))
            self.lista_monedas.append(Monedas((35,35),(995,135)))

    def crear_trampa(self):
        if(self.lvl == "nivel_uno"):
            self.lista_trampas.append(Trampas((55,55),(400,645),5,1100,900))
            self.lista_trampas.append(Trampas((55,55),(1030,95),5,550,400))
        
        elif(self.lvl == "nivel_dos"):
            self.lista_trampas.append(Trampas((55,55),(450,550),5,1038,920))
            self.lista_trampas.append(Trampas((55,55),(130,200),5,1380,1280))
            self.lista_trampas.append(Trampas((55,55),(755,650),5,800,700))

        elif(self.lvl == "nivel_tres"):
            self.lista_trampas.append(Trampas((60,60),(506,645),5,1038,920))
            self.lista_trampas.append(Trampas((60,60),(1100,645),5,600,400))
            self.lista_trampas.append(Trampas((60,60),(470,270),5,1050,970))
            self.lista_trampas.append(Trampas((60,60),(1280,100),5,250,190))

    
    def update(self, reloj):
        for piso in self.lista_pisos:
            piso.draw(self.pantalla)

        for plataforma in self.lista_plataformas:
            plataforma.draw(self.pantalla)
            plataforma.update(reloj)

        for trampa in self.lista_trampas:
            trampa.draw(self.pantalla)
            trampa.mover_x(ANCHO)
        
        for moneda in self.lista_monedas:
            moneda.draw(self.pantalla)
            if(self.player.lados["main"].colliderect(moneda.lados["main"])):
                self.player.puntos_player += 50
                self.lista_monedas.remove(moneda)

            if(len(self.lista_monedas) <= 0):
                self.win=True

        self.draw_rect()


    def draw_rect(self):

        if get_mode():
            for i in self.player.rectangulo:
                pygame.draw.rect(self.pantalla, ROJO, self.player.rectangulo, 4)
            for lado in self.player.lados:
                pygame.draw.rect(self.pantalla, BLANCO, self.player.lados[lado], 2)


            for i in range(len(self.lista_monedas)):
                pygame.draw.rect(self.pantalla, ROJO, self.lista_monedas[i].rectangulo, 4)
            for moneda in self.lista_monedas:
                for lado in moneda.lados:
                    pygame.draw.rect(self.pantalla, AQUA, moneda.lados[lado], 2)

            
            for i in range(len(self.lista_plataformas)):
                pygame.draw.rect(self.pantalla, ROJO, self.lista_plataformas[i].rect, 4)
            for plataforma in self.lista_plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self.pantalla, AQUA, plataforma.lados[lado], 2)



