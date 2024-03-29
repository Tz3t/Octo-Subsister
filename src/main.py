#Charles Madsen
import pygame

pygame.init()
screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
game_state = "start_menu"
pygame.display.set_caption('Octo-Subsistors')

def startScreen():
   #Background 
   screen.fill((100, 52, 78))
   #font
   font = pygame.font.SysFont('arial', 40)
   #Title
   title = font.render('Welcome To Octo-Subsistors', True, (255, 255, 255))
   start_button = font.render('Press Space to Play', True, (255, 255, 255))
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
def characterScreen():
  screen.fill((100, 52, 78))
  font = pygame.font.SysFont('arial', 30)
  title = font.render('Please choose your character', True, (255, 255, 255))
  screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/3 - title.get_height()/3/2))
  #input box
  input_rect = pygame.Rect(200, 200, 140, 32) 

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
           game_state = "name"
           game_over = False
   elif game_state == "game_over":
       deathScreen()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_p]:
           game_state = "start_menu"
       if keys[pygame.K_o]:
           pygame.quit()
           quit()
   elif game_state == 'name':
       characterScreen()
   elif game_over:
       game_state = "game_over"
       game_over = False
