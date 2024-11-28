import pygame
from Gui.gui_form import*
from Gui.gui_botton import*
from Gui.gui_textbox import*
from Gui.gui_progressbar import*

#_Menu para elegir niveles
class FormLevels(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None) -> None:
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.condicion_lvl2 = True
        self.condicion_lvl3 = True
                                            #x=375
        self.level1 = Button(master=self, x=170, y=70, w=70, h=70, color_background=None, color_border=None, image_background="Recursos/Menu/niveles/1.1.png", on_click=self.iniciar_level, 
                            on_click_param="level_uno", text=None, font="Verdana", font_size=30, font_color=BLANCO)
        
        self.level2 = Button(master=self,x=170,y=270,w=70,h=70,color_background=None,color_border=None,image_background="Recursos/Menu/niveles/2.2.png",
                            on_click=self.iniciar_level,on_click_param="level_dos",text=None,font="Verdana",font_size=30,font_color=BLANCO)

        self.level3 = Button(master=self,x=170,y=470,w=70,h=70,color_background=None,color_border=None,image_background="Recursos/Menu/niveles/3.3.png",
                            on_click=self.iniciar_level,on_click_param="level_tres",text=None,font="Verdana",font_size=30,font_color=BLANCO)
        
        self.volver_menu = Button(master=self,x=80,y=680,w=100,h=80,color_background=None,color_border=None,image_background="Recursos/Menu/Buttons/home.png",
                                on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=BLANCO)
                                        #x=330
        self.txt1 = TextBox(master=self,x=80,y=40,w=250,h=150,color_background=None,color_border=None,image_background="Recursos/fondo/fondo_lvl1.png",
                            text=None,font="Arial",font_size=40,font_color=NEGRO)
        
        self.txt2 = TextBox(master=self,x=80,y=240,w=250,h=150,color_background=None,color_border=None,image_background="Recursos/fondo/fondo_lvl2.jpg",
                            text=None,font="Arial",font_size=40,font_color=NEGRO)

        self.txt3 = TextBox(master=self,x=80,y=440,w=250,h=150,color_background=None,color_border=None,image_background="Recursos/fondo/fondo_lvl3.jpg",
                            text=None,font="Arial",font_size=40,font_color=NEGRO)
        
        self.lista_widget = [self.txt1, self.txt2, self.txt3, self.level1, self.level2, self.level3, self.volver_menu]


    def on_click_boton1(self, parametro):
        #_activa el formulario al momento de hacer click en el boton
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

        if(self.condicion_lvl2):
            self.level2.on_click_param = "level_dos"
        else:
            self.level2.on_click_param = "levels"

        if(self.condicion_lvl3):
            self.level3.on_click_param = "level_tres"
        else:
            self.level3.on_click_param = "levels"

        
    def iniciar_level(self, parametro):
        #_inicia el nivel gardado en el parametro
        self.on_click_boton1(parametro)
        self.forms_dict["pause"].cambiar_lvl(parametro)

    def draw(self):
        super().draw()
        self.surface.blit(self.image_background, self.image_background_rect)
        for aux_boton in self.lista_widget:
            aux_boton.draw()