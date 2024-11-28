import pygame
from gui.Gui_Form import*
from niveles.constantes import*

class BarraVida(Form):
    def __init__(self, screen, x=0, y=0, w=200, h=50, color_background=VERDE,color_border=ROJO, border_size=-1, color_vida=BLANCO, value=1, value_max=5) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        self.color_vida = color_vida
        self.barra = pygame.Rect(0, 0, w, h)

        self.value_min = 0
        self.value = value_max
        self.value_max = value_max

    def render_vida(self, player_hp):
        super().render()
        self.barra.w = player_hp * self._w / self.value_max
        self._slave.fill(self.color_vida, self.barra)

    def update(self, lista_eventos, player_hp):
        self.render_vida(player_hp)