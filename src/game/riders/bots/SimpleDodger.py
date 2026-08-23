import random
from ..Rider import Rider
from ..util import HORIZONTAL, VERTICAL, validTurn, moveInDirection


class SimpleDodger(Rider):
    """If there is a wall ahead, chooses a random direction to avoid it
    """

    def random_valid_change(self):
        if self.direction in HORIZONTAL:
            return random.choice(VERTICAL)
        
        return random.choice(HORIZONTAL)

    def update_dir(self, game_state) -> bool:
        curr_pos = self.pos.copy()
        attempt = self.direction

        for _ in range(5):
            moveInDirection(curr_pos,self.direction,1)
            if (self._collide(game_state,curr_pos)):
                attempt = self.random_valid_change()

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
    
