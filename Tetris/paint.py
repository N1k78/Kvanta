import pygame
import sys
from generait import generait_map,set_color,do_collor,get_color,map
from sprites import SHAPES
import random
from time import sleep

def number_to_color(number)->list:
    if number == 1:
        in_kube = (0, 255, 255)
        out_kube = in_kube
    elif number == 2:
        in_kube = (255, 255, 0)
        out_kube = in_kube
    elif number == 3:
        in_kube = (128, 0, 128)
        out_kube = in_kube
    elif number == 4:
        in_kube = (0, 255, 0)
        out_kube = in_kube
    elif number == 5:
        in_kube = (255, 0, 0)
        out_kube = in_kube
    elif number == 6:
        in_kube = (0, 0, 255)
        out_kube = in_kube
    elif number == 7:
        in_kube = (255, 165, 0)
        out_kube = in_kube
    else:
        in_kube = (0,0,0)
        out_kube = (255,255,255)
    return in_kube,out_kube

def color_to_number(color)->list:
    if color == (0, 255, 255):
      number = 1  
    elif color == (255, 255, 0):
        number = 2
    elif color == (128, 0, 128):
        number = 3
    elif color == (0, 255, 0):
        number = 4
    elif color == (255, 0, 0):
        number = 5
    elif color == (0, 0, 255):
        number = 6
    elif color == (255, 165, 0):
        number = 7
    else:
        number = 0
    return number

# 0 0 0 0 
# 0 2 0 0
# 1 2 2 2


def paint_map(screen,map):
    global X,Y,stor
    # print(type(map))
    h = len(map)    # висота 
    l = len(map[0]) # довжина
    # print("h = ",h)
    # print("l = ",l)
    for iL in range(0,l):
        for iH in range(0,h):
            try:
                into, out = number_to_color(map[iH][iL])
            except IndexError:
                print(f"iH = {iH}")
                print(f"iL = {iL}")
            pygame.draw.rect(screen, (out), (X+int(stor*iL), Y+int(stor*iH), stor, stor))
            pygame.draw.rect(screen, (into), (X+int(stor*iL)+1, Y+int(stor*iH)+1, stor-2, stor-2))

def paint_shape(shape,color,x_position,y_position): # намалювати фігуру
    global surface
    global screen
    for hight in range(0,len(shape)):
        for lenght in range(0,len(shape[hight])):
            if shape[hight][lenght] == 1:
                rect = pygame.Rect(x_position * stor + stor * lenght, int(y_position) * stor + stor * hight, stor, stor) 
                pygame.draw.rect(surface, color, rect)
    screen.blit(surface, (Y, X))

def move(data,dx,dy):
    active_new = active.copy()
    name = data["name"]
    color = SHAPES[name]["color"]
    rotation = data["rotation"]
    shape = SHAPES[name]["patterns"][rotation]
    active_new["x"] = data["x"] + dx
    active_new["y"] = int(data["y"])+dy
    return active_new

def spawn_pies() -> dict:
    global L
    # name = "I"
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


def Is_corect(data)->bool:
    next = SHAPES[data["name"]]["patterns"][data["rotation"]]
    # 0 0 0 0 0 0 0 0 0 0|1
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 0 0 0 0 0 0 0 0 0 0|
    # 1 1 1 1 0 0 0 0 0 0|
    # 0 0 0 2 0 0 0 0 0 0|20
    if data["x"] + len(next[0]) < L+1:
        to_return = True
        if data["x"] > -1:
            to_return = True
            if int(data["y"]) + len(next) < H + 1:
                to_return = True
            else:
                to_return = False
        else:
            to_return = False
    else:
        to_return = False
    return to_return

def route(data)->dict:
    rotations_count = SHAPES[data["name"]]["rotations_count"]
    rotation = active["rotation"]+1
    active_new = data.copy()
    active_new["rotation"] = rotation%rotations_count
    if Is_corect(active_new):
        # print(True)
        return active_new
    else:
        # print(False)
        return data

