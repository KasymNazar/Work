import pygame
from random import randrange
pygame.init()

Height=800
size=30
x,y=randrange(size,Height-size,size),randrange(size,Height-size,size)
x1,y1=randrange(size,Height-size,size),randrange(size,Height-size,size)
length=1
snake=[(x,y)]
score=0
dx,dy=0,0
l=0
fps=5
dire = {'W': True, 'S': True, 'A': True, 'D': True }
Black=(0,0,0)
Green=(0,255,0)
Red=(255,0,0)
clock= pygame.time.Clock()
screen=pygame.display.set_mode((Height,Height))
level=1
sco=1
time=0
timer=20
sc=12
f_score = pygame.font.SysFont('Arial', 26)
f_level = pygame.font.SysFont('Arial', 26)
f_end = pygame.font.SysFont('Arial', 66)
while True:
    time+=1
    screen.fill(Black)
    [pygame.draw.rect(screen,Green,pygame.Rect(i,j,size-1,size-1)) for i,j in snake]
    pygame.draw.rect(screen,Red,pygame.Rect(x1,y1,size,size))
    render_score = f_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    render_level = f_level.render(f'LEVEL:{level}', 1,pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    screen.blit(render_level,(650,5))
    
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_w] and dire['W']:
        dire = {'W': False, 'S': True, 'A': True, 'D': True }
        dx,dy=0,-1
    if pressed[pygame.K_a] and dire['A']:
        dire = {'W': True, 'S': True, 'A': False, 'D': True }
        dx,dy=-1,0
    if pressed[pygame.K_s] and dire['S']:
        dire = {'W': True, 'S': False, 'A': True, 'D': True }
        dx,dy=0,1
    if pressed[pygame.K_d] and dire['D']:
        dire = {'W': True, 'S': True, 'A': True, 'D': False }
        dx,dy=1,0
        
    if timer==0:
        timer=(20/level)+3
        x1,y1=randrange(size,Height-size,size),randrange(size,Height-size,size)
    if time%sc==0:
        timer-=0.2
        time=0
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length:]
    if x < 0 or x > Height - size or y < 0 or y > Height - size or len(snake) != len(set(snake)):
        render_end = f_end.render('GAME OVER', 1, pygame.Color('orange'))
        screen.blit(render_end, (Height // 2 - 200, Height // 3))
        pygame.display.flip()
        pygame.quit()
        exit()
    
    if snake[-1]==(x1,y1): 
        score+=sco
        if level!=1:
            sco=randrange(1,level)
        x1,y1=randrange(size,Height-size,size),randrange(size,Height-size,size)
        length+=1
    if score==(level*level)+1:
        score=0
        sc-=1
        level+=1
        length=1
        snake=[(x,y)]
        x,y=randrange(size,Height-size,size),randrange(size,Height-size,size)
        x1,y1=randrange(size,Height-size,size),randrange(size,Height-size,size)
        dx,dy=0,0
        dire = {'W': True, 'S': True, 'A': True, 'D': True }
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(60)
    pygame.display.flip()
