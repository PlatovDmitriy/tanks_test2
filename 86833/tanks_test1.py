from pygame import *
from time import time as timer
x = 10
y = 10
x1 = 500
y1 = 500
font.init()
font1 = font.Font(None,36)
BLACK = (0,0,0)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, x_speed, y_speed):
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
    def shoot(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets.append(bullet)
        
    def shoot2(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets4.append(bullet)
 
    def shoot3(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets2.append(bullet)

    def shoot4(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets3.append(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
    def update_2(self):
        self.rect.y -= self.speed
    
    def update_3(self):
        self.rect.x += self.speed
        
    def update_4(self):
        self.rect.x -= self.speed
class Player2(GameSprite):
    def update_45(self):
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
    def shoot_2(self):
        bullet2 = Bullet2('ener.png',x1,y1,20)
        bulls2.add(bullet2)
        bullets_2.append(bullet2)
        
    def shoot2_2(self):
        bullet2 = Bullet2('ener.png',x1,y1,20)
        bulls2.add(bullet2)
        bullets4_2.append(bullet2)
 
    def shoot3_2(self):
        bullet2 = Bullet2('ener.png',x1,y1,20)
        bulls2.add(bullet2)
        bullets2_2.append(bullet2)

    def shoot4_2(self):
        bullet2 = Bullet2('ener.png',x1,y1,20)
        bulls2.add(bullet2)
        bullets3_2.append(bullet2)


class Bullet2(GameSprite):
    def update_2(self):
        self.rect.y += self.speed
        
    def update_2_2(self):
        self.rect.y -= self.speed
    
    def update_3_2(self):
        self.rect.x += self.speed
        
    def update_4_2(self):
        self.rect.x -= self.speed
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
rec_time2 = False
num_fire2 = 0
shooot = 'shot.jpg'
bulls = sprite.Group()
bulls2 = sprite.Group()
#bullets2 = sprite.Group()
#bullets3 = sprite.Group()
#bullets4 = sprite.Group()
f = 1
wallsg = sprite.Group()

bullets = []
bullets2 = []
bullets3 = []
bullets4 = []
bullets_2 = []
bullets2_2 = []
bullets3_2 = []
bullets4_2 = []
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
player_1 = Player(down,10,10,0,0)
player_2 = Player2(down,500,500,0,0)
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
                    elif e.key == K_SPACE and rg == 2:
                        player_1.shoot2()
                    elif e.key == K_SPACE and rg == 3:
                        player_1.shoot()
                    elif e.key == K_SPACE and rg == 4:
                        player_1.shoot3()        
                    if e.key == K_LEFT:
                        player_1.x_speed = -10
                        player_1.image = transform.scale(image.load(left),(65,65))
                        rg = 2
            elif e.key == K_RIGHT:
                player_1.x_speed = 10
                player_1.image = transform.scale(image.load(right),(65,65))
                rg = 1
            elif e.key == K_UP:
                player_1.y_speed = -10
                player_1.image = transform.scale(image.load(top),(65,65))
                rg = 4
            elif e.key == K_DOWN:
                player_1.y_speed = 10
                player_1.image = transform.scale(image.load(down),(65,65))
                rg = 3
        
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                player_1.x_speed = 0
            elif e.key == K_RIGHT:
                player_1.x_speed = 0
            elif e.key == K_UP:
                player_1.y_speed = 0
            elif e.key == K_DOWN:
                player_1.y_speed = 0

            if num_fire >= 1 and rec_time == False:# не 
                    last_time = timer()
                    rec_time = True
                    
            if e.key == K_SPACE:
                if num_fire2 < 1 and rec_time2 == False:
                    num_fire2 += 1
                    if e.key == K_RSHIFT and sc == 1:
                        player_2.shoot4_2()
                    elif e.key == K_RSHIFT and sc == 2:
                        player_2.shoot2_2()
                    elif e.key == K_RSHIFT and sc == 3:
                        player_2.shoot_2()
                    elif e.key == K_RSHIFT and sc == 4:
                        player_2.shoot3_2()
                if num_fire2 >= 1 and rec_time2 == False:
                    last_time2 = timer()
                 
       
    if finish != True:
        window.blit(background,(0,0))
        player_1.reset()
        player_1.update()
        player_2.reset()
        player_2.update_45()
        wallsg.draw(window)
        bulls.draw(window)
        bulls2.draw(window)
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
        for bult in bullets_2:
            if bult.rect.y >= -65 and bult.rect.y <= h + 65:
                bult.update_2()
            #bulls.add(bul)
        for bult in bullets2_2:
            if bult.rect.y >= -65 and bult.rect.y <= h + 65:
                bult.update_2_2()
            #bulls.add(bul)
        for bult in bullets3_2:
            if bult.rect.x >= -65 and bult.rect.x <= w + 65:
                bult.update_3_2()
            #bulls.add(bul)
        for bult in bullets4_2:
            if bult.rect.x >= -65 and bult.rect.x <= w + 65:
                bult.update_4_2()
            #bulls.add(bul) 
        collides2 = sprite.groupcollide(bulls2, wallsg, True,True)
        if rec_time == True:
            now_time = timer()
            if now_time - last_time < 1.5:
                text_reload = font1.render('Перезарядка',1,(200,0,0)) 
                window.blit(text_reload,(260,460))
            else:
                num_fire = 0
                rec_time = False
        if rec_time2 == True:
            now_time2 = timer()
            if now_time2 - last_time < 1.5:
                text_reload2 = font1.render('Перезарядка',1,(200,0,0)) 
                window.blit(text_reload2,(600,460))
            else:
                num_fire2 = 0
                rec_time2 = False

        #if key.get_pressed()[K_w]:
         #   player_1 = Player(top,x,y,10)
          #  rg = 4
#
 #       if key.get_pressed()[K_s]:
  #          player_1 = Player(down,x,y,10)
   #         rg = 3
#
 #       if key.get_pressed()[K_a]:
  #          player_1 = Player(left,x,y,10)
   #         rg = 2
#
 #       if key.get_pressed()[K_d]:
  #          player_1 = Player(right,x,y,10)
   #         rg = 1
#
 #       if key.get_pressed()[K_UP]:
  #          player_2 = Player2(top,x1,y1,10)
   #         sc = 4
#
 #       if key.get_pressed()[K_DOWN]:
  #          player_2 = Player2(down,x1,y1,10)
   #         sc = 3
#
 #       if key.get_pressed()[K_LEFT]:
  #          player_2 = Player2(left,x1,y1,10)
   #         sc = 2
#
 #       if key.get_pressed()[K_RIGHT]:
  #          player_2 = Player2(right,x1,y1,10)
   #         sc = 1
#
 #       display.update()
  #  clock.tick(FPS)
