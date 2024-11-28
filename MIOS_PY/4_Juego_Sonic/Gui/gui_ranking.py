import pygame
from Gui.gui_form import*
from Gui.gui_botton import*
from Gui.gui_textbox import*
import sqlite3 as sql
from Sqlite.controller import*

class FormRanking(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None) -> None:
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.data_player = readRows()
        self.name = name
        self.lista_widget_nombre = []
        self.lista_widget_puntos = []

        self.eje_y = 120

        for i in range(5):
            self.lista_widget_nombre.append(Widget(master_form=self,x=10,y=self.eje_y,w=340,h=65,color_background=None,color_border=None,
                                        image_background="Recursos/Menu/Table.png",text= self.data_player[i][1],font="Arial",font_size=40,font_color=BLANCO))
            
            self.lista_widget_puntos.append(Widget(master_form=self, x=350, y=self.eje_y, w=340, h=65, color_background=None, color_border=None,
                                        image_background="Recursos/Menu/Table.png", text=self.data_player[i][2], font="Arial", font_size=40, font_color=BLANCO))
            
            self.eje_y += 70

        self.score = Widget(master_form=self, x=w/2 - 50, y=-30, w=100, h=150, color_background=None, color_border=None, image_background=None, text="Score",
                                        font="Arial", font_size=40, font_color=BLANCO)
        
        self.boton_atras = Button(master=self,x=15,y=510,w=70,h=50,color_background=None,color_border=None,image_background="Recursos/Menu/Buttons/home.png",
                                    on_click=self.on_click_boton1,on_click_param="ranking",text=None,font="Verdana",font_size=30,font_color=BLANCO)
        
        self.lista_widget = [self.score, self.boton_atras]


    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        self.update_ranking(lista_eventos)
        self.draw()

    def draw(self):
        super().draw()
        self.surface.blit(self.image_background, self.image_background_rect)
        for widget_nombre in self.lista_widget_nombre:
            widget_nombre.draw()
        for aux in self.lista_widget:
            aux.draw()
        for widget_puntos in self.lista_widget_puntos:
            widget_puntos.draw()


    def update_ranking(self, lista_eventos):
        #_mantiene actualizada la informacion desde la base de datos, sin salir del juego
        self.data_player = readRows()

        for i in range(len(self.lista_widget_nombre)):
            self.lista_widget_nombre[i]._text = self.data_player[i][1]
            self.lista_widget_puntos[i]._text = self.data_player[i][2]

        for widget_nombre in self.lista_widget_nombre:
            widget_nombre.update(lista_eventos)
        for widget_puntos in self.lista_widget_puntos:
            widget_puntos.update(lista_eventos)
        for aux in self.lista_widget:
            aux.update(lista_eventos)
