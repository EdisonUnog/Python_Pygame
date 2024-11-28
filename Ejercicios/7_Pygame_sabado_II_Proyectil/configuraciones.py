
import pygame

#_funcion que me da vuelta la imagen para cuando camine a la izquierda
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

#_reescalar o agrandar la imagen a la medida que desee
def reescalar_imagenes(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

# sueperficie asociado a un rect
def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario
    

personaje_quieto = [pygame.image.load("Recursos/Quieto/1.png")]  
personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True, False)

personaje_camina = [pygame.image.load("Recursos/Derecha/7.png"),
                    pygame.image.load("Recursos/Derecha/8.png"),
                    pygame.image.load("Recursos/Derecha/9.png"),
                    pygame.image.load("Recursos/Derecha/10.png"),
                    pygame.image.load("Recursos/Derecha/11.png"),
                    pygame.image.load("Recursos/Derecha/12.png")]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load("Recursos/Salta/2.png")]
personaje_salta_izquierda = girar_imagenes(personaje_salta, True, False)

personaje_dispara = [pygame.image.load("Recursos/Dispara/dispara.png")]
personaje_dispara_izquierda = girar_imagenes(personaje_dispara, True, False)

lista_proyectiles = [pygame.image.load("Recursos/Proyectiles/1.png"),
                    pygame.image.load("Recursos/Proyectiles/2.png"),
                    pygame.image.load("Recursos/Proyectiles/3.png"),
                    pygame.image.load("Recursos/Proyectiles/4.png"),
                    pygame.image.load("Recursos/Proyectiles/5.png"),
                    pygame.image.load("Recursos/Proyectiles/6.png"),
                    pygame.image.load("Recursos/Proyectiles/7.png")]


### Enemigos

mis_enemigos = [pygame.image.load("Recursos/Enemigo/enemigo1.png"),
                pygame.image.load("Recursos/Enemigo/enemigo2.png"),
                pygame.image.load("Recursos/Enemigo/enemigo3.png"),
                pygame.image.load("Recursos/Enemigo/enemigo4.png")]

mis_enemigo_izquierda = girar_imagenes(mis_enemigos, True, False)
