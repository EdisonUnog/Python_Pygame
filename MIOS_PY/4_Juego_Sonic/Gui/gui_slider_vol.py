import pygame
from Gui.gui_widget import*
import math

class Slider(Widget):
    def __init__(self, master, master_x, master_y, x, y, w, h, color_background, color_border, image_background, text, font, font_size, font_color, value, color_circulo) -> None:
        super().__init__(master, x, y, w, h, color_background, color_border, image_background, text, font, font_size, font_color)

        self.value = value 
        self.color_circulo = color_circulo
        self._slave = pygame.Surface((w,y))

        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += master_x
        self.slave_rect_collide.y += master_y
        
        w_circle = w / 20
        h_circle = h * 2.5
        self.rectangulo_circulo = pygame.Rect(0, 0, w_circle, h_circle)
        self.rectangulo_circulo.center = (x + w * value, self.slave_rect.centery)

        diagonal = math.sqrt(w_circle ** 2 + h_circle ** 2)
        self.radio_circulo = diagonal / 2

        self.render()
    
    def render(self):
        self._slave.fill(self.color_background)

        
    def draw(self):
        super().draw()
        #pygame.draw.circle(self.master_form, self.color_circulo, self.rectangulo_circulo.center, self.radio_circulo)

    def circle(self):
        super().circle()
        pygame.draw.circle(self.master_form, self.color_circulo, self.rectangulo_circulo.center, self.radio_circulo)

    def update(self, lista_eventos):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.slave_rect_collide.collidepoint(mouse_pos):
                valor = (mouse_pos[0] - self.slave_rect_collide.x) / self._slave.get_width()
                
                self.value = round(valor * 100) / 100 # redondeo el valor
                
                self.rectangulo_circulo.center = (self.slave_rect.x + self._slave.get_width() * self.value, self.slave_rect.centery)
        #self.draw()

    def get_value(self):
        return self.value
