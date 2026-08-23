import pygame
from tron_ai.game.riders.util import LineType, Directions, getLineTypeFromDir


class Line:
    def __init__(self, pos: pygame.Vector2, direction: Directions):
        self.start = pos.copy()
        self.end = pos
        self.type = getLineTypeFromDir(direction)

    def cut(self):
        self.end = self.end.copy()

    def isbetween(self, p: float, a: float, b: float):
        return min(a, b) <= p <= max(a, b)

    def collide(self, pos):
        match self.type:
            case LineType.HORIZONTAL:
                return self.isbetween(pos.x, self.start.x, self.end.x)
            case LineType.VERTICAL:
                return self.isbetween(pos.y, self.start.y, self.end.y)


class Track:
    def __init__(self):
        self.vertical: list[list[Line]] = [[] for _ in range(600)]
        self.horizontal: list[list[Line]] = [[] for _ in range(600)]

    def addLine(self, line: Line):
        if line.type == LineType.HORIZONTAL:
            self.horizontal[int(line.start.y)].append(line)
        else:
            self.vertical[int(line.start.x)].append(line)

    def collide(self, pos: pygame.Vector2):
        for line in self.vertical[int(pos.x)]:
            if line.collide(pos):
                return line
        for line in self.horizontal[int(pos.y)]:
            if line.collide(pos):
                return line
        return False
