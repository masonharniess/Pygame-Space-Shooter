import pygame.font


class Button:
    def __init__(self, aiGame, message):
        """Initialise button attributes."""
        self.screen = aiGame.screen
        self.screenRect = self.screen.get_rect()
        # Dimensions & properties of button.
        self.width, self.height = 200, 50
        self.buttonColour = (0, 255, 0)
        self.textColour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Build button rect object and centre it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        self._createMessage(message)

    def _createMessage(self, message):
        """Create rendered image from message and centre text on the button."""
        self.messageImage = self.font.render(message, True, self.textColour, self.buttonColour)
        self.messageImageRect = self.messageImage.get_rect()
        self.messageImageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColour, self.rect)
        self.screen.blit(self.messageImage, self.messageImageRect)