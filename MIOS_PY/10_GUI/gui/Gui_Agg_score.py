import pygame

from gui.Gui_Form import*
from gui.Gui_Widget import*
from gui.Gui_button_imagen import*
from gui.Gui_textbox import*
from niveles.constantes import*
from sqlite.controller import*


class FormTextName(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, puntos_totales) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.puntos_totales = puntos_totales
        self.nombre_enviado = ""

        self.nombre_player = TextBox(self._slave, x, y, w/2 - 100, h/2 -90, 200, 50, GRIS, BLANCO, ROJO, AZUL, 2, font = "Comic Sans", font_size = 15, font_color = NEGRO)
        
        self.btn_send = Button_Image(self._slave, x, y, w/2 - 65, h/2 - 25, 130, 50, "Recursos/menu/btn_send.png", self.btn_enviar_nombre, "")
        
        self._btn_home = Button_Image(self._slave, x, y, w/2 - 25, h - 80, 50, 50, "Recursos/menu/home.png", self.btn_home_click, "atras")

        self.lista_widgets = [self.btn_send, self.nombre_player, self._btn_home]


    def render(self):
        self._slave.fill(self._color_background)

    
    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

            self.agregar_info_sqlite()


    def btn_enviar_nombre(self, param):
        self.nombre_enviado = self.nombre_player._text
        self.end_dialog()

    def agregar_info_sqlite(self):
        self.nombre = self.nombre_enviado
        if(self.nombre != ""):
            insertRow(self.nombre, self.puntos_totales)
            self.nombre = ""
            self.nombre_enviado = ""
            self.nombre_player._text = "Player"

    def btn_home_click(self, texto): #me lleva al menu principal
        self.end_dialog()

    