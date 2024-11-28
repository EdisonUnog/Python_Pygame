import pygame

class Personaje:
    def __init__(self,x,y,speed) -> None:
        self.image = pygame.image.load("jogo/link.png")
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y    
        self.speed = speed
        self.stop = False

    def update(self,x_y,direccion):
        if x_y == "x":
            if direccion == "left":
                self.x = self.x -self.speed
            else :
                self.x = self.x + self.speed
        else :
            if direccion == "up":
                self.y = self.y -self.speed
            else :
                self.y = self.y + self.speed 
    
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
