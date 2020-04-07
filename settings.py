class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initializes the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
