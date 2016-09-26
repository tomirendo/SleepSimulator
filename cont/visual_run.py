import pygame 

CREATURE_RADIUS
pygame.init()
screen = pygame.display.set_moce([500,500])
clock = pygame.time.Clock()


def draw_creature(creature):
    pygame.draw.circle(screen, creature.color, 
        list(creature.location), CREATURE_RADIUS)


