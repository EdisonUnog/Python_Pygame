import pygame

class Mundo():
    def __init__(self, data, long_lineas, long_alto) -> None:
        
        self.column = long_alto #x
        self.lineas = long_lineas #y

        self.bloque_lista = []

        bloque_1 = pygame.image.load('img/1.png')
        bloque_2 = pygame.image.load('img/2.png')
        bloque_3 = pygame.image.load('img//3.png')

        cont_linea = 0

        for fila in data:
            cont_col = 0
            for num_bloque in fila:

                if num_bloque == 1:
                    img = pygame.transform.scale(bloque_1, (self.column, self.lineas))
                    img_rect = img.get_rect()
                    img_rect.x = cont_col * self.column
                    img_rect.y = cont_linea * self.lineas
                    lados = obtener_rectangulo(img_rect)
                    bloque = (img, img_rect)
                    self.bloque_lista.append(bloque)

                if num_bloque == 2:
                    img = pygame.transform.scale(bloque_2, (self.column, self.lineas))
                    img_rect = img.get_rect()
                    img_rect.x = cont_col * self.column
                    img_rect.y = cont_linea * self.lineas
                    lados = obtener_rectangulo(img_rect)
                    bloque = (img, img_rect)
                    self.bloque_lista.append(bloque)
                    
                if num_bloque == 3:
                    img = pygame.transform.scale(bloque_3, (self.column, self.lineas))
                    img_rect = img.get_rect()
                    img_rect.x = cont_col * self.column
                    img_rect.y = cont_linea * self.lineas
                    lados = obtener_rectangulo(img_rect)
                    bloque = (img, img_rect)
                    self.bloque_lista.append(bloque)
                
                cont_col += 1
            cont_linea += 1

    def draw(self, pantalla):
        for bloque in self.bloque_lista:
            pantalla.blit(bloque[0], bloque[1])


def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario