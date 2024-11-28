
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
from GUI_widget import*
from GUI_checkbox import*
from sqlite.controller import*

class FormPrueba(Form):
    def __init__(self,  screen, x, y, w, h, color_background, color_border = NEGRO, border_size = -1, active = True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        self.volumen = 0.1
        self.flag_play = True #por defecto incia reproducieondo el volumen

        pygame.mixer.init()

        ###_Controles_############################################

        self.lbl_nombre= Label(self._slave, 50, 20, 150, 40, "Nombre :_", "Comic Sans", 15, "White", "Table.png")
        self.lbl_puntos = Label(self._slave, 50, 60, 150, 40, "Puntos :_", "Comic Sans", 15, "White", "Table.png")
        self.txt_nombre = TextBox(self._slave, x, y, 210, 20, 150, 35, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.txt_puntos = TextBox(self._slave, x, y, 210, 60, 150, 35, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.btn_send= Button(self._slave, x, y, 370, 40, 120, 30, AZUL_CLARO, NEGRO, 1, self.btn_get_txt_click, "Nombre", "Guardar db", font="Comic Sans", font_size=15, font_color=NEGRO)

        self.btn_play = Button(self._slave, x, y, 50, 110, 100, 50, ROJO, NEGRO, 1, self.btn_play_click, "Nombre", "Pause", font="Verdana", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 400, 180, 100, 50, "20%", "Comic Sans", 15, "White", "Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 50, 200, 300, 15, self.volumen, "Blue", "White" ) #sube, baja volumen
        self.btn_tabla = Button_Image(self._slave, x, y, 200, 110, 50, 50, "Menu_BTN.png", self.btn_tabla_click, "text_param")
        self.checkbox = CheckBox(self._slave, x,y,50, 260, 100, 50, "home.png", "home.png")

        ################################################################

        #agregar control a una lista de controles que tiene el formulario 
        self.lista_widgets.append(self.lbl_nombre)
        self.lista_widgets.append(self.lbl_puntos)
        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.txt_puntos)
        self.lista_widgets.append(self.btn_send)

        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.checkbox)

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

                if self.checkbox.get_esta_prendido():
                    self._color_background = AQUA
                else:
                    self._color_background = GRIS

        else:
            self.hijo.update(lista_eventos)


    def render(self):
        self._slave.fill(self._color_background)


    def btn_get_txt_click(self, texto): # agg nombre y puntos a la base de datos
        nombre = self.txt_nombre.get_text()
        puntos = self.txt_puntos.get_text()

        if(nombre != "" and puntos != ""):
            insertRow(nombre, puntos)
            #print(nombre, puntos)
            self.txt_nombre.set_text("")
            self.txt_puntos.set_text("")
        else:
            print("nada que agregar")

    

    
    def btn_play_click(self, texto):  #_modo sonido sel juego
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

        #nombre = self.txtbox.get_text()
        #print(nombre)

    def update_volumen(self, lista_eventos): #voy a estar actualizando la lista de eventos
        self.volumen = self.slider_volumen.value
        #self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        
        lista_player = readRows()
        dict_score = {}
        dict_score = []

        for i in range(5):
            dict_score.append({"nombre":lista_player[i][1], "puntos":lista_player[i][2]})
            
        form_puntaje = FormMenuScore(self._master, 250, 15, 700, 570, NEGRO, AQUA, True, "Window.png", dict_score, 100, 10, 10)

        self.show_dialog(form_puntaje)




