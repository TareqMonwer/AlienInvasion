import sys
import pygame

from bullet import Bullet


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_f:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def check_event(screen, ai_settings, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(screen, ai_settings, ship, bullets):
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
