import pygame
from Gui.gui_form import *
from Gui.gui_botton import *
from Gui.gui_textbox import *

class FormPauseLvl(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.txt2 = Widget(master_form=self,x=45,y=-10,w=300,h=150,color_background=None,color_border=None,image_background="Recursos/Menu/Buttons/header.png",
                            text=None,font="Arial",font_size=40,font_color=None)

        self.reanudar = Button(master=self,x=w/2 - 120/2,y=130,w=120,h=60,color_background=None,color_border=None,image_background="Recursos/Menu/play.png",
                                on_click=self.on_click_boton1,on_click_param="level_uno",text=None,font="Verdana",font_size=30,font_color=BLANCO)

        self.menu = Button(master=self,x=w/2 - 120/2,y=330,w=120,h=60,color_background=None,color_border=None,image_background="Recursos/Menu/Buttons/boton_menu.png",
                            on_click=self.on_click_boton1,on_click_param="levels",text=None,font="Verdana",font_size=30,font_color=BLANCO)

        self.resetear = Button(master=self,x=w/2 - 120/2,y=230,w=120,h=60,color_background=None,color_border=None,image_background="Recursos/Menu/Buttons/restart.png",
                                on_click=self.on_click_boton_reset,on_click_param="level_uno",text=None,font="Verdana",font_size=30,font_color=BLANCO)

        self.lista_widget = [self.reanudar,self.menu,self.txt2,self.resetear]

    def on_click_boton1(self,parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def on_click_boton_reset(self,parametro):
        '''
        El metodo reinicia el nivel dependiendo en el nivel.
        Recibe por parametro el nombre del lvl.
        '''
        self.set_active(parametro)
        self.forms_dict[parametro].resetear()
    
    def cambiar_lvl(self,parametro):
        '''
        El metodo guarda el on_click_param del boton que haya clickeado en el form de niveles para poder reiniciar el del formulario que se encuentre.
        '''
        self.reanudar.on_click_param = parametro
        self.resetear.on_click_param = parametro

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()