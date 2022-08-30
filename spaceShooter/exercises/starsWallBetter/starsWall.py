# 13-2. Better Stars: You can make a more realistic star pattern by introducing randomness when you
# place each star. Recall that you can get a random num- ber like this:
#   from random import randint
#   random_number = randint(-10, 10)
# This code returns a random integer between −10 and 10. Using your code in Exercise 13-1, adjust each star’s
# position by a random amount

import sys
import pygame
from settings import Settings
from star import Star
from random import randint


class starsWall:
    """A class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        self.stars = pygame.sprite.Group()

        pygame.display.set_caption(self.settings.titleBar)
        self.background = self.settings.background

    def runGame(self):
        """Start main loop for game"""
        self._createStarLine()
        while True:
            self._checkEvents()
            self._updateScreen()
            self.screen.blit(self.background.image, self.background.rect)

    def _checkEvents(self):
        """Respond to key presses and mouse events"""

        # Event loop to watch for keyboard and mouse events
        # To access the events that pygame detects, pygame.event.get() function is used.
        # This function returns a list of events that have taken place since the last time this function was called.
        # Any keyboard or mouse events will cause this for loop to run.
        for event in pygame.event.get():
            # When user clicks game window's close button, pygame.QUIT is detected and sys.exit() is called
            if event.type == pygame.QUIT:
                sys.exit()

    def _updateScreen(self):
        """Update images2 on the screen and flip to the new screen"""
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _createStarLine(self):
        """Create lines of stars."""
        star = Star(self)  # Alien instance so we can attain alienWidth
        starWidth, starHeight = star.rect.size  # get height and width from size tuple
        availableSpaceX = self.settings.screenWidth - (2 * starWidth)
        numberOfStarsX = availableSpaceX // (2 * starWidth)  # Calculate aliens that can fit on one row
        availableSpaceY = (self.settings.screenHeight - (3 * starHeight) - 50)
        numberOfRows = availableSpaceY // (3 * starHeight)

        for rowNumber in range(numberOfRows):
            for starNumber in range(numberOfStarsX):
                self._createStar(starNumber, rowNumber)

    def _createStar(self, starNumber, rowNumber):
        """Create a star and place it in the row."""
        star = Star(self)
        starWidth, starHeight = star.rect.size
        star.x = starWidth + 2 * starWidth * starNumber
        star.rect.x = star.x + randint(-10, 10) # Add horizontal randomness
        star.rect.y = star.rect.height + 2 * star.rect.height * rowNumber + randint(-10, 10) # Add vertical randomness
        self.stars.add(star)


if __name__ == '__main__':
    # Make a game instance
    sw = starsWall()
    # Run the game
    sw.runGame()