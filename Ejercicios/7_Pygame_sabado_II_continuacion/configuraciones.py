
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
    

personaje_quieto = [pygame.image.load("Quieto/4.png"),
                    pygame.image.load("Quieto/5.png"),
                    pygame.image.load("Quieto/6.png"),
                    pygame.image.load("Quieto/7.png")]  

personaje_quieto_iz = girar_imagenes(personaje_quieto, True, False)

personaje_camina = [pygame.image.load("Camina/Adelante/0.png"),
                    pygame.image.load("Camina/Adelante/1.png"),
                    pygame.image.load("Camina/Adelante/2.png"),
                    pygame.image.load("Camina/Adelante/3.png")]

personaje_camina_iz = girar_imagenes(personaje_camina, True, False)


personaje_salta = [pygame.image.load("Salta/0.png")]
personaje_salta_iz = girar_imagenes(personaje_salta, True, False)

personaje_dispara = [pygame.image.load("dispara.png")]
personaje_dispara_iz = girar_imagenes(personaje_dispara, True, False)



proyectiles = [pygame.image.load("Proyectiles/1.png"),
                    pygame.image.load("Proyectiles/2.png"),
                    pygame.image.load("Proyectiles/3.png"),
                    pygame.image.load("Proyectiles/4.png"),
                    pygame.image.load("Proyectiles/5.png"),
                    pygame.image.load("Proyectiles/6.png"),
                    pygame.image.load("Proyectiles/7.png")]

proyectiles_iz = girar_imagenes(proyectiles, True, False)

plataforma_uno = pygame.image.load("plataforma.png")
plataforma_dos = pygame.image.load("plataforma.png")



##############################################################
#___________MONEDAS_______________
lista_monedas = [pygame.image.load("Monedas/moneda1.png"),
                pygame.image.load("Monedas/moneda2.png"),
                pygame.image.load("Monedas/moneda3.png"),
                pygame.image.load("Monedas/moneda4.png"),
                pygame.image.load("Monedas/moneda5.png")]