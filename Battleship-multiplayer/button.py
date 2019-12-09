import pygame
class button():
    def __init__(self,color,x,y,width,height,text=''):
       #(color of the button,x and y coordinates,width and height of the button,text in the button)
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text

    def draw(self,win,outline=None):#(giving a window to draw button on to,outline of the button)
        #call this method to draw the button the screen
        if outline:#if we have an outline color 
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            #outline is 2 pixels thick
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':#if text is there
            font = pygame.font.SysFont('comicsans', 45)#font and size of the text
            text = font.render(self.text, 1, (0,0,0))#color of the text
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))#placing text in middle of the button

    def isOver(self, pos):
        #pos is the mouse position or a tuple of (x,y) coordinates 
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
