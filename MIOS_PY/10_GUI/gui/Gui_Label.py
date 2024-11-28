import pygame, sys
from pygame.locals import *
from gui.Gui_Widget import*
from niveles.constantes import*


# class Label(Widget):
#     def __init__(self, screen,x,y,w,h,text, font, font_size, font_color, path_image):
#         super().__init__(screen, x, y, w, h)

#         self._text = text
#         self.path_image = path_image

#         self._slave = pygame.Surface((self._w, self._h), pygame.SRCALPHA)
#         self.slave_rect = self._slave.get_rect()
#         self.slave_rect.x = self._x
#         self.slave_rect.y = self._y

#         if(self.path_image != None): #_carga y escala la imagen ingresada
#             self.image_background = pygame.image.load(self.path_image) 
#             self.image_background = pygame.transform.scale(self.image_background, (w, h))
#         else:
#             self.image_background = None

#         if(self._text != None): #_Texto ingresado "text"
#             pygame.font.init()
#             self._font_sys = pygame.font.SysFont(font, font_size)
#             self._font_color = font_color

#     def render(self):
#         #_mantenemos actualizado el widget, ya sea que se ingreso nuevo texto o imagen
#         if(self.image_background == None):
#             self._slave.fill(self._color_background)

#         if(self.image_background != None):
#             self._slave.blit(self.image_background, (0,0))

#         if (self._text != None):
#             self._text = str(self._text)
#             self._slave.blit(self.image_background , (0, 0)) 
#             image_text = self._font_sys.render(self._text, True, self._font_color)
            
#             media_texto_horizontal = image_text.get_width() / 2
#             media_texto_vertical = image_text.get_height() / 2

#             media_horizontal = self._w / 2
#             media_vertical = self._h / 2 - 3
#             diferencia_horizontal = media_horizontal - media_texto_horizontal 
#             diferencia_vertical = media_vertical - media_texto_vertical
            
#         self._slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))

    
#     def set_text(self, text):
#         self._text = text
#         self.render()

#     def get_text(self):
#         return self._text
    
#     def update(self, lista_eventos):
#         self.render()


class Label(Widget):
    def __init__(self, screen,x,y,w,h,text, font, font_size, font_color, path_image):
        super().__init__(screen, x, y, w, h)
        
        pygame.font.init()

        self._text = text
        self._font = pygame.font.SysFont(font, font_size)
        self._font_color = font_color
        #if path_image != "":
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        #else:
            # aux_image = pygame.Surface((w,h))
            #aux_image.set_alpha(0)#Transparente
            
        self._slave = aux_image
        self.img_original = aux_image.copy()
            
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y

        self.render()

    
    def render(self):
        self._text = str(self._text)
        self._slave.blit(self.img_original, (0, 0)) 
        image_text = self._font.render(self._text, True, self._font_color)
        
        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self._w / 2
        media_vertical = self._h / 2 - 3
        diferencia_horizontal = media_horizontal - media_texto_horizontal 
        diferencia_vertical = media_vertical - media_texto_vertical
        
        self._slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))
    
    def set_text(self, text):
        self._text = text
        self.render()

    def get_text(self):
        return self._text
    
    def update(self, lista_eventos):
        self.draw()
        self.render()