import pygame

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

# def obtener_rectangulo(rect_principal) -> dict:
#     diccionario = {} #va tener rect
#     diccionario["main"] = rect_principal
#     diccionario["top"] = pygame.Rect(rect_principal.x  , rect_principal.y , rect_principal.w , 10)
#     diccionario["bottom"] = pygame.Rect(rect_principal.x , rect_principal.y + rect_principal.h - 5, rect_principal.w, 10)
#     diccionario["right"] = pygame.Rect(rect_principal.x + rect_principal.w - 5, rect_principal.y + 15, 5, rect_principal.h - 25)
#     diccionario["left"] = pygame.Rect(rect_principal.x, rect_principal.y + 15 , 5, rect_principal.h - 25)
#     return diccionario

# sueperficie asociado a un rectangulo principal de cualquier imagen
def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2 , rect_principal.top + 15, 2, rect_principal.height - 35)   
    diccionario["left"] = pygame.Rect(rect_principal.left , rect_principal.top + 15, 2, rect_principal.height - 35)
    return diccionario

# def obtener_rectangulo(rect_principal) -> dict:
#     diccionario = {} #va tener rect
#     diccionario["main"] = rect_principal
#     diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
#     diccionario["right"] = pygame.Rect(rect_principal.right -2 , rect_principal.top, 2, rect_principal.height)
#     diccionario["left"] = pygame.Rect(rect_principal.left , rect_principal.top, 2, rect_principal.height)
#     diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
#     return diccionario


#########################################################################################################

# #_listas de imagenes
# personaje_quieto = [pygame.image.load("Recursos/Personaje/Quieto/1.png"),
#                     pygame.image.load("Recursos/Personaje/Quieto/2.png"),
#                     pygame.image.load("Recursos/Personaje/Quieto/3.png"),
#                     pygame.image.load("Recursos/Personaje/Quieto/4.png")]

# personaje_quieto_iz = girar_imagenes(personaje_quieto, True, False)

# personaje_camina = [pygame.image.load("Recursos/Personaje/Camina/1.png"),
#                     pygame.image.load("Recursos/Personaje/Camina/2.png"),
#                     pygame.image.load("Recursos/Personaje/Camina/3.png"),
#                     pygame.image.load("Recursos/Personaje/Camina/4.png")]

# personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
# #_Ture: gira en las X
# #_False: no gira en las Y, sino queda patas arriba

# personaje_salta = [pygame.image.load("Recursos/Personaje/Salta/1.png")] #img por defecto esta a la deracha
# personaje_salta_iz = girar_imagenes(personaje_salta, True, False) # cuando se mantiene del lado que esta



# personaje_dispara = [pygame.image.load("Recursos/Dispara/dispara.png")]
# personaje_dispara_iz = girar_imagenes(personaje_dispara, True, False)

# #_Lista de Proyectiles
# lista_proyectiles = [pygame.image.load("Recursos/Proyectiles/1.png"),
#                     pygame.image.load("Recursos/Proyectiles/2.png"),
#                     pygame.image.load("Recursos/Proyectiles/3.png"),
#                     pygame.image.load("Recursos/Proyectiles/4.png"),
#                     pygame.image.load("Recursos/Proyectiles/5.png"),
#                     pygame.image.load("Recursos/Proyectiles/6.png"),
#                     pygame.image.load("Recursos/Proyectiles/7.png")]



#########################################################################################################
# img de pisos
# pisos_img = [pygame.image.load("Recursos/Pisos/piso0.png"),
#             pygame.image.load("Recursos/Pisos/piso1.png"),
#             pygame.image.load("Recursos/Pisos/piso2.png"),
#             pygame.image.load("Recursos/Pisos/piso3.png"),
#             pygame.image.load("Recursos/Pisos/piso4.png")]

