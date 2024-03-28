# Charles Madsen
import pygame
#RGB
white = (255, 255, 255)
#X,Y
X = 500
Y = 500
#Global Variables
Naming = True
ChoosingC = True
ChoosingM = True
#pygame Initalize
pygame.init()
#Set up display
pygame.display.set_caption('Octo_Subsister')
#fullscreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((500, 500), vsync=1)
#Background Color as place holder for png
BG = (100, 222, 255)
screen.fill(BG)
pygame.display.flip()
font = pygame.font.SysFont('Arial', 20)

def startScreen(screen):
  global s
  t = True
  while t:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
    if pygame.mouse.get_pressed()[0]:
      pygame.time.delay(10)
      print("clicked")
      s = False
      t = False
    screen.fill(BG)
    text = "Welcome to Octo-Subsistors!"
    text = font.render(text, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (X //2, 225)
    screen.blit(text, textRect)
    clickText = "Click to play"
    clickText = font.render(clickText, True, (255, 255, 255))
    clickRect = clickText.get_rect()
    clickRect.center = (X //2, 250)
    screen.blit(clickText, clickRect)
    pygame.display.flip()

def nameScreen(screen):
    global Naming
    while Naming:
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
    screen.fill(BG)
    text = "Type in your Name"
    text = winFond.render(text, True, (0, 0, 0))
    rect = text.get_rect()
    rect.center = (X //2, 250)
    screen.blit(text, rect)
    pygame.display.flip()

#Main
run = True
start = True
s = True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      print('GameEnded')
      pygame.quit()
      quit()
    if s:
      startScreen(screen)
      print('startscreen')
    if Naming:
       nameScreen(screen)
       print('Namescreen')

       


