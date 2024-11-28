import pygame, sys

from niveles.Class_Monedas import*
from niveles.Class_Nivel_Uno import*
from niveles.modo import*

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, lista_monedas, lista_enemigos, ubicar, img_fondo) -> None:
        self._slave = pantalla
        self._slave_ancho = pantalla.get_width()
        self._slave_alto = pantalla.get_height()
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.monedas = lista_monedas
        self.enemigos = lista_enemigos
        self.posicion = ubicar
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

        for moneda in self.monedas:
            moneda.draw(self._slave, self.jugador, self.monedas)

        for enemigo in self.enemigos:
            enemigo.update(self._slave)
            enemigo.collicion_enemigo(self.jugador, self.enemigos)
            enemigo.pierde(self.jugador, self.enemigos, (self._slave_alto/2 - 350, 710))

        self.posicion(self.enemigos, self._slave_ancho)
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

        if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)


    def dibujar_rect(self): #tab
        if get_mode(): # dibuja rect piso y rect personaje

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, Colores.VERDE, self.jugador.lados[lado], 2)

            for i in range(len(self.plataformas)):
                    pygame.draw.rect(self._slave, Colores.ROJO, self.plataformas[i].rectangulo, 4)

            for plataforma in self.plataformas:
                for i in plataforma.lados:
                    pygame.draw.rect(self._slave, Colores.VERDE, plataforma.lados[i]  , 2)

            for enemigo in self.enemigos:
                for i in enemigo.lados:
                    pygame.draw.rect(self._slave, Colores.VERDE, enemigo.lados[i]  , 2)
        

