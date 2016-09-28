from random import random
from creature import Creature, Location, Move

def rand_location(size):
    return Location([random()*size for _ in range(2)])

class Board:
    def __init__(self, size, number_of_creatures):
        self.creatures = [Creature() for _ in range(number_of_creatures)]
        self.size = size
        self.locate_creatures()
    def locate_creatures(self):
        arranged_creatures = []
        for creature in self.creatures:
            creature.location = rand_location(self.size)
            while True:
                if creature_overlaps(creature, arranged_creatures):
                    creature.location = rand_location(self.size)
                else :
                    break
            arranged_creatures.append(creature)
    def move(self):
        for c in self.creatures:
            c.move()
            if creature_overlaps(c, [i for i in self.creatures if i is not c]):
                c.move_back()


def creature_overlaps(creature, list_of_creatures):
    for c in list_of_creatures:
        if c.location.distance(creature.location) < \
                creature.radius + c.radius:
                return True 
    return False



            
