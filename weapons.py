from configuration import *
import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.y = y
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.bullet_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.direction = self.game.player.direction
        
        self.damage=1
        
    def move(self):
        
        if self.direction =="right":
            self.rect.x += BULLET_STEPS
             
            
        if self.direction =="left":
            self.rect.x -= BULLET_STEPS        
            
        if self.direction =="up":
            self.rect.y -= BULLET_STEPS
            
        if self.direction =="down":
            self.rect.y += BULLET_STEPS
    def collide_block(self):
         collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
         if collide:
             self.kill()
    def collide_Enemy(self):
         collide = pygame.sprite.spritecollide(self, self.game.enemies, False)
         if collide:
             collide[0].damage(self.damage)   
             self.kill()
    def update(self):
        self.move()
        self.collide_Enemy()
        self.collide_block()
        

class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.y = y
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.bullet_spritesheet.get_image(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.direction = self.game.player.direction
        
        self.damage=1
        
    def move(self):
        
        if self.direction =="right":
            self.rect.x += BULLET_STEPS
             
            
        if self.direction =="left":
            self.rect.x -= BULLET_STEPS        
            
        if self.direction =="up":
            self.rect.y -= BULLET_STEPS
            
        if self.direction =="down":
            self.rect.y += BULLET_STEPS
    def collide_block(self):
         collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
         if collide:
             self.kill()
    def collide_Player(self):
         collide = pygame.sprite.spritecollide(self, self.game.mainPlayer , False)
         if collide:
            self.game.player.damage(self.damage)
            self.game.enemy_hit_sound.play()  # Play enemy hit sound
            self.kill()
             
    def update(self):
        self.move()
        self.collide_Player()
        self.collide_block()