import pygame


def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista_imagenes, ancho, alto):
    for lista in lista_imagenes:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i], (ancho, alto))


personaje_quieto = [pygame.image.load("Quieto/4.png"),
                    pygame.image.load("Quieto/5.png"),
                    pygame.image.load("Quieto/6.png"),
                    pygame.image.load("Quieto/7.png")]

personaje_camina = [pygame.image.load("Camina/Adelante/0.png"),
                    pygame.image.load("Camina/Adelante/1.png"),
                    pygame.image.load("Camina/Adelante/2.png"),
                    pygame.image.load("Camina/Adelante/3.png")]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load("Salta/0.png")]