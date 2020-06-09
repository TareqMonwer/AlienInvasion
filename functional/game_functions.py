import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """Check if any aliens have reached teh bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, score_board, ship, aliens, bullets)
            break


def check_bullet_alien_collisions(ai_settings, screen, stats, score_board, ship, aliens, bullets):
    """Respond to bullet alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Update score on alien shoot.
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()
        check_high_score(stats, score_board)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        start_new_level(ai_settings, screen, stats, score_board, ship, bullets, aliens)


def check_events(ai_settings, screen, score_board, ship, bullets, stats, play_button, aliens):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        # checks for exit
        if event.type == pygame.QUIT:
            # store the high score in a file
            with open('high_score.txt', 'w') as f:
                high_score = str(stats.high_score)
                f.write(high_score)
            sys.exit()

        # Check for play button click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score_board, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)

        # checks for keydown left & right
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens)

        # checks for keyup left & right
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_high_score(stats, score_board):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens):
    """Response to keypresess."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # store the high score in a file
        with open('high_score.txt', 'w') as f:
            high_score = str(stats.high_score)
            f.write(high_score)
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        play_game(ai_settings, stats, aliens, bullets, screen, ship)


def check_keyup_events(event, ship):
    """Response to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Starts a new game when the player clicks play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        play_game(ai_settings, stats, aliens, bullets, screen, ship, score_board)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_of_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        # Create a row of aliens.
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if user has not reached bullet limit."""
    # Create a new bullet and add to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    # Spacing between each alien is equal to one alien width.
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_of_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def play_game(ai_settings, stats, aliens, bullets, screen, ship, score_board):
    """Starts the game."""
    # Reset the game settings.
    ai_settings.initialize_dynamic_settings()
    # Hide mouse cursor.
    pygame.mouse.set_visible(False)
    # Reset game stats
    stats.reset_stats()
    stats.game_active = True
    # Reset the scoreboard images.
    score_board.prep_score()
    score_board.prep_high_score()
    score_board.prep_level()
    score_board.prep_ships()
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    # Create a new fleet and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def ship_hit(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1
        # Update scoreboard.
        score_board.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause.
        sleep(1)
    else:
        stats.game_active = False
        # If game is not active, show cursor to click
        pygame.mouse.set_visible(True)


def start_new_level(ai_settings, screen, stats, score_board, ship, bullets, aliens):
    """Clear old bullets, speed-up, level update and create new fleet."""
    bullets.empty()
    ai_settings.increase_speed()

    # Increase level.
    stats.level += 1
    score_board.prep_level()
    # create new fleet
    create_fleet(ai_settings, screen, ship, aliens)


def update_screen(ai_settings, stats, score_board, screen, aliens, ship, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw the scoreboard.
    score_board.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, score_board, ship, bullets, aliens):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    check_bullet_alien_collisions(ai_settings, screen, stats, score_board, ship, aliens, bullets)


def update_aliens(ai_settings, stats, screen, score_board, aliens, ship, bullets):
    """
    Check if the fleet is at an edge;
    and then, update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, score_board, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, score_board, ship, aliens, bullets)