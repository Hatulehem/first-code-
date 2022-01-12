import pygame
import time

# screen size 
WINDOW_W = 1360
WINDOW_H = 1080
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# BK_COLOR = (205,255,255)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hypnosis mic: Alternative Rap Battle")

img = pygame.image.load("dotsuirate hompo12.jpg")

play = True
while play:
  # screen.fill(BK_COLOR)
  screen.blit(img,(0,0))
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

pygame.quit()
