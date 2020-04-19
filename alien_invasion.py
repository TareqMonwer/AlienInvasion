import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    score_board = ScoreBoard(ai_settings, screen, stats)

    # Make a ship, group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, score_board, ship, bullets, stats, play_button, aliens)

        if stats.game_active:
            # Ship move control
            ship.update()
            # Update bullets
            gf.update_bullets(ai_settings, screen, stats, score_board, ship, bullets, aliens)
            # Update alien positions
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)

        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, stats, score_board, screen, aliens, ship, bullets, play_button)


run_game()




























