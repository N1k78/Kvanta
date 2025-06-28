import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill(pygame.Color("white"))
pygame.draw.circle(screen, pygame.Color("red"), (320, 240), 100)
pygame.display.flip()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()