from random import random
from creature import Creature, Location, Move
from food import Food

def rand_location(size):
    return Location([random()*size for _ in range(2)])

class Board:
    def __init__(self, size, number_of_creatures, number_of_foods=30):
        self.creatures = [Creature() for _ in range(number_of_creatures)]
        self.foods = [Food() for _ in range(number_of_foods)]
        self.size = size
        self.locate_creatures()
        self.locate_foods()

    @property
    def objects(self):
        return self.creatures + self.foods

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

    def locate_foods(self):
        arranged_foods = []
        for food in self.foods:
            food.location = rand_location(self.size)
            while True:
                if creature_overlaps(food, arranged_foods + self.creatures):
                    food.location = rand_location(self.size)
                else :
                    break
            arranged_foods.append(food)

    def move(self):
        for c in self.creatures:
            c.move()
            if creature_overlaps(c, [i for i in self.creatures if i is not c]):
                c.move_back()
            else :
                foods_eaten_by_creature = list(overlaping_foods(c, self.foods))
                for f  in foods_eaten_by_creature:
                    self.foods.remove(f)
                c.foods_eaten.extend(foods_eaten_by_creature)





def creature_overlaps(creature, list_of_creatures):
    for c in list_of_creatures:
        if c.location.distance(creature.location) < \
                creature.radius + c.radius:
                return True 
    return False

def overlaping_foods(creature, foods):
    for f in foods:
        if f.location.distance(creature.location) < \
            creature.radius + f.radius:
                yield f 


            
