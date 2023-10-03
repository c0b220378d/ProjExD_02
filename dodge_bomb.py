import random as ran
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

def cheak_b(obj_rct: pg.Rect):
    """
    引数:こうかとんRect or 爆弾Rect
    戻り値:タプル(横方向判定結果, 縦方向判定結果)
    画面外ならTrue 画面内ならFalse
    """
    y, t = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        y = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        t = False
    return y, t


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bom_img = pg.Surface((20, 20))
    pg.draw.circle(bom_img, (255, 0, 0), (10, 10), 10)
    bom_img.set_colorkey((0, 0, 0))
    bom_rct = bom_img.get_rect()
    r_w = ran.randint(0, WIDTH)
    r_h = ran.randint(0, HEIGHT)
    bom_rct.center = (r_w, r_h)
    key_d = {
        pg.K_UP:(0, -5),
        pg.K_DOWN:(0, 5),
        pg.K_LEFT:(-5, 0),
        pg.K_RIGHT:(5, 0)
    }
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)
    vx, vy = 5, 5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bom_img, bom_rct)
        pg.display.update()
        key_lst = pg.key.get_pressed()
        sum_v = [0, 0]
        for key, mv in key_d.items():
            if key_lst[key]:
                sum_v[0] += mv[0]
                sum_v[1] += mv[1]
        bom_rct.move_ip(vx, vy)
        kk_rct.move_ip(sum_v[0], sum_v[1])

        #画面外チェック
        cheak_kk = cheak_b(kk_rct)
        if cheak_kk != (True, True):
            kk_rct.move_ip(-sum_v[0], -sum_v[1])
        cheak_bom = cheak_b(bom_rct)
        if cheak_bom[0] == False:
            vx *= -1
        if cheak_bom[1] == False:
            vy *= -1
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()