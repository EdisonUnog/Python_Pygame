import pygame
from niveles.constantes import*
from gui.Gui_Widget import*
from gui.Gui_Form import*
from gui.Gui_Slider import*
from gui.Gui_Label import*
from gui.Gui_checkbox import*
from gui.Gui_button_imagen import*

class FormOpciones(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border=BLANCO, border_size=-1, active=True, volumen = None) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.color_fondo = color_background

        self.volumen = volumen

        img_fonfo_volumen = "Recursos/menu/Table.png"
        self.on = "Recursos/menu/sonido/on.png"
        self.off = "Recursos/menu/sonido/off.png"
        self.flag_play = True

        ###_Controles_############################################
        self.nombre_manu = Label(self._slave, 375, 30, 150, 60, "Opciones", "Comic Sans", 20, NEGRO, img_fonfo_volumen)
        self.slider_volumen = Slider(self._slave, x, y, 230, 150, 300, 15, self.volumen, NEGRO, BLANCO) #sube, baja volumen
        self.label_volumen = Label(self._slave, 580, 130, 100, 50, "20%", "Comic Sans", 15, BLANCO, img_fonfo_volumen)
        self.checkbox = CheckBox(self._slave, x, y,400, 230, 100, 50, self.off, self.on) # color de fondo del menu principal

        self._btn_home = Button_Image(screen=self._slave, x=20, y=280, master_x=x, master_y=y, w=50, h=50, onclick=self.btn_home_click,
                                        onclick_param="", path_image="Recursos/menu/home.png")

        #agregar control a una lista de controles que tiene el formulario
        self.lista_widgets = [self.nombre_manu, self.slider_volumen, self.label_volumen, self.checkbox, self._btn_home]
        
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)


    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
                widget.draw()

            self.update_volumen() 
            

    def update_volumen(self): #voy a estar actualizando la lista de eventos
        if self.flag_play:
            if self.checkbox.get_esta_prendido():
                self.volumen = 0
                self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
                pygame.mixer.music.set_volume(self.volumen)
            else:
                self.volumen = self.slider_volumen.value
                self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
                pygame.mixer.music.set_volume(self.volumen)

        self.flag_play = not self.flag_play
        print(self.volumen)

        
    def get_volumen(self):
        return self.volumen

    def btn_home_click(self, texto): #me lleva al menu principal
        self.end_dialog()







 # def volumen_on_off(self):
    #     if self.checkbox.get_esta_prendido():
    #         if self.flag_play:
    #             pygame.mixer.music.pause()
    #     else:
    #         pygame.mixer.music.unpause()

    #     self.flag_play = not self.flag_play