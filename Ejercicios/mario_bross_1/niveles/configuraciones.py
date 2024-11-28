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


# sueperficie asociado a un rectangulo principal de cualquier imagen
def obtener_rectangulo(rect_principal) -> dict:
    diccionario = {} #va tener rect
    diccionario["main"] = rect_principal
    diccionario["bottom"] = pygame.Rect(rect_principal.left, rect_principal.bottom - 10, rect_principal.width, 10)
    diccionario["right"] = pygame.Rect(rect_principal.right - 2, rect_principal.top, 2, rect_principal.height)
    diccionario["left"] = pygame.Rect(rect_principal.left, rect_principal.top, 2, rect_principal.height)
    diccionario["top"] = pygame.Rect(rect_principal.left, rect_principal.top, rect_principal.width, 10)
    return diccionario

#########################################################################################################

#_listas de imagenes
personaje_quieto = [pygame.image.load("Quieto/2.png"),
                    pygame.image.load("Quieto/2.png"),
                    pygame.image.load("Quieto/2.png"),
                    pygame.image.load("Quieto/3.png"),
                    pygame.image.load("Quieto/3.png"),
                    pygame.image.load("Quieto/3.png")]

personaje_camina = [pygame.image.load("Derecha/7.png"),
                    pygame.image.load("Derecha/8.png"),
                    pygame.image.load("Derecha/9.png"),
                    pygame.image.load("Derecha/10.png"),
                    pygame.image.load("Derecha/11.png"),
                    pygame.image.load("Derecha/12.png")]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
#_Ture: gira en las X
#_False: no gira en las Y, sino queda patas arriba

personaje_salta = [pygame.image.load("Salta/2.png")] #img por defecto esta a la deracha

personaje_abajo = [pygame.image.load("Abajo_Muere/1.png")]

personaje_salta_izquierda = girar_imagenes(personaje_salta, True, False) # cuando se mantiene del lado que esta

#########################################################################################################
#____________PLATAFORMAS__________

plataformas_img = [pygame.image.load("Plataformas/0.png"),
                    pygame.image.load("Plataformas/1.png"),
                    pygame.image.load("Plataformas/2.png"),
                    pygame.image.load("Plataformas/3.png"),
                    pygame.image.load("Plataformas/meta2.png")]

piso1 = pygame.image.load("Recursos/fondo_1.1.png")
piso2 = pygame.image.load("Recursos/fondo_2.2.png")
piso3 = pygame.image.load("Recursos/fondo_3.3.png")

bandera_meta = pygame.image.load("Plataformas/bandera.png")


#########################################################################################################
#____________MONEDAS__________

mis_monedas = [pygame.image.load("Monedas/moneda1.png"),
                pygame.image.load("Monedas/moneda2.png"),
                pygame.image.load("Monedas/moneda3.png"),
                pygame.image.load("Monedas/moneda4.png"),
                pygame.image.load("Monedas/moneda5.png")]

mis_enemigos = [pygame.image.load("Enemigo/enemigo1.png"),
                pygame.image.load("Enemigo/enemigo2.png"),
                pygame.image.load("Enemigo/enemigo3.png"),
                pygame.image.load("Enemigo/enemigo4.png")]

mis_enemigo_izquierda = girar_imagenes(mis_enemigos, True, False)

