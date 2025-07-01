import pygame
import sys
from generait import generait_map,set_color,do_collor,map

def number_to_color(number)->list:
    if number == 1:
        in_kube = (255,0,0)
        out_kube = (255,255,255)
    elif number == 2:
        in_kube = (0,255,0)
        out_kube = (255,255,255)
    elif number == 3:
        in_kube = (0,0,255)
        out_kube = (255,255,255)
    else:
        in_kube = (0,0,0)
        out_kube = (255,255,255)
    return in_kube,out_kube


def paint_map(screen,map):
    global X,Y,stor
    h = len(map)
    l = len(map[0])
    print("h = ",h)
    print("l = ",l)
    for iL in range(0,l):
        for iH in range(0,h):
            inn,out = number_to_color(map[iH][iL])
            pygame.draw.rect(screen, (out), (X+int(stor*iL), Y+int(stor*iH), stor, stor))
            pygame.draw.rect(screen, (inn), (X+int(stor*iL)+1, Y+int(stor*iH)+1, stor-2, stor-2))

if __name__ == "__main__":
    stor = 20
    h = 20
    l = 10
    X = 20
    Y = 20
    generait_map(h,l)
    set_color(2,4,do_collor())
    for rous in range(0,len(map)):
        print(map[rous])

    pygame.init()
    screen = pygame.display.set_mode((20*(l+2)+100, 20*(h+2)))
    screen.fill(pygame.Color("black"))
    
    paint_map(screen,map)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()