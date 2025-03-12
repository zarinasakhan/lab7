import pygame
pygame.init()
screen=pygame.display.set_mode((500,590))
audios=['luther.ogg','telekinesis.ogg','LA.ogg']
current=0
clock = pygame.time.Clock()
running=True
def play():
    pygame.mixer.music.load(audios[current])
    pygame.mixer.music.play()
    print(f"playing: {audios[current]}")

def stop():
    pygame.mixer.music.stop()
    print("track is stopped")

def next():
    global current
    current=(current+1)%len(audios)
    play()
def back():
    global current
    current=(current-1)%len(audios)
    play()
play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                play()
            elif event.key==pygame.K_n:
                next()
            elif event.key==pygame.K_b:
                back()
            elif event.key==pygame.K_s:
                stop()

    screen.fill(("pink"))
    dog=pygame.image.load("music.jpg")
    image_rect = dog.get_rect(center=(250,245))
    

    screen.blit(dog, image_rect )
    pygame.display.flip()
    clock.tick(60)