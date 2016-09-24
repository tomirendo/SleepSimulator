from elements import Location, Action, Direction
from random import randint, choice
from values import create_value, copy_chain, evolve_chain
from itertools import product

MAX_MOVES = 20
def rand_move():
    return (choice([Action.move, Action.eat]), Direction(randint(0,7)))
    
def mutate_list_of_moves(ls):
    option =  randint(0, 5)
    random_index = randint(0, len(ls)-1)
    if option == 1 and (len(ls)-1):
        ls.pop(random_index)
    elif option == 2:
        to_add = rand_move()
        ls.insert(random_index, to_add)
    elif option == 3:
        new_move = rand_move()
        ls[random_index] = new_move


all_actions =  list(product(Action.__members__.values(), Direction.__members__.values()))
def pick_action(value):
    return all_actions[value % len(all_actions)]

class Creature: 
    def __init__(self):
        self.position = Location([0,0])
        self.rank = 0 
        self.color = tuple(randint(0,255) for _ in range(3))
        self.chain = create_value(self)
    
    def copy(self):
        c = Creature()
        c.color = self.color
        c.chain = copy_chain(self.chain)
        evolve_chain(c.chain)
        return c

    def move(self):
        return pick_action(self.chain.value())


    def init(self):
        self.rank = 0
        self.move_index = 0

    def eat(self):
        self.rank += 1
    def eaten(self):
        self.rank = -1    
    def update(self, value):
        pass
    def __gt__(self, second):
        return self.rank > second.rank
    def __lt__(self, second):
        return self.rank < second.rank
    def __eq__(self, second):
        return self.rank == second.rank
    def __repr__(self):
        return "C {} Rank : {}".format(repr(self.chain), self.rank)