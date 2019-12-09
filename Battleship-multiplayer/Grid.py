from pygame import *
import pygame
from os import *
y = 85#length and breadth of each box in the grid
X=image.load(path.join('img','w.png'))#assigns image to variable
Y=image.load(path.join('img','b.png'))
Z=image.load(path.join('img','h.png'))
M=image.load(path.join('img','m.png'))
C=image.load(path.join('img','C.png'))
class grid :
    def __init__(self):
        self.lines =[[[0,y],[5*y,y]], # horizontal lines
                     [[0,y*2],[5*y,y*2]],
                     [[0,y*3],[5*y,3*y]],
                     [[0,y*4],[5*y,4*y]],
                     [[0,y*5],[5*y,y*5]], 
                     [[0,y*6],[5*y,6*y]],
                     [[0,y*7],[5*y,7*y]],
                     [[0,y*8],[5*y,8*y]],
                     [[0,y*9],[5*y,9*y]],
		             [[0,10*y],[5*y,10*y]],
                     [[0,11*y],[5*y,11*y]],
                     [[y,0],[y,11*y]],     #vertical lines
                     [[y*2,0],[y*2,11*y]],
                     [[y*3,0],[y*3,11*y]],
                     [[y*4,0],[y*4,11*y]],


                      #end1coo,end2coo
                    ]
        self.grid =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0], #assigning empty boxes in the grid
        [1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.grid1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0], 
        [1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    def sketch(self,board):
        for line in self.lines:
                draw.line( board,(255,255,255),line[0],line[1],5)
        draw.line(board,(250,250,250),[0,85*5+42],[85*5,85*5+42],85)
            #          screen,(color),end1,end2,thickness
        for y in range(11):#display
            for x in range(5):
                if self.grid[y][x]=='S' or self.grid1[y][x]=='S':
                    board.blit(X,(x*85 ,y*85)) # DISPLAY ship ON SCREEN
                if self.grid[y][x]=='Bo' or self.grid1[y][x]=='Bo':
                    board.blit(Y,(x*85+10 ,y*85))
                if self.grid[y][x]=='Bl' or self.grid1[y][x]=='Bl':
                    board.blit(Z,(x*85+10 ,y*85+20))
                if self.grid[y][x]=='miss' or self.grid1[y][x]=='miss':
                    board.blit(M,(x*85+10,y*85+10))
                if self.grid[y][x]=='C' or self.grid1[y][x]=='C':
                    board.blit(C,(x*85+10,y*85+10))


    def get_from_mouse(self,x,y,count,grid):
        if grid[y][x]==0:
          if y <= 5:
              grid[y][x]='S'
          elif y >= 6:
              grid[y][x]='Bo'

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value,lst):
        lst[y][x] = value

    def isthere(self,x,y,lst):
        if lst[y-6][x]=='S':
            return True
        else:
            return False

    def addText(self,txt,x,y,board):
        text=pygame.font.Font('freesansbold.ttf',25)
        text_turn=text.render(txt,True,(0,0,0))
        board.blit(text_turn,(x,y))
