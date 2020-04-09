import pygame


class Settings:
    def __init__(self):
        # Basic window/screen settings
        self.window_width = 1000
        self.window_height = 500
        self.bg_color = (111, 212, 255)

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 238, 69, 31
