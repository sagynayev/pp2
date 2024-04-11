import pygame
import sys
from pygame.locals import *
import random
import time

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 100, 100)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCOREENEMY = 0
SCORECOINS = 0
COINCOLLECTED = 0
NEWCOIN = 1
SCORECOINCHECK = 0
HEVCOINCOLLECTED = 0
NEWHEVCOIN = 1
SCOREHEVCOINCHECK = 0
MUSICPLAYG = 0
COINVISIBLE = 1
HEVCOINVISIBLE = 1

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("pp2/lab8/racer/resources/AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#creating enemy sprite 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pp2/lab8/racer/resources/Enemy.png") #image of enemy's car
        self.rect = self.image.get_rect() #creating rectangle around a image of enemy 
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) #spawning enemy in random range of x axis

    def move(self):
        global SCOREENEMY
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600: #if statement for checking that enemy will leave from the screen
            SCOREENEMY += 1 #number of enemy passed
            self.rect.top = 0 #changing position of enemy to the top of the screen
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #spawning enemy in random range of x axis

#creating player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pp2/lab8/racer/resources/Player.png") #image of player's car
        self.rect = self.image.get_rect() #creating rectangle around a image of player
        self.rect.center = (160, 520) #initial position of player's car
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0: #checking for not leaving from the screen
            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0) #changing coordinate of x when pressing left or a keys
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0) #changing coordinate of x when pressing right or d keys


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab8/racer/resources/coin.PNG") #image of coin
        self.image = pygame.transform.scale(self.image, (60, 60)) #changing resolution of coin's image
        self.rect = self.image.get_rect() #creating rectangle around a image of coin
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0) #random spawn

    def move(self):
        global SCORECOINS
        global COINCOLLECTED
        COINCOLLECTED = 0
        self.rect.move_ip(0, SPEED) #chaning y coordinate of coin
        if self.rect.bottom > 600: #checking for not leaving from the screen
            self.rect.top = 0 #changing position of coin to the top of the screen
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #random spawn
            global SCORECOINCHECK
            SCORECOINCHECK = 0 
        if self.rect.bottom < 100:
            global NEWCOIN
            NEWCOIN = 1

class HeavyCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab8/racer/resources/hev_coin.png") #loading an image of heavy coin
        self.image = pygame.transform.scale(self.image, (60, 60)) #changing resolution of heavy coin image
        self.rect = self.image.get_rect() #creating rectangle around a heavy coin image
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0) #random spawn

    def move(self):
        global SCORECOINS
        global HEVCOINCOLLECTED

        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 650:
            self.rect.top = 0
            HEVCOINCOLLECTED = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0) #random spawn
            global SCOREHEVCOINCHECK
            SCOREHEVCOINCHECK = 0
        if self.rect.bottom < 100:
            global NEWHEVCOIN
            NEWHEVCOIN = 1

def play_music():
    pygame.mixer.music.load("pp2/lab8/racer/resources/background.wav")
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()


# Creating objects of sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
HC1 = HeavyCoin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
heavy_coins = pygame.sprite.Group()
heavy_coins.add(HC1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 500) #creating a timer for speed

# Game Loop
while True:
    # Play music at the beginning
    if not MUSICPLAYG:
        play_music()
        MUSICPLAYG = 1

    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED: #checking for inc_speed occurence, so the speed will change
            SPEED += 0.2
        if event.type == QUIT: #quit 
            pygame.quit()
            sys.exit()

    # Print background and scores
    DISPLAYSURF.blit(background, (0, 0))
    scores_en = font_small.render(str(SCOREENEMY), True, BLACK)
    DISPLAYSURF.blit(scores_en, (10, 10))
    scores_coin = font_small.render("Coins: " + str(SCORECOINS), True, BLACK)
    DISPLAYSURF.blit(scores_coin, (SCREEN_WIDTH - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect) #displaying player and enemy sprites

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        stop_music()
        time.sleep(1/3) #delay after player hits enemy
        pygame.mixer.Sound('pp2/lab8/racer/resources/crash.wav').play() #sound of crash
        time.sleep(1) #delay after sound

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250)) #displaying text of game over
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Move coins
    C1.move()
    HC1.move()

    if pygame.sprite.spritecollideany(P1, coins):
        if COINVISIBLE: #checking if coin is on the screen, it is initially visiable
            SCORECOINCHECK = 1 #we are using this variable for adding value to the total score
            COINCOLLECTED = 1 #we are using this variable for checking if coin is collected or not

    if pygame.sprite.spritecollideany(P1, heavy_coins):
        if HEVCOINVISIBLE: #checking if heavy coin on the screen
            SCOREHEVCOINCHECK = 1
            HEVCOINCOLLECTED = 1

    # Continue displaying coin if not
    if not COINCOLLECTED: #if player didn't collect coin it will be continue to display
        if not pygame.sprite.spritecollideany(E1, coins): #this if statement helps us to prevent cases when enemies and coins are on the same position
            for entity in coins:
                DISPLAYSURF.blit(entity.image, entity.rect)
                COINVISIBLE = 1
        else:
            COINVISIBLE = 0
    
    else:
        if SCORECOINCHECK == 1 and NEWCOIN == 1:
            SCORECOINS += 1
            NEWCOIN = 0



    # Continue displaying coin if not
    if not HEVCOINCOLLECTED:
        if not pygame.sprite.spritecollideany(E1, heavy_coins):
            if not pygame.sprite.spritecollideany(C1, heavy_coins):
                for entity in heavy_coins:
                    DISPLAYSURF.blit(entity.image, entity.rect)
                    HEVCOINVISIBLE = 1
            else:
                HEVCOINVISIBLE = 0
        else:
            HEVCOINVISIBLE = 0
    # Plus score if collected
    else:
        if SCOREHEVCOINCHECK == 1 and NEWHEVCOIN == 1:
            SCORECOINS += 3
            NEWHEVCOIN = 0
        
    pygame.display.update()
    FramePerSec.tick(FPS)