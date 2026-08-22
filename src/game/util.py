from enum import Enum
from pygame import Vector2


class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

HORIZONTAL = [Directions.LEFT,Directions.RIGHT]
VERTICAL = [Directions.UP,Directions.DOWN]

ALLDIRECTIONS = VERTICAL + HORIZONTAL

class LineType(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


def getLineTypeFromDir(direction: Directions):
    if direction in HORIZONTAL:
        return LineType.HORIZONTAL
    return LineType.VERTICAL

def copyVec2(pos: Vector2):
    return Vector2(pos.x,pos.y)

def transferVec2(src: Vector2, tar: Vector2):
    tar.x = src.x 
    tar.y = src.y


def validTurn(old: Directions, new: Directions):
    if (old == new):
        return False
    if (old in HORIZONTAL) and (new in HORIZONTAL):
        return False
    if (old in VERTICAL) and (new in VERTICAL):
        return False

    return True
    