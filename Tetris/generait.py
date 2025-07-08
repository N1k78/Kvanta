import random

map = []

def do_collor()->int: # створити віпадковий колір
    return random.randint(1,3)

def generait_map(h,l)->None: # створити карту
    global map
    for high in range(0,h):
        rou = [] # рядок для генерації
        for lien in range(0,l):
            rou.append(0)
        map.append(rou)

def set_color(x,y,color)->None: # встановити колік за кордінат (x,y)
    map[y][x] = color

def get_color(x,y)->int: # отримат колік за кордінат (x,y)
    return map[y-1][x-1]

if __name__ == "__main__":
    h = int(input("h = ")) # висота 
    l = int(input("l = ")) # довжина
    generait_map(h, l)
    for rous in range(0,len(map)):
        print(map[rous])
    X = int(input("X = ")) #
    Y = int(input("Y = ")) #
    set_color(X,Y,do_collor())
    for rous in range(0,len(map)):
        print(map[rous])
    