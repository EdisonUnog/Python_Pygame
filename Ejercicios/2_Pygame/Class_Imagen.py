import pygame

class Imagen:
    def __init__(self, tamaño, origen, colores) -> None:
        self.imagen = pygame.Surface(tamaño) #tupla valores
        self.color = colores[0]
        self.color_collision = colores[1]
        
        self.imagen.fill(self.color) #pinto imagen
        self.rectangulo = self.imagen.get_rect() # creo el rectangulo
        self.rectangulo.center = origen

    def mover_imagen(self, sentido:str, desplazamiento:int, tamaño_pantalla:tuple):
        if sentido == "Vertical":
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top > tamaño_pantalla[1] :
                self.rectangulo.bottom = 0

        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > tamaño_pantalla[0]:
                self.rectangulo.right = 0

    def detectar_colision(self, otra_imagen):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.imagen.fill(self.color_collision)
            otra_imagen.imagen.fill(otra_imagen.color_collision)
        else:
            self.imagen.fill(self.color)
            otra_imagen.imagen.fill(otra_imagen.color)
