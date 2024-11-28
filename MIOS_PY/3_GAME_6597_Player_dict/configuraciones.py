import pygame

########################################
#funcion que gira ma img a la izquierda 
def girar_imagenes(lista_img:list, flip_x, flip_y):

    lista_girada = []

    for img in lista_img:
        lista_girada.append(pygame.transform.flip(img, flip_x, flip_y))

    return lista_girada

########################################
#_me define el tamaño de la lista de las imagenes
def reescalar_img(lista_img:list, tamaño:tuple):
    for i in range(len(lista_img)):
        lista_img[i] = pygame.transform.scale(lista_img[i], tamaño)

########################################
#_sueperficie asociado a un rectangulo principal de cualquier imagen
#_rectangulo principal dentro de otros rectangulo
def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario


###########################################################################

#_listas de imagenes
personaje_quieto = [pygame.image.load("Recursos/Mover/Quieto/2.png")]
personaje_quieto_iz = girar_imagenes(personaje_quieto, True, False)

###_________
personaje_camina = [pygame.image.load("Recursos/Mover/Derecha/7.png"),
                    pygame.image.load("Recursos/Mover/Derecha/8.png"),
                    pygame.image.load("Recursos/Mover/Derecha/9.png"),
                    pygame.image.load("Recursos/Mover/Derecha/10.png"),
                    pygame.image.load("Recursos/Mover/Derecha/11.png"),
                    pygame.image.load("Recursos/Mover/Derecha/12.png")]

personaje_camina_iz = girar_imagenes(personaje_camina, True, False)

##________

personaje_salta = [pygame.image.load("Recursos/Mover/Salta/2.png")] 
personaje_salta_iz = girar_imagenes(personaje_salta, True, False)

##________
personaje_dispara = [pygame.image.load("Recursos/Mover/Dispara/dispara.png")] 
personaje_dispara_iz = girar_imagenes(personaje_dispara, True, False)


#__Diccionario Personaje

diccionario_personaje = {} # va en la funcion reescalar_animacion("aqui")
diccionario_personaje["quieto"] = personaje_quieto
diccionario_personaje["quieto_iz"] = personaje_quieto_iz
diccionario_personaje["salta"] = personaje_salta
diccionario_personaje["salta_iz"] = personaje_salta_iz
diccionario_personaje["camina_derecha"] =  personaje_camina
diccionario_personaje["camina_iz"] = personaje_camina_iz
diccionario_personaje["dispara"] = personaje_dispara
diccionario_personaje["dispara_iz"] = personaje_dispara_iz