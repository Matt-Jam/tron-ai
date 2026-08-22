from abc import ABC, abstractmethod
from pygame import Vector2, draw

from .util import Directions, copyVec2, transferVec2
from .Track import Track, Line

SPEED = 1


class Rider(ABC):
    def __init__(self,pos: Vector2, direction: Directions):
        self.pos = pos
        self.trackPoints = [copyVec2(pos)]
        self.direction = direction
        self.trackStore = Track()
        self.line = Line(pos,direction)
        self.trackStore.addLine(self.line)

    def move(self,game_state):

        if (self.update_dir(game_state)):
            self.line.cut()
            self.line = Line(self.pos,self.direction)
            self.trackStore.addLine(self.line)
            self.trackPoints.append(copyVec2(self.pos))

        return self.iterate_pos(game_state)

    def _collide(self, game_state,attempt):
        if attempt.x <= 0 or attempt.x >=600:
            return True
        if attempt.y <= 0 or attempt.y >= 600:
            return True
        
        if game_state.p1.trackStore.collide(attempt):
            return True

        return game_state.p2.trackStore.collide(attempt)
        
    def iterate_pos(self, game_state):

        attempt = copyVec2(self.pos)

        match self.direction:
            case Directions.UP:
                attempt.y -= SPEED
            case Directions.DOWN:
                attempt.y += SPEED
            case Directions.LEFT:
                attempt.x -= SPEED
            case _:
                attempt.x += SPEED

        if(self._collide(game_state,attempt)):
            return False

        transferVec2(attempt,self.pos)
        return True

    def draw_track(self,screen):
        draw.lines(screen,"black",False,self.trackPoints+[self.pos],1)

    @abstractmethod
    def update_dir(self,game_state) -> bool:
        pass



    