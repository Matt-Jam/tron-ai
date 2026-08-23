from typing import Sequence
import pygame
from tron_ai.app.resources import get_main_font


class GameOver:

    def __init__(self, screen):
        self.screen = screen
        self.messages = ["Player 1 wins", "Player 2 wins", "Player 3 wins"]
        self.state = 0

    def draw(self):
        self.screen.fill("purple")
        message = get_main_font().render(
            self.messages[self.state], True, (0, 0, 0))
        self.screen.blit(message, (100, 100))

    def step(self, keys: Sequence[bool]):
        self.draw()

        if keys[pygame.K_SPACE]:  # pylint: disable=no-member
            return False

        return True
