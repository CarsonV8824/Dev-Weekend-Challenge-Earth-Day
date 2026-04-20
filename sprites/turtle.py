import pygame
import random
import os

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Turtle(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int):
        self.images = ["Turtle.png"]
        self.chossen_image = random.choice(self.images)
        self.image_path = os.path.join(PROJECT_ROOT, "assets", self.chossen_image)
        super().__init__()
        # Load the PNG image
        self.image = pygame.image.load(self.image_path).convert_alpha()
        # Optionally scale it
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        # Create rect for positioning
        self.x = float(x)
        self.y = float(y)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def update(self):
        pass

    def get_coords(self) -> tuple[float, float]:
        return (self.x, self.y)