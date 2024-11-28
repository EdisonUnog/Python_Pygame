import pygame
from niveles.Configuraciones import*

#_Personaje
dict_Personaje = {}
dict_Personaje["quieto_der"] = personaje_quieto
dict_Personaje["quieto_izq"] = Personaje_quieto_izq
dict_Personaje["salta_der"] = personaje_salta
dict_Personaje["salta_izq"] = personaje_salta_izq
dict_Personaje["camina_derecha"] = personaje_camina
dict_Personaje["camina_izquierda"] = personaje_camina_izq
dict_Personaje["dispara_der"] = personaje_dispara
dict_Personaje["dispara_izq"] = personaje_dispara_izq
dict_Personaje["agachado_der"] = personaje_agachado
dict_Personaje["agachado_izq"] = personaje_agachado_izq

######################################################################

diccionario_cierra = {}
diccionario_cierra["derecha"] = cierra_img
diccionario_cierra["izquierda"] = cierra_img_izq