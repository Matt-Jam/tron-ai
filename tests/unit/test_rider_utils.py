from pygame import Vector2
import pytest 
from tron_ai.game.riders.util import Directions, getLineTypeFromDir, LineType, transferVec2, validTurn, moveInDirection, getDirectionFromVector

@pytest.mark.parametrize("direction",[
    Directions.LEFT,
    Directions.RIGHT
])
def test_getLineTypeFromDir_H(direction):
    assert getLineTypeFromDir(direction) == LineType.HORIZONTAL


@pytest.mark.parametrize("direction",[
    Directions.UP,
    Directions.DOWN
])
def test_getLineTypeFromDir_V(direction):
    assert getLineTypeFromDir(direction) == LineType.VERTICAL

def test_transferVec2_val():
    v1 = Vector2(0,2)
    v2 = Vector2(3,4)
    transferVec2(v1,v2)
    assert v1 == v2 

def test_transferVec2_ref():
    v1 = Vector2(0,0)
    v2 = Vector2(0,0)
    transferVec2(v1,v2)
    assert not (v1 is v2) 

@pytest.mark.parametrize("old, new",[
    (Directions.RIGHT, Directions.UP),
    (Directions.UP, Directions.RIGHT),
    (Directions.LEFT,Directions.DOWN),
    (Directions.UP, Directions.LEFT)
])
def test_validTurn_T(old, new):
    assert validTurn(old,new)

@pytest.mark.parametrize("old, new",[
    (Directions.RIGHT, Directions.RIGHT),
    (Directions.UP, Directions.DOWN),
    (Directions.LEFT,Directions.RIGHT),
    (Directions.DOWN, Directions.UP)
])
def test_validTurn_F(old, new):
    assert not validTurn(old,new)

@pytest.mark.parametrize("pos, direction, speed, goal",[
    (Vector2(0,1),Directions.UP, 1, Vector2(0,0)),
    (Vector2(1,1),Directions.DOWN, -1, Vector2(1,0)),
    (Vector2(3,-1),Directions.RIGHT, 3, Vector2(6,-1)),
    (Vector2(0,1),Directions.LEFT, 1, Vector2(-1,1)),
    (Vector2(0,1),Directions.UP, 0, Vector2(0,1)),
])
def test_moveInDirection(pos, direction, speed, goal):
    moveInDirection(pos, direction, speed)
    assert pos == goal

@pytest.mark.parametrize("vec, tar",[
    (Vector2(0,1),Directions.DOWN),
    (Vector2(1,0),Directions.RIGHT),
    (Vector2(0,-1),Directions.UP),
    (Vector2(-1,0),Directions.LEFT),
    (Vector2(2,1),Directions.RIGHT),
    (Vector2(-1,-2),Directions.UP),
    (Vector2(-1,-0.5),Directions.LEFT),

])
def test_getDirectionFromVector(vec, tar):
    assert getDirectionFromVector(vec) == tar

