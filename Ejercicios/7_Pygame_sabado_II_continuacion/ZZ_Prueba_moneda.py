
## image_files = ["Monedas/moneda1.png", "Monedas/moneda2.png", "Monedas/moneda3.png", "Monedas/moneda4.png"]

import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Clase del personaje
class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_PANTALLA // 2
        self.rect.y = ALTO_PANTALLA - 70

    def update(self):
        # Mover el personaje con las teclas de flecha izquierda y derecha
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

        # Evitar que el personaje salga de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO_PANTALLA - 50:
            self.rect.x = ANCHO_PANTALLA - 50

# Clase del proyectil
class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()

# Inicializar pantalla
pantalla = pygame.display.set_mode([ANCHO_PANTALLA, ALTO_PANTALLA])
pygame.display.set_caption("Personaje Disparando")

# Crear grupo de sprites
sprites = pygame.sprite.Group()

# Crear personaje
personaje = Personaje()
sprites.add(personaje)

# Variable para controlar el tiempo de disparo
tiempo_disparo = pygame.time.get_ticks()

# Bucle principal del juego
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    # --- Procesamiento de eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Disparar proyectil si han pasado al menos 500 milisegundos desde el último disparo
                if pygame.time.get_ticks() - tiempo_disparo > 500:
                    proyectil = Proyectil(personaje.rect.x + 20, personaje.rect.y)
                    sprites.add(proyectil)
                    tiempo_disparo = pygame.time.get_ticks()

    # --- Lógica del juego ---
    sprites.update()

    # --- Renderizado ---
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    reloj.tick(60)

# Cerrar Pygame
pygame.quit()




