import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object at ship's current position."""
        super().__init__()  # python3 way of inheritance
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        slef.rect = pygame.Rect(0, 0, ai_settings.bullet_settings,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullets position as a decimal value.
        slef.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def updat(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect positon
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, slef.rect)
