import pygame
from button import *
from os import *
pygame.init()
win_inst = pygame.display.set_mode((425,935))#window
def instructions():
    run = True
    greenButton4 = button((0,255,0),285,790,90,50, 'Back')
    #(button color,x and y coordinates,width and height of the button,text in the button)
    G=pygame.image.load(path.join('img/I.png'))#image on which button is to be present

    def redrawWindow(G):
        win_inst.blit(G, (0, 0))#coordinates of the image in the window
        greenButton4.draw(win_inst)

    while run:
        redrawWindow(G)
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:#for x in the window
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greenButton4.isOver(pos):#when button is pressed
                    #start()
                    run=False

            if event.type ==pygame.MOUSEMOTION:
                #if mouse cursor is at button then button color is blue
                #else button color is green
                if greenButton4.isOver(pos):
                    greenButton4.color = (0,0,255)
                else:
                    greenButton4.color = (0,255,0)
#instructions()
