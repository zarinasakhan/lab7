import pygame
import time
pygame.init()
WIDTH=800
HEIGHT=800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
clock_img=pygame.image.load("clock.png")
sec_img=pygame.image.load("sec_hand.png")
min_img=pygame.image.load("min_hand.png")
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current=time.localtime()
    minutes=current.tm_min
    seconds=current.tm_sec
    min_angle=-6*minutes
    sec_angle=-6*seconds
    rotated_sec=pygame.transform.rotate(sec_img, sec_angle)
    rotated_min=pygame.transform.rotate(min_img, min_angle)
    sec_rect=rotated_sec.get_rect(center=(WIDTH//2, HEIGHT//2))
    min_rect=rotated_min.get_rect(center=(WIDTH//2, HEIGHT//2))
    clock_rect=clock_img.get_rect(center=(WIDTH//2, HEIGHT//2))

    screen.fill((255, 255, 255))
    screen.blit(clock_img,clock_rect)
    screen.blit(rotated_sec,sec_rect)
    screen.blit(rotated_min,min_rect)
    pygame.display.flip()
    clock.tick(60)


