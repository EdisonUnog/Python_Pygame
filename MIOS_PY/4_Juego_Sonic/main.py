import pygame, sys
from niveles.constantes import*
from niveles.Class_Colores import*
from niveles.Configuraciones import*
from niveles.modo import*

from Gui.gui_form_menu import*
from Gui.gui_menu_options import*
from Gui.gui_form_levels import*
from Gui.gui_form_pause import*
from Gui.gui_form_lvl1 import*
from Gui.gui_form_lvl2 import*
from Gui.gui_form_lvl3 import*
from Gui.gui_form_score_db import*
from Gui.gui_form_rankings import*
from Gui.gui_ranking import*

pygame.init()
pygame.mixer.music.load("Recursos/music/Vengeance.wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode(screen_size)        

menu = FormMenu("Menu", PANTALLA,0, 0, ANCHO, ALTO , NEGRO, True, image_background="Recursos/fondo/fondo_menu.jpg", color_background=None)
options = FormOptions("opciones", PANTALLA, 0, 0, ANCHO, ALTO, NEGRO, False, image_background="Recursos/fondo/fondo_options.jpg", color_background=None)
levels = FormLevels("niveles",PANTALLA,0,0,ANCHO, ALTO, NEGRO,False,image_background="Recursos/fondo/fondo_juego.jpg",color_background=None)

level_uno = LevelUno("nivel_uno",PANTALLA,0,0,ANCHO,ALTO, NEGRO,False,image_background=None,color_background=None)
level_dos = LevelDos("nivel_dos",PANTALLA,0,0,ANCHO,ALTO, NEGRO,False,image_background=None,color_background=None)
level_tres = LevelTres("nivel_tres",PANTALLA,0,0,ANCHO,ALTO, NEGRO,False,image_background=None,color_background=None)

pause = FormPauseLvl("pause",PANTALLA, ANCHO / 2 - 400 / 2,100,400,450,None,False,image_background="Recursos/Menu/Buttons/bg.png",color_background=None)

form_name_player = FormTextName("name_puntos",PANTALLA,0,0,ANCHO,ALTO,None,False,"Recursos/fondo/fondo_list_ranking.png",None)

form_clasifiaciones = FormClasificaciones("ranking",PANTALLA,0,0, ANCHO, ALTO, None, False,"Recursos/fondo/fondo_ranking.jpg",None)
puntos_db = FormRanking("Table_Data",PANTALLA, ANCHO / 2 - 350, ALTO / 2 -300, 700, 600, None, False, "Recursos/Menu/Buttons/Window.png",None) 

while True:
    reloj = RELOJ.tick(FPS)

    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    if(menu.active):
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
    

    pygame.display.update()
pygame.quit()