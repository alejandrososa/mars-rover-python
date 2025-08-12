from enum import Enum

class Direction(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"

    def left(self):
        # Turn left (counterclockwise)
        order = [Direction.N, Direction.W, Direction.S, Direction.E]
        i = order.index(self)
        return order[(i + 1) % 4]

    def right(self):
        # Turn right (clockwise)
        order = [Direction.N, Direction.E, Direction.S, Direction.W]
        i = order.index(self)
        return order[(i + 1) % 4]