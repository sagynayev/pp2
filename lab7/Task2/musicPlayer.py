import pygame

def play_music():
    global currentSong, paused
    if not paused:
        pygame.mixer.music.load(currentSong)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global currentSong, musicIndex, paused
    
    musicIndex += 1
    if musicIndex > len(musicCol) - 1:
        musicIndex = 0
        currentSong = musicCol[musicIndex]
        play_music()
    else:
        currentSong = musicCol[musicIndex]
        play_music()
  

def prev_music():
    global currentSong, musicIndex, paused
    musicIndex -= 1
    if musicIndex < 0:
        musicIndex = 0
        currentSong = musicCol[musicIndex]
        play_music()
    else:
        currentSong = musicCol[musicIndex]
        play_music()
   

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Music player")
clock = pygame.time.Clock()


playSurf = pygame.image.load('pp2/lab7/Task2/img/play-button.png').convert_alpha()
playSurf = pygame.transform.rotozoom(playSurf, 0, 0.1)
playRect = playSurf.get_rect(midbottom = (350, 350))

pauseSurf = pygame.image.load('pp2/lab7/Task2/img/pause.png').convert_alpha()
pauseSurf = pygame.transform.rotozoom(pauseSurf, 0, 0.1)
pauseRect = pauseSurf.get_rect(midbottom = (420, 350))

prevSurf = pygame.image.load('pp2/lab7/Task2/img/previous.png').convert_alpha()
prevSurf = pygame.transform.rotozoom(prevSurf, 0, 0.1)
prevRect = prevSurf.get_rect(midbottom = (280, 350))

nextSurf = pygame.image.load('pp2/lab7/Task2/img/next-button.png').convert_alpha()
nextSurf = pygame.transform.rotozoom(nextSurf, 0, 0.1)
nextRect = nextSurf.get_rect(midbottom = (500, 350))

music1 = 'pp2/lab7/Task2/mp3/first.mp3'
music2 = 'pp2/lab7/Task2/mp3/second.mp3'
music3 = 'pp2/lab7/Task2/mp3/third.mp3'

musicCol = [music1, music2, music3]
musicIndex = 0
currentSong = musicCol[musicIndex]
paused = False

image = pygame.image.load('pp2/lab7/Task2/img/kairat.jpeg')
image = pygame.transform.scale(image, (500, 280))
imageRect = image.get_rect(center = (400, 140))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and playRect.collidepoint(event.pos):
            play_music()
        
        if event.type == pygame.MOUSEBUTTONDOWN and pauseRect.collidepoint(event.pos):
            pause_music()
        
        if event.type == pygame.MOUSEBUTTONDOWN and nextRect.collidepoint(event.pos):
            next_music()

        if event.type == pygame.MOUSEBUTTONDOWN and prevRect.collidepoint(event.pos):
            prev_music()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                prev_music()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                play_music()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                pause_music()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                next_music()

    screen.fill('#191919')
    screen.blit(image, imageRect)
    pygame.draw.line(screen, 'Black', (0, 280), (800, 280), width=3)
    screen.blit(playSurf, playRect)
    screen.blit(pauseSurf, pauseRect)
    screen.blit(prevSurf, prevRect)
    screen.blit(nextSurf, nextRect)
    
    

    clock.tick(30)
    pygame.display.update()