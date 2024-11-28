import pygame
from niveles.Class_Plataformas import *


#_PLATAFORMAS
#                          tamaño         imagen           posicion

lista_plataformas = [Plataforma((150, 45), plataformas_img[1], (250, 680)),
                    Plataforma((55, 45), plataformas_img[0], (170, 570)),
                    Plataforma((55, 45), plataformas_img[0], (290, 450)),
                    Plataforma((55, 45), plataformas_img[0], (470, 450)),
                    Plataforma((55, 45), plataformas_img[0], (670, 450)),
                    
                    Plataforma((55, 45), plataformas_img[0], (770, 330)),
                    Plataforma((55, 45), plataformas_img[0], (610, 230)),
                    Plataforma((450, 45), plataformas_img[3], (30, 130)),
                    Plataforma((225, 45), plataformas_img[2], (950, 540)),
                    Plataforma((55, 45), plataformas_img[0], (1200, 420)),
                    Plataforma((55, 45), plataformas_img[0], (1300, 300)),
                    Plataforma((150, 45), plataformas_img[1], (1100, 200)),
                    
                    Plataforma((150, 110), plataformas_img[4], (1490, 10)),
                    Plataforma((250, 45), plataformas_img[2], (1440, 120))]

bandera_1 = Bandera((25, 25), bandera_meta, (1555, 95))

