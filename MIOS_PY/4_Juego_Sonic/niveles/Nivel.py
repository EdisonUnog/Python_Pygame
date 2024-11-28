import pygame, sys

from niveles.modo import*
from niveles.Class_Colores import*
#########################################################################################################

class Nivel:
    def __init__(self, pantalla, personaje, list_pisos, mis_monedas, plataformas, trampas, fondo) -> None:
        self._slave_An = pantalla.get_width()
        self._slave_Al = pantalla.get_height()

        self._slave = pantalla
        self.personaje = personaje
        self.plataformas = plataformas
        self.monedas = mis_monedas
        self.pisos = list_pisos
        self.trampas = trampas
        self.fondo = fondo

#########################################################################################################
                
    def update(self, lista_eventos, fps):
        for event in lista_eventos:           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cambiar_modo()

        self.actualizar_pantalla(fps)
        self.leer_inputs()
        self.dibujar_rect()

#########################################################################################################

    def actualizar_pantalla(self, fps):
        self._slave.blit(self.fondo, (0, 0))

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)
            plataforma.update(fps)

        for piso in self.pisos:
            piso.draw(self._slave)

        for moneda in self.monedas:
            moneda.draw(self._slave)

        for trampa in self.trampas:
            trampa.draw(self._slave)
            trampa.mover_x(self._slave_An)

        self.personaje.update(self._slave, self.pisos, self.plataformas, self.trampas)

#########################################################################################################
            
    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.personaje.un_salto == False:
            self.personaje.que_hace = "salta"
        
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.personaje.que_hace = "derecha"
            self.personaje.direccion = 1
    
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.personaje.que_hace = "izquierda"
            self.personaje.direccion = -1

        elif keys[pygame.K_l] and self.personaje.un_salto == False:
            self.personaje.que_hace = "dispara"

        elif keys[pygame.K_s] and self.personaje.un_salto == False:
            self.personaje.que_hace = "agachar"

        else:
            self.personaje.que_hace = "quieto"

        if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            False


        if keys[pygame.K_l] == False:
            self.personaje.disparando = False


        if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)

#########################################################################################################
                
    def dibujar_rect(self): #tab
        if get_mode(): # dibuja rect piso y rect personaje
            # for i in range(len(self.pisos)):
            #     pygame.draw.rect(self._slave, Colores.AZUL, self.pisos[i].rectangulo, 4)

            for piso in self.pisos:
                for i in piso.lados:
                    pygame.draw.rect(self._slave, Colores.AZUL, piso.lados[i]  , 2)

            for plat in self.plataformas:
                for i in plat.lados:
                    pygame.draw.rect(self._slave, Colores.BLANCO, plat.lados[i]  , 2)

