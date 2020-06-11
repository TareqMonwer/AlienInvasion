import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        # Initialize settings for applying game settings.
        self.settings = Settings()

        # Create window with title.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Classy Alien Invasion")

        # Initialize the ship
        self.ship = Ship(self)   # pass self as the ai_game argument of Ship.

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard input and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        # Redraw the screen during each pas through loop.
        self.screen.fill(self.settings.bg_color)
        # Draw the ship on screen.
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()
