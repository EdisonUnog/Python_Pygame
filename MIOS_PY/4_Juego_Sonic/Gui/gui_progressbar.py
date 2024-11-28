import pygame, sys
from Gui.gui_form import*
from Gui.gui_botton import*
from Gui.gui_botton import*
from Gui.gui_widget import*

class ProgressBar(Widget):
    def __init__(self, master, x=0, y=0, w=200, h=50, color_background=VERDE, color_border=ROJO, image_background=None, image_progress=None, value=1, value_max=5) -> None:
        super().__init__(master, x, y, w, h, color_background, color_border, image_background, None, None, None, None)

        self.surface_element = pygame.image.load(image_progress)
        self.surface_element = pygame.transform.scale(self.surface_element, (w/value_max, h)).convert_alpha()
        self.master = master

        self.value = value
        self.value_max = value_max
        self.render()

    def render(self):
        super().render()
        for x in range(self.value):
            self.slave_surface.blit(self.surface_element, (x*self.w / self.value_max, 0))

    def update(self, lista_elementos):
        self.render()