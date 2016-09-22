from random import randint

class Value:
    def __init__(self, creature):
        self.creature = creature
    def value(self):
        return 0

class ConstValue(Value):
    def __init__(self, creature):
        self.value = randint(0,10)
    def value(self)
        return self.value

class XValue(Value):
    def value(self):
        return self.creature.position.x

class YValue(Value):
    def value(self):
        return self.creature.position.y

