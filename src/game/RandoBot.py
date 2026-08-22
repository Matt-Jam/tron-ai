import random
from .Rider import Rider
from .util import ALLDIRECTIONS, validTurn


class RandoBot(Rider):
    def update_dir(self, game_state) -> bool:
        if (game_state.frame % 10 != 0):
            return False
        attempt = random.choice(ALLDIRECTIONS)

        if validTurn(self.direction,attempt):
            self.direction = attempt
            return True
        return False
