import pygame
import random
import os
import math

class Trash(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, angle:float=45, speed:int=4):
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

        self.x_speed = int(speed)
        self.y_speed = int(speed)
        angle_rad = math.radians(angle)
        self.vel_x = math.cos(angle_rad) * speed
        self.vel_y = math.sin(angle_rad) * speed
        
        # Wobble parameters for non-linear motion
        self.frame = 0
        self.wobble_amplitude = random.uniform(7, 11)
        self.wobble_frequency = random.uniform(0.02, 0.04)
    
    def update(self, turtle_coords:tuple[int|float, int|float]):
        x_distance_apart = turtle_coords[0] - self.x
        y_distance_apart = turtle_coords[1] - self.y

        self.angle = math.atan2(y_distance_apart, x_distance_apart)

        self.x_speed = random.randint(2, 5)
        self.y_speed = random.randint(2,5)

        self.vel_x = math.cos(self.angle) * self.x_speed
        self.vel_y = math.sin(self.angle) * self.y_speed
        
        # Add wobble motion (sine wave perpendicular to direction)
        wobble_offset = math.cos(self.frame * self.wobble_frequency) * self.wobble_amplitude
        # Perpendicular angle (90 degrees offset)
        wobble_angle = self.angle + math.pi / 2
        self.vel_x += math.cos(wobble_angle) * wobble_offset
        self.vel_y += math.sin(wobble_angle) * wobble_offset
        self.frame += 1
        
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