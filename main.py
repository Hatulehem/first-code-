from operator import truediv
from re import M
import pygame
import time

from pygame import surface
from pygame.draw import circle

# screen size 
WINDOW_W = 900
WINDOW_H = 500
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
  #קווים
  # pygame.draw.line(screen, (102,255,178) , [50,100] , [850,100] , 6)
  # pygame.draw.line(screen, (102,255,178) , [50,100] , [50,400] , 6)
  # pygame.draw.line(screen, (102,255,178) , [50,400] , [850,400] , 6)
  # pygame.draw.line(screen, (102,255,178) , [850,400] , [850,100] , 6)
  # i = 0
  # for i in range(0,900,30):
  #   pygame.draw.line(screen, (102,255,178) , [i,0] , [i,900] , 8)
  #   pygame.draw.line(screen, (102,255,178) , [0,i] , [900,i] , 8)
    #ניסיון
  # i = 0
  # for i in range(20):
  #   Y=0
  #   X=400
  #   pygame.draw.line(screen, (244,205,178) , [450,250] , [X,250+Y] , 3)
  #   pygame.draw.line(screen, (244,205,178), [450,250], [X,250-Y] , 3)
  #   if i < 10:
  #     X = X + 10
  #     Y = Y + 5
  #   if i >= 10:
  #     X = X - 10
  #     Y = Y - 5
  #עיגול
    # pygame.draw.circle(screen , (255,51,153) , (450,250) , i + 20 , 5 )
  # i = 0
  # for i in range(0,900,20):
  #   pygame.draw.circle(screen , (0,0,0) , (450,250) , i + 20 , 5 )

  #מלבן
  # pygame.draw.rect(screen, (0,0,0), (0,0,900,500),7)
  # i = 0
  # for i in range(0,900,50):
  #    pygame.draw.rect(screen, (0,0,0), (0,0,900-i,500),7)
  # for i in range(0,900,50):
  #   pygame.draw.rect(screen, (0,0,0), (0,0,900,500-i),7)

  #ריבוע
  # pygame.draw.rect(screen,(0,0,0),(300,0,300,300),7)

  #מצולע
  # pygame.draw.polygon(screen,(0,0,0),((0,0),(400,0),(400,250)))

  #ניסיון קווים 2
  # i = 0
  # m = 0
  # for i in range(250,500,50):
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450 - m, 250+ i], 5)
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450 - m, 250-i], 5)
  # for m in range(450,900,50):
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450 + m, 250 - i], 5)
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450 - m, 250 -i], 5)
  # for m in range(450,900,50):
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450- i, 250+ m], 5)
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450-i, 250-m], 5)
  # for i in range(250,500,50):
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450 + i, 250-m], 5)
  #   pygame.draw.line(screen, (0,0,0), [450,250], [450 - i, 250-m], 5)
  # i = 0
  # for i in range(0,600,30):
  #   pygame.draw.line(screen, (102,255,178) , [450,250] , [i,900] , 3)
  #   pygame.draw.line(screen, (102,255,178) , [450,250] , [900,i] , 3)
  #ניסיון קווים 3
  i = 0
  for i in range(300,400,50):
    # pygame.draw.line(screen,(0,0,0),[450,250],[0+i,0],3)
    # pygame.draw.line(screen,(0,0,0),[450,250],[0,0+i],3)
    # pygame.draw.line(screen,(0,0,0),[450,250],[0+i,500], 3)
    pygame.draw.line(screen,(0,0,0),[450,250],[900,0+i],3)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

pygame.quit()
