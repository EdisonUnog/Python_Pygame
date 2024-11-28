import pygame, sys

pygame.init()

width = 500
height = 400
size = (width, height)

PANTALLA = pygame.display.set_mode(size) #px
pygame.display.set_caption("miprimer juego")

#pygame.draw.circle(PANTALLA,(0,0,255), (250,250), 75)

PANTALLA.fill("Red")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.circle(PANTALLA,(0,0,255), (250,250), 75)
    pygame.draw.rect(PANTALLA, (255, 255, 0), (30, 30, 60, 60))

    pygame.display.flip()