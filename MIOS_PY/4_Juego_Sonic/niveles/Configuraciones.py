import pygame

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
# img de pisos
pisos_img = [pygame.image.load("Recursos/Pisos/piso1.png"),
            pygame.image.load("Recursos/Pisos/piso2.png"),
            pygame.image.load("Recursos/Pisos/piso3.png")]

#########################################################################################################
# img de personaje
personaje_quieto = [pygame.image.load("Recursos/Personaje/Quieto/947.png")]
Personaje_quieto_izq = girar_imagenes(personaje_quieto, True, False)

personaje_camina_izq = [pygame.image.load("Recursos/Personaje/Camina/4.png"),
                        pygame.image.load("Recursos/Personaje/Camina/5.png"),
                        pygame.image.load("Recursos/Personaje/Camina/6.png"),
                        pygame.image.load("Recursos/Personaje/Camina/7.png")]
personaje_camina = girar_imagenes(personaje_camina_izq, True, False)

personaje_dispara_izq = [pygame.image.load("Recursos/Personaje/Dispara/266.png")]
personaje_dispara = girar_imagenes(personaje_dispara_izq, True, False)

personaje_agachado_izq = [pygame.image.load("Recursos/Personaje/Agacharse/25.png")]
personaje_agachado = girar_imagenes(personaje_agachado_izq, True, False)

personaje_salta_izq = [pygame.image.load("Recursos/Personaje/Salta/448.png")]
personaje_salta = girar_imagenes(personaje_salta_izq, True, False)

#########################################################################################################
#_Plataformas

monedas_img = [pygame.image.load("Recursos/Materiales/monedas_trampolin/0.png"),
                pygame.image.load("Recursos/Materiales/monedas_trampolin/1.png"),
                pygame.image.load("Recursos/Materiales/monedas_trampolin/2.png"),
                pygame.image.load("Recursos/Materiales/monedas_trampolin/3.png"),
                pygame.image.load("Recursos/Materiales/monedas_trampolin/5.png"),
                pygame.image.load("Recursos/Materiales/monedas_trampolin/6.png"),
                pygame.image.load("Recursos/Materiales/monedas_trampolin/7.png")]

#########################################################################################################
#_Sierras
cierra_img = [pygame.image.load("Recursos/Materiales/Trampas/1.png"),
                pygame.image.load("Recursos/Materiales/Trampas/2.png"),
                pygame.image.load("Recursos/Materiales/Trampas/3.png"),
                pygame.image.load("Recursos/Materiales/Trampas/4.png")]

cierra_img_izq = girar_imagenes(cierra_img, True, False)
