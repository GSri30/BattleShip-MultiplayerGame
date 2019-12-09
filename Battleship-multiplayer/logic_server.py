import socket
import threading
from Grid import *
from pygame import *
from blast import *
from final_win import *
from final_lost import *
import pygame
import sys
from pygame.locals import *
from won import*

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ('127.0.0.1', int(sys.argv[1])) )

s.listen(1)
print("server started")

conn, add = None, None
conn_active = False
environ['SDL_VIDEO_WINDOW_POS'] = '300,50'
grid = grid()
info=False
turn = True
blasted=0
b='is not there'
global_winner=None
global_over=None
global_quit=None
def play_game():
    Tie = None
    winner = None
    game_on=True
    count1 = 0
    temp_count1=0
    count2 = 0
    global turn,info,b,global_winner,global_over,blasted,global_quit
    init()
    x_len=425
    y_len=935
    board = display.set_mode((x_len,y_len))
    pygame.display.set_caption('Battleship: Server')
    icon=pygame.image.load("./img/icon.png")
    pygame.display.set_icon(icon)

    while(game_on):
        for items in event.get():
            if items.type == QUIT:  
                game_on = False
                sdata="0 0 quit"
                conn.send(sdata)
                pygame.quit()
                quit()
            
        if global_quit:
            print("Other player exited..So exiting")
            game_on=False
            pygame.quit()
            quit()
        if(winner!=None):
            game_on=False
        if global_over:
            game_on=False
            
        if won(grid.grid):
            winner=1
            global_winner=True
            game_on=False

        if items.type == MOUSEBUTTONDOWN and conn_active and winner==None:
            
            if mouse.get_pressed()[0] and turn:
                click_position = mouse.get_pos()
                xcell = click_position[0]//85
                ycell = click_position[1]//85

                if(count1<=5) and grid.grid[ycell][xcell] == 0 and ycell<5:
                    grid.get_from_mouse(xcell, ycell, count1,grid.grid)
                    count1 += 1
                    info=False

                if count1>=7 and grid.grid[ycell][xcell]==0 and ycell>=6 and b=='is not there': 
                    grid.set_cell_value(xcell,ycell,'Bo',grid.grid)            
                    sdata=str(xcell)+" "+str(ycell)+" play"
                    print (sdata)
                    conn.send(sdata)
                    turn=False
                    count1+=1

                if count1==6:
                    temp_count1=1
                    turn=False
                    sdata="Null Null play"
                    print(sdata)
                    conn.send(sdata)
                    count1+=1

        board.fill((0, 118, 190)) 
        grid.sketch(board)  
        
        if(count1<=5 and winner==None):
            grid.addText("Place your ships!",80,450,board)
        if(temp_count1==1 and not(info) and not turn and winner==None):
            grid.addText("Please wait for your opponent!",5,450,board)

        if(info and turn and winner==None):
            grid.addText("Your turn!       "+str(blasted),60,450,board)
        if(count1>7 and not turn and winner==None):
            grid.addText("Opponent turn!       "+str(blasted),60,450,board)
        display.flip()
        pygame.display.update()

    if global_winner:
        sdata="0 0 over"
        conn.send(sdata)
        gameover("You Won!",800)

    if global_over:
        gameoverl("You Lost!",800)


def make_thread(tar):
    thread = threading.Thread(target = tar)
    thread.daemon = True
    thread.start()
    

def recieveData():
    make_thread(play_game)
    global turn,info,b,global_over,blasted,global_quit
    count=0
    while True:
        if conn != None:
            data = conn.recv(128).split(' ')
            print("server: "+str(data))
            if data[2] == "play":
                b='is not there'
                turn = True
                info=True            
            if data[2]=="over":
                global_over=True
                turn=True
            if data[2]=="quit":
                global_quit=True
                turn=True
            if data[2]=="bomb":
                blasted+=1
                X,Y=int(data[0]),int(data[1])
                b='is there'
                grid.set_cell_value(X,Y,'C',grid.grid)
                turn = False
            if count>0 and  data[2]!='bomb':
                x, y = int(data[0]), int(data[1])
                if grid.isthere(x,y,grid.grid):
                    grid.set_cell_value(x,y-6,'Bl',grid.grid)
                    sdata=str(x)+" "+str(y)+" bomb"
                    conn.send(sdata)
                else:
                    grid.set_cell_value(x,y-6,'miss',grid.grid) 
            
            
            count+=1


def waitForConnection():
    global conn, add, conn_active
    conn, add = s.accept()
    print('Connection established')
    print(str(conn) + ' ' + str(add))
    conn_active = True
    print(conn_active)
    recieveData()

# waitForConnection()
