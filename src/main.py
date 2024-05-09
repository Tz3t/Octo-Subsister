#Charles Madsen | Main.py
import pygame#, enemy
from player import Player
p1 = Player(100, 1, 10)
pygame.init()
screen_width = 1920
screen_height = 1080
bgSize = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
game_state = "start_menu"
pygame.display.set_caption('Octo-Subsistors')
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, bgSize)
playerx = 1000/2
playery = 750/2
x_direction = 0
y_direction = 0
fps = 60




def startScreen(): 
   #Background 
   screen.fill((100, 52, 78))
   #font
   font = pygame.font.SysFont('arial', 40)
   #Title
   title = font.render('Welcome To Octo-Subsistors', True, (255, 255, 255))
   start_button = font.render('Press Space to play or Esc to exit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
   pygame.display.update()

def deathScreen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 30)
   title = font.render('Game Over', True, (255, 255, 255))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()
def playScreen():
   #setting background
   screen.blit(bg, (0, 0))
   #drawing player
   p1.draw_player(playerx, playery, screen)



   
   pygame.display.flip
   

   pygame.display.update()
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()
   if game_state == "start_menu":
       startScreen()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_SPACE]:
           game_state = "play"
           game_over = False
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             pygame.quit()
   elif game_state == "game_over":
       deathScreen()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_p]:
           game_state = "start_menu"
       if keys[pygame.K_o]:
           pygame.quit()
           quit()
   elif game_state == 'play':
       #screen.fill((255, 255, 255))
       playScreen()
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
             x_direction = 1
          elif event.key == pygame.K_LEFT:
             x_direction = -1
          elif event.key == pygame.K_UP:
             y_direction = -1
          elif event.key == pygame.K_DOWN:
             y_direction = 1
       if event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
             x_direction = 0
          elif event.key == pygame.K_LEFT:
             x_direction = 0
          elif event.key == pygame.K_UP:
             y_direction = 0
          elif event.key == pygame.K_DOWN:
             y_direction = 0
       playerx += p1.speed * x_direction
       playery += p1.speed * y_direction
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             pygame.quit()
          
       p1.draw_player(playerx, playery, screen)
   elif game_over:
       game_state = "game_over"
       game_over = False
pygame.display.flip

