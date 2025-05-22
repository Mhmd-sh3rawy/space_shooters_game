import pygame
from laser import Laser
from loadfucntions import *
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,screen_width ,screen_height,offset):
        super().__init__()
        self.screen_width =screen_width
        self.screen_height = screen_height
        self.offset =offset
        image = pygame.image.load(path_load("Graphics/space_ship.png"))
        self.image =pygame.transform.scale(image,(50,40))
        self.rect = self.image.get_rect(midbottom = ((self.screen_width+self.offset)/2,self.screen_height))
        self.speed =5
        self.laser_group = pygame.sprite.Group()
        self.laserready =True
        self.laserTime =0
        self.delay = 300
        self.laser_sound =pygame.mixer.Sound(path_load("Sounds/laser.ogg"))



    def Keys(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed
        if Keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if Keys[pygame.K_SPACE] and self.laserready:
            self.laserready =False
            self.laser_sound.play()
            laser =Laser(self.rect.center , 5, self.screen_height)
            self.laser_group.add(laser)
            self.laserTime = pygame.time.get_ticks()

    def movment_spce(self):
        if self.rect.right > self.screen_width:
            self.rect.right =self.screen_width
        if self.rect.left < self.offset:
            self.rect.left = self.offset


    def laser_fire(self):
        if not self.laserready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laserTime >= self.delay:
                self.laserready =True

    def update(self):
        self.Keys()
        self.movment_spce()
        self.laser_group.update()
        self.laser_fire()

    def reset(self):
        self.rect =self.image.get_rect(midbottom =((self.screen_width+self.offset)/2 ,self.screen_height))
        self.laser_group.empty()