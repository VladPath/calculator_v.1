import pygame as pg

W = 300
H = 400

WHITE = (255,255,255)
LIGHT_BLACK = (36, 35, 33)
DARK_GREY = (48, 47, 44)
GREY = (89, 86, 83)
ORANGE = (214, 159, 47)

sc = pg.display.set_mode((W,H))
hight_button = (H-100)//5
width_button = W/4

print(hight_button)

pg.display.set_caption('Calculator v1.0')
icon = pg.image.load('img/calc_icon.jpg').convert()
icon.set_colorkey(WHITE)
pg.display.set_icon(icon)

# background for display
pg.draw.rect(sc, LIGHT_BLACK, (0,0,W,100),0,)
# background for digits
pg.draw.rect(sc, GREY, (0,100,W,H),0,)
# background for first upper line
pg.draw.rect(sc, DARK_GREY, (0,100,W,hight_button),0,)
# background for left line
pg.draw.rect(sc, ORANGE, (W-width_button,100,W,H),0,)


# class for buttons
class buttons_math:
    size_h = (H-75)//5
    size_w = W//4
    def __init__(self, color:set, math:str,icon_src:str) -> None:
        self.color = color
        self.math = math
        self.icon = pg.image.load(icon_src).convert()

class buttons_num:
    size_h = (H-75)//5
    size_w = W//4
    def __init__(self, color:set, digit:str) -> None:
        self.color = color
        self.digit = digit
        if int(self.digit) == 0:
            self.size_w = W//2
    

pg.display.update()


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            