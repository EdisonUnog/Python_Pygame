import pygame
import block

   
class Mapa:
    def __init__(self) -> None:
        self.lista_block = []

    def constructor(self,map_draw):
        for fila_index, fila in enumerate(map_draw):
            for col_index,columna in enumerate(fila):
                x = col_index * 25
                y = fila_index * 25
                if columna == "x":
                    print("anda")
                    new_block = block.Block(x,y)
                    self.lista_block.append(new_block)

    def draw_map(self,screen):
        for blocke in self.lista_block:
            screen.blit(blocke.image,blocke.rect)








'''
def colision(rect,lista_bloques):
    for box in lista_bloques:
        if rect.colliderect(box):
            
            print("golpeo")
            return True
        else : 
            return False'''