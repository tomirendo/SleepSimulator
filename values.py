from random import randint
from elements import Action, Direction

def rand_in_range():
    return randint(0, len(Action.__members__)*len(Direction.__members__))

class Value:
    def __init__(self, creature):
        self.creature = creature
        self.inputs = []
        self.links = 0
        self.args = (creature,)
    def add_input(self, input):
        self.inputs.append(input)
    def value(self):
        return 0
    def get_empty_link(self):
        if self.links > len(self.inputs):
            return self
        else :
            for value in self.inputs:
                link = value.get_empty_link()
                if link is not None:
                    return link
        return None
    def __repr__(self):
        return str(self.__class__.__name__)
    def copy(self):
        a_copy = type(self)(None)
        a_copy.__dict__ = dict(self.__dict__)
        return a_copy


class TwoInputValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.links = 2
    def __repr__(self):
        a,b = self.inputs
        return "({},{}) -> {}".format(repr(a), repr(b), self.__class__.__name__)

class Add(TwoInputValue):
    def value(self):
        a,b = self.inputs
        return a.value() + b.value()
class Subtract(TwoInputValue):
       def value(self):
        a,b = self.inputs
        return a.value() - b.value()
class Multiply(TwoInputValue):
    def value(self):
        a,b = self.inputs
        return a.value() * b.value()

class Mod(TwoInputValue):
    def value(self):
        a,b = self.inputs
        b_value = b.value()
        if b_value != 0 :
            return a.value() % b_value
        return 0

class ConstValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.const_value = rand_in_range() 
    def value(self):
        return self.const_value
class CounterValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.counter = 0 
    def value(self):
        self.counter += 1
        return self.counter
class RandomValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.max = rand_in_range()
    def value(self):
        return randint(0, self.max)
class XValue(Value):
    def value(self):
        return self.creature.position.x
class YValue(Value):
    def value(self):
        return self.creature.position.y



values = [ConstValue, CounterValue, XValue, YValue, RandomValue, Add, Subtract, Multiply, Mod]

#Temporary
no_input_values = [RandomValue, ConstValue, CounterValue, XValue, YValue]
two_input_values = [Add, Subtract, Multiply, Mod]

from random import choice
def random_value(creature):
    return choice(values)(creature)

def create_value(creature):
    last_value = random_value(creature)
    emtpy_link = last_value.get_empty_link()
    while emtpy_link is not None:
        emtpy_link.add_input(random_value(creature))
        emtpy_link = last_value.get_empty_link()
    return last_value

def copy_chain(chain):
    top_chain = chain.copy()
    top_chain.inputs = []
    for link in chain.inputs:
        top_chain.add_input(copy_chain(link))
    return top_chain

def evolve_chain(chain):
    if randint(0,5) == 0:
        chain_type = type(chain)
        if chain_type in no_input_values:
            return choice(no_input_values)(chain.creature)
        elif chain_type in two_input_values:
            new_chain = choice(two_input_values)(chain.creature)
            for input in chain.inputs:
                new_chain.add_input(input)
            return new_chain
    elif randint(0,5) == 0:
        return create_value(chain.creature)
    elif randint(0,5) == 0 and chain.inputs :
        random_index = randint(0, len(chain.inputs) - 1)
        chain.inputs[random_index] = evolve_chain(chain.inputs[random_index])
        return chain
    else :
        return chain










