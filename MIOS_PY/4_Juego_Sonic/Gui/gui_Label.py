import pygame
from Gui.gui_widget import*

class Label(Widget):
    def __init__(self, master_form, x, y, w, h, color_background, color_border, image_background, text, font, font_size, font_color) -> None:
        super().__init__(master_form, x, y, w, h, color_background, color_border, image_background, text, font, font_size, font_color)

        pygame.font.init()

        self.render()
    
    def render(self):
        super().render()
    
    def set_text(self, text):
        self._text = text
        self.render()

    def get_text(self):
        return self._text
    
    def update(self, lista_eventos):
        self.draw()