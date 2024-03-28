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
angle2 = 0 - (minute * 6) - 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(backSurf, (0, 0))
    rightHcopy = pygame.transform.rotate(rightH, angle1)
    leftHcopy = pygame.transform.rotate(leftH, angle2)

    

    screen.blit(rightHcopy, (400 - int(rightHcopy.get_width() / 2), 275 - int(rightHcopy.get_height() / 2)))

    if(angle1 % 360) == 0:
        angle2 -= 6
        screen.blit(leftHcopy, (400 - int(leftHcopy.get_width() / 2), 275 - int(leftHcopy.get_height() / 2)))
    else:
        screen.blit(leftHcopy, (400 - int(leftHcopy.get_width() / 2), 275 - int(leftHcopy.get_height() / 2)))

    angle1 -= 6

    pygame.display.update()
    clock.tick(1)