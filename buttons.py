import pygame as pg
clock = pg.time.Clock()

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
    
symblos_id=[
    {56:'*',
    44: '%',
    53: ',',
    45: '-',
    61: '+',
    47: '/',
    97: 'abs',}
]

def calculate_func(calc_symbol:int, eq:int, x:int=0, y:int=0) -> str:
    try :
        x = int(x)
    except:
        x = float(x)
    try :
        y = int(y)
    except:
        y = float(y)
    # вычисление 
    if symblos_id[0][calc_symbol] == '*':
        # если ищутся =
        if eq == pg.K_EQUALS:
            return str(x*y)
        # иначе ищутся %
        else:
            return str(str(0.01 * y))
            
    elif symblos_id[0][calc_symbol] =='%':
        if eq == pg.K_EQUALS: 
            return str(x%y)
        # для процента вариантов нет
        
    elif symblos_id[0][calc_symbol] =='+':
        if eq == pg.K_EQUALS: 
            return str(round((x+y), 2))
        else:
            return x + ((x/100)*y)
    
    elif symblos_id[0][calc_symbol] =='-':
        if eq == pg.K_EQUALS:  
            return str(x-y)
        else:
            return x - ((x/100)*y)
        
    elif symblos_id[0][calc_symbol] =='/':
        if eq == pg.K_EQUALS: 
            if y == 0:
                return "Ошибка деления на 0"
            else:
                return str(int(x/y))
        else:
            pass
    
    return str('Ошибка 101')
    
print(10*1%0.1)