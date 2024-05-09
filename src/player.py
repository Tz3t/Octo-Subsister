#Charles Madsen | Player.py
import pygame
class Player:

    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.pl = pygame.image.load("player.png")
        self.pl = pygame.transform.scale(self.pl, (100,100))
        damage = 10
        health = 100
        speed = 1
    def draw_player(self, playerx, playery, screen):
        self.playerx = playerx
        self.playery = playery
        screen.blit(self.pl, (playerx - 10, playery - 10))
