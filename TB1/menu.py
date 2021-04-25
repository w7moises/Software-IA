import sys, pygame
from pygame.locals import *
import os
# Game Initialization
import game
import BotVsBot as bot
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load("fondo.jpg")


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "Retro.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="bot"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        game.main()
                    if selected=="bot":
                        screen.fill(black)
                        bot.main()


        # Main Menu UI
        screen.blit(background_image,(0,0))
        title=text_format("Laberinto  /  A* algoritm", font, 90, yellow)
        if selected=="start":
            text_start= text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)

        if selected=="bot":
            text_bot = text_format("BOT", font, 75, white)
        else:
            text_bot = text_format("BOT", font, 75, black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        bot_rect=text_bot.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 100))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2),500))
        screen.blit(text_bot, (screen_width/2 - (bot_rect[2]/2), 560))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Menu")

main_menu()
pygame.quit()