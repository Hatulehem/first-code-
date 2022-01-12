import pygame
import time

from pygame import surface
from pygame.draw import circle

# screen size 
WINDOW_W = 900
WINDOW_H = 505
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# BK_COLOR = (205,255,255)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hypnosis mic: Alternative Rap Battle")

img = pygame.image.load("hypmic bg1.jpg")

play = True
while play:
  # screen.fill(BK_COLOR)
  screen.blit(img,(0,0))
  # pygame.draw.line(screen, (102,255,178) , [50,100] , [850,100] , 6)
  # pygame.draw.line(screen, (102,255,178) , [50,100] , [50,400] , 6)
  # pygame.draw.line(screen, (102,255,178) , [50,400] , [850,400] , 6)
  # pygame.draw.line(screen, (102,255,178) , [850,400] , [850,100] , 6)
  # i = 0
  # for i in range(0,900,30):
    # pygame.draw.line(screen, (102,255,178) , [i,0] , [i,900] , 8)
    # pygame.draw.line(screen, (102,255,178) , [0,i] , [900,i] , 8)
  i = 0
  for i in range(20):
    Y=0
    X=400
    pygame.draw.line(screen, (244,205,178) , [450,250] , [X,250+Y] , 3)
    pygame.draw.line(screen, (244,205,178), [450,250], [X,250-Y] , 3)
    if i < 10:
      X = X + 10
      Y = Y + 5
    if i >= 10:
      X = X - 10
      Y = Y - 5
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

pygame.quit()
