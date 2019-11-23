
import pygame

pygame.init()

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
black = (0, 0, 0)
DISPLAY_WIDTH = 400 
DISPLAY_HEIGH = 400 

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("My first game")
x = 50
y = 50
width = 40
height = 40
vol = 5
clock=pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
  pygame.time.delay(100)
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("User asked to quit.")
      done = True
  keys = pygame.key.get_pressed()    
  

  if keys[pygame.K_LEFT] and x > 0:
      x -= vol
  if keys[pygame.K_RIGHT] and x < DISPLAY_WIDTH - width:
      x += vol
  if keys[pygame.K_UP] and y > 0:
      y -= vol
  if keys[pygame.K_DOWN] and y < DISPLAY_HEIGH - height:
      y += vol
  pygame.draw.rect(screen, (255,0,0),  [x, y, width, height])
  pygame.display.update()
  
  
  
  # if event.type == pygame.KEYDOWN:
  #     print("User pressed a down key.")
  # if event.type == pygame.KEYUP:
  #     print("User let go of a up key.")
  # if event.type == pygame.MOUSEBUTTONDOWN:
  #     print("User pressed a mouse button")

  # pygame.draw.rect(screen, (255,0,0),  [x, y, widht, height])
  # --- Game logic should go here
  # --- Drawing code should go here
  # First, clear the screen to white. Don't put other 
  # drawing commands above this, 
  # or they will be erased with this command.
  
  screen.fill(black)
  
  # --- Go ahead and update the screen with what we've drawn.
  
  # --- Limit to 60 frames per second
  clock.tick(60)