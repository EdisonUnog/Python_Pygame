import pygame
from Class_Proyectil import*

class Player():
    def __init__(self, x, y, w, h, ancho_P, alto_p) -> None:

        self.ancho_p = ancho_P
        self.alto_p = alto_p

        self.img_derecha = []
        self.img_izquierda = []

        self.indice = 0
        self.contar = 0

        for num in range(1, 8):
            img_derecha = pygame.image.load(f"img/player{num}.png")
            img_derecha = pygame.transform.scale(img_derecha, (w, h))
            img_izquierda = pygame.transform.flip(img_derecha, True, False)

            self.img_derecha.append(img_derecha)
            self.img_izquierda.append(img_izquierda)

        self.imagenes = self.img_derecha[self.indice]
        self.ancho_img = self.imagenes.get_width()
        self.alto_img = self.imagenes.get_height()

        self.rect = self.imagenes.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocidad_y = 0
        self.saltando = False
        self.un_salto = True

        # a que lado mira el personaje
        self.direccion = 0
        self.disparando = False

        #lista de proyectiles
        self.lista_disparos = []
        self.disparos = False
        self.velocidad_disparos = 10

    def update(self, pantalla, mundo, player):
        # pos del jugador 
        dx = 0
        dy = 0
        caminar_enfriamiento = 4

        # teclas para animar
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.saltando == False and self.un_salto == False:
            self.velocidad_y = -14
            self.saltando = True
        if keys[pygame.K_SPACE] == False:
            self.saltando = False

        if keys[pygame.K_a]:
            dx -= 5
            self.contar += 1
            self.direccion = -1

        if keys[pygame.K_d]:
            dx += 5
            self.contar += 1
            self.direccion = 1
        
        # tecla disparar
        if keys[pygame.K_l]:
            x, y = player.rect.center
            player.dispara(x, y, self.direccion, self.velocidad_disparos)
            self.disparando = True

        if keys[pygame.K_l] == False:
            self.disparando = False

        if len(player.lista_disparos) > 0:
            for x in player.lista_disparos:
                x.update(pantalla)
                x.mover()

                if x.rect.x < 10:
                    player.lista_disparos.remove(x)
                if x.rect.x > self.ancho_p - 10:
                    player.lista_disparos.remove(x)

        if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            self.contar = 0
            self.indice = 0
            if self.direccion == 1:
                self.imagenes = self.img_derecha[self.indice]
            if self.direccion == -1:
                self.imagenes = self.img_izquierda[self.indice]

        # manejar animacion
        if self.contar > caminar_enfriamiento:
            self.contar = 0
            self.indice += 1
            if self.indice >= len(self.img_derecha):
                self.indice = 0
            if self.direccion == 1:
                self.imagenes = self.img_derecha[self.indice]
            if self.direccion == -1:
                self.imagenes = self.img_izquierda[self.indice]
            
        # gravedad al caer del salto
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10
        dy += self.velocidad_y

        # collision con las plataformas
        self.un_salto = True
        for linea in mundo.bloque_lista:
            # comprobar si hay colisión en la dirección x
            if linea[1].colliderect(self.rect.x + dx, self.rect.y, self.ancho_img, self.alto_img):
                dx = 0
            # comprobar si hay colisión en la dirección y
            if linea[1].colliderect(self.rect.x, self.rect.y + dy, self.ancho_img, self.alto_img):
                #verificar si debajo del grupo i. mi. saltando
                if self.velocidad_y < 0:
                    dy = linea[1].bottom - self.rect.top
                    self.velocidad_y = 0
                
                elif self.velocidad_y >= 0:
                    dy = linea[1].top - self.rect.bottom
                    self.velocidad_y = 0
                    self.un_salto = False

        #actualizar las coordenadas del jugador
        self.rect.x += dx
        self.rect.y += dy
    
        if self.rect.bottom > self.alto_p:
            self.rect.bottom = self.alto_p
            dy = 0

        #dibujaer en la pantalla
        pantalla.blit(self.imagenes, self.rect)

    def dispara(self, x, y, direccion, velocidad):
        miProyectil = Proyectil(x, y, lista_proyectiles, direccion, velocidad)
        self.lista_disparos.append(miProyectil)