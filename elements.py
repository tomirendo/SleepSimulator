from enum import Enum
class Direction(Enum):
    r = 0
    rd = 1
    d = 2
    ld = 3
    l = 4
    lu = 5
    u = 6
    ru = 7
    
class Action(Enum):
    move = 0
    eat = 1
    look = 2    

class Location:
    def __init__(self, loc):
        self.x, self.y = loc
    def __iter__(self):
        return iter([self.x,self.y])
    def in_board(self, size):
        return self.x < size and self.y < size and (self.y>=0) and (self.x>=0)
    def __eq__(self, second):
        return self.x == second.x and self.y == second.y
    def __repr__(self):
        return repr(tuple(self))

def action_destination(direction, location):
    destination = Location(list(location))
    if direction in (Direction.d, Direction.rd, Direction.ld):
        destination.y += 1
    elif direction in (Direction.u, Direction.ru, Direction.lu):
        destination.y -= 1
    if direction in (Direction.r, Direction.rd, Direction.ru):
        destination.x -= 1
    elif direction in (Direction.l, Direction.ld, Direction.lu):
        destination.x += 1
    return destination
