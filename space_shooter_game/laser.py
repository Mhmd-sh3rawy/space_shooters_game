import pygame

class Laser(pygame.sprite.Sprite):
    """
    Represents a laser projectile that moves vertically on screen.
    
    Args:
        position: Tuple of (x, y) coordinates for laser's initial center position
        speed: Movement speed of the laser (pixels per frame)
        screen_height: Height of the game screen for boundary checking
    """
    def __init__(self,position ,speed,screen_height):
        super().__init__()
        # make a rectangle
        self.image= pygame.Surface((4,15))
        self.image.fill((243,216,63))  # Yellow color
        self.rect =self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height =screen_height
    
    def update(self):
        """Updates laser position and removes it when it goes off-screen."""
        self.rect.y -= self.speed
        # Remove laser when it goes off screen (top or bottom)
        if self.rect.y > self.screen_height+15 or self.rect.y < 0:
            self.kill()