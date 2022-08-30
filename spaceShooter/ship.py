# Module to control most behaviours of the ship.
import pygame
from pygame.sprite import Sprite


# In Ship, everything is treated as a rectangle (rect), which is more efficient than using
# geometrically complex shapes.

class Ship(Sprite):
    """A class to manage ship assets."""

    # The __init__ method takes itself, and a reference to the current instance of AlienInvasion
    # This will give Ship access to all the game resources defined in AlienInvasion
    def __init__(self, aiGame):
        """Initialise the ship and set its starting position."""
        super().__init__()

        # Assign the screen to an attribute of Ship so we can access all methods in the class
        self.screen = aiGame.screen

        self.settings = aiGame.settings
        # Access screen's rect attribute using the get_rect() method and assign it to self.screenRect
        #This allows us to place ship in correct location of screen
        self.screenRect = aiGame.screen.get_rect()

        # Load ship image using pygame.image.load
        # This function returns a surface representing the ship, which is assigned to self.image
        self.filepath = 'images/spaceship.png'
        self.image = pygame.image.load(self.filepath)
        self.image = pygame.transform.scale(self.image, (50, 50))
        # Once image is loaded, call get_rect() to access ship surface's rect attribute so we can later
        # use it to place the ship
        self.rect = self.image.get_rect()

        # Start each new ship at bottom centre of screen
        self.rect.centerx = 600
        self.rect.centery = 765

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag – becomes true when player presses right arrow key
        self.movingRight = False
        self.movingLeft = False

    def update(self):
        """Update ship's position based on the movement flag."""
        if self.movingRight and self.rect.right < self.screenRect.right - 5:
            self.x += self.settings.shipSpeed
        # Use separate if blocks to avoid movingRight taking priority when both are pressed
        if self.movingLeft and self.rect.left > self.screenRect.left + 5:
            self.x -= self.settings.shipSpeed
        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def centreShip(self):
        """Centre the ship on the screen."""
        self.rect.midbottom = self.screenRect.midbottom
        self.x = float(self.rect.x)
