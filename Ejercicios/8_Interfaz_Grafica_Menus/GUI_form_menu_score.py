import pygame
from pygame.locals import*
from Class_Colores import Colores
from GUI_button import Colores

from GUI_form import*
from GUI_Label import*
from GUI_button_imagen import*
from GUI_widget import Colores

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, score, margen_y, margen_x, espacio) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self._score = score

        self._margen_y = margen_y

        lbl_jugador= Label(self._slave, x=margen_x + 10, y=20, w=w/2-margen_x-10, h=50, text="Jugador", 
                            font="Verdana", font_size=30, font_color="White", path_image="bar.png")
        
        lbl_puntaje = Label(self._slave, x=margen_x + 10 + w/2 - margen_x - 10, y=20, w=w/2-margen_x-10, h=50, text="Puntaje", 
                            font="Verdana", font_size=30, font_color="White", path_image="bar.png")
        
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)

        #_empezar a escribir los puntajes y jugadores
        pos_inicial_y = margen_y

        for j in self._score: #jugador, siguiente jugador 
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, w/2 - margen_x, 100, cadena, "Verdana", 
                                30, "White", "Table.png")
                
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x            
            pos_inicial_y += 100 + espacio

        #_casita: retorno al menu principal
        self._btn_home = Button_Image(screen=self._slave, x=w-70, y=h-70, master_x=x, master_y=y, w=50, h=50, 
                                        color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, 
                                        onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="home.png")
        
        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self, texto): # me lleva al menu principal
        self.end_dialog()


    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)           
            self.draw()





