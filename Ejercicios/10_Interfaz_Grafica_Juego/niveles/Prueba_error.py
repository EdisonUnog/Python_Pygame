import pygame

pygame.init()

screen_size = (1000, 600)

PANTALLA = pygame.display.set_mode(screen_size)
fondo = pygame.image.load("fondo_space.png")
fondo = pygame.transform.scale(fondo, screen_size)


run = True
while (run):
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False
    
    PANTALLA.blit(fondo, (0, 0))

    pygame.display.update()
pygame.quit()