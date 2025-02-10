from configuration import *
import pygame
import random
import math
from weapons import *

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.terrain_spritesheet.get_image(991, 541, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.terrain_spritesheet.get_image(447, 353, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coin(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = COIN_LAYER
        self.groups = self.game.all_sprites, self.game.coins
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.coin_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if pygame.sprite.spritecollide(self, self.game.mainPlayer, False):
            self.kill()
            self.game.score += 1
            self.game.coin_sound.play()
            if self.game.score >= self.game.coins_to_collect:
                self.game.level_completed = True              
        
class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        self.game=game
        self._layer=PLAYER_LAYER
        self.healthbar = Player_Healthbar(game, x, y)
        
        self.groups = self.game.all_sprites, self.game.mainPlayer
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change= 0
        self.y_change= 0
        
        self.animationCounter= 1
        
        
        self.image = self.game.player_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.direction = "right"
        
        self.swordEqipped=False
        
        self.counter =0
        self.waitTime =10
        self.shootState ="shoot"
        
        self.health = PLAYER_HEALTH
       
        
    def move(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]:
            
            self.x_change = self.x_change - PLAYER_STEPS
            self.direction = "left"
            
            
        elif pressed[pygame.K_RIGHT]:
            
            self.x_change = self.x_change + PLAYER_STEPS
            self.direction = "right"            
 
        elif pressed[pygame.K_UP]:
            
            self.y_change = self.y_change - PLAYER_STEPS
            self.direction = "up"   

        elif pressed[pygame.K_DOWN]:
            
            self.y_change = self.y_change + PLAYER_STEPS
            self.direction = "down"  
    
    def update(self):
        self.move()
        self.animation()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
        self.collide_block()
        self.collide_enemy()
        self.x_change=0
        self.y_change=0
        
    def animation(self):
        
        downAnimation = [self.game.player_spritesheet.get_image(0,0,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,0,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,0,self.width, self.height),]
        
        
        leftAnimation = [self.game.player_spritesheet.get_image(0,32,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,32,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,32,self.width, self.height),]    
        
        rightAnimation = [self.game.player_spritesheet.get_image(0,64,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,64,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,64,self.width, self.height),]        

        upAnimation = [self.game.player_spritesheet.get_image(0,96,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,96,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,96,self.width, self.height),]          
        
        if self.direction =="down":
            if self.y_change ==0:
                self.image = self.game.player_spritesheet.get_image(0,0, self.width, self.height)
            
            else:
                self.image = downAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0

        if self.direction =="up":
            if self.y_change ==0:
                self.image = self.game.player_spritesheet.get_image(32,96, self.width, self.height)
            
            else:
                self.image = upAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0

        if self.direction =="left":
            if self.x_change ==0:
                self.image = self.game.player_spritesheet.get_image(32,32, self.width, self.height)
            
            else:
                self.image = leftAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0   
                    
                    
        if self.direction =="right":
            if self.x_change ==0:
                self.image = self.game.player_spritesheet.get_image(32,64, self.width, self.height)
            
            else:
                self.image = rightAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0  
                    
                    
    def collide_block(self):
        
        pressed = pygame.key.get_pressed()
        collideBlock = pygame.sprite.spritecollide(self,self.game.blocks, False, pygame.sprite.collide_rect_ratio(0.85) )
        
        if collideBlock:
            
            self.game.block_collided=True
          
            if pressed[pygame.K_LEFT]:
                self.rect.x += PLAYER_STEPS
                
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
                
            elif pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS     
    
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS  
        else:
            self.game.block_collided=False
                

    def collide_enemy(self):
        collide = pygame.sprite.spritecollide(self, self.game.enemies, False, pygame.sprite.collide_rect_ratio(0.85))
        if collide:
            self.game.enemy_hit_sound.play()  # Play enemy hit sound
            self.damage(1)  # Reduce player health by 1

    
    def damage(self, amount):
        self.health = self.health - amount
        self.healthbar.damage()
        
        if self.health <=0:
            self.kill()
            self.healthbar.kill_healthbar()
           # self.game.running=0
        
  
class Enemy(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change= 0
        self.y_change= 0
        
        self.image = self.game.enemy_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.numberSteps =random.choice([30,40,50,60,70,80,90])
        self.stallSteps = 120
        self.currentSteps =0
        
        self.state ="moving"
        self.animationCounter=1
        
        
        self.shootCounter =0
        self.waitShoot = random.choice([10,20,30,40,50,60,70,80,90])
        self.shootState = "halt"      
        
    def shoot(self):
        
        self.shootCounter +=1
        if self.shootCounter >= self.waitShoot:
            self.shootState="shoot"
            self.shootCounter=0
        
        
    def move(self):
        
        if self.state=="moving":
            
            
            if self.direction == "left":
                self.x_change = self.x_change - ENEMY_STEPS
                self.currentSteps += 1
                
                if self.shootState=="shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState="halt"
                
            
            elif self.direction == "right":
                self.x_change = self.x_change + ENEMY_STEPS
                self.currentSteps += 1
                if self.shootState=="shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)   
                    self.shootState="halt"
    
                
            elif self.direction == "up":
                self.y_change = self.y_change - ENEMY_STEPS            
                self.currentSteps += 1
                if self.shootState=="shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState="halt"
                
            elif self.direction == "down":
                self.y_change = self.y_change + ENEMY_STEPS    
                self.currentSteps += 1
                if self.shootState=="shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)   
                    self.shootState="halt"
                
        elif self.state =="stalling":
            self.currentSteps +=1
            if self.currentSteps == self.stallSteps:
                self.state ="moving"
                self.currentSteps=0
                self.direction = random.choice(['left', 'right', 'up', 'down'])  
            
    def animation(self):
        
        downAnimation = [self.game.enemy_spritesheet.get_image(0,0,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(32,0,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(64,0,self.width, self.height),]
        
        
        leftAnimation = [self.game.enemy_spritesheet.get_image(0,32,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(32,32,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(64,32,self.width, self.height),]    
        
        rightAnimation = [self.game.enemy_spritesheet.get_image(0,64,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(32,64,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(64,64,self.width, self.height),]        

        upAnimation = [self.game.enemy_spritesheet.get_image(0,96,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(32,96,self.width, self.height),
                         self.game.enemy_spritesheet.get_image(64,96,self.width, self.height),]          
        
        if self.direction =="down":
            if self.y_change ==0:
                self.image = self.game.enemy_spritesheet.get_image(0,0, self.width, self.height)
            
            else:
                self.image = downAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0

        if self.direction =="up":
            if self.y_change ==0:
                self.image = self.game.enemy_spritesheet.get_image(32,96, self.width, self.height)
            
            else:
                self.image = upAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0

        if self.direction =="left":
            if self.x_change ==0:
                self.image = self.game.enemy_spritesheet.get_image(32,32, self.width, self.height)
            
            else:
                self.image = leftAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0   
                    
                    
        if self.direction =="right":
            if self.x_change ==0:
                self.image = self.game.enemy_spritesheet.get_image(32,64, self.width, self.height)
            
            else:
                self.image = rightAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >=3:
                    self.animationCounter=0                  
 
            
    def update(self):
        self.move()
        self.animation()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
        self.x_change=0
        self.y_change=0 
        if self.currentSteps == self.numberSteps:
            if self.state!="stalling":
                self.currentSteps=0

            self.numberSteps =random.choice([30,40,50,60,70,80,90])
            self.state="stalling"
        self.collide_block()
        self.collide_Player()
        self.shoot()
     
    
    def collide_block(self):
        
        collideBlocks = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if collideBlocks:
            
         
            if self.direction=="left":
                self.rect.x += PLAYER_STEPS
                self.direction="right"
                
            elif self.direction=="right":
                self.rect.x -= PLAYER_STEPS
                self.direction="left"
                
            elif self.direction=="up":
                self.rect.y += PLAYER_STEPS  
                self.direction="down"
    
            elif self.direction=="down":
                self.rect.y -= PLAYER_STEPS  
                self.direction="up"
    
    def collide_Player(self):
        collide =  pygame.sprite.spritecollide(self, self.game.mainPlayer, True)
        if collide:
            self.game.running=False
        
            
        

class Player_Healthbar(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game=game
        self._layer=HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.healthbar
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        
        self.width = 40
        self.height = 10
        

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y- TILESIZE/2
    
    def move(self):
        self.rect.x = self.game.player.rect.x
        self.rect.y = self.game.player.rect.y - TILESIZE/2
    
    def kill_healthbar(self):
        self.kill()
        
    def damage(self):
        
        self.image.fill(RED)
        width = self.rect.width * self.game.player.health/PLAYER_HEALTH
        pygame.draw.rect( self.image, GREEN, (0,0,width, self.height), 0)
    def update(self):
        self.move()
