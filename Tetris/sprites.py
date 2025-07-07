import random

SHAPES = {
    'I': {
        'patterns': [[
            [1, 1, 1, 1]
        ],
        [
            [1],
            [1],
            [1],
            [1]
        ]
        ],
        'rotations_count': 2,
        'color': (0, 255, 255)  # Cyan / Ціановий
    },
    'O': {
        'patterns': [
            [
                [1, 1],
                [1, 1]
            ]
        ],
        'rotations_count': 1,
        'color': (255, 255, 0)  # Yellow / Жовтий
    },
    'T': {
        'patterns': [[
            [0, 1, 0],
            [1, 1, 1]
        ],
        [
            [1, 0],
            [1, 1],
            [1, 0]
        ],
        [
            [1, 1, 1],
            [0, 1, 0]
        ],
        [
            [0, 1],
            [1, 1],
            [0, 1]
        ]
        ],
        'rotations_count': 4,
        'color': (128, 0, 128)  # Purple / Фіолетовий
    },
    'S': {
        'patterns': [[
            [0, 1, 1],
            [1, 1, 0]
        ],
        [
            [1, 0],
            [1, 1],
            [0, 1]
        ]
        ],
        'rotations_count': 2,
        'color': (0, 255, 0)  # Green / Зелений
    },
    'Z': {
        'patterns': [[
            [1, 1, 0],
            [0, 1, 1]
        ],
        [
            [0, 1],
            [1, 1],
            [1, 0]
        ]
        ],
        'rotations_count': 2,
        'color': (255, 0, 0)  # Red / Червоний
    },
    'J': {
        'patterns': [[
            [1, 0, 0],
            [1, 1, 1]
        ],
        [
            [1, 1],
            [1, 0],
            [1, 0]
        ],
        [
            [1, 1, 1],
            [0, 0, 1]
        ],
        [
            [0, 1],
            [0, 1],
            [1, 1]
        ]
        ],
        'rotations_count': 4,
        'color': (0, 0, 255)  # Blue / Синій
    },
    'L': {
        'patterns': [[
            [0, 0, 1],
            [1, 1, 1]
        ],
        [
            [1, 0],
            [1, 0],
            [1, 1]
        ],
        [
            [1, 1, 1],
            [1, 0, 0]
        ],
        [
            [1, 1],
            [0, 1],
            [0, 1]
        ]
        ],
        'rotations_count': 4,
        'color': (255, 165, 0)  # Orange / Помаранчевий
    }
}

                                                      

def get_data(shape_name): # встановити дані за фигури shape_name
    shape_data = SHAPES[shape_name]
    return shape_data