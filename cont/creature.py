from math import pi, sqrt, sin, cos, acos, asin, atan
from random import random, randint
from direction import Direction, evolve_direction

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
    def vector_angle(self):
        if self.y > 0:
            return atan(self.y / self.x) 
        else :
            return pi + atan(self.y / self.x)

    def __iter__(self):
        return iter([self.x, self.y])
    def __repr__(self):
        return repr(list(self))

class Move:
    def __init__(self, direction, speed = 3):
        self.direction = direction % (2*pi)
        self.speed = speed
    def step(self):
        return Location([cos(self.direction)*self.speed, 
            sin(self.direction)*self.speed])

class Creature:
    def __init__(self, game = None, color = None):
        self.direction =  Direction()
        self.game = game

        if color is None:
            self.color = [randint(0,255) for _ in range(3)]
        else :
            self.color = color
        self.location = Location([0,0])
        self.radius = CREATURE_RADIUS
        self.foods_eaten = []

    def move(self):
        self.location = self.location + Move(self.direction.move()).step()

    def move_back(self):
        self.location = self.location - Move(self.direction.last_move()).step()

    def amount_eaten(self):
        return len(self.foods_eaten)

    def restart(self):
        self.foods_eaten = []
        self.location = Location([0,0])
        self.direction.index = 0
        self.direction.subindex = 0 



def evolve_creature(c):
    new_creature = Creature(game = c.game)
    new_creature.direction, is_new = evolve_direction(c.direction)
    if not is_new:
        new_creature.color = c.color
    return new_creature 