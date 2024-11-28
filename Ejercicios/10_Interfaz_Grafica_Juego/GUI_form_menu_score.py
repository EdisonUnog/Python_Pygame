import pygame
from pygame.locals import*
from Class_Colores import*
from GUI_button import*

from GUI_form import*
from GUI_Label import*
from GUI_button_imagen import*
from GUI_widget import*

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, score, margen_y, margen_x, espacio) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self._score = score

        self._margen_y = margen_y

        lbl_jugador= Label(self._slave, x=margen_x + 10, y=15, w=w/2-margen_x-10, h=50, text="Jugador", font="Comic Sans", font_size=30, font_color=BLANCO, path_image="bar.png")
        
        lbl_puntaje = Label(self._slave, x=margen_x + 10 + w/2 - margen_x - 10, y=15, w=w/2-margen_x-10, h=50, text="Puntaje", font="Comic Sans", font_size=30, font_color=BLANCO, path_image="bar.png")
        
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)

        #_empezar a escribir los puntajes y jugadores
        pos_inicial_y = margen_y

        for j in self._score: #jugador, siguiente jugador 
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, w/2 - margen_x, 70, cadena, "Comic Sans", 30, BLANCO, "Table.png")
                print(cadena)
                
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x            
            pos_inicial_y += 70 + espacio

        #_casita: retorno al menu principal
        self._btn_home = Button_Image(screen=self._slave, master_x=x, master_y=y, x= w/2-25, y=h-80, w=50, h=50, 
                                        color_background=ROJO, color_border=FUCSIA, onclick=self.btn_home_click, 
                                        onclick_param="", text="", font="Comic Sans", font_size=15, font_color=(0,255,0), path_image="home.png")
        
        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self, texto): # me lleva al menu principal
        self.end_dialog()


    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)           
            self.draw()





