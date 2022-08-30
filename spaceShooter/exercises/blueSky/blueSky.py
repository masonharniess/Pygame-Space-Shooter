# 12-1. Blue Sky: Make a Pygame window with a blue background.

import sys
import pygame

from settings import Settings


class BlueSky:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        self.bgColour = self.settings.bgColour

        pygame.display.set_caption(self.settings.titleBar)

    def runGame(self):
        while True:
            self._checkEvents()
            self._updateScreen()

    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _updateScreen(self):
        self.screen.fill(self.settings.bgColour)
        pygame.display.flip()


bs = BlueSky()
bs.runGame()