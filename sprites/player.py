import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,x:int=400, y:int=400):
        super().__init__()
        self.image_path = os.path.join("assets", "Net.png")
        self.image = pygame.image.load(self.image_path).convert_alpha()
        # Optionally scale it
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        # Create rect for positioning
        self.x = float(x)
        self.y = float(y)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, screen_width:int=1280, screen_height:int=720):
        keys = pygame.key.get_pressed()
        speed = 5
        
        # Movement with arrow keys or WASD
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += speed
        
        # Boundary checking - keep player on screen
        sprite_width = 50
        sprite_height = 50
        
        if self.x < 0:
            self.x = 0
        if self.x + sprite_width > screen_width:
            self.x = screen_width - sprite_width
        if self.y < 0:
            self.y = 0
        if self.y + sprite_height > screen_height:
            self.y = screen_height - sprite_height
        
        # Update rect position
        self.rect.x = self.x
        self.rect.y = self.y