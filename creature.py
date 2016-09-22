from elements import Location, Action, Direction
from random import randint, choice

MAX_MOVES = 20
def rand_move():
    return (choice([Action.move, Action.eat]), Direction(randint(0,7)))

class ConstValue:
    def __init__(self, value):
        self.value = value
    def value(self)
        return self.value


class x(Value):
    def 

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


class Creature: 
    def __init__(self):
        self.position = Location([0,0])
        self.number_of_moves = randint(1,MAX_MOVES)
        self.list_of_moves = [rand_move() for _ in range(self.number_of_moves)]
        self.move_index = 0
        self.rank = 0 
        self.color = tuple(randint(0,255) for _ in range(3))
    
    def copy(self):
        c = Creature()
        c.color = self.color
        c.list_of_moves = list(self.list_of_moves)
        mutate_list_of_moves(c.list_of_moves)
        c.number_of_moves = len(c.list_of_moves)
        return c

    def move(self):
        self.move_index = (self.move_index + 1) % self.number_of_moves
        return self.list_of_moves[self.move_index]

    def init(self):
        self.rank = 0
        self.move_index = 0

    def eat(self):
        self.rank += 1
    def eaten(self):
        self.rank -= 1
    
    def update(self, value):
        pass
    def __gt__(self, second):
        return self.rank > second.rank
    def __lt__(self, second):
        return self.rank < second.rank
    def __eq__(self, second):
        return self.rank == second.rank
    def __repr__(self):
        return "C {} Rank : {}".format(repr(self.list_of_moves), self.rank)