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
from gui.Gui_Form_Jugar import*
from gui.Gui_form_menu_score import*
from gui.Gui_Agg_score import*
from sqlite.controller import*

#############################################################################################################################
class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border=BLANCO, border_size=-1, active=True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)


        pygame.mixer.init()
        
        self.volumen = 0.1
        pygame.mixer.music.load("Recursos/music/Vengeance.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.btn_play = Button_Image(self._slave, x, y, 700, 350, 130, 50, "Recursos/menu/btn_play.png", self.btn_play_click, "play")
        self.btn_opciones = Button_Image(self._slave, x, y, 700, 410, 130, 50, "Recursos/menu/btn_opciones.png", self.btn_opciones_click, "opciones")
        self.btn_ranking = Button_Image(self._slave, x, y, 700, 470, 130, 50, "Recursos/menu/btn_ranking.png", self.btn_tabla_click, "opciones")
        self.btn_agg_score = Button_Image(self._slave, x, y, 700, 530, 130, 50, "Recursos/menu/btn_agg_score.png", self.btn_agg, "agg_score")

        self.lista_widgets = [self.btn_play, self.btn_opciones, self.btn_ranking, self.btn_agg_score]


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

    
    def btn_play_click(self, param):
        form_jugar = FormMenuPlay(screen=self._master, 
                                x = 0, y = 0,
                                w = ANCHO, h = ALTO,
                                color_background = GRIS,
                                color_border = ROJO,
                                active = True,
                                )

        self.show_dialog(form_jugar)

    def btn_opciones_click(self, param):
        opciones = FormOpciones(screen=self._master, 
                                x=self._master.get_width() / 2 - 450,
                                y=self._master.get_height() / 2 - 200,
                                w=900, h=350, 
                                color_background=AZUL_CLARO, 
                                color_border=BLANCO, 
                                border_size=5, 
                                active=True,
                                volumen=self.volumen)
        
        self.show_dialog(opciones)

    
    def btn_tabla_click(self, texto):
        form_puntaje = FormMenuScore(self._master, 
                                    self._master.get_width() / 2 - 350, 
                                    self._master.get_height() / 2 - 290, 700, 580, 
                                    GRIS, ROJO, 4, True, 
                                    "Recursos/menu/Window.png", 
                                    100, 10, 5)
        
        self.show_dialog(form_puntaje)


    def btn_agg(self, texto):

        score_agg = FormTextName(self._master, 
                                self._master.get_width()  / 2 -150, 
                                self._master.get_height() / 2 - 200, 300, 400, 
                                GRIS, AQUA, 4, 
                                True, 1900)

        self.show_dialog(score_agg)


    


    



















    #     self.color_fondo = color_background
    #     self.volumen = 0.2
    #     pygame.mixer.init()

    #     img_fonfo_volumen = "Recursos/menu/Table.png"
    #     self.on = "Recursos/menu/sonido/on.png"
    #     self.off = "Recursos/menu/sonido/off.png"
    #     self.flag_play = True

    #     ###_Controles_############################################
    #     self.nombre_manu = Label(self._slave, 375, 30, 150, 60, "Opciones", "Comic Sans", 20, NEGRO, img_fonfo_volumen)
    #     self.slider_volumen = Slider(self._slave, x, y, 230, 150, 300, 15, self.volumen, NEGRO, BLANCO) #sube, baja volumen
    #     self.label_volumen = Label(self._slave, 580, 130, 100, 50, "20%", "Comic Sans", 15, BLANCO, img_fonfo_volumen)
    #     self.checkbox = CheckBox(self._slave, x,y,400, 230, 100, 50, self.off, self.on) # color de fondo del menu principal

    #     #agregar control a una lista de controles que tiene el formulario
    #     self.lista_widgets = [self.nombre_manu, self.slider_volumen, self.label_volumen, self.checkbox]

    #     pygame.mixer.music.load("Recursos/music/Vengeance.wav")
    #     pygame.mixer.music.set_volume(self.volumen)
    #     pygame.mixer.music.play(-1)
    #     self.render()

    # def render(self):
    #     self._slave.fill(self._color_background)

    # def update(self, lista_eventos):
    #     if self.verificar_dialog_resul():
    #         if self.active:
    #             self.draw()
    #             self.render()
    #             for widget in self.lista_widgets:
    #                 widget.update(lista_eventos)
    #             self.update_volumen(lista_eventos)

    #             self.volumen_on_off()
    #     else:
    #         self.hijo.update(lista_eventos)


    # def update_volumen(self, lista_eventos): #voy a estar actualizando la lista de eventos
    #     self.volumen = self.slider_volumen.value
    #     self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
    #     pygame.mixer.music.set_volume(self.volumen)

    # def volumen_on_off(self):
    #     if self.checkbox.get_esta_prendido():
    #         if self.flag_play:
    #             pygame.mixer.music.pause()
    #     else:
    #         pygame.mixer.music.unpause()

    #     self.flag_play = not self.flag_play
