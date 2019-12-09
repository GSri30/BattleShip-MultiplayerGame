from pygame import *  
from os import *
import pygame
init()
G=pygame.image.load(path.join('img','E.png'))
def gameover(msg,x):
    environ['SDL_VIDEO_WINDOW_POS'] = str(x)+',50'
    pygame.init()
    board1 = pygame.display.set_mode((425, 900))  # SIZE OF WINDOW
    pygame.display.set_caption("GAME OVER !!")#caption to be displayed on top of the window
    font =pygame.font.SysFont('Sans',55)#font style
    font.set_bold(True)
    text=font.render(msg,True,(0,255,0))#color of the text
    notexit = True
    while(notexit):
        for items in pygame.event.get():
            if items.type == pygame.QUIT:  # for x button in window
                notexit = False
                pygame.quit()
                quit()                
        board1.fill((0, 0, 0))  # color
        board1.blit(G,(0,0))#coordinates of the image in the window
        board1.blit(text,[80,700])#text coordinates
        pygame.display.flip()

