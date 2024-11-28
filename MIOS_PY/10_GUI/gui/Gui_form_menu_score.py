import pygame

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
from sqlite.controller import*

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, path_image, margen_y, margen_x, espacio) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen

        self.lista_nombre = []
        self.lista_puntos = []

        self.lista_player = readRows()
        self.dict_score = {}
        self.dict_score = []

        #for i in range(len(self.lista_player)):
        for i in range(5):
            self.dict_score.append({"nombre":self.lista_player[i][1], "puntos":self.lista_player[i][2]})

            self.lista_nombre.append(self.lista_player[i][1])
            self.lista_puntos.append(self.lista_player[i][2])


        self._score = self.dict_score

        self._margen_y = margen_y

            #screen,x,y,w,h,text, font, font_size, font_color, path_image)
        lbl_jugador= Label(self._slave, x=margen_x + 10, y=20, w=w/2-margen_x-10, h=50, text="Jugador", font="Comic Sans", 
                            font_size=30, font_color=BLANCO, path_image="Recursos/menu/bar.png")
        
        lbl_puntaje = Label(self._slave, x=margen_x + 10 + w/2 - margen_x - 10, y=20, w=w/2-margen_x-10, h=50, text="Puntaje", font="Comic Sans", 
                                font_size=30, font_color=BLANCO, path_image="Recursos/menu/bar.png")
        
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)

        #_empezar a escribir los puntajes y jugadores
        pos_inicial_y = margen_y

        for j in self._score: #jugador, siguiente jugador 
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, w/2 - margen_x, 70, cadena, "Comic Sans", 
                                30, BLANCO, "Recursos/menu/Table.png")
                
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x            
            pos_inicial_y += 70 + espacio

        #_casita: retorno al menu principal
        self._btn_home = Button_Image(screen=self._slave, x= w / 2 - 25, y= h-90, master_x=x, master_y=y, w=50, h=50, 
                                        color_background=ROJO, color_border=FUCSIA, onclick=self.btn_home_click, 
                                        onclick_param="", text="", font="Comic Sans", font_size=15, font_color=(0,255,0), path_image="Recursos/menu/home.png")
        
        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self, texto): # me lleva al menu principal
        self.end_dialog()


    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)           
            self.draw()

            self.update_ranking(lista_eventos)



    def update_ranking(self, lista_eventos):

        self.lista_player = readRows()

        for i in range(len(self.lista_nombre)):
            self.lista_nombre[i] = self.lista_player[i][1]
            self.lista_puntos[i] = self.lista_player[i][2]

            self.dict_score.append({"nombre":self.lista_nombre[i], "puntos":self.lista_puntos[i]})









