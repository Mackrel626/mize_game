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

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))

backgrount = transform.scale(image.load("background1.jpg"), (win_width, win_height))
display.set_caption("Лабіринт")

player = Player("patron.png", 10, win_height-80, 4)
enemy = Enemy("enem.png", win_width-80, win_height-145, 2)
final = GameShrite('bomb.png', win_width-80, win_height-80, 0)

wall = Wall(84, 18, 18, 50, 20, 15, 350)
wall1 = Wall(84, 18, 18, 50, 20, 600, 15)
wall2 = Wall(84, 18, 18, 50, 480, 500, 15)
wall3 = Wall(84, 18, 18, 135, 135, 15, 350)
wall4 = Wall(84, 18, 18, 225, 20, 15, 350)
wall5 = Wall(84, 18, 18, 315, 135, 15, 350)
wall6 = Wall(84, 18, 18, 420, 20, 15, 350)
wall7 = Wall(84, 18, 18, 535, 420, 15, 70)


game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

while game:
    window.blit(backgrount, (0, 0))
    wall.draw_wall()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    player.update()
    enemy.update()
    player.draw()
    enemy.draw()
    final.draw()
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(player, wall) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) or sprite.collide_rect(player, enemy):
        kick.play()
        player.rect.x = 10
        player.rect.y = win_height-85
    if sprite.collide_rect(player, final):
        time.delay(1000)
        money.play()
        game = False
    display.update()
    clock.tick(FPS)

    







