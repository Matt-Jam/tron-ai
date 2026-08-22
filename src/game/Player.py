import pygame
from .Rider import Rider
from .util import Directions, validTurn

class Player(Rider):
    """Player driven rider, controlled by WASD
    """
    def update_dir(self, game_state) -> bool:
        keys = game_state.keys   
        attempt = None

        if keys[pygame.K_w]:
            attempt = Directions.UP
        elif keys[pygame.K_s]:
            attempt = Directions.DOWN
        elif keys[pygame.K_a]:
            attempt = Directions.LEFT
        elif keys[pygame.K_d]:
            attempt = Directions.RIGHT
        else:
            return False

        if (validTurn(self.direction,attempt)):
            self.direction = attempt
            return True
        
        return False
        
