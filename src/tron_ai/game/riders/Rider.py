from abc import ABC, abstractmethod
from pygame import Vector2

from tron_ai.game.riders.util import Directions, moveInDirection, collide
from tron_ai.game.riders.Track import Track
from tron_ai.config import config

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

    def iterate_pos(self, game_state):

        moveInDirection(self.pos, self.direction, SPEED)

        if collide(game_state, self.pos):
            return False

        self.track.addPoint(self.pos)

        return True

    def draw_track(self, screen):
        self.track.draw(screen)

    def get_opponent(self, game_state) -> 'Rider':
        if self.player == 1:
            return game_state.p2
        return game_state.p1

    def _send_ray(self, game_state, dir: Directions, lim=config.screen_size):
        base = self.pos.copy()
        for i in range(lim):
            moveInDirection(base, dir, SPEED)
            if collide(game_state, base):
                return (True, i, base)
        return False

    @abstractmethod
    def update_dir(self, game_state) -> bool:
        pass
