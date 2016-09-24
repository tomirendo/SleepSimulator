#!/usr/local/bin/python3.5
import pygame
 
from simboard import Board
from creature import Creature
from elements import Location, Action
from random import shuffle, choice, seed

import argparse


seed(11)
seed(12 )
parser = argparse.ArgumentParser()
parser.add_argument('visual', metavar='v', type=str, 
                    help='Should display visual')
args = parser.parse_args()
if args.visual == "novisual":
    visual = False
else :
    visual = True

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ACTION_COLOR = {Action.move : WHITE, Action.eat : GREEN} 
pygame.init()
 
# Set the height and width of the screen
size = [500, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing Rectangle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 2
rect_change_y = 2
 
GENERATION_LEGNTH = 1
GAME_LENGTH = 250
SPEED = 50 

screen_size = 32
original_creatures = [Creature() for _ in range((screen_size//2)**2)]
number_of_creatures = len(original_creatures)
game = Board(screen_size, original_creatures)
block_size = (size[0] // screen_size, size[1]//screen_size)

def draw_at_location(position, color):
    pygame.draw.rect(screen, color, [position.x*block_size[0], position.y*block_size[1], block_size[0], block_size[1]])
    

# -------- Main Program Loop -----------
def single_run(visual = True):
    for _ in range(GAME_LENGTH):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)
        for creature in game.creatures:
            if visual:
                draw_at_location(creature.position, creature.color)
        moves = game.move()
        if visual:
            clock.tick(SPEED)
            pygame.display.flip()

        #for dest, act in moves :
        #    draw_at_location(dest , ACTION_COLOR[act])
        #clock.tick(100)
        pygame.display.flip()
 
def generation(visual = True):
    for _ in range(GENERATION_LEGNTH):
        shuffle(original_creatures)
        game.creatures = list(original_creatures)
        game.init_board()
        single_run(visual = visual)

from collections import Counter
while not done:
    # --- Event Processing
    generation(visual = visual)
    ordered_creatures = sorted(original_creatures)
    top_creatures = ordered_creatures[number_of_creatures//2:]
    print(len(set(c.color for c in top_creatures)), repr(top_creatures[-1]))
    original_creatures = list(top_creatures)
    for creature in top_creatures:
        original_creatures.append(creature.copy())
        creature.init()
    print(len(original_creatures))





    
# Close everything down
pygame.quit()
