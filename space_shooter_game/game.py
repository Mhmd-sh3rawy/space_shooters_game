import  pygame ,random
from spaceship import Spaceship
from alien import Alien
from laser import Laser
from alien import Mystery_ship
from loadfucntions import *

class Game:
    def __init__(self, screen_width , screen_height, offset):
        self.screen_width = screen_width
        self.screen_height =screen_height
        # all parameters
        self.offset = offset
        self.alien_direction = 1
        self.lives = 3
        self.run =True
        self.score =0
        self.high_score =0
        self.get_high_score()
        self.load_lastscore()

        # add all opjects  to be simple
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width ,self.screen_height ,self.offset))
        self.aliens_group =pygame.sprite.Group()
        self.creat_aliens()
        self.alien_laser_group = pygame.sprite.Group()
        self.mystery_ship_group =pygame.sprite.GroupSingle()
        # add music
        self.music =pygame.mixer.music.load(path_load("Sounds/music.ogg"))
        pygame.mixer.music.play(-1)
        self.explotion = pygame.mixer.Sound(path_load("Sounds/explosion.ogg"))



    def creat_aliens(self):
        for raw in range(5):
            for column in range(12):
                x =75+column*60
                y =110+raw*60
                if raw == 0:
                    alien_type = 3
                elif raw in(1,2):
                    alien_type =2
                else :
                    alien_type=1
                alien =Alien(alien_type ,x+self.offset/2 ,y )
                self.aliens_group.add(alien)

    def move_aliens(self):
        self.aliens_group.update(self.alien_direction)
        # get sprite of alien group
        alien_sprite = self.aliens_group.sprites()
        for alien in alien_sprite:
            if alien.rect.right >= self.screen_width+self.offset/2:
                self.alien_direction =-1
                self.move_down()
            if alien.rect.left <=self.offset/2:
                self.alien_direction= 1
                self.move_down()
    def move_down(self):
        # if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y +=1

    def alien_laser(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite= Laser(random_alien.rect.center ,-5 ,self.screen_height)
            self.alien_laser_group.add(laser_sprite)

    def creat_mystery(self):
        self.mystery_ship_group.add(Mystery_ship(self.screen_width,self.offset))


    def check_collision(self):
        # in space ship
        if self.spaceship_group.sprite.laser_group:
            for laser_sprite in self.spaceship_group.sprite.laser_group:
               aliens_hit=  pygame.sprite.spritecollide(laser_sprite,self.aliens_group,True)
               if aliens_hit:
                   self.explotion.play()
               for alien in aliens_hit:
                   self.score += alien.type*100
                   self.get_high_score()
                   laser_sprite.kill()
               if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                   self.score +=500
                   self.explotion.play()
                   self.get_high_score()
                   laser_sprite.kill()
        # in alien laser
        if self.alien_laser_group:
            for laser_sprite in self.alien_laser_group:
                if pygame.sprite.spritecollide(laser_sprite ,self.spaceship_group,False):
                    laser_sprite.kill()
                    self.lives -=1
                    if self.lives ==0:
                        self.game_over()
        # in alien group
        if self.aliens_group:

            for alien in self.aliens_group:
                if pygame.sprite.spritecollide(alien ,self.spaceship_group,False):
                   self.game_over()

    def get_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt","w") as file :
                 file.write(str(self.high_score))

    def load_lastscore(self):
        try:
            with open("highscore.txt","r") as file:
                self.high_score =int(file.read())
        except FileNotFoundError:
            self.high_score =0

    def game_over(self):
        self.run =False

    def reset(self):
        self.run =True
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_laser_group.empty()
        self.creat_aliens()
        self.mystery_ship_group.empty()
        self.score =0








