import pygame
import personaje as personaje_f
pygame.init()
ancho_ventana = 720
alto_ventana = 540

ventana = pygame.display.set_mode([ancho_ventana,alto_ventana])
fondo = pygame.image.load("fondobrand.jpg")
pygame.display.set_caption("jogo spider")
player = personaje_f.crear(ancho_ventana/2,alto_ventana-200,200,200)

run_prg=True
while run_prg:
    
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            run_prg=False

    ventana.blit(fondo,(0,0))

    personaje_f.actualizar_pantalla(player,ventana)
    personaje_f.update(player, -1)

    pygame.display.update() 
pygame.quit()
