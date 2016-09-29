from math import pi

class Value():
    def __init__(self, creature):
        self.input_count = 0
        self.inputs = []
        self.creature = creature
    def value(self):
        return (self._value()) % (pi * 2)

    def _value(self):
        return 0

class ClosestFoodDirection(Value):
    def _value(self):
        closest_food = min(self.creature.game.foods, lambda x: self.creature.direction(x.location))
        direction = (closest_food.location - self.creature.location).vector_angle()
        return direction

def random_value(creature):
    return ClosestFoodDirection(creature)

def evolve_value(v):
    return v

