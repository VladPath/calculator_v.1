import pygame as pg
from buttons import button_block

pg.init()

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
img = font.render('+', True, WHITE)
sc.blit(img, (HIGHT_SUM_DISPLAY,HIGHT_SUM_DISPLAY))
buttons = [
    {'title':'AC','coords':(0, HIGHT_SUM_DISPLAY), 'color':DARK_GREY},
    {'title':'plus_minus','coords':(width_button, HIGHT_SUM_DISPLAY),'color':DARK_GREY},
    {'title':'percent','coords':(width_button*2, HIGHT_SUM_DISPLAY),'color':DARK_GREY},
    {'title':'devide','coords':(width_button*3, HIGHT_SUM_DISPLAY),'color':ORANGE},
    {'title':'multyply','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button),'color':ORANGE},
    {'title':'minus','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button*2),'color':ORANGE},
    {'title':'plus','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button*3),'color':ORANGE},
    {'title':'result','coords':(width_button*3, HIGHT_SUM_DISPLAY+hight_button*4),'color':ORANGE},
    {'title':'point','coords':(width_button*2, HIGHT_SUM_DISPLAY+hight_button*4),'color':GREY},
    {'title':'zero','coords':(0, HIGHT_SUM_DISPLAY+hight_button*4),'color':GREY, 'is_zero':1},
    {'title':'one','coords':(0, HIGHT_SUM_DISPLAY+hight_button*3),'color':GREY},
    {'title':'two','coords':(width_button, HIGHT_SUM_DISPLAY+hight_button*3),'color':GREY},
    {'title':'three','coords':( width_button*2, HIGHT_SUM_DISPLAY+hight_button*3),'color':GREY},
    {'title':'four','coords':( 0, HIGHT_SUM_DISPLAY+hight_button*2),'color':GREY},
    {'title':'five','coords':( width_button, HIGHT_SUM_DISPLAY+hight_button*2),'color':GREY},
    {'title':'six','coords':( width_button*2, HIGHT_SUM_DISPLAY+hight_button*2),'color':GREY},
    {'title':'seven','coords':( 0, HIGHT_SUM_DISPLAY+hight_button),'color':GREY},
    {'title':'eight','coords':(width_button, HIGHT_SUM_DISPLAY+hight_button),'color':GREY},
    {'title':'nine','coords':( width_button*2, HIGHT_SUM_DISPLAY+hight_button),'color':GREY},
]


for but in buttons:
    if but.get('is_zero'):
        x = button_block(but['title'],but['color'],but['coords'][0],but['coords'][1],is_zero=1)
    else:
        x = button_block(but['title'],but['color'],but['coords'][0],but['coords'][1])
    x.get_block()
     
    

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
    
pg.display.update()
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            