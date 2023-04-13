from datetime import datetime 
import pygame 
import os
pygame.init() 
screen=pygame.display.set_mode((400,400)) 
a = datetime.now() 
image = pygame.image.load("C:/Users/Kasym_Nazar/Downloads/photo_5314738359551248550_x.jpg") 
image = pygame.transform.scale(image, (400, 400)) 
handl = pygame.image.load("C:/Users/Kasym_Nazar/Downloads/photo_5314738359551248557_m.jpg")  
handl.set_colorkey((255,255,255))
handl = pygame.transform.scale(handl, (200, 200)) 
handr =pygame.image.load("C:/Users/Kasym_Nazar/Downloads/photo_5314738359551248556_m.jpg")
handr.set_colorkey((255,255,255))
handr = pygame.transform.scale(handr, (200, 200)) 
#Left hand
def left_hand(surf, image, topleft, angle):  
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect) 
#Right hand
def right_hand(surf, image, topleft, angle):   
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect) 
#Angles of MC's hands
anglel=(51-a.second)*6 
angleh=308-(a.minute*6) 
#Coordinates
x=100 
y=80 
running = True 
n=a.second 
while running: 
    #Another variable for time 
    b=datetime.now() 
    screen.fill((255,255,255)) 
    #MC
    screen.blit(image,(0,0))
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            pygame.quit() 
            quit() 
    #Right and left hands 
    left_hand(screen, handl, [x,y], anglel) 
    right_hand(screen,handr,[x,y], angleh) 
     
    pygame.display.update()   
    #    
    if b.second>=0 and b.second !=n: 
        n=b.second 
        anglel-=6 
    if b.second==0: 
        angleh-=0.1 
    print(b.second)