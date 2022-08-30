class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""

        # Screen Settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColour = (230, 230, 230)  # Light grey
        self.titleBar = "Sideways Shooter"

        # Ship Settings
        self.shipSpeed = 1.5

        # Bullet settings
        self.bulletSpeed = 2.0
        self.bulletWidth = 15 # Pixels
        self.bulletHeight = 3 # Pixels
        self.bulletColour = (60, 60, 60)
        self.maxBullets = 3