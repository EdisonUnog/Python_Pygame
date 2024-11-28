from gui.Gui_Widget import*
from niveles.constantes import*


class Form(Widget):
    def __init__(self, screen, x, y, w, h, color_background, color_border=NEGRO, border_size=-1, active = True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        self._slave = pygame.Surface((w,h))
        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None

    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self
    
    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_resul(self):
        return self.hijo == None or self.hijo.dialog_result != None
    
    def render(self):
        super().render()

    def update(self, lista_eventos):
        pass


# class Form:
#     def __init__(self, screen, x, y, w, h, color_background, color_border=NEGRO, border_size=-1, active = True) -> None:
#         #super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

#         self._slave = pygame.Surface((w,h))
#         self.slave_rect = self._slave.get_rect()
#         self.slave_rect.x = x
#         self.slave_rect.y = y
#         self.active = active
#         self.lista_widgets = []
#         self.hijo = None
#         self.dialog_result = None
#         self.padre = None

#         self.pantalla = screen
#         self._color_border = color_border
#         self._color_background = color_background
#         self.border_size = border_size


#     def show_dialog(self, formulario):
#         self.hijo = formulario
#         self.hijo.padre = self
    
#     def end_dialog(self):
#         self.dialog_result = "OK"
#         self.close()

#     def close(self):
#         self.active = False

#     def verificar_dialog_resul(self):
#         return self.hijo == None or self.hijo.dialog_result != None
    
#     def render(self):
#         pass

#     def update(self, lista_eventos):
#         pass

#     def draw(self):
#         self.pantalla.blit(self._slave, self.slave_rect)
#         pygame.draw.rect(self.pantalla, self._color_border, self.slave_rect, self.border_size)