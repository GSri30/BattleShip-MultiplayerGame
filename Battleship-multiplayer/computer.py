import socket
import threading
import random
from Grid import *
from pygame import *
from blast import *
from final_win import *
from final_lost import *
import pygame
import sys
from won import*


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ('127.0.0.1', int(sys.argv[1])) )

environ['SDL_VIDEO_WINDOW_POS'] = '800,50'
grid = grid()

turn = False
info1=False
blasted1=0
global_winner1=None
global_over1=None
b1='is not there'
l=[]


def play_game_comp():
    
    Tie = None
    winner = None
    game_on=True
    count11 = 0
    temp_count11=0
    count22 = 0
    i=0
    
    global turn,info1,b1,global_winner1,global_over1,blasted1

    init()
    x_len=425
    y_len=935
    board = display.set_mode((x_len,y_len))
    pygame.display.set_caption('Battleship: Computer')
    icon=pygame.image.load("./img/icon.png")
    pygame.display.set_icon(icon)

    while(game_on):
        for items in event.get():
            if items.type == QUIT: 
                game_on = False
                pygame.quit()
                quit()
        if(winner!=None):
            game_on=False
        if global_over1:
            game_on=False
        if won(grid.grid1):
            winner=0
            global_winner1=True
            game_on=False
            
        text=pygame.font.Font('freesansbold.ttf',100)
        text_turn=text.render('Place your ships',True,(0,0,0))
        board.blit(text_turn,(160,480))
        
        if turn and winner==None:           
            while(i<6):
                
                xcell=random.randint(0,4)
                ycell=random.randint(0,4)
                
                while((xcell,ycell) in l):
                    xcell=random.randint(0,4)
                    ycell=random.randint(0,4)
                l.append((xcell,ycell))
                
                print(xcell,ycell)
                grid.grid1[xcell][ycell]='S'
                count11 += 1            
                i+=1
            
            if count11>=7 and b1=='is not there' and i>6:
                xcell=random.randint(0,4)
                ycell=random.randint(6,10)
                grid.set_cell_value(xcell,ycell,'Bo',grid.grid1)
                sdata=str(xcell)+" "+str(ycell)+" play"
                print (sdata)
                s.send(sdata)
                turn=False
                count11+=1
            
            if i==6:
                info1=False
                turn=False
                temp_count11+=1
                count11+=1
                sdata="Null Null play"
                print(sdata)
                s.send(sdata)
                i+=1
                
        board.fill((0, 118, 190))  
        grid.sketch(board)  
        
        if(count11<=6 and not info1 and winner==None and not temp_count11):
            grid.addText("Place your ships!",80,450,board)
        if(temp_count11==1 and not info1 and not turn and winner==None):
            grid.addText("Your opponent's turn!    0",80,450,board)
        if(info1 and turn and winner==None):
            grid.addText("Your turn!      "+str(blasted1),60,450,board)
        if(count11>7 and not turn and winner==None):
            grid.addText("Opponent turn!      "+str(blasted1),60,450,board)
        display.flip()
        pygame.display.update()

    if global_winner1:
        sdata="0 0 over"
        s.send(sdata)
        gameover("You Lost!",300)
        
    if global_over1:
        gameoverl("You Won!",300)


def make_thread_comp(target):
    thread = threading.Thread(target = target)
    thread.daemon = True
    thread.start()


def recieveDataComp():
    make_thread_comp(play_game_comp)
    global turn,info1,b1,global_over1,blasted1
    temp=0
    while True:
            data = s.recv(128).split(' ')
            print("client: "+str(data))
            if data[2] == "play":
                b1='is not there'
                turn = True
                info1=True
            if data[2]=="over":
                global_over1=True
                turn=True
            if data[2]=="bomb":
                X1,Y1=int(data[0]),int(data[1])
                blasted1+=1
                b1='is there'
                grid.set_cell_value(X1,Y1,'C',grid.grid1)
                turn = False

            if data[0]=="Null" and data[1]=="Null":
                info1=False

            if temp>0 and data[2]!='bomb':
                x, y = int(data[0]), int(data[1])
                if grid.isthere(x,y,grid.grid1):
                    grid.set_cell_value(x,y-6,'Bl',grid.grid1)
                    sdata=str(x)+" "+str(y)+" bomb"
                    s.send(sdata)   
                else:
                    grid.set_cell_value(x,y-6,'miss',grid.grid1)                    
            temp+=1

#recieveDataComp()

