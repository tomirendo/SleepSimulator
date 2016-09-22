EMPTY_CELL = str 
from creature import Creature
from elements import Action, Direction, Location
from elements import action_destination
import pandas as pd
class Board:
    def __init__(self, size, creatures):
        self.creatures = list(creatures)
        self.size = size
        self.init_board()
        
    def init_board(self): 
        size = self.size
        self.board = [[EMPTY_CELL() for _ in range(size)] for _ in range(size)]
        for creature, i in zip(self.creatures, range(0,size ** 2,2)):
            x,y = [(1+(i//size*2))%size,(1+i)%size]
            self.board[x][y] =  creature
            creature.position = Location([x,y])
    
    def get_position(self, position):
        return self.board[position.y][position.x]
    
    def set_position(self, position, value):
        self.board[position.y][position.x] = value
    
    def clear_position(self, position):
        self.board[position.y][position.x] =  EMPTY_CELL()
            
            
    def is_action_available(self, location, action, direction):
        destination = action_destination(direction, location)
        if destination.in_board(self.size):
            if action == Action.move:
                return self.creature_on_location(destination) is None
            if action == Action.look:
                return True
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
                elif action == Action.look:
                    pass
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