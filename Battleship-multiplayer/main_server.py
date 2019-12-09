import pygame
from logic_server import *
from instructions import *
from button import *

pygame.init()
win = pygame.display.set_mode((425,935))#window

run = True
#buttons in the starting window of the game
greenButton = button((0,255,0),100,125,200,100, 'Start')
greenButton1 = button((0,255,0),100,275,200,100, 'Instructions')
greenButton2 = button((0,255,0),100,425,200,100, 'Quit')
img = pygame.image.load("img/backg.jpg")#image of the starting window

def redrawWindow(img):
    win.blit(img, (0, 0))#coordinates of the image in the window
    greenButton.draw(win)
    greenButton1.draw(win)
    greenButton2.draw(win)

while run:
    redrawWindow(img)
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:#for x in window
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):#start button
                #print('clicked the button')
                waitForConnection()#waiting for connection

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton1.isOver(pos):#instructions button
                #print('clicked the button')
                instructions()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton2.isOver(pos):#quit button
                run=False

        if event.type ==pygame.MOUSEMOTION:
            #if mouse cursor is at button then button color is blue
            #else button color is green
            if greenButton.isOver(pos):
                greenButton.color = (0,0,255)
            else:
                greenButton.color = (0,255,0)

            if greenButton1.isOver(pos):
                greenButton1.color = (0,0,255)
            else:
                greenButton1.color = (0,255,0)

            if greenButton2.isOver(pos):
                greenButton2.color = (0,0,255)
            else:
                greenButton2.color = (0,255,0)
