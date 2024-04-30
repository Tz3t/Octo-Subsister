#Charles Madsen | Player.py
import pygame
class Player:

    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.pl = pygame.image.load("player.png")
        self.pl = pygame.transform.scale(self.pl, (200,200))
        damage = 10
        health = 100
        speed = 1
    def draw_player(self, x, y, screen):
        self.x = x
        self.y = y
        screen.blit(self.pl, (x - 10, y - 10))
