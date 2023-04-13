import pygame

# Initialize Pygame
pygame.init()

# Set game window dimensions
w_width = 800
w_height = 600
screen=pygame.display.set_mode((w_width,w_height))
# Set game colors
color = (0,0,0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
coor=(0,0)
fps=60
clock=pygame.time.Clock()
while True:
    key=pygame.key.get_pressed()
    if key[pygame.K_1]:
        color=white
    if key[pygame.K_2]:
        color=black
    if key[pygame.K_3]:
        color=red
    if key[pygame.K_4]:
        color=green
    if key[pygame.K_5]:
        color=blue
    coor=pygame.mouse.get_pos()
    if key[pygame.K_q]:
        pygame.draw.rect(screen, color,pygame.Rect(coor[0], coor[1], 50, 100))
    if key[pygame.K_w]:
        pygame.draw.circle(screen, color, coor, 25)
    if key[pygame.K_e]:
        pygame.draw.rect(screen,color,pygame.Rect(coor[0],coor[1],50,50))
    if key[pygame.K_r]:
        pygame.draw.polygon(screen, color, ((coor[0],coor[1]),(coor[0],coor[1]+50),(coor[0]-50,coor[1]+50)))
    if key[pygame.K_t]:
        pygame.draw.polygon(screen,color,((coor[0],coor[1]),(coor[0]+50,coor[1]+100),(coor[0]-50,coor[1]+100)))
    if key[pygame.K_y]:
        pygame.draw.polygon(screen,color,((coor[0],coor[1]),(coor[0]+50,coor[1]+100),(coor[0]-50,coor[1]+100)))
        pygame.draw.polygon(screen,color,((coor[0],coor[1]+200),(coor[0]+50,coor[1]+100),(coor[0]-50,coor[1]+100)))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(fps)