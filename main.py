from fcntl import flock
import pygame as pg
from buttons import button_block

clock = pg.time.Clock()

pg.init()

FPS = 60
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

print(hight_button)

pg.display.set_caption('Calculator v1.0')
icon = pg.image.load('img/calc_icon.jpg').convert()
icon.set_colorkey(WHITE)
pg.display.set_icon(icon)

font = pg.font.SysFont(None, 45)
# img = font.render('+', True, WHITE)
# pos = img.get_rect(center=(,10))
# sc.blit(img, (HIGHT_SUM_DISPLAY,HIGHT_SUM_DISPLAY))

buttons = [
    {'title':'AC','coords':(0, HIGHT_SUM_DISPLAY), 'color':DARK_GREY,'symbol':'AC'},
    {'title':'plus_minus','coords':(width_button, HIGHT_SUM_DISPLAY),'color':DARK_GREY,'symbol':'+/-'},
    {'title':'percent','coords':(width_button*2, HIGHT_SUM_DISPLAY),'color':DARK_GREY,'symbol':'%'},
    {'title':'devide','coords':(width_button*3, HIGHT_SUM_DISPLAY),'color':ORANGE,'symbol':'÷'},
    {'title':'multyply','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button),'color':ORANGE,'symbol':'x'},
    {'title':'minus','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button*2),'color':ORANGE,'symbol':'-'},
    {'title':'plus','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button*3),'color':ORANGE,'symbol':'+'},
    {'title':'result','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button*4),'color':ORANGE,'symbol':'='},
    {'title':'point','coords':(width_button*2, HIGHT_SUM_DISPLAY+hight_button*4),'color':GREY,'symbol':','},
    {'title':'zero','coords':(0, HIGHT_SUM_DISPLAY+hight_button*4),'color':GREY, 'symbol':'0','is_zero':1},
    {'title':'one','coords':(0, HIGHT_SUM_DISPLAY+hight_button*3),'color':GREY,'symbol':'1'},
    {'title':'two','coords':(width_button, HIGHT_SUM_DISPLAY+hight_button*3),'color':GREY,'symbol':'2'},
    {'title':'three','coords':( width_button*2, HIGHT_SUM_DISPLAY+hight_button*3),'color':GREY,'symbol':'3'},
    {'title':'four','coords':( 0, HIGHT_SUM_DISPLAY+hight_button*2),'color':GREY,'symbol':'4'},
    {'title':'five','coords':( width_button, HIGHT_SUM_DISPLAY+hight_button*2),'color':GREY,'symbol':'5'},
    {'title':'six','coords':( width_button*2, HIGHT_SUM_DISPLAY+hight_button*2),'color':GREY,'symbol':'6'},
    {'title':'seven','coords':( 0, HIGHT_SUM_DISPLAY+hight_button),'color':GREY,'symbol':'7'},
    {'title':'eight','coords':(width_button, HIGHT_SUM_DISPLAY+hight_button),'color':GREY,'symbol':'8'},
    {'title':'nine','coords':( width_button*2, HIGHT_SUM_DISPLAY+hight_button),'color':GREY,'symbol':'9'},
]


for but in buttons:
    if but.get('is_zero'):
        x = button_block(but['title'],but['color'],but['coords'][0],but['coords'][1],but['symbol'],is_zero=1)
    else:
        x = button_block(but['title'],but['color'],but['coords'][0],but['coords'][1],but['symbol'])
    x.get_block()
    x.create_symbol()
     
    

# horisontal_lines
x = width_button
for i in range(3):
    if i == 0:
        pg.draw.aaline(sc,LIGHT_BLACK,(x,HIGHT_SUM_DISPLAY),(x,HIGHT_SUM_DISPLAY+hight_button*4))
    else:
        pg.draw.aaline(sc,LIGHT_BLACK,(x,HIGHT_SUM_DISPLAY),(x,H))
    x += width_button

# vertical lines
y = hight_button+HIGHT_SUM_DISPLAY
for i in range(4):
    pg.draw.aaline(sc,LIGHT_BLACK,(0,y),(W,y))
    y += hight_button

# signs for results
left_sign = '20'
right_sigh = '10'
# font for sum 
font = pg.font.SysFont(None, 45)
one_symb = 18
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    sum = int(left_sign) + int(right_sigh)
    rect1 = pg.Rect((0,HIGHT_SUM_DISPLAY-40,(W-30)-(one_symb)*len(str(sum))+5,0))
    pos = rect1.bottomright
    print_result = font.render(str(sum), True, WHITE)
    sc.blit(print_result, pos)
    
    pg.display.update()                
    clock.tick(FPS)
            