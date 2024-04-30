#Charles Madsen | Enemy.py
import pygame, sys

class Enemy:
    def __init__(self, display, colour, start_pos, radius):
     self.display = display
     self.colour = colour
     self.x, self.y = start_pos
     self.radius = radius
     self.turn_around = False
     self.start_pos = self.x

def draw_moving_enemy(self, speed, end_pos):
    # the circle will go backwards once it's reached the given end position
    if self.x <= end_pos - speed and self.turn_around == False:
        self.x += speed
        if self.x > end_pos - speed:
            self.turn_around = True
    # the circle will go forwards once it's reached the start positionel
    if self.x >= self.start_pos + speed and self.turn_around == True:
        self.x -= speed
        if self.x < self.start_pos + speed:
            self.turn_around = False
        
    self.circle = pygame.draw.circle(self.surface, self.colour, (self.x, self.y), self.radius)

def check_collision(self, player):
    # check if the player has collided with an enemy
    if self.circle.colliderect(player):
        print("collision")
        pygame.time.delay(1000)
        sys.exit()
