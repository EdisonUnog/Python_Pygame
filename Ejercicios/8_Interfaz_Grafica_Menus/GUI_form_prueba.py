
import pygame
from pygame.locals import *
from Class_Colores import *

from GUI_button import *
from GUI_Slider import *
from GUI_textbox import *
from GUI_Label import *
from GUI_form import *
from GUI_button_imagen import *
from GUI_widget import*
from GUI_form_menu_score import*
from GUI_widget import Colores
from GUI_checkbox import*

class FormPrueba(Form):
    def __init__(self,  screen, x, y, w, h, color_background, color_border = Colores.NEGRO, border_size = -1, active = True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        self.volumen = 0.2
        self.flag_play = True #por defecto incia reproducieondo el volumen

        pygame.mixer.init()

        ###_Controles_############################################

        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.btn_play = Button(self._slave, x, y, 50, 100, 100, 50, "red", "Blue", self.btn_play_click, "Nombre", "Pause", font="Verdana", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 400, 180, 100, 50, "20%", "Comic Sans", 15, "White", "Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 50, 200, 300, 15, self.volumen, "Blue", "White" ) #sube, baja volumen
        self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "Menu_BTN.png", self.btn_tabla_click, "text_param")
        #self.checkbox = CheckBox(self._slave, x,y,50, 260, 100, 50, "home.png", "Table.png")

        ################################################################

        #agregar control a una lista de controles que tiene el formulario 
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        #self.lista_widgets.append(self.checkbox)

        ################################################################ 

        pygame.mixer.music.load("Vengeance (Loopable).wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()


    def update(self, lista_eventos):
        if self.verificar_dialog_resul():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)

            # if self.checkbox.get_esta_prendido():
            #     self._color_background = Colores.GRIS
            # else:
            #     self._color_background = Colores.NEGRO
        else:
            self.hijo.update(lista_eventos)


    def render(self):
        self._slave.fill(self._color_background)

    
    def btn_play_click(self, texto):  #_modo sonido sel juego
        if self.flag_play:
            pygame.mixer.music.pause() #pausa la musica
            self.btn_play._color_background = "Cyan" #cambia de dolor el boton
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play") #cambia el texto
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play

        #nombre = self.txtbox.get_text()
        #print(nombre)

    def update_volumen(self, lista_eventos): #voy a estar actualizando la lista de eventos
        self.volumen = self.slider_volumen.value
        #self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        dict_score = [{"Jugador":"Gio", "Score":1000},
                        {"Jugador":"Fausto", "Score":900},
                        {"Jugador":"Gonza", "Score":750}]
            
        form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220,0,220), "White", True, "Window.png", dict_score, 100, 10, 10)

        self.show_dialog(form_puntaje)



