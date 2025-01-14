import pygame, sys
from pygame.locals import*
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen_width = 1000
screen_height = 1000
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("plataformas Part 10 score, text")

#defone font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

# dedfine game variables
tile_size = 50
game_over = 0
main_menu = True
level = 0
max_levels = 7
score = 0

# define colors
white = (255, 255, 255)
blue = (0, 0, 255)

#load img
sun_img = pygame.image.load("img/sun.png")
bg_img = pygame.image.load("img/sky.png")

restart_img = pygame.image.load("img/restart_btn.png")
start_img = pygame.image.load("img/start_btn.png")
exit_img = pygame.image.load("img/exit_btn.png")

##############################################################################################################

def draw_grid():  #dibujar cuadrícula
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

##############################################################################################################

# text in screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

##############################################################################################################

# function to reset level
def reset_level(level):
    player.reset(100, screen_height - 130)
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()

    #load in level data and cretae world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')  #level es una variables definida al inicio
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world

##############################################################################################################

class Button():
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):

        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                #print("click")
                action = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #draw button
        screen.blit(self.image, self.rect)

        return action

##############################################################################################################
class Player():
    def __init__(self, x,y) -> None:

        self.reset(x, y)

    def update(self, game_over):
        #posicion del jugador
        dx = 0
        dy = 0
        walk_cooldown = 5

        if game_over == 0:
            # get key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False: #salto
                self.vel_y = -15
                self.jumped = True 
            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_a]:
                dx -= 5
                self.counter += 1
                self.direccion= -1

            if key[pygame.K_d]:
                dx += 5
                self.counter += 1
                self.direccion = 1

            if key[pygame.K_a] == False and key[pygame.K_d] == False:
                self.counter = 0
                self.index = 0
                if self.direccion == 1:
                    self.image = self.images_right[self.index]
                if self.direccion == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direccion == 1:
                    self.image = self.images_right[self.index]
                if self.direccion == -1:
                    self.image = self.images_left[self.index]

            #add gravity __ caida del salto
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            self.in_air = True #solo salta una vez en el aire
            for tile in world.tile_list:
                #check for collision in x direccion
                if tile[1].colliderect(self.rect.x + dx, self.rect.y , self.width, self.height):
                    dx = 0

                #check for collision in y direccion
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the group i. e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0

                    #check if below the group i. e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            #check for collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
            
            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            #check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0

        elif game_over == -1:
            self.image = self.dead_image
            draw_text('GAME OVER!', font, blue, (screen_width // 2) - 150, screen_height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        #draw player anto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, "Red", self.rect, 2)

        return game_over
    
    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(1, 5):
            img_right = pygame.image.load(f"img/guy{num}.png")
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)

            self.images_right.append(img_right)
            self.images_left.append(img_left)
        
        self.dead_image = pygame.image.load("img/ghost.png") #cuando el player collisiona y muere
        self.image = self.images_right[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False 
        #importante
        self.direccion = 0

        self.in_air = True

##############################################################################################################

# calculate new player position. ---  calcular la posición del nuevo jugador.
# check collision at new position.  ---  Compruebe la colisión en la nueva posición.
# adjust player position. ---  ajustar la posición del jugador

class World():
    def __init__(self, data) -> None:

        self.tile_list = []
        #load img
        dirt_img = pygame.image.load("img/dirt.png")
        grass_img = pygame.image.load("img/grass.png")

        row_count = 0
        for row in data:

            col_count = 0
            for tile in row:

                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    blob_group.add(blob)

                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)

                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                
                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, "Black", tile[1], 1)

##############################################################################################################

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/blob.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direccion = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direccion
        self.move_counter += 1
        if abs(self.move_counter > 50):
            self.move_direccion *= -1
            self.move_counter *= -1

##############################################################################################################

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("img/lava.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

##############################################################################################################

class Coin(pygame.sprite.Sprite): #moneda
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("img/Coin.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

##############################################################################################################

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("img/exit.png")
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

##############################################################################################################

'''world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]'''

player = Player(100, screen_height - 130)
blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

#create dummy coin for showing the escore
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

#load in level data and cretae world
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')  #level es una variables definida al inicio
    world_data = pickle.load(pickle_in)
world = World(world_data)

#create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

##############################################################################################################

run = True
while (run):

    clock.tick(FPS)

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100, 100))

    if main_menu == True:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False

    else:
        world.draw() #draw img matriz

        if game_over == 0:
            blob_group.update()
            #update score
            #check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
            draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)

        blob_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        #if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        #if player has completed the level
        if game_over == 1:
            #reset game and go to next level
            level += 1
            if level <= max_levels:
                #reset level...
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text('YOU WIN', font, blue, (screen_width // 2) - 140, screen_height // 2)
                #reset game
                if restart_button.draw():
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0
    
    lista_eventos = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
pygame.quit()



'''
if keys[pygame.K_ESCAPE]:
    run = False
'''