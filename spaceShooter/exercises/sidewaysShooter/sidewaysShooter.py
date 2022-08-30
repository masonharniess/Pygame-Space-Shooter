# 12-6. Sideways Shooter: Write a game that places a ship on the left side of the screen and allows
# the player to move the ship up and down. Make the ship fire a bullet that travels right across the
# screen when the player presses the space- bar. Make sure bullets are deleted once they disappear
# off the screen.

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class SidewaysShooter:
    """A class to manage game assets and behaviour."""
    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bgColour = self.settings.bgColour  # Light grey
        pygame.display.set_caption(self.settings.titleBar)

    def runGame(self):
        """Start main loop for game"""
        while True:
            self._checkEvents()
            self.ship.update()
            self._updateBullets()
            self._updateScreen()

    def _checkEvents(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checkKeyDownEvents(event)
            elif event.type == pygame.KEYUP:
                self._checkKeyUpEvents(event)

    def _checkKeyDownEvents(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.movingDown = True
        elif event.key == pygame.K_LEFT:
            self.ship.movingUp = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fireBullet()

    def _checkKeyUpEvents(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.movingDown = False
        if event.key == pygame.K_LEFT:
            self.ship.movingUp = False

    def _fireBullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.maxBullets:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)

    def _updateBullets(self):
        self.bullets.update()
        # Delete bullets off screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)

    def _updateScreen(self):
        """Update images2 on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bgColour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        pygame.display.flip()


if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.runGame()