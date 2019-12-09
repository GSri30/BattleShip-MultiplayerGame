from Grid import *
from pygame import *
#from array import *
from blast import *

from win import *
from lost import *
import pygame
array = [[0, 0, 0, 0, 0], [0, 0, 'S', 0, 0], [0, 'S', 'S', 0, 0], [0, 0, 'S', 'S', 0], [0, 0, 'S', 0, 0],[1,1,1,1,1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
init()
grid = grid()
#grid1 = grid()
count1 = 0
count2 = 0
count11=0
count22=0
game_on = True
Tie = None
winner = None
player=0
x_len=425
y_len=935
board = display.set_mode((x_len,y_len))
pygame.display.set_caption('Battleship')
icon=pygame.image.load("./img/icon.png")
pygame.display.set_icon(icon)
blasted1 = 0
blasted11=0
while(game_on):
    for items in event.get():
        if items.type == QUIT:  # for x button in window
            game_on = False
        #if count1+count2 == 31:
         #   game_on = False
        if items.type == MOUSEBUTTONDOWN:
            # print(mouse.get_pressed())
            if mouse.get_pressed()[0]:
                click_position = mouse.get_pos()
                xcell = click_position[0]//85
                ycell = click_position[1]//85
                # to make sure that on clicking on the already occupied block does not change the player .and on clicking next on the valid(empty)
                if(count1<=5):
                    if player==0:
                        if (count1 <= 5) and grid.grid[ycell][xcell] == 0:
                            if xcell<5 and ycell<5:
                                grid.get_mouse(xcell, ycell, count1,grid.grid)
                                count1 += 1
                else:
                    player=1
                    if count11<=5:
                        if player==1:
                            if (count11 <= 5) and grid.grid1[ycell][xcell] == 0:
                                if xcell<5 and ycell<5:
                                    grid.get_mouse(xcell, ycell, count11,grid.grid1)
                                    count11 += 1
                if count1==6 and count11==6:
                    player=0
                    if(player==0 and count1==6):
                        if count1 == 6 and grid.grid[ycell][xcell] == 0:
                            if xcell<5 and ycell>5:
                                grid.get_mouse(xcell,ycell,count2,grid.grid)
                                count2 += 1
                        player=1
                        blasted1=blast(grid.grid1,grid.grid,blasted1)
                    if player==1 and count11==6:
                        if count11 == 6 and grid.grid1[ycell][xcell] == 0:
                            if xcell<5 and ycell>5:
                                grid.get_mouse(xcell,ycell,count22,grid.grid1)
                                count22 += 1
                        player=0
                        blasted11=blast(grid.grid,grid.grid1,blasted11)
    board.fill((0, 118, 190))  # color
    grid.sketch(board)  # draw grid
    display.flip()

if winner==0:
    gameover("A is winner")
    gameoverl("B is loser")
if winner==1:
    gameover("B is winner")
    gameoverl("A is loser")

print(grid.grid)
print(grid.grid1)
print(winner)

