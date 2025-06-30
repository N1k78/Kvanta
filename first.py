import pygame
import math
import sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill(pygame.Color("white"))
r = float(input("r = "))
x = float(input("x = "))
y = float(input("y = "))
# x = 100
# y = 100
# r = 50
center_x, center_y = x, y
size = r


pygame.draw.circle(screen,(0,0,0),      (x, y), r+3,3)
pygame.draw.circle(screen,(255,255,0),      (x, y), r,)
pygame.draw.circle(screen,(255,255,255),    (center_x-r/3, center_y-r/3), r/4)
pygame.draw.circle(screen,(255,255,255),    (center_x+r/3, center_y-r/3), r/4)
pygame.draw.circle(screen,(0,0,0),          (center_x-r/3, center_y-r/3), r/8)
pygame.draw.circle(screen,(0,0,0),          (center_x+r/3, center_y-r/3), r/8)
pygame.draw.circle(screen,(255,255,255),    (center_x-r/3, center_y-r/3), r/32)
pygame.draw.circle(screen,(255,255,255),    (center_x+r/3, center_y-r/3), r/32)
pygame.draw.arc(   screen,(0,0,0),          (center_x-r/2, center_y-r/3, size, size), math.pi, 0, 3)


pygame.display.flip()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()