import re
from enum import Enum

class Directions(Enum):
    right = 0
    left = 1
    up = 2
    down = 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError("CANNOT MOVE IN THIS DIRECTION")
    return f"moving {direction.name}"


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    print(move(Directions.diagonal))

    for direction in Directions:
        print(direction, direction.value, direction.name)
