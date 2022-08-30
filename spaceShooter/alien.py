import pygame


class Alien(pygame.sprite.Sprite):
    """A class to manage singular alien assets."""
    def __init__(self, aiGame):
        """Initialise the alien and set its starting position."""
        super().__init__()
        self.screen = aiGame.screen
        self.settings = aiGame.settings
        self.filepath = 'images/ufo.png'
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (70, 50)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def checkEdges(self):
        """Return True if alien is at edge of screen."""
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alienSpeed * self.settings.fleetDirection
        self.rect.x = self.x
