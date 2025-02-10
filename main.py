from configuration import *
from weapons import *
from sprites import *
import sys
import pygame

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()

    def get_image(self, x,y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        
        return sprite
class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png') #991,541
        self.player_spritesheet = Spritesheet('assets/images/cats.png')
        self.enemy_spritesheet = Spritesheet('assets/images/evil.png')
        self.bullet_spritesheet = Spritesheet('assets/images/powerBall.png')
        self.coin_spritesheet = Spritesheet('assets/images/coin.png')
        self.running = True
        self.enemy_collided = False
        self.block_collided = False
        self.score = 0
        self.level = 1
        self.coins_to_collect = 10  # For Level 1
        self.level_completed = False
        self.game_over = False
        self.message = None
        self.message_timer = 0
        self.restart = False

        # Load sounds
        pygame.mixer.music.load('assets/sounds/background.mp3')
        pygame.mixer.music.play(-1)
        self.coin_sound = pygame.mixer.Sound('assets/sounds/coin.wav')
        self.enemy_hit_sound = pygame.mixer.Sound('assets/sounds/enemy_hit.wav')
        self.enemy_hit_sound.set_volume(0.5)

        # Camera variables
        self.camera_x = 0
        self.camera_y = 0
        
        
        
    def createTileMap(self, tilemap):
        for i, row in enumerate(tilemap):
            for j , column in enumerate(row):
                Ground(self,j,i)
                if column=='B':
                    Block(self,j,i)
                if column=='P':
                    self.player=Player(self,j,i)
                if column=="E":
                    Enemy(self,j,i)
                if column =="C":
                    Coin(self,j,i)
    
    
    def create(self):
        self.all_sprites =pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        
        self.enemies= pygame.sprite.LayeredUpdates()
        self.mainPlayer = pygame.sprite.LayeredUpdates()
        
        self.bullets = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.coins = pygame.sprite.LayeredUpdates()

        if self.level == 1:
            self.createTileMap(tilemap_level1)
        else:
            self.createTileMap(tilemap_level2)

        # Calculate level boundaries
        self.level_width = len(tilemap_level1[0]) * TILESIZE
        self.level_height = len(tilemap_level1) * TILESIZE
    
    def update(self):

        if self.game_over or self.level_completed:
            return
    
        self.all_sprites.update()

        if self.level_completed:
            if self.level == 1:
                self.message = "Level 1 Completed!  "
                self.message_timer = pygame.time.get_ticks()
                self.level = 2
                self.coins_to_collect = 20  # For Level 2
                self.create()
                self.level_completed = False
            else:
                self.message = "Level 2 Completed.  You Win!  "
                self.message_timer = pygame.time.get_ticks()
                self.game_over = True

        if self.player.health <= 0:
            self.message = "Game Over!  "
            self.message_timer = pygame.time.get_ticks()
            self.game_over = True

        # Clear message after 5 seconds
        if self.message and pygame.time.get_ticks() - self.message_timer > 5000:
            self.message = None
            if self.player.health <= 0 or self.game_over:
                self.running = False

    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (self.game_over or self.level_completed):
                    self.restart = True
    
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        # Split the text into two lines if it's too long
        lines = text.split('  ')  # Split at '  ' for the second line (you can adjust this)
    
        y_offset = y
        for line in lines:
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y_offset)
            self.screen.blit(text_surface, text_rect)
            y_offset += size  # Move the y position down for the next line
    
    def camera(self):
        if self.game_over or self.level_completed:
            return  # Prevent movement if the game is over or the level is completed

        # Center the camera on the player
        self.camera_x = self.player.rect.x - WIN_WIDTH // 2
        self.camera_y = self.player.rect.y - WIN_HEIGHT // 2

        # Restrict camera movement to level boundaries
        self.camera_x = max(0, min(self.camera_x, self.level_width - WIN_WIDTH))
        self.camera_y = max(0, min(self.camera_y, self.level_height - WIN_HEIGHT))



    def draw(self):
        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y - self.camera_y))
        
        # Draw the level and score text
        self.draw_text(f"Level: {self.level} | Score: {self.score}", 36, WHITE, WIN_WIDTH // 2, 20)

        # Display multi-line messages
        if self.message:
            self.draw_text(self.message + "PRESS SPACE TO PLAY AGAIN", 72, WHITE, WIN_WIDTH // 2, WIN_HEIGHT // 2)
        pygame.display.update()


    def main(self):
        while self.running:
            self.events()
            self.camera()
            self.update()
            self.draw()
            if self.restart:
                self.__init__()
                self.create()
                self.restart = False
    
    


game = Game()
game.create()

while game.running:
    game.main()
    
pygame.quit()
sys.exit()
