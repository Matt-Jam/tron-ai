"""Code to drive the game screen, where two riders battle
"""

import pygame
from dataclasses import dataclass
from typing import Sequence

from tron_ai.game.riders.bots.RandoBot import RandoBot
from tron_ai.game.riders.bots.SimpleDodger import SimpleDodger
from tron_ai.game.riders.bots.ScaredBot import ScaredBot
from tron_ai.game.riders.players.player import Player
from tron_ai.game.riders.bots.AgroSimpleDodger import AgroSimpleDodger
from tron_ai.game.riders.bots.ChillBot import ChillBot
from tron_ai.game.riders.Rider import Rider
from tron_ai.game.riders.util import Directions


@dataclass
class GameState:
    keys: Sequence[bool]
    p1: Rider
    p2: Rider
    frame: int
    winner = -1


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.p1 = ChillBot(pygame.Vector2(300, 250), Directions.LEFT, 1)
        self.p2 = ScaredBot(
            pygame.Vector2(200, 550), Directions.RIGHT, 2)
        self.frame = 0
        self.game_state = GameState([], self.p1, self.p2, self.frame)

    def _draw_rider(self, rider: Rider):
        rider.draw_track(self.screen)
        pygame.draw.circle(self.screen, "red", rider.pos, 5)

    def handle_lose(self, p1_safe: bool, p2_safe: bool):
        if p1_safe:
            if p2_safe:
                return True
            self.game_state.winner = 0
            return False

        if p2_safe:
            self.game_state.winner = 1
            return False

        self.game_state.winner = 2
        return False

    def draw(self):
        self.screen.fill("white")
        self._draw_rider(self.p1)
        self._draw_rider(self.p2)

    def step(self, keys: Sequence[bool]):
        self.game_state.keys = keys
        self.game_state.frame = self.frame

        p1_safe = self.p1.move(self.game_state)
        p2_safe = self.p2.move(self.game_state)

        self.draw()

        self.frame += 1

        return self.handle_lose(p1_safe, p2_safe)
