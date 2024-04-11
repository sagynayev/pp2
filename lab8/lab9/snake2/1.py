# Imports
import pygame
import time
import random
import sys

# Initializg
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 500))

# Setting FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Program global vars
GREEN = (100, 200, 100)
BLACK = (0, 0, 0)
SCORE = 0
SCOREAPPLECHECK = 0
APPLECOLLECTED = 0
NEWAPPLE = 1
SCOREFRUITS = 0
SCOREPEARCHECK = 0
PEARCOLLECTED = 0
NEWPEAR = 1
SCOREBANANACHECK = 0
BANANACOLLECTED = 0
NEWBANANA = 1
BANANATIME = 0
NOBANANATIME = 0
SCORE4 = 4
SCOREUNDER4 = 8
LEVEL = 1
LENGTH = 1
ALLSNAKE = []
DIR = 0
KEYBEFORE = 0
MUSICPLAYG = 0
SPEED = 3
check = 1
x = 100
y = 80

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, BLACK)


# Class for apples
class apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab8/snake/resources/apple.png") #loading apple image
        self.image = pygame.transform.scale(self.image, (20, 20)) 
        self.rect = self.image.get_rect() #creating a reactangle around apple
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWAPPLE
        global APPLECOLLECTED
        if not NEWAPPLE: #when there is no apple on the screen, then it means we've collected it
            APPLECOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn
            NEWAPPLE = 1 #this value has to 1 since there is already one apple on the screen


