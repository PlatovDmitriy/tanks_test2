from pygame import *
from time import time as timer
x = 10
y = 10
x1 = 900
y1 = 900
font.init()
font1 = font.SysFont('Arial',36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, x_speed,y_speed):#добавила скорость по x и по y
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.x_speed = x_speed #добавила скорость по x и по y
        self.y_speed = y_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        #движение по горизонтали
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)

        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        #движение по вертикали
        self.rect.y += self.y_speed    
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        # keys_pressed = key.get_pressed()
        # if keys_pressed[K_UP] and self.rect.y > 0:
        #     self.rect.y -= 15
        #     global y 
        #     y -= 15
        # if keys_pressed[K_DOWN] and self.rect.y < 920:
        #     self.rect.y += 15
        #     y += 15
        # if keys_pressed[K_LEFT] and self.rect.x > 0:
        #     self.rect.x -= 15
        #     global x 
        #     x -= 15
        # if keys_pressed[K_RIGHT] and self.rect.x < 1800:
        #     self.rect.x += 15
        #     x += 15
    def shoot(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,20,20)
        bulls.add(bullet)
        bullets.append(bullet)
        
    def shoot2(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,20,20)
        bulls.add(bullet)
        bullets4.append(bullet)
 
    def shoot3(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,20,20)
        bulls.add(bullet)
        bullets2.append(bullet)

    def shoot4(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,20,20)
        bulls.add(bullet)
        bullets3.append(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.y_speed
        
    def update_2(self):
        self.rect.y -= self.y_speed
    
    def update_3(self):
        self.rect.x += self.x_speed
        
    def update_4(self):
        self.rect.x -= self.x_speed
        
class Walls(sprite.Sprite):
    def __init__(self,name,cor_x, cor_y ):
        super().__init__ ()
        self.image = transform.scale(image.load(name),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

                
rec_time = False
num_fire = 0
shooot = 'shot.jpg'
bulls = sprite.Group()
#bullets2 = sprite.Group()
#bullets3 = sprite.Group()
#bullets4 = sprite.Group()
f = 1
wallsg = sprite.Group()

bullets = []
bullets2 = []
bullets3 = []
bullets4 = []

sc = 0
rg = 0

rg1 = 0
game = True
clock = time.Clock()
FPS = 120
finish = False
w = 1900
h = 1000
top = 'tank_player_1_top.png'
down = 'tank_player_1_down.png'
left = 'tank_player_1_left.png'
right = 'tank_player_1_right.png'
#sv = 0
#top1 = 'top.png'
#down1 = 'down.png'
#left1 = 'left.png'
window = display.set_mode((w,h))
background = transform.scale(image.load('background1.jpg'),(w,h))
player_1 = Player(down,10,10,0,0) #сюда добавили обе скорости по 0
wall1 = Walls('block.png',150,150)
wall2 = Walls('block.png',150,85)
wall3 = Walls('block.png',150,215)
wall4 = Walls('block.png',150,280)
wall5 = Walls('block.png',150,345)
wall6 = Walls('block.png',150,410)
wall7 = Walls('block.png',150,475)
wall8 = Walls('block.png',150,540)
wallsg.add(wall1)
wallsg.add(wall2)
wallsg.add(wall3)
wallsg.add(wall4)
wallsg.add(wall5)
wallsg.add(wall6)
wallsg.add(wall7)
wallsg.add(wall8)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 1 and rec_time == False:
                    num_fire += 1
                    
                    if e.key == K_SPACE and rg == 1:
                        player_1.shoot4()
                    if e.key == K_SPACE and rg == 2:
                        player_1.shoot2()
                    if e.key == K_SPACE and rg == 3:
                        player_1.shoot()
                    if e.key == K_SPACE and rg == 4:
                        player_1.shoot3()
        #движение теперь вот тут        
            elif e.key == K_a:
                player_1.x_speed = -10
                player_1.image = transform.scale(image.load(left),(65,65))
                rg = 2
                x -=10
            elif e.key == K_d:
                player_1.x_speed = 10
                player_1.image = transform.scale(image.load(right),(65,65))
                rg = 1
                x +=10
            elif e.key == K_w:
                player_1.y_speed = -10
                player_1.image = transform.scale(image.load(top),(65,65))
                rg = 4
                x -= 10
            elif e.key == K_s:
                player_1.y_speed = 10
                player_1.image = transform.scale(image.load(down),(65,65))
                rg = 3
                x += 10
    
        elif e.type == KEYUP:
            if e.key == K_a:
                player_1.x_speed = 0
            elif e.key == K_d:
                player_1.x_speed = 0
            elif e.key == K_w:
                player_1.y_speed = 0
            elif e.key == K_s:
                player_1.y_speed = 0

        if num_fire >= 1 and rec_time == False:
            last_time = timer()
            rec_time = True
        
       
    if finish != True:
        window.blit(background,(0,0))
        player_1.reset()
        player_1.update()
        wallsg.draw(window)
        bulls.draw(window)
        for bul in bullets:
            if bul.rect.y >= -65 and bul.rect.y <= h + 65:
                bul.update()
            #bulls.add(bul)
        for bul in bullets2:
            if bul.rect.y >= -65 and bul.rect.y <= h + 65:
                bul.update_2()
            #bulls.add(bul)
        for bul in bullets3:
            if bul.rect.x >= -65 and bul.rect.x <= w + 65:
                bul.update_3()
            #bulls.add(bul)
        for bul in bullets4:
            if bul.rect.x >= -65 and bul.rect.x <= w + 65:
                bul.update_4()
            #bulls.add(bul) 
        collides = sprite.groupcollide(bulls, wallsg, True,True)
        if rec_time == True:
            now_time = timer()
            if now_time - last_time < 1.5:
                #text_reload = font1.render('Перезарядка',1,(200,0,0)) 
                #window.blit(text_reload,(260,460))
                pass
            else:
                num_fire = 0
                rec_time = False

        if key.get_pressed()[K_w] and y > 0:
            pass
        #     player_1 = Player(top,x,y,10)
        #     rg = 4

        # if key.get_pressed()[K_DOWN]:
        #     player_1 = Player(down,x,y,10)
        #     rg = 3

        # if key.get_pressed()[K_LEFT]:
        #     player_1 = Player(left,x,y,10)
        #     rg = 2

        # if key.get_pressed()[K_RIGHT]:
        #     player_1 = Player(right,x,y,10)
        #     rg = 1
        

        display.update()
    clock.tick(FPS)
