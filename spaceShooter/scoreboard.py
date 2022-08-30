import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, aiGame):
        """Initialize scoreboard attributes."""
        self.aiGame = aiGame
        self.screen = aiGame.screen
        self.screenRect = self.screen.get_rect()
        self.settings = aiGame.settings
        self.stats = aiGame.stats
        self.font = pygame.font.SysFont(None, 48)
        self.textColour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.createScore()
        self.createHighScore()
        self.createLevel()
        self.prepareShips()

    def createScore(self):
        """Turn the score into a rendered image."""
        roundedScore = round(self.stats.score, -1)
        scoreString = "{:,}".format(roundedScore)
        self.scoreImage = self.font.render(scoreString, True, self.textColour, self.settings.bgColour)
        # Display the score at the top right of the screen.
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def showScore(self):
        """Draw score to the screen."""
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)

    def createHighScore(self):
        """Turn the high score into a rendered image."""
        highScore = round(self.stats.highScore, -1)
        highScoreString = "{:,}".format(highScore)
        self.highScoreImage = self.font.render(highScoreString, True,
        self.textColour, self.settings.bgColour)

        # Center the high score at the top of the screen.
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top

    def checkHighScore(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.highScore:
            self.stats.highScore = self.stats.score
            self.createHighScore()

    def createLevel(self):
        """Turn the level into a rendered image."""
        levelString = str(self.stats.level)
        self.levelImage = self.font.render(levelString, True,self.textColour, self.settings.bgColour)
        # Position the level below the score.
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10

    def prepareShips(self):
        """Show how many ships are left."""
        self.ships = Group()
        for shipNumber in range(self.stats.numOfShipsLeft):
            ship = Ship(self.aiGame)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

