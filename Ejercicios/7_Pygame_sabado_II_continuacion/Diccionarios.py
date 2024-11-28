
import pygame
from configuraciones import*

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

#__Diccionaro_Monedaas
'''
diccionario_monedas = {}
diccionario_monedas["moneda"] = monedas_img'''

diccionario_bala = {}
diccionario_bala["derecha"] = proyectiles
diccionario_bala["izquierda"] = proyectiles_iz