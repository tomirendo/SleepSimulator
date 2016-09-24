EMPTY_CELL = str 
from creature import Creature
from elements import Action, Direction, Location
from elements import action_destination
from random import shuffle

class Board:
    def __init__(self, size):
        self.size = size
        self.creatures = [Creature(self) for _ in range((size//2)**2)]
        self.all_creatures = list(self.creatures)
        self.init_board()
        
    def init_board(self): 
        size = self.size

        shuffle(self.all_creatures)
        self.creatures = list(self.all_creatures)

        self.board = [[EMPTY_CELL() for _ in range(size)] for _ in range(size)]
        for creature, i in zip(self.creatures, range(0,size ** 2,2)):
            x,y = [(1+(i//size*2))%size,(1+i)%size]
            self.board[x][y] =  creature
            creature.position = Location([x,y])

    def new_generation(self):
        ordered_creatures = sorted(self.all_creatures)
        top_creatures = ordered_creatures[len(self.all_creatures)//2:]
        self.all_creatures = list(top_creatures)
        for creature in top_creatures:
            self.all_creatures.append(creature.copy())
            creature.init()
        self.creatures = list(self.all_creatures)
    
    def get_position(self, position):
        return self.board[position.y][position.x]
    
    def set_position(self, position, value):
        self.board[position.y][position.x] = value
    
    def clear_position(self, position):
        self.board[position.y][position.x] =  EMPTY_CELL()
        
    def is_in_board(self, position):
        return position.in_board(self.size)
            
    def is_action_available(self, location, action, direction):
        destination = action_destination(direction, location)
        if destination.in_board(self.size):
            if action == Action.move:
                return self.creature_on_location(destination) is None
            if action == Action.eat:
                return not (self.creature_on_location(destination) is None)
            
        else :
            return False
            
    def creature_on_location(self, location):
        for creature in self.creatures:
            if location == creature.position:
                return creature
   
    def move(self):
        all_moves = []
        size = self.size
        for creature in self.creatures:
            action, direction = creature.move()
            location = creature.position
            if self.is_action_available(location, action, direction):
                destination = action_destination(direction, location)
                all_moves.append([destination, action])
                if action == Action.move:
                    self.set_position(location, EMPTY_CELL())
                    self.set_position(destination, creature)
                    creature.position = destination
                elif action == Action.eat:
                    eated_creature = self.creature_on_location(destination)
                    eated_creature.eaten()
                    self.creatures.remove(eated_creature)
                    self.set_position(location,EMPTY_CELL()) 
                    #self.set_position(destination, creature)
                    #creature.position = destination
                    creature.eat()
        return all_moves 
                
            
    def _repr_html_(self):
        return pd.DataFrame(self.board)._repr_html_()