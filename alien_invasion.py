import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf


def run_game():
    # initialize game
    pygame.init()
    # settings obj
    ai_settings = Settings()
    # make a screen
    screen = pygame.display.set_mode((
        ai_settings.window_width, ai_settings.window_height))
    pygame.display.set_caption("Alien Invasion Personal Version")

    # create a ship
    ship = Ship(screen)
    # make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game
    while True:
        gf.check_event(screen, ai_settings, ship, bullets)
        # ship movement (x,y)
        ship.update()
        # moving bullets up (y)
        bullets.update()
        # update screen
        gf.update_screen(screen, ai_settings, ship, bullets)
        # display game
        pygame.display.flip()


run_game()
