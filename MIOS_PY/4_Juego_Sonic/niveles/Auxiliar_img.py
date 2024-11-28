import pygame

class Auxiliar:
    def get_img(path, colum, filas, flip = False, step = 1, scale = 1):

        lista_img = []
        imagen = pygame.image.load((path)).convert_alpha()
        ancho = int(imagen.get_width() / colum)
        alto = int(imagen.get_height() / filas)
        ancho_scaled = int(ancho * scale)
        alto_scaled = int(alto * scale)

        x = 0

        for fila in range(filas):
            for colum in range(0, colum,step):
                x = colum * ancho
                y = fila * alto
                img = imagen.subsurface(x, y,ancho,alto)
                if(scale != 1):
                    img = pygame.transform.scale(img, (ancho_scaled, alto_scaled)).convert_alpha()
                
                if(flip):
                    img = pygame.transform.flip(img, True, False).convert_alpha()

                lista_img.append(img)
        
    
    def cargarImagen(path_format, quantity, flip=False,step = 1, scale=1, w=0, h=0, frame=1):
        lista_plataforma = []
        for i in range(1, quantity + 1):
            path = path_format.format(i)

            img = pygame.image.load(path)
            ancho_scaled = int(img.get_rect().w * scale)
            alto_scaled = int(img.get_rect().h *scale)
            
            if(scale == 1 and w != 0 and h != 0):
                img = pygame.transform.scale(img, (w, h)).convert_alpha()
            if(scale != 1):
                img = pygame.transform.scale(img, (ancho_scaled, alto_scaled)).convert_alpha()
            if(flip):
                img = pygame.transform.flip(img, True, False).convert_alpha()

            for i in range(frame):
                lista_plataforma.append(img)
        return lista_plataforma
            

    def cargarImagen2(path_format, cantidad, flip=False,step = 1, escala=1,w=0, h=0, marco=1):
        lista_plataforma = []

        for i in range(1, cantidad + 1):

            path = path_format.format(i)
            img = pygame.image.load(path)

            ancho_img = int(img.get_rect().w * escala)
            alto_img = int(img.get_rect().h * escala)

            if(escala == 1 and w != 0 and h != 0):
                img = pygame.transform.scale(img, (ancho_img, alto_img)).convert_alpha()
            if(escala != 1):
                img = pygame.transform.scale(img, (ancho_img, alto_img)).convert_alpha()
            if(flip):
                img = pygame.transform.scale(img, True, False).convert_alpha()

            for i in range(marco):
                lista_plataforma.append(img)

        return lista_plataforma