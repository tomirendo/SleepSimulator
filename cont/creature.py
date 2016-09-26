from math import pi
from random import random, randint

class Location:
    def __init__(self, *args):
        if len(args) == 2:
            self.x, self.y = args
        else:
            self.x, self.y = args[0]
    def __add__(self, seoncd):
        if not isinstance(Location, seoncd):
            second = Location(second)
        return Location(self.x + second.x, self.y + second.y)
    def __iter__(self):
        return iter([self.x, self.y])

class Move:
    def __init__(self, direction, speed = 1):
        self.direction = direction % (2*pi)
        self.speed = speed

class Creature:
    def __init__(self, color = None):
        self.next_move = Move(random() * 2 * pi ) 
        if color is None
            self.color = [randint(0,255) for _ in range(3)]
        else :
            self.color = color
        self.location([0,0])

    def move(self):
        return self.next_move
