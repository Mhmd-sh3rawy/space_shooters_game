import pygame, sys
from button import Button
from loadfucntions import *
pygame.init()

SCREEN = pygame.display.set_mode((910, 690))
pygame.display.set_caption("Menu")

BG = pygame.image.load(path_load("assets/img_230629_siwd_title_logo.webp"))
resizeBG = pygame.transform.scale(BG ,(900,550))

def get_font(size):
    return pygame.font.Font(path_load("assets/font.ttf"), size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        import main
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(resizeBG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.image.load(path_load("assets/Quit Rect.png")), pos=(245, 550),
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="yellow")
        QUIT_BUTTON = Button(image=pygame.image.load(path_load("assets/Quit Rect.png")), pos=(655, 550),
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="yellow")



        for button in [PLAY_BUTTON,  QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()