
#caracteristicas
    #Cantidad_Pasajeros
    #velocidad
    #km_totales
    #distancia_recorrida

#Comoportamiento

import pygame

class Transporte:

    def __init__(self, cantidad:int, velocidad:float):
        self.cantidad_pasajeros = cantidad #publico
        self.velocidad = velocidad
        self.km_totales = 0
        self.distancia_recorrida = 0

    def avanzar(self):
        print("*esta avanzando ")

    def frenar(self):
        print("*esta frenando ")

    def mostrar(self):
        print(f"\n*********{type(self)}************")
        print(f" *Cantidad pasajeros: {self.cantidad_pasajeros}, Velocidad: {self.velocidad}, Destino: {self.km_totales}")