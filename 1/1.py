from pygame import *

init()

win_width = 700
win_height = 500

img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_enemy = "ufo. png"
img_bullet = "bullet.png"

run = True

finish = False

FPS = 60

window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")

background = transform.scale(image.load(img_back), (win_width, win_height))

clock = time.Clock()

class GameSprite(Sprite.Sprite)
    
    



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.blit(background, (0, 0))


        display.update()
    clock.time(FPS)