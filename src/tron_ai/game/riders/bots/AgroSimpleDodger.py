import random
from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import HORIZONTAL, VERTICAL, validTurn, moveInDirection, getDirectionFromVector


class AgroSimpleDodger(Rider):
    """Aim for the opponent unless there is a wall, at which point dodge randomly
    """

    def random_valid_change(self):
        if self.direction in HORIZONTAL:
            return random.choice(VERTICAL)

        return random.choice(HORIZONTAL)

    def update_dir(self, game_state) -> bool:
        curr_pos = self.pos.copy()
        attempt = self.direction

        opponent = self.get_opponent(game_state)
        attempt = getDirectionFromVector(opponent.pos - curr_pos)

        for _ in range(5):
            moveInDirection(curr_pos, attempt, 1)
            if (self._collide(game_state, curr_pos)):
                attempt = self.random_valid_change()

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
