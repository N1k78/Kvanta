import pygame
import sys
from generait import generait_map,set_color,do_collor,map
from sprites import SHAPES
import random
from time import sleep

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
    h = len(map)    # висота 
    l = len(map[0]) # довжина
    # print("h = ",h)
    # print("l = ",l)
    screen.fill(pygame.Color("green"))
    for iL in range(0,l):
        for iH in range(0,h):
            pygame.draw.rect(screen, ((255,255,255)), (X+int(stor*iL), Y+int(stor*iH), stor, stor))
            pygame.draw.rect(screen, ((0,0,0)), (X+int(stor*iL)+1, Y+int(stor*iH)+1, stor-2, stor-2))

def paint_shape(shape,color,x_position,y_position): # намалювати фігуру
    global surface
    global screen
    for hight in range(0,len(shape)):
        for lenght in range(0,len(shape[hight])):
            if shape[hight][lenght] == 1:
                rect = pygame.Rect(x_position * stor + stor * lenght, y_position * stor + stor * hight, stor, stor) 
                pygame.draw.rect(surface, color, rect)
    screen.blit(surface, (Y, X))

def move(data,dx,dy):
    global active
    name = data["name"]
    color = SHAPES[name]["color"]
    rotation = data["rotation"]
    shape = SHAPES[name]["patterns"][rotation]
    if (active["x"] + len(shape[0])  < L) and dx > 0:
        active["x"] = data["x"]+dx
    if (active["x"] >= 1) and dx < 0:
        active["x"] = data["x"] + dx
    active["y"] = int(data["y"])+dy

def spawn_pies() -> dict:
    global L
    name = random.choice(list(SHAPES.keys()))
    SHAPES_data = SHAPES[name]
    x = L // 2 - len(SHAPES_data['patterns'][0][0]) // 2
    base ={
        'name' : name,
        'patterns' : SHAPES_data['patterns'][0],
        'rotation' : 0,
        'x' : x,
        'y' : "0"
    }
    return base   

if __name__ == "__main__":
    stor = 20
    H = 20
    L = 10
    X = 20
    Y = 20
    generait_map(H,L)
    # set_color(2,4,do_collor())
    # for rous in range(0,len(map)):
    #     print(map[rous])

    pygame.init()
    screen = pygame.display.set_mode((20*(L+2)+100, 20*(H+2)))
    pygame.display.set_caption('Tetris')
    screen.fill(pygame.Color("black"))
    
    surface_width = L * stor
    surface_height = H * stor
    surface = pygame.Surface((surface_width, surface_height), pygame.SRCALPHA)
    
    paint_map(screen,map)
    
    sprite = "I"
    x_position = 2
    y_position = 3
    # paint_shape(SHAPES[sprite]["patterns"][0],SHAPES[sprite]["color"],x_position,y_position)

    active = spawn_pies()
    print(active)
    
    move(active,-1,1)
    
    while True:
        for event in pygame.event.get():
            keboard = event.type
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif keboard == pygame.KEYDOWN:
                keboard = event.key
                if keboard == pygame.K_LEFT:
                    print("1")
                    move(active,-1,0)
                elif keboard == pygame.K_RIGHT:
                    print("2")
                    move(active,1,0)
                elif keboard == pygame.K_DOWN:
                    print("3")
                    move(active,0,1)
                elif keboard == pygame.K_UP:
                    active["rotation"] = (active["rotation"]+1)%4
        paint_map(screen,map)
        paint_shape(SHAPES[active["name"]]["patterns"][active["rotation"]],SHAPES[sprite]["color"],active["x"],active["y"])
        pygame.display.flip()
        screen.fill(pygame.Color("green"))
        sleep(0.1)
