import pygame, sys
from pygame.locals import*
from Gui.gui_widget import*
from Niveles.constantes import*

class BarraVida(Widget):
    def __init__(self, master, x=0, y=0, w=200, h=50, color_background=VERDE, color_border=ROJO, image_background=None, color_vida=BLANCO, image_progress=None, value=1, value_max=5) -> None:
        super().__init__(master, x, y, w, h, color_background, color_border, image_background, None, None, None, None)

        self.color_vida = color_vida
        self.barra = pygame.Rect(0, 0, w, h)

        self.value_min = 0
        self.value = value_max
        self.value_max = value_max

    def render_vida(self, player_hp):
        #_vida del personaje, recibe por parametro la vida actualizada
        super().render()
        self.barra.w = player_hp * self.w / self.value_max
        self.slave_surface.fill(self.color_vida, self.barra)

    def update(self, lista_eventos, player_hp):
        self.render_vida(player_hp)
        
