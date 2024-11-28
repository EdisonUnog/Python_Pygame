import pygame
from niveles.constantes import*
from gui.Gui_Widget import*
from gui.Gui_Form import*
from gui.Gui_Slider import*
from gui.Gui_Label import*
from gui.Gui_checkbox import*
from gui.Gui_button_imagen import*
from gui.Gui_Form_Opciones import*
from gui.Gui_Nivel_Uno import*
from gui.Gui_Contenedor_nivel import*
from gui.manejador_niveles import*


class FormMenuPlay(Form):
    
    def __init__(self, screen, x, y, w, h, color_background, color_border, active) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        self.manejador_niveles = Manejador_niveles(self._master)

        self.btn_uno = Button_Image(self._slave, x, y, 160, 115, 130, 70, "Recursos/menu/uno.png", self.entrar_nivel, "nivel_uno")
        self.img_uno = PictureBox(self._slave, 100, 50, 250, 200, "Recursos/menu/marco.png")

        self.btn_dos = Button_Image(self._slave, x, y, 685, 115, 130, 70, "Recursos/menu/dos.png", self.entrar_nivel, "nivel_dos")
        self.img_dos = PictureBox(self._slave, 625, 50, 250, 200, "Recursos/menu/marco.png")

        self.btn_tres = Button_Image(self._slave, x, y, 1210, 115, 130, 70, "Recursos/menu/tres.png", self.entrar_nivel, "nivel_tres")
        self.img_tres = PictureBox(self._slave, 1150, 50, 250, 200, "Recursos/menu/marco.png")

        self._btn_home = Button_Image(screen=self._slave, x=ANCHO /2 - 25, y=ALTO - 100, master_x=x, master_y=y, w=50, h=50, onclick=self.btn_home_click,
                                        onclick_param="", path_image="Recursos/menu/home.png")

        self.lista_widgets = [self.img_uno, self.img_dos, self.img_tres, self.btn_uno, self.btn_dos, self.btn_tres, self._btn_home]

    def render(self):
        self._slave.fill(self._color_background)

    def update(self,lista_eventos):
        if self.verificar_dialog_resul():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos) 

        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        comenzar = FormContenedorNivel(self._master, nivel)
        self.show_dialog(comenzar)

    def btn_home_click(self, texto): #me lleva al menu principal
        self.end_dialog() 
