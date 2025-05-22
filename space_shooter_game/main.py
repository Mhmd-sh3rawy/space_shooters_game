import pygame
import random
from game import Game
from loadfucntions import *
pygame.init()

yellow= (208,192,80)
red = (230, 79, 80)
font = pygame.font.Font(path_load("Font/monogram.ttf"),40)
font2 = pygame.font.Font(path_load("Font/monogram.ttf"),100)
levelsurface = font.render("LEVEL 01",False,yellow)
game_oversurface =font.render("GAME OVER",False ,yellow)
resetsurface = font.render("R :TO RESERT",False,yellow)
scoresurface =font.render("SCORE:" ,False,yellow)
high_scoreSurface =font.render("HIGH SCORE:" ,False,yellow)
playAGAINsurface = font.render("R :PLAY AGAIN",False,yellow)
game_winsurface =font2.render("YOU WIN",False ,yellow)

screenWidth = 860
screenHeight =590
OFFSET = 50
screen=pygame.display.set_mode((screenWidth+OFFSET ,screenHeight+2*OFFSET))
pygame.display.set_caption("SPACE INVADERS")
clock = pygame.time.Clock()

game =Game(screenWidth ,screenHeight,OFFSET)

shoot_laser =pygame.USEREVENT
pygame.time.set_timer(shoot_laser ,200)

mystery_ship = pygame.USEREVENT+1
pygame.time.set_timer(mystery_ship,(random.randint(4000,5000)))

def screen_draw():
    # drawing
    screen.fill((29,29,27))
    pygame.draw.rect(screen ,red  ,(10,10,890,670) ,2,0,0,0,0,0)
    pygame.draw.line(screen,red,(25,620),(885,620),3)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_laser_group.draw(screen)
    game.mystery_ship_group.draw(screen)


    # updating
    if game.run:
        screen.blit(levelsurface, (700, 630, 50, 50))
        screen.blit(scoresurface,(50,20,50,50))
        fromate_score = str(game.score).zfill(5)
        game_scoresurface = font.render(fromate_score, False, yellow)
        screen.blit(game_scoresurface,(50,50,50,50))
        screen.blit(high_scoreSurface,(700,20,50,50))
        fromate_highscore = str(game.high_score).zfill(5)
        game_highscoresurface = font.render(fromate_highscore, False, yellow)
        screen.blit(game_highscoresurface,(740,50,50,50))

        game.spaceship_group.update()
        game.move_aliens()
        game.alien_laser_group.update()
        game.mystery_ship_group.update()
        game.check_collision()
        game.victory()
    if game.run == 2 :
        screen.blit(game_winsurface ,(320 ,590/2))
        screen.blit(playAGAINsurface,(360,630,50,50))

    if game.run == 0:
        screen.blit(game_oversurface,(700,630, 50, 50))
        screen.blit(resetsurface,(360,630,50,50))
    x =60
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image,(x,630))
        x+=60

    pygame.display.update()

# game loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == shoot_laser and game.run:
            game.alien_laser()

        if event.type == mystery_ship and game.run ==1:
            game.creat_mystery()
            pygame.time.set_timer(mystery_ship,random.randint(4000,8000))

        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_r] and game.run == 0 :
            game.reset()
        if Keys[pygame.K_r] and game.run == 2 :
            game.reset()


    screen_draw()