import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coin_speed_dollar = 5
coin_speed_ruble = 3
coin_score = 0


# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading images
background = pygame.image.load("Images/AnimatedStreet.png")
enemy_image = pygame.image.load("Images/Enemy.png")
player_image = pygame.image.load("Images/Player.png")
coin_ruble_image = pygame.image.load("Images/coin_ruble.png")
coin_dollar_image = pygame.image.load("Images/coin_dollar.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Class for enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Class for player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Class for coin
class CoinDollar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_dollar_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global dollar
        self.rect.move_ip(0, coin_speed_dollar)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class CoinRuble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_ruble_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global ruble
        self.rect.move_ip(0, coin_speed_ruble)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Hole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.y += SPEED

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = CoinDollar()
C2 = CoinRuble()

coin_r = pygame.sprite.Group()
coin_r.add(C2)

# Creating Sprites Groups
coin = pygame.sprite.Group()
coin.add(C1)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

level = 1
process = True
hole_count = 0
hole_standart = 5
holes = pygame.sprite.Group()

# Game Loop
while process:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    scores = font_small.render(f"SCORE: {SCORE}", True, RED)
    DISPLAYSURF.blit(scores, (10, 10))

    level_text = font_small.render(f"LEVEL: {level}", True, BLACK)
    DISPLAYSURF.blit(level_text, (150, 10))

    score_of_coin = font_small.render(f"Coin Score: {coin_score}", True, BLACK)
    DISPLAYSURF.blit(score_of_coin, (250, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if SCORE % hole_standart == 0 and SCORE > 0 and hole_count == 0:
        hole = Hole()
        holes.add(hole)
        all_sprites.add(hole)
        hole_count += 1

    if pygame.sprite.spritecollideany(P1, holes):
        pygame.mixer.Sound("Sounds/crash.wav").play()
        holes.empty()
        hole_count += 1
        if hole_count >= 2:
            pygame.mixer.Sound('Sounds/crash.wav')
            time.sleep(0.5)
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(4)
            pygame.quit()
            sys.exit()

    if pygame.sprite.spritecollideany(P1, coin):
        pygame.mixer.Sound("Sounds/sound_coin_selection.mp3").play()
        coin_speed_dollar += 0.5
        coin_score += 1
        C1.rect.y = -100
        C1.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    if pygame.sprite.spritecollideany(P1, coin_r):
        pygame.mixer.Sound("Sounds/sound_coin_selection.mp3").play()
        coin_speed_ruble += 0.3
        coin_score += 1
        C2.rect.y = -100
        C1.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('Sounds/crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(4)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
