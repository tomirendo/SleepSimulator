from simboard import Board
from creature import Creature
from elements import Location, Action
from random import shuffle

screen_size = 40
number_of_iterations = 10
original_creatures = [Creature() for _ in range((screen_size//2)**2)]
game = Board(screen_size, original_creatures)

for _ in range(number_of_iterations):
    for _ in range(1000):
        game.move()
    shuffle(original_creatures)
    game.creature = list(original_creatures)
    game.init_board()


