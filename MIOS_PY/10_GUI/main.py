import pygame, sys
from niveles.constantes import*
from gui.Gui_Widget import* 
from gui.Gui_Slider import*
from gui.Gui_Label import*
from gui.Gui_Form_Principal import*
from gui.Gui_Barra_Vida import*
from niveles.Class_trampa import*
from gui.Gui_Agg_score import*

from gui.Gui_Nivel_Uno import*

pygame.init()

PANTALLA = pygame.display.set_mode(scren_size)
reloj = pygame.time.Clock()


Form_Principal = FormPrincipal(PANTALLA, 0, 0, ANCHO,  ALTO, GRIS, AQUA, 4, True)


run = True
while (run):

    delta= reloj.tick(FPS)
    eventos = pygame.event.get()
    kEYS = pygame.key.get_pressed()
    PANTALLA.fill(GRIS)

    for event in eventos:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    Form_Principal.update(eventos)

    
    if kEYS[pygame.K_ESCAPE]:
        run = False

    pygame.display.update()
pygame.quit()









'''volumen = 0.2
#_Musica_fondo
pygame.mixer.music.load("Recursos/music/Vengeance.wav")
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1)

def update_volumen(lista_eventos):
    volumen = slider_volumen.value
    label_volumen.set_text(f"{round(volumen * 100)}%")
    pygame.mixer.music.set_volume(volumen)

#widget = Widget(PANTALLA, 500, 150, 500, 500, None, AQUA,5)
slider_volumen = Slider(PANTALLA, 0, 0, 50, 200, 300, 15, volumen, AQUA, BLANCO)
# "Recursos/menu/Table.png"
label_volumen = Label(PANTALLA, 400, 180, 100, 50, "20%", "Comic Sans", 15, BLANCO, "Recursos/menu/Table.png") 


#dentro del while:
#label_volumen.draw()
    label_volumen.update(eventos)
        
    #slider_volumen.draw()
    slider_volumen.update(eventos)
    update_volumen(eventos)'''