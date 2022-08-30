import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ssGame):
        super().__init__()
        self.screen = ssGame.screen
        self.settings = ssGame.settings
        self.colour = self.settings.bulletColour

        self.rect = pygame.Rect(20, 20, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rect.midright = ssGame.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        self.x += self.settings.bulletSpeed
        self.rect.x = self.x

    def drawBullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
