""" Provides a "Player" rider that allows users to control a rider
"""
import pygame
from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import Directions, validTurn


class Player(Rider):
    """Player driven rider, controlled by WASD
    """

    def update_dir(self, game_state) -> bool:
        keys = game_state.keys
        attempt = None

        if keys[pygame.K_w]:  # pylint: disable=no-member
            attempt = Directions.UP
        elif keys[pygame.K_s]:  # pylint: disable=no-member
            attempt = Directions.DOWN
        elif keys[pygame.K_a]:  # pylint: disable=no-member
            attempt = Directions.LEFT
        elif keys[pygame.K_d]:  # pylint: disable=no-member
            attempt = Directions.RIGHT
        else:
            return False

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
