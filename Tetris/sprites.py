SHAPES = {
    'I': {
        'pattern': [
            [1, 1, 1, 1]
        ],
        'color': (0, 255, 255)  # Cyan / Ціановий
    },
    'O': {
        'pattern': [
            [1, 1],
            [1, 1]
        ],
        'color': (255, 255, 0)  # Yellow / Жовтий
    },
    'T': {
        'pattern': [
            [0, 1, 0],
            [1, 1, 1]
        ],
        'color': (128, 0, 128)  # Purple / Фіолетовий
    },
    'S': {
        'pattern': [
            [0, 1, 1],
            [1, 1, 0]
        ],
        'color': (0, 255, 0)  # Green / Зелений
    },
    'Z': {
        'pattern': [
            [1, 1, 0],
            [0, 1, 1]
        ],
        'color': (255, 0, 0)  # Red / Червоний
    },
    'J': {
        'pattern': [
            [1, 0, 0],
            [1, 1, 1]
        ],
        'color': (0, 0, 255)  # Blue / Синій
    },
    'L': {
        'pattern': [
            [0, 0, 1],
            [1, 1, 1]
        ],
        'color': (255, 165, 0)  # Orange / Помаранчевий
    }
}

def get_data(shape_name): # встановити дані за фигури shape_name
    shape_data = SHAPES[shape_name]
    pattern = shape_data['pattern']
    color = shape_data['color']
    return color, pattern