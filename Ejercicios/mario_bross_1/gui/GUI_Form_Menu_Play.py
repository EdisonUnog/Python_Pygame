import pygame
from pygame.locals import *
from niveles.Class_Colores import *

from gui.GUI_button import *
from gui.GUI_Slider import *
from gui.GUI_button import Colores
from gui.GUI_textbox import *
from gui.GUI_Label import *
from gui.GUI_form import *
from gui.GUI_button_imagen import *
from gui.GUI_widget import*
from gui.GUI_form_menu_score import*
from gui.GUI_checkbox import*
from gui.GUI_picture_box import*
from niveles.Class_ManejadorNiveles import *
from gui.GUI_Form_Contenedor_Niveles import*

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        self.manejar_niveles = Manejador_niveles(self._master) ##

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))

        self.fondo_1= pygame.image.load("Recursos/fondo6.png")
        self.fondo_1 = pygame.transform.scale(self.fondo_1,(w,h))

        self.flag_nivell1 = 1
        self.flag_nivell2 = 0
        self.flag_nivell3 = 0

        self._btn_level1 = Button_Image(screen=self._slave, x=90, y=100, master_x=x, master_y=y, w=150, h=150, onclick=self.entrar_nivel,
                                            onclick_param="nivel_uno", path_image="1.png")
        
        self._btn_level2 = Button_Image(screen=self._slave, x=260, y=100, master_x=x, master_y=y, w=150, h=150, onclick=self.entrar_nivel,
                                            onclick_param="nivel_dos", path_image="2.png")
        
        self._btn_level3 = Button_Image(screen=self._slave, x=170, y=260, master_x=x, master_y=y, w=150, h=150, onclick=self.entrar_nivel,
                                        onclick_param="nivel_tres", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="3.png")
        
        self._btn_home = Button_Image(screen=self._slave, x=400, y=400, master_x=x, master_y=y, w=50, h=50, onclick=self.btn_home_click,
                                        onclick_param="", path_image="gui/home.png")
        
        self.lista_widgets.append(self._btn_level1)
        self.lista_widgets.append(self._btn_level2)
        self.lista_widgets.append(self._btn_level3)
        self.lista_widgets.append(self._btn_home)
        self.render()

    def render(self):
        self._slave.fill(self._color_background)

    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_resul():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            self._slave.blit(self.fondo_1, (0,0))
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejar_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, texto): #me lleva al menu principal
        self.end_dialog()