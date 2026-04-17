import pygame
import random
import os
import math

class Trash(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, angle:float=45, speed:int=2):
        self.images = ["Bottle.png", "Plastic_Bag.png", ]
        self.chossen_image = random.choice(self.images)
        self.image_path = os.path.join("assets", self.chossen_image)
        super().__init__()
        # Load the PNG image
        self.original_image = pygame.image.load(self.image_path).convert_alpha()
        # Optionally scale it
        self.original_image = pygame.transform.scale(self.original_image, (50, 50))
        
        # Store angle and rotate image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, -angle)
        
        # Create rect for positioning
        self.x = float(x)
        self.y = float(y)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.speed = int(speed)
        angle_rad = math.radians(angle)
        self.vel_x = math.cos(angle_rad) * speed
        self.vel_y = math.sin(angle_rad) * speed
    
    def update(self, tutrle_coords:tuple[int|float, int|float]):
        x_distance_apart = tutrle_coords[0] - self.x
        y_distance_apart = tutrle_coords[1] - self.y

        self.angle = math.atan2(y_distance_apart, x_distance_apart)

        self.vel_x = math.cos(self.angle) * self.speed
        self.vel_y = math.sin(self.angle) * self.speed
        # Move sprite
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Rotate image (convert radians to degrees for rotation)
        angle_degrees = math.degrees(self.angle)
        self.image = pygame.transform.rotate(self.original_image, -angle_degrees)
        
        # Update rect position (center to avoid position jumping)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
        self.rect.x = self.x
        self.rect.y = self.y