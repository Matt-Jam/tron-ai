"""Code to drive the game screen, where two riders battle
"""

import pygame
from dataclasses import dataclass
from typing import Sequence

from .riders.bots.RandoBot import RandoBot
from .riders.bots.SimpleDodger import SimpleDodger
from .riders.Rider import Rider
from .riders.util import Directions

@dataclass
class GameState:
    keys: Sequence[bool]
    p1: Rider
    p2: Rider
    frame: int
    winner = -1

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.p1 = SimpleDodger(pygame.Vector2(100,320),Directions.DOWN,1)
        self.p2 = RandoBot(pygame.Vector2(400,400),Directions.LEFT,2)
        # self.p2 = SimpleDodger(pygame.Vector2(400,400),Directions.LEFT,2)
        self.frame = 0
        self.game_state = GameState([],self.p1,self.p2,self.frame)


    def _draw_rider(self,rider: Rider):
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

        return self.handle_lose(p1_safe,p2_safe)



