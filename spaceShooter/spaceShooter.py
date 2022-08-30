import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gameStats import gameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """A class to manage game assets and behaviour."""
    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        self.stats = gameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # self.bgColour = self.settings.bgColour # Light grey
        self.background = self.settings.background
        pygame.display.set_caption(self.settings.titleBar)
        self.playButton = Button(self, "Start")

    def runGame(self):
        """Start main loop for game"""
        self._createFleet()
        while True:
            self._checkEvents()
            self.screen.blit(self.background.image, self.background.rect)
            if self.stats.gameActive:
                self.ship.update()
                self._updateBullets()
                self._updateAliens()
            self._updateScreen()

    def _createFleet(self):
        """Create fleet of aliens."""
        alien = Alien(self)  # Alien instance so we can attain alienWidth
        alienWidth, alienHeight = alien.rect.size  # get height and width in tuple
        availableSpaceX = self.settings.screenWidth - (2 * alienWidth)
        numberOfAliensX = availableSpaceX // (2 * alienWidth)  # Calculate aliens that can fit on one row
        shipHeight = self.ship.rect.height
        availableSpaceY = (self.settings.screenHeight - (3 * alienHeight) - shipHeight)
        numberOfRows = availableSpaceY // (3 * alienHeight)
        for rowNumber in range(numberOfRows):
            for alienNumber in range(numberOfAliensX):
                self._createAlien(alienNumber, rowNumber)

    def _checkEvents(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checkKeyDownEvents(event)
            elif event.type == pygame.KEYUP:
                self._checkKeyUpEvents(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._checkPlayButton(mouse_pos)

    def _checkPlayButton(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        buttonClicked = self.playButton.rect.collidepoint(mouse_pos)
        if buttonClicked and not self.stats.gameActive:
            self.settings.initializeDynamicSettings()
            self.stats.resetStats()
            self.stats.gameActive = True
            self.sb.createScore()
            self.sb.createLevel()
            self.sb.prepareShips()
            self.aliens.empty()
            self.bullets.empty()
            self._createFleet()
            self.ship.centreShip()
            pygame.mouse.set_visible(False)

    def _checkKeyDownEvents(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fireBullet()

    def _checkKeyUpEvents(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        if event.key == pygame.K_LEFT:
            self.ship.movingLeft = False

    def _fireBullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.maxBullets:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)

    def _updateBullets(self):
        """Update position of bullets and remove old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._checkBulletAlienCollisions()

    def _checkBulletAlienCollisions(self):
        """Respond to bullet alien collisions"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alienPoints * len(aliens)
            self.sb.createScore()
            self.sb.checkHighScore()
        if not self.aliens: # if all aliens killed
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._createFleet()
            self.settings.increaseSpeed()
            # Increase level.
            self.stats.level += 1
            self.sb.createLevel()

    def _updateAliens(self):
        """Check if fleet is at edge and update the positions of all aliens in the fleet."""
        self._checkFleetEdges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._shipHit()
        self._checkAliensHitBottom()

    def _shipHit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.numOfShipsLeft > 0:
            self.stats.numOfShipsLeft -= 1
            self.sb.prepareShips()
            self.aliens.empty()
            self.bullets.empty()
            self._createFleet()
            self.ship.centreShip()
            sleep(0.5) # pause game for 0.5 seconds
        else:
            self.stats.gameActive = False
            pygame.mouse.set_visible(True)

    def _checkAliensHitBottom(self):
        """Check if aliens have reached the bottom of the screen."""
        screenRect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screenRect.bottom:
                self._shipHit() # Same outcome as ship being hit.
                break

    def _updateScreen(self):
        """Update images on the screen and flip to the new screen."""
        # self.screen.fill(self.settings.bgColour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        self.aliens.draw(self.screen)
        self.sb.showScore()
        if not self.stats.gameActive:
            self.playButton.drawButton()
        pygame.display.flip()

    def _createAlien(self, alienNumber, rowNumber):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alienWidth, alienHeight = alien.rect.size
        alien.x = alienWidth + 2 * alienWidth * alienNumber
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
        self.aliens.add(alien)

    def _checkFleetEdges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.checkEdges():
                self._changeFleetDirection()
                break

    def _changeFleetDirection(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleetDropSpeed
        self.settings.fleetDirection *= -1


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()
