from background import Background


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""

        # Screen Settings
        self.screenWidth = 1200
        self.screenHeight = 800
        #self.bgColour = (230, 230, 230)  # Light grey
        self.titleBar = "Stars Wall"
        self.background = Background('images2/starsBackground.jpeg', [0, 0])