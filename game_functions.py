import sys
import pygame


def check_keydown_events(event, ship):
    """Response to keypresess."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Response to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():

        # checks for exit
        if event.type == pygame.QUIT:
            sys.exit()

        # checks for keydown left & right
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        # checks for keyup left & right
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()