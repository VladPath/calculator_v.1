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

    def __init__(self,name,color,x,y,symbol:str='1',is_zero=0) -> None:
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.symbol = symbol
        
        if is_zero:
            self.coords = (self.x,self.y,width_button*2,hight_button)
        else:    
            self.coords = (self.x,self.y,width_button,hight_button)
        self.buttons.append({'title':self.name,'coords':self.coords})
        
    def create_symbol(self):
        font = pg.font.SysFont(None, 45)
        img = font.render(self.symbol, True, WHITE)
        sc.blit(img, (self.coords[0]+self.coords[2]//2-10,self.coords[1]+self.coords[3]//2-15))
        
    def get_coords(self):
        return self.coords
    
    def get_block(self):
        return pg.draw.rect(sc, self.color, self.coords,)


# # ac button
# ac = button_block(DARK_GREY, buttons['AC']['coords'][0], buttons['AC']['coords'][1])
# ac.get_block()
# # plus_minus
# plus_minus = button_block(DARK_GREY, width_button, HIGHT_SUM_DISPLAY)
# plus_minus.get_block()
# # percent
# percent = button_block(DARK_GREY, width_button*2, HIGHT_SUM_DISPLAY)
# percent.get_block()
# devide
# devide = button_block(ORANGE, width_button*3, HIGHT_SUM_DISPLAY)
# devide.get_block()
# multyply
# multyply = button_block(ORANGE, width_button*3, HIGHT_SUM_DISPLAY+hight_button)
# multyply.get_block()
# # minus
# minus = button_block(ORANGE, width_button*3, HIGHT_SUM_DISPLAY+hight_button*2)
# minus.get_block()
# plus
# plus = button_block(ORANGE, width_button*3, HIGHT_SUM_DISPLAY+hight_button*3)
# plus.get_block()
# result
# result = button_block(ORANGE, width_button*3, HIGHT_SUM_DISPLAY+hight_button*4)
# result.get_block()
# # pont
# point = button_block(GREY, width_button*2, HIGHT_SUM_DISPLAY+hight_button*4)
# point.get_block()
# zero
# zero = button_block(GREY, 0, HIGHT_SUM_DISPLAY+hight_button*4,1)
# zero.get_block()
# one
# one = button_block(GREY, 0, HIGHT_SUM_DISPLAY+hight_button*3)
# one.get_block()
# two
# two = button_block(GREY, width_button, HIGHT_SUM_DISPLAY+hight_button*3)
# two.get_block()
# three
# three = button_block(GREY, width_button*2, HIGHT_SUM_DISPLAY+hight_button*3)
# three.get_block()
# four
# four = button_block(GREY, 0, HIGHT_SUM_DISPLAY+hight_button*2)
# four.get_block()
# five
# five = button_block(GREY, width_button, HIGHT_SUM_DISPLAY+hight_button*2)
# five.get_block()
# six
# six = button_block(GREY, width_button*2, HIGHT_SUM_DISPLAY+hight_button*2)
# six.get_block()
# # seven
# seven = button_block(GREY, 0, HIGHT_SUM_DISPLAY+hight_button)
# seven.get_block()
# eitght
# eitght = button_block(GREY, width_button, HIGHT_SUM_DISPLAY+hight_button)
# eitght.get_block()
# # nine
# nine = button_block(GREY, width_button*2, HIGHT_SUM_DISPLAY+hight_button)
# nine.get_block()
