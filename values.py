from random import randint
from elements import Action, Direction, action_destination

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
        return "({}{}{})".format(repr(a), self.sign, repr(b))
class OneInputValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.links = 1
    def __repr__(self):
        a, = self.inputs
        return "{}({})".format(self.__class__.__name__, repr(a))
  


class Add(TwoInputValue):
    sign = '+'
    def value(self):
        a,b = self.inputs
        return a.value() + b.value()
class Subtract(TwoInputValue):
    sign = '-'
    def value(self):
        a,b = self.inputs
        return a.value() - b.value()
class Multiply(TwoInputValue):
    sign = '*'
    def value(self):
        a,b = self.inputs
        return a.value() * b.value()
class Mod(TwoInputValue):
    sign = '%'
    def value(self):
        a,b = self.inputs
        b_value = b.value()
        if b_value != 0 :
            return a.value() % b_value
        return 0
class Compare(TwoInputValue):
    sign = '>'
    def value(self):
        a,b = self.inputs
        return int(a.value() > b.value())
class Div(TwoInputValue):
    sign = '/'
    def value(self):
        a,b = self.inputs
        b_value = b.value()
        if b_value == 0 :
            return 0
        return a.value()//b_value

class ConstValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.const_value = rand_in_range() 
    def __repr__(self):
        return str(self.const_value)
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

all_directions = list(Direction.__members__.values())
number_of_directions = len(all_directions)
def map_integer_to_direction(number):
    return all_directions[number % number_of_directions]

class GreenValue(Value):
    def __init__(self, *args):
        Value.__init__(self, *args)
        self.direction = map_integer_to_direction(randint(0, number_of_directions-1))
    def value(self):
        dest = action_destination(self.direction, self.creature.position)
        if self.creature.game.is_in_board(dest):
            object_at_position = self.creature.game.get_position(dest)
            if object_at_position:
                return object_at_position.color[1] // 25
        return 0
    def __repr__(self):
        return "GreenValue({})".format(self.direction)



values = [GreenValue, ConstValue, CounterValue, Add, Subtract, Multiply, Mod, Compare, Div]

#Temporary
no_input_values = [GreenValue, ConstValue, CounterValue]
two_input_values = [Add, Subtract, Multiply, Mod, Compare, Div]
one_input_values = []

from random import choice
def random_value(creature):
    rnd = randint(1,100)
    if rnd <= 60:
        return choice(one_input_values + no_input_values)(creature)
    else :
        return choice(two_input_values)(creature)

def create_value(creature):
    last_value = choice(two_input_values)(creature)
    count = 1
    emtpy_link = last_value.get_empty_link()
    while emtpy_link is not None:
        if count < 15:
            emtpy_link.add_input(random_value(creature))
        else :
            emtpy_link.add_input(choice(no_input_values)(creature))
        emtpy_link = last_value.get_empty_link()
        count += 1
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
        elif chain_type in one_input_values:
            new_chain = choice(one_input_values)(chain.creature)
            new_chain.add_input(chain.inputs[0])
            return new_chain
    elif randint(0,5) == 0:
        return create_value(chain.creature)
    elif randint(0,3) == 0 and chain.inputs :
        random_index = randint(0, len(chain.inputs) - 1)
        chain.inputs[random_index] = evolve_chain(chain.inputs[random_index])
        return chain
    else :
        return chain










