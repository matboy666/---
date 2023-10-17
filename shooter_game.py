#Создай собственный Шутер!

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
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
    #def fire(self):
        #pul = Bullet("bullet.png", self.rect.centerx, self.rect.top, -15, 20, 15)
        #puly.add(pul)
    



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

puly = sprite.Group()



monsters = sprite.Group()



asteroids = sprite.Group()



#for i in range(5):     
    #vrag = Enemy("ufo.png", randint(5,640), 0, randint(1,5), 60, 55)
   # monsters.add(vrag)
#
#for i in range(3):     
    #asteroid = Asteroid("asteroid.png", randint(5,640), 0, 2, 60, 55)
   # asteroids.add(asteroid)
    


player = Player("rack.png", 50, 250, 5, 80, 100)
player1 = Player("rack.png", 600, 250, 5, 80, 100)
chet1 = 0
propusk1 = 0


rel_time = False
num_fire = 0
run = True 
finish = False
font.init()
font = font.Font(None, 36)

       
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    player.fire()
                elif num_fire >= 5 and rel_time == False:
                        rel_time = True
                        last_time = timer()

                
            
            


    if finish != True:
        window.blit(background,(0,0))
        player.reset()
        player1.reset()
        monsters.draw(window)
        player.update()
        player1.update()
        monsters.update()
        asteroids.update()
        asteroids.draw(window)
        puly.draw(window)
        puly.update()
    sprites_list = sprite.groupcollide(monsters, puly, True, True)
    for c in sprites_list:
        chet1 += 1
        vrag = Enemy("ufo.png", randint(5,640), 0, randint(1,5), 60, 55)
        monsters.add(vrag)   
    if chet1 > 5:
        finish = True
        window.blit(win,(200,200))
    if propusk1 > 20  or sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, asteroids, False):
        finish = True
        window.blit(lose,(200,200))   

    if rel_time == True:
        new_time = timer()     
        if new_time - last_time < 3:
            window.blit(per,(100,100))
        else:
            num_fire = 0
            rel_time = False
    display.update()

 