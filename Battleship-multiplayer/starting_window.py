import pygame
from button import *
pygame.init()
win = pygame.display.set_mode((1000,1000))

run = True
greenButton = button((0,255,0),350,125,350,100, 'Start')          
greenButton1 = button((0,255,0),350,275,350,100, 'Instructions')
greenButton2 = button((0,255,0),350,425,350,100, 'Quit')
img = pygame.image.load("backg.jpg") #loads the image in the background for the starting page

def redrawWindow(img):#adds background and buttons in the starting page
    win.blit(img, (0, 0)) 
    greenButton.draw(win)
    greenButton1.draw(win)
    greenButton2.draw(win)

while run:#run is initialised to True
    redrawWindow(img)#calls the function redrawWindow to 
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()#gets the position of the mouse pointer

        if event.type == pygame.QUIT:
            run = False             
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):#checks if the mouse pointer is on the start button
                print('clicked the button')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton1.isOver(pos):#checks if the mouse pointer is on the instructions button
                print('clicked the button')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton2.isOver(pos):#checks if the mouse pointer is on the quit button
                print('clicked the button')

        if event.type ==pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color = (0,0,255)#changes the color of button if mouse pointer is placed over it
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
