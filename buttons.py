import pygame as pg
W = 300
H = 400
HIGHT_SUM_DISPLAY = 100

WHITE = (255,255,255)
LIGHT_BLACK = (36, 35, 33)
DARK_GREY = (48, 47, 44)
GREY = (89, 86, 83)
ORANGE = (214, 159, 47)
hight_button = (H-HIGHT_SUM_DISPLAY)//5
width_button = W/4

sc = pg.display.set_mode((W,H))
class button_block:
    buttons = []

    def __init__(self,name,color,x,y,is_zero=0) -> None:
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        if is_zero:
            self.coords = (self.x,self.y,width_button*2,hight_button)
        else:    
            self.coords = (self.x,self.y,width_button,hight_button)
        self.buttons.append({'title':self.name,'coords':self.coords})
        
    
    def get_coords(self):
        return self.coords
    
    def get_block(self):
        return pg.draw.rect(sc, self.color, self.coords,)

