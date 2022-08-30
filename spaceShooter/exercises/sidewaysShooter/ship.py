import pygame


class Ship:
    """A class to manage ship assets."""
    
    def __init__(self, ssGame):
        """Initialise the ship and set its starting position."""
        self.screen = ssGame.screen

        self.settings = ssGame.settings
        self.screenRect = ssGame.screen.get_rect()
        self.filepath = 'images/spaceship.png'
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.centerx = 30
        self.rect.centery = 400
        self.y = float(self.rect.y)
        self.movingDown = False
        self.movingUp = False

    def update(self):
        """Update ship's position based on the movement flag."""
        if self.movingDown and self.rect.bottom < self.screenRect.bottom - 5:
            self.y += self.settings.shipSpeed
        if self.movingUp and self.rect.top > self.screenRect.top + 5:
            self.y -= self.settings.shipSpeed
        self.rect.y = self.y


    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)