import pygame 
pygame.init()
sc=pygame.display.set_mode((300,350))
white=(255,255,255)
clock= pygame.time.Clock()


_currently_playing_song=None
stop=False


_song = ["music/VALORANT - Die For You.mp3","music/Imagine Dragons - thunder.mp3","music/Imagine Dragons - Bones.mp3"]
i=0
pygame.mixer.music.load(_song[i])
pygame.mixer.music.play()
size=len(_song)
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
    pressed = pygame.key.get_pressed()  
    
    if pressed[pygame.K_SPACE]:
        stop = not stop
        if stop == True:
            pygame.mixer.music.pause()
        if stop == False:
            pygame.mixer.music.unpause()
    if pressed[pygame.K_LEFT]:
        k=i
        i-=1
        if i<0:i=0
        if i==k: continue
        pygame.mixer.music.load(_song[i])
        pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]:
        k=i
        i+=1
        if i>(size-1):i=(size-1)
        if i==k:continue
        pygame.mixer.music.load(_song[i])
        pygame.mixer.music.play()
    #   text = pygame.font.SysFont('Times New Roman', 50).render(_song[i], False, white)
    clock.tick(15)
