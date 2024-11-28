import pygame, sys
from Gui.gui_barra_vida import*
from Gui.gui_botton import*
from Gui.gui_form_levels import*
from Gui.gui_form_lvl1 import*
from Gui.gui_form_lvl2 import*
from Gui.gui_form_lvl3 import*
from Gui.gui_form_menu import*
from Gui.gui_form_pause import*
from Gui.gui_form_rankings import*
from Gui.gui_form_score_db import*
from Gui.gui_form import*
from Gui.gui_menu_options import*
from Gui.gui_progressbar import*
from Gui.gui_ranking import*
from Gui.gui_textbox import*
from Gui.gui_widget import*                                             
from Niveles.constantes import*

pygame.init()

pygame.mixer.music.load("Recursos/music/Vengeance.wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)                     


screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
clock = pygame.time.Clock()

menu = FormMenu("Menu", screen,0, 0, ANCHO_VENTANA, ALTO_VENTANA, NEGRO, True, image_background="Recursos/fondo/fondo_menu.jpg", color_background=None)
options = FormOptions("Options", screen, 0, 0, ANCHO_VENTANA, ALTO_VENTANA, NEGRO, False, image_background="Recursos/fondo/fondo_options.jpg", color_background=None)
levels = FormLevels("levels",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,NEGRO,False,image_background="Recursos/fondo/fondo_juego.jpg",color_background=None)

level_uno = LevelUno("level_uno",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,NEGRO,False,image_background=None,color_background=None)
level_dos = LevelDos("level_dos",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,NEGRO,False,"Recursos/fondo/game_background_3. 2.png",color_background=None)
level_tres = LevelTres("level_tres",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,NEGRO,False,"Recursos/fondo/game_background_3. 2.png",None)

pause = FormPauseLvl("pause",screen,ANCHO_VENTANA / 2 - 400 / 2,100,400,450,None,False,image_background="Recursos/Menu/Buttons/bg.png",color_background=None)
form_name_player = FormTextName("name_player",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,False,"Recursos/fondo/game_background_3. 2.png",None)

form_clasifiaciones = FormClasificaciones("ranking",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,False,"Recursos/fondo/fondo_ranking.jpg",None)
puntos_db = FormRanking("Table_Data",screen,550,100,400,600,None,False,"Recursos/Menu/Buttons/Window.png",None) 


while True:

    reloj = clock.tick(FPS)

    eventos = pygame.event.get()
    for evento in eventos:
        if(evento.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    if (menu.active):
        menu.update(eventos)
        menu.draw()

    elif(options.active):
        options.update(eventos)
        options.draw()

    elif(pause.active):
        pause.update(eventos)
        pause.draw()

    elif(levels.active):
        levels.update(eventos)
        levels.draw()

    elif(level_uno.active):
        level_uno.draw()
        level_uno.update(reloj, eventos)
        
    elif(level_dos.active):
        level_dos.draw()
        level_dos.update(reloj, eventos)
    
    elif(level_tres.active):
        level_tres.draw()
        level_tres.update(reloj, eventos)

    elif(form_name_player.active and not level_tres.win_lvl3 or level_tres.win_lvl3):
        form_name_player.update(eventos)
        form_name_player.draw()
    
    elif(form_clasifiaciones.active):
        form_clasifiaciones.update(eventos)
        form_clasifiaciones.draw()

    elif(puntos_db.active):
        puntos_db.update(eventos)

    pygame.display.update() # actualiza mi pantalla
pygame.quit()
        