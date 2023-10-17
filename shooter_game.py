from pygame import *
from random import *
from time import time as timer #(Импортируем функцию для засекания времени)



window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('galaxy.jpg'),(700,500))



x = 65
y = 65



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
       
    def update1(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

    #def fire(self):
        #pul = Bullet("bullet.png", self.rect.centerx, self.rect.top, -15, 20, 15)
        #puly.add(pul)

        #if keys_pressed[K_w] and self.rect.y > 5:
            #self.rect.y -= self.speed
        #if keys_pressed[K_s] and self.rect.y < 650:
            #self.rect.y += self.speed
        #keys_pressed = key.get_pressed()
    



#class Enemy(GameSprite):
    #def update(self):
        #self.rect.y += self.speed
        #global propusk1
        #if self.rect.y > 500:
            #self.rect.y = 0
            #self.rect.x = randint(0, 630)
            #propusk1 += 1



#class Bullet(GameSprite):
    #def update(self):
        #self.rect.y += self.speed
        #if self.rect.y < 0:
            #self.kill()



#class Asteroid(GameSprite):
    #def update(self):
        #self.rect.y += self.speed
        #if self.rect.y > 500:
            #self.rect.y = 0
            #self.rect.x = randint(0, 630)    





#for i in range(5):     
    #vrag = Enemy("ufo.png", randint(5,640), 0, randint(1,5), 60, 55)
   # monsters.add(vrag)
#
#for i in range(3):     
    #asteroid = Asteroid("asteroid.png", randint(5,640), 0, 2, 60, 55)
   # asteroids.add(asteroid)
    


player = Player("rack.png", 50, 250, 5, 80, 100)
player1 = Player("rack.png", 600, 250, 5, 80, 100)
ball1 = Player("ball2.jpg", 250, 250, 5, 80, 100)
chet1 = 0
propusk1 = 0
speed_x = 3
speed_y = 3




rel_time = False
num_fire = 0
run = True 
finish = False
font.init()
font = font.Font(None, 36)

lose1 = font.render('Player 1 lose!', True,(180, 0, 0))
lose2 = font.render('Player 2 lose!', True,(180, 0, 0))
       
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False
    if ball1.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball1.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))
   

                
            
            


    if finish != True:
        
        ball1.rect.x += speed_x
        ball1.rect.y += speed_y
        
        window.blit(background,(0,0))
        player.reset()
        player1.reset()
      
        player.update()
        player1.update1()
       
        ball1.update()
        ball1.reset()        

    
        ball1.rect.x += speed_x
        ball1.rect.y += speed_y
        if ball1.rect.y > 500-80 or ball1.rect.y < 0:
        
            speed_y *= -1
        if sprite.collide_rect(player, ball1) or sprite.collide_rect(player1, ball1):
            speed_x *= -1

        
       
 
    display.update()

 

 
