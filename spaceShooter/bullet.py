import pygame


class Bullet(pygame.sprite.Sprite): # Inherits from Sprite class
    """A class to manage bullets fired from the ship"""
    def __init__(self, aiGame):
        super().__init__() # Inherit properly from Sprite
        self.screen = aiGame.screen
        self.settings = aiGame.settings
        self.colour = self.settings.bulletColour
        self.rect = pygame.Rect(0, 0, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rect.midtop = aiGame.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bulletSpeed
        self.rect.y = self.y

    def drawBullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
