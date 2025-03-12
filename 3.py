import pygame
pygame.init()
WIDTH=400
HEIGHT=400
circle_x=WIDTH//2
circle_y=HEIGHT//2
circle_radius=25
screen=pygame.display.set_mode((WIDTH,HEIGHT))
running=True
movement_speed=20
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and circle_y-circle_radius>0:
        circle_y-=movement_speed
    if pressed_keys[pygame.K_DOWN] and circle_y+circle_radius<HEIGHT:
        circle_y+=movement_speed
    if pressed_keys[pygame.K_RIGHT] and circle_x+circle_radius<WIDTH:
        circle_x+=movement_speed
    if pressed_keys[pygame.K_LEFT] and circle_x-circle_radius>0:
        circle_x-=movement_speed
        

    screen.fill((255,255,255))
    pygame.draw.circle(screen,"red", (circle_x,circle_y), circle_radius )
    pygame.display.flip()
    clock.tick(60)