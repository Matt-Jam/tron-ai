from abc import ABC, abstractmethod
from pygame import Vector2, draw

from .util import Directions, transferVec2, moveInDirection
from .Track import Track, Line

SPEED = 1


class Rider(ABC):
    def __init__(self,pos: Vector2, direction: Directions, player: int):
        self.pos = pos
        self.trackPoints = [pos.copy()]
        self.direction = direction
        self.trackStore = Track()
        self.line = Line(pos,direction)
        self.trackStore.addLine(self.line)
        self.player = player

    def move(self,game_state):

        if (self.update_dir(game_state)):
            self.line.cut()
            self.line = Line(self.pos,self.direction)
            self.trackStore.addLine(self.line)
            self.trackPoints.append(self.pos.copy())

        return self.iterate_pos(game_state)

    def _collide(self, game_state, attempt: Vector2):
        if attempt.x <= 0 or attempt.x >=600:
            return True
        if attempt.y <= 0 or attempt.y >= 600:
            return True
        
        if game_state.p1.trackStore.collide(attempt):
            return True

        return game_state.p2.trackStore.collide(attempt)

    
    def iterate_pos(self, game_state):

        attempt = self.pos.copy()
        moveInDirection(attempt,self.direction,SPEED)

        if(self._collide(game_state,attempt)):
            return False

        transferVec2(attempt,self.pos)
        return True

    def draw_track(self,screen):
        draw.lines(screen,"black",False,self.trackPoints+[self.pos],1)

    def get_opponent(self,game_state) -> 'Rider':
        if self.player == 1:
            return game_state.p2
        return game_state.p1
    
    @abstractmethod
    def update_dir(self,game_state) -> bool:
        pass



    