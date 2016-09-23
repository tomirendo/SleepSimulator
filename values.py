from random import randint

"""
#X Value - input 0 output 1
#Y Value 
#Random
#Constant

#Add
#Subtract
#Multiply 
"""


class Value:
    def __init__(self, creature):
        self.creature = creature
        self.inputs = []
        self.links= 0
    def add_input(input)
        self.inputs.append(input)
    def value(self):
        return 0
    def get_empty_link(self):
        if self.links < len(self.inputs):
            return self
        else :
            for value in self.inputs:
                link = get_empty_link(value)
                if link is not None:
                    return link

class TwoInputValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.links = 2

class Add(TwoInputValue):
    def value(self):
        a,b = self.inputs
        return a.value()+b.value()
class Subtract(TwoInputValue):
       def value(self):
        a,b = self.inputs
        return a.value() - b.value()
class Multiply(TwoInputValue):
    def value(self):
        a,b = self.inputs
        return a.value() * b.value()

class ConstValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.value = randint(0,10)
    def value(self)
        return self.value
class XValue(Value):
    def value(self):
        return self.creature.position.x
class YValue(Value):
    def value(self):
        return self.creature.position.y


values = [ConstValue, XValue, YValue, Add, Subtract, Multiply]

from random import choice
def random_value():
    return choice(values)
def create_value(creature):
    last_value = random_value()
    emtpy_link = last_value.get_empty_link()
    while emtpy_link is not None:
        emtpy_link.add_input(random_value)
        emtpy_link = last_value.get_empty_link()




