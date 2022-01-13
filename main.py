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

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hypnosis Arc: Neko Arc's Battle")

clock = pygame.time.Clock()

img = pygame.image.load("neko arc12.jpg")
X_pos_rct=0
Y_pos_rct=0
w = 80
h=100
vel = 10
jump = False
jumpCount = 10
# x_pos_circle=450
# y_pos_circle=250
run = True
while run:
  pygame.time.delay(50)
  #display
  screen.blit(img,(0,0))
  #הזזת צורות
  # pygame.draw.circle(screen , (51,51,255) , (x_pos_circle,y_pos_circle) , 50)
  # pygame.draw.rect(screen,(255,102,178),(X_pos_rct,Y_pos_rct,100,100))
  # X_pos_rct+=5
  # Y_pos_rct-=5
  # x_pos_circle+=5
  # y_pos_circle+=5

  # clock.tick(70)

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and X_pos_rct > vel:
    X_pos_rct-=vel
  if keys[pygame.K_RIGHT] and X_pos_rct < 900 - w - vel:
    X_pos_rct+=vel
  # if not(jump):
  if keys[pygame.K_UP] and Y_pos_rct > vel:
     Y_pos_rct-=vel
  if keys[pygame.K_DOWN] and Y_pos_rct < 500 - h - vel:
    Y_pos_rct+=vel
  #   if keys[pygame.K_SPACE]:
  #     jump = True
  # else:
  #   if jumpCount >= -10:
  #     neg = 1
  #     if jumpCount < 0:
  #       neg = -1
  #     Y_pos_rct-= (jumpCount ** 2) * 0.5 * neg
  #     jumpCount -= 1
  #   else:
  #     jump = False
  #     jumpCount = 10
  pygame.draw.rect(screen,(51,255,73),(X_pos_rct,Y_pos_rct,w,h))
  pygame.display.update()
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()
