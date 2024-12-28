import pygame as pg

W = 300
H = 400

WHITE = (255,255,255)
DARK_GREY = (46, 45, 43)
GREY = (89, 86, 83)
sc = pg.display.set_mode((W,H))

pg.display.set_caption('Calculator v1.0')
icon = pg.image.load('img/calc_icon.jpg').convert()
icon.set_colorkey(WHITE)
pg.display.set_icon(icon)

# background
pg.draw.rect(sc, DARK_GREY, (0,0,W,75),0,)
pg.draw.rect(sc, GREY, (0,75,W,H),0,)
pg.display.update()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            