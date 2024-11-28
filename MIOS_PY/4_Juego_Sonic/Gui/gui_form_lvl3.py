import pygame, sys
from Gui.gui_form import*
from Gui.gui_botton import*
from Gui.gui_botton import*
from Gui.gui_widget import*
from Gui.gui_textbox import*
from Gui.gui_barra_vida import*
from niveles.constantes import*

class LevelTres(Form):
    def __init__(self, name, master_form, x, y, w, h, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_form, x, y, w, h, color_border, active, image_background, color_background)

        self.master_form = master_form
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_border = color_border
        self.active = active
        self.image_background = image_background
        self.color_background = color_background

        #Lista con la información total del level 2.
        self.lista_info = Datalevels(master_form,"nivel_tres")

        #Imagen de fondo que va a tener el nivel 2.
        self.imagen_fondo = pygame.image.load("Recursos/Materiales/Fondos/fondo_level_1.png").convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO,ALTO))

        #El player del nivel y su barra de vida.
        self.barra_vida = BarraVida(self,x=10,y=10,w=500,h=50,color_background=NEGRO,color_border=AZUL,image_background=None,image_progress=None,
                                    value = self.lista_info.player.hp, value_max=self.lista_info.player.hp,color_vida=BLANCO)
        
        self.image_vida = Widget(self,512,10,45,45,None,None,"Recursos/Menu/heart.png",None,"Arial",None,None)

        #Lista piso.
        self.lista_pisos= self.lista_info.lista_pisos

        #Lista plataformas.
        self.lista_plataformas = self.lista_info.lista_plataformas

        #Lista frutas.
        self.monedas = self.lista_info.lista_monedas

        #Lista Trampas
        self.trampas = self.lista_info.lista_trampas

        #Puntos.
        self.score = Widget(self,1300,0,200,50,None,None,"Recursos/Menu/Buttons/fondo_botones.png",self.lista_info.player.puntos_player,"Arial",30,NEGRO)
        self.puntos_totales = self.lista_info.player.puntos_player

        #Tiempo.
        self.time_juego = 60
        self.acumulador_time = 0
        self.time = Widget(self,650,0,200,50,None,None,"Recursos/Menu/Buttons/fondo_botones.png",self.time_juego,"Arial",30,NEGRO)
        self.image_time = Widget(self,850,5,50,50,None,None,"Recursos/Menu/clock.png",None,"Arial",None,None)
        self.tick_1s = pygame.USEREVENT+0
        pygame.time.set_timer(self.tick_1s,1000)

        #ganó O perdió.
        self.win_lvl3 = self.lista_info.win
        self.win = Widget(self,x,y,w,h,None,None,"Recursos/Menu/Buttons/you win.png",None,"Arial",30,NEGRO)
        self.lose = Widget(self,x,y,w,h,None,None,"Recursos/Menu/Buttons/you lose.png",None,"Arial",30,NEGRO)
        
        #Lista de widgets.
        self.lista_widget = [self.time,self.score,self.image_time,self.image_vida]
        
    def draw(self):
        super().draw()
        '''
        Dibuja en el formulario el fondo.
        '''
        self.surface.blit(self.imagen_fondo,(0,0))

    def resetear(self):
        '''
        El metodo resetea el nivel, para volver a jugar.
        '''
        self.__init__(self.name,self.master_form,self.x,self.y,self.w,self.h,self.color_border,self.active,self.image_background,self.color_background)
        
        
    def update(self,delta_ms,lista_events):
        '''
        El metodo updatea todo lo necesario para podrucir el nivel 1.
        Recibe por parametro el tiempo actual del juego y la lista de eventos.
        '''
        
        if(not self.lista_info.win and not self.lista_info.player.muerte and self.time_juego > 0):
            #Información total del lvl 1.
            self.lista_info.update(delta_ms)
            
            #Widgets.
            for aux_widget in self.lista_widget:    
                aux_widget.update(lista_events)
                aux_widget.draw()

            #Score.
            self.score.update(lista_events)
            self.score._text = self.lista_info.player.puntos_player
            self.puntos_totales = self.lista_info.player.puntos_player
            
            #Tiempo.
            self.time.update(lista_events)
            self.time._text = self.time_juego
            
            #Player y su barra de vida.
            # self.lista_info.player.update(delta_ms,self.lista_plataformas,self.lista_enemigos,lista_events,self.lista_info.lista_plataformas)
            # self.lista_info.player.draw()

            self.lista_info.player.update(self.master_form, self.lista_pisos, self.lista_plataformas, self.trampas)
            self.barra_vida.update(lista_events,self.lista_info.player.hp)
            self.barra_vida.draw()

        elif(self.lista_info.win):  
            self.win_lvl3 = True
            self.win.update(lista_events)
            self.win.draw()
            self.display_finish_lvl(delta_ms)
                
        elif(self.lista_info.player.muerte or self.time_juego <= 0):
            self.lose.update(lista_events)
            self.lose.draw()
            self.display_finish_lvl(delta_ms)
        
        #Eventos
        for event in lista_events:
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.set_active("pause")
            if (event.type == self.tick_1s):
                self.time_juego -= 1


    def display_finish_lvl(self,delta_ms):
        '''
        El metodo activa segun la condicion un formulario cuando finaliza el nivel, ya sea consiguiendo el objetivo o perdiendo por muerte o tiempo y resetea el nivel.
        '''
        self.acumulador_time += delta_ms
        if(self.acumulador_time >= 2000):
            
            #self.set_active("guardar_puntos")
            self.set_active("name_puntos")
            self.forms_dict["name_puntos"].puntos_totales = self.puntos_totales
            self.resetear()
            self.acumulador_time = 0