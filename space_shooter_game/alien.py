import pygame ,random

class Alien(pygame.sprite.Sprite):
    def __init__(self ,type ,x ,y):
        super().__init__()
        self.type = type
        self.x =x
        self.y =y
        path =f"Graphics/alien_{type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self ,direction):
        # direction is a brameter for move
        self.rect.x += direction

class Mystery_ship(pygame.sprite.Sprite):
    def __init__(self,screen_width,offset):
        super().__init__()
        self.image = pygame.image.load("Graphics/mystery.png")
        self.speed = 3
        self.screen_width = screen_width
        self.offset =offset
        x= random.choice([self.offset/2 ,self.screen_width+self.offset-self.image.get_width()])
        self.rect = self.image.get_rect(topleft =(x ,80))

        if x ==self.offset/2:
            self.speed = 3
        else:
            self.speed = -3
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width+self.offset:
            self.kill()
        if self.rect.left < self.offset/2:
            self.kill()



