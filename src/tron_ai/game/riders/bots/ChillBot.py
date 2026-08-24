from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import ALLDIRECTIONS, validTurn


class ChillBot(Rider):
    """Won't dodge until 5 away from a wall, at which point picks
        the direction a wall is furthest from
    """

    def update_dir(self, game_state) -> bool:
        if not self._send_ray(game_state, self.direction, 5):
            return False

        attempt = self.direction
        d = -1
        for possible in ALLDIRECTIONS:
            if validTurn(self.direction, possible):
                if r := self._send_ray(game_state, possible):
                    if r[1] > d:
                        attempt = possible
                        d = r[1]

        if validTurn(self.direction, attempt):
            self.direction = attempt
            return True
        return False
