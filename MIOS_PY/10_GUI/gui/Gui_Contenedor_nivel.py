import pygame
from gui.Gui_Widget import*
from niveles.constantes import*
from gui.Gui_Widget import*
from gui.Gui_Form import*
from gui.Gui_Slider import*
from gui.Gui_Label import*
from gui.Gui_checkbox import*
from gui.Gui_button_imagen import*
from gui.Gui_Form_Opciones import*
from gui.Gui_Nivel_Uno import*
from niveles.constantes import*

class FormContenedorNivel(Form):
    def __init__(self, screen: pygame.Surface, nivel) -> None:
        super().__init__(screen, 0, 0, screen.get_width(), screen.get_height(), GRIS, ROJO, -1, True)
        
        self._slave = self._slave
        self.nivel = nivel
        
        self._btn_home = Button_Image(screen, 0, 0, ANCHO / 2 - 60, ALTO - 45, 120, 40, onclick=self.btn_home_click, 
                                    onclick_param="", path_image="Recursos/menu/btn_niveles.png")

        self.lista_widgets = [self.nivel, self._btn_home]

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_resul():
            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)

        else:
            self.hijo.update(lista_eventos)


    def btn_home_click(self, texto): # me lleva al menu principal
        self.end_dialog()
