import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
is_red = (255,0,0)
x = 30
y = 30

clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        
        pressed = pygame.key.get_pressed()
        if y>=0+50:
            if pressed[pygame.K_UP]: y -= 20
        if y<=700-50:
            if pressed[pygame.K_DOWN]: y += 20
        if x>=0+50:
            if pressed[pygame.K_LEFT]: x -= 20
        if x<=1000-50:
            if pressed[pygame.K_RIGHT]: x += 20
        
        screen.fill((255, 255, 255))
        color = is_red
        pygame.draw.circle(screen, color,(x, y),25)
        
        pygame.display.flip()
        clock.tick(120)