from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption("Shooter")
background = transform.scale(image.load("galaxy.jpg"), (700,500))

class player():
    def __init__(self, image1, x, y):
        self.image1 = transform.scale(image.load(image1), (100, 100))
        self.rect = self.image1.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image1, (self.rect.x, self.rect.y))

class enemy(sprite.Sprite):
    def __init__(self, image2, x, y):
        super().__init__()
        self.image2 = transform.scale(image.load(image2), (70, 40))
        self.rect = self.image2.get_rect()
        self.rect.x = randint(1, 600)
        self.rect.y = 0
        self.speed = randint(1, 5)

    def update1(self):
        window.blit(self.image2, (self.rect.x, self.rect.y))

    def movement(self):
        global missed
        if self.rect.y >= 500:
            self.rect.y = 0
            missed += 1
        self.rect.y += self.speed

class bullet(sprite.Sprite):
    def __init__(self, image1, x, y):
        super().__init__()
        self.image1 = transform.scale(image.load(image1), (10, 20))
        self.rect = self.image1.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 7
        
    def update1(self):
        window.blit(self.image1, (self.rect.x, self.rect.y))

    def bsp(self):
        self.rect.y -= self.speed    



mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

init()
font1 = font.SysFont('Arial', 36)


game = True
clock = time.Clock()

missed = 0
score = 0
timer = time.get_ticks()
rocket = player("rocket.png", 100, 390)
ufo1 = enemy("ufo.png", 100, 100)
ufo2 = enemy("ufo.png", 100, 100)
ufo3 = enemy("ufo.png", 100, 100)
ufo4 = enemy("ufo.png", 100, 100)
ufo5 = enemy("ufo.png", 100, 100)

enemys = sprite.Group()
bullets = sprite.Group()
enemys.add(ufo1)
enemys.add(ufo2)
enemys.add(ufo3)
enemys.add(ufo4)
enemys.add(ufo5)


while game:
    window.blit(background, (0, 0))
    
    for i in enemys:
        i.update1()
        i.movement()

    rocket.update()
    
    x1 = sprite.groupcollide(enemys, bullets, True, True)
    if x1:
        score += 1
        ufo1 = enemy("ufo.png", 100, 100)
        enemys.add(ufo1)

    if key.get_pressed()[K_LEFT] and rocket.rect.x >= 10:
        rocket.rect.x -= 5

    if key.get_pressed()[K_RIGHT] and rocket.rect.x <= 590:
        rocket.rect.x += 5

    msd = font1.render(f"{missed}", True, (255, 255, 255))
    window.blit(msd, (680, 10))
    scr = font1.render(f"{score}", True, (255, 255, 255))
    window.blit(scr, (10, 10))


    for e in event.get():
        if e.type == QUIT:
            game = False

    if key.get_pressed()[K_SPACE] and time.get_ticks() - timer >= 500:
        fire = bullet("bullet.png", rocket.rect.x + 45, rocket.rect.y)
        bullets.add(fire)
        timer = time.get_ticks()
        

    for new_bullet in bullets:
        new_bullet.update1()
        new_bullet.bsp()

    display.update()
    clock.tick(60)

print(missed)