def is_valid_position(tetromino: dict) -> bool: 
    shape_pattern = SHAPES[tetromino['name']]['patterns'][tetromino['rotation']] 
    for row_index, row in enumerate(shape_pattern): 
        for col_index, cell in enumerate(row): 
            if cell != 0: 
                x = tetromino['x']
                y = int(tetromino['y'])
                grid_x = x + col_index 
                grid_y = y + row_index 
                if not (0 <= grid_x < L and 0 <= grid_y < H): 
                    return False
                if map[grid_y][grid_x] != 0:
                    # print(False)
                    return False
    return True

def clearn_bonus():
    global bouns
    try:
        bonus += 1
        bonus -= 1
    except:
        bonus = 0
    map_now = map.copy()
    for number, row in enumerate(map_now):
        next_row = [0 for _ in range(0,len(row))]
        if 0 not in row:
           map_now[number] = next_row
           print(row not in map_now)
           bonus += 1
           print(bonus)
    for rous in range(0,len(map_now)):
        print(map[rous])
    print(len(map_now))
    return map_now
    # map = map_new.copy()


def clear_lines(): 
    """ Перевіряє сітку на наявність заповнених рядків, видаляє їх і зсуває верхні рядки вниз. Повертає кількість очищених рядків для нарахування очок. """ 
    lines_cleared = 0 
    # Ітеруємо знизу вгору, щоб індекси не збивалися при видаленні 
    map_new = map.copy()
    y = H - 1 
    while y >= 0: 
        row = map_new[y] 
    # Якщо в рядку немає порожніх клітинок (None) 
        clear = True
        for cell in row:
            # type: ignore
            if cell == 0:
                clear =False
        if clear:
            lines_cleared += 1 
            # Видаляємо заповнений рядок 
            map_new.pop(y) 
            # # Додаємо новий порожній рядок нагорі, щоб зберегти висоту поля 
            map_new.insert(0, [0 for _ in range(L)]) 
        else: 
        # # Якщо рядок не заповнений, переходимо до перевірки наступного (вище) 
            y -= 1 
        return map_new, lines_cleared

def pin(tetromino: dict):
    shape_pattern = SHAPES[tetromino['name']]['patterns'][tetromino['rotation']]
    color = SHAPES[tetromino['name']]['color']
    number = color_to_number(color)

    for row_index, row in enumerate(shape_pattern):
        for col_index, cell in enumerate(row):
            if cell != 0:
                x = tetromino['x'] + col_index
                y = int(tetromino['y']) + row_index
                set_color(x, y, number)

    

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
    
    # set_color(5,5,7)
    
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
    
    bonus = 0
    
    active_new = active.copy()
    clock = pygame.time.Clock()
    DROP_EVENT = pygame.USEREVENT+1
    pygame.time.set_timer(DROP_EVENT,1000)
    game_over = False
    while True:
        sprite = active["name"]
        for event in pygame.event.get():
            keboard = event.type
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == DROP_EVENT and not game_over:
                active_new = move(active,0,1)
                if is_valid_position(active_new):
                    active = active_new
                else:
                    pin(active)
                    active = spawn_pies()
                    if not is_valid_position(active):
                        game_over = True
                map, lines_cleared = clear_lines()
                bonus += lines_cleared
            elif keboard == pygame.KEYDOWN and not game_over:
                keboard = event.key
                if keboard == pygame.K_LEFT:
                    active_new = move(active,-1,0)
                    if is_valid_position(active_new):
                        active = active_new
                elif keboard == pygame.K_RIGHT:
                    active_new = move(active,1,0)
                    if is_valid_position(active_new):
                        active = active_new
                elif keboard == pygame.K_DOWN:
                    active_new = move(active,0,1)
                    if is_valid_position(active_new):
                        active = active_new
                elif keboard == pygame.K_UP:
                    active = route(active)
        # pygame.time.set_timer(move(active,0,1), 100) 
        if not game_over:
            paint_map(screen,map)
            paint_shape(SHAPES[active["name"]]["patterns"][active["rotation"]],SHAPES[sprite]["color"],active["x"],active["y"])
            pygame.display.flip()
            # screen.fill(pygame.Color("green"))
            surface_width = L * stor
            surface_height = H * stor
            surface = pygame.Surface((surface_width, surface_height), pygame.SRCALPHA)
        else:
            print(f"bonus {bonus}")
