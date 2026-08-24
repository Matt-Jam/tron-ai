from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import ALLDIRECTIONS, validTurn


class ScaredBot(Rider):
    """Chooses the direction furthest from a wall every 10 frames
    """

    def update_dir(self, game_state) -> bool:
        if (game_state.frame % 5 != 0):
            return False

        attempt = self.direction
        d = -1
        for possible in ALLDIRECTIONS:
            if validTurn(self.direction, possible) or possible == self.direction:
                if r := self._send_ray(game_state, possible):
                    if r[1] > d:
                        attempt = possible
                        d = r[1]

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
