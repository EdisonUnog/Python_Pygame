import pygame
from pygame.locals import*
from Gui.gui_widget import*
from Niveles.constantes import*

class Button(Widget):
    def __init__(self, master, x=0, y=0, w=200, h=50, color_background=VERDE, color_border=ROJO, image_background=None, text=None, font="Arial", font_size=14, font_color=AZUL, on_click=None, on_click_param=None) -> None:
        super().__init__(master, x, y, w, h, color_background, color_border, image_background, text, font, font_size, font_color)

        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.render()

    def render(self):
        super().render() #renderiza el texto del boton a la imagen

        # if self.state == M_STATE_HOVER: # Se aclara la imagen
        #     self.slave_surface.fill(M_STATE_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        # elif self.state == M_BRIGHT_CLICK: # Se oscurece la imagen
        #     self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB)

    def update(self, lista_eventos):

        #_actualiza la posicion del mouse y las colliciones (click).
        #_recibe por parametro el evento que va a buscar en la lista

        self.render()
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL

        if(self.slave_rect_collide.collidepoint(mousePos)):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_BRIGHT_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if(evento.type == pygame.MOUSEBUTTONDOWN):
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)
