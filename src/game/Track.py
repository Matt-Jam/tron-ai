import pygame
from .util import LineType, Directions, getLineTypeFromDir, copyVec2

    
class Line:
    def __init__(self, pos:pygame.Vector2, direction: Directions):
        self.start = copyVec2(pos)
        self.end = pos
        self.type = getLineTypeFromDir(direction)

    def cut(self):
        self.end = copyVec2(self.end)

    def isbetween(self,p:float, a:float, b:float):
        return min(a,b) <= p <= max(a,b)
    
    def collide(self,pos):
        match self.type:
            case LineType.HORIZONTAL:
                return self.isbetween(pos.x,self.start.x,self.end.x)
            case LineType.VERTICAL:
                return self.isbetween(pos.y,self.start.y,self.end.y)

class Track:
    def __init__(self):
        self.db = 0
        self.dv = 0
        self.vertical: list[list[Line]] = [[] for _ in range(600)]
        self.horizontal: list[list[Line]] = [[] for _ in range(600)]

    def addLine(self,line: Line):
        if line.type == LineType.HORIZONTAL:
            self.horizontal[int(line.start.y)].append(line)
        else:
            self.vertical[int(line.start.x)].append(line)

    def collide(self, pos: pygame.Vector2):
        for l in self.vertical[int(pos.x)]:
            self.dv +=1
            if l.collide(pos):
                return l
        for l in self.horizontal[int(pos.y)]:
            self.db +=1
            if l.collide(pos):
                return l
        return False






