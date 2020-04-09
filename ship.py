import pygame


class Ship:

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # load the shijp and get its rect.
        self.image = pygame.image.load("images/rocket.png")
        self.rect = self.image.get_rect()  # rect is the image itself
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # ship movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Update the ship based on the movement flag."""
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= 1
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
