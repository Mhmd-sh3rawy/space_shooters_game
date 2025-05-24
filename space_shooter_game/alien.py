import pygame ,random
from loadfucntions import *

class Alien(pygame.sprite.Sprite):
    """
    Represents an alien enemy sprite that can move horizontally.
    
    Args:
        type: The type/variant of alien (affects sprite appearance)
        x: Initial x position
        y: Initial y position
    """
    def __init__(self ,type ,x ,y):
        super().__init__()
        self.type = type
        self.x =x
        self.y =y
        path =f"Graphics/alien_{type}.png"
        self.image = pygame.image.load(path_load(path))
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self ,direction):
        """
        Updates the alien's position by moving it horizontally.
        
        Args:
            direction: Horizontal movement amount (positive = right, negative = left)
        """
        # direction is a brameter for move
        self.rect.x += direction

class Mystery_ship(pygame.sprite.Sprite):
    """
    Represents a mystery ship that flies across the screen horizontally.
    The ship spawns from either side and moves across, disappearing when it reaches the opposite edge.
    
    Args:
        screen_width: Width of the game screen
        offset: Screen offset/margin value
    """
    def __init__(self,screen_width,offset):
        super().__init__()
        self.image = pygame.image.load(path_load("Graphics/mystery.png"))
        self.speed = 3
        self.screen_width = screen_width
        self.offset =offset
        # Randomly spawn from left or right side of screen
        x= random.choice([self.offset/2 ,self.screen_width+self.offset-self.image.get_width()])
        self.rect = self.image.get_rect(topleft =(x ,80))

        # Set movement direction based on spawn position
        if x ==self.offset/2:
            self.speed = 3  # Move right
        else:
            self.speed = -3  # Move left
    
    def update(self):
        """Updates the mystery ship's position and removes it when it goes off-screen."""
        self.rect.x += self.speed
        # Remove ship when it goes off the right edge
        if self.rect.right > self.screen_width+self.offset:
            self.kill()
        # Remove ship when it goes off the left edge
        if self.rect.left < self.offset/2:
            self.kill()