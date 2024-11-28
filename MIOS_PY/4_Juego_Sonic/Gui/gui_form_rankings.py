import pygame
from Gui.gui_form import *
from Gui.gui_botton import *
from Gui.gui_textbox import *
from niveles.constantes import *

class FormClasificaciones(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.text_ranking = Widget(self,ANCHO/2 - 400/ 2,100,400,100,None,None,None,"RANKING","Arial",40,BLANCO,)

        self.ranking_final = Button(master=self, x=ANCHO/2 - 200/ 2, y=350, w=200, h=80, color_background=None, color_border=None, 
            image_background="Recursos/Menu/Table.png", on_click=self.on_click_boton1, on_click_param="Table_Data", text="Ver Datos",
            font="Verdana", font_size=30, font_color=BLANCO)

        self.back = Button(master=self,x=80,y=680,w=100,h=80,color_background=None,color_border=None,image_background="Recursos/Menu/Buttons/home.png",
            on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=BLANCO)

        self.lista_widget = [self.ranking_final,self.back,self.text_ranking]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()