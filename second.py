import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill(pygame.Color("white"))

n = int(input("n = "))
stor = 10
x = 0
y = 0
count = [stor*x for x in range(0,n,1)] # 0, 10, 20, ..., 10*(n-1)
for i in range(0,n,1):
  for i1 in range(0,i+1,1):
    pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (x+int(count[i1]), y+int(count[i]), stor, stor))

pygame.display.flip()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()