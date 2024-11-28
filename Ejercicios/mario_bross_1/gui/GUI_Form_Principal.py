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
from gui.GUI_Form_Menu_Play import*

#############################################################################################################################
class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border=Colores.NEGRO, border_size=-1, active=True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()

        self.fondo_1= pygame.image.load("Recursos/fondo4.png")
        self.fondo_1 = pygame.transform.scale(self.fondo_1,(w,h))
        
        self.fondo_2= pygame.image.load("Recursos/fondo6.png")
        self.fondo_2 = pygame.transform.scale(self.fondo_2,(w,h))

        ###_Controles_############################################
        #self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size = 15, font_color = "Black")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Green", "Blue", self.btn_play_click, "Nombre", "Pause", font="Verdana", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Comic Sans", 15, "White", "gui/Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 300, 15, self.volumen, "Blue", "White" ) #sube, baja volumen
        self.checkbox = CheckBox(self._slave, x,y,100, 230, 100, 50, "gui/home.png", "gui/home.png")
        self.picture_box = PictureBox(self._slave, 300, 230, 100, 50, "gui/picture.png")

        self.btn_tabla = Button_Image(self._slave, x, y, 225, 100, 50, 50, "gui/Menu_BTN.png", self.btn_tabla_click, "text_param") #menu jugador
        self.btn_jugar = Button_Image(self._slave, x, y, 300, 100, 50, 50, "Quieto/1.png", self.btn_jugar_click, "a")
        pygame.mixer.music.load("sonidos/theme1.mp3")

        #agregar control a una lista de controles que tiene el formulario 
        #self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.checkbox)
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_tabla) ##score jugador
        self.lista_widgets.append(self.btn_jugar)

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        self.render()

    def render(self):
        self._slave.fill(self._color_background)
        self._slave.blit(self.fondo_1, (0,0))

    def update(self, lista_eventos):
        if self.verificar_dialog_resul():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)

                if self.checkbox.get_esta_prendido():
                    self._color_background = Colores.AZUL_CLARO #cambio de color el fondo
                else:
                    self._color_background = Colores.GRIS #color de fondo del menu principal
                
        else:
            self.hijo.update(lista_eventos)


    def update_volumen(self, lista_eventos): #voy a estar actualizando la lista de eventos
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)


    def btn_jugar_click(self, param): # menu de elegir los niveles
        form_jugar = FormMenuPlay(screen=self._master, 
                                x = self._master.get_width() / 2 - 250,
                                y = self._master.get_height() / 2 - 250,
                                w = 500,
                                h = 500,
                                color_background = Colores.GRIS, #fucsia
                                color_border = Colores.BLANCO,   #Blanco
                                active = True, 
                                path_image = "gui/Window.png"
                                )
        self.show_dialog(form_jugar)

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

    def btn_tabla_click(self, texto):
        dict_score = [{"Jugador":"Gio", "Score":1000},
                        {"Jugador":"Fausto", "Score":900},
                        {"Jugador":"Gonza", "Score":750}]
            
        form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220,0,220), "White", True, "gui/Window.png", dict_score, 100, 10, 10)

        self.show_dialog(form_puntaje)