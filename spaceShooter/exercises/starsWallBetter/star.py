import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to manage singular alien assets."""

    def __init__(self, swGame):
        super().__init__()
        self.screen = swGame.screen

        self.filepath = 'images/star.png'
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (50, 50)).convert()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)