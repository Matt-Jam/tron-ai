import random

from pygame import Vector2
from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import HORIZONTAL, VERTICAL, Directions, validTurn, getDirectionFromVector


class AgroSimpleDodger(Rider):
    """Aim for the opponent unless there is a wall, at which point dodge randomly
    """

    def __init__(self, pos: Vector2, direction: Directions, player: int):
        super().__init__(pos, direction, player)
        self.cooldown = 0

    def random_valid_change(self):
        if self.direction in HORIZONTAL:
            return random.choice(VERTICAL)

        return random.choice(HORIZONTAL)

    def update_dir(self, game_state) -> bool:
        curr_pos = self.pos.copy()
        attempt = self.direction

        if self.cooldown == 0:
            opponent = self.get_opponent(game_state)
            attempt = getDirectionFromVector(opponent.pos - curr_pos)
        else:
            self.cooldown -= 1

        if self._send_ray(game_state, attempt, 10):
            attempt = self.random_valid_change()
            self.cooldown = 100

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
