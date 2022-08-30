from background import Background


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""

        # Screen Settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColour = (230, 230, 230)  # Light grey
        self.titleBar = "Space Shooter"
        self.background = Background('images/starsBackground.jpeg', [0, 0])

        # Ship Settings
        self.shipLimit = 3

        # Bullet settings
        self.bulletWidth = 3 # Pixels
        self.bulletHeight = 15 # Pixels
        self.bulletColour = (0, 203, 0)
        self.maxBullets = 3

        # Alien settings
        self.fleetDropSpeed = 2

        self.speedupScale = 1.1
        self.scoreScale = 1.5
        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        """Initialise changing values."""
        self.shipSpeed = 1.5
        self.bulletSpeed = 2.0
        self.alienSpeed = 0.3
        self.fleetDirection = 1  # 1 represents right, -1 represents left
        self.alienPoints = 50

    def increaseSpeed(self):
        """Increase speed settings."""
        self.shipSpeed *= self.speedupScale
        self.bulletSpeed *= self.speedupScale
        self.alienSpeed *= self.speedupScale
        self.alienPoints = int(self.alienPoints * self.scoreScale)
        print(self.alienPoints)