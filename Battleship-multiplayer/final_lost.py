from pygame import *  
from os import *
import pygame
init()
G=pygame.image.load(path.join('img','e.png'))#image path
def gameoverl(msg,x):
    environ['SDL_VIDEO_WINDOW_POS'] = str(x)+',50'
    pygame.init()
    board2 = pygame.display.set_mode((425, 900))  # SIZE OF WINDOW
    pygame.display.set_caption("GAME OVER !!")#caption of the window
    font =pygame.font.SysFont("Sans",55)#font of the text to be displayed on screen
    font.set_bold(True)
    text=font.render(msg,True,(255,0,0))#(text,true,color of the text)
    notexit = True
    while(notexit):
        for items in pygame.event.get():
            if items.type == pygame.QUIT:  # for x button in window
                notexit = False  
                pygame.quit()
                quit()              
        board2.fill((255, 255, 0))  # color of the board
        board2.blit(G,(0,0))#coordinates of picture to be displayed 
        board2.blit(text,[80,700])#(text,coordinates)
        pygame.display.flip()
