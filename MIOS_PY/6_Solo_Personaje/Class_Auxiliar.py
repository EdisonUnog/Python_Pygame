import pygame,sys
from Constantes import*

class Auxiliar:
    #def cargarImagen(path_format, cantidad, flip=False,step = 1, escala=1,w=0, h=0, marco=1):
    def cargarImagen(path_format, cantidad, flip=False, escala=1,w=0, h=0):
        lista_imagenes = []
        rango = 1

        for i in range(rango, cantidad + rango):

            path = path_format.format(i)
            img = pygame.image.load(path)

            ancho_img = int(img.get_rect().w * escala)
            alto_img = int(img.get_rect().h * escala)

            if(escala == 1 and w != 0 and h != 0):
                img = pygame.transform.scale(img, (w, h)).convert_alpha()
            if(escala != 1):
                img = pygame.transform.scale(img, (ancho_img, alto_img)).convert_alpha()
            if(flip):
                img = pygame.transform.flip(img, True, False).convert_alpha()

            for i in range(rango):
                lista_imagenes.append(img)

        return lista_imagenes