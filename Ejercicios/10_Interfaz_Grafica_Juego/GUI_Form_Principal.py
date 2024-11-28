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
from GUI_Form_Menu_Play import*
from sqlite.controller import*

#############################################################################################################################
class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border=BLANCO, border_size=-1, active=True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.flag_play = True
        self.color_fondo = color_background
        self.volumen = 0.2
        pygame.mixer.init()

        ###_Controles_############################################
        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.btn_txt= Button(self._slave, x, y, 220, 50, 120, 30, AQUA, BLANCO, 1, self.btn_get_txt_click, "Nombre", "Print Consola", font="Comic Sans", font_size=15, font_color=NEGRO)
        self.btn_play = Button(self._slave, x, y, 50, 100, 100, 50, ROJO, BLANCO, 1, self.btn_play_click, "Nombre", "Pause", font="Verdana", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 400, 180, 100, 50, "20%", "Comic Sans", 15, "White", "Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 50, 200, 300, 15, self.volumen, "Blue", "White" ) #sube, baja volumen
        self.checkbox = CheckBox(self._slave, x,y,50, 260, 100, 50, "home.png", "Table.png") # color de fondo del menu principal
        self.picture_box = PictureBox(self._slave, 300, 260, 100, 50, "bar.png")

        self.btn_tabla = Button_Image(self._slave, x, y, 200, 100, 50, 50, "Menu_BTN.png", self.btn_tabla_click, "text_param")
        self.btn_jugar = Button_Image(self._slave, x, y, 300, 100, 50, 50, "home.png", self.btn_jugar_click, "a")

        ##agregar control a una lista de controles que tiene el formulario 
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_txt)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.checkbox)
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)

        pygame.mixer.music.load("Vengeance (Loopable).wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        self.render()

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_resul():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)

                if self.checkbox.get_esta_prendido():
                    self._color_background = GRIS
                else:
                    self._color_background = NEGRO
        else:
            self.hijo.update(lista_eventos)

    
    def btn_get_txt_click(self, texto):
        nombre = self.txtbox.get_text()
        print(nombre)

    def btn_jugar_click(self, param):
        form_jugar = FormMenuPlay(screen=self._master, 
                                x = self._master.get_width() / 2 - 400,
                                y = self._master.get_height() / 2 - 250,
                                w = 800,
                                h = 500,
                                color_background = GRIS,
                                color_border = ROJO,
                                active = True, 
                                path_image = "Window.png"
                                )
        self.show_dialog(form_jugar)

    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause() #pausa la musica
            self.btn_play._color_background = AQUA #cambia de dolor el boton
            self.btn_play._font_color = ROJO
            self.btn_play.set_text("Play") #cambia el texto
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = ROJO
            self.btn_play._font_color = BLANCO
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos): #voy a estar actualizando la lista de eventos
        self.volumen = self.slider_volumen.value
        #self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):

        lista_player = readRows()
        dict_score = {}
        dict_score = []

        for i in range(len(lista_player)):
            dict_score.append({"nombre":lista_player[i][1], "puntos":lista_player[i][2]})

            
        form_puntaje = FormMenuScore(self._master, 400, 100, 700, 600, GRIS, BLANCO, True, "Window.png", dict_score, 100, 10, 1)

        self.show_dialog(form_puntaje)
