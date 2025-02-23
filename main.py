from pygame import *

class GameShrite(sprite.Sprite):
    def __init__(self, pimage, x, y, speed):
        super().__init__()

        self.pimage = transform.scale(image.load(pimage), (65, 65))
        self.rect = self.pimage.get_rect()
        self.speed =  speed
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.pimage, (self.rect.x, self.rect.y))

class Player(GameShrite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-self.rect.height:
            self.rect.y += self.speed
        if keys[K_a]  and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d]  and self.rect.x < win_width-self.rect.width:
            self.rect.x += self.speed

class Enemy(GameShrite):
    direction = 'left'
    def update(self):
        if self.rect.x > win_width-self.rect.width:
           self.direction = 'left'
        if self.rect.x < win_width*0.7:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed


win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))

backgrount = transform.scale(image.load("background.jpg"), (win_width, win_height))
display.set_caption("Лабіринт")

player = Player("hero.png", 10, win_height-80, 4)
enemy = Enemy("cyborg.png", win_width-80, 80, 2)
final = GameShrite('treasure.png', win_width-80, win_height-80, 0)
game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    window.blit(backgrount, (0, 0))
    player.update()
    enemy.update()
    player.draw()
    enemy.draw()
    final.draw()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

    







