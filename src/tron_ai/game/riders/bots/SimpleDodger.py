import random
from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import HORIZONTAL, VERTICAL, validTurn


class SimpleDodger(Rider):
    """If there is a wall ahead, chooses a random direction to avoid it
    """

    def random_valid_change(self):
        if self.direction in HORIZONTAL:
            return random.choice(VERTICAL)
        return random.choice(HORIZONTAL)

    def update_dir(self, game_state) -> bool:
        attempt = self.direction

        if self._send_ray(game_state, self.direction, 5):
            attempt = self.random_valid_change()

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
