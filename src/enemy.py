class Enemy:
    def __init__(self, x, y, speed, damage, health):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.health = health
        health = 100
        speed = 1
        damage = 5
    def draw enemy

    def move_towards_player(self, player_x, player_y):
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed

        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed

    def check_collision(self, player_x, player_y):
        if self.x == player_x and self.y == player_y:
            return True
        else:
            return False
