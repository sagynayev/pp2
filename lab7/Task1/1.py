import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Micky Clock")
clock = pygame.time.Clock() 

backSurf = pygame.image.load('pp2/lab7/Task1/img/clock.jpg').convert_alpha()
backSurf = pygame.transform.scale(backSurf, (800, 550))

leftH = pygame.image.load('pp2/lab7/Task1/img/left.png').convert_alpha()
leftHrect = leftH.get_rect(center = (380, 275))
rightH = pygame.image.load('pp2/lab7/Task1/img/right.png').convert_alpha()
rightHrect = rightH.get_rect(center = (420, 275))

currentTime = datetime.datetime.now()
second = currentTime.second
minute = currentTime.minute

angle1 = 0 - (second * 6)
angle2 = 0 - (minute * 6) - 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(backSurf, (0, 0))
    rightHcopy = pygame.transform.rotate(rightH, angle1)
    leftHcopy = pygame.transform.rotate(leftH, angle2)

    leftHcopyRect = leftHcopy.get_rect()
    leftHcopyRect.center = leftHrect.center

    rightHcopyRect = rightHcopy.get_rect()
    rightHcopyRect.center = rightHrect.center

    screen.blit(rightHcopy, rightHcopyRect)
    if((angle1-6) % 360) == 0:
        angle2 -= 6
        screen.blit(leftHcopy, leftHcopyRect)
    else:
        screen.blit(leftHcopy, leftHcopyRect)
        
    angle1 -= 6

    pygame.display.update()
    clock.tick(1)