class pear(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab8/snake/resources/pear.png") #loading pear image
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect() #creating a rectangle around pear image
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWPEAR
        global PEARCOLLECTED
        if not NEWPEAR: #when there is no pear on the screen, then it means we've collected it
            PEARCOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn
            NEWPEAR = 1 #this value has to 1 since there is already one apple on the screen


class banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab8/snake/resources/Banana.png") #loading banana image
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect() #creating rectangle around banana image
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWBANANA
        global BANANACOLLECTED
        if not NEWBANANA:
            BANANACOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            NEWBANANA = 1


# Class for snake parts
class snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.draw.rect(screen, GREEN, [x, y, 20, 20]) #creating a rectangle - part of snake
        self.rect = pygame.Rect(x, y, 20, 20) #rectangle around a snake

    def move(self, all_snake):
        for i in all_snake:
            pygame.draw.rect(screen, GREEN, [i[0], i[1], 20, 20]) #all_snake is list which contains all of the rectangles of snake, so this loop will display these rectangles
        self.rect = pygame.Rect(x, y, 20, 20)


# Function for quitting after game over
def quit():
    stop_music()
    time.sleep(1/3) #delay after snake hits wall or itself
    screen.fill((240, 80, 90))
    screen.blit(game_over, (235, 200)) #game over text
    pygame.display.update()
    time.sleep(3) #delay after game over text is shown on the screen
    pygame.quit()
    sys.exit()


# Play music
def play_music():
    pygame.mixer.music.load("pp2/lab8/snake/resources/background.wav")
    pygame.mixer.music.play(-1)


# Stop music
def stop_music():
    pygame.mixer.music.stop()


# Objects from our classes
A1 = apple()
apples = pygame.sprite.Group()
apples.add(A1)
P1 = pear()
pears = pygame.sprite.Group()
pears.add(P1)
B1 = banana()
bananas = pygame.sprite.Group()
bananas.add(B1)
H1 = snake()
heads = pygame.sprite.Group()
heads.add(H1)

while check:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = 0

        # Choosing direction
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if KEYBEFORE != pygame.K_w and KEYBEFORE != pygame.K_s: #if we didn't click w or s before, we will be allowed to move in the up direction
                y -= 20
                KEYBEFORE = pygame.K_w
                DIR = "up" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a: 
            if KEYBEFORE != pygame.K_a and KEYBEFORE != pygame.K_d: #if we didn't click a or d before, we will be allowed to move in the left direction
                x -= 20
                KEYBEFORE = pygame.K_a
                DIR = "left" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if KEYBEFORE != pygame.K_s and KEYBEFORE != pygame.K_w: #if we didn't click w or s before, we will be allowed to move in the down direction
                y += 20
                KEYBEFORE = pygame.K_s
                DIR = "down" #direction's value
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if KEYBEFORE != pygame.K_d and KEYBEFORE != pygame.K_a: #if we didn't click a or d before, we will be allowed to move in the right direction
                x += 20
                KEYBEFORE = pygame.K_d
                DIR = "right" #direction's value

    # Play music at the beginning
    if not MUSICPLAYG:
        play_music()
        MUSICPLAYG = 1

    # Yellow background
    screen.fill((255, 255, 100))

    # Showing score and level
    score = font_small.render("Score: " + str(SCOREFRUITS), True, BLACK)
    screen.blit(score, (800 - 110, 10))
    level = font_small.render("Level: " + str(LEVEL), True, BLACK)
    screen.blit(level, (10, 10))

    # Moving objects
    H1.move(ALLSNAKE)
    A1.move()
    P1.move()
    B1.move()

    # Continue moving in chosen direction
    if DIR == "down":
        y += SPEED
    elif DIR == "up":
        y -= SPEED
    elif DIR == "left":
        x -= SPEED
    elif DIR == "right":
        x += SPEED

    # Game over if hit wall or self
    if y >= 480 or y <= 0 or x >= 780 or x <= 0:
        quit()
    for i in ALLSNAKE[:-1]:
        if x == ALLSNAKE[-1]:
            quit()

    # Append current coordinates of head to coordinates of all snake
    current_head = []
    current_head.append(x) #we are updating x and y values of head
    current_head.append(y)
    ALLSNAKE.append(current_head) #adding current_head list to allsnake list

    # Delete the end of a snake if length didn't grow
    if len(ALLSNAKE) > LENGTH:
        del ALLSNAKE[0]

    # If collected apple: +length, +score
    if pygame.sprite.spritecollideany(H1, apples):
        APPLECOLLECTED = 1
        LENGTH += 1

    if pygame.sprite.spritecollideany(H1, pears):
        PEARCOLLECTED = 1
        LENGTH += 1

    if pygame.sprite.spritecollideany(H1, bananas):
        if NOBANANATIME < 240: #if 
            BANANACOLLECTED = 1
            LENGTH += 1

    # Level up if score += 4. Speed up
    if SCOREFRUITS >= SCORE4 and SCOREFRUITS < SCOREUNDER4: #borders of values when we move to the next level
        FPS += 10
        LEVEL += 1
        SCORE4 += 4
        SCOREUNDER4 += 4

    # Continue displaying apple if not collected
    if not APPLECOLLECTED:
        for entity in apples:
            screen.blit(entity.image, entity.rect)
    
    else:
        if NEWAPPLE == 1:
            SCOREFRUITS += 1
            NEWAPPLE = 0

    if not PEARCOLLECTED:
        for entity in pears:
            screen.blit(entity.image, entity.rect)

    else:
        if NEWPEAR == 1:
            SCOREFRUITS += 4
            NEWPEAR = 0

    if not BANANACOLLECTED:
        if NOBANANATIME < 240: #if value is lower than 240 then image of banana will be displayed
            for entity in bananas:
                screen.blit(entity.image, entity.rect)
                NOBANANATIME += 1 #it has to increase in value since, if we didn't collected banana then it has to disappear after some time
        else:
            if NOBANANATIME < 600: #in the range from 240 until 600 there will be no banana on the screen
                NOBANANATIME += 1
            else:
                NOBANANATIME = 0 #if value is equal or bigger than 600, then we need to display banana again

    
    else:
        NOBANANATIME = 240 #if banana is collected then we need to wait until 600, so it will appear again on the screen
        if NEWBANANA == 1: #if we got one banana then score will increase for 2
            SCOREFRUITS += 2
            NEWBANANA = 0

    pygame.display.update()
    FramePerSec.tick(FPS)