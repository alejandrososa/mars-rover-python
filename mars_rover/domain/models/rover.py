from dataclasses import dataclass
from mars_rover.domain.models.position import Position
from mars_rover.domain.models.direction import Direction

@dataclass
class Rover:
    pos: Position
    dir: Direction