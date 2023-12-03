import pygame
from pygame.locals import *
import pygame_menu
from PongGame import PongGame, WIDTH, HEIGHT

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))

game = PongGame()

def set_game_mode(pair, players):
    game.num_players = players

def start_the_game():
    menu.disable()
    game.run()
    menu.enable()

menu = pygame_menu.Menu('Pong', WIDTH, HEIGHT,
                       theme=pygame_menu.themes.THEME_GREEN)

menu.add.selector('', [('1 Player', 1), ('2 Players', 2)], onchange=set_game_mode)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


menu.mainloop(surface)
