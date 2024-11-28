import pygame

ANCHO = 1500
ALTO = 800
scren_size = (ANCHO, ALTO)
FPS = 20

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
AQUA = (0,255,255)
AMARILLO = (255,255,0)
FUCSIA = (255,0,255)
GRIS = (37,37,37)

#########################################################################################################

#_funcion que me da vuelta la imagen para cuando camine a la izquierda
def girar_imagenes(lista_original, flip_x, flip_y): 
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

# paso una lista de imagenes y me las devuelve del tamaño que le pido
def reescalar_imagenes(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

# sueperficie asociado a un rectangulo principal de cualquier imagen
def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2 , rect_principal.top + 15, 2, rect_principal.height - 35)   
    diccionario["left"] = pygame.Rect(rect_principal.left , rect_principal.top + 15, 2, rect_principal.height - 35)
    return diccionario