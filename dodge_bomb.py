import random as ran
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bom_img = pg.Surface((10, 10))
    pg.draw.circle(bom_img, (255, 0, 0), (5, 5), 5)
    bom_img.set_colorkey((0, 0, 0))
    bom_rct = bom_img.get_rect()
    r_w = ran.randint(0, WIDTH)
    r_h = ran.randint(0, HEIGHT)
    bom_rct.center = (r_w, r_h)
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bom_img, bom_rct)
        pg.display.update()
        bom_rct.move_ip(5, 5)
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()