class gameStats:
    """Track statistics for alien invasion."""

    def __init__(self, aiGame):
        """Initialise statistics."""
        self.settings = aiGame.settings
        self.resetStats()
        self.gameActive = False
        self.highScore = 0

    def resetStats(self):
        """Initialise statistics that can change during the game."""
        self.numOfShipsLeft = self.settings.shipLimit
        self.score = 0
        self.level = 1
