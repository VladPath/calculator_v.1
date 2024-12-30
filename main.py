from fcntl import flock
import pygame as pg
from buttons import button_block, calculate_func

clock = pg.time.Clock()

pg.init()

FPS = 60
W = 300
H = 400
HIGHT_SUM_DISPLAY = 100
one_symb = 18

WHITE = (255,255,255)
LIGHT_BLACK = (36, 35, 33)
DARK_GREY = (48, 47, 44)
GREY = (89, 86, 83)
ORANGE = (214, 159, 47)
hight_button = (H-HIGHT_SUM_DISPLAY)//5
width_button = W/4

sc = pg.display.set_mode((W,H))


pg.display.set_caption('Calculator v1.0')
icon = pg.image.load('img/calc_icon.jpg').convert()
icon.set_colorkey(WHITE)
pg.display.set_icon(icon)

pg.draw.rect(sc, DARK_GREY, (0,0,W,HIGHT_SUM_DISPLAY),0)


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

digits = [
    pg.K_0,pg.K_1,pg.K_2,pg.K_3,
    pg.K_4,pg.K_5,pg.K_6,pg.K_7,
    pg.K_8,pg.K_9,
]
symbols = [
    pg.K_8,
    pg.K_5,
    pg.K_MINUS,
    pg.K_SLASH,
    pg.K_BACKSPACE,
    61,
    pg.K_a,
    pg.K_COMMA,
    pg.K_PERIOD,
    ]

for i in symbols:
    print(i)

# signs for results
left_sign = ''
right_sigh = ''
sum = '0'

# font for sum 
font = pg.font.SysFont(None, 45)

the_calc_symbol=False
while 1:
    pg.draw.rect(sc, DARK_GREY, (0,0,W,HIGHT_SUM_DISPLAY),0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
        # Главный цикл программы
        elif event.type == pg.KEYDOWN:
            print(event.key)
            if event.key == pg.K_PLUS:
                left_sign = '+'
                
            # ввод '=' для получения результата x,y 
            elif  event.key in(pg.K_EQUALS,pg.K_RETURN) and event.mod != pg.KMOD_LSHIFT and right_sigh\
                or event.key == pg.K_5 and event.mod == pg.KMOD_LSHIFT and right_sigh:
                    
                sum = calculate_func(the_calc_symbol,event.key, left_sign, right_sigh)
                left_sign = sum
                calculate = left_sign 
                right_sigh = ''
                the_calc_symbol = False
                
            # ввод символов для вычисления
            elif event.mod == pg.KMOD_LSHIFT and  event.key in symbols and not the_calc_symbol:
                # Если нажали Lshift + а производим противоположное число
                if event.key == pg.K_a:
                    if right_sigh:
                        if int(right_sigh) > 0:
                            right_sigh = '-'+right_sigh
                        else:
                            right_sigh = right_sigh[1:]
                    elif left_sign:
                        if int(left_sign) > 0:
                            left_sign = '-'+left_sign
                        else:
                            left_sign = left_sign[1:]
                            
                # если нажата клавиша shift+5  и нет  значения счета 
                # вернуть какой это процент от ста
                elif event.key == pg.K_5 and not the_calc_symbol:
                    left_sign = str(int(left_sign)/100)
                
                elif event.key == pg.K_5 and the_calc_symbol:
                    right_sigh = str(int(left_sign)/100)
                
                elif event.key in (pg.K_COMMA,pg.K_PERIOD ) and not the_calc_symbol:
                    left_sign = left_sign + '.'
                    
                elif event.key in (pg.K_COMMA,pg.K_PERIOD ) and the_calc_symbol:
                    right_sigh = right_sigh + '.'
                
                else:       
                    the_calc_symbol = event.key
            
            # Ввод цифр в левое и правое значение
            elif event.key in digits:
                for i,dig in enumerate(digits):
                    if event.key == dig and not the_calc_symbol:
                        left_sign = left_sign + str(i)
                    if event.key == dig and the_calc_symbol:
                        right_sigh = right_sigh + str(i)

                
        
    # sum = int(left_sign) + int(right_sigh) + int(start_zero)
    if not left_sign:
        calculate = sum
    elif not the_calc_symbol:
        calculate = left_sign
    elif the_calc_symbol and not right_sigh:
        calculate = 0
    elif the_calc_symbol and right_sigh:
        calculate = right_sigh
    
    
        
    rect1 = pg.Rect((0,HIGHT_SUM_DISPLAY-40,(W-30)-(one_symb)*len(str(calculate))+5,0))
    pos = rect1.bottomright
    print_result = font.render(str(calculate), True, WHITE)
    sc.blit(print_result, pos)
    # pg.draw.rect(sc,WHITE,(0,HIGHT_SUM_DISPLAY,W,0),1)
    pg.display.update()
    clock.tick(FPS)
            