import unittest
from unittest.mock import patch, Mock
import pygame
from alien_invasion import AlienInvasion


class TestAlienInvasion(unittest.TestCase):

    def setUp(self):
        self.ai = AlienInvasion()
        self.ai.initialize_game()

    def tearDown(self):
        pygame.quit()

    def test_check_keydown_events_right_key_moves_ship_right(self):
        event = Mock()
        event.key = pygame.K_RIGHT

        self.ai._check_keydown_events(event)

        self.assertTrue(self.ai.ship.moving_right)
        self.assertFalse(self.ai.ship.moving_left)

    def test_fire_bullet_adds_bullet_to_group(self):
        initial_bullet_count = len(self.ai.bullets)

        self.ai._fire_bullet()

        self.assertEqual(len(self.ai.bullets), initial_bullet_count + 1)


if __name__ == '__main__':
    unittest.main()
