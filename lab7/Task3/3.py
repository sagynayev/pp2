import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Moving Circle ')
clock = pygame.time.Clock()
x = 400
y = 200
rad = 20
mov = 20

while True:
    screen.fill('White')
    pygame.draw.circle(screen, 'Red', (int(x), int(y)), rad)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if y > 0:
                y -= 20
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if y < 400: 
                y += 20
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if x < 800:
                x += 20
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if x > 0:
                x -= 20

    
    pygame.display.update()
    clock.tick(60)