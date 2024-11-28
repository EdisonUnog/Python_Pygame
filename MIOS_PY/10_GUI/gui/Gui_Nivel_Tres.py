import pygame
from gui.Gui_Widget import NEGRO
from niveles.constantes import*
from gui.Gui_Widget import*
from gui.Gui_Form import*
from gui.Gui_Slider import*
from gui.Gui_Label import*
from gui.Gui_checkbox import*
from gui.Gui_button_imagen import*
from gui.Gui_Form_Opciones import*
from gui.Gui_picture_box import*
from gui.Gui_Barra_Vida import*
from niveles.constantes import*
from niveles.info_niveles import*

class LevelTres(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size=-1, active=True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self._color_background = color_background
        self._color_border = color_border

        self.lista_info = DataLevels(self._slave, "nivel_tres")
        self.reloj_tick= self.lista_info.reloj

        #imagen de fondo
        self.imagen_fondo = pygame.image.load("Recursos/Fondos/fondo_space.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO, ALTO))

        self.lista_pisos = self.lista_info.lista_pisos
        self.lista_plataformas = self.lista_info.lista_plataformas
        self.lista_monedas = self.lista_info.lista_monedas
        self.lista_trampas = self.lista_info.lista_trampas

        #player y barra de vida
        self.value = self.lista_info.player.hp
        self.value_max = self.lista_info.player.hp
        self.barra_vida = BarraVida(self._slave, 20, 25, 500, 50, NEGRO, AZUL, 4, BLANCO, self.value, self.value_max)

        self.img_tabla = "Recursos/menu/Table.png"
        
        #nombre_nivel
        self.nombre_lvl = Label(self._slave, ANCHO - 400, 25, 150, 60,  self.lista_info.lvl, "Comic Sans", 20, NEGRO, self.img_tabla)

        #puntos
        self.score = Label(self._slave, ANCHO - 170, 25, 150, 60,  self.lista_info.player.puntos_player, "Comic Sans", 20, NEGRO, self.img_tabla)
        self.puntos_totales = self.lista_info.player.puntos_player

        #tiempo
        self.time_juego = 30
        self.acumulador_time = 0
        self.img_reloj = "Recursos/menu/reloj.png"
        self.time = Label(self._slave, ANCHO / 2 - 75, 25, 150, 60, self.time_juego, "Comic Sans", 20, NEGRO, self.img_tabla)
        self.reloj = Label(self._slave, ANCHO / 2 + 80, 25, 50, 50, "", "Comic Sans", 20, NEGRO, self.img_reloj)
        self.tick_1s = pygame.USEREVENT+0
        pygame.time.set_timer(self.tick_1s, 1000)

        #gana o pierde  ##PictureBox(self._slave, 300, 260, 100, 50, "bar.png")
        self.win_lvl3 = self.lista_info.win
        self.gana = PictureBox(self._slave, x, y, w, h, "Recursos/menu/gana.png")
        self.pierde = PictureBox(self._slave, x, y, w, h, "Recursos/menu/pierde.png")

        #lista Widget del form lvl 
        self.lista_widgets = [self.nombre_lvl, self.time, self.score, self.reloj]

    def draw(self):
        super().draw()
        self._slave.blit(self.imagen_fondo, (0,0))

    def resetear(self):
        self.__init__(self.screen, self.x, self.y, self.w, self.h, self._color_background, self._color_border, self.border_size, self.active)

    def update(self, lista_eventos):
        self.draw()
        delta = self.reloj_tick.tick(FPS)

        if(not self.lista_info.win and not self.lista_info.player.muerte and self.time_juego > 0):

            self.lista_info.update()

            #_Widget
            for aux_widget in self.lista_widgets:
                aux_widget.update(lista_eventos)
                aux_widget.draw()

            #_Tiempo
            self.time._text = self.time_juego

            #:Player y su barra
            self.lista_info.player.update(self.screen, self.lista_pisos, self.lista_plataformas, self.lista_trampas)
            self.barra_vida.update(lista_eventos, self.lista_info.player.hp)
            self.barra_vida.draw()

            #_Score
            self.score._text = self.lista_info.player.puntos_player
            self.puntos_totales = self.lista_info.player.puntos_player

        elif(self.lista_info.win):
            self.win_lvl3 = True
            self.gana.update(lista_eventos)
            self.gana.draw()
            self.sin_tiempo(delta)
            self.active = True

        elif(self.lista_info.player.muerte or self.time_juego <= 0):
            self.pierde.update(lista_eventos)
            self.pierde.draw()
            self.sin_tiempo(delta)

        #_Eventos
        for event in lista_eventos:
            if event.type == self.tick_1s:
                self.time_juego -= 1

            
    def sin_tiempo(self, delta):
        self.acumulador_time += delta  
        if(self.acumulador_time == 2000):
            #self.end_dialog()
            self.resetear()
            self.acumulador_time = 0