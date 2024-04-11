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
SCOREAPPLE = 0
APPLEDIF = 0
LEVEL = 1
LENGTH = 1
ALLSNAKE = []
DIR = 0
KEYBEFORE = 0
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
        self.image = pygame.image.load("pp2/lab8/snake/resources/apple.png") #loading image of apple
        self.image = pygame.transform.scale(self.image, (20, 20)) #changing resolution of apple's image
        self.rect = self.image.get_rect() #creating rectangle around apple's image
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn

    def move(self):
        global NEWAPPLE
        global APPLECOLLECTED
        if not NEWAPPLE: #checking if there is no apple on the screen
            APPLECOLLECTED = 0 #checking for apple collected or not
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25)) #random spawn
            NEWAPPLE = 1 #apple will disappear from the screen


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
    time.sleep(1/3) #delay after snake hits wall or itself
    screen.fill((240, 80, 90))
    screen.blit(game_over, (235, 200)) #gamve over text
    pygame.display.update()
    time.sleep(3) #delay after game over text is shown on the screen
    pygame.quit()
    sys.exit()


# Creating objects of sprites
A1 = apple()
apples = pygame.sprite.Group() #sprite group for apple
apples.add(A1)
H1 = snake()
heads = pygame.sprite.Group() #sprite group for head of the snake
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


    # Yellow background
    screen.fill((255, 255, 100))

    # Showing score and level
    score = font_small.render("Score: " + str(SCOREAPPLE), True, BLACK)
    screen.blit(score, (800 - 110, 10))
    level = font_small.render("Level: " + str(LEVEL), True, BLACK)
    screen.blit(level, (10, 10))

    # Moving objects
    H1.move(ALLSNAKE)
    A1.move()

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

    # Level up if score += 4. Speed up
    if SCOREAPPLE % 4 == 0 and SCOREAPPLE - APPLEDIF != 0:
        FPS += 10
        LEVEL += 1
        APPLEDIF += 4

    # Continue displaying apple if not collected
    if not APPLECOLLECTED:
        for entity in apples:
            screen.blit(entity.image, entity.rect)
    # Plus score if collected + making new apple
    else:
        if NEWAPPLE == 1:
            SCOREAPPLE += 1
            NEWAPPLE = 0
    FramePerSec.tick(FPS)
    pygame.display.update()
    