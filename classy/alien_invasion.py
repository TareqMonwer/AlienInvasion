import sys

import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()

        # Create window with title.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Classy Alien Invasion")

        # Set background color.
        self.bg_color = (250, 250, 250)  # a lightgray color.

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard input and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pas through loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()
