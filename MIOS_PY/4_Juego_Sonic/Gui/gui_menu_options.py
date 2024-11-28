import pygame, sys
from Gui.gui_form import*
from Gui.gui_botton import*
from Gui.gui_botton import*
from Gui.gui_widget import*
from Gui.gui_progressbar import*
from Gui.gui_slider_vol import*
from Gui.gui_Label import*

class FormOptions(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_border, active, image_background=None, color_background=None) -> None:
        super().__init__(name, master_surface, x, y, w, h, color_border, active, image_background, color_background)

        self.sonido_fondo = 0.7 #_tiempo de la musica
        self.on = "Recursos/Menu/on.png"
        self.off = "Recursos/Menu/off.png"


        self.volumen = 0.2

        #_boton de regreso al menu principal
        self.back = Button(master=self, x=80,y=680, w=100, h=80, color_background=None, color_border=None, image_background="Recursos/Menu/Buttons/home.png",
                            on_click=self.on_click_boton1, on_click_param="Menu", text=None, font="Verdana", font_size=30, font_color=BLANCO)
        
        #_Volumne
        self.subir = Button(master=self, x=890, y=250, w=50, h=50, color_background=None, color_border=None, image_background="Recursos/Menu/Buttons/sube.png", 
                            on_click=self.on_click_subir_vol, on_click_param="Options", text=None, font="Verdana", font_size=30, font_color=BLANCO)       
        self.bajar = Button(master=self, x=600, y=250, w=50, h=50, color_background=None, color_border=None, image_background="Recursos/Menu/Buttons/baja.png", 
                            on_click=self.on_click_bajar_vol, on_click_param="Options", text=None, font="Verdana", font_size=30, font_color=BLANCO)
        
        self.pb1 = ProgressBar(master=self, x=650, y=250, w=240, h=50, color_background=None, color_border=None, image_background="Recursos/Other/vol_null.png",
                                image_progress="Recursos/Other/sube_baja.png", value=8, value_max=8)
        
        self.mute_desmute = Button(master=self, x=700, y=330, w=150, h=100, color_background=None, color_border=None, image_background="Recursos/Menu/on.png",
                                    on_click=self.on_click_boton_mute_desmute, on_click_param="Options", text=None, font="Verdana", font_size=30, font_color= BLANCO)
        
        self.text_sound = Widget(master_form=self, x=650, y=190, w=240,h=50, color_background=None, color_border=None, image_background=None, text="SONIDO", font="Arial", font_size=40, font_color=NEGRO)


        # self.label_volumen = Label(self, 450, 380, 100, 50, None, None, None, "20%","Arial", 15, BLANCO)
        # self.slider_volumen = Slider(master=self, master_x=x, master_y=y, x=100, y=400, w=300, h=10, color_background=BLANCO, color_border=None, image_background=None, 
        #                         text=None, font=None, font_size=None, font_color=None, value=self.volumen, color_circulo=BLANCO)
        
        #_lista de botones para activas buscando en la lista
        self.lista_widget = [self.back, self.subir, self.bajar, self.pb1, self.mute_desmute, self.text_sound]


        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
    
    #_funcion de subir volumen
    def on_click_subir_vol(self, parametro):
        if(self.pb1.value < self.pb1.value_max and self.mute_desmute.path_image != self.off):
            self.pb1.value +=1
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
            self.sonido_fondo += 0.1

    #_funcion de bajar volumen
    def on_click_bajar_vol(self, parametro):
        if(self.pb1.value >= 0 and self.mute_desmute.path_image != self.off):
            self.pb1.value -= 1
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
            self.sonido_fondo -= 0.1
            if(self.pb1.value <= 0):
                pygame.mixer.music.set_volume(0.0)

    #_activa y desactiva el sonido
    def on_click_boton_mute_desmute(self, parametro):
        if(self.mute_desmute.path_image == self.on):
            self.mute_desmute.path_image = self.off
            pygame.mixer.music.set_volume(0.0)
            self.mute_desmute.image_background = pygame.image.load(self.off).convert()

        elif(self.mute_desmute.path_image == self.off):
            self.mute_desmute.path_image = self.on
            pygame.mixer.music.set_volume(self.sonido_fondo)
            self.mute_desmute.image_background = pygame.image.load(self.on).convert()

        self.mute_desmute.image_background = pygame.transform.scale(self.mute_desmute.image_background, (self.mute_desmute.w, self.mute_desmute.h))

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        #self.update_volumen(lista_eventos)

    # def update_volumen(self, lista_eventos): #voy a estar actualizando la lista de eventos
    #     self.volumen = self.slider_volumen.value
    #     self.label_volumen.update(lista_eventos)
    #     self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
    #     pygame.mixer.music.set_volume(self.volumen)

    def draw(self):
        super().draw()
        self.surface.blit(self.image_background, self.image_background_rect)
        for aux_boton in self.lista_widget:
            aux_boton.draw()