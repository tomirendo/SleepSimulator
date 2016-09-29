from math import pi, sqrt, sin, cos
from random import random, randint
CREATURE_RADIUS = 15

class Location:
    def __init__(self, *args):
        if len(args) == 2:
            self.x, self.y = args
        else:
            self.x, self.y = args[0]
    def __add__(self, second):
        if not isinstance(second, Location):
            second = Location(second)
        return Location(self.x + second.x, self.y + second.y)
    def __sub__(self,second):
        if not isinstance(second, Location):
            second = Location(second)
        return Location(self.x - second.x, self.y - second.y)
    def distance(self, second):
        return sqrt(sum([i*i for i in list(self - second)] ))
    def __iter__(self):
        return iter([self.x, self.y])
    def __repr__(self):
        return repr(list(self))

class Move:
    def __init__(self, direction, speed = 1):
        self.direction = direction % (2*pi)
        self.speed = speed
    def step(self):
        return Location([cos(self.direction)*self.speed, 
            sin(self.direction)*self.speed])

class Creature:
    def __init__(self, color = None):
        self.next_move = Move(random() * 2 * pi ) 
        if color is None:
            self.color = [randint(0,255) for _ in range(3)]
        else :
            self.color = color
        self.location = Location([0,0])
        self.radius = CREATURE_RADIUS
        self.foods_eaten = []

    def move(self):
        self.location = self.location + self.next_move.step()

    def move_back(self):
        self.location = self.location - self.next_move.step()
