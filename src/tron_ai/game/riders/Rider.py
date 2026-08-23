from abc import ABC, abstractmethod
from pygame import Vector2

from tron_ai.game.riders.util import Directions, moveInDirection
from tron_ai.game.riders.Track import Track

SPEED = 1


class Rider(ABC):
    def __init__(self, pos: Vector2, direction: Directions, player: int):
        self.pos = pos
        self.direction = direction
        self.track = Track()
        self.player = player

    def move(self, game_state):
        self.update_dir(game_state)
        return self.iterate_pos(game_state)

    def _collide(self, game_state, pos):
        if pos.x <= 0 or pos.x >= 600:
            return True

        if pos.y <= 0 or pos.y >= 600:
            return True

        if game_state.p1.track.collide(pos):
            return True

        return game_state.p2.track.collide(pos)

    def iterate_pos(self, game_state):

        moveInDirection(self.pos, self.direction, SPEED)

        if self._collide(game_state, self.pos):
            return False

        self.track.addPoint(self.pos)

        return True

    def draw_track(self, screen):
        self.track.draw(screen)

    def get_opponent(self, game_state) -> 'Rider':
        if self.player == 1:
            return game_state.p2
        return game_state.p1

    @abstractmethod
    def update_dir(self, game_state) -> bool:
        pass
