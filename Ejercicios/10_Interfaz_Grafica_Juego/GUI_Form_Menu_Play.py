import pygame
from pygame.locals import *
from Class_Colores import *
from Class_Colores import*

from GUI_button import *
from GUI_Slider import *
from GUI_button import*
from GUI_textbox import *
from GUI_Label import *
from GUI_form import *
from GUI_button_imagen import *
from GUI_widget import*
from GUI_form_menu_score import*
from GUI_checkbox import*
from GUI_picture_box import*
from niveles.Class_ManejadorNiveles import *
from GUI_Form_Contenedor_Niveles import*

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        self.manejar_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))

        self._btn_level1 = Button_Image(screen=self._slave, x=125, y=100, master_x=x, master_y=y, w=100, h=150, onclick=self.entrar_nivel,
                                        onclick_param="nivel_uno", path_image="bar.png")
        
        self._btn_level2 = Button_Image(screen=self._slave, x=350, y=100, master_x=x, master_y=y, w=100, h=150, onclick=self.entrar_nivel,
                                        onclick_param="nivel_dos", path_image="bar.png")
        
        self._btn_level3 = Button_Image(screen=self._slave, x=575, y=100, master_x=x, master_y=y, w=100, h=150, onclick=self.entrar_nivel,
                                        onclick_param="nivel_tres", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="bar.png")
        
        self._btn_home = Button_Image(screen=self._slave, x=375, y=350, master_x=x, master_y=y, w=50, h=50, onclick=self.btn_home_click,
                                        onclick_param="", path_image="home.png")
        
        #self._btn_home = Button_Image(screen=self._slave, x=400, y=400, master_x=x, master_y=y, w=50, h=50, 
                                        #color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, 
                                        #onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="home.png")

        

        self.lista_widgets.append(self._btn_level1)
        self.lista_widgets.append(self._btn_level2)
        self.lista_widgets.append(self._btn_level3)
        self.lista_widgets.append(self._btn_home)

    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_resul():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejar_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, texto): #me lleva al menu principal
        self.end_dialog()