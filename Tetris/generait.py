import random

map = []

def do_collor()->int:
    return random.randint(1,3)

def generait_map(h,l)->None:
    global map
    for high in range(0,h):
        rou = []
        for lien in range(0,l):
            rou.append(0)
        map.append(rou)

def set_color(x,y,color)->None:
    map[x-1][y-1] = color

def get_color(x,y)->None:
    return map[x-1][y-1]

if __name__ == "__main__":
    h = int(input("h = "))
    l = int(input("l = "))
    generait_map(h, l)
    for rous in range(0,len(map)):
        print(map[rous])
    X = int(input("X = "))
    Y = int(input("Y = "))
    set_color(X,Y,do_collor())
    for rous in range(0,len(map)):
        print(map[rous])
    