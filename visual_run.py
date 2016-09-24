#!/usr/local/bin/python3.5
import pygame
 
from simboard import Board
from creature import Creature
from elements import Location, Action
from random import shuffle, choice, seed

import argparse


seed()

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
full_size = [900, 500]
screen = pygame.display.set_mode(full_size)
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
GAME_LENGTH = 150
SPEED = 100 

screen_size = 32
game = Board(screen_size)
block_size = (size[0] // screen_size, size[1]//screen_size)

def draw_at_location(position, color):
    pygame.draw.rect(screen, color, [position.x*block_size[0], position.y*block_size[1], block_size[0], block_size[1]])

def display_creature(creature, index):
    x,y = [(1+(index//screen_size*2))%screen_size,(1+index)%screen_size]
    #pygame.draw.rect(creatures_display, creature.color, [x*block_size[0], y*block_size[1], block_size[0], block_size[1]])    

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
    for index, creature in enumerate(game.all_creatures):
            if visual:
                display_creature(creature, index)
    for _ in range(GENERATION_LEGNTH):
        game.init_board()
        single_run(visual = visual)

from collections import Counter
while not done:
    # --- Event Processing
    generation(visual = visual)
    game.new_generation()





    
# Close everything down
pygame.quit()
