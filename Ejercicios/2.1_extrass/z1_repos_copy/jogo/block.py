import pygame
import niveles_data

class Block:
    def __init__(self,x,y) -> None:
        self.image = pygame.image.load("jogo/block.png")
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #def draw(self,screen):
    #    screen.blit(self.image,(self.x,self.y))
