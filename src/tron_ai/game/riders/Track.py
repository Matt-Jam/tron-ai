from pygame import Vector2, Surface, SRCALPHA  # pylint: disable=no-name-in-module
import numpy as np
from tron_ai.config import config


class Track:
    def __init__(self):
        self.grid = np.zeros(
            (config.screen_size, config.screen_size), dtype=bool)
        self.surface = Surface(
            (config.screen_size, config.screen_size), SRCALPHA)
        self.surface.fill((0, 0, 0, 0))

    def addPoint(self, point: Vector2):
        self.grid[int(point.x)][int(point.y)] = True
        self.surface.set_at(point, (0, 0, 0, 255))

    def collide(self, pos: Vector2):
        return self.grid[int(pos.x)][int(pos.y)]

    def draw(self, target: Surface):
        target.blit(self.surface, (0, 0))
