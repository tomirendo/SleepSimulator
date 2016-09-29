import pygame 
from board import Board

BACKGROUND = [0,0,0]

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()


def draw_creature(creature):
    pygame.draw.circle(screen, creature.color, 
        list(map(int, creature.location)), int(creature.radius))

def draw_display(board):
    screen.fill(BACKGROUND)
    for c in board.creatures:
        draw_creature(c)
    for f in board.foods:
        draw_creature(f)
        
game = Board (500, 50)

while True:
    clock.tick(20)
    game.move()
    draw_display(game)
    pygame.display.flip()





