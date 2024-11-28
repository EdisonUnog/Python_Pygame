import pygame
from niveles.configuraciones import*

#_PERSONAJE
diccionario_persona = {}
diccionario_persona["quieto"] = personaje_quieto
diccionario_persona["salta"] = personaje_salta
diccionario_persona["camina_derecha"] = personaje_camina
diccionario_persona["camina_izquierda"] = personaje_camina_izquierda
diccionario_persona["abajo"] = personaje_abajo

diccionario_enemigo = {}
diccionario_enemigo["derecha"] = mis_enemigos
diccionario_enemigo["izquierda"] = mis_enemigo_izquierda