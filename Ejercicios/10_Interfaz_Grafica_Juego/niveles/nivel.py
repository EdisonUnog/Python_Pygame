import pygame, sys
from niveles.Class_Personaje import*
from niveles.Class_monedas import*
from niveles.modo import*

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, img_fondo) -> None:
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = img_fondo

    def update(self, lista_eventos):
        for event in lista_eventos:           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cambiar_modo()

        self.leer_inputs()
        self.actualizar_pantalla()
        self.dibujar_rect()

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0, 0))

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas)


    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.jugador.que_hace = "derecha"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_SPACE]:
            self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto"

    def dibujar_rect(self): #tab
        if get_mode(): # dibuja rect piso y rect personaje

            #for lado in lados_piso:
            #    pygame.draw.rect(PANTALLA, Colores.AZUL, lados_piso[lado], 2)

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, Colores.VERDE, self.jugador.lados[lado], 2)

            for i in range(len(self.plataformas)):
                    pygame.draw.rect(self._slave, Colores.ROJO, self.plataformas[i].rectangulo, 4)

            for plataforma in self.plataformas:
                for i in plataforma.lados:
                    pygame.draw.rect(self._slave, Colores.VERDE, plataforma.lados[i]  , 2)
